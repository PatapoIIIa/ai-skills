# Subsystem Map

Generated for Azure-Peak from actual subsystem macro declarations in `code/**` and `modular/**`.

- Total subsystem declarations detected: **115**
- Macro family breakdown: movement=2, processing=24, standard=89
- Naming rule: `SUBSYSTEM_DEF(X)` creates global `SSX`; `SUBSYSTEM_DEF(ticker)` becomes `SSticker` by token paste.

## Category Summary

| Category | Subsystems | Examples |
|---|---:|---|
| Boot and infrastructure | 11 | `SSasset_loading`, `SSassets`, `SSatoms`, `SSblackbox`, `SSdbcore` |
| Gameplay simulation | 46 | `SSachievements`, `SSacid`, `SSadjacent_air`, `SSai_controllers`, `SSambience` |
| Movement and pathing | 5 | `SSai_movement`, `SSconveyors`, `SSminecarts`, `SSmove_manager`, `SSmovement` |
| Processing loops | 23 | `SSaggro`, `SSai_behaviors`, `SSbasic_avoidance`, `SSdcs`, `SSfarming` |
| Round flow and player lifecycle | 8 | `SSgamemode`, `SSjob`, `SSlobbymenu`, `SSmaturity_guard`, `SSmigrants` |
| UI, comms and admin | 9 | `SSchat`, `SScommunications`, `SSdiscord`, `SSinput`, `SSradio` |
| World generation and map state | 13 | `SSdungeon_generator`, `SSfire_burning`, `SSfire_spread`, `SSlighting`, `SSoutdoor_effects` |

## Atom Lifecycle (SSatoms)

Read `code/controllers/subsystem/atoms.dm` before changing `Initialize()`, `LateInitialize()`, or mapload order. Atoms returning `INITIALIZE_HINT_LATELOAD` are queued and receive `LateInitialize()` after map atoms finish initializing. Plain parent `..()` usually returns `INITIALIZE_HINT_NORMAL`, so subclasses that need `LateInitialize()` must return `INITIALIZE_HINT_LATELOAD` explicitly.

## Complete Subsystem Index

