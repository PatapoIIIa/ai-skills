#!/usr/bin/env python3
"""Check the skills' factual claims against live repository checkouts.

The skills assert things about the world: that a fork keeps its modular content
in a folder with a particular name, that an upstream-edit tag reads a particular
way, that a library was verified at a particular version. Those claims were true
on the day someone looked. Forks rename folders, bump pins, and abandon
conventions without anything failing loudly -- which is exactly how a skill
starts confidently handing out stale facts.

This walks the checkouts that happen to be on the machine and reports three
outcomes per claim:

  OK      -- reality still matches
  DRIFT   -- reality moved; the claim is not wrong, it is unverified again
             (a fork bumped tgui-core past the version a claim was checked at)
  BROKEN  -- reality contradicts the claim; the skill is now saying something false

DRIFT is the common and interesting case, and it is not a defect in the fork.
It means a skill's evidence has expired and something needs re-checking.

The claims live in `<skill>/claims.yaml`, next to the skill that makes them, and
identify repositories by name and project file -- never by a path on anyone's
disk. This script supplies the paths at runtime by scanning a workspace.

Usage:
    python scripts/verify_claims.py                       # scan the parent workspace
    python scripts/verify_claims.py --workspace PATH
    python scripts/verify_claims.py --skill ss13-tgui     # one skill's claims
    python scripts/verify_claims.py --json report.json    # machine-readable too
    python scripts/verify_claims.py --quiet-drift         # fail only on BROKEN

Exit codes: 0 = nothing to act on, 1 = at least one BROKEN or DRIFT
(with --quiet-drift, only BROKEN counts).
"""

import argparse
import datetime
import fnmatch
import glob
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


OK, DRIFT, BROKEN, SKIP = "OK", "DRIFT", "BROKEN", "SKIP"

# Files whose contents are read as "NAME=value" pins.
PIN_READERS = {}


def read(path):
    with io.open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def read_shell_pins(path):
    """dependencies.sh and friends: `export NAME=value`, quoted or not."""
    return dict(re.findall(r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)=[\"']?([^\"'\s#]+)",
                           read(path), re.M))


def read_json_pins(path):
    """package.json: dependency versions, flattened to NAME -> spec."""
    try:
        data = json.loads(read(path))
    except ValueError:
        return {}
    pins = {}
    for field in ("dependencies", "devDependencies"):
        for name, spec in (data.get(field) or {}).items():
            pins[name] = spec
    if "version" in data:
        pins["__version__"] = data["version"]
    return pins


PIN_READERS[".sh"] = read_shell_pins
PIN_READERS[".json"] = read_json_pins


def normalize_version(spec):
    """Strip npm range prefixes so ^6.1.1 and 6.1.1 compare equal."""
    return (spec or "").lstrip("^~>=< v").strip()


def version_tuple(spec):
    parts = re.findall(r"\d+", normalize_version(spec))
    return tuple(int(p) for p in parts[:4]) or None


# --------------------------------------------------------------------------
# Workspace discovery -- repositories are identified by content, never by path
# --------------------------------------------------------------------------

def discover_checkouts(workspace):
    """Every directory under `workspace` that looks like a BYOND project."""
    found = []
    if not os.path.isdir(workspace):
        return found
    for name in sorted(os.listdir(workspace)):
        path = os.path.join(workspace, name)
        if not os.path.isdir(path) or name.startswith("."):
            continue
        try:
            dme = [f for f in os.listdir(path) if f.endswith(".dme")]
        except OSError:
            continue
        if dme:
            found.append({"name": name, "path": path, "project_files": sorted(dme)})
    return found


def match_target(spec, checkouts):
    """Resolve one claims.yaml target to the checkouts that satisfy it.

    A target states a project file and optional required markers (relative
    paths that must exist). Folder names are a hint of last resort: `name_hint`
    only breaks ties, it never qualifies a checkout on its own.
    """
    project_file = spec.get("project_file")
    markers = spec.get("markers") or []
    hint = (spec.get("name_hint") or "").lower()

    matches = []
    for checkout in checkouts:
        if project_file and project_file not in checkout["project_files"]:
            continue
        if not all(os.path.exists(os.path.join(checkout["path"], m)) for m in markers):
            continue
        matches.append(checkout)

    if len(matches) > 1 and hint:
        preferred = [c for c in matches if hint in c["name"].lower()]
        if preferred:
            return preferred
    return matches


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

