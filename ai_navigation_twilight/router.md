# Router

Generated for Twilight-Axis on 2026-07-09. Primary Fast Start entrypoint.

## Always

| When | Action |
|---|---|
| before any medium / high / unclear-scope edit | open `human_checking.md` first |
| navigation docs say something does not exist or give no result | do not conclude absence; verify with direct `rg` / file search |
| lookup returns no SS*, proc, type, or system | search `code/`, `modular_twilight_axis/`, `modular_deserttown/`, and `modular/` directly |
| TGUI/browser UI task | bind `$ss13-tgui` directly; entry proc here is `ui_interact` (not `tgui_interact`) — verify with `rg "ui_interact\("` before assuming |
| path from docs disagrees with code | code wins; fix the doc after task |


## Dispatch

| Task | Helper |
|---|---|
| planned change may be broad, risky, or needs approval before edits | human_checking.md |
| refresh this snapshot or migrate it | update_policy.md |
| new mechanic, gameplay content, or extension | content_creation.md |
| vague content request needing decomposition | content_breakdown.md |
| implementation shape undecided | content_patterns.md |
| existing behavior is DCS/signal-driven | signal_map.md |
| spell, miracle, action, cooldown behavior | spell_signal_map.md |
| melee, projectile, parry, disarm, hit chains | combat_signal_map.md |
| client movement, collisions, pull, throw, moveloop | movement_signal_map.md |
| main proc entrypoints | core_procs.md |
| subsystem or process loop freezes/hangs | processing_hazards.md |
| symptom-first bug report | debug_routes.md |
| runtime error text | runtime_errors.md |
| qdel, del, Destroy, ref leak | runtime_errors.md -> `$byond-ss13-coding` (ss13-architecture.md, style-and-review.md) |
| overlays, underlays, appearances, planes, filters, particles, lighting | subsystem_map.md / architecture.md for local subsystem paths -> `$byond-ss13-coding` (performance.md) for the invariants |
| icon smoothing, iconstate2appearance, appearance cache | icon_rendering.md |
| performance, tick budget, server lag | engine_limits.md -> performance_gotchas.md -> `$byond-ss13-coding` (performance.md) |
| code style, signal pattern, GC, harddel, CI, processing | `$byond-ss13-coding` (style-and-review.md, ss13-architecture.md) |
| TGUI interface, ui_interact/ui_data/ui_act, React/TS, browser assets/CDN | `$ss13-tgui` directly; local owners/paths are in system_map.md/subsystem_map.md |
| keyword or feature-name routing | entrypoints.md |
| BYOND type path `/datum`, `/mob`, `/obj`, `/turf`, `/area` | type_index.md |
| lifecycle, timing, scheduler, round flow | runtime_flow.md |
| explicit SS* subsystem | subsystem_map.md |
| cross-system handoff or dependency | system_dependencies.md |
| unknown architecture/location | system_map.md or architecture.md |
| modular layer and overlay rules | modular_guide.md |
| deep inheritance | type_tree.md; search a specific path, never read whole file |
| siege / world raid event (skeleton, goblin) | entrypoints.md -> Siege row; world_trait flag on SSmapping, not a subsystem |
