# File Specs — the DNA of a semantic base

Per-file specification sufficient to regenerate any base file from the codebase alone, without copying an existing base. Format per file: **Q** = the question an agent opens it for; **Contains** = required sections; **Source** = generated (from commands) vs authored (from reading code); **Drift** = fast / medium / slow / policy (see `integrity.md`).

Skip any file whose underlying system the target repo lacks (see `bootstrap.md` §Assessment). Every file that lists concrete paths must only list paths that exist at generation time.

## Tier 0 — Entry

### SKILL.md
**Q:** "Should an agent load this base at all, and where does it enter?"
**Contains:** frontmatter (`name: <repo>-ai-navigation`, pushy triggering description naming the repo and task types); core rules (code is truth; cheapest entrypoint first; check overlay after core); entry-points table (need → file); refresh workflow summary; current anchors table (domain → live repo route). **Source:** authored. **Drift:** slow.

### AGENTS.md
**Q:** "I was handed this repo with a goal — how do I start?"
**Contains:** terminology note (navigation layer ≠ in-game maps `_maps/**`/`SSmapping`); truth disclaimer (routing aid, may lag one refresh cycle, code wins, report mismatches); start-mode table — Fast (`router.md`) / Guided (this file) / Maintenance (`update_policy.md`); guided bootstrap steps (open router → exactly 1 helper → ≤2-3 source files → check overlay branch → escalate only if unresolved); project facts (project file, overlay layer, docs-only warning); pointers to `DEVELOPER_GUIDE.md`, `task_templates.md`. **Source:** authored. **Drift:** slow.

### start_matrix.md
**Q:** "Which entrypoint is cheapest for this situation?"
**Contains:** situation → start-with → then table (~8 rows); repo guardrails (project file, overlay path). **Source:** authored. **Drift:** slow.

## Tier 1 — Routing

### router.md  (keep under 3 KB — it is read constantly)
**Q:** "Which single helper file do I open for task X?"
**Contains:** "Always" table (pre-edit risk check → `human_checking.md`; Navigation Miss rules: absent from docs ≠ absent from code, verify with `rg`, flag the gap); dispatch table task-pattern → helper file (or direct repo path for domains with an obvious single home). Every target must exist. **Source:** authored. **Drift:** slow, but validate every refresh.

### router_deep.md
**Q:** "Router didn't resolve it / task touches performance or timing."
**Contains:** budget rules (1 helper, ≤2 sources, overlay check, approval gates); memorize-these engine constraints (tick budget, per-tick costs, reference-after-sleep, iteration hazards). **Source:** authored. **Drift:** slow.

### entrypoints.md
**Q:** "Keyword/feature → which directory first?"
**Contains:** minimal-route procedure (match row → open listed dirs → escalation ladder to debug_routes/system_dependencies/runtime_flow/subsystem_map); fast index table: keywords → open first → then check → runtime owner. One row per major gameplay domain. **Source:** authored from system_map + grep confirmation. **Drift:** fast.

### debug_routes.md
**Q:** "User reports a symptom, not a system."
**Contains:** symptom → open first → then check → likely owner table covering this repo's ~12 most common failure categories (startup/mapload runtimes, ability does nothing, combat chain breaks, movement wrong, effect never expires, wrong role/loadout, stale UI values, AI decisions wrong, tick freeze, visual/overlay lag + repo-specific domains). **Source:** authored. **Drift:** medium.

### task_templates.md
**Q:** (human, not agent) "How do I write a good task brief for this repo?"
**Contains:** header redirecting agents to router; default routing rule block; copy-paste templates: minimal fast task, bugfix, feature/content, refresh — each with Goal/Context/Constraints/Verification skeleton + repository-guidance line. **Source:** authored. **Drift:** policy.

## Tier 2 — Ownership

### architecture.md
**Q:** "How is this repo put together; which layer owns what?"
**Contains:** composition model (engine, lineage, include-graph shape, overlay position in include order); runtime backbone (world → master → subsystem discovery → scheduler contract; the atom-init bridge); domain layers (top-level dirs with one-line roles); engine-constraint bridge note (tick budget ↔ subsystem work). **Source:** authored. **Drift:** slow.

### system_map.md
**Q:** "Fast index of systems before opening source."
**Contains:** repository hotspots (family, project file, overlay packs, largest module slices by file count — generated); type-path counts for the ~10 hottest roots (generated); major systems table: system → primary dirs → runtime owner → notes. Header: "Last validated YYYY-MM-DD". **Source:** mixed; counts generated. **Drift:** fast.

