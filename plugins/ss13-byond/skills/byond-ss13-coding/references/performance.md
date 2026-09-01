# Performance

Main-thread time is the scarce resource: one DM thread runs all simulation, and whatever you burn, every other system loses (see dm-language-and-runtime.md → world tick for the tick anatomy). But *never* justify a change with "BYOND is single-threaded so everything must be fast" — every recommendation here names its specific cost source and its applicability. Recommendations that need measurement are tagged **[measure]**; take them as hypotheses until profiled.

## Contents

- [Method: cost = frequency × work](#method-cost--frequency--work)
- [Tick budgeting](#tick-budgeting)
- [Algorithmic costs](#algorithmic-costs)
- [Allocations](#allocations)
- [Appearances, overlays, icons](#appearances-overlays-icons)
- [Timers, signals, and background work](#timers-signals-and-background-work)
- [Caching](#caching)
- [Deletion cost](#deletion-cost)
- [What not to do](#what-not-to-do)

## Method: cost = frequency × work

Before optimizing anything, establish two numbers:

1. **How often does this run?** Per world tick? Per mob per SSmobs fire? Once per interaction? Once per round? Trace the callers; for `process()`, note the subsystem's `wait`.
2. **How big is the data?** Ten items or every atom on the z-level?

Hot path = high frequency × non-trivial work: `process()` bodies, movement handlers (`Moved`, `Entered`/`Exited`), combat procs, signal handlers on chatty signals, anything under SSfastprocess, `Life()`. Cold path = verbs used occasionally, round setup, admin tools. **Optimizing cold paths is churn; reviewing hot paths is duty.** A once-per-round O(n²) over 50 items needs nothing; a per-tick allocation in `Moved` on every mob does.

When the numbers are unknown and the stakes are real, say so and recommend the profiler (the built-in world profiler / `SSprofiler` where present) rather than guessing. **[measure]** applies to any claim below when transplanted to an unfamiliar context.

## Tick budgeting

The MC gives each subsystem a slice; your job is to be interruptible:

- Subsystem `fire()`: call `MC_TICK_CHECK` after each unit of work; design the loop to resume (`resumed`, `current_run` snapshot).
- Long non-subsystem loops (setup, admin mass-operations): `CHECK_TICK` (`code/__DEFINES/_tick.dm`) yields when the tick is overspent, via `stoplag()`.
- Never distribute work with bare `sleep(x)` inside a loop over game objects — the references pin, the world changes mid-loop, and the work escapes budgeting. Chunk via subsystem resumption or timers instead.
- Verbs execute after SendMaps at tick end (tg TICK_ORDER.md): an expensive verb is disproportionately likely to cause overtime. Verbs validate + enqueue; subsystems do the work.

## Algorithmic costs

- **Kill full-world scans.** `for (var/mob/M in world)` and `typesof`-driven sweeps touch everything everywhere. Nearly every codebase keeps global lists of the interesting subsets (`GLOB.mob_list`, `GLOB.machines`, per-z lists…) — find and use the local registry; iterate the smallest existing list that contains your targets.
- **Spatial queries:** `view()`/`range()` are VM built-ins optimized below DM level — prefer them to manual x/y loops over turfs. **On tg, check for a maintained index first:** `SSspatial_grid` keeps live per-cell lists and its helpers (`get_hearers_in_view/_range/_LOS`, `code/__HELPERS/spatial_info.dm`) beat re-scanning with `view()`. Scope it honestly — that grid indexes exactly three categories (**hearing-sensitive movables, client mobs, atmos machines**), so it replaces hearer/player/atmos lookups and nothing else; for an arbitrary type you are still on `view()`/`range()` plus a typecache.
- **Type dispatch:** chains of `istype` else-ifs in hot code → typecache lookup (`typecacheof`, cached in a static/global). One assoc lookup, no chain.
- **`for (var/x in 1 to L.len)` vs `for (var/x in L)`:** the for-in form is measurably faster in tg's profiling and iterates a copy (safe against mutation); use indexed loops only when you need the index or parallel arrays. [tg STANDARDS]
- **Repeat lookups:** hoist `x.y.z` chains and proc calls out of loops when the value can't change mid-loop; DM does not do that for you (every `.` is a runtime lookup).
- **String assembly in loops:** each `+=` on text builds a new interned string (strings are immutable, stored in a global tree [dev 2024-10-01]). For big assemblies collect parts in a list and `jointext()` once. **[measure]** below a few dozen concatenations.

## Allocations

Allocation isn't free and garbage isn't free either (refcount churn + eventual scan pressure):

- **Temp lists in hot procs:** a fresh `list()` per call in `process()`/`Moved()` on many instances is real pressure. Reuse a static scratch list (`var/static/list/scratch`), or restructure to avoid the intermediate. Two conditions, both easy to get wrong: it must be re-entrancy-safe (no sleeps while it is dirty), and remember `static` is **one slot for the entire type tree** — subtypes do not get their own (dm-language-and-runtime.md → static and global vars), so two subtypes using “their” scratch list in the same tick are using the same list.
- **`list + list` vs `+=`:** `+` allocates a new list each time; `+=` mutates. In accumulation loops always `+=`/`Add`. (Semantics: dm-language-and-runtime.md → Lists.)
- **Var-definition list initializers** allocate per object created, used or not, via the hidden init proc — and tg is explicit that “an empty list that is never used takes up more memory than just `null`”. The `LAZYADD`/`LAZYREMOVE`/`LAZYINITLIST` family (`code/__HELPERS/_lists.dm`) keeps the var null until first write. **Apply tg's own criterion rather than blanket-lazying everything:** lazylists are “best used on **hot types** when making lists that are **not always used**” — the canonical example is a list on every atom that most atoms never populate. tg equally warns that you “probably should not be using these macros if your list is not a lazylist”, since it obfuscates code that was never going to be null. A list that is populated in `Initialize` and used for the object's whole life is not a lazylist candidate. [tg `_lists.dm`]
- **Assoc lists cost ~3× flat lists per entry** and tree-search on lookup; when a fixed small set of keys is known at compile time, flat list + index defines (or plain vars) beat an assoc map. [tg STANDARDS] Don't contort genuinely dynamic keyed data to avoid it — correctness first.
- **`typesof()`/`subtypesof()` allocate a list per call** — cache in a static/GLOB if called more than once.

## Appearances, overlays, icons

The client renders *appearances*; the server manages their global table and tells clients about new ones.

- Passing an `icon` object or icon-state string to `overlays`/`add_overlay` converts it to an appearance **every insert**, including a global-table insert and client notification. Convert once (`iconstate2appearance`-style helpers), store in a `static`, add the stored appearance. [tg STANDARDS] Skip caching only for one-time init overlays.
- Each *distinct* combination of appearance vars is a new appearance object sent to every client that sees it — per-player procedurally-varied overlays multiply both memory and network. Design overlay sets around a small vocabulary of reusable states. [tg STANDARDS + dev]
- `flick()` is cheap (a tiny broadcast message; doesn't create a persistent appearance) [dev 2025-03-28].
- **`/mutable_appearance` is the intended tool for “this appearance changes a lot”, not a footnote.** An appearance is an *immutable* shared object, so every edit to an atom's appearance “generates new appearances, many of which may be temporary” — and reading `overlays` builds a temporary list object, so churning that list churns appearances. A `/mutable_appearance` lets you make **many changes without creating all those temporaries**, and assigning it to `appearance` compiles it into one new immutable appearance. Build up, then assign once, instead of rebuilding the overlay stack edit by edit. [DM Ref: mutable appearance] Scope it correctly though: this is a **server-side** saving only — the concept does not exist on the client, which sees finished appearances either way [dev 2023-12-14].
- SendMaps cost scales with clients × icons in view [dev 2023-12-14], and it is not hypothetical. tg's own `TICK_ORDER.md` puts a number on the per-player slope: **~0.45% of the tick per connected player** (measured 2022-03-20), rising to ~0.6% on most highpop rounds — i.e. **~22–30% of every tick consumed by SendMaps at 50 players, after all DM code has stopped executing** [tg TICK_ORDER.md, verified against master 2026-07-18]. Prefer this figure when arguing maptick cost: it is tg-documented and per-player, so it scales to the server in question. Busy servers have separately measured ~70% of the tick going to maptick after their proc code was already optimized [dev 2023-04-03]. An experienced SS13 developer's account of the pre-BYOND-515 era: SendMaps left only **~20 ms** of tick budget to run all game logic with 60–80 concurrent players (some servers ran 250+), which is why that era's SS13 code was so aggressively hand-optimized — one server even considered splitting the simulation across two processes communicating via `world/Export()` to work around it [community 2025-12-11]. Modern multi-threaded SendMaps (see below) changes this balance, but the *shape* of the cost (scales with clients × view contents) is unchanged. Keeping perpetually-animating or perpetually-changing atoms out of dense areas is a real lever. **[measure]**
- Classic overlays are efficient *when they rarely change* — the cost is churn (each change re-reconciles the appearance and notifies clients), not existence [dev 2022-05-18]. Client-side the unit of filter cost is the **added render context**, not the shader maths: *“effectively the issue is # of added render contexts… there are of course costs for the shaders themselves, but I think those costs are low compared to the cost of changing up contexts”* [dev 2024-02-20]. Every filter adds at least one context, and **more passes means more contexts — so cost scales with the filter's *size*, not merely its presence.** A Gaussian blur is two passes at size 1 (horizontal then vertical, 19 texture samples each); larger radii need *more* passes, because you cannot simply widen the kernel — stretching a fixed sample count over a bigger radius degrades the image, so the engine iterates instead (it does take shortcuts for huge blurs) [dev 2024-02-20, community 2026-09-01]. That is why `blur(16)` is far from 8× the cost of `blur(2)` in the naive sense but decidedly *not* free either. Outline is one pass at 1 pixel (9 samples) and more when wider; motion blur is one pass unless large (same filter as Gaussian, one direction); alpha is two samples; drop shadow bundles blur + possible outline + compositing; bloom is the heaviest, and is meant for whole scenes where that is acceptable. Net: “just a blur” on many simultaneously-visible objects is a client framerate lever that grows with radius, and it is invisible to server profiling — no amount of `world.cpu` staring will show it. [dev 2025-11-21]
- `icon()` operations (`Blend`, `Scale`, …) at runtime are expensive and generate cache entries; do icon math at compile/init time or in rustg where available. **[measure]**
- **Huge `.dmi` files cause client-side freezes on first load**: the engine developer traced ~1-second client hiccups in a live SS13 test to big icon files loading when the player first wandered into an area using them [dev 2023-02-13]. Split giant sprite sheets; treat "one .dmi with everything" as a client-latency hazard, not a tidiness win.

## Timers, signals, and background work

Every persistent "thing that will run later" has bookkeeping cost and a leak surface:

- Don't create a timer per instance for something a single processing subsystem pass can do — thousands of timers churn SStimer's queues. Conversely, don't put a datum on SSfastprocess to poll for a condition a single `TIMER_UNIQUE` timer could handle. Match mechanism to cardinality and cadence.
- Signals are cheap to *have* but not free to *fire*: a signal sent per tick per atom with a dozen listeners is a hidden hot path. Don't add listeners to chatty signals (`COMSIG_MOVABLE_MOVED` on everything) when a narrower hook exists.
- No unmanaged `spawn()` loops as heartbeats — invisible to profiling-by-subsystem, unbudgeted, reference-pinning. Use SSprocessing/SStimer.
- `INVOKE_ASYNC` starts a proc that runs until its first sleep *now* — async ≠ deferred ≠ free.

## Caching

- Cache derived values that are read often and change rarely (typecaches, appearance sets, computed stat totals). Compute once in `Initialize`/first use; store in `static`/GLOB when shared across instances.
- **Every cache needs an invalidation story.** Cache + signal-driven invalidation (listen to what changes the inputs) is the tg-idiomatic pair (cf. `update_appearance`/`update_overlays` pipelines). A stale cache is a correctness bug you traded for speed.
- Static caches keyed by instance hold references → hard-delete risk; key by type/ID or clean up on `COMSIG_QDELETING`.
- Prefer per-consumer plain vars / indexed lists over central assoc caches in root systems (assoc overhead, ownership ambiguity). [tg STANDARDS]

## Deletion cost

- `qdel` of a well-behaved datum is cheap; a **hard delete scans all of memory** and scales with total list volume in the world [dev 2023-11-15]. Mass-deleting badly-cleaned objects (e.g. bulk turf contents wipes) can produce multi-second stalls. Fix the `Destroy()` cleanup, not the delete site.
- Creating and discarding many short-lived datums per tick is a refcount + GC treadmill; pool or reuse when the pattern is structural (projectiles, effects) and the local codebase already has a pooling idiom — introducing pooling *anew* needs profiling justification. **[measure]**

## What not to do

- Don't micro-optimize cold paths, sacrifice clarity for unmeasured wins, or duplicate state to save a lookup you can't show matters.
- Don't trade correctness for speed: a fast proc that skips `QDELETED` checks after a sleep is a runtime factory.
- Don't cargo-cult one fork's optimization (e.g. tg's appearance caching helpers) into a fork that lacks the helpers — port the *reason*, implement with local tools.
- Don't present any **[measure]**-grade claim as fact in review comments; phrase as "likely, verify with the profiler".
