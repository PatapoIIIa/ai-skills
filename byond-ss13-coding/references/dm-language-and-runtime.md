# DM Language and BYOND Runtime

Engine-tier facts (tier 1). Sources are tagged: **[DM Ref]** = official DM Reference (byond.com/docs/ref; a local copy ships with every BYOND install — see source-index.md), **[tg]** = tgstation `.github/guides/`, **[dev]** = a statement by the BYOND engine's own developer on the official Discord (highest heuristic grade — see source-index.md for the sourcing method), **[community]** = a statement by another experienced Discord participant, corroborating but not authoritative on engine internals, **[heuristic]** = engineering inference, not documented. Anything untagged in this file is [DM Ref].

## Contents

- [Types and inheritance](#types-and-inheritance)
- [Procs, overrides, and arguments](#procs-overrides-and-arguments)
- [Return semantics and the dot variable](#return-semantics-and-the-dot-variable)
- [Truthiness and numbers](#truthiness-and-numbers)
- [Lists](#lists)
- [Type introspection](#type-introspection)
- [References and garbage collection](#references-and-garbage-collection)
- [sleep, spawn, waitfor — the async model](#sleep-spawn-waitfor--the-async-model)
- [The world tick](#the-world-tick)
- [Preprocessor and compile-time](#preprocessor-and-compile-time)
- [Built-in movement and spatial procs](#built-in-movement-and-spatial-procs)
- [animate() and visual timing](#animate-and-visual-timing)
- [Particles](#particles)
- [Common runtime errors and defenses](#common-runtime-errors-and-defenses)

## Types and inheritance

- A type path (`/obj/item/sword`) is a first-class value. Child types inherit vars and procs; any var or proc can be redefined downstream.
- **Types can be re-opened from any file.** The compiler merges every declaration of `/obj/item/foo` across the codebase into one type. This is why modular overlays work at all: adding a var, proc override, or subtype never *requires* editing the file that defined the parent. (The `tgstation-modular-content` skill builds its whole method on this.)
- `parent_type` can re-parent a type explicitly; the `::` operator reads another type's compile-time initial values (`/obj/item/fork::damage`) — supported in modern BYOND and preferred over `initial()` in definitions where the type is static. [tg STYLE]
- Everything non-atom derives from `/datum`. Atom hierarchy: `/atom` → `/area`, `/turf`, `/atom/movable` → `/obj`, `/mob`. Turfs and areas are special: they occupy the map permanently and are **not garbage collected** [DM Ref: garbage]. Areas are singletons shared by all their turfs.

## Procs, overrides, and arguments

- `..()` calls the parent implementation with the same arguments by default; passing arguments explicitly replaces them. Root procs marked `SHOULD_CALL_PARENT(TRUE)` (a SpacemanDMM lint, present in all six profiled repos) must have their override chains call `..()` — usually because the root sends a signal.
- Named arguments (`new /obj/thing(loc, is_red = TRUE)`) work on any call. tg style: name the Initialize argument after the var and assign with `src.var = var`. [tg STYLE]
- Default argument values are evaluated per call. Argument lists are accessible via `args` (a real list).
- Proc calls are dispatched **by name** through a per-type lookup table; call overhead is non-zero and the engine developer flags it as significant when a small proc is called very many times (e.g. sort comparators, per-item helpers in hot loops) [dev 2023-11-30, 2022-01-04]. Inlining or a macro is the escape hatch for proven hot cases — not a default style.
- A proc that runtimes does not crash its caller: execution continues at the call site, and the failed proc returns whatever `.` held at the moment of the error. Use this deliberately (set `.` to a safe fallback early in procs where callers can continue) and defensively (never assume a callee "must have" finished). [tg STANDARDS]

## Return semantics and the dot variable

- `.` is an implicit variable holding the proc's return value; bare `return` returns `.`.
- `. = ..()` then more code is the standard override pattern and is preferred over storing `..()` in a named var. [tg STYLE]
- Outside `. = ..()`, prefer explicit `return value` — implicit `.` returns from distant assignments are a classic source of "why did this return TRUE" bugs. [tg STANDARDS]

## Truthiness and numbers

- Falsy: `null`, `0`, `""` (empty string). Everything else — including negative numbers and `"0"` — is truthy.
- Numbers are 32-bit IEEE floats: integers are exact only up to 2^24 (16,777,216); beyond that, increments silently lose precision. [DM Ref: operators]
- **Bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`) operate on 24-bit integers, max value 16,777,215.** Bits above that are lost. Bit flags therefore fit in positions 0–23; `(1 << 24)` and up is a silent bug. [DM Ref — verified against the local reference; note this *corrects* older material that claims 16-bit/65535, which described ancient BYOND versions]
- `world.time` and all `sleep`/`spawn`/timer delays are in **deciseconds** (1/10 s). Use the codebase's `SECONDS`/`MINUTES` defines instead of raw numbers. [tg STYLE]

## Lists

- 1-based indexing. Reading or writing `list[i]` with `i` out of `1..length` throws a runtime error — it does not return null.
- `list + list2` allocates a new list; `list += list2` (or `Add`) mutates in place. In hot code the difference is real allocation pressure. [tg STANDARDS]
- **`for (var/x in mylist)` iterates over a copy of the list** — mutations during the loop don't affect the iteration (exception: looping `world` contents is not a copy). [DM Ref: for list] The `for (var/i in 1 to mylist.len)` form evaluates its bounds **once** at loop start; if the body changes the list length, the loop and the list disagree. [DM Ref]
- A typed loop var carries a hidden `istype` filter: `for (var/obj/item/I in contents)` silently skips nulls and non-matches. Use `as anything` to skip the check when the list is homogeneous — faster, and surfaces stray nulls as runtimes instead of hiding them. [tg STANDARDS]
- Associative lists are internally a hybrid of array + red-black tree; the array part preserves insertion order, and keyed lookup is an O(log n) tree search, not O(1) hashing. [dev 2023-12-17, 2024-01-31] Associative storage costs roughly 3× the memory of flat entries (tg cites 24 vs 8 bytes/entry). [tg STANDARDS]
- Special engine lists (`contents`, `overlays`, `underlays`, `vis_contents`) are managed by the engine and do not support associative values; they also behave unusually when copied — treat them as views, not plain lists.
- Declaring a list initializer in a var definition (`var/list/L = list()`) runs through a hidden per-object init proc and allocates even if never used; for rarely-used lists, allocate lazily (in `Initialize` or on first use — tg's `LAZYADD`/`LAZYINITLIST` helper family exists for exactly this). [tg STANDARDS]

## Type introspection

- `istype(x, /path)` — true for the path and descendants; `istype(null, anything)` is false. `ispath()`, `isnull()`, `islist()` and friends are cheap built-ins.
- `istype` itself is an **O(1) check** (the compiler/engine assigns depth-first IDs to the type tree at startup precisely so istype stays fast; the developer treats it as a hot-loop call) [dev 2024-05-18, 2026-07-07]. So the win from typecaches and `as anything` comes from removing *many* checks and the implicit filtering semantics, not because one istype is slow.
- `typesof(/path)` returns the path and all subtypes; `subtypesof` excludes the root. Both allocate a fresh list per call — never call them in a loop; cache the result.
- **Typecache pattern** (tg `typecacheof()` in `code/__HELPERS/_lists.dm`): build an associative list `type → TRUE` once, then test membership with `cache[x.type]` — O(log n) and no istype chain. Standard for "is this one of N types" checks in hot paths. [tg]
- `locate(ref_string)` resolves a text reference to an object. **Security:** never `locate(ref)` from user/href input without constraining it to a known list (`locate(ref) in contents`) — an unconstrained locate is an exploit vector. [tg STANDARDS]
- `locate()` cost gradient: by ref string or `tag` is fast (tag lookup is a small tree search); the slow forms are **type-path searches over the whole world or a very large list** [dev 2024-05-08, 2024-05-18]. Never `locate(/type) in world` in recurring code — keep a registry list.

## References and garbage collection

Verified against [DM Ref: garbage]:

- GC is reference counting. When the count hits zero, the object is freed. **Circular references are never collected** — a pair of datums pointing at each other leaks until something breaks the cycle or hard-deletes.
- Things that count as references: stored in a var; item in (or key of) a list; has a `tag`; on the map (always true for turfs); inside `contents`; inside `vis_contents`; a temporary value in a still-running proc (including a *sleeping* proc's `src`, args, and locals); a mob with a `key`; an image attached to an atom.
- `world.contents` does **not** count as a reference. Turfs and areas are not GC'd at all. Mobs with a key and anything with a non-empty `tag` are effectively immortal until those are cleared.
- On world shutdown, every object is torn down regardless of reference count [DM Ref: garbage] — this is an engine-level memory fact, not a promise that a codebase's own `Destroy()` proc runs for each one; don't rely on shutdown to fire cleanup side effects that live in `Destroy()`.
- `del obj` clears the obvious references first, then — if references remain — **searches all of memory** for the rest. That search is the "hard delete" cost, and it scales with world size (per the engine developer, scanning lists is roughly linear in the combined length of all lists in the game [dev 2023-11-15]). The gradient: references sitting in running/sleeping procs are cleared cheaply up front; references buried in lists are what makes the full search expensive [dev 2023-12-14]. This is why every profiled codebase uses `qdel()` + `Destroy()` (clean your own references, let refcounting do the free) and treats hard deletes as bugs. See ss13-architecture.md → Lifecycle.
- `\ref[x]` / weakref datums hold a non-counting reference; resolving may return null. Use for "cares about but doesn't own" relationships.

## sleep, spawn, waitfor — the async model

DM is single-threaded with cooperative scheduling; `sleep` and `spawn` are the yield points. Verified against [DM Ref: sleep, spawn, waitfor]:

- `sleep(0)` always yields, for as short a time as possible. `sleep(-1)` yields **only if** other scheduled events are backlogged — a cheap "be polite in a long computation" check (tg's `stoplag()`/`CHECK_TICK` build on this idea with tick-usage checks).
- `spawn(Delay) block` schedules a *copy* of the current proc to run the block. `spawn(0)` runs it right after currently-pending events (same tick if budget allows — do **not** model it as "costs a full tick"). `spawn(-1)` runs the block immediately and defers the code *after* the spawn instead. Plain (non-object) locals and args are *copied* into the spawned block — mutations don't propagate; objects and lists are shared.
- `set waitfor = 0` makes a proc return control to its caller at its first sleep, returning the current `.` value. This is how "fire and forget" procs are written without spawn. Modern default is `waitfor = 1`.
- Mechanically: `sleep` parks the *entire call stack* in the scheduler and resumes it outside-in; `spawn` parks a *copy* of the current proc [dev 2023-11-12]. A sleeping proc keeps `src` and all its locals alive (GC references). If `src` is deleted (hard delete), the engine replaces the scheduled proc's src and the proc ends immediately on wake [dev 2026-02-19]. If some *other* object your proc references is deleted, your local var becomes a dangling reference to a qdel'd object or null — **always re-validate references after any sleep or `do_after`**: `if (QDELETED(target)) return`.
- SS13 codebases forbid raw `sleep`/`spawn` in most contexts in favor of timers, callbacks, and processing subsystems — those are inspectable, cancellable, and budgeted. See ss13-architecture.md → Timers.

## The world tick

- `world.tick_lag` (deciseconds per tick) / `world.fps` set simulation rate. `world.cpu` = % of tick budget spent; sustained ≥100 means the server cannot finish a tick on time and timed events slip. `world.map_cpu` isolates the SendMaps share. [DM Ref: world vars]
- Tick order in practice (from tg's `TICK_ORDER.md`, [tg]): sleeping procs resume (the Master Controller wakes here, deliberately last among sleepers) → control passes to BYOND internals → **SendMaps** computes and sends per-client view updates (cost scales with clients and with icons in view [dev 2023-12-14]) → **client verbs execute at the very end of the tick**. Consequence: expensive verbs are the most likely code to overrun the tick — keep verbs thin and defer real work to a subsystem. The same thin-enqueuer discipline applies to `Topic()` handlers: an SS13 contributor tracing glide stutter found incoming verb/Topic calls execute immediately at their processing point rather than waiting politely, so a heavy handler stutters everything else — validate, enqueue, return. [community 2026-06-21]
- `world.tick_usage` reads the % of the current tick consumed so far — the primitive under all tick-budget macros (`TICK_CHECK`, `CHECK_TICK`, `MC_TICK_CHECK`).
- An infinite loop that never sleeps gets aborted by the engine's runaway detection. It is a crash guard, not a scheduling tool.

## Preprocessor and compile-time

- `#define` is textual paste. Parenthesize macro bodies and macro arguments; a macro that performs work should look like a call (`#define FOO(...)`), not a constant. Multi-statement macros need `do { } while (FALSE)` hygiene and `__`-prefixed internal vars. [tg STYLE — see style-and-review.md]
- Include order matters: defines must be included before code that uses them, which is why every profiled repo keeps `code/__DEFINES/` first in the `.dme`. Fork overlays compile **last** so their re-opened types win.
- `#undef` file-local macros at end of file to prevent cross-file leaks. [tg STYLE]
- Compile-time type checking is shallow: the `:` operator bypasses it entirely (banned in all profiled style guides — cast properly), and string type paths (`"/obj/item"`) bypass existence checks (also banned).
- **Version-gate with `#if DM_VERSION >= 515` / `>= 516`** (compile-time; `DM_BUILD` is the beta-cycle minor version, rarely needed outside BYOND's own beta testing) — this is the actual mechanism behind every "515+"/"516+" feature note elsewhere in this skill (`caller`/`callee` walking, `client.RenderIcon`, `byondStorage`, the native `BYOND` JS object). For logic that can't be resolved at compile time (e.g. per-connecting-client capability checks), the runtime equivalents are `world.byond_version`/`world.byond_build` and `client.byond_version`/`client.byond_build`. [DM Ref: preprocessor DM_VERSION, DM_BUILD]

## Built-in movement and spatial procs

- `view()`/`range()`/`oview()` are VM-optimized built-ins — cheaper than hand-rolled coordinate sweeps of the same area. Prefer them for spatial queries. [heuristic, consistent across tg guidance; profile when it matters]
- Max view size is about 5000 tiles (~70×70). [DM Ref: client.view var — corrects older material claiming a hard max of 10]
- `walk_to`/`step_to` **silently do nothing if the target is farther than 2× `world.view` steps** [DM Ref: walk_to] — a classic "mob just stands there" bug.
- The `walk_*()` family runs in an engine-internal loop outside any subsystem's control; MC-based codebases ban it and provide a movement manager (tg: `SSmove_manager`/`GLOB.move_manager`; check the local equivalent). Also, an atom in a walk queue is retained by it until `walk(x, 0)`. [tg STANDARDS, DM Ref]
- **Gliding** (`glide_size` var, `LONG_GLIDE` appearance flag) is what makes a tile-to-tile move look smooth instead of an instant jump; leave `glide_size` unset to let the client scale it itself against `client.fps` vs `world.fps`. Without `LONG_GLIDE`, diagonal glides follow strict Euclidean distance (slower than cardinal); with it, a diagonal takes exactly as long as a cardinal move. **Gotcha**: under `LEGACY_MOVEMENT_MODE`, setting any bound/step var away from its default silently turns gliding off for that atom. [DM Ref: notes/gliding]
- **Pixel movement** (`bound_x`/`bound_y`/`bound_width`/`bound_height`, `step_size`/`step_x`/`step_y` on movable atoms) lets a mover advance in smaller-than-a-tile steps — relevant only on forks that actually use it (most SS13 forks stay tile-based; check before assuming this applies). Two gotchas when it is: `Enter()`/`Exit()` can fire for several turfs/areas in a single move, or **not fire at all** if the atom stays within one turf's pixel bounds — never assume a 1:1 call-per-tile-crossing; and `pixel_x`/`pixel_y`/`pixel_z` are purely visual offsets that do **not** move the bounding box, so collision/hit-testing code must not treat them as position. [DM Ref: notes/pixel-movement]

## animate() and visual timing

- **The server-side appearance change from `animate()` is instant.** The animation itself is a set of interpolation instructions sent to the client; the atom's actual appearance is already the final state of the last `animate()` call. Server code reading appearance vars mid-"animation" sees the end state, not the interpolated one. [dev 2024-04-01]
- **Don't sleep between chained `animate()` steps.** A superseding animation started after a sleep begins from whatever the appearance happens to be then, which is inconsistent with setting up the full chain at once — build multi-stage animations as one `animate(...)` + `animate(...)` chain in a single execution. [dev 2025-04-21]
- `animate()` is for visual interpolation, not gameplay position: a projectile's real trajectory should be stepped tick by tick; use animate only for cosmetics like spin. [dev 2025-04-21]

## Particles

- `/particles` is a client-side-computed visual-effect datum — spawns and tracks many pixels or icons with a lifespan (confetti, sparks, exhaust, rain) entirely on the client, off the server's tick budget once attached. Instantiate with `new`, configure vars, assign to an atom's `particles` var. [DM Ref: notes/particles]
- **Silent no-op gotcha**: vector/color particle vars don't support partial (indexed) mutation — `particles.gravity[2] = 0` does nothing, silently. Reassign the whole vector instead (`particles.gravity = list(x, 0, z)`). Same family of trap as the `animate()`-after-sleep and `RenderIcon` savefile issues elsewhere in this skill: looks like it should work, fails without an error. [DM Ref: notes/particles]
- Two built-in performance knobs: `count` (max concurrent particles) and `spawning` (particles created per 0.1s tick). The z coordinate must resolve to between -100 and 100 after projection or the particle isn't guaranteed to display. [DM Ref: notes/particles]

## Common runtime errors and defenses

| Runtime | Typical cause | Defense |
|---|---|---|
| `Cannot read null.X` / `null.proc()` | Reference died during a sleep/do_after/input gap; uninitialized var | Re-validate after every async gap; `QDELETED()` checks |
| `list index out of bounds` | Index math past `len`; list mutated under a `1 to len` loop | Iterate `for-in` (copy semantics) or re-check `len`; never mutate the iterated list |
| `bad index` / `not associative` | Assoc access on special lists (`contents` etc.) | Don't; keep a parallel normal list |
| Silent wrong values | Bit ops above bit 23; float precision past 2^24 | Keep flags in 24 bits; don't count with huge integers |
| Proc "randomly stops" | It runtimed mid-way; caller continued | Read the runtime log first; set `.` fallbacks in resilient procs |
| Input/verb exploit | State validated before a prompt, not after | Re-check state and location *after* `input`/`alert`/`tgui_input` returns [tg STANDARDS] |

When a bug makes no sense, check the runtime log (`world.log`) before theorizing: DM's continue-past-errors model means the visible failure is often two procs downstream of the actual runtime.

On BYOND 515+ you can also walk the live call chain from inside a proc via the `caller` var and `/callee` type — `for (var/callee/frame = caller, frame, frame = frame.caller)` exposes each frame's `src`, `usr`, `file`, and `line` [dev 2024-10/2024-05, 516 era]. Invaluable for "who actually called this" debugging without instrumenting every call site; check the installed BYOND version supports it before relying on it.
