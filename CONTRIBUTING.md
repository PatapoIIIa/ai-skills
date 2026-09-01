# Contributing

This repository ships knowledge, not code. A change here is accepted on whether
its claims are **true and checkable**, not on whether it reads well — so most of
what follows is about evidence rather than style.

`CLAUDE.md` is the full maintainer brief; `AGENTS.md` is the short version for
coding agents. Read one of them before a non-trivial change.

## Run these before opening anything

```bash
python scripts/validate_ecosystem.py
```
```bash
claude plugin validate ./plugins/ss13-byond && claude plugin validate .
```

The first exits non-zero on error and is the one that catches real damage:
broken links, orphaned reference files, over-long descriptions, missing EN+RU
eval pairs, machine paths, CRLF, and the cross-file touches listed below. The
manifest warning about a missing `version` is **intentional** — see below.

Optional, network-dependent, non-gating:

```bash
python scripts/check_versions.py      # upstream pins the skills quote
python scripts/verify_claims.py       # skill claims vs. local checkouts
python scripts/run_evals.py --dry-run # eval files parse; expectations resolve
```

## The rules that get changes rejected

**Every engine or fork claim needs a source, and the source decides its tag.**
A tier-1 BYOND fact needs the official DM Reference; a tg convention needs a
grep against a live checkout. Tags are `[DM Ref]`, `[tg]`, `[dev]`,
`[community]`, `[heuristic]`, `[measure]`. Something plausible and unverified is
tagged as such or left out — it is never promoted to fact. Record what was
checked in the skill's `source-index.md` / `source-corpus.md`.

**Never a real person's handle or nickname.** Sources are credited by *role*,
never identity — in skills, docs, commit messages and notes alike.

**Never a machine-specific path or a username** — in skills *or* semantic bases,
because the whole repo is public. Identify a repository by name and project file
(`Twilight-Axis`, `roguetown.dme`), never by where it sits on a disk. Grep the
tree for `C:\`, `C:/`, `/home/`, `/Users/` before finishing.

**Routing lives in exactly one place** — the controller's dispatch gates. Every
other skill states only its own boundary. A skill that restates the interaction
matrix is drift: delete the copy rather than fork the logic.

**Example prompts come in EN + RU pairs.** Evals, docs and skill examples all
follow this; a single-language example is an incomplete one.

**Don't claim something ran unless it ran.** "Validated the manifest" and
"loaded the plugin in a session" are different claims. This binds contributions
exactly as it binds the skills themselves.

## Adding or removing a skill touches six places

Miss one and the ecosystem contradicts itself; `validate_ecosystem.py` enforces
touches 2–6 mechanically. The list, in order, is in `CLAUDE.md` → *Adding or
removing a skill is a 6-touch change*. Touch #1 — whether the SKILL.md body is
any good — is the only one no script has an opinion about.

## Versioning

There is none, deliberately. `plugin.json` omits `version`, which makes the git
SHA the version, so subscribers track the default branch's latest commit with no
manual bumps. `claude plugin validate` warns about this; **do not "fix" it by
pinning a version** — that would silently freeze every existing subscriber.
Notable changes go in `CHANGELOG.md`, dated rather than numbered.

## Semantic bases

The `ai_navigation_*` directories are fork-specific **data**, not skills, and sit
outside the plugin so subscribers never receive them. They are regenerable
("cattle, not pets"): when one drifts, prefer regenerating it from
`references/file-specs.md` over patching. All of them are currently stale and
say so in their own banners.
