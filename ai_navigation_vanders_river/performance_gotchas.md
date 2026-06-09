# Performance Gotchas

Situation-indexed hazards derived from the BYOND/Dream Maker Designer's Guide. Each entry is a concrete scenario that causes server slowdown or correctness failures.

Read `engine_limits.md` first for the underlying numbers. This file answers "what specific code patterns trigger those limits?"

---

## 1. Infinite Loop Without a Sleep → World Lockup

**Situation:** A `for(;;)` or `while(1)` loop that never calls `sleep()`, `spawn()`, or any other yielding instruction.

**Effect:** The single-threaded server cannot process any other procedure or player input until the loop exits. The engine's **automatic abort** will eventually kill the procedure, but not before causing a visible freeze.

**Fix:** Any long-running background loop must `sleep(N)` inside its body. Use the subsystem `fire()` / `process()` pattern instead of raw loops in gameplay code.

**Repo anchor:** `code/controllers/subsystem.dm` → `fire()` is the correct scheduling unit for recurring work. See `ai_navigation/subsystem_map.md` for the full subsystem list.

---

## 2. Looping Over `world.contents` While Mutating It → Undefined Behavior

**Situation:** Iterating `for(X in world.contents)` while simultaneously creating (`new`) or deleting (`del`) objects.

**Effect:** `world.contents` is explicitly excluded from the engine's "copy the list at loop start" protection. Results are unpredictable — objects may be skipped or double-processed.

**Fix:** Take an explicit temporary copy before iterating: `var/list/snapshot = world.contents.Copy()`, then loop over `snapshot`.

**Repo anchor:** Any proc that spawns or deletes atoms inside an area-wide sweep. Common in mapgen (`code/modules/mapping/**`, `code/modules/procedural_mapping/**`) and round-end cleanup.

---

## 3. Sleeping Inside a Server-Callback Proc → Silent No-Op Delay

**Situation:** Calling `sleep()` inside procs that the engine calls directly: `Enter()`, `Exit()`, `Login()`, `Logout()`, `New()` on atoms, etc.

**Effect:** The engine immediately resumes as if the proc returned — the intended delay does **not** block the triggering action. This is not an error; it is engine behavior. The remaining code after the sleep runs later but the server-side action (e.g. the mob moving) has already completed.

**Fix:** Use `spawn()` to detach delayed work from server callbacks. Never expect `sleep()` inside `Enter`/`Exit`/`Login` to postpone the event itself.

**Repo anchor:** `code/game/atoms_movable.dm` (Move/Enter/Exit chains), `code/modules/mapping/**` (area enter hooks). Also relevant in signal handlers — see `ai_navigation/signal_map.md`.

---

## 4. Not Null-Checking Object References After a Sleep → Proc Crash

**Situation:** A proc stores a reference to an object, calls `sleep()`, then uses the reference after resuming without checking it.

**Effect:** The object may have been deleted during the sleep. Accessing a variable or proc on a null (deleted-object) reference crashes the procedure and logs a runtime to `world.log`.

**Fix:** After every `sleep`, treat all object references as potentially null. Pattern:
```dm
sleep(10)
if(!istype(src)) return   // src auto-cancels; this is for other refs
if(!myobj) return
```

**Repo anchor:** Common in status effect procs (`code/datums/status_effects/**`), timed combat effects, and any `do_after`-style pattern in `code/__HELPERS/**`.

---

## 5. `list + list2` in a Tight Loop → Repeated Allocation

**Situation:** Using `mylist = mylist + other` (the `+` operator) inside a loop or a frequently-called proc.

**Effect:** Each `+` creates a **new list object**. In a loop this allocates N new lists, all of which the GC must eventually reclaim. On a busy server this adds GC pressure between ticks.

**Fix:** Use `mylist += other` (in-place append) whenever you do not need to preserve the original list. Accumulate into a pre-allocated list and return it once.

**Repo anchor:** Spell effect resolution (`code/datums/components/**`), reagent chain processing (`code/modules/reagents/**`), anywhere a list of targets is built iteratively.

