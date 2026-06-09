# Debug Routes

Generated for Azure-Peak. Use this file when the user reports a symptom rather than a system name.

| Symptom | Open first | Then check | Likely owner |
|---|---|---|---|
| Runtime during startup, mapload, or `LateInitialize` | `ai_navigation/runtime_flow.md`, `code/controllers/subsystem/atoms.dm` | parent `Initialize()` return hints, mapload-only assumptions | `SSatoms`, target subsystem |
| Spell button works poorly or spell does nothing | `ai_navigation/spell_signal_map.md`, `code/modules/spells/**`, `code/datums/actions/**` | `code/datums/status_effects/**`, components/elements, cooldown/action caller | direct spell/action code, `SSskills` |
| Melee hit, parry, block, disarm, or projectile chain breaks | `ai_navigation/combat_signal_map.md`, `code/_onclick/item_attack.dm` | `code/modules/mob/living/combat/**`, `code/modules/projectiles/projectile.dm`, components/elements | `SSdcs`, direct combat chain |
| Movement, pulling, buckling, riding, or thrown-object travel is wrong | `ai_navigation/movement_signal_map.md`, `code/modules/mob/mob_movement.dm`, `code/game/atoms_movable.dm` | `code/game/objects/buckling.dm`, `code/controllers/subsystem/movement/**`, `code/controllers/subsystem/throwing.dm` | `SSmovement`, `SSmove_manager`, `SSthrowing`, `SSdcs` |
| Status effect applies then disappears or never ticks | `code/datums/status_effects/**`, `ai_navigation/runtime_flow.md` | caller that applies it, components/elements, `SSmood` if mood-related | direct status datum/caller |
| Player gets wrong role, wrong loadout, or latejoin is broken | `code/modules/jobs/**`, `code/datums/migrants/**`, `ai_navigation/runtime_flow.md` | `modular/code/modules/jobs/**`, `SSrole_class_handler`, spawn landmarks | `SSjob`, `SSmigrants`, `SSrole_class_handler` |
| Quest contract, scroll, courier/retrieval/kill objective, or ledger breaks | `code/modules/roguetown/roguemachine/questing/**` | `code/__DEFINES/questing.dm`, `code/modules/roguetown/roguemachine/questing/questing_components.dm`, `code/modules/roguetown/roguemachine/questing/contract_ledger.dm` | `SSdcs`, `SSroguemachine`, ledger flow |
| Ambush or regional threat behavior is wrong | `code/controllers/subsystem/rogue/regional_threat/**`, `modular/ambush/ambush_config/**` | `code/game/objects/structures/roguetown/rogueflora.dm`, `code/game/objects/items/signal_horn.dm` | `SSregionthreat`, direct proc/component flow |
| UI opens, but values are wrong or stale | `code/modules/tgui/**`, `code/modules/tgui_input/**`, `code/modules/tgui_panel/**`, `tgui/packages/**` | underlying gameplay datum/mob, browser handlers, status/components | `SStgui`, `SSchat`, `SSstatpanel` |
| NPC pathing or hostile mob decisions are wrong | `code/datums/ai/**`, `code/controllers/subsystem/ai_controller.dm` | `code/controllers/subsystem/processing/ai_behaviours.dm`, `code/controllers/subsystem/processing/ai_movement.dm`, movement map | `SSai_controllers`, `SSai_behaviors`, `SSai_movement` |
| Economy, treasury, merchant, faction money is wrong | `code/modules/economy/**`, `code/controllers/subsystem/rogue/treasury.dm`, `code/controllers/subsystem/merchant.dm` | `code/datums/world_factions/**` | `SSeconomy`, `SStreasury`, `SSmerchant` |
| Ticks freeze, lag spikes, or subsystem budget blows up | `ai_navigation/subsystem_map.md`, `ai_navigation/processing_hazards.md`, `ai_navigation/performance_gotchas.md` | exact `SS*` file and `fire()` loop | target `SS*`, `Master` |
| Overlay/visual/network lag or icon rendering issue | `ai_navigation/visuals_guide.md`, `ai_navigation/icon_rendering.md` | overlay/vis/icon smoothing subsystems, atom appearance call sites | `SSoverlays`, `SSvis_overlays`, `SSicon_smooth`, `SStgui` |
