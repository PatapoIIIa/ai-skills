# SS13 Architecture

Tier-3/4 knowledge: the tgstation architectural toolkit and how far it extends across forks. All six profiled repos (tgstation, BandaStation, cmss13, CEV-Eris, Twilight-Axis, Vanderlin) ship this skeleton — Master Controller, subsystems, `Initialize`/`Destroy`/`qdel`, dcs signals, components, elements — but with different depth of adoption (see repository-profiles.md). Anchor paths below are tgstation unless noted; on a fork, grep for the local equivalent before citing a path.

## Contents

- [Master Controller and subsystems](#master-controller-and-subsystems)
- [Atom and datum lifecycle](#atom-and-datum-lifecycle)
- [qdel, Destroy, and hard deletes](#qdel-destroy-and-hard-deletes)
- [Signals](#signals)
- [Components and elements](#components-and-elements)
- [Traits](#traits)
- [Actions](#actions)
- [Timers and callbacks](#timers-and-callbacks)
- [Global state](#global-state)
- [Initialization order](#initialization-order)
- [Choosing the right mechanism](#choosing-the-right-mechanism)
- [Boundaries: maps, TGUI, modular layers](#boundaries-maps-tgui-modular-layers)

## Master Controller and subsystems

The Master Controller (`Master`, `code/controllers/master.dm`) replaces "everything ticks itself" with centrally budgeted work. Each `/datum/controller/subsystem` declares:

- `wait` — fire interval (deciseconds); `priority` — share of tick budget under load; `flags` — `SS_NO_FIRE` (data holder, never fires), `SS_BACKGROUND` (yields to foreground), `SS_TICKER` (fires every tick, wait in ticks) — defines in `code/__DEFINES/MC.dm`.
- `Initialize()` — one-time setup during world start; `fire(resumed)` — periodic work.

Inside `fire()`, cooperate with the budget: check `MC_TICK_CHECK` (pauses the subsystem, resumes next fire with `resumed = TRUE`) after each work unit. A subsystem that ignores tick checks stalls every lower-priority subsystem behind it. State kept between resumptions lives on the subsystem (`current_run` list pattern).

**Processing subsystems** (`code/controllers/subsystem/processing/processing.dm`) are the standard way for many objects to tick: `START_PROCESSING(SSobj, src)` / `STOP_PROCESSING(SSobj, src)` and implement `process(seconds_per_tick)`. Rules:

- Stop processing in `Destroy()` — a processing entry is a reference and a leak.
- `process()` must be frame-independent: per-second rates × `seconds_per_tick` (named `delta_time` on older forks — match local naming). [tg STANDARDS]
- Pick the slowest subsystem that fits (SSobj vs SSfastprocess vs SSprocessing): frequency is the single biggest cost multiplier.
- `process()` returning `PROCESS_KILL` (where supported) removes the datum from processing.

Verbs run at the very end of the tick after SendMaps (see dm-language-and-runtime.md → world tick): keep verb bodies thin; enqueue real work into a subsystem or timer.

## Atom and datum lifecycle

**Creation.** For atoms, put setup in `Initialize(mapload, ...)`, not `New()`: mapload calls `New` for every mapped atom outside MC control, while `Initialize` is driven by SSatoms with budgeting. [tg STANDARDS] Contract (tg `code/game/atom/atoms_initializing_EXPENSIVE.dm`; same shape in all profiled forks' `atoms.dm`):

- Always `. = ..()` first — the parent chain sets up shared atom state (flags, smoothing, overlays machinery). After a successful init, SSatoms sends `COMSIG_ATOM_AFTER_SUCCESSFUL_INITIALIZE` (tg naming).
- **Never sleep in `Initialize`** — it runs under the init loop; sleeping corrupts init order. Defer with `INITIALIZE_HINT_LATELOAD` (implement `LateInitialize()`) or a timer.
- Return an `INITIALIZE_HINT_*` (`code/__DEFINES/subsystems.dm`): `NORMAL`, `LATELOAD`, or `QDEL` (self-destructs cleanly right after init).
- `mapload` tells you whether this atom came from map instantiation or runtime creation — branch on it for costly cosmetic setup.
- Do not convert legacy `New()` code to `Initialize` as a drive-by; the parent/child interplay makes bulk conversions bug-prone. [tg STANDARDS]

Plain datums just use `New()`.

**Destruction.** `Destroy(force)` exists on `/datum` (`code/datums/datum.dm`). Its only job is releasing references: unregister signals, kill timers, null owned datums (`QDEL_NULL(field)`), remove self from global/manager lists, `STOP_PROCESSING`. No gameplay side effects, no messages, no sleeping. End with `return ..()`.

## qdel, Destroy, and hard deletes

`qdel(x)` (SSgarbage, `code/controllers/subsystem/garbage.dm`) calls `Destroy()`, then queues the object; if references still exist after the grace period, the engine hard-deletes it — the memory-wide reference search described in dm-language-and-runtime.md → GC. **`qdel`/`Destroy`/`SSgarbage` are entirely tgstation-authored conventions, not BYOND primitives** — BYOND itself only gives you `del()` and refcounting GC; the staged, tracked deletion pipeline is userspace code built on top (a wish for the engine to have this natively has been voiced even by experienced SS13 tooling developers [community 2026-01-14]). This matters when porting to non-tg-family code: don't assume `qdel` exists — check for it. Hard deletes are treated as bugs in every profiled repo that measures them (tg, BandaStation, Vanderlin ship `HARDDELETES.md`).

Working rules (from tg HARDDELETES.md, generalizable):

- Whatever `Initialize` acquires, `Destroy` releases. That symmetry is the first thing to review in any patch.
- Mutual ownership: each side nulls the other's backref in its `Destroy`.
- Non-owned references: hold a `WEAKREF(x)` (`/datum/weakref`, resolve may return null) — or, for hot fields where weakref cost matters, register `COMSIG_QDELETING` on the target and null your field in the handler (last resort; collides with other registrations on the same signal).
- Helper defines in `code/__DEFINES/qdel.dm`: `QDELETED(x)` (null or being destroyed), `QDEL_NULL(field)`, `QDEL_IN(x, time)`, `QDEL_LIST`.
- Never call `del` directly in game code.
- Debugging: tg-family repos have compile-time reference tracking (`_compile_options.dm`, `REFERENCE_TRACKING`) that logs who held the reference.

## Signals

The dcs ("datum component system") event bus — defines under `code/__DEFINES/dcs/`, signal names in `dcs/signals/`:

- `SEND_SIGNAL(target, COMSIG_X, args...)` returns ORed handler return flags — senders can branch on e.g. `COMPONENT_CANCEL_*` responses.
- `RegisterSignal(target, COMSIG_X, PROC_REF(handler))`, `UnregisterSignal(target, sig_or_list)`. Registration is per (listener, target, signal); duplicate registration runtimes unless `override = TRUE` (which usually masks a cleanup bug — comment why if you must).
- Handlers start with `SIGNAL_HANDLER` and **must not sleep**; lint-enforced. Sleeping work goes through `INVOKE_ASYNC(...)` or a timer. [tg STANDARDS]
- Proc references always via `PROC_REF` / `TYPE_PROC_REF(/type, name)` / `GLOBAL_PROC_REF` so renames break at compile time. [tg STANDARDS]
- Unregistration is automatic when either side is destroyed *if* cleanup paths run — but explicit `UnregisterSignal` in `Destroy()`/detach paths is the norm; don't rely on component internals you haven't read.
- Adding a signal to a root proc → mark the proc `SHOULD_CALL_PARENT(TRUE)` so overrides can't silently stop the broadcast. [tg STANDARDS]

Fork caveat: the bus exists everywhere, but signal *coverage* differs wildly (Eris: 41 files use RegisterSignal; tg: ~1600). On low-coverage forks, the signal you want probably isn't sent — check the sender exists before writing a listener.

## Components and elements

Both live under `code/datums/components/` and `code/datums/elements/`; core: `_component.dm`, `_element.dm`; behavior flags in `code/__DEFINES/dcs/declarations.dm`.

- **Component** — per-instance datum attached to a parent, with its own state and lifecycle. `AddComponent(/datum/component/x, args)`, `GetComponent`, deleted with parent. Duplicate policy via `dupe_mode` (`COMPONENT_DUPE_ALLOWED`, `...UNIQUE`, `...UNIQUE_PASSARGS`...). Use when behavior needs *state per attached instance* or must be added/removed at runtime.
- **Element** — flyweight: one instance shared by every attachee (`ELEMENT_BESPOKE` creates one instance per distinct arg tuple). `AddElement`/`RemoveElement`. No per-target state on the element itself (bespoke args are the only differentiation; detach must pass the *same* args). Use for cheap, stateless behavior stamped onto many atoms.
- Both attach behavior **without editing the target type** — which also makes them the preferred cross-fork/modular mechanism.
- Prefer an existing component/element over a new subtype-override chain when the behavior is orthogonal to the type tree (e.g. "this thing squeaks", "slippery", "wearable X").

## Traits

Boolean facts with provenance — `ADD_TRAIT(target, TRAIT_X, SOURCE)`, `REMOVE_TRAIT(..., SOURCE)`, `HAS_TRAIT(target, TRAIT_X)`; defines under `code/__DEFINES/traits/`. Multiple sources stack: the trait persists until every source removes it — this is the whole point; never fake it with a boolean var when more than one system can set the state. Trait add/removal fires signals (`SIGNAL_ADDTRAIT`/`SIGNAL_REMOVETRAIT`) you can listen to.

## Actions

`/datum/action` — grantable buttons/abilities attached to a mob (`Grant`/`Remove`, `Trigger`). Use the local cooldown action subtype for abilities with cooldowns rather than hand-rolling timers. Coverage and API drift between forks — read the local `/datum/action` base before subclassing.

## Timers and callbacks

`addtimer(CALLBACK(target, PROC_REF(name), args...), delay, flags)` — SStimer; defines in `code/__DEFINES/subsystems.dm` and `callbacks.dm`.

- Flags: `TIMER_UNIQUE` (dedupe), `TIMER_OVERRIDE` (with UNIQUE: restart instead of ignore), `TIMER_STOPPABLE` (returns an id for `deltimer`), `TIMER_LOOP` (repeating), `TIMER_DELETE_ME` (kill with target).
- Store the id of any `TIMER_STOPPABLE`/looping timer you may need to cancel, and `deltimer` it in `Destroy()`.
- `CALLBACK` holds a reference to its target — a pending timer keeps the target alive; that's usually fine (grace period) but a `TIMER_LOOP` without cleanup is a leak.
- Choosing: one-shot future event → timer. Continuous per-tick behavior → processing subsystem. "After the current call stack unwinds" → `INVOKE_ASYNC` or a 0-delay timer. Raw `sleep` in gameplay procs → almost never; it freezes that proc's chain and pins references (acceptable in linear do-something sequences like `do_after` flows that expect it).

## Global state

- tg-family: `GLOB.x` (managed global lists/vars via `GLOBAL_LIST_EMPTY(...)` etc.); older forks may use `global.x` or bare globals. Grep the local pattern.
- Global managers (station data, lookups) are usually `SS_NO_FIRE` subsystems or GLOB datums — prefer extending the existing manager over adding a new global.
- Anything added to a global list at creation must be removed in `Destroy()` — top hard-delete cause.

## Initialization order

Subsystems declare `init_order` (defines in `code/__DEFINES/subsystems.dm`); the MC initializes them in that order at world start, then SSatoms initializes mapped atoms. Practical rules:

- Code in `Initialize()` of an atom cannot assume a *later-initializing* subsystem is ready; check `Master.current_initializing_subsystem` patterns in the local repo, or defer to `LateInitialize`.
- `LateInitialize` (via `INITIALIZE_HINT_LATELOAD`) runs after all atoms on the z-level finished normal init — the standard fix for "I need the machine next to me to exist".
- Subsystem `Initialize` order bugs surface as null crashes only on cold boot — test-boot claims require an actual boot; don't guess.

## Choosing the right mechanism

Decision path for "where does my behavior live":

1. Existing proc override point on the type (smallest change, no new moving parts)?
2. Existing signal you can listen to (zero-touch on the sender)?
3. Existing component/element that already does 90%?
4. New element (stateless, many attachees) / new component (stateful, per-instance)?
5. New signal on a root proc (`SHOULD_CALL_PARENT`) — touches upstream; on tracking forks needs modular placement review.
6. New subsystem — only for genuinely new *periodic global work*; a processing subsystem entry or timers usually suffice. New subsystems are architecture, not content: propose, don't sneak in.

The universal anti-pattern: a new abstraction (manager datum, event bus, registry) duplicating a mechanism the codebase already has. Reuse beats elegance.

## Boundaries: maps, TGUI, modular layers

- **Maps**: mapped atoms come with `mapload = TRUE` and preset vars from the `.dmm`; var edits on mapped instances live in the map file, not code. Map file edits need the fork's map tooling (mapmerge etc.) — out of scope for this skill; flag them.
- **TGUI**: this skill owns the DM side of the boundary — `ui_data`/`ui_static_data` payload shape, `ui_act` security (validate everything; the client lies), and *when* to push updates. Everything inside `tgui/` (React/TS/SCSS, components, lifecycle, ByondUi) belongs to the **ss13-tgui** skill; open it for any task that crosses into UI internals. Note the entry proc dialect: `ui_interact` (tg-family) vs `tgui_interact` (cmss13).
- **Modular layers**: on forks that track upstream, *where* a change lives (upstream file vs modular overlay vs override file) is decided per **tgstation-modular-content**; this skill only supplies the implementation inside that placement. On hard forks (cmss13, Eris) the whole tree is fork-owned and placement reduces to "follow local file organization".