---

## 6. Broadcasting to `world` or `view()` With Heavy Data → Bandwidth Spike

**Situation:** `world << large_output` or sending large sound/icon resources to many clients at once.

**Effect:** Resources are automatically transmitted to all clients that don't have them cached. Sending many large files simultaneously creates a bandwidth spike that manifests as network lag (distinct from server CPU lag).

**Fix:** Prefer targeted sends. Pre-load resources during init if they will be needed at runtime. Use `world.cpu` vs. perceived lag to distinguish network lag from CPU lag.

**Repo anchor:** `code/modules/tgui/**` (UI updates to all clients), `code/modules/visual_ui/**` (visual effect broadcasts), sound subsystem.

---

## 7. Excessive Unique Overlay Combinations → Appearance Object Accumulation

**Situation:** Dynamically generating overlays with many varying parameters per mob or object (e.g. per-player color-shifted icons, animated overlays that change every tick for many entities).

**Effect:** Each unique combination of icon/state/color/transform registers a distinct Appearance object in the engine. These accumulate in server memory. Every time an Appearance changes on a visible atom, the new state must be sent over the network to every client that can see it. High overlay churn on many entities = high memory + high bandwidth simultaneously.

**Fix:** Reuse Appearance objects by caching icon references rather than recomputing them. Limit per-tick overlay changes. Prefer icon state changes (`icon_state =`) over overlay add/remove cycling. Batch overlay updates and only apply them at the end of the owning proc.

**Repo anchor:** `modular_rmh/` overlay and clothing systems; `code/modules/visual_ui/**`; any system that calls `overlays +=` or `overlays -=` in a loop or per-tick proc.

---

## 8. Decreasing `tick_lag` Too Far → Counter-Productive CPU Overhead

**Situation:** Setting `world.tick_lag` to a very small value (e.g. `0.1` or lower) to get more precise timings.

**Effect:** The per-tick scheduling overhead grows with tick frequency. Below a viable threshold, the overhead itself consumes more CPU than the actual game logic, making `world.cpu` spike and the server run *slower* in absolute terms.

**Fix:** Profile `world.cpu` before changing `tick_lag`. The project's master controller (`code/controllers/master.dm`) manages tick budget — consult `ai_navigation/runtime_flow.md` before adjusting scheduler timing.

---

## 9. `view()` with a Large Range on Many Mobs → Spatial Query Flood

**Situation:** Calling `view(10)` or `range(10)` in a proc that fires every tick for every mob (e.g. inside a subsystem `process()` that iterates all living mobs).

**Effect:** Even though `view()` is a built-in VM instruction, calling it at tick frequency for hundreds of mobs multiplies its cost. The 21×21 grid at range 10 is roughly 4× the tile count of the default 11×11.

**Fix:** Cache the view list when the mob has not moved. Compute it only on movement or at a longer interval using a lower-priority subsystem. Use `range()` (ignores opacity) instead of `view()` if line-of-sight is not needed.

**Repo anchor:** NPC AI subsystem, spell AoE code (`code/datums/spells/**`), combat detection procs.

---

## 10. Bitwise Operations on Values Outside 0–65535 → Silent Truncation

**Situation:** Using `&`, `|`, `^`, `~`, or bit-shift operators on numbers outside the 16-bit unsigned range.

**Effect:** Values are silently truncated to 16 bits. No runtime error is thrown. Flag checks on large integers will produce wrong results without any warning.

**Fix:** Keep all bitwise flag values within 0–65535. The project's flag defines in `code/__DEFINES/` already do this — do not add new flags that require more than 16 bits without switching to a different mechanism.

---

*Cross-references: → `engine_limits.md` for the underlying numbers behind each hazard. → `processing_hazards.md` for subsystem-level freeze diagnosis. → `runtime_flow.md` for scheduler and tick-budget context. → `visuals_guide.md` for full overlay/plane/appearance system details. → `coding_standards.md` for appearance caching patterns and harddel fixes.*
