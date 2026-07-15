# Style and Review

Tier-3 conventions (modern tgstation, from `.github/guides/STYLE.md` + `STANDARDS.md`) plus the review procedure. On a fork, the local guide wins where it differs — cmss13 enforces an older tg snapshot, CEV-Eris has its own guide; see repository-profiles.md → Style dialects.

## Contents

- [Core style (tg baseline)](#core-style-tg-baseline)
- [Macros](#macros)
- [Security checklist](#security-checklist)
- [Code review checklist](#code-review-checklist)
- [Static self-check procedure](#static-self-check-procedure)
- [User-runnable checks](#user-runnable-checks)
- [Honest reporting](#honest-reporting)

## Core style (tg baseline)

Layout and naming:

- Tabs for indentation, never spaces; no mid-line alignment padding.
- Absolute type paths in definitions (`/obj/item/thing/proc/use()`), never nested indentation trees; paths start with `/`, snake_case; datums spelled with the `/datum/` prefix.
- `var/name` declaration form. Descriptive names — no `M`/`C`/`H` single letters (`user`, `victim`, `target`); `i` acceptable only for numeric loops. No negative names (`is_flying`, not `is_not_flying`). Time-unit vars carry the unit in the name unless deciseconds (`seconds_per_tick`).
- No inline control bodies (`if (x) return` on one line — split it). Comparisons read `variable op constant`, not reversed.
- Operators: spaces around boolean/comparison/assignment ops and after commas; no space after `!` or around `.`.

Language use:

- Early returns over nesting pyramids.
- No magic numbers/strings — named `#define`s; time values via `SECONDS`/`MINUTES` defines.
- `TRUE`/`FALSE` for booleans.
- No `:` type-unsafe access — cast to the proper type. No string type paths.
- `static` keyword over the misleading `global` for type-scoped vars.
- Prefer `::` over `initial()` when the type is static at compile time (modern tg; older forks may lack `::` support — check the local BYOND version before using).
- Avoid getter procs for plain var access (real proc-call overhead, no encapsulation benefit in DM); prefer vars maintained by setters when derived state must stay in sync.
- Explicit `return value` over implicit `.` mutation, except the idiomatic `. = ..()`. Use `.` deliberately for runtime-resilient fallbacks and then `return .` explicitly.
- Named arguments where a bare literal would be opaque (`give_pizza(hot = TRUE, toppings = 2)`).
- Initialize-arg pattern: name the argument after the var, assign `src.var = var`.
- Multiline calls/lists: one indent, trailing comma, closing paren at call indentation. Backslash continuations only where macros force them.
- Avoid `++x`/`x++` cleverness in expressions; increment on its own line.
- Avoid BYOND pointer vars (`&x`) — hidden references, hard-delete bait, low readability. [tg STANDARDS]
- New files in the right folder; lowercase filenames, unique across the tree where possible (runtime traces don't show full paths).

## Macros

- SCREAMING_SNAKE_CASE. Parenthesize the body and every argument use.
- A macro that executes work takes `(...)` so call sites look like calls.
- Multi-statement macros: `do { ... } while (FALSE)` scope + `__`-prefixed internals; never evaluate an argument twice (hoist into `__` vars).
- Be hygienic: pass in what the macro needs; leaking or consuming call-site vars needs a strong reason.
- `#undef` file-local defines at file end; shared defines live in the defines tree (`code/__DEFINES/`), never in feature files.

## Security checklist

From tg STANDARDS (applies everywhere; exploits don't care about lineage):

- All player input sanitized/escaped; treat every input as malicious.
- Re-validate state **after** any `input`/`alert`/tgui prompt returns (input stalling: player holds the dialog open until conditions changed). Also guard against stacking multiple concurrent prompts.
- Every `Topic()`/`ui_act` handler validates that the action is legal for the current state — never trust that the UI only sends valid actions.
- `locate(ref)` from user data always constrained to a known list (`in contents`), never global.
- SQL strictly through parameterized queries.
- Round/antag metadata stays admin-only; don't leak it through outputs, stat panels, or UI data.

## Code review checklist

Work through in order; the early items are where SS13 patches actually break.

**Lifecycle and references**
1. Everything acquired in `Initialize`/`New`/attach is released in `Destroy`/detach: signals, timers (stored ids + `deltimer`), processing (`STOP_PROCESSING`), global-list entries, mutual backrefs.
2. `Destroy()` clears refs only — no side effects, no sleeps — and returns `..()`.
3. Non-owned stored references are weakrefs or `COMSIG_QDELETING`-guarded; no strong ref to something another system owns.
4. No new `del` calls; deletion via `qdel`/`QDEL_NULL`/`QDEL_IN`.

**Async safety**
5. Every reference used after `sleep`/`do_after`/input/`INVOKE_ASYNC` boundary is re-validated (`QDELETED`, null-checks, state re-checks).
6. No sleep in `Initialize`, `Destroy`, `process`, or any `SIGNAL_HANDLER` proc (sleeping work → `INVOKE_ASYNC`/timer).
7. `spawn`/`sleep` not used where a timer/subsystem is the local idiom.

**Signals and overrides**
8. `RegisterSignal` uses `PROC_REF` family; handler declared with `SIGNAL_HANDLER`; `override = TRUE` only with a justifying comment.
9. Overridden procs call `..()` where the parent chain matters (esp. `SHOULD_CALL_PARENT` procs); return values propagated correctly (`. = ..()`).
10. New root-proc signals ship with `SHOULD_CALL_PARENT(TRUE)`.

**Correctness**
11. `process()` uses the delta argument; no frame-dependent rates.
12. Lists not mutated while iterated with index loops; `as anything` only on lists guaranteed homogeneous.
13. Bit flags within 24 bits; no float-precision-sensitive integer math.
14. Runtime-resilience reviewed: what happens to the *caller* if this proc runtimes midway?

**Cost** (see performance.md)
15. New per-tick / per-move / per-mob work justified by frequency × size; allocations hoisted out of hot loops; no full-world scans where a registry list exists.

**Fit**
16. Change is minimal and in the right layer (modular placement on tracking forks → tgstation-modular-content); no drive-by refactors; naming and idiom match the surrounding file; new abstractions justified against existing mechanisms (ss13-architecture.md → Choosing the right mechanism).

## Static self-check procedure

After writing code, before reporting:

1. Re-read the diff top to bottom simulating a cold reviewer; check every item above that the diff touches.
2. Trace one full lifecycle on paper: create → use → qdel. Name the exact line releasing each acquired resource.
3. Trace one hostile input through every new `ui_act`/`Topic`/verb path.
4. Grep your new identifiers: every proc you reference exists, every define you use is included before use, every signal you send has its define.
5. Check include wiring if you added files (`.dme` or the fork's aggregator — per local convention).
6. Diff hygiene: no stray whitespace churn, no debug output, no commented-out code.

This is a static review — it does not replace compilation, and you must not imply it does.

## User-runnable checks

Offer these (they are the user's to run unless explicitly delegated):

- **Compile**: the repo's build script (`BUILD.cmd` / `tools/build`) or DreamMaker CLI (`dm <project>.dme`). Catches include, path, and macro errors.
- **DreamChecker / SpacemanDMM** (`SpacemanDMM.toml` present in most profiled repos): static lints including `SHOULD_CALL_PARENT`, `SIGNAL_HANDLER` sleep detection, return-type checks.
- **OpenDream compiler** where CI uses it — a second, stricter frontend; pragma files (cmss13 `code/__pragmas.dm`, Vanderlin's OPENDREAM-gated copy) elevate lint categories to errors.
- **CI suite** (`.github/workflows/`): full lint + compile + unit tests on tg-family.
- **Unit tests** (`code/modules/unit_tests/` on tg-family) for testable logic; integration/reference tracking builds for harddel hunts.

## Honest reporting

- Never state or imply the code compiled, ran, or passed anything unless the command executed in this session and you saw the output.
- Separate in the report: (a) what was changed, (b) what was statically verified and how, (c) what remains unverified and which command closes each gap.
- If you could not find a definition or confirm an assumption, say so explicitly rather than smoothing it over — a named uncertainty is recoverable; a hidden one becomes a runtime three weeks later.