### subsystem_map.md
**Q:** "Which SS* owns this; where is its file?"
**Contains:** generated header (total declarations, macro-family breakdown, `SUBSYSTEM_DEF(X)` → `SSX` naming rule); category summary table; complete index: SS global → kind → category → type path → file. Plus a prose block for the atom lifecycle (Initialize/LateInitialize/`INITIALIZE_HINT_LATELOAD`) — the single most repeated confusion. **Source:** generated (`rg "^(SUBSYSTEM_DEF|PROCESSING_SUBSYSTEM_DEF|...)\("`) + authored categories. **Drift:** fast.

### modular_guide.md
**Q:** "Where does fork content go and what are the overlay rules?"
**Contains:** overlay dir(s) and their include position (with `.dme` line evidence); what may/may not be edited in core; edit-marker conventions; how to check whether `modular` extends a core branch. Fork facts only — the mergeability *method* lives in the `tgstation-modular-content` skill; link it. **Source:** authored. **Drift:** slow.

### type_index.md
**Q:** "Given a BYOND type path, cheapest route to its home."
**Contains:** major roots table (root → usually means → open first); high-value branches table (branch → open first → then check) for the ~15 branches tasks actually hit. **Source:** authored. **Drift:** medium.

### type_tree.md
**Q:** "Deep inheritance for one specific path." (Search it, never read whole — it is the largest file.)
**Contains:** generated full type tree from `rg "^/(datum|mob|obj|turf|area)"`. Header states generation date + command. **Source:** generated. **Drift:** medium; regenerate, never hand-edit.

## Tier 3 — Reasoning

### runtime_flow.md
**Q:** "Order of execution / lifecycle, not file location."
**Contains:** canonical flows, each as: typical chain (arrow line) → runtime owners → open first → use when. Minimum set: world bootstrap + scheduler start; atom init lifecycle; round flow to role/antag assignment; player spawn; input→action→effect; signal/component reaction path; movement. **Source:** authored. **Drift:** medium.

### system_dependencies.md
**Q:** "Change crosses systems — which owners to inspect together?"
**Contains:** one table: system → depends on / hands off to → runtime owner → primary paths. One row per major system. **Source:** authored from system_map. **Drift:** medium.

### failure_modes.md
**Q:** "Owner known, break mode unclear."
**Contains:** scale-first classification (one object / one family / whole subsystem); per-scope catalog of break modes (blocking call in fire path, dropped from processing list, timer never set, cleanup path divergence, silent engine abort with its symptoms). **Source:** authored. **Drift:** slow.

### runtime_errors.md
**Q:** "Concrete runtime error text → diagnosis route."
**Contains:** common runtime patterns (null access after sleep, bad index, qdel/harddel, type mismatch) → likely cause → route; GC/del contract pointers into `coding_standards.md`. **Source:** authored. **Drift:** slow.

### processing_hazards.md
**Q:** "A whole process-driven system stalls with no runtimes."
**Contains:** use-when list; red-flag blocking calls inside `process()/tick()/fire()` (`sleep`, `do_after`, `input`, `alert`, `browse`, walk-family, `waitfor`); safe async escape hatches; debug order (owner → fire path → blocking sweep → only then blame load); cheap `rg` patterns. **Source:** authored. **Drift:** slow.

## Tier 4 — Contracts

### signal_map.md
**Q:** "What signals exist here; who sends/listens?"
**Contains:** generated stats header (active defines, referenced, with SEND sites, with Register sites); definition-files table (file → define count); local/file-scoped defines with notes; full index: signal → define file → SEND file count → Register file count; how-to-use table routing to domain maps. **Source:** generated from `COMSIG_*`/`SEND_SIGNAL`/`RegisterSignal` scans. **Drift:** medium; regenerate.

### combat_signal_map.md / movement_signal_map.md / spell_signal_map.md
**Q:** "Proc-and-signal contract for this domain."
**Contains:** the domain's proc chain (e.g. click → pre_attack → attackby → afterattack) interleaved with the signals fired at each step, plus the files owning each link. Build only for domains that are actually signal-driven in this repo. **Source:** authored from signal_map + source reading. **Drift:** medium.

