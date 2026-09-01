# Repository Agent Guide

> **STALE — audited 2026-09-01.** Generated 2026-07-09; the target repo has moved on (last commit 2026-08-23). Structurally this base is the healthiest of the three: **0 broken path references**, and its load-bearing entry-proc claim re-verified (`ui_interact` ×170, `tgui_interact` ×0). Still: treat it as a **routing aid only** — follow it to the right area of the code, then read the code for literal identifiers. Do not quote a symbol from here into a diff without grepping it first.

Canonical standalone base: this `ai_navigation_twilight` folder, kept alongside the rest of the ai-skills content — never assume a fixed disk path for it. Target repository: Twilight-Axis (project file `roguetown.dme`), wherever it's checked out locally.

Terminology:

- `AI mapping`, `navigation layer`, or `mental snapshot` means these repository-orientation docs.
- It does not mean in-game map files under `_maps/**`, `code/modules/mapping/**`, or `SSmapping`.

Treat this navigation layer as a routing aid. The Twilight-Axis repository's code is always the source of truth; verify load-bearing facts with `rg` or neighboring files before editing.

## Start Mode Selection

| Situation | Mode | Entrypoint |
|---|---|---|
| ordinary task with known keyword, type path, or symptom | Fast Start | router.md |
| broad, risky, multi-system, or explicitly human-guided | Guided Start | this file -> router.md |
| refresh or migration of this navigation layer | Maintenance Start | update_policy.md |
| TGUI/web UI/browser asset task | Bound Start | `$ss13-tgui` directly; local owners/paths are in system_map.md/subsystem_map.md |


## Guided Bootstrap

1. Open `router.md`.
2. Choose exactly one helper file.
3. Open up to two source files from the Twilight-Axis repository.
4. Check `modular_twilight_axis/**` first, then `modular_deserttown/**` and legacy `modular/**` if the core branch is extended.
5. Escalate only if unresolved.
6. Before edits, classify blast radius with `human_checking.md`.
