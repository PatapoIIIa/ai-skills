# System Dependencies

Generated for Azure-Peak. Use this when a change crosses system boundaries and you need to know which owners to inspect together.

| System | Depends on / hands off to | Runtime owner | Primary paths |
|---|---|---|---|
| World bootstrap | master controller, subsystem discovery, atom initialization | `Master`, `SSatoms`, target `SS*` | `code/world.dm`, `code/controllers/master.dm`, `code/controllers/subsystem.dm`, `code/controllers/subsystem/atoms.dm` |
| Jobs / migrants / role classes | mob spawn, loadout, class selection, later antag overlays | `SSjob`, `SSmigrants`, `SSrole_class_handler` | `code/modules/jobs/**`, `code/datums/migrants/**`, `modular/code/modules/jobs/**` |
| Actions / spells | status effects, cooldowns, mob/item effects, components/elements | direct action/spell code, `SSskills`, `SSmood` | `code/modules/spells/**`, `code/datums/actions/**`, `code/datums/status_effects/**` |
| Combat | click chain, mob defense, projectiles, movement and signals | `SSdcs`, `SSprojectiles`, direct combat procs | `code/_onclick/**`, `code/modules/mob/living/combat/**`, `code/modules/projectiles/**` |
| Movement | client input, movable signals, pull/buckle/throw, moveloops | `SSmovement`, `SSmove_manager`, `SSthrowing`, `SSdcs` | `code/modules/mob/mob_movement.dm`, `code/game/atoms_movable.dm`, `code/game/objects/buckling.dm`, `code/controllers/subsystem/movement/**` |
| AI | mob state, behavior trees, movement/pathing, combat targets | `SSai_controllers`, `SSai_behaviors`, `SSai_movement`, `SSaggro` | `code/datums/ai/**`, `code/controllers/subsystem/ai_controller.dm`, `code/controllers/subsystem/processing/ai_behaviours.dm` |
| Questing | contract ledger, scrolls/items, objective components, treasury payout | `SSdcs`, `SSroguemachine`, `SStreasury` | `code/modules/roguetown/roguemachine/questing/**`, `code/__DEFINES/questing.dm` |
| Ambush / regional threat | foliage/travel triggers, threat regions, ambush configs, mob spawn | `SSregionthreat`, direct proc/component flow | `code/controllers/subsystem/rogue/regional_threat/**`, `modular/ambush/ambush_config/**`, `code/game/objects/items/signal_horn.dm` |
| Mapping / worldgen | landmarks, spawn points, dungeons, mapgen placement | `SSmapping`, `SSminor_mapping`, `SSdungeon_generator`, `SSmapgen`, `SSpathfinder` | `_maps/**`, `code/modules/mapping/**`, `code/modules/procedural_mapping/**`, `code/controllers/subsystem/processing/mapgen.dm` |
| Economy / treasury / merchants | currency, tax, faction/world state, quest payout | `SSeconomy`, `SStreasury`, `SSmerchant` | `code/modules/economy/**`, `code/controllers/subsystem/rogue/treasury.dm`, `code/datums/world_factions/**` |
| Crafting / farming / food | skills, recipes, reagents, food items, farming loops | `SSskills`, `SSfarming` | `code/modules/crafting/**`, `code/modules/farming/**`, `modular/Neu_Food/code/**`, `code/modules/reagents/**` |
| Gods / stress / wounds / mood | character state, status effects, skill and trait systems | `SSskills`, `SSmood`, direct datums | `code/datums/gods/**`, `code/datums/stress/**`, `code/datums/wounds/**`, `code/datums/status_effects/**` |
| Sex/arousal | sexcon datums, components, chat/mob state, modular processing | `SSsex`, `SSdcs` | `code/datums/sexcon2/**`, `code/modules/sexcon/**`, `modular/code/controllers/subsystem/processing/sex.dm` |
| UI / TGUI / browser | DM UI datums -> gameplay datum/mob -> frontend state | `SStgui`, `SSchat`, `SSstatpanel` | `code/modules/tgui/**`, `code/modules/tgui_input/**`, `code/modules/tgui_panel/**`, `interface/**`, `tgui/packages/**` |
| Visuals / overlays / icon smoothing | atom appearance, overlay caches, vis overlays, network output | `SSoverlays`, `SSvis_overlays`, `SSdamoverlays`, `SSicon_smooth` | `code/controllers/subsystem/overlays.dm`, `code/controllers/subsystem/vis_overlays.dm`, `code/controllers/subsystem/rogue/damoverlays.dm`, `code/controllers/subsystem/icon_smooth.dm` |
