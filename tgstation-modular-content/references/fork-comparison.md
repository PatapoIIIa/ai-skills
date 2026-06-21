# Fork comparison: Bubberstation vs Vanderlin vs cmss13-MARINES

Static comparison of three /tg/-lineage codebases to separate **universal modular rules** from **fork-specific architecture** that must not leak into a general skill. Focus fork is Bubberstation; the other two are contrast cases.

## At a glance

| Aspect | Bubberstation | Vanderlin | cmss13-MARINES |
|---|---|---|---|
| Relationship to /tg/ | Tracks upstream, rebases regularly | Heavily diverged /tg/ descendant, still pulls some | Hard fork, effectively its own codebase |
| Modular root | `modular_skyrat/`, `modular_zubbers/` | `modular_abel/` (single) | **None** — edits `code/` directly |
| Override folder | `master_files/` mirrors upstream path | Organized by **theme** (`erp/`, `dun_world/`, `races/`), not path-mirrored | n/a |
| Include mechanism | Flat `#include` list in main `.dme` (`BEGIN/END_INCLUDE`) | **One** line in `.dme` → `_module.dm` aggregator → nested `_xxx.dm` sub-aggregators | Flat `#include` list in `.dme` (`BEGIN_INCLUDE`) |
| tgui entry proc | `ui_interact` | `ui_interact` | `tgui_interact` |
| Upstream-edit tagging | `BUBBER EDIT` / `SKYRAT EDIT` | module `upstream_fixes.dm` overrides + tags | n/a (whole tree is fork-owned) |
| Modular maps | Automapper (TOML + templates) | Map *import pipeline* (generated `.dmm` from upstream source) | Direct map ownership |

## Universal (put in the general skill)

These hold for any fork that re-opens /tg/ types and rebases:

- **Re-open types instead of editing the file that defines them** (`. = ..()`, add vars/subtypes). This is a DM-language property, not a fork feature — works everywhere.
- **Keep new content in a modular root** and reference assets by full modular path.
- **Never edit upstream binaries or upstream maps**; use a modular map mechanism.
- **Every new `.dm` must be registered** in whatever include mechanism the fork uses.
- **Tag any unavoidable upstream edit** so the next merge is legible.
- **Modular defines need a dedicated, late-loading location** to avoid define-file conflicts.
- **Declare cross-file/cross-module dependencies** (a per-module readme or equivalent).

## Worth borrowing from Vanderlin

- **Single-line aggregator include.** Vanderlin's `.dme` contains exactly one modular line: `#include "modular_abel\_module.dm"`. `_module.dm` then `#include`s `erp/_erp.dm`, `dun_world/_dun_world.dm`, `races/_races.dm`, etc., and each of those is itself a sub-aggregator. Effect: the **upstream `.dme` almost never conflicts on rebase** (one stable line vs Bubberstation's thousands of churned include lines), and includes are grouped by feature. If a fork's `.dme` include list is a frequent conflict source, an aggregator file per module is the fix. **But follow the local convention** — on Bubberstation you add to the flat list, because that is what its tooling/CI expects.
- **`upstream_fixes.dm` — one module file that overrides upstream procs** to patch them without editing upstream, with explicit "re-sync when upstream changes" notes in the readme. A clean home for the handful of wraps a fork needs, kept together and documented.
- **Honest readme that names the dependency and the risk.** Vanderlin's `modular_abel/README.md` flags a temporary `force_load.dm` override of `SSmapping/PreInit()` and says **delete before release**, and notes `upstream_fixes.dm` overrides an upstream unit-test `Run()` body that must be re-synced. Documenting *fragile* overrides (not just the clean ones) is the borrowable habit.

## Vanderlin: architecture-specific — do NOT generalize

- **Temp-DME build pipeline.** Vanderlin compiles through a disposable `vanderlin.modular_abel.dme` so the module can be built without modifying the upstream `vanderlin.dme` *at all*. Powerful, but it is bespoke build infrastructure tied to their tooling; do not prescribe it as a general pattern.
- **Map *import* pipeline.** `modular_abel/dun_world/` regenerates a `.dmm` from an external upstream (Azure-Peak) via a path-replacement table (`config/map.json`), prepare/build scripts, and map-QA python. This is "port a whole map from another game" infrastructure — far heavier than the automapper's "edit a room" need. Specific to their map-import goal.
- **Theme-based override layout.** Vanderlin organizes by feature theme rather than mirroring upstream paths. Fine for a heavily-diverged fork where most content is net-new, but on a closely-tracking fork the **path-mirroring** of Bubberstation's `master_files/` is easier to maintain (an override sits next to where you'd look for the upstream original). Prefer path-mirroring for overrides unless the local fork has already standardized on themes.

## cmss13-MARINES: the anti-model (mostly)

- cmss13 has **no modular root** — content lives directly in `code/`, and it uses `tgui_interact` rather than `ui_interact`. It is a **hard fork** that no longer tracks /tg/ closely, so "don't edit upstream" is not even a meaningful constraint there.
- **Lesson, not a pattern:** this is what a codebase looks like when it stops isolating its changes — every file is fork-owned, and re-syncing with /tg/ is effectively impossible. It is the destination a tracking fork is trying *not* to reach. Do not copy its layout onto a fork that still pulls upstream.
- If you are actually working *in* cmss13 (or any heavy fork with no modular root), the modular rules don't apply — confirm the local workflow first. That case is the final bullet of the SKILL's "When to stop and ask a human."

## Decision: which include style to use on a new fork

- Fork already has a flat `.dme` include list and tooling/CI around it (Bubberstation) → **add to the flat list**, sorted, matching neighbors.
- Fork uses or you are creating per-module aggregators (Vanderlin) → **add your include to the relevant `_xxx.dm` aggregator**, and the `.dme` keeps its single stable line.
- Greenfield modular setup where you control it → the **aggregator** approach minimizes `.dme` rebase conflicts and is the better default.
