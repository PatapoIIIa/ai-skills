#!/usr/bin/env python3
"""Execute the eval sets that ship with each skill.

The repo carries 46 evals across five skills. Until this script existed none of
them had ever been run: they were files asserting that routing works, with
nothing checking that claim. `validate_ecosystem.py` verifies the repo agrees
with itself and `verify_claims.py` verifies the skills agree with reality --
this one verifies the *model* does what the skills say it will.

Two modes, and the cheap one is the point:

  routing (default)  Ask which skills the model would load for the prompt, and
                     nothing else. This tests the controller's dispatch gates,
                     which are the ecosystem's core claim, at roughly one short
                     answer per eval.
  full               Actually run the prompt and save the transcript for review.
                     Expensive, and grading is left to a human or a judge model;
                     use it on a handful of evals, not the whole set.

Expected routing comes from two optional fields on an eval entry:

    "expect_skills": ["byond-ss13-coding"],
    "forbid_skills": ["ss13-tgui", "tgstation-modular-content"]

When `expect_skills` is absent the owning skill is assumed -- an eval that ships
inside `ss13-tgui/evals/` should route to `ss13-tgui`. `forbid_skills` is how
the dispatch gates get tested negatively, which is the half that actually
catches over-triggering: a router that loads everything always "passes" a purely
positive check.

Usage:
  python scripts/run_evals.py --dry-run        # no model calls; validate + show the plan
  python scripts/run_evals.py                  # routing mode over every skill
  python scripts/run_evals.py --skill ss13-tgui
  python scripts/run_evals.py --mode full --limit 3

Exit code 0 = every eval passed (or dry run was clean), 1 = failures.

NOTE: this shells out to the `claude` CLI, which must be authenticated in the
shell you run it from. A non-interactive/nested shell often is not -- if you see
"Not logged in", run it from your own terminal rather than from an agent
session.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SKILLS = os.path.join(ROOT, "plugins", "ss13-byond", "skills")
PLUGIN_DIR = os.path.join(ROOT, "plugins", "ss13-byond")

ROUTING_SUFFIX = (
    "\n\n---\n"
    "Do NOT perform the task above and do not ask clarifying questions. "
    "Name only the skills you would load to handle it, one per line, with no other text. "
    "If you would load none, reply exactly: NONE"
)


def load_evals(only_skill=None):
    """Return [(skill_name, eval_dict), ...] for every eval file present."""
    out = []
    if not os.path.isdir(SKILLS):
        sys.exit("skills directory not found: %s" % SKILLS)
    for name in sorted(os.listdir(SKILLS)):
        if only_skill and name != only_skill:
            continue
        path = os.path.join(SKILLS, name, "evals", "evals.json")
        if not os.path.isfile(path):
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, ValueError) as exc:
            sys.exit("%s: unreadable evals.json (%s)" % (name, exc))
        for entry in data.get("evals") or []:
            out.append((name, entry))
    return out


def known_skills():
    return sorted(
        n for n in os.listdir(SKILLS)
        if os.path.isfile(os.path.join(SKILLS, n, "SKILL.md"))
    )


def expectations(skill, entry, valid):
    """Resolve expected/forbidden skills, defaulting expectation to the owner."""
    expect = entry.get("expect_skills") or [skill]
    forbid = entry.get("forbid_skills") or []
    bad = [s for s in list(expect) + list(forbid) if s not in valid]
    return expect, forbid, bad


def run_claude(prompt, timeout, extra_args=None):
    cmd = ["claude", "--plugin-dir", PLUGIN_DIR, "-p", prompt]
    if extra_args:
        cmd[1:1] = extra_args
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout,
            encoding="utf-8", errors="replace",
        )
    except FileNotFoundError:
        sys.exit("the `claude` CLI was not found on PATH")
    except subprocess.TimeoutExpired:
        return None, "timed out after %ss" % timeout
    body = (proc.stdout or "").strip()
    if "Not logged in" in body or "Not logged in" in (proc.stderr or ""):
        sys.exit(
            "the `claude` CLI is not authenticated in this shell.\n"
            "Run this script from your own terminal (a nested/agent shell "
            "usually has no session)."
        )
    if proc.returncode != 0 and not body:
        return None, (proc.stderr or "").strip()[:300] or "exit %d" % proc.returncode
    return body, None


def named_skills(text, valid):
    """Which known skill names appear in the reply."""
    found = set()
    for s in valid:
        # match the bare name or the plugin-namespaced form
        if re.search(r"(?<![\w-])(?:ss13-byond:)?%s(?![\w-])" % re.escape(s), text):
            found.add(s)
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", help="run only this skill's evals")
    ap.add_argument("--mode", choices=("routing", "full"), default="routing")
    ap.add_argument("--dry-run", action="store_true",
                    help="validate the eval files and print the plan; no model calls")
    ap.add_argument("--limit", type=int, help="stop after N evals")
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--out", help="write a JSON report here")
    args = ap.parse_args()

    valid = known_skills()
    evals = load_evals(args.skill)
    if not evals:
        sys.exit("no evals found" + (" for %s" % args.skill if args.skill else ""))
    if args.limit:
        evals = evals[:args.limit]

    # Validate before spending anything.
    problems = []
    for skill, entry in evals:
        _, _, bad = expectations(skill, entry, valid)
        if bad:
            problems.append("%s eval %s names unknown skill(s): %s"
                            % (skill, entry.get("id"), ", ".join(bad)))
        if not entry.get("prompt"):
            problems.append("%s eval %s has no prompt" % (skill, entry.get("id")))
    if problems:
        for p in problems:
            print("ERROR  %s" % p)
        return 1

    print("%d evals across %d skill(s); mode=%s%s"
          % (len(evals), len({s for s, _ in evals}), args.mode,
             "  [DRY RUN]" if args.dry_run else ""))

    if args.dry_run:
        for skill, entry in evals:
            expect, forbid, _ = expectations(skill, entry, valid)
            lang = entry.get("lang", "--")
            print("  %-28s #%-3s %s  expect=%s%s"
                  % (skill, entry.get("id"), lang, ",".join(expect),
                     "  forbid=" + ",".join(forbid) if forbid else ""))
        print("\nDry run clean. Drop --dry-run to execute (needs an authenticated `claude`).")
        return 0

    results, failures = [], 0
    for i, (skill, entry) in enumerate(evals, 1):
        expect, forbid, _ = expectations(skill, entry, valid)
        prompt = entry["prompt"]
        if args.mode == "routing":
            prompt += ROUTING_SUFFIX

        started = time.time()
        reply, err = run_claude(prompt, args.timeout)
        elapsed = round(time.time() - started, 1)

        rec = {"skill": skill, "id": entry.get("id"), "lang": entry.get("lang"),
               "expect": expect, "forbid": forbid, "seconds": elapsed,
               "reply": reply, "error": err}

        if err:
            verdict, detail = "ERROR", err
        elif args.mode == "full":
            verdict, detail = "SAVED", "%d chars" % len(reply or "")
        else:
            got = named_skills(reply or "", valid)
            missing = [s for s in expect if s not in got]
            leaked = [s for s in forbid if s in got]
            if missing or leaked:
                verdict = "FAIL"
                bits = []
                if missing:
                    bits.append("missing " + ",".join(missing))
                if leaked:
                    bits.append("over-triggered " + ",".join(leaked))
                detail = "; ".join(bits)
            else:
                verdict, detail = "PASS", ",".join(sorted(got)) or "none"
        rec["verdict"] = verdict
        rec["detail"] = detail
        results.append(rec)
        if verdict in ("FAIL", "ERROR"):
            failures += 1
        print("[%d/%d] %-6s %-28s #%-3s %-3s %5ss  %s"
              % (i, len(evals), verdict, skill, entry.get("id"),
                 entry.get("lang", "--"), elapsed, detail))

    passed = sum(1 for r in results if r["verdict"] == "PASS")
    print("\n%d passed, %d failed/errored, %d total"
          % (passed, failures, len(results)))

    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
            json.dump({"mode": args.mode, "results": results}, fh,
                      indent=2, ensure_ascii=False)
        print("report: %s" % args.out)

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
