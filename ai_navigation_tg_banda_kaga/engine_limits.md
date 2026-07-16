# Engine Limits

Updated 2026-07-16. Universal engine facts (tick anatomy, cooperative single-threading, GC/refcounting, numeric/bitwise limits, list and string costs, appearance mechanics) live in the **byond-ss13-coding** skill — `references/dm-language-and-runtime.md` and `references/performance.md`, verified against the official DM Reference. This file keeps the *repo-specific* half: where this codebase sets, checks, and works around those limits.

## Tick system (as configured here)

- The world runs at `world.fps = 20` (set in `code/world.dm`). One tick is the scheduling unit for everything.
- The Master Controller (`code/controllers/master.dm`) gives each subsystem a slice of each tick, weighted by `priority`. A subsystem must finish or yield within its slice.
- `TICK_USAGE` is the percentage of the current tick consumed. `Master.current_ticklimit` is the soft cap for the current run.

## Yielding (the only safe way to do long work)

| Macro | Use inside | Effect | Defined in |
|---|---|---|---|
| `MC_TICK_CHECK` | a subsystem `fire()` | pause the SS, resume next fire | `code/__DEFINES/MC.dm` |
| `CHECK_TICK` | any long loop (init, non-SS proc) | sleep until the next tick | `code/__DEFINES/_tick.dm` |
| `CHECK_TICK_HIGH_PRIORITY` | loop allowed to use more budget | yields at ~95% | `code/__DEFINES/_tick.dm` |

## Native offload available here

Blocking calls freeze the single DM thread (`ai_navigation/processing_hazards.md`). Native offload exists only via `rust_g.dll`, `dreamluau.dll`, `librust_utils.dll` and auxtools — not general game code.

## Lifecycle cost mitigations this repo ships

- Deletion goes through `SSgarbage`; a missed reference forces a slow hard delete (`ai_navigation/runtime_errors.md`).
- Pre-warming pools (e.g. `SSwardrobe`) exist because object creation cost is real — reuse them before writing spawn loops.
- Overlay/vis_overlay compositing is deferred to `SSoverlays` / `SSvis_overlays`; heavy per-atom overlay churn is a known cost (`ai_navigation/visuals_guide.md`).

## Rule of thumb

If a task adds per-tick, per-step, or per-atom work across a large population, it is a tick-budget risk → classify as high risk (`ai_navigation/human_checking.md`) and prefer event-driven signals over polling.
