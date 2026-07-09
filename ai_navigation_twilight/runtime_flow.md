# Runtime Flow

| Flow | Typical chain |
|---|---|
| World bootstrap | code/world.dm -> code/controllers/master.dm -> subsystem initialization |
| Subsystem owner lookup | subsystem_map.md -> owner file -> fire/process/init procs |
| Atom init | SSatoms in code/controllers/subsystem/atoms.dm -> Initialize/LateInitialize |
| Round flow | SSticker in code/controllers/subsystem/ticker.dm -> jobs/roles/antags |
| Input to action | client/input -> click/verb/action -> owner proc -> signals/components |
| Signal reaction | SEND_SIGNAL site -> signal_map.md -> RegisterSignal listeners |
| TGUI update | ui_interact -> SStgui.try_update_ui -> ui_data/static/assets -> ui_act -> SStgui.update_uis |
| Asset delivery | /datum/asset -> SSassets transport -> asset/mappings -> resolveAsset |
