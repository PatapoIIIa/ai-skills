# Debug Routes

| Symptom | Open first |
|---|---|
| Blank/white TGUI, all browser windows fail | tgui_guide.md + $ss13-tgui runtime triage |
| TGUI asset/image missing | tgui_guide.md; check /datum/asset registration and resolveAsset mapping |
| Action button does nothing | backend ui_act in owning DM file; validate params and return TRUE |
| Combat chain breaks | combat_signal_map.md; code/_onclick/**; rogueweapon files |
| Movement/collision wrong | movement_signal_map.md; code/controllers/subsystem/movement/** |
| Spell/miracle/cooldown wrong | spell_signal_map.md; spell files and action datums |
| Family tree UI/data wrong | modular_twilight_axis/familytree_module/** |
| Manor panel values/assets wrong | modular_twilight_axis/manors/** plus ManorPanel.tsx |
| Origin/lore choice wrong | modular_twilight_axis/lore/** and preferences overlay |
| Desert map/content wrong | modular_deserttown/** and _maps/map_files/deserttown/** |
| Process loop freezes without runtimes | processing_hazards.md then subsystem owner |
| Runtime qdel/harddel/ref error | runtime_errors.md then coding_standards.md |
