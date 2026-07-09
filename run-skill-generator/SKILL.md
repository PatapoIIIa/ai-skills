---
name: "run-skill-generator"
description: "Top-level controller for an SS13/BYOND skill ecosystem: defines how architecture-knowledge skills (ss13-tgui, tgstation-modular-content, and future ones) interact with each other, and when to hand off to the semantic-controller skill that discovers, creates, and maintains per-repository semantic bases (ai_navigation folders). Use at the start of any non-trivial task in an SS13/BYOND fork; whenever the user mentions семантика/семантический анализ репозитория, семантическая база, ai_navigation, navigation layer, восстановить инфраструктуру, новая кодовая база, skill ecosystem; whenever it is unclear which skill applies; and whenever two architecture skills could both apply and their interaction order matters."
---

# Run Skill Generator — ecosystem controller

This bundle is self-sufficient: it assumes **nothing** about the machine it runs on. No pre-existing bases, no fixed folder layout, no absolute paths. Given only the installed skills and a codebase — even one never seen before — the system builds its own working infrastructure: architecture skills carry the invariants, the semantic controller discovers or rebuilds the repo's factual layer, and work proceeds.

## The four layers

| # | Layer | Role | How to locate |
|---|---|---|---|
| 1 | **Controller** (this skill) | Interaction contract between architecture skills; hands base work to layer 3 | installed skill |
| 2 | **Architecture skills** | The deepest, fork-invariant design patterns and anti-patterns | installed skills, referenced **by name**: `ss13-tgui`, `tgstation-modular-content` |
| 3 | **Semantic controller** | Binds layer 2 to layer 4; discovers existing bases, **creates** them when absent, controls their integrity | installed skill: `semantic-controller` |
| 4 | **Semantic bases** | Factual current state of one fork (`ai_navigation/` folders); regenerable data, never authoritative over code | discovered on disk by the semantic controller (see its Discovery protocol) — never hardcoded |

Truth hierarchy across layers: **repo code > semantic base (fork facts) > architecture skill (fork-specific claims)** — but an architecture skill always wins on framework invariants and anti-patterns. A base recommending an anti-pattern is a broken base.

If a referenced skill is not installed, degrade gracefully: state which skill is missing, continue from the layers that are present, and do not guess its content from memory.

## How architecture skills interact

Each architecture skill has an activation guard — respect it; do not stretch a skill past its domain.

| Situation | Contract |
|---|---|
| Task is pure UI/webview (tgui files, ui_* procs, ByondUi, blank windows) | `ss13-tgui` alone |
| Task is fork content that must survive upstream sync | `tgstation-modular-content` alone |
| Modular tgui interface (both apply) | `tgstation-modular-content` decides **placement and file layout** (overlay dir, include wiring, edit markers); `ss13-tgui` decides **implementation** (lifecycle, data flow, components). Placement constraints outrank implementation convenience — a correct UI in the wrong layer is a merge conflict later |
| Skills appear to disagree | They own different axes (mergeability vs framework correctness); a real clash means one is applied outside its guard — re-check the guards |
| Task reveals knowledge neither skill has | Route the fact to the right layer: invariant everywhere → the architecture skill (enrichment intake); true only in this fork → the semantic base, via the semantic controller |

New architecture skills join this table with: name, domain guard, and interaction rules against the existing ones.

## When to hand off to the semantic controller

Open the `semantic-controller` skill for anything touching layers 3-4:

- a coding task inside a fork (it discovers the repo's base, checks its identity and freshness, and produces the binding brief);
- **a new codebase appears** — it assesses the repo and bootstraps a base from zero;
- the repo's family is unknown or not SS13 at all — its Stage 0 assessment decides which layers even have equivalents; architecture skills stay out of domains the repo lacks;
- a base looks stale, contradicts code, or fails validation — it owns integrity control;
- creating, registering, or syncing bases and the workspace registry.

## Cold start (fresh machine, zero infrastructure)

1. Install the three-skill bundle (this skill, `semantic-controller`) plus the architecture skills.
2. Point a session at any SS13/BYOND repo and start a task — no other setup.
3. The semantic controller's discovery finds a base if the repo ships one (`<repo>/ai_navigation/`); otherwise it works from source and offers to bootstrap a base from its file specs.
4. The first bootstrap also creates the workspace registry (a local **data** file owned by the user's machine, not by any skill) — from then on, multi-repo dispatch is data-driven.

Keep that property when editing this bundle: machine state (which repos exist, where bases live, what drifted) belongs in the workspace registry and the bases themselves — **never** in these skills. Never write an absolute path into a skill.
