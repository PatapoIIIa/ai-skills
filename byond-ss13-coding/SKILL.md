---
name: "byond-ss13-coding"
description: "Universal BYOND Dream Maker (DM) and SS13 codebase development skill: writing idiomatic DM code, building or changing SS13 systems (items, mechanics, subsystems, components, elements, signals, traits, actions, timers), fixing runtimes and lifecycle/qdel/Destroy/harddel bugs, optimizing hot procs and tick usage, porting changes between forks, and doing static analysis or code review of DM patches. Use for ANY coding, review, refactoring, optimization, or debugging task that touches BYOND, Dream Maker, DM, SS13, tgstation or an SS13 fork (BandaStation, cmss13, CEV-Eris, Twilight-Axis, Vanderlin, and others) — whenever the user mentions proc, datum, subsystem, component, signal, qdel, lifecycle, tick, performance, review, or debugging in an SS13/BYOND context, even if they don't name the skill. For tgui/web-UI internals also open ss13-tgui; for modular placement on upstream-tracking forks also open tgstation-modular-content."
---

# BYOND / SS13 Coding

Write, review, and optimize DM code across the whole SS13 family — from upstream tgstation to heavily diverged forks — without pretending they all share one style. The skill separates what is *engine truth* from what is *convention*, and tells you which wins when they collide.

## Knowledge tiers and precedence

Every rule you apply belongs to exactly one tier. Never present a lower-tier rule as a higher-tier fact.

| Tier | What it is | Examples | Can be overridden by a project? |
|---|---|---|---|
| 1. BYOND/DM semantics | How the engine actually behaves | `for(x in list)` iterates a copy; refcount GC; 24-bit bitwise ops | **No** — engine truth binds everyone |
| 2. Engineering basics | Language-agnostic practice | DRY, early returns, minimal diffs, no dead code | Rarely, and only explicitly |
| 3. tgstation conventions | Modern /tg/ style and architecture | `Initialize` over `New`, `PROC_REF`, `SIGNAL_HANDLER`, seconds_per_tick | Yes — by tiers 4–5 |
| 4. Fork architecture | How a specific lineage diverges | cmss13 uses `tgui_interact`; Eris barely uses signals | Yes — by tier 5 |
| 5. Local repo rules | This checkout's own instructions | `AGENTS.md`, in-repo `ai_navigation/`, local guides | This *is* the top |

Working inside an existing project: **local instructions and surrounding code > fork architecture > tg conventions.** For new or fork-neutral SS13 code, default to modern tgstation style — but never force a tg pattern onto a fork whose architecture rejects it (see [references/repository-profiles.md](references/repository-profiles.md)).

## Ecosystem: who does what

This skill is an architecture-layer skill in the SS13 skill ecosystem (see the `byond-codemaster-controller` skill for the dispatch and layer contract). Respect the guards:

| Situation | Handoff |
|---|---|
| Task touches tgui files, `ui_interact`/`ui_data`/`ui_act`, ByondUi, blank windows, browser assets | Open **ss13-tgui**; this skill keeps only the DM-side data/action boundary |
| Change must survive upstream re-sync on a /tg/-tracking fork (modular roots, `master_files`, edit tags) | **tgstation-modular-content** decides placement and file layout; this skill decides implementation |
| Repo needs a semantic base discovered, verified, or bootstrapped (`ai_navigation/` folders) | **byond-codemaster-controller** owns base lifecycle and produces the binding brief |
| Pure DM/SS13 coding, review, optimization, debugging | This skill alone |

Truth hierarchy across layers: **repo code > semantic base (fork facts) > this skill's fork-specific claims** — but this skill wins on engine invariants and anti-patterns. A base recommending an anti-pattern is a broken base; report it.

## Task workflow

Follow this order for any implementation, fix, refactor, port, or review task.

