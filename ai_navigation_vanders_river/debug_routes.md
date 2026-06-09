# Debug Routes

Generated on 2026-03-11. Use this file when the task starts from a symptom instead of a known file, type path, or subsystem.

## Symptom-First Routes

| Symptom | Open first | Then check | Runtime owner(s) |
|---|---|---|---|
| Whole process-driven feature freezes at once, no runtimes, timers stop expiring | `ai_navigation/processing_hazards.md`, owner subsystem file | blocking calls in the owner path, then `ai_navigation/failure_modes.md`; use `ai_navigation/subsystem_map.md` only if ownership is still unclear | target `SS*`, `Master` |
| Antagonist does not spawn, wrong villain, missing thralls | `ai_navigation/runtime_flow.md` (round flow), `code/modules/events/antagonist/**`, `code/modules/antagonists/**` | `code/datums/migrants/waves/antagonist/**`, map landmarks/spawn points, `ai_navigation/subsystem_map.md` | `SSticker`, `SSgamemode`, `SSevents` |
| Spell button works poorly or spell does nothing | `ai_navigation/spell_signal_map.md`, `code/modules/spells/spell.dm`, specific spell file | `code/datums/status_effects/**`, `code/datums/components/**`, `code/datums/elements/**`, then `ai_navigation/runtime_flow.md` if order/timing is still unclear | `SSmagic`, `SSstatusprocess`, `SSskills` |
| Hit logic, weapon effect, unarmed attack, or projectile behavior is wrong | `ai_navigation/combat_signal_map.md`, `code/_onclick/item_attack.dm` or `code/modules/projectiles/projectile.dm` | `code/_onclick/other_mobs.dm`, defense/species files, combat listeners/components, then `ai_navigation/movement_signal_map.md` if collision or travel is involved | `SSdcs`, mob/projectile paths, AI combat listeners |
| Player movement, collision, pull, buckle, or automated movement behaves wrong | `ai_navigation/movement_signal_map.md`, `code/modules/mob/mob_movement.dm` | `code/modules/mob/living/living_movement.dm`, `code/controllers/subsystem/movement/**`, movable signal listeners, then `ai_navigation/combat_signal_map.md` if bumps or projectile travel are involved | `SSmovement`, `SSdcs`, mob movement paths |
| Sex, arousal, or ERP behavior is slow, stale, or inconsistent | `code/datums/sex/**`, `code/datums/components/arousal.dm` | `ai_navigation/signal_map.md`, mob/chat hooks, `modular_rmh` lewd and horny-AI overlays | `SSobj`, `SSdcs`, mob/chat paths |
| Status effect applies then disappears or never ticks | `code/datums/status_effects/**`, `ai_navigation/runtime_flow.md` | if many effects freeze together or there are no runtimes, open `ai_navigation/processing_hazards.md`; if the owner is known but the break mode is unclear, open `ai_navigation/failure_modes.md`; otherwise check components/elements, signal hooks, spell/action caller | `SSstatusprocess`, sometimes `SSmagic` |
| Player gets wrong role, wrong loadout, or latejoin is broken | `code/modules/jobs/**`, `code/datums/migrants/**`, `ai_navigation/runtime_flow.md` (role/job flow) | `modular_rmh/code/modules/jobs/**`, `SSrole_class_handler`, spawn landmarks | `SSjob`, `SSmigrants`, `SSrole_class_handler` |
| Overlay does not appear, flickers, duplicates, or fails to clear; visual state is wrong after fire/burn/status | `ai_navigation/visuals_guide.md`, `ai_navigation/performance_gotchas.md` §7 | `ai_navigation/signal_map.md` if the trigger is indirect; `ai_navigation/coding_standards.md` §GC if overlay holder may have been deleted before visual cleared; check `managed_overlays` contract and `update_overlays()` call chain | `SSoverlays`, `SSdcs`, owning mob/atom path |
| UI opens, but values are wrong or stale | `code/modules/tgui/**`, `code/modules/visual_ui/**`, `tgui/packages/**` | underlying gameplay datum/mob, status/components, browser handlers | `SStgui`, `SSvisual_ui`, `SSchat` |
| Roundstart/startup/runtime order looks wrong | `code/world.dm`, `code/controllers/master.dm`, `ai_navigation/runtime_flow.md`, `ai_navigation/subsystem_map.md` | target subsystem file and its `fire()/Initialize()` path | `Master`, target `SS*` |
| Map landmark is missing or wrong place is used | `_maps/**`, `code/modules/mapping/**`, `ai_navigation/runtime_flow.md` (mapping flow) | landmark type path, event/job consumer, procedural mapgen | `SSmapping`, `SSminor_mapping`, `SSdungeon_generator` |
| Feature changes state indirectly and there is no obvious proc chain | `ai_navigation/signal_map.md`, `code/datums/components/**`, `code/datums/elements/**` | `code/__DEFINES/dcs/**`, original caller via `SEND_SIGNAL`, then `ai_navigation/core_procs.md` if the hook family is still unclear | `SSdcs` plus the owning feature subsystem |
| Lag, hitching, runaway processing, or MC pressure | `ai_navigation/engine_limits.md` → `ai_navigation/performance_gotchas.md`, then `ai_navigation/subsystem_map.md` and owner subsystem file | hot feature files, signal/component hotspots, high-frequency loops; check `world.cpu` first to distinguish server lag from network lag | target `SS*`, `Master` |
| NPC is idle, stuck, chooses wrong target, or pathfinding silently stops | `code/datums/ai/**`, `ai_navigation/runtime_flow.md` (AI flow) | `code/controllers/subsystem/processing/ai_behaviors.dm`, `ai_movement.dm`, mob-specific files; if the NPC uses `walk_to` / `walk_towards`, check whether the target is within `world.view * 2 + 1` tiles (default 11) — `walk_to` is a silent no-op beyond that range; see `ai_navigation/engine_limits.md` §View and Map | `SSai_controllers`, `SSai_behaviors`, `SSai_movement` |

## Cheap Debugging Rules

- Pick one route row first. Do not open `ai_navigation/system_map.md` unless the symptom still does not localize.
- Once the owner subsystem is known, switch from maps to source files quickly.
- If a symptom obviously maps to a BYOND type path, use `ai_navigation/type_index.md` instead.
- If a whole subsystem or effect family stops without runtimes, open `ai_navigation/processing_hazards.md` before assuming raw load.
- For process-driven bugs, grep blocking calls in the owner path: `input`, `alert`, `browse`, `do_after`, `sleep`, `waitfor`, and also `walk(`, `walk_to(`, `walk_towards(`, `walk_rand(` — all of these sleep internally.
- If the owner is known but the cause is still fuzzy, open `ai_navigation/failure_modes.md` and classify the scale of failure before guessing.
- For lag or performance symptoms, open `ai_navigation/engine_limits.md` first for the hard numbers, then `ai_navigation/performance_gotchas.md` for pattern-level hazards.
- Only if the current source still does not explain a systemic freeze, inspect recent commits as a fallback.
- After finding the core implementation, always check the same branch in `modular_rmh`.
