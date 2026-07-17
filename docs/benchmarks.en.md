# byond-ss13-coding — usage metrics

Numeric A/B test results: the same task was given in parallel to two independent subagents on the same model — one with access to the `byond-ss13-coding` skill, one without. Date: 2026-07-16/17. Artifacts (fixtures, full outputs, ground truth) are preserved in the session's working directory.

## Methodology

Ground-truth answers were fixed **before** the runs — 9 deliberately planted defects in a test DM patch, and 10 engine facts verified against the official BYOND reference. This rules out grading criteria being tuned to the outcome after the fact.

## Track A — code review (finding 9 planted defects)

Patch: a `bounty_hunter` component with deliberate lifecycle/signal/async-safety violations (leaked signal registration, leaked timer, `sleep()` inside a `SIGNAL_HANDLER`, missing `..()` in `Destroy()`, raw `del()` instead of `qdel()`, no reference re-validation after `sleep`/`do_after`, etc.)

| Metric | With skill | Without skill |
|---|---|---|
| Defects found | **9 / 9 (100%)** | 8 / 9 (89%) |
| False positives | 0 | 0 |
| Tokens | 70,500 | 44,400 |
| Time | 201 s | 128 s |

**Defect the baseline missed**: no `QDELETED()` re-validation of references after `sleep`/`do_after` — the one bug belonging to the "compiles clean, breaks silently in production" class.

## Track B — engine-fact quiz (10 questions)

Questions on BYOND/DM semantics, verified against the official DM Reference: bitwise operator width, list-copy semantics in `for-in`, the `walk_to` trigger distance, the cost of `sleep(0)`, GC behavior for keyed mobs and circular references, `world.contents`, and the complexity of `istype()` and associative lists.

| Metric | With skill | Without skill |
|---|---|---|
| Correct answers | **10 / 10** | 7.5 / 10 |
| Tokens | 46,200 | 37,100 |
| Time | 19 s | 43 s |

**Baseline errors**: `for-in` called a "live list" (it's actually a copy — the error encourages unnecessary defensive copying in real code); `walk_to` given as "~127 tiles" (actually 2×view ≈ 11 — a real source of "mob just stands there" bugs); the mechanism behind `istype()` described half-wrong.

## Track E — false-positive stress test

The same patch, but **fixed** (all 9 defects resolved) — the correct answer is "no defects found."

| Metric | With skill |
|---|---|
| False positives | **0** |
| Candidate nitpicks explicitly rejected | 3 (including the correct `/datum/component` convention of no `..()` in `Initialize`) |

Shows the review checklist doesn't induce "finding problems for the sake of finding them."

## Track C — independent fact audit of the skill itself

A separate, adversarial agent checked the 10 most load-bearing `[DM Ref]`-tagged claims in `references/dm-language-and-runtime.md` against the official BYOND reference.

| Metric | Result |
|---|---|
| Confirmed | **10 / 10** |
| Contradicted | 0 |
| Not found in source | 0 |

One tag imprecision was found and fixed (the max-`view` claim cited the wrong reference entry).

## Four-skill linkage economy

A separate test: a combined task requiring all three axes at once (DM implementation + modular placement + tgui), routed strictly through the `byond-codemaster-controller` dispatcher.

| Metric | Value |
|---|---|
| Documents loaded | 9 (out of 20+ available) |
| Routing loops | 0 |
| Unused loads | 0 |

The run surfaced and fixed 3 friction points in the controller (a gitignore-glob blind spot in discovery, over-eager bind lists working against router economy, and no explicit 3-axis composition rule).

## Dollar cost

At Claude Sonnet 5 rates (intro pricing: $2/$10 per 1M input/output tokens, in effect through 2026-08-31), assuming most of the token delta is reference-file reads (input):

| Track | Δ tokens | Estimated cost |
|---|---|---|
| A (review) | +26,100 | ~$0.05–0.10 per run |
| B (quiz) | +9,100 | ~$0.02–0.03 per run |

## Bottom line

The skill's overhead (+25–59% tokens, a few cents per run) pays for itself on a single prevented incident: the one defect the baseline missed belongs to the most expensive bug class there is — "compiles clean, breaks live in production." The skill's value concentrates not in generic advice but in (a) async-safety invariants and (b) verified engine facts where common "folk knowledge" is simply wrong.

## Limitations

One run per cell (no variance estimate); both arms used the same model; the review fixture was authored by the skill's author, which may have made the defects a good match for its own checklist. A stronger next step would be a compilation-based ground truth with 3+ runs per cell.