1. **Read local instructions first.** Repo root `AGENTS.md`/`CLAUDE.md`, `.github/guides/` (STANDARDS, STYLE, HARDDELETES if present), `CONTRIBUTING.md`, `.editorconfig`, lint configs (`SpacemanDMM.toml`, pragma files). They outrank everything in this skill except engine semantics.
2. **Identify the codebase family.** Fingerprint it (project `.dme` name, modular roots, defines layout, signal penetration) — see [references/repository-profiles.md](references/repository-profiles.md). Don't assume tg idioms exist until you've seen them.
3. **Use the navigation layer if one exists.** In-repo `ai_navigation/router.md`, or a workspace base found via the `byond-codemaster-controller` discovery protocol. Route through it instead of scanning the repo; verify its load-bearing facts against code before trusting identifiers.
4. **Locate real definitions** of every type, proc, signal, component, trait, and subsystem you will touch (`grep` for the definition, not the usage). Read the parent chain of any proc you override.
5. **Study the 2–3 nearest modern implementations** of similar behavior. Prefer recently touched examples (`git log -1 -- <file>`) — old files are fossils of dead conventions, and every large SS13 repo contains plenty.
6. **Choose the change layer**: upstream file, modular overlay, override, or project-specific. On a fork that tracks upstream, this decision belongs to `tgstation-modular-content` — placement constraints outrank implementation convenience.
7. **Design the minimal change.** Reuse the existing mechanism (component, element, signal, trait, timer, processing subsystem) before inventing a new one. If an existing mechanism solves the task "well enough", that beats a new abstraction that solves it "perfectly".
8. **Implement without churn.** No drive-by refactors, no whitespace storms, no renames outside the task, no `New`→`Initialize` conversions of untouched code (tg explicitly warns these cause months-long bugs).
9. **Static self-check** against the checklist in [references/style-and-review.md](references/style-and-review.md): lifecycle pairing, signal hygiene, null-safety after async gaps, tick cost, frame independence.
10. **Report honestly.** List the checks the user can run (compile, DreamChecker, CI) — and never state or imply that the code compiled, ran, or passed tests unless those commands actually executed in this session.

## Reference dispatch

Load only what the task needs — do not read all references for every task.

| Task | Read |
|---|---|
| Any DM code you write or judge — language semantics, lists, refs, sleep/spawn, GC, tick model | [references/dm-language-and-runtime.md](references/dm-language-and-runtime.md) |
| Subsystems, components, elements, signals, traits, actions, timers, init order, Destroy/qdel design | [references/ss13-architecture.md](references/ss13-architecture.md) |
| "Optimize this", hot paths, tick budget, allocations, caches, appearance/overlay cost | [references/performance.md](references/performance.md) |
| Style questions, code review, security checks, the self-check checklist, user-runnable verification | [references/style-and-review.md](references/style-and-review.md) |
| Which fork is this / porting between forks / what's allowed here | [references/repository-profiles.md](references/repository-profiles.md) |
| Where a claim comes from, verification status, how to consult the BYOND ref or Discord logs | [references/source-index.md](references/source-index.md) |

## Always-on invariants

These apply to essentially every DM change, on every fork examined so far (all six ship the same lifecycle skeleton — `Initialize(mapload)`, `Destroy()`, `qdel`, SSgarbage, dcs signals):

- **Pair every acquisition with a release.** Signal registered → unregistered; timer with a stored id → deleted; global list entry → removed in `Destroy()`. `Destroy()` clears references — nothing else, no side effects.
- **After any `sleep`, `do_after`, input, or other async gap, re-validate references** (`QDELETED(x)` / null-check). The world changed while you slept.
- **Signal handlers never sleep** (`SIGNAL_HANDLER`; use `INVOKE_ASYNC` for sleeping work).
- **Reference procs via `PROC_REF`/`TYPE_PROC_REF`/`GLOBAL_PROC_REF`** in `RegisterSignal`/`CALLBACK` wherever the codebase has these macros (all six profiled repos do).
- **No BYOND `walk_*()` procs** in MC-driven codebases — use the local movement manager; no bare `spawn()` loops as heartbeats — use timers or a processing subsystem.
- **`process()` is frame-independent** — multiply per-second rates by the delta argument (`seconds_per_tick` / `delta_time`, per local naming).
- **Absolute type paths, no `:` operator, no string type paths, no magic numbers** — defines with names.
- **Don't recompute what you can cache, don't allocate in a loop what you can hoist** — but only claim a performance win you can argue from call frequency × data size ([references/performance.md](references/performance.md)).
- **Compile claims are sacred.** If you didn't run it, say "not compiled — run X to verify".

## Execution limits

By default this skill's work is static: reading, writing, and reviewing code. Do not launch DreamDaemon, game servers, or long test suites on your own initiative; propose the commands and let the user run them, unless the user has explicitly asked you to run them.
