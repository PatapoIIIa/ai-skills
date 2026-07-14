# Entrypoints

Generated on 2026-07-09. Match the user's keyword to one row, open the listed files/dirs, then verify with source.

| Keyword / system | Open first | Runtime owner / next map |
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
| Siege / worldsiege / skeleton-goblin raid | code/datums/world_traits/sieges.dm, code/modules/events/raids/skeleton.dm, code/modules/events/raids/goblin.dm, code/modules/events/omens/skellysiege.dm, code/modules/jobs/job_types/roguetown/other/siege_skeleton.dm, code/modules/jobs/job_types/roguetown/other/goblin.dm | SSmapping.active_world_traits (add_world_trait/has_world_trait); ghost join via mob/dead/observer/proc/horde_respawn |
| Economic blockade (trade region raided) | code/controllers/subsystem/rogue/economy/blockade_lifecycle.dm, code/modules/roguetown/roguestock/blockade.dm, code/modules/roguetown/roguemachine/questing/types/kill/quest_blockade_defense.dm, code/modules/roguetown/roguemachine/questing/items/quest_scroll_blockade.dm, code/__DEFINES/economy/internal_trade_and_quests.dm (BLOCKADE_*) | SSeconomy (datum/economic_region.is_region_blockaded); cleared via 3-wave Blockade Defense quest writ |
