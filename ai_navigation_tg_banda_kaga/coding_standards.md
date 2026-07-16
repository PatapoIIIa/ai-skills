# Coding Standards

Updated 2026-07-16. Conventions for `BandaStation-Kagelite_DEV`. Universal DM/tg conventions (lifecycle contract, signals/components/elements, PROC_REF discipline, GC/harddel patterns, performance rules, macro hygiene, security) live in the **byond-ss13-coding** skill — `references/style-and-review.md` and `references/ss13-architecture.md`. The linters and CI are authoritative — if this file and tooling disagree, trust the tooling and update this file.

## Quick decision table (fork routing)

| Situation | Rule |
|---|---|
| Any DM implementation/review question | byond-ss13-coding skill (universal), then this file for local placement |
| New fork feature | a `modular_bandastation/` module (`ai_navigation/modular_guide.md`) |
| Touching `code/**` shared roots | classify risk first (`ai_navigation/human_checking.md`) |
| Long loop | `CHECK_TICK` (general) or `MC_TICK_CHECK` (inside `fire()`) — paths in `engine_limits.md` |

## Style & formatting (local tooling)

- DM files: **tab** indentation, **LF** line endings, UTF-8 (`.editorconfig`). `.dm`, `.json`, `.md` use tab indent; other files space indent — follow `.editorconfig`.
- `SpacemanDMM.toml` enforces `disallow_relative_type_definitions` and `disallow_relative_proc_definitions` — declare full absolute type/proc paths.
- Prefer typed vars over the ambiguous `.` member operator so DreamChecker can verify.

## File placement (fork layers)

- Upstream-shaped code → `code/**` matching the existing tree.
- Fork features → a `modular_bandastation/<module>/` module; add each file to the module's `_<module>.dme`.
- Fork-wide components belong in `modular_bandastation/~components`.
- New compile-time defines → `code/__DEFINES/**` (core) or `_defines220` (fork-wide).
- Adding/removing include lines in `tgstation.dme` or a module `.dme` is a build-graph change — get explicit approval.

## SQL

- All DB access goes through `SSdbcore` (`code/controllers/subsystem/dbcore.dm`); parameterised queries only (`:param` placeholders). Schema changes require a migration under `SQL/**`.

## TGUI

See `ai_navigation/tgui_guide.md` and the **ss13-tgui** skill. In short: data via `ui_data`/`ui_static_data`, never trust `ui_act` params (validate server-side), the React component name must match the `.tsx` filename.

## Continuous Integration

CI (`.github/workflows/ci_suite.yml` → `run_linters.yml`) runs, among others:

| Check | What it enforces |
|---|---|
| DreamChecker (SpacemanDMM) | DM static analysis — type/proc-path errors, unused vars |
| OpenDream compile (`--define=CIBUILDING`) | the project compiles under OpenDream |
| `__odlint.dm` / `tools/ci/od_lints.dm` | extra `#pragma` lints under OpenDream |
| define sanity / trait validity | `tools/define_sanity`, `tools/trait_validity` |
| ticked-file enforcement | every `.dm` file is included in the `.dme` |
| grep checks | `tools/ci/check_grep.sh` — banned patterns |
| map / maplint checks | `_maps/**` integrity |
| TGUI checks | `tools/build/build.sh --ci lint tgui-test` (Biome + tests) |
| changelog check | a changelog entry exists |

JS/TS/CSS in `tgui/` is formatted and linted by **Biome** (`biome.json`): tab indent, single quotes, `var` banned, organise-imports on.

Run locally before pushing: `BUILD.cmd` (compile) and the tgui lint via `tools/build`.
