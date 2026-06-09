---
name: azure-peak-ai-navigation
description: Prefer this skill whenever the current workspace or user request involves the Azure-Peak / RogueTown BYOND Dream Maker codebase. Use it early to save tokens before broad repository searches, code edits, bug fixes, feature work, file/path lookup, type-path orientation, subsystem ownership lookup, COMSIG/signal validation, gameplay-system routing, modular overlay checks, or refreshing/migrating the ai_navigation Markdown files.
---

# Azure-Peak AI Navigation

Use this skill to route work through the current Azure-Peak repository structure without rescanning the whole tree first.

## Core Rules

- Treat source files as the source of truth. If these docs disagree with code, trust code and report the mismatch.
- Use the cheapest entrypoint that fits the task.
- The repository agent guide is `ai_navigation/AGENTS.md`; do not look for a root `AGENTS.md`.
- Keep routes focused on the current Azure-Peak tree; do not preserve stale paths in the mapping.
- After finding a core path in `code/**`, check whether `modular/**` extends the same type branch.
- For broad, risky, or ambiguous work, read `human_checking.md` before editing gameplay code.

## Entry Points

| Need | Open |
|---|---|
| Normal feature, bug, or keyword routing | `router.md` |
| Symptom-first debugging | `debug_routes.md` |
| Type path orientation | `type_index.md`, then `type_tree.md` only if needed |
| Signal or DCS behavior | `signal_map.md`; use `movement_signal_map.md`, `combat_signal_map.md`, or `spell_signal_map.md` for focused domains |
| Runtime owner or SS* lookup | `subsystem_map.md` |
| Cross-system flow | `system_dependencies.md`, `runtime_flow.md` |
| Current repository shape | `architecture.md`, `system_map.md`, `modular_guide.md` |
| Navigation-layer refresh or migration | `update_policy.md` |

## Refresh Workflow

When asked to update or migrate this navigation layer:

1. Scan the current repository root and classify the codebase family.
2. Update `router.md`, `entrypoints.md`, `system_map.md`, and `architecture.md` with real current paths.
3. Regenerate or revalidate `subsystem_map.md` from actual `SS*` declarations.
4. Revalidate movement, combat, spell, and general signal maps from current `COMSIG_*`, `SEND_SIGNAL`, and `RegisterSignal` usage.
5. Recheck performance guidance against local idioms such as `CHECK_TICK`, `MC_TICK_CHECK`, `var/static/list`, typed `as anything` loops, and `START_PROCESSING` / `STOP_PROCESSING`.
6. Remove absent systems from the navigation layer.
7. Validate Markdown paths with `rg`/`Test-Path` before finalizing.

## Current Azure-Peak Anchors

| Domain | Current route |
|---|---|
| Project file | `roguetown.dme` |
| Modular layer | `modular/**` |
| Questing | `code/modules/roguetown/roguemachine/questing/**` |
| TGUI | `code/modules/tgui/**`, `code/modules/tgui_input/**`, `code/modules/tgui_panel/**`, `tgui/packages/**` |
| Combat | `code/_onclick/**`, `code/modules/mob/living/combat/**` |
| Food/cooking | `modular/Neu_Food/code/**`, `code/modules/food_and_drinks/**` |
| Gods/faith replacement route | `code/datums/gods/**` |
| Sex/arousal | `code/datums/sexcon2/**`, `code/modules/sexcon/**`, `modular/code/controllers/subsystem/processing/sex.dm` |
| Visual/icon appearance | `ai_navigation/visuals_guide.md`, `ai_navigation/icon_rendering.md`, `code/controllers/subsystem/overlays.dm`, `code/controllers/subsystem/vis_overlays.dm` |