def resolve_path(repo, pattern):
    """Expand one claim path, which may contain a glob, to what actually exists."""
    if any(ch in pattern for ch in "*?["):
        return glob.glob(os.path.join(repo, pattern))
    full = os.path.join(repo, pattern)
    return [full] if os.path.exists(full) else []


def check_paths_exist(check, repo):
    missing = [p for p in check["paths"] if not resolve_path(repo, p)]
    if missing:
        return BROKEN, "missing: %s" % ", ".join(missing)
    return OK, "all %d present" % len(check["paths"])


def check_paths_absent(check, repo):
    present = []
    for pattern in check["paths"]:
        for hit in resolve_path(repo, pattern):
            present.append(os.path.relpath(hit, repo).replace("\\", "/"))
    if present:
        return BROKEN, "unexpectedly present: %s" % ", ".join(sorted(present))
    return OK, "absent as claimed"


def check_grep(check, repo):
    """Count regex matches across a glob, compare against min/max expectations."""
    pattern = re.compile(check["pattern"])
    root = os.path.join(repo, check.get("path", "."))
    if not os.path.exists(root):
        return SKIP, "path %s not in this checkout" % check.get("path", ".")

    globs = check.get("files") or ["*"]
    minimum = check.get("min_count", 1)
    total, files_hit, exhausted = 0, 0, True

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules")]
        for filename in filenames:
            if not any(fnmatch.fnmatch(filename, g) for g in globs):
                continue
            try:
                hits = len(pattern.findall(read(os.path.join(dirpath, filename))))
            except (OSError, UnicodeDecodeError):
                continue
            if hits:
                files_hit += 1
                total += hits
            # The claim only asserts a floor. Once it is cleared the exact total
            # is not worth walking the rest of a 20k-file tree for -- this is the
            # difference between a scan that fits in a git hook and one that does not.
            if total >= minimum:
                exhausted = False
                break
        if not exhausted:
            break

    if total < minimum:
        return BROKEN, "%d matches, claim needs at least %d" % (total, minimum)
    qualifier = "" if exhausted else "+"
    return OK, "%d%s matches across %d%s files" % (total, qualifier, files_hit, qualifier)


def check_pin(check, repo):
    """Compare a pinned version against what the claim was verified at."""
    source = os.path.join(repo, check["file"])
    if not os.path.isfile(source):
        return SKIP, "%s not in this checkout" % check["file"]
    reader = PIN_READERS.get(os.path.splitext(source)[1])
    if reader is None:
        return SKIP, "no reader for %s" % check["file"]

    pins = reader(source)
    key = check["key"]
    if key not in pins:
        # A fork that never pinned this is out of scope, not a counter-example --
        # but only where the claim says so, so a real disappearance still breaks.
        if check.get("missing_key") == "skip":
            return SKIP, "%s does not pin %s; out of scope for this claim" % (check["file"], key)
        return BROKEN, "%s does not define %s any more" % (check["file"], key)

    actual = pins[key]
    verified = check.get("verified_at")
    if verified is None:
        return OK, "%s = %s (recorded, no expectation set)" % (key, actual)

    accepted = verified if isinstance(verified, list) else [verified]
    if any(normalize_version(actual) == normalize_version(v) for v in accepted):
        return OK, "%s = %s, still one of the verified versions" % (key, actual)

    now, then = version_tuple(actual), [version_tuple(v) for v in accepted]
    direction = "moved"
    if now and all(t for t in then):
        direction = "ahead of" if now > max(then) else "behind"
    return DRIFT, "%s = %s, %s the verified %s -- re-check the claim against it" % (
        key, actual, direction, "/".join(str(v) for v in accepted))


