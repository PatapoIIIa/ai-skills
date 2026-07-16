# Coding Standards

Updated 2026-07-16. Universal DM/tg conventions (style, lifecycle, signals, GC/harddel patterns, macros, security, optimization) now live in the **byond-ss13-coding** skill — `references/style-and-review.md`, `references/ss13-architecture.md`, `references/dm-language-and-runtime.md`. Do not re-learn them here; this file keeps only what is specific to this repository.

The navigation layer may lag behind the live documents. If this file and the repo's own docs disagree, trust the repo docs.

## Repo-specific facts

- The repo ships its own copies of tg-derived guides: `STANDARDS.md`, `STYLE.md`, `CI.md`, `HARDDELETES.md` — they are the local authority over the skill's tier-3 defaults.
- **Delta-arg naming caution:** the shipped guides use tg's `seconds_per_tick` wording, but live subsystem code in this lineage uses the older `delta_time` naming — match the actual signature of the proc you override, not the guide.
- **Movement manager caution:** the guides' `SSmove_manager` tables are inherited from tg; verify the symbol exists here (`grep -rn "move_manager" code/`) before recommending it — this lineage may keep a different or older movement API.
- Appearance caching helpers (`iconstate2appearance`-style) exist — see `code/controllers/subsystem/overlays.dm`.
- Hard-delete debugging: enable `REFERENCE_TRACKING_STANDARD` in `_compile_options.dm`; output lands in `[log_dir]/harddels.log` inside the round's log folder.

## Continuous Integration (repo pipeline)

CI runs on every PR; failures block merge:

| Stage | What it checks |
|---|---|
| **Run Linters** | Files included in `.dme`, spelling, map formatting. If "Run Linters" fails but "Annotate Lints" passes, check "Annotate Lints" for the actual error — it also appears in the "Files Changed" tab. |
| **Compile Maps** | All maps (including ruins) compile cleanly. Passes here + fails below = code compiles but doesn't work. |
| **Integration Tests** | Round starts, tests run on every station map. Any runtime = failure. Map-specific failures → map-specific bug or a flaky test (ask maintainer to re-run). |
| **Screenshot Tests** | Appearance regressions. Auto-posts before/after diff on the PR if something changes visually. |
| **Codeowner Reviews** | Alerts contributors that their file was changed. Not a test — if it fails, contact a maintainer. |

*Cross-references: → `visuals_guide.md` (visual systems), → `performance_gotchas.md` (hazard→anchor map), → `signal_map.md` (signal routing), → `human_checking.md` (risk gating).*
