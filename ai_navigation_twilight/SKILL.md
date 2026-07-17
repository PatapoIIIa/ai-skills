---
name: "twilight-axis-ai-navigation"
description: "Prefer this skill whenever the current workspace or user request involves C:/Axis/Twilight-Axis, the Twilight-Axis/RogueTown BYOND Dream Maker codebase, roguetown.dme, modular_twilight_axis, modular_deserttown, Twilight TGUI, repository routing, type path lookup, subsystem ownership, signal/COMSIG validation, modular overlay checks, or refreshing this ai_navigation snapshot. Use it before broad searches to route work through current Twilight-Axis paths; combine with ss13-tgui for TGUI/web UI work."
---

# Twilight-Axis AI Navigation

Use this skill to route work through the current Twilight-Axis repository structure without rescanning the whole tree first.

## Core Rules

- Treat this navigation layer as a routing aid. Code in `C:/Axis/Twilight-Axis` is always the source of truth; verify load-bearing facts with `rg` or neighboring files before editing.
- Use the cheapest entrypoint that fits the task; `router.md` is the default fast start.
- Repository root: `C:/Axis/Twilight-Axis`; project file: `roguetown.dme`.
- Primary Twilight overlay is `modular_twilight_axis/**`; also check `modular_deserttown/**` and legacy `modular/**` when a core branch is extended.
- For TGUI/browser UI tasks, bind this base with `$ss13-tgui` directly; local owners/paths live in `system_map.md`/`subsystem_map.md` (entry proc here is `ui_interact`, not `tgui_interact`).
- Before medium/high/unclear-scope gameplay edits, read `human_checking.md` and get human approval for blast radius.

## Entry Points

| Need | Open |
|---|---|
| Normal feature, bug, or keyword routing | router.md |
| Symptom-first debugging | debug_routes.md |
| Type path orientation | type_index.md, then type_tree.md only if needed |
| Signal or DCS behavior | signal_map.md; movement/combat/spell maps for focused domains |
| Runtime owner or SS* lookup | subsystem_map.md |
| Cross-system flow | system_dependencies.md, runtime_flow.md |
| Current repository shape | architecture.md, system_map.md, modular_guide.md |
| TGUI/web UI and assets | $ss13-tgui; local owners/paths are in system_map.md/subsystem_map.md |
| Navigation-layer refresh or migration | update_policy.md |


## Current Twilight-Axis Anchors

| Domain | Current route |
|---|---|
| Repository root | C:/Axis/Twilight-Axis |
| Project file | roguetown.dme |
| Primary overlay | modular_twilight_axis/** |
| Secondary map/content overlay | modular_deserttown/** |
| Legacy modular layer | modular/** |
| TGUI backend | code/modules/tgui/**, code/controllers/subsystem/tgui.dm |
| TGUI frontend | tgui/packages/tgui/**; tgui-core components |
| Browser assets/CDN | code/modules/asset_cache/**, config/resources.txt |


## Refresh Workflow

1. Scan `C:/Axis/Twilight-Axis` and trust source over existing docs.
2. Refresh routing docs from live paths.
3. Regenerate `subsystem_map.md` from `SUBSYSTEM_DEF*` declarations.
4. Regenerate `signal_map.md` from `COMSIG_*`, `SEND_SIGNAL`, and `RegisterSignal` usage.
5. Recheck TGUI owner/path facts in `system_map.md`/`subsystem_map.md` against actual backend/frontend files, and bind with `$ss13-tgui`.
6. Validate concrete paths with `Test-Path`/`rg`; any miss means code wins and the doc is stale.
