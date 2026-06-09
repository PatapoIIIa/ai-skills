# Router

Generated for Azure-Peak. This is the primary Fast Start entrypoint for normal tasks.

## Always

| When | Action |
|---|---|
| before any medium / high / unclear-scope edit | open `ai_navigation/human_checking.md` first |
| navigation docs say something does not exist or give no result | do not conclude it is absent; verify with direct `rg` / file search first |
| navigation lookup returns nothing for an SS*, proc, type, or system | search `code/` and `modular/` directly; if found, use it and flag the navigation gap |
| you used navigation and got an unexpected result | say navigation may be stale, then verify directly |

## Dispatch

| Task | Helper |
|---|---|
| planned change may be broad, risky, or needs approval before edits | `ai_navigation/human_checking.md` |
| refresh the navigation layer, rebuild its docs, or migrate this repository-orientation stack to another codebase | `ai_navigation/update_policy.md` |
| new mechanic, gameplay content, or extension to an existing feature with known shape | `ai_navigation/content_creation.md` |
| vague content request needing delivery/base/delta/effect decomposition | `ai_navigation/content_breakdown.md` |
| content goal is known but the implementation form is undecided | `ai_navigation/content_patterns.md` |
| existing behavior is indirect, DCS-driven, or signal-listener based | `ai_navigation/signal_map.md` |
| implementing a new component, element, or signal listener | `ai_navigation/content_patterns.md`, then `ai_navigation/signal_map.md` |
| spell, miracle, action, or cooldown behavior depends on signals | `ai_navigation/spell_signal_map.md` |
| melee, projectile, hit, disarm, parry, or combat chains depend on signals | `ai_navigation/combat_signal_map.md` |
| client movement, collisions, buckle, pull, throw, or moveloop behavior | `ai_navigation/movement_signal_map.md` |
| main proc entrypoints before searching source | `ai_navigation/core_procs.md` |
| whole subsystem or process loop freezes/hangs/stops without runtimes | `ai_navigation/processing_hazards.md` |
| explicit failure-mode analysis after the owner is known | `ai_navigation/failure_modes.md` |
| symptom-first bug report | `ai_navigation/debug_routes.md` |
| runtime error to diagnose or fix | `ai_navigation/runtime_errors.md` |
| qdel, del, Destroy(), ref leak | `ai_navigation/runtime_errors.md` -> `ai_navigation/coding_standards.md` |
| overlays, underlays, Appearance objects, planes, filters, particles, lighting, animate(), render relays, multiz | `ai_navigation/visuals_guide.md` |
| recolorable sprite or sprite-layer request | `ai_navigation/visuals_guide.md` |
| icon smoothing, smooth_icon, smoothing_flags, smoothing_groups, bitmask smoothing | `ai_navigation/icon_rendering.md` |
| iconstate2appearance, icon2appearance, appearance cache, vis_contents cache | `ai_navigation/icon_rendering.md` |
| performance, tick budget, CPU, server lag | `ai_navigation/engine_limits.md`, then `ai_navigation/performance_gotchas.md` |
| code style, signal pattern, GC, harddel, CI, walk procs, delta-time | `ai_navigation/coding_standards.md` |
| reagents, chemistry, holder, reagent container, splash | `code/modules/reagents/**`, especially `code/modules/reagents/chemistry/holder.dm` and `code/modules/reagents/chemistry/readme.md` |
| TGUI interface, `ui_interact`, `ui_data`, `ui_act`, React component | `ai_navigation/tgui_guide.md` |
| keyword or feature-name routing | `ai_navigation/entrypoints.md` |
| BYOND type path `/datum/...` `/mob/...` `/obj/...` | `ai_navigation/type_index.md` |
| lifecycle, timing, scheduler, round flow | `ai_navigation/runtime_flow.md` |
| `Initialize()`, `LateInitialize()`, atom init order, mapload setup | `ai_navigation/runtime_flow.md`, then `code/controllers/subsystem/atoms.dm` |
| explicit `SS*` subsystem | `ai_navigation/subsystem_map.md` |
| cross-system handoff or dependency | `ai_navigation/system_dependencies.md` |
| unknown architecture or location | `ai_navigation/system_map.md` or `ai_navigation/architecture.md` |
| modular layer and overlay rules | `ai_navigation/modular_guide.md` |
| deep inheritance | `ai_navigation/type_tree.md`; search the specific path, do not read whole file |
| budget rules, engine constraints detail | `ai_navigation/router_deep.md` |