| SS global | Kind | Category | Type path | File |
|---|---|---|---|---|
| `SSachievements` | standard | Gameplay simulation | `/datum/controller/subsystem/achievements` | `code/controllers/subsystem/achievements.dm` |
| `SSacid` | standard | Gameplay simulation | `/datum/controller/subsystem/acid` | `code/controllers/subsystem/acid.dm` |
| `SSadjacent_air` | standard | Gameplay simulation | `/datum/controller/subsystem/adjacent_air` | `code/controllers/subsystem/adjacent_air.dm` |
| `SSaggro` | processing | Processing loops | `/datum/controller/subsystem/processing/aggro` | `code/controllers/subsystem/aggro.dm` |
| `SSai_behaviors` | processing | Processing loops | `/datum/controller/subsystem/processing/ai_behaviors` | `code/controllers/subsystem/processing/ai_behaviours.dm` |
| `SSai_controllers` | standard | Gameplay simulation | `/datum/controller/subsystem/ai_controllers` | `code/controllers/subsystem/ai_controller.dm` |
| `SSai_movement` | processing | Movement and pathing | `/datum/controller/subsystem/processing/ai_movement` | `code/controllers/subsystem/processing/ai_movement.dm` |
| `SSambience` | standard | Gameplay simulation | `/datum/controller/subsystem/ambience` | `code/controllers/subsystem/music_update.dm` |
| `SSasset_loading` | standard | Boot and infrastructure | `/datum/controller/subsystem/asset_loading` | `code/controllers/subsystem/asset_loading.dm` |
| `SSassets` | standard | Boot and infrastructure | `/datum/controller/subsystem/assets` | `code/controllers/subsystem/assets.dm` |
| `SSatoms` | standard | Boot and infrastructure | `/datum/controller/subsystem/atoms` | `code/controllers/subsystem/atoms.dm` |
| `SSbasic_avoidance` | processing | Processing loops | `/datum/controller/subsystem/processing/basic_avoidance` | `code/controllers/subsystem/processing/ai_avoidance.dm` |
| `SSblackbox` | standard | Boot and infrastructure | `/datum/controller/subsystem/blackbox` | `code/controllers/subsystem/blackbox.dm` |
| `SSBMtreasury` | standard | Gameplay simulation | `/datum/controller/subsystem/BMtreasury` | `code/modules/roguetown/roguemachine/merchant/bathmaster.dm` |
| `SSchat` | standard | UI, comms and admin | `/datum/controller/subsystem/chat` | `code/controllers/subsystem/chat.dm` |
| `SSchimeric_tech` | standard | Gameplay simulation | `/datum/controller/subsystem/chimeric_tech` | `code/controllers/subsystem/rogue/heart_tech_subsystem.dm` |
| `SScommunications` | standard | UI, comms and admin | `/datum/controller/subsystem/communications` | `code/controllers/subsystem/communications.dm` |
| `SSconveyors` | movement | Movement and pathing | `/datum/controller/subsystem/movement/conveyors` | `code/controllers/subsystem/movement/conveyors.dm` |
| `SScrediticons` | standard | Gameplay simulation | `/datum/controller/subsystem/crediticons` | `code/controllers/subsystem/rogue/crediticons.dm` |
| `SSdamoverlays` | standard | Gameplay simulation | `/datum/controller/subsystem/damoverlays` | `code/controllers/subsystem/rogue/damoverlays.dm` |
| `SSdbcore` | standard | Boot and infrastructure | `/datum/controller/subsystem/dbcore` | `code/controllers/subsystem/dbcore.dm` |
| `SSdcs` | processing | Processing loops | `/datum/controller/subsystem/processing/dcs` | `code/controllers/subsystem/dcs.dm` |
| `SSdiscord` | standard | UI, comms and admin | `/datum/controller/subsystem/discord` | `code/controllers/subsystem/discord.dm` |
| `SSdroning` | standard | Gameplay simulation | `/datum/controller/subsystem/droning` | `code/modules/droning/droning.dm` |
| `SSdungeon_generator` | standard | World generation and map state | `/datum/controller/subsystem/dungeon_generator` | `code/controllers/subsystem/dungeon_generator.dm` |
| `SSeconomy` | standard | Gameplay simulation | `/datum/controller/subsystem/economy` | `code/controllers/subsystem/economy.dm` |
| `SSelastic` | standard | Gameplay simulation | `/datum/controller/subsystem/elastic` | `code/controllers/subsystem/elastic.dm` |
| `SSevent_scheduler` | standard | Gameplay simulation | `/datum/controller/subsystem/event_scheduler` | `code/controllers/subsystem/rogue/scheduled_event_subsytem.dm` |
| `SSevents` | standard | Gameplay simulation | `/datum/controller/subsystem/events` | `code/controllers/subsystem/events.dm` |
| `SSfarming` | processing | Processing loops | `/datum/controller/subsystem/processing/farming` | `code/controllers/subsystem/processing/farming.dm` |
| `SSfastprocess` | processing | Processing loops | `/datum/controller/subsystem/processing/fastprocess` | `code/controllers/subsystem/processing/fastprocess.dm` |
| `SSfire_burning` | standard | World generation and map state | `/datum/controller/subsystem/fire_burning` | `code/controllers/subsystem/fire_burning.dm` |
| `SSfire_spread` | standard | World generation and map state | `/datum/controller/subsystem/fire_spread` | `code/controllers/subsystem/fire_spread.dm` |
| `SSfluids` | processing | Processing loops | `/datum/controller/subsystem/processing/fluids` | `code/controllers/subsystem/processing/fluids.dm` |
| `SSgamemode` | standard | Round flow and player lifecycle | `/datum/controller/subsystem/gamemode` | `code/controllers/subsystem/storyteller.dm` |
| `SSgarbage` | standard | Boot and infrastructure | `/datum/controller/subsystem/garbage` | `code/controllers/subsystem/garbage.dm` |
| `SSgnoll_scaling` | standard | Gameplay simulation | `/datum/controller/subsystem/gnoll_scaling` | `code/controllers/subsystem/rogue/gnolls_subsystem.dm` |
| `SShaunting` | processing | Processing loops | `/datum/controller/subsystem/processing/haunting` | `code/controllers/subsystem/processing/haunting.dm` |
| `SShotspots` | standard | Gameplay simulation | `/datum/controller/subsystem/hotspots` | `code/controllers/subsystem/hotspots.dm` |
| `SShuds` | processing | Processing loops | `/datum/controller/subsystem/processing/huds` | `code/controllers/subsystem/processing/huds.dm` |
| `SSicon_smooth` | standard | Gameplay simulation | `/datum/controller/subsystem/icon_smooth` | `code/controllers/subsystem/icon_smooth.dm` |
| `SSidle_ai_behaviors` | processing | Processing loops | `/datum/controller/subsystem/processing/idle_ai_behaviors` | `code/controllers/subsystem/processing/idle_ai_behaviors.dm` |
| `SSidlenpcpool` | processing | Processing loops | `/datum/controller/subsystem/processing/idlenpcpool` | `code/controllers/subsystem/idlenpcpool.dm` |
| `SSincone` | standard | Gameplay simulation | `/datum/controller/subsystem/incone` | `code/controllers/subsystem/processing/incone.dm` |
| `SSinput` | standard | UI, comms and admin | `/datum/controller/subsystem/input` | `code/controllers/subsystem/input.dm` |
| `SSipintel` | standard | Gameplay simulation | `/datum/controller/subsystem/ipintel` | `code/controllers/subsystem/ipintel.dm` |
| `SSjob` | standard | Round flow and player lifecycle | `/datum/controller/subsystem/job` | `code/controllers/subsystem/job.dm` |
| `SSlanguage` | standard | Gameplay simulation | `/datum/controller/subsystem/language` | `code/controllers/subsystem/language.dm` |
| `SSlibrarian` | standard | Gameplay simulation | `/datum/controller/subsystem/librarian` | `code/controllers/subsystem/librarian.dm` |
| `SSlighting` | standard | World generation and map state | `/datum/controller/subsystem/lighting` | `code/controllers/subsystem/lighting.dm` |
| `SSlobbymenu` | standard | Round flow and player lifecycle | `/datum/controller/subsystem/lobbymenu` | `code/controllers/subsystem/lobby.dm` |
| `SSmachines` | standard | Gameplay simulation | `/datum/controller/subsystem/machines` | `code/controllers/subsystem/machines.dm` |
| `SSmapgen` | processing | Processing loops | `/datum/controller/subsystem/processing/mapgen` | `code/controllers/subsystem/processing/mapgen.dm` |
| `SSmapping` | standard | Boot and infrastructure | `/datum/controller/subsystem/mapping` | `code/controllers/subsystem/mapping.dm` |
| `SSmatthios_mobs` | standard | Gameplay simulation | `/datum/controller/subsystem/matthios_mobs` | `code/controllers/subsystem/mobs/matthios.dm` |
| `SSmaturity_guard` | standard | Round flow and player lifecycle | `/datum/controller/subsystem/maturity_guard` | `modular/code/modules/maturity-prompt/code/maturity_subsystem.dm` |
| `SSmerchant` | standard | Gameplay simulation | `/datum/controller/subsystem/merchant` | `code/controllers/subsystem/merchant.dm` |
| `SSmigrants` | standard | Round flow and player lifecycle | `/datum/controller/subsystem/migrants` | `code/controllers/subsystem/migrants.dm` |
| `SSminecarts` | movement | Movement and pathing | `/datum/controller/subsystem/movement/minecarts` | `code/controllers/subsystem/movement/minecarts.dm` |
| `SSminor_mapping` | standard | Boot and infrastructure | `/datum/controller/subsystem/minor_mapping` | `code/controllers/subsystem/minor_mapping.dm` |
| `SSmobs` | standard | Gameplay simulation | `/datum/controller/subsystem/mobs` | `code/controllers/subsystem/mobs.dm` |
| `SSmobs_dead` | standard | Gameplay simulation | `/datum/controller/subsystem/mobs_dead` | `code/controllers/subsystem/mobs.dm` |
| `SSmood` | processing | Processing loops | `/datum/controller/subsystem/processing/mood` | `code/controllers/subsystem/moods.dm` |
| `SSmouse_entered` | standard | Gameplay simulation | `/datum/controller/subsystem/mouse_entered` | `code/controllers/subsystem/mouse_entered.dm` |
| `SSmousecharge` | processing | Processing loops | `/datum/controller/subsystem/processing/mousecharge` | `code/controllers/subsystem/processing/mousecharge.dm` |
| `SSmove_manager` | standard | Movement and pathing | `/datum/controller/subsystem/move_manager` | `code/controllers/subsystem/movement/move_manager.dm` |
| `SSmovement` | standard | Movement and pathing | `/datum/controller/subsystem/movement` | `code/controllers/subsystem/movement/movement_loop.dm` |
| `SSnightshift` | standard | Gameplay simulation | `/datum/controller/subsystem/nightshift` | `code/controllers/subsystem/nightshift.dm` |
| `SSnpcpool` | standard | Gameplay simulation | `/datum/controller/subsystem/npcpool` | `code/controllers/subsystem/npcpool.dm` |
| `SSobj` | processing | Processing loops | `/datum/controller/subsystem/processing/obj` | `code/controllers/subsystem/processing/obj.dm` |
| `SSoutdoor_effects` | standard | World generation and map state | `/datum/controller/subsystem/outdoor_effects` | `code/controllers/subsystem/particle_weather_outdoors.dm` |
| `SSoverlays` | standard | Gameplay simulation | `/datum/controller/subsystem/overlays` | `code/controllers/subsystem/overlays.dm` |
| `SSParticleWeather` | standard | World generation and map state | `/datum/controller/subsystem/ParticleWeather` | `code/controllers/subsystem/particle_weather.dm` |
| `SSpathfinder` | standard | World generation and map state | `/datum/controller/subsystem/pathfinder` | `code/controllers/subsystem/pathfinder.dm` |
| `SSpersistence` | standard | Gameplay simulation | `/datum/controller/subsystem/persistence` | `code/controllers/subsystem/persistence.dm` |
| `SSping` | standard | Boot and infrastructure | `/datum/controller/subsystem/ping` | `code/controllers/subsystem/ping.dm` |
| `SSpollutants` | processing | Processing loops | `/datum/controller/subsystem/processing/pollutants` | `code/controllers/subsystem/processing/pollutants.dm` |
| `SSpollution` | standard | World generation and map state | `/datum/controller/subsystem/pollution` | `code/controllers/subsystem/pollution.dm` |
| `SSprocessing` | standard | Gameplay simulation | `/datum/controller/subsystem/processing` | `code/controllers/subsystem/processing/processing.dm` |
| `SSprojectiles` | processing | Processing loops | `/datum/controller/subsystem/processing/projectiles` | `code/controllers/subsystem/processing/projectiles.dm` |
| `SSradio` | standard | UI, comms and admin | `/datum/controller/subsystem/radio` | `code/controllers/subsystem/radio.dm` |
| `SSregionthreat` | standard | Gameplay simulation | `/datum/controller/subsystem/regionthreat` | `code/controllers/subsystem/rogue/regional_threat/regional_threat.dm` |
| `SSrivers` | standard | World generation and map state | `/datum/controller/subsystem/rivers` | `code/controllers/subsystem/rivers.dm` |
| `SSrogueinfo` | standard | Gameplay simulation | `/datum/controller/subsystem/rogueinfo` | `code/controllers/subsystem/rogue/rogue_info_subsystem.dm` |
| `SSroguemachine` | processing | Processing loops | `/datum/controller/subsystem/processing/roguemachine` | `code/controllers/subsystem/rogue/roguemachine.dm` |
| `SSroguerot` | processing | Processing loops | `/datum/controller/subsystem/processing/roguerot` | `code/controllers/subsystem/rogue/roguerot.dm` |
| `SSrole_class_handler` | standard | Round flow and player lifecycle | `/datum/controller/subsystem/role_class_handler` | `code/controllers/subsystem/rogue/role_class_handler/role_class_handler.dm` |
| `SSrunechat` | standard | UI, comms and admin | `/datum/controller/subsystem/runechat` | `code/controllers/subsystem/runechat.dm` |
| `SSserver_maint` | standard | Boot and infrastructure | `/datum/controller/subsystem/server_maint` | `code/controllers/subsystem/server_maint.dm` |
| `SSsex` | processing | Processing loops | `/datum/controller/subsystem/processing/sex` | `modular/code/controllers/subsystem/processing/sex.dm` |
| `SSskills` | standard | Gameplay simulation | `/datum/controller/subsystem/skills` | `code/controllers/subsystem/skills.dm` |
| `SSsoundloopers` | standard | Gameplay simulation | `/datum/controller/subsystem/soundloopers` | `code/controllers/subsystem/rogue/soundloopers.dm` |
| `SSsounds` | standard | Gameplay simulation | `/datum/controller/subsystem/sounds` | `code/controllers/subsystem/sounds.dm` |
| `SSspatial_grid` | standard | World generation and map state | `/datum/controller/subsystem/spatial_grid` | `code/controllers/subsystem/spatial_gridmap.dm` |
| `SSstatpanel` | standard | UI, comms and admin | `/datum/controller/subsystem/statpanel` | `code/controllers/subsystem/processing/stat_cache.dm` |
| `SSstickyban` | standard | Boot and infrastructure | `/datum/controller/subsystem/stickyban` | `code/controllers/subsystem/stickyban.dm` |
| `SSsun` | standard | World generation and map state | `/datum/controller/subsystem/sun` | `code/controllers/subsystem/sun.dm` |
| `SStgui` | standard | UI, comms and admin | `/datum/controller/subsystem/tgui` | `code/controllers/subsystem/tgui.dm` |
| `SSthrowing` | standard | Gameplay simulation | `/datum/controller/subsystem/throwing` | `code/controllers/subsystem/throwing.dm` |
| `SSticker` | standard | Round flow and player lifecycle | `/datum/controller/subsystem/ticker` | `code/controllers/subsystem/ticker.dm` |
| `SStime_track` | standard | Gameplay simulation | `/datum/controller/subsystem/time_track` | `code/controllers/subsystem/time_track.dm` |
| `SStimer` | standard | Gameplay simulation | `/datum/controller/subsystem/timer` | `code/controllers/subsystem/timer.dm` |
| `SStitle` | standard | Gameplay simulation | `/datum/controller/subsystem/title` | `code/controllers/subsystem/title.dm` |
| `SStracks` | processing | Processing loops | `/datum/controller/subsystem/processing/tracks` | `code/controllers/subsystem/tracks.dm` |
| `SStramprocess` | processing | Processing loops | `/datum/controller/subsystem/processing/tramprocess` | `code/controllers/subsystem/processing/tram.dm` |
| `SStraumas` | standard | Gameplay simulation | `/datum/controller/subsystem/traumas` | `code/controllers/subsystem/traumas.dm` |
| `SStreasury` | standard | Gameplay simulation | `/datum/controller/subsystem/treasury` | `code/controllers/subsystem/rogue/treasury.dm` |
| `SStreesetup` | standard | Gameplay simulation | `/datum/controller/subsystem/treesetup` | `code/controllers/subsystem/treestuff.dm` |
| `SStriumphs` | standard | Round flow and player lifecycle | `/datum/controller/subsystem/triumphs` | `code/controllers/subsystem/rogue/triumphs/triumphs.dm` |
| `SSvis_overlays` | standard | Gameplay simulation | `/datum/controller/subsystem/vis_overlays` | `code/controllers/subsystem/vis_overlays.dm` |
| `SSvote` | standard | UI, comms and admin | `/datum/controller/subsystem/vote` | `code/controllers/subsystem/vote.dm` |
| `SSwardrobe` | standard | Gameplay simulation | `/datum/controller/subsystem/wardrobe` | `code/controllers/subsystem/wardrobe.dm` |
| `SSwaterlevel` | standard | World generation and map state | `/datum/controller/subsystem/waterlevel` | `code/controllers/subsystem/rogue/water_level.dm` |
| `SSweather` | standard | World generation and map state | `/datum/controller/subsystem/weather` | `code/controllers/subsystem/weather.dm` |
| `SSwet_floors` | processing | Processing loops | `/datum/controller/subsystem/processing/wet_floors` | `code/controllers/subsystem/processing/wet_floors.dm` |
