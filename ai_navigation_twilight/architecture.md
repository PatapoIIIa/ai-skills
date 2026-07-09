# Architecture

Generated on 2026-07-09 from `C:/Axis/Twilight-Axis`.

Twilight-Axis is a RogueTown/Vanderlin-family BYOND DM codebase. The project manifest is `roguetown.dme` with 4176 include lines. Core code is in `code/**`; fork content is layered mostly through `modular_twilight_axis/**`, with `modular_deserttown/**` for desert map/content and legacy `modular/**` for older modular additions.

## Include Roots

| Top include root | Includes | First line | Last line |
|---|---|---|---|
| code | 3470 | 13 | 3482 |
| modular_twilight_axis | 544 | 3595 | 4149 |
| modular | 107 | 3488 | 3594 |
| modular_deserttown | 47 | 4138 | 4185 |
| interface | 5 | 3483 | 3487 |
| _maps | 3 | 10 | 12 |


## Runtime Backbone

- World startup begins in `code/world.dm` and controller setup in `code/controllers/master.dm`.
- Subsystems live under `code/controllers/subsystem/**` plus modular declarations.
- Atom initialization is owned by `SSatoms` in `code/controllers/subsystem/atoms.dm`.
- TGUI is owned by `SStgui` in `code/controllers/subsystem/tgui.dm` and `code/modules/tgui/**`.
- Asset delivery is owned by `SSassets` and `code/modules/asset_cache/**`.

## Domain Layers

| System | Open first | Runtime owner / next map |
|---|---|---|
| TGUI | code/modules/tgui, code/controllers/subsystem/tgui.dm, tgui/packages/tgui/interfaces, modular_twilight_axis/manors/code/manor_tgui.dm | SStgui, SSassets |
| Twilight overlay | modular_twilight_axis, roguetown.dme | see subsystem_map.md |
| Desert overlay | modular_deserttown, _maps/map_files/deserttown | see subsystem_map.md |
| Legacy modular | modular, roguetown.dme | see subsystem_map.md |
| Family tree | modular_twilight_axis/familytree_module | SSfamilytree |
| Manors | modular_twilight_axis/manors | see subsystem_map.md |
| Origin/lore | modular_twilight_axis/lore, modular_twilight_axis/code/modules/client/preferences.dm | see subsystem_map.md |
| Cards/chess | modular_twilight_axis/code/cards, modular_twilight_axis/code/chess | see subsystem_map.md |
| Vampires | modular_twilight_axis/code/modules/vampire_neu, code/modules/vampire_neu | see subsystem_map.md |
| ERP/sexcon | modular_twilight_axis/code/modules/erp_system, modular_twilight_axis/code/datums/sexcon, modular/code/controllers/subsystem/processing/sex.dm | see subsystem_map.md |
| Firearms | modular_twilight_axis/firearms | see subsystem_map.md |
| Artillery | modular_twilight_axis/awful_artillery | see subsystem_map.md |
| Church classes | modular_twilight_axis/church_classes | see subsystem_map.md |
| Spells | code/modules/spells, modular_twilight_axis/code/modules/spells, modular_twilight_axis/code/modules/spell | see subsystem_map.md |
| Combat | code/_onclick, code/game/objects/items/rogueweapons, modular_twilight_axis/code/game/objects/items/rogueweapons | see subsystem_map.md |
| Movement | code/controllers/subsystem/movement, code/__DEFINES/movement.dm, modular_twilight_axis/code/modules/mob/living/carbon/human/table_crawl.dm | SSmovement, SSmove_manager, movement subsystems |
| Economy/trade | code/controllers/subsystem/rogue/economy, code/controllers/subsystem/rogue/merchant_trade.dm, modular_twilight_axis/code/modules/roguetown/roguemachine | SSeconomy, SSmerchant_trade, treasury/merchant subsystems |
| Mapping/world | _maps, code/controllers/subsystem/mapping.dm, code/controllers/subsystem/dungeon_generator.dm, modular_twilight_axis/code/controllers/subsystem/automapper_subsystem.dm | SSmapping, SSdungeon_generator, SSautomapper |
| Visuals/icons | icons, code/controllers/subsystem/overlays.dm, code/controllers/subsystem/vis_overlays.dm, code/__HELPERS/icons.dm | see subsystem_map.md |
