# System Dependencies

| System | Depends on / hands off to | Primary paths |
|---|---|---|
| TGUI | SSassets, client browser, tgui bundle | code/modules/tgui/**, tgui/packages/** |
| Assets/CDN | config resources, /datum/asset, tgui asset middleware | code/modules/asset_cache/**, config/resources.txt |
| Family tree | mob login/logout/death/revive/job signals | modular_twilight_axis/familytree_module/** |
| Manors | mind ownership, workstations, TGUI assets | modular_twilight_axis/manors/** |
| Origin/lore | preferences, species/language names, lore datums | modular_twilight_axis/lore/** |
| Combat | click handlers, rogue weapons, mob/item signals | code/_onclick/**, rogueweapon dirs |
| Spells | actions, cooldowns, status effects, COMSIG hooks | code/modules/spells/**, Twilight spell overlays |
| Movement | movement subsystems, bump/pre-move signals | code/controllers/subsystem/movement/** |
| Economy/trade | treasury, merchant trade, roguemachine extensions | code/controllers/subsystem/rogue/** |
| Mapping/world | SSmapping, dungeon generator, automapper | _maps/**, mapping/automapper subsystems |
