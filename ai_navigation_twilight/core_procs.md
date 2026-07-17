# Core Procs

| Proc family | Use when | Notes |
|---|---|---|
| Initialize(mapload) / LateInitialize() | mapload/setup behavior | Read SSatoms and neighboring types. |
| Destroy() / qdel() | cleanup/ref leak/harddel | Unregister signals and stop processing. |
| process() / fire() | subsystem or processing behavior | No blocking waits inside hot paths. |
| ui_interact, ui_data, ui_static_data, ui_assets, ui_act | TGUI | Bind with $ss13-tgui. |
| attackby, attack_hand, afterattack, click handlers | interactions/combat | Check combat signal map. |
| RegisterSignal, UnregisterSignal, SEND_SIGNAL | DCS behavior | Check signal_map.md. |
| do_after | timed player actions | Safe in interaction procs; suspicious in process/fire. |
