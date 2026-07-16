# Performance Gotchas

Updated 2026-07-16. The *universal* hazards (infinite loops without sleep, `world.contents` mutation during iteration, stale refs after sleep, `list + list` allocation, appearance churn, tick_lag tuning, view() flooding, bitwise/precision limits) are covered — with verified numbers — by the **byond-ss13-coding** skill: `references/performance.md` and `references/dm-language-and-runtime.md`. Read those for the mechanics; this file maps each hazard class to *this repo's* likely hot spots.

| Hazard class (see skill) | Where it bites in this repo |
|---|---|
| Long loops / init sweeps without yielding | mapgen (`code/modules/mapping/**`, `code/modules/procedural_mapping/**`), round-end cleanup |
| Stale references after `sleep`/`do_after` | status effects (`code/datums/status_effects/**`), timed combat effects, `do_after`-style helpers in `code/__HELPERS/**` |
| List allocation in tight loops | spell effect resolution (`code/datums/components/**`), reagent chains (`code/modules/reagents/**`), iterative target-list builds |
| Broadcast/bandwidth spikes | `code/modules/tgui/**` mass UI updates, `code/modules/visual_ui/**` effect broadcasts, sound subsystem |
| Appearance/overlay churn | `modular_rmh/` overlay and clothing systems; `code/modules/visual_ui/**`; any per-tick `overlays +=`/`-=` |
| Per-tick spatial queries (`view()`/`range()`) on many mobs | NPC AI subsystem, spell AoE (`code/datums/spells/**`), combat detection procs |
| Scheduler timing changes | `code/controllers/master.dm` owns tick budget — consult `runtime_flow.md` before touching `tick_lag`/`fps` |

Stonekeep-lineage caution (applies to this family): weather/outdoor-lighting systems that scan whole z-levels per pass and NPC populations built from full `/mob/living/carbon/human` instances are known dominant cost centers — profile those first when the server lags (details: byond-ss13-coding `references/repository-profiles.md`).

*Cross-references: → `engine_limits.md` (pointer to verified engine numbers). → `processing_hazards.md` for subsystem-level freeze diagnosis. → `runtime_flow.md` for scheduler context. → `visuals_guide.md` for the overlay/plane system.*
