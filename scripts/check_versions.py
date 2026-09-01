#!/usr/bin/env python3
"""Watch package and toolchain versions in the upstream repositories the skills describe.

The skills quote versions: "verified present in tgui-core 5.6.0", "built rust-g
6.1.0", "needed BYOND 516.1661". Those are the claims that expire silently --
upstream bumps a pin and the skill keeps asserting behaviour it read against an
older release.

This reads a handful of named files straight from the canonical upstreams over
HTTPS, extracts the pins, and diffs them against a committed baseline. Because
the baseline is tracked in git, `git log -p scripts/version_baseline.json`
becomes a history of when each project moved.

Why not read the local clones: they lie. Measured 2026-09-01, the tgstation
working tree on this machine was 1039 commits behind its own origin/master and
still said BYOND_MINOR=1659 while upstream said 1685. A downstream fork lags
further still -- reading one to check a claim about its upstream produced a
false alarm against ss13-tgs-deploy, whose numbers turned out to match
Monkestation/Vanderlin exactly.

Usage:
    python scripts/check_versions.py                 # report what moved
    python scripts/check_versions.py --update        # accept current as the new baseline
    python scripts/check_versions.py --offline-ok    # network failure is not an error

Exit codes: 0 = nothing moved, 1 = something moved or a fetch failed
(with --offline-ok, fetch failures alone do not fail the run).
"""

import argparse
import datetime
import io
import json
import os
import re
import subprocess
import sys

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML is required: pip install pyyaml\n")
    raise SystemExit(2)

try:
    from urllib.request import urlopen, Request
    from urllib.error import URLError, HTTPError
except ImportError:                                        # pragma: no cover
    sys.stderr.write("Python 3 is required\n")
    raise SystemExit(2)


SAME, MOVED, NEW, GONE, ERROR = "SAME", "MOVED", "NEW", "GONE", "ERROR"

SHELL_PIN_RE = re.compile(
    r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)=[\"']?([^\"'\s#]+)", re.M)


def read(path):
    with io.open(path, encoding="utf-8") as fh:
        return fh.read()


def normalize(spec):
    """Strip npm range prefixes so ^6.1.1 and 6.1.1 compare equal."""
    return (spec or "").lstrip("^~>=< v").strip()


def fetch_urllib(url, timeout):
    request = Request(url, headers={"User-Agent": "ss13-ai-skills-version-watch"})
    with urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", "replace")


