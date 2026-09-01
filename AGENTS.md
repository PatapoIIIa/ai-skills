# AGENTS.md — ai-skills

Entry point for any coding agent working **on this repository**. If you are an
agent that was pointed at an SS13 fork and merely *uses* these skills, you want
the skills themselves, not this file.

`CLAUDE.md` in this directory is the full maintainer brief — module map, the
6-touch rule for adding a skill, the version watch, the claim-drift workflow,
and the footguns. This file is the short version plus the cross-platform notes,
kept separate because `AGENTS.md` is the convention several non-Claude agents
read and `CLAUDE.md` is not.

## What this repo is

A **Claude Code plugin and marketplace** shipping five skills for SS13 / BYOND
work. Markdown specs, JSON manifests, a few Python helpers. There is no build
and no compiler — "does it compile" is not a question this repo can answer
about itself.

- Marketplace: `.claude-plugin/marketplace.json` (`ss13-ai-skills`)
- Plugin: `plugins/ss13-byond/` (`ss13-byond`), skills under `skills/`
- `ai_navigation_*/` at the root are **fork data, not skills**, deliberately
  outside the plugin so subscribers never receive them.

## Before you change anything

Read `CLAUDE.md`. The two rules most often broken by an agent that skips it:

1. **Routing lives in exactly one place** — the controller's dispatch gates.
   Every other skill states only its own boundary. A skill that restates the
   interaction matrix is drift; delete the copy rather than fork the logic.
2. **Nothing machine-specific, ever** — no absolute paths, no usernames, in
   skills *or* semantic bases, because the whole repo is public. Identify a
   repository by name and project file, never by where it sits on a disk.

## Checks

Run all three before finishing. The first is the one that catches real damage.

```
python scripts/validate_ecosystem.py     # repo self-consistency; exits non-zero on error
claude plugin validate ./plugins/ss13-byond
claude plugin validate .
```

Two more, both needing network, neither gating:

```
python scripts/check_versions.py         # upstream pins the skills quote
python scripts/verify_claims.py          # skill claims vs. checkouts on this machine
python scripts/run_evals.py --dry-run    # eval files parse and their expectations resolve
```

`run_evals.py` without `--dry-run` calls the `claude` CLI and needs an
authenticated shell — a nested or agent-run shell usually has none, and will
stop with "Not logged in" rather than pretend.

## Cross-platform surface

Each skill ships `agents/openai.yaml` (display name, short description, a
default prompt) so non-Claude hosts can present it. When you add or rename a
skill, that file is part of the change — the skill's own body is portable
Markdown and needs no per-host variant.

Skills are namespaced `ss13-byond:<name>` under Claude Code. Elsewhere they are
plain directories: point the host at `plugins/ss13-byond/skills/<name>/` and it
gets `SKILL.md` plus that skill's `references/`.

## Honesty

The skills forbid claiming that code compiled, ran, or passed unless the
command executed and its output was seen. That rule binds work *on* the skills
too: "validated the manifest" and "loaded the plugin in a session" are
different claims, and only one of them is cheap.
