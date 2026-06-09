# Entrypoints

Generated for Azure-Peak. Use this file before the larger maps when the goal can be matched to a known system quickly.

## Minimal Route

1. Match the task to one row below.
2. Open only the listed directories/files first.
3. Escalate only if needed:
   - symptom-first debugging -> `ai_navigation/debug_routes.md`
   - handoff between systems unclear -> `ai_navigation/system_dependencies.md`
   - execution order/lifecycle unclear -> `ai_navigation/runtime_flow.md`
   - ownership unclear -> `ai_navigation/subsystem_map.md`
   - system unclear -> `ai_navigation/system_map.md`
   - branch/root unclear for a type path -> `ai_navigation/type_index.md`
   - deep inheritance unclear -> `ai_navigation/type_tree.md`
   - architecture/layer question -> `ai_navigation/architecture.md`

## Fast Index

| Task or keyword | Open first | Then check | Runtime owner |
|---|---|---|---|
| `vampire`, `werewolf`, `antag`, `thrall`, `villain` | `code/modules/antagonists/**` | `code/modules/events/antagonist/**`, `code/datums/storytellers/**`, `code/datums/migrants/**` | `SSgamemode`, `SSevents`, `SSticker` |
| `job`, `role`, `latejoin`, `spawn role`, `migrant`, `class` | `code/modules/jobs/**`, `code/datums/migrants/**` | `modular/code/modules/jobs/**`, `code/modules/mob/**` | `SSjob`, `SSmigrants`, `SSrole_class_handler` |
| `spell`, `ability`, `action`, `miracle`, `rituos`, `projectile`, `aoe`, `cone`, `touch` | `code/modules/spells/**`, `ai_navigation/spell_signal_map.md` | `code/datums/actions/**`, `code/datums/status_effects/**`, `code/datums/components/**`, `code/datums/elements/**` | `SSskills`, `SSmood`, direct action/spell code |
| `combat`, `melee`, `attack`, `hit`, `weapon`, `disarm`, `parry`, `block`, `shield`, `projectile` | `ai_navigation/combat_signal_map.md`, `code/_onclick/item_attack.dm` | `code/_onclick/other_mobs.dm`, `code/modules/mob/living/combat/**`, `code/modules/projectiles/projectile.dm`, defense/species files | `SSdcs`, mob/projectile paths, AI combat listeners |
| `sex`, `lewd`, `arousal`, `erp`, `kink` | `code/datums/sexcon2/**`, `code/modules/sexcon/**`, `code/modules/sexcon/components/arousal.dm` | `modular/code/controllers/subsystem/processing/sex.dm`, `modular/code/game/objects/items/lewd/**`, `code/modules/mob/**`, `ai_navigation/signal_map.md` | `SSsex`, `SSdcs`, mob/chat paths |
| `ai`, `npc`, `behavior`, `controller`, `hostile mob` | `code/datums/ai/**`, `code/modules/mob/**` | `code/controllers/subsystem/ai_controller.dm`, `code/controllers/subsystem/processing/ai_behaviours.dm`, `code/controllers/subsystem/processing/ai_movement.dm` | `SSai_controllers`, `SSai_behaviors`, `SSai_movement` |
| `movement`, `move`, `collision`, `pull`, `buckle`, `throw`, `glide`, `moveloop`, `pathing` | `ai_navigation/movement_signal_map.md`, `code/modules/mob/mob_movement.dm`, `code/game/atoms_movable.dm` | `code/modules/mob/living/living_movement.dm`, `code/game/objects/buckling.dm`, `code/controllers/subsystem/movement/**` | `SSmovement`, `SSmove_manager`, `SSthrowing`, `SSdcs` |
| `quest`, `questing`, `contract`, `bounty`, `courier`, `retrieval`, `scroll`, `compass`, `quest_object`, `contractledger` | `code/modules/roguetown/roguemachine/questing/**` | `code/modules/roguetown/roguemachine/questing/contract_ledger.dm`, `code/modules/roguetown/roguemachine/questing/questing_components.dm`, `code/modules/roguetown/roguemachine/questing/types/**`, `code/modules/roguetown/roguemachine/questing/items/**`, `code/__DEFINES/questing.dm` | `SSdcs`, `SSroguemachine`, player/ledger flow |
| `quest map config`, `quest difficulty`, `quest reward modifier`, `quest distance bonus` | `code/__DEFINES/questing.dm`, `code/modules/roguetown/roguemachine/questing/**` | `modular/ambush/ambush_config/**`, `code/controllers/subsystem/rogue/regional_threat/**` | no dedicated SS; quest generation/ledger flow |
| `quest ambush`, `ambush payload`, `ambush_config`, `regional threat`, `signal horn` | `modular/ambush/ambush_config/**`, `code/controllers/subsystem/rogue/regional_threat/**` | `code/game/objects/structures/roguetown/rogueflora.dm`, `code/game/objects/items/signal_horn.dm`, `code/__DEFINES/questing.dm` | `SSregionthreat`, direct component/proc flow |
| `map`, `dungeon`, `worldgen`, `template`, `spawn landmark` | `_maps/**`, `code/modules/mapping/**`, `code/modules/procedural_mapping/**` | `code/controllers/subsystem/mapping.dm`, `minor_mapping.dm`, `dungeon_generator.dm`, `code/controllers/subsystem/processing/mapgen.dm`, `modular/Mapping/**` | `SSmapping`, `SSminor_mapping`, `SSdungeon_generator`, `SSmapgen`, `SSpathfinder` |
| `economy`, `merchant`, `treasury`, `property`, `housing`, `faction` | `code/modules/economy/**`, `code/controllers/subsystem/economy.dm`, `code/controllers/subsystem/rogue/treasury.dm` | `code/datums/world_factions/**`, `code/controllers/subsystem/merchant.dm` | `SSeconomy`, `SStreasury`, `SSmerchant` |
| `craft`, `recipe`, `material`, `runeword`, `anvil`, `fishing`, `farming` | `code/modules/crafting/**`, `code/modules/farming/**`, `modular/code/modules/crafting/**` | `code/modules/roguetown/roguejobs/fisher/**`, `modular/Neu_Farming/**`, `code/datums/brewing_recipes/**` | `SSskills`, `SSfarming` |
| `faith`, `god`, `patron`, `mana`, `quirk`, `wound`, `stress`, `mood` | `code/datums/gods/**`, `code/datums/stress/**`, `code/datums/wounds/**`, `code/datums/status_effects/**` | `code/datums/special_traits/**`, `code/datums/usurpation_rite/**` | `SSskills`, `SSmood`, direct datums |
| `skill`, `skill level`, `dream`, `xp`, `experience`, `skill_holder` | `code/datums/skills/**`, `code/datums/skill_holder.dm` | `code/modules/jobs/**`, `modular/code/modules/jobs/**` for spawn grants | `SSskills` |
| `special_intent`, `aoe intent`, `clash`, `riposte`, `guard`, `stamina cost` | `code/modules/mob/living/combat/**` | `code/modules/mob/living/combat/special_intents.dm`, `code/modules/mob/living/combat/azure_combat.dm`, `ai_navigation/combat_signal_map.md` | `SSdcs`, combat chain |
| `culture`, `character background`, `species culture`, `on_after_spawn` | `code/datums/mob_descriptors/**`, `code/datums/special_traits/**` | species/job spawn code depending on actual feature | no dedicated SS |
| `cooking`, `food`, `recipe`, `raw food`, `NeuFood`, `brew`, `tea` | `modular/Neu_Food/code/**`, `code/modules/food_and_drinks/**` | `modular/Neu_Food/code/NeuFood.dm`, `modular/Neu_Food/code/cooked/**`, `modular/Neu_Food/code/raw/**`, `modular/Neu_Food/code/recipes/**`, `code/modules/reagents/**` | `SSskills`, direct crafting/reagent paths |
| `rage`, `rage meter`, `rage tier`, `bloodpool`, `werewolf rage` | `code/modules/antagonists/roguetown/villain/werewolf/**`, `code/modules/vampire_neu/**` | `code/datums/status_effects/**`, `ai_navigation/signal_map.md` | no dedicated SS |
| `recolor`, `sprite layers`, `appearance`, `overlay` | `ai_navigation/visuals_guide.md`, `ai_navigation/icon_rendering.md` | icon/appearance code for the target item or mob | `SSoverlays`, `SSvis_overlays`, `SSdamoverlays` |
| `icon smoothing`, `smooth_icon`, `smoothing_flags`, `smoothing_groups`, `SMOOTH_BITMASK`, `bitmask wall`, `tile junction` | `ai_navigation/icon_rendering.md`, `code/__HELPERS/icon_smoothing.dm` | `code/controllers/subsystem/icon_smooth.dm` | `SSicon_smooth` |
| `iconstate2appearance`, `icon2appearance`, `appearance cache`, `vis_contents cache` | `ai_navigation/icon_rendering.md`, `code/controllers/subsystem/overlays.dm` | `code/controllers/subsystem/vis_overlays.dm`, `code/__DEFINES/layers.dm` | `SSoverlays`, `SSvis_overlays`, `SSdamoverlays` |
| `liquid`, `fluid`, `weather`, `fire`, `overlay`, `lighting` | `code/controllers/subsystem/processing/fluids.dm`, `code/datums/particle_weathers/**`, `code/datums/weather/**`, `ai_navigation/visuals_guide.md` | `code/controllers/subsystem/weather.dm`, `particle_weather.dm`, `particle_weather_outdoors.dm`, fire/overlay subsystems | `SSfluids`, `SSParticleWeather`, `SSoutdoor_effects`, `SSweather`, `SSfire_burning`, `SSfire_spread`, `SSlighting` |
| `tgui`, `ui`, `browser`, `hud`, `interface` | `code/modules/tgui/**`, `code/modules/tgui_input/**`, `code/modules/tgui_panel/**`, `interface/**` | `tgui/packages/**`, `html/**` | `SStgui`, `SSchat`, `SSstatpanel` |
| `lag`, `runtime`, `processing`, `tick`, `scheduler`, `master`, `startup` | `ai_navigation/subsystem_map.md`, `code/world.dm`, `code/controllers/master.dm`, `code/controllers/subsystem.dm` | `code/controllers/subsystem/**`, `rg` for the relevant `SS*` | `Master`, target `SS*` |
| exact BYOND type path like `/datum/...`, `/mob/...`, `/obj/...` | `ai_navigation/type_index.md` | matching DM branch in `code/**` and `modular/**`, then `ai_navigation/type_tree.md` if needed | depends on branch |

## Escalation Rules

- If a keyword row matches, do not open `ai_navigation/system_map.md` immediately.
- If the user gives a symptom instead of a feature name, switch to `ai_navigation/debug_routes.md`.
- If the first branch is wrong, switch rows once before doing a broad repository search.
- After locating a core path in `code/`, always check whether `modular` extends the same branch.