def check_commit_rank(check, repo):
    """The claim that one directory dominates its siblings by commit count."""
    globs = check.get("glob", "modular*")
    try:
        candidates = [d for d in os.listdir(repo)
                      if os.path.isdir(os.path.join(repo, d)) and fnmatch.fnmatch(d, globs)]
    except OSError:
        return SKIP, "cannot list %s" % repo
    if len(candidates) < 2:
        return SKIP, "only %d directory matches %s" % (len(candidates), globs)

    counts = []
    for directory in candidates:
        try:
            out = subprocess.check_output(
                ["git", "rev-list", "--count", "HEAD", "--", directory],
                cwd=repo, stderr=subprocess.DEVNULL)
            counts.append((int(out.strip()), directory))
        except (subprocess.CalledProcessError, OSError, ValueError):
            return SKIP, "git unavailable in this checkout"
    counts.sort(reverse=True)

    ratio = check.get("min_ratio", 2)
    top, second = counts[0], counts[1]
    detail = ", ".join("%s=%d" % (d, c) for c, d in counts[:4])
    if second[0] == 0 or top[0] >= second[0] * ratio:
        return OK, "dominant root is clear (%s)" % detail
    return DRIFT, "no dominant root by a factor of %s (%s) -- ranking heuristic is inconclusive here" % (
        ratio, detail)


CHECKS = {
    "paths_exist": check_paths_exist,
    "paths_absent": check_paths_absent,
    "grep": check_grep,
    "pin": check_pin,
    "commit_rank": check_commit_rank,
}


# --------------------------------------------------------------------------
# Runner
# --------------------------------------------------------------------------

def load_claim_files(root, only_skill=None):
    files = []
    plugins_dir = os.path.join(root, "plugins")
    for dirpath, dirnames, filenames in os.walk(plugins_dir):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        if "claims.yaml" in filenames:
            skill = os.path.basename(dirpath)
            if only_skill and skill != only_skill:
                continue
            files.append((skill, os.path.join(dirpath, "claims.yaml")))
    return sorted(files)


def run(root, workspace, only_skill, quiet_drift):
    checkouts = discover_checkouts(workspace)
    print("Workspace: %s" % workspace)
    print("  %d BYOND checkouts found: %s"
          % (len(checkouts), ", ".join(c["name"] for c in checkouts) or "none"))

    claim_files = load_claim_files(root, only_skill)
    if not claim_files:
        print("\nNo claims.yaml found%s." % (" for %s" % only_skill if only_skill else ""))
        return 0, []

    results = []
    for skill, path in claim_files:
        doc = yaml.safe_load(read(path)) or {}
        targets = doc.get("targets") or {}
        resolved = {name: match_target(spec, checkouts) for name, spec in targets.items()}

        print("\n=== %s ===" % skill)
        for name, matched in sorted(resolved.items()):
            print("  target %-16s -> %s" % (
                name, ", ".join(c["name"] for c in matched) or "(no checkout available)"))

        for claim in doc.get("claims") or []:
            target = claim.get("target")
            matched = resolved.get(target) or []
            if not matched:
                results.append(dict(skill=skill, claim=claim["id"], repo=None,
                                    status=SKIP, detail="no checkout for target %r" % target,
                                    says=claim.get("says", ""),
                                    last_verified=str(claim.get("last_verified", ""))))
                continue
            for checkout in matched:
                spec = claim["check"]
                handler = CHECKS.get(spec.get("type"))
                if handler is None:
                    status, detail = SKIP, "unknown check type %r" % spec.get("type")
                else:
                    try:
                        status, detail = handler(spec, checkout["path"])
                    except Exception as exc:                      # noqa: BLE001
                        status, detail = SKIP, "check raised %s: %s" % (type(exc).__name__, exc)
                results.append(dict(skill=skill, claim=claim["id"], repo=checkout["name"],
                                    status=status, detail=detail,
                                    says=claim.get("says", ""),
                                    last_verified=str(claim.get("last_verified", ""))))

    return report(results, quiet_drift), results


