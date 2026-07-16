# Engine Limits

Universal BYOND/Dream Daemon runtime facts (tick model, threading, GC, list/appearance/network costs, numeric limits) now live in the **byond-ss13-coding** skill — `references/dm-language-and-runtime.md` for semantics and `references/performance.md` for costs. That skill's copy is verified against the official DM Reference (2026-07) and supersedes the Designer's-Guide-derived text this file used to carry; three of the old claims were corrected there (bitwise ops are 24-bit, max view ~70×70, `sleep(0)`/`spawn(0)` are sub-tick — see the skill's `references/source-index.md` §Verification results).

Keep in this file only limits *specific to this repo* (none recorded yet — add fork-measured numbers here, e.g. its `world.fps`, map size, mob population ceilings, with the measurement date).

*Cross-references: → `performance_gotchas.md` for this repo's hazard→anchor map. → `router.md` for task dispatch. → `processing_hazards.md` for subsystem freeze diagnosis. → `visuals_guide.md` for appearance/overlay details. → `coding_standards.md` for repo conventions.*
