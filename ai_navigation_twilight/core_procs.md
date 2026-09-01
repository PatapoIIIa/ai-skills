# Core Procs

| Proc family | Use when | Notes |
|---|---|---|
| Initialize(mapload) / LateInitialize() | mapload/setup behavior | Read SSatoms and neighboring types. |
| Destroy() / qdel() | cleanup/ref leak/harddel | Unregister signals and stop processing. |
| process() / fire() | subsystem or processing behavior | No blocking waits inside hot paths. |
| ui_interact, ui_data, ui_static_data, ui_assets, ui_act | TGUI | Bind with $ss13-tgui. |
| attackby, attack_hand, afterattack, click handlers | interactions/combat | Check combat signal map. |
| RegisterSignal, UnregisterSignal, SEND_SIGNAL | DCS behavior | Check signal_map.md. |
| do_after | timed player actions | **Blocking**: a `while` + `stoplag()` loop that sleeps the caller chain for the whole duration — hence fine in interaction procs, wrong in process/fire or a signal handler. It already re-checks user/target loc, held item and incapacitation each poll; relax via `timed_action_flags`, don't re-implement. Depth: `$byond-ss13-coding` (ss13-architecture.md). |