### core_procs.md
**Q:** "Main proc families to keep in mind before broad search."
**Contains:** lifecycle procs (New/Initialize/Destroy/qdel); interaction hooks; combat hooks; per-family one-line use-when. **Source:** authored. **Drift:** slow.

### engine_limits.md
**Q:** "What does the engine itself constrain?"
**Contains:** tick system (tick_lag, world.cpu, overtime); client input limits; loop abort behavior; appearance/network flood mechanics; reference invalidation after sleep. **Source:** authored (engine knowledge + local settings). **Drift:** slow.

### performance_gotchas.md
**Q:** "Which local patterns are known to burn the budget?"
**Contains:** numbered local hazards with the idiomatic fix (`CHECK_TICK`/`MC_TICK_CHECK`, static lists, typed `as anything` loops, START/STOP_PROCESSING discipline, overlay churn) — each tied to real local idioms, verified present. **Source:** authored. **Drift:** slow.

## Tier 5 — Policy

### human_checking.md
**Q:** "Does this edit need human approval first?"
**Contains:** risk tiers no/low/medium/high with repo-calibrated examples (high = subsystems, shared roots like `/obj/item`, per-tick hooks, global signals); default rule (unclear scope ⇒ ≥ medium); approval gates per tier; the 5 blast-radius questions to ask the human. **Source:** authored policy. **Drift:** policy.

### coding_standards.md
**Q:** "Local style, GC contract, CI expectations."
**Contains:** naming/style rules actually enforced here; qdel/Destroy/harddel contract; signal registration hygiene; walk/delta-time idioms; CI pipeline facts if present. **Source:** authored from local docs + CI configs. **Drift:** policy.

### content_creation.md / content_breakdown.md / content_patterns.md
**Q:** "New mechanic/content: how to scope, decompose, and pick the implementation shape."
**Contains:** creation — workflow from request to narrowest host (define audience/frequency first; prefer cheapest trigger surface before components/global hooks); breakdown — delivery/base/delta/effect decomposition for vague requests; patterns — catalog of local implementation shapes (subtype vs component vs element vs status effect vs signal listener) with when-to-use. **Source:** authored policy. **Drift:** policy.

### tgui_guide.md
**Q:** "Fork facts for UI work." (Invariants live in the `ss13-tgui` skill — link, don't duplicate.)
**Contains:** owner table (SStgui, /datum/tgui, extension procs, states, inputs, panel — with live paths); entry proc name in THIS fork; component import path; route registration mechanism; local UI policies (e.g. Azure's localization pipeline is a base-level requirement no cross-fork skill knows). **Source:** authored. **Drift:** medium.

### visuals_guide.md / icon_rendering.md
**Q:** "Appearance, overlays, planes, filters / icon smoothing and caches."
**Contains:** owner subsystems with paths; local rendering pipeline facts; recolor/sprite-layer recipes; smoothing flags and cache mechanics. Build only if the repo has nontrivial visual systems. **Source:** authored. **Drift:** slow.

### update_policy.md
**Q:** "How to refresh this base or migrate the layer to another codebase."
**Contains:** the base's own maintenance manual: Navigation Miss Protocol (verbatim rule + a worked example); drift-speed table; staged rebuild order with per-stage commands; refresh validation checklist; original collection commands; migration part (preserve the reasoning model, pre-migration assessment, what to drop/keep). Keep this file even though this skill exists — the base must be self-maintaining when handed to an agent without this skill. **Source:** authored policy. **Drift:** policy.

### DEVELOPER_GUIDE.md
**Q:** (human) "How do I attach an agent to this layer?"
**Contains:** what the layer is/is not; the 3 start modes; minimum handoff pattern (goal first, then repo + guidance); bilingual if the team is. **Source:** authored. **Drift:** policy.

## Deep maps (optional, per large subsystem)

### <subsystem>/AI_NAVIGATION.md
**Q:** "Everything about one big subsystem before touching it."
**Contains:** freshness header (path + date); start rules; agent TL;DR table (task → open first → adjacent layers); include/compile map; file-by-file module composition; data model with source-of-truth statements; runtime flows (arrow chains); impact map ("change X → check list"); development protocol (no isolated edits; before/after checklists); gotchas; common recipes; fast search commands.
Place it **with the subsystem** (subdirectory named after it), not at base root — a root-level deep map for one subsystem misleads routing. **Source:** authored; the most expensive artifact, justified only for subsystems with 10+ files and cross-layer coupling. **Drift:** medium.
