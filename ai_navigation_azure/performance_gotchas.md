# Performance Gotchas

Azure-Peak performance hazards. Read `ai_navigation/engine_limits.md` first for the underlying BYOND limits.

## 1. Infinite Loop Without Yielding

**Situation:** A `for(;;)` or `while(1)` loop never calls `sleep()`, `spawn()`, `CHECK_TICK`, or a subsystem pause path.

**Effect:** The single-threaded server cannot process other procs or player input until the loop exits or the engine aborts it.

**Fix:** Use subsystem `fire()` / `process()` loops for recurring work. In large one-shot loops, follow local patterns with `CHECK_TICK` or subsystem `MC_TICK_CHECK` where the surrounding code already uses them.

**Repo anchor:** `code/controllers/subsystem.dm`, `code/controllers/master.dm`, `code/__DEFINES/_tick.dm`, `code/__DEFINES/MC.dm`.

## 2. Mutating `world.contents` While Iterating

**Situation:** Iterating `for(X in world.contents)` while creating or deleting atoms.

**Effect:** `world.contents` is not protected by the engine's normal list-copy iteration behavior. Objects can be skipped or processed twice.

**Fix:** Copy to a temporary list before mutating: `var/list/snapshot = world.contents.Copy()`.

**Repo anchor:** map cleanup, mapgen, admin/debug sweeps, and broad atom scans.

## 3. Sleeping Inside Server Callback Procs

**Situation:** Calling `sleep()` inside engine-called procs such as `Enter()`, `Exit()`, `Login()`, `Logout()`, `New()`, movement hooks, or signal handlers that are expected to return a gate value.

**Effect:** The triggering server action continues; delayed code resumes later against possibly changed state.

**Fix:** Use timers/callbacks for delayed side effects. Do not rely on `sleep()` to block movement, entry, exit, or login.

**Repo anchor:** `code/game/atoms_movable.dm`, `code/modules/mob/mob_movement.dm`, `ai_navigation/movement_signal_map.md`.

## 4. Not Null-Checking After Delay

**Situation:** A proc stores object refs, yields or schedules delayed work, then uses those refs without checking deletion.

**Effect:** The object may be qdeleted by the time the code resumes.

**Fix:** Re-check refs with local repo macros/patterns such as `QDELETED(x)`, `QDEL_NULL(x)`, or simple null/`istype` checks before use.

**Repo anchor:** `code/__DEFINES/qdel.dm`, `code/controllers/subsystem/garbage.dm`, timed spell/status/component code.

## 5. Repeated List Allocation in Tight Loops

**Situation:** Using `list_a = list_a + list_b` or building new temporary lists inside hot loops.

**Effect:** Repeated allocation increases GC pressure.

**Fix:** Use in-place mutation (`+=`, `|=`, `Cut`, lazy-list helpers where already used). Prefer `var/static/list` for constant lookup tables that are reused across calls.

**Repo anchor:** `code/datums/ai/**`, `code/modules/spells/**`, `code/modules/reagents/**`, `code/game/turfs/**`.

## 6. Untyped or Slow Iteration in Hot Paths

**Situation:** Hot loops iterate broad lists without type information or repeat expensive casts.

**Effect:** BYOND pays more per iteration and may do unnecessary runtime checks.

**Fix:** Follow local style in hot paths: typed loops (`for(var/atom/movable/thing as anything in contents)` where the list is known), `var/static/list` caches for constant tables, and pre-filtered subsystem/global lists instead of broad scans.

**Repo anchor:** `code/game/turfs/turf.dm`, `code/datums/ai/_ai_controller.dm`, `code/controllers/master.dm`.

## 7. Missing `START_PROCESSING` / `STOP_PROCESSING` Pairing

**Situation:** A datum starts processing in a subsystem and fails to stop during cleanup.

**Effect:** Dead or inactive datums stay in processing lists, causing needless tick work or runtimes.

**Fix:** Pair `START_PROCESSING(Processor, Datum)` and `STOP_PROCESSING(Processor, Datum)` with `Destroy()`/state transitions. Do not manually mutate subsystem processing lists unless the local subsystem does so.

**Repo anchor:** `code/__DEFINES/MC.dm`, processing subsystem files under `code/controllers/subsystem/processing/**`.

## 8. Broadcasting Heavy Data to Many Clients

**Situation:** `world << large_output`, broad sound/resource sends, or UI updates that refresh too much state for all clients.

**Effect:** Bandwidth spikes look like client lag even if `world.cpu` is low.

**Fix:** Prefer targeted sends and smaller `ui_data`. Update only the state that changed.

**Repo anchor:** `code/modules/tgui/**`, `code/modules/tgui_input/**`, `code/modules/tgui_panel/**`, `code/modules/tgchat/**`, sound subsystems.

## 9. Excessive Unique Overlay Combinations

**Situation:** Dynamically generating overlays with many unique icon/state/color/transform combinations, especially per mob or per tick.

**Effect:** Each unique Appearance is tracked by the engine and may be sent to every observing client.

**Fix:** Cache appearance/icon state combinations. Prefer `icon_state` swaps over repeated overlay add/remove cycles. Batch overlay changes and apply once at the end of the owning proc.

**Repo anchor:** `code/controllers/subsystem/overlays.dm`, `code/controllers/subsystem/vis_overlays.dm`, `code/game/objects/effects/**`, `code/modules/clothing/**`, `modular/**`.

## 10. Large `view()` / `range()` Scans on Many Mobs

**Situation:** Calling `view(10)` or `range(10)` every tick for many mobs or AI controllers.

**Effect:** Spatial query cost multiplies quickly across mobs and ticks.

**Fix:** Cache results where movement has not changed. Use subsystem cadence, spatial grid helpers, or shorter ranges when line-of-sight is not needed.

**Repo anchor:** `code/datums/ai/**`, `code/controllers/subsystem/spatial_gridmap.dm`, spell AoE code.

## 11. Bitwise Operations Outside 16-Bit Assumptions

**Situation:** Adding new flags without checking the bitfield assumptions used by the repo.

**Effect:** BYOND bitwise operators can silently truncate values in unsafe ranges.

**Fix:** Use existing flag helpers/macros and define new flags near the owning `code/__DEFINES/**` file. Prefer existing `ENABLE_BITFIELD` / `DISABLE_BITFIELD` style where present.

**Repo anchor:** `code/__DEFINES/flags.dm`, `code/__DEFINES/**`.

Cross-references: `ai_navigation/processing_hazards.md`, `ai_navigation/runtime_flow.md`, `ai_navigation/visuals_guide.md`, `ai_navigation/coding_standards.md`.