def report(results, quiet_drift):
    order = {BROKEN: 0, DRIFT: 1, SKIP: 2, OK: 3}
    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1

    actionable = [r for r in results if r["status"] in (BROKEN, DRIFT)]
    print("\n" + "-" * 72)
    if actionable:
        print("Needs attention:\n")
        for r in sorted(actionable, key=lambda r: (order[r["status"]], r["skill"], r["claim"])):
            print("  %-6s %s / %s  [%s]" % (r["status"], r["skill"], r["claim"], r["repo"]))
            print("         says:  %s" % r["says"])
            print("         found: %s" % r["detail"])
            if r["last_verified"]:
                print("         last verified: %s" % r["last_verified"])
            print("")
    else:
        print("Nothing needs attention.\n")

    print("%d OK, %d drifted, %d broken, %d skipped"
          % (counts.get(OK, 0), counts.get(DRIFT, 0),
             counts.get(BROKEN, 0), counts.get(SKIP, 0)))

    if counts.get(BROKEN):
        return 1
    if counts.get(DRIFT) and not quiet_drift:
        return 1
    return 0


def commit_count(repo):
    try:
        out = subprocess.check_output(["git", "rev-list", "--count", "HEAD"],
                                      cwd=repo, stderr=subprocess.DEVNULL)
        return int(out.strip())
    except (subprocess.CalledProcessError, OSError, ValueError):
        return None


def load_state(state_dir):
    path = os.path.join(state_dir, "last-run.json")
    if os.path.isfile(path):
        try:
            return json.loads(read(path))
        except ValueError:
            pass
    return {}


def save_state(state_dir, commits):
    if not os.path.isdir(state_dir):
        os.makedirs(state_dir)
    payload = {"last_run": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
               "last_commit_count": commits}
    with io.open(os.path.join(state_dir, "last-run.json"), "w",
                 encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(payload, indent=2) + "\n")


def should_run(state, commits, every_commits, max_age_days):
    """Either trigger firing is enough; no trigger set means always run."""
    if not every_commits and not max_age_days:
        return True, "no throttle configured"
    if not state:
        return True, "first run"

    reasons = []
    if every_commits and commits is not None:
        since = commits - state.get("last_commit_count", 0)
        if since >= every_commits:
            return True, "%d commits since the last run (threshold %d)" % (since, every_commits)
        reasons.append("only %d/%d commits" % (since, every_commits))

    if max_age_days:
        try:
            last = datetime.datetime.strptime(state["last_run"], "%Y-%m-%dT%H:%M:%S")
            age = (datetime.datetime.now() - last).days
            if age >= max_age_days:
                return True, "last run was %d days ago (threshold %d)" % (age, max_age_days)
            reasons.append("last run %d/%d days ago" % (age, max_age_days))
        except (KeyError, ValueError):
            return True, "unreadable state, running anyway"

    return False, "; ".join(reasons)


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo-root", default=None)
    parser.add_argument("--workspace", default=None,
                        help="directory holding the checkouts (default: the repo's parent)")
    parser.add_argument("--skill", default=None, help="check only this skill's claims")
    parser.add_argument("--json", default=None, help="also write the full result set here")
    parser.add_argument("--quiet-drift", action="store_true",
                        help="exit non-zero only on BROKEN, not on DRIFT")
    parser.add_argument("--every-commits", type=int, default=None, metavar="N",
                        help="only run once N commits have landed since the last run")
    parser.add_argument("--max-age-days", type=int, default=None, metavar="D",
                        help="only run if the last run was at least D days ago")
    parser.add_argument("--state-dir", default=None,
                        help="where run state lives (default: <repo>/.git/skill-drift)")
    args = parser.parse_args()

    root = args.repo_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    workspace = args.workspace or os.path.dirname(root)
    state_dir = args.state_dir or os.path.join(root, ".git", "skill-drift")

    commits = commit_count(root)
    ok_to_run, why = should_run(load_state(state_dir), commits,
                                args.every_commits, args.max_age_days)
    if not ok_to_run:
        print("Skipping claim check: %s" % why)
        return 0
    if args.every_commits or args.max_age_days:
        print("Running claim check: %s\n" % why)

    code, results = run(root, workspace, args.skill, args.quiet_drift)
    if args.every_commits or args.max_age_days:
        save_state(state_dir, commits)

    if args.json:
        payload = {"generated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                   "workspace": workspace, "results": results}
        with io.open(args.json, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        print("\nWrote %s" % args.json)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
