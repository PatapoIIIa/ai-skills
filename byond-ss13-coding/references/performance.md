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
- **Spatial queries:** `view()`/`range()` are VM built-ins optimized below DM level — prefer them to manual x/y loops over turfs.
- **Type dispatch:** chains of `istype` else-ifs in hot code → typecache lookup (`typecacheof`, cached in a static/global). One assoc lookup, no chain.
- **`for (var/x in 1 to L.len)` vs `for (var/x in L)`:** the for-in form is measurably faster in tg's profiling and iterates a copy (safe against mutation); use indexed loops only when you need the index or parallel arrays. [tg STANDARDS]
- **Repeat lookups:** hoist `x.y.z` chains and proc calls out of loops when the value can't change mid-loop; DM does not do that for you (every `.` is a runtime lookup).
- **String assembly in loops:** each `+=` on text builds a new interned string (strings are immutable, stored in a global tree [dev 2024-10-01]). For big assemblies collect parts in a list and `jointext()` once. **[measure]** below a few dozen concatenations.

## Allocations

Allocation isn't free and garbage isn't free either (refcount churn + eventual scan pressure):

- **Temp lists in hot procs:** a fresh `list()` per call in `process()`/`Moved()` on many instances is real pressure. Reuse a static scratch list (`var/static/list/scratch`; must be re-entrancy-safe: no sleeps while it's dirty), or restructure to avoid the intermediate.
- **`list + list` vs `+=`:** `+` allocates a new list each time; `+=` mutates. In accumulation loops always `+=`/`Add`. (Semantics: dm-language-and-runtime.md → Lists.)
- **Var-definition list initializers** allocate per object created, used or not, via the hidden init proc. For lists most instances never use: `LAZYADD`/`LAZYREMOVE`/`LAZYINITLIST` family (`code/__HELPERS/_lists.dm`) keeps the var null until needed. [tg STANDARDS]
- **Assoc lists cost ~3× flat lists per entry** and tree-search on lookup; when a fixed small set of keys is known at compile time, flat list + index defines (or plain vars) beat an assoc map. [tg STANDARDS] Don't contort genuinely dynamic keyed data to avoid it — correctness first.
- **`typesof()`/`subtypesof()` allocate a list per call** — cache in a static/GLOB if called more than once.

## Appearances, overlays, icons

The client renders *appearances*; the server manages their global table and tells clients about new ones.

- Passing an `icon` object or icon-state string to `overlays`/`add_overlay` converts it to an appearance **every insert**, including a global-table insert and client notification. Convert once (`iconstate2appearance`-style helpers), store in a `static`, add the stored appearance. [tg STANDARDS] Skip caching only for one-time init overlays.
- Each *distinct* combination of appearance vars is a new appearance object sent to every client that sees it — per-player procedurally-varied overlays multiply both memory and network. Design overlay sets around a small vocabulary of reusable states. [tg STANDARDS + dev]
- `flick()` is cheap (a tiny broadcast message; doesn't create a persistent appearance) [dev 2025-03-28]. Mutable appearances are a *server-side* construction convenience only [dev 2023-12-14].
- SendMaps cost scales with clients × icons in view [dev 2023-12-14]; keeping perpetually-animating or perpetually-changing atoms out of dense areas is a real lever. **[measure]**
- `icon()` operations (`Blend`, `Scale`, …) at runtime are expensive and generate cache entries; do icon math at compile/init time or in rustg where available. **[measure]**

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
