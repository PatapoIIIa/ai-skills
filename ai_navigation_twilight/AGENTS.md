# Repository Agent Guide

Canonical standalone base: `C:/Axis/ai-skills/ai_navigation_twilight`. Target repository: `C:/Axis/Twilight-Axis`.

Terminology:

- `AI mapping`, `navigation layer`, or `mental snapshot` means these repository-orientation docs.
- It does not mean in-game map files under `_maps/**`, `code/modules/mapping/**`, or `SSmapping`.

Treat this navigation layer as a routing aid. Code in `C:/Axis/Twilight-Axis` is always the source of truth; verify load-bearing facts with `rg` or neighboring files before editing.

## Start Mode Selection

| Situation | Mode | Entrypoint |
|---|---|---|
| ordinary task with known keyword, type path, or symptom | Fast Start | router.md |
| broad, risky, multi-system, or explicitly human-guided | Guided Start | this file -> router.md |
| refresh or migration of this navigation layer | Maintenance Start | update_policy.md |
| TGUI/web UI/browser asset task | Bound Start | tgui_guide.md + $ss13-tgui |


## Guided Bootstrap

1. Open `router.md`.
2. Choose exactly one helper file.
3. Open up to two source files from `C:/Axis/Twilight-Axis`.
4. Check `modular_twilight_axis/**` first, then `modular_deserttown/**` and legacy `modular/**` if the core branch is extended.
5. Escalate only if unresolved.
6. Before edits, classify blast radius with `human_checking.md`.