def fetch_curl(url, timeout):
    """Fallback transport with its own trust store.

    Python's OpenSSL and curl do not always agree about a certificate chain. On
    a machine behind an intercepting proxy, urllib refused every request here
    ("Basic Constraints of CA cert not marked critical") while curl accepted the
    same chain. curl still verifies -- this is a different trust store, not a
    weaker check. Verification is never disabled; if both transports refuse, the
    run reports the failure rather than working around it.
    """
    result = subprocess.run(
        ["curl", "-sS", "--fail", "--max-time", str(timeout),
         "-H", "User-Agent: ss13-ai-skills-version-watch", url],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise OSError(result.stderr.decode("utf-8", "replace").strip() or
                      "curl exited %d" % result.returncode)
    return result.stdout.decode("utf-8", "replace")


def fetch(url, timeout, transport):
    """Return (text, transport_used). `transport` records what worked last."""
    if transport["name"] == "curl":
        return fetch_curl(url, timeout), "curl"
    try:
        return fetch_urllib(url, timeout), "urllib"
    except HTTPError:
        raise
    except (URLError, OSError) as exc:
        if not _is_tls_trust_error(exc) or not _have_curl():
            raise
        text = fetch_curl(url, timeout)
        transport["name"] = "curl"          # stop retrying urllib for every file
        return text, "curl"


def _is_tls_trust_error(exc):
    return "CERTIFICATE_VERIFY_FAILED" in str(exc) or "SSL" in str(exc)


def _have_curl():
    try:
        subprocess.run(["curl", "--version"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (OSError, subprocess.SubprocessError):
        return False


def parse_shell(text):
    return dict(SHELL_PIN_RE.findall(text))


def parse_npm(text):
    try:
        data = json.loads(text)
    except ValueError:
        return {}
    pins = {}
    for field in ("dependencies", "devDependencies"):
        for name, spec in (data.get(field) or {}).items():
            pins[name] = spec
    return pins


PARSERS = {"shell": parse_shell, "npm": parse_npm}


def collect(config, offline_ok):
    """Read every watched file from every watched repo. Returns observations + errors."""
    base = config["fetch"]["base_url"].rstrip("/")
    timeout = config["fetch"].get("timeout_seconds", 20)

    observed, errors = {}, []
    transport = {"name": "urllib"}
    for repo in config["repos"]:
        repo_id = repo["id"]
        observed[repo_id] = {}
        for spec in config["files"]:
            url = "%s/%s/%s/%s" % (base, repo["owner_repo"], repo["branch"], spec["path"])
            try:
                text, _used = fetch(url, timeout, transport)
            except HTTPError as exc:
                # A 404 is information: the file is genuinely not in that repo.
                errors.append((repo_id, spec["path"], "HTTP %s" % exc.code))
                continue
            except (URLError, OSError) as exc:
                errors.append((repo_id, spec["path"], "unreachable (%s)" % exc))
                continue

            pins = PARSERS[spec["format"]](text)
            for key in spec["keys"]:
                if key in pins:
                    observed[repo_id][key] = pins[key]
    return observed, errors, transport["name"]


def compare(observed, baseline, watched_repos):
    """Diff observations against the recorded baseline, per repo and key."""
    rows = []
    for repo_id in watched_repos:
        now = observed.get(repo_id, {})
        before = (baseline.get("repos") or {}).get(repo_id, {})

        # A repo we could not read at all this run has nothing to say; leaving
        # its baseline alone is better than reporting every key as GONE.
        if not now and before:
            continue

        for key in sorted(set(now) | set(before)):
            new, old = now.get(key), before.get(key)
            if old is None:
                rows.append((repo_id, key, NEW, old, new))
            elif new is None:
                rows.append((repo_id, key, GONE, old, new))
            elif normalize(new) != normalize(old):
                rows.append((repo_id, key, MOVED, old, new))
            else:
                rows.append((repo_id, key, SAME, old, new))
    return rows


def claim_note(config, repo_id, key, new_value):
    """If a moved key backs a skill claim, say which claim now needs re-reading."""
    link = (config.get("claim_links") or {}).get(key)
    if not link:
        return None
    scope = link.get("scope_repo")
    if scope and scope != repo_id:
        return None
    verified = [normalize(v) for v in link.get("verified_at", [])]
    if normalize(new_value) in verified:
        return None
    return "%s / %s was verified at %s -- re-read it against %s" % (
        link["skill"], link["claim"], "/".join(link.get("verified_at", [])), new_value)


def report(config, rows, errors, offline_ok):
    moved = [r for r in rows if r[2] in (MOVED, NEW, GONE)]

    print("\nCurrent pins")
    print("-" * 72)
    repos = {r["id"]: r for r in config["repos"]}
    for repo_id in repos:
        keys = [r for r in rows if r[0] == repo_id and r[4] is not None]
        if not keys:
            continue
        print("  %s (%s)" % (repo_id, repos[repo_id]["owner_repo"]))
        for _repo, key, status, _old, new in sorted(keys, key=lambda r: r[1]):
            flag = " <-- %s" % status if status != SAME else ""
            print("      %-24s %s%s" % (key, new, flag))
        print("")

    if moved:
        print("Changed since the baseline")
        print("-" * 72)
        for repo_id, key, status, old, new in moved:
            if status == MOVED:
                print("  MOVED  %s / %s: %s -> %s" % (repo_id, key, old, new))
            elif status == NEW:
                print("  NEW    %s / %s: %s" % (repo_id, key, new))
            else:
                print("  GONE   %s / %s: was %s, no longer defined" % (repo_id, key, old))
            note = claim_note(config, repo_id, key, new)
            if note:
                print("         %s" % note)
        print("")
    else:
        print("Nothing moved since the baseline.\n")

    if errors:
        print("Could not read")
        print("-" * 72)
        for repo_id, path, why in errors:
            print("  %s / %s: %s" % (repo_id, path, why))
        print("")

    code = 0
    if moved:
        code = 1
    if errors and not offline_ok:
        code = 1
    return code


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--config", default=None)
    parser.add_argument("--baseline", default=None)
    parser.add_argument("--update", action="store_true",
                        help="record what was observed as the new baseline")
    parser.add_argument("--offline-ok", action="store_true",
                        help="do not fail the run when a repo cannot be reached")
    args = parser.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    config_path = args.config or os.path.join(here, "version_watch.yaml")
    baseline_path = args.baseline or os.path.join(here, "version_baseline.json")

    config = yaml.safe_load(read(config_path))
    baseline = {}
    if os.path.isfile(baseline_path):
        try:
            baseline = json.loads(read(baseline_path))
        except ValueError:
            print("Baseline is unreadable; treating every pin as new.")

    watched = [r["id"] for r in config["repos"]]
    print("Reading %d files from %d upstream repositories over HTTPS"
          % (len(config["files"]), len(watched)))

    observed, errors, transport = collect(config, args.offline_ok)
    if transport != "urllib":
        print("  (transport: %s -- Python's TLS trust store rejected the chain)" % transport)
    rows = compare(observed, baseline, watched)
    code = report(config, rows, errors, args.offline_ok)

    if args.update:
        # Never let a failed fetch erase a repo's recorded pins.
        merged = dict((baseline.get("repos") or {}))
        for repo_id, pins in observed.items():
            if pins:
                merged[repo_id] = pins
        payload = {
            "generated": datetime.datetime.now().strftime("%Y-%m-%d"),
            "note": "Written by scripts/check_versions.py --update. "
                    "Committed on purpose: its git history is the record of when "
                    "each upstream moved a pin.",
            "repos": merged,
        }
        with io.open(baseline_path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        print("Baseline updated: %s" % os.path.basename(baseline_path))
        return 0

    return code


if __name__ == "__main__":
    raise SystemExit(main())
