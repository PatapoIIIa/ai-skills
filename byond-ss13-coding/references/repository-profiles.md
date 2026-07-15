# Repository Profiles

Tier-4 knowledge: the profiled SS13 lineages and how to fingerprint an unknown one. Facts below were read statically from the checkouts (2026-07); repos drift — treat profiles as priors and re-verify anything load-bearing. Paths are repo-relative; checkout locations are machine state (see source-index.md).

## Contents

- [Fingerprinting an unknown codebase](#fingerprinting-an-unknown-codebase)
- [tgstation](#tgstation)
- [BandaStation-Kagelite_DEV](#bandastation-kagelite_dev)
- [cmss13-MARINES](#cmss13-marines)
- [CEV-Eris](#cev-eris)
- [Twilight-Axis](#twilight-axis)
- [Vanderlin](#vanderlin)
- [Style dialects summary](#style-dialects-summary)
- [Porting between forks](#porting-between-forks)

## Fingerprinting an unknown codebase

Run these checks before assuming anything:

1. **Project file**: root `*.dme` name; `#include` layout (flat list vs aggregators).
2. **Local instructions**: `AGENTS.md`, `CLAUDE.md`, `.github/guides/`, `CONTRIBUTING.md`, in-repo `ai_navigation/` — read before coding; they outrank this file.
3. **Modular roots**: `modular_*` directories; which one is *active* (`git log` per root — old forks keep dead generations).
4. **Toolkit depth**: count of files using `RegisterSignal(` (`rg -l | wc -l`) tells you whether signals are living idiom or imported skeleton; same for `AddComponent`, `addtimer`.
5. **Era markers**: `seconds_per_tick` in controllers → current tg; `delta_time` → ~2020-2023 tg snapshot; `.proc/name` references → pre-515 codebase (no `PROC_REF`).
6. **UI stack**: `tgui/` (React) vs `nano/` (NanoUI) vs raw `browse()`; entry proc `ui_interact` vs `tgui_interact`.
7. **Lint infra**: `SpacemanDMM.toml`, pragma files, CI workflows — defines what "passes checks" means locally.

All six profiled repos share the tg lifecycle skeleton: `/atom/proc/Initialize(mapload, ...)`, `/datum/proc/Destroy(force)`, `qdel` + SSgarbage, `code/__DEFINES/dcs/` signals, `code/datums/components/` + `elements/`. Differences are depth, era, and layers — not presence.

## tgstation

- **Role**: upstream master; the tier-3 default this skill teaches. `tgstation.dme`.
- **Guides**: `.github/guides/` — STANDARDS.md, STYLE.md, HARDDELETES.md, TICK_ORDER.md, VISUALS.md, ATOMIZATION.md (normative; the source of most tier-3 content here).
- **Anchors**: atom init `code/game/atom/atoms_initializing_EXPENSIVE.dm`; `Destroy` in `code/datums/datum.dm`; MC defines `code/__DEFINES/MC.dm`, tick defines `code/__DEFINES/_tick.dm`; qdel defines `code/__DEFINES/qdel.dm`; dcs `code/__DEFINES/dcs/`; components `code/datums/components/_component.dm`; typecache + LAZY list helpers `code/__HELPERS/_lists.dm`; timers/init hints `code/__DEFINES/subsystems.dm`; traits `code/__DEFINES/traits/`.
- **Idiom notes**: `seconds_per_tick`; `::` operator in use; movement via move manager (grep `move_manager` — the `SSmove_manager` global was reworked; verify current form before citing); ~1600 files use RegisterSignal — signals are the primary extension seam.
- **Layer rule**: it *is* upstream — modular-fork rules do not apply; PRs here follow upstream guides directly.

## BandaStation-Kagelite_DEV

- **Family**: current tg derivative (ss220club BandaStation), Russian-localized. `tgstation.dme`.
- **Local law**: root `AGENTS.md` declares itself + in-repo `ai_navigation/` the authoritative agent instructions — follow them (router-first navigation, risk classification via `human_checking.md`, no build-graph changes without approval).
- **Layers**: `code/**` = upstream mirror; `modular_bandastation/**` = fork overlay, compiled last, overrides core. Check the overlay for overrides after finding anything in `code/`.
- **Toolkit**: effectively tg-identical (same guides, same defines layout, ~1580 RegisterSignal files); tg tier-3 applies nearly 1:1, but placement of changes goes through the modular overlay per tgstation-modular-content.

## cmss13-MARINES

- **Family**: hard fork (Colonial Marines); no upstream tracking, no modular root — the whole tree is fork-owned; edits to `code/` are normal here. `colonialmarines.dme`.
- **Era**: guides are an older tg snapshot: `delta_time` argument naming, `sanitizeSQL`-style guidance, `.proc/xyz` still being phased out (`PROC_REF` exists — use it). Own `STANDARDS.md`/`STYLES.md` in `.github/guides/`.
- **Dialect**: `tgui_interact` (not `ui_interact`); moderate signal usage (~300 files); own pragma safety net `code/__pragmas.dm` (lint categories as compile errors — respect it, CI runs it).
- **Extra local rule**: "convert division to multiplication where trivial" (`x * 0.5` over `x / 2`) appears in their standards — a micro-rule tg dropped; follow it there, don't export it.

## CEV-Eris

- **Family**: own architectural branch (Eris lineage, Bay ancestry far back); hard fork, no modular root. `cev_eris.dme`.
- **Structure quirks**: subsystems live in `code/controllers/subsystems/` (plural — path differs from tg); tg-style dcs exists but is *marginal* (~40 files use RegisterSignal) — the living idioms are proc overrides and direct calls; don't build signal-driven designs where no one sends signals.
- **UI**: `CONTRIBUTING.md` mandates NanoUI over raw browse; a `tgui/` tree also exists — determine which stack the touched system uses before UI work and follow it (flag the ambiguity to the user).
- **Process**: top-down development — significant features need design approval; balance changes in 15–25% steps; deprecated systems listed in CONTRIBUTING (Datacore, old PDAs, single-function consoles).
- **Style**: own guide in CONTRIBUTING.md (full paths, no inline control statements, TRUE/FALSE, spacing rules, "no unnecessary trailing return"). Follow it over tg style here.

## Twilight-Axis

- **Family**: Stonekeep/RogueTown lineage (medieval-fantasy total conversion; Azure-Peak heritage), still merging its upstream. `roguetown.dme`.
- **Layer decay (critical)**: three modular generations coexist (`modular/`, `modular_deserttown/`, `modular_twilight_axis/`) while most recent commits edit `code/` directly; legacy edit tags from dead lineages (`AZURE EDIT`, `CIT CHANGE`, …) are fossils. Do your own work modularly in the *active* root, but verify per `git log` and flag the decayed convention to the user rather than presenting any folder as law. (Full case study: tgstation-modular-content → references/fork-comparison.md.)
- **Toolkit**: tg skeleton present, moderate signal usage (~305 files); pre-`seconds_per_tick` era; no `SpacemanDMM.toml` at root — lint expectations are weaker; total-conversion content (no space-station assumptions — combat, stats, and interaction models are bespoke; read the local system before porting tg gameplay logic).
- **Navigation**: a workspace semantic base exists for this repo (discovered via semantic-controller; base folder `ai_navigation_twilight` at the workspace level).

## Vanderlin

- **Family**: tg-like Stonekeep/RogueTown descendant — same medieval domain as Twilight-Axis but far closer to modern tg engineering. `vanderlin.dme`.
- **Layers**: single modular root `modular_abel/` with the **aggregator include** pattern (one `.dme` line → `_module.dm` → per-feature `_xxx.dm`); new files register in the relevant aggregator, not the `.dme`.
- **Toolkit**: strong tg discipline: ships `HARDDELETES.md`, `SpacemanDMM.toml`, biome/bun tgui toolchain, OPENDREAM-gated pragmas; heavy signal usage (~540 files). tg tier-3 mostly applies; placement per tgstation-modular-content.
- **Navigation**: workspace semantic base `ai_navigation_vanders_river` (note its `engine_limits.md` carries known outdated engine claims — see source-index.md → Corrections).

## Style dialects summary

| Aspect | tg / Banda | cmss13 | Eris | Twilight | Vanderlin |
|---|---|---|---|---|---|
| Style authority | `.github/guides` | own snapshot of tg guides | CONTRIBUTING.md | none coherent — mimic file | tg-like (+ HARDDELETES) |
| process() delta arg | `seconds_per_tick` | `delta_time` | n/a mostly | `delta_time`-era | `delta_time`-era |
| UI entry | `ui_interact` | `tgui_interact` | NanoUI (+partial tgui) | mixed/legacy | `ui_interact` |
| Change placement | upstream rules / modular overlay (Banda) | direct, fork-owned | direct, fork-owned + approval culture | active modular root (decayed) | `modular_abel` aggregators |
| Signals as living idiom | yes | moderate | **no** | moderate | yes |

## Porting between forks

1. Port the **behavior contract**, not the diff: identify what the change does in terms of lifecycle hooks, signals, and data — then re-express it in the target's idiom (a tg signal listener may become a proc override on Eris).
2. Check every referenced symbol exists in the target (defines, signals, helpers like LAZYADD/typecacheof, subsystems) — same-name procs may have different signatures/eras; read the target's definition, don't assume.
3. Re-place the change per the target's layer rules (table above).
4. Translate dialect: delta arg naming, UI entry proc, `::` availability (target BYOND version), PROC_REF availability on pre-515 trees.
5. Re-run the review checklist against the *target*'s guides, not the source's.
