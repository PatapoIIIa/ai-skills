# Bootstrap — build a semantic base from zero

For a codebase that has no base yet, including one never seen before. The output is a new base at `<repo>/ai_navigation/` that satisfies `file-specs.md`, plus a row in the workspace registry (`ai_navigation_registry.md`, see SKILL.md §Discovery).

Preserve the **reasoning model**, not file names: cheap routing first, deep reference second, contracts before exhaustive search, code always outranks docs. The file set flexes; the model does not.

## Stage 0 — Assessment (before writing anything)

Classify the codebase and decide which spec files apply:

| Question | How to answer | If yes | If no |
|---|---|---|---|
| What family/lineage? | root project file (`*.dme` for BYOND), README, CI configs | reuse family idioms in all examples | describe from scratch |
| Deep inheritance tree? | scan type declarations | `type_index` + `type_tree` | replace with registry/class list |
| Scheduler / subsystem model? | look for master-controller equivalent | `subsystem_map` | service-owner map instead |
| Signal / event system? | grep signal/event define patterns | `signal_map` (+ domain maps for signal-driven domains only) | callback/hook map instead |
| Late-included overlay layer? | include order in the project file | `modular_guide` | omit overlay guidance entirely |
| Web-UI framework (tgui)? | `tgui/` dir or equivalent | `tgui_guide` (fork facts; link `ss13-tgui`) | omit |
| Nontrivial rendering pipeline? | overlay/lighting subsystems | `visuals_guide` / `icon_rendering` | omit |
| CI / enforced style? | workflow configs, lint configs | fold into `coding_standards` | note "linter-only" and move on |

**Never invent a helper for a system the repo lacks** — a fake signal map costs more tokens than it saves. Record assessment answers at the top of `architecture.md`.

The assessment table works for non-BYOND codebases too: answer each row with the target stack's equivalents (scheduler → service container, signals → event bus, overlay → plugin dir) and keep only the reasoning model. The command block below is family-specific — replace it, don't force it.

For BYOND/DM repos, the raw collection commands:

```bash
rg --files --glob "*.dm" | head -20                      # shape sanity check
rg -n "^(SUBSYSTEM_DEF|PROCESSING_SUBSYSTEM_DEF|TIMER_SUBSYSTEM_DEF|MOVEMENT_SUBSYSTEM_DEF|VERB_MANAGER_SUBSYSTEM_DEF)\(" code/controllers/subsystem -g "*.dm"
rg -n "^/(datum|mob|obj|turf|area)" code modular* -g "*.dm" | grep -v "//"   # type paths
rg -n "^#define COMSIG_" code/__DEFINES -g "*.dm"        # signal defines
rg -c "SEND_SIGNAL\(|RegisterSignal\(" code modular* -g "*.dm"               # call sites
rg -c "AddComponent\(|apply_status_effect\(" code modular* -g "*.dm"         # composition hotspots
```

## Stages 1-7 — Build order

Each stage depends on the previous; the routing layer is useless without the ownership layer. Per-file content requirements are in `file-specs.md` — this is the sequence and the exit criteria.

1. **Orientation** — `architecture.md` (+ `modular_guide.md` if overlay exists). Describe the shape; route nothing yet. *Exit: include order and runtime backbone stated with file evidence.*
2. **Ownership** — `subsystem_map.md` (or service-owner equivalent). Generated index + authored categories. The single highest-value file for routing accuracy. *Exit: every owner maps to a real file.*
3. **Routing** — `system_map.md` → `entrypoints.md` → `router.md` (<3 KB). *Exit: every route target exists (`validate_semantic_base.py` clean on these files).*
4. **Reasoning** — `runtime_flow.md`, `system_dependencies.md`, `debug_routes.md` (from this repo's actual common symptoms, not a copied list).
5. **Contracts** — only those that passed assessment: `signal_map` (generated), domain signal maps, `core_procs`, `engine_limits`, `performance_gotchas`. Stamp each generated file with date + command.
6. **Policy** — `human_checking.md` (risk tiers calibrated to this repo's scale), `coding_standards.md`, content trio, `tgui_guide.md`/visual guides as applicable. Link architecture skills; do not duplicate them.
7. **Entry** — final `router.md` pass; `AGENTS.md`, `start_matrix.md`, `SKILL.md`, `task_templates.md`, `DEVELOPER_GUIDE.md`, `update_policy.md` (the base's self-maintenance manual — write it even though this skill exists, so the base survives being handed to an agent without it).

Minimum viable base (when time is short): tier 0 + `router.md` + `architecture.md` + ownership map. Add the rest when a real task would have used it — note deferred files in the base `SKILL.md`.

## Finalize

1. Validate: `python scripts/validate_semantic_base.py <base> --repo <repo-root>` → zero missing.
2. Stamp: "Last validated YYYY-MM-DD" in `system_map.md` header; generation stamps on all generated files.
3. **Deploy**: the base lives at `<repo>/ai_navigation/` (its docs self-reference that path). If the workspace convention keeps a master copy outside the repo, deploy a byte-identical copy and record both locations in the registry.
4. **Register**: add a row to `ai_navigation_registry.md` at the workspace root (create the file from the template in SKILL.md if this is the first base): base path, repo(s), project file, overlay layer, deploy location, notes.
5. Smoke-test: give a fresh agent one realistic task brief (from `task_templates.md`) and check it reaches the right source files through the base within ~3 file opens. A base that fails its smoke test routes worse than no base.
