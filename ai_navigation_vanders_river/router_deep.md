# Router — Extended Reference

Open this file only if the dispatch table in `router.md` did not resolve the task, or the task involves performance or timing.

---

## Budget

- Open exactly 1 helper first.
- Then open up to 2 source files.
- Check `modular_rmh` on the same branch.
- Before editing medium/high/unknown-risk work, stop and get human approval.
- For whole-loop stalls with no runtimes, do a blocking-call sweep before blaming load.
- Escalate only if unresolved.

## Engine Constraints Quick Reference

When a task touches performance, timing, or visual systems, apply this chain before writing code:

1. **What is the engine limit?** → `ai_navigation/engine_limits.md`
2. **Does my pattern trigger a known hazard?** → `ai_navigation/performance_gotchas.md`
3. **Which subsystem owns the budget?** → `ai_navigation/subsystem_map.md` or `ai_navigation/runtime_flow.md`

Key constraints (memorise these, don't open files just for them):
- `world.cpu ≥ 100` = server overtime; any new per-tick work makes this worse.
- Clients send **1 command/tick** max; `tick_lag` controls precision vs CPU cost.
- Infinite loops without `sleep()` are auto-aborted — do not rely on this.
- `overlays +=` / `overlays -=` on many atoms per tick → Appearance accumulation + network flood.
- After any `sleep()`, all object references must be null-checked before use.
- Do **not** iterate `world.contents` while creating or destroying objects.
