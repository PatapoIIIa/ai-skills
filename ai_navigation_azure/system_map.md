# System Map

Generated for Azure-Peak. Use this as the fast index of gameplay and infrastructure systems before opening source files.

## Repository Hotspots

- Codebase family: Azure-Peak / RogueTown, TGStation-derived BYOND Dream Maker project.
- Project file: `roguetown.dme`.
- Modular layer: `modular/`.
- `code/modules` largest slices by DM file count: `mob` (348), `spells` (253), `jobs` (232), `roguetown` (178), `events` (83), `admin` (80), `clothing` (69), `surgery` (57).
- `code/datums` largest slices by DM file count: `ai` (107), `components` (78), `sexcon2` (73), `gods` (29), `elements` (17), `migrants` (16), `brewing_recipes` (15), `status_effects` (15).
- `modular` top-level packs: `Creechers` (1 DM), `Mapping` (1 DM), `Neu_Farming` (1 DM), `Neu_Food` (45 DM), `ambush` (4 DM), `code` (16 DM), `icons` (0 DM), `piercing` (6 DM), `ze_genesis_call` (1 DM).
- Detected subsystem declarations: `115`.
- Signal calls: `RegisterSignal` `683`, `SEND_SIGNAL` `561`, `AddComponent` `505`.

## Type Path Counts

| Type root | Count |
|---|---:|
| `/mob` | 411 |
| `/datum/action` | 173 |
| `/datum/status_effect` | 449 |
| `/datum/component` | 173 |
| `/datum/element` | 16 |
| `/datum/ai_controller` | 53 |
| `/datum/ai_behavior` | 80 |
| `/datum/antagonist` | 38 |
| `/datum/skill` | 53 |
| `/datum/wound` | 76 |

## Major Systems

| System | Primary directories | Runtime owner | Notes |
|---|---|---|---|
| Master controller and round flow | `code/world.dm`, `code/controllers/**` | `Master`, `SSticker`, `SSatoms`, `SStimer` | `/world` boots; master discovers subsystem subtypes and drives runlevels/tick budgets. |
| DCS components and elements | `code/datums/components/**`, `code/datums/elements/**`, `code/__DEFINES/dcs/**`, `code/__DEFINES/components.dm` | `SSdcs` | Main composition/event system. Many combat/item signals are in `code/__DEFINES/components.dm`, not only `code/__DEFINES/dcs/**`. |
| Antagonists and events | `code/modules/antagonists/**`, `code/modules/events/**`, `code/datums/storytellers/**` | `SSgamemode`, `SSevents`, `SSticker` | Storytellers select events; antagonist datums and event controls bridge into roles. |
| Status effects, actions, spells | `code/datums/status_effects/**`, `code/modules/spells/**`, `code/datums/actions/**` | `SSskills`, `SSmood`, direct action cooldowns | Search direct status/action code and signal listeners. |
| AI controllers and behaviors | `code/datums/ai/**`, `code/modules/mob/**` | `SSai_controllers`, `SSai_behaviors`, `SSai_movement`, `SSidle_ai_behaviors`, `SSbasic_avoidance`, `SSaggro` | AI behavior file spelling is `code/controllers/subsystem/processing/ai_behaviours.dm` for the subsystem file. |
| Mobs, jobs, migrants | `code/modules/mob/**`, `code/modules/jobs/**`, `code/datums/migrants/**` | `SSjob`, `SSmobs`, `SSmobs_dead`, `SSmigrants`, `SSrole_class_handler` | Spawn-time role structure is core; `modular/**` may add content but not a separate architecture. |
| Economy, treasury, merchants, factions | `code/modules/economy/**`, `code/controllers/subsystem/economy.dm`, `code/controllers/subsystem/rogue/treasury.dm`, `code/datums/world_factions/**` | `SSeconomy`, `SStreasury`, `SSmerchant` | Inspect economy, treasury, merchant, and faction paths directly. |
| Questing and contracts | `code/modules/roguetown/roguemachine/questing/**`, `code/__DEFINES/questing.dm` | `SSdcs`, `SSroguemachine`, player/ledger flow | Contract flow is DM-side under the questing branch. |
| Crafting, farming, food | `code/modules/crafting/**`, `code/modules/farming/**`, `code/modules/food_and_drinks/**`, `modular/Neu_Food/code/**` | `SSskills`, `SSfarming` | Fisher job code is under `code/modules/roguetown/roguejobs/fisher/**`. |
| Skills, dreams, XP | `code/datums/skills/**`, `code/datums/skill_holder.dm` | `SSskills` | Skills are event-driven progression datums; job files grant initial skill state. |
| Gods, stress, wounds, mood | `code/datums/gods/**`, `code/datums/stress/**`, `code/datums/wounds/**`, `code/datums/status_effects/**` | `SSmood`, `SSskills`, direct datums | Patron/god data uses `code/datums/gods/**`. |
| Sex/arousal systems | `code/datums/sexcon2/**`, `code/modules/sexcon/**`, `modular/code/controllers/subsystem/processing/sex.dm` | `SSsex`, `SSdcs` | Arousal components live under `code/modules/sexcon/components/**`. |
| Combat intents and clash | `code/modules/mob/living/combat/**`, `code/_onclick/**` | `SSdcs`, direct combat chain | Clash lives in `azure_combat.dm`. |
| Mapping, dungeons, worldgen | `_maps/**`, `code/modules/mapping/**`, `code/modules/procedural_mapping/**`, `code/controllers/subsystem/processing/mapgen.dm` | `SSmapping`, `SSminor_mapping`, `SSdungeon_generator`, `SSmapgen`, `SSpathfinder` | Map/world behavior is split across mapping, dungeon, mapgen, and pathfinder subsystems. |
| Environment, fluids, weather, fire | `code/datums/particle_weathers/**`, `code/datums/weather/**`, `code/controllers/subsystem/particle_weather.dm`, `code/controllers/subsystem/weather.dm`, `code/controllers/subsystem/processing/fluids.dm` | `SSParticleWeather`, `SSoutdoor_effects`, `SSweather`, `SSfluids`, `SSfire_burning`, `SSfire_spread`, `SSlighting` | Use `SSfluids` for fluid processing. |
| UI and frontend stack | `code/modules/tgui/**`, `code/modules/tgui_input/**`, `code/modules/tgui_panel/**`, `interface/**`, `tgui/packages/**`, `html/**` | `SStgui`, `SSchat`, `SSstatpanel` | TGUI and interface paths own current UI flow. |
| Visuals, overlays, icon smoothing | `code/controllers/subsystem/overlays.dm`, `code/controllers/subsystem/vis_overlays.dm`, `code/controllers/subsystem/icon_smooth.dm`, `code/game/objects/effects/**` | `SSoverlays`, `SSvis_overlays`, `SSdamoverlays`, `SSicon_smooth` | Inspect icon/appearance code directly for recolor or sprite-layer behavior. |
| Azure modular extension layer | `modular/**` | Existing core `SS*` singletons plus `SSsex`, `SSmaturity_guard` | Late included in `roguetown.dme`; use it as an overlay/pack layer after checking core `code/`. |

## Dependency Awareness

- Components/elements are the main cross-cutting mechanism; prefer checking `RegisterSignal` listeners before assuming a direct proc call.
- Status effects are common state containers; inspect the status effect datum and caller lifecycle directly.
- Map/world systems are layered: `_maps` templates, mapping modules, `SSmapping`, `SSminor_mapping`, `SSdungeon_generator`, `SSmapgen`, and `SSpathfinder` own different phases.
- `modular/` does not create a second architecture. It extends or adds to core roots, so locate the core path first and then search the modular overlay.
