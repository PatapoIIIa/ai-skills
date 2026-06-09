# Update And Migration Policy

This is the `Maintenance Start` entrypoint for monthly refreshes, post-drift rebuilds, and migration to another codebase.

## Terminology

- `navigation layer` / `AI mapping` / `repository mapping` = docs in `ai_navigation/` plus `ai_navigation/AGENTS.md`
- does NOT mean in-game map files, `_maps/**`, `code/modules/mapping/**`, or `SSmapping`

For ordinary feature work, do not start here. Use `ai_navigation/router.md` instead.

---

# Part 1 — Monthly Refresh

## Ground Rules

- Source files are the authority. Navigation docs are hints only.
- Never treat existing navigation docs as ground truth during a refresh.
- If a navigation doc and code disagree, update the doc to match the code.
- Do not modify source files during a refresh unless explicitly asked.

## Navigation Miss Protocol (applies during ALL work, not just refreshes)

Navigation docs drift. A missing or wrong entry does not mean the thing doesn't exist.

**When a navigation lookup fails or gives a suspicious result:**

1. **Do not conclude the thing doesn't exist.** Say "navigation may be stale here" and verify directly.
2. **Grep the source** before making assumptions:
   ```
   # SS* subsystem
   rg -rn "SUBSYSTEM_DEF(atoms)" code/controllers/subsystem
   # type or proc
   rg -rn "/obj/structure/fake_machine" code/ -g "*.dm" -l
   # any keyword
   rg -rn "LateInitialize" code/ -g "*.dm" -l
   ```
3. **If grep confirms it exists** — use the real file, not the navigation entry.
4. **Tell the user** that navigation was stale and what you found.
5. **Propose a navigation fix** so the same miss doesn't happen again.

**Example of the failure this prevents:**
Navigation had `SSatoms` listed as "Handles atoms" with no lifecycle detail. AI assumed `LateInitialize` had no mechanism and invented a workaround instead of reading `code/controllers/subsystem/atoms.dm`. Correct behavior: notice the thin entry, grep for `LateInitialize`, find `atoms.dm`, read it, use `INITIALIZE_HINT_LATELOAD`.

## What Drifts First

Not all files drift at the same rate. Check in this order:

| Drift speed | Files | Why |
|---|---|---|
| Fast (every sprint) | `entrypoints.md`, `subsystem_map.md`, `system_map.md` | New systems, new SS*, renamed paths |
| Medium (monthly) | `signal_map.md`, `combat_signal_map.md`, `spell_signal_map.md`, `movement_signal_map.md`, `runtime_flow.md` | Signal contracts change with new features |
| Slow (quarterly) | `architecture.md`, `router.md`, `core_procs.md`, `processing_hazards.md` | Structural changes are rare |
| Rarely | `human_checking.md`, `content_creation.md`, `content_patterns.md`, `coding_standards.md` | Policy files, not derived from code |

**Minimal monthly refresh:** stages 2 and 4 only (runtime ownership + system routing). This covers 80% of routing value in ~20% of effort.

## Rebuild Order

### Stage 1 — Repository shape (only if architecture may have changed)
- verify top-level directories, major languages, modular overlay paths
- confirm `modular_rmh` still acts as a late-included overlay
- confirm `.dme` include order has not changed
- **skip this stage if no structural changes were made this month**

### Stage 2 — Runtime ownership ⬅ always refresh
- rebuild `ai_navigation/subsystem_map.md`:
  ```
  rg -n "^(SUBSYSTEM_DEF|PROCESSING_SUBSYSTEM_DEF|TIMER_SUBSYSTEM_DEF|MOVEMENT_SUBSYSTEM_DEF|AI_CONTROLLER_SUBSYSTEM_DEF|VERB_MANAGER_SUBSYSTEM_DEF)\(" code/controllers/subsystem -g "*.dm"
  ```
- verify each SS* global still matches a real file
- update the Quick Lookup category anchors if categories shifted

### Stage 3 — Type structure (only if major type trees changed)
- rerun type path extraction from `.dm` files
- refresh `ai_navigation/type_tree.md` and `ai_navigation/type_index.md`
- update type counts in `ai_navigation/system_map.md` header
- **skip if no significant new type hierarchies were added**

### Stage 4 — System routing ⬅ always refresh
- refresh `ai_navigation/system_map.md` — verify every system section still points to real paths:
  ```
  rg --files code/modules | sort > /tmp/current_modules.txt
  rg --files code/datums  | sort > /tmp/current_datums.txt
  # diff against entries in system_map.md
  ```
- refresh `ai_navigation/entrypoints.md` — walk each row, verify "Open first" paths exist
- check `ai_navigation/router.md` dispatch table — verify every target file exists

### Stage 5 — Runtime reasoning (refresh if signal contracts or lifecycle changed)
- `ai_navigation/system_dependencies.md` — verify cross-system handoffs still accurate
- `ai_navigation/runtime_flow.md` — verify round flow, SS* init order still correct
- `ai_navigation/debug_routes.md` — verify symptom → route mappings still lead to the right files

### Stage 6 — Contract helpers (refresh if relevant domain changed)
- `ai_navigation/signal_map.md` — recheck SEND_SIGNAL / RegisterSignal hotspot counts:
  ```
  rg -c "RegisterSignal\(" code modular_rmh -g "*.dm" | awk -F: '{sum+=$2} END{print sum}'
  rg -c "SEND_SIGNAL\(" code modular_rmh -g "*.dm" | awk -F: '{sum+=$2} END{print sum}'
  ```
- `ai_navigation/spell_signal_map.md`, `combat_signal_map.md`, `movement_signal_map.md` — verify proc names and signal defines still match source
- `ai_navigation/core_procs.md`, `processing_hazards.md`, `failure_modes.md` — verify examples still compile

### Stage 7 — Workflow helpers (refresh only if policy changed)
- `ai_navigation/human_checking.md`, `content_creation.md`, `content_breakdown.md`, `content_patterns.md`
- `ai_navigation/task_templates.md`, `ai_navigation/AGENTS.md`
- `ai_navigation/coding_standards.md`, `ai_navigation/visuals_guide.md`, `ai_navigation/tgui_guide.md`
- `ai_navigation/modular_guide.md` — verify modular_rmh directory structure still matches

## Refresh Validation Checklist

Run before closing a refresh:

- [ ] every file referenced in `router.md` dispatch table exists
- [ ] every "Open first" path in `entrypoints.md` points to a real directory or file
- [ ] every SS* in `subsystem_map.md` has a real file mapped
- [ ] `architecture.md` Runtime Ownership Quick Reference matches current SS* set
- [ ] `AGENTS.md` Start Mode Selection table still accurate
- [ ] no source files were modified (docs-only task)
- [ ] `system_map.md` header says "Last validated YYYY-MM-DD"

## How The Navigation Layer Was Originally Collected

For the next agent doing a full rebuild from scratch:

```
# 1. repo shape
rg --files --glob "*.dm" | head -20  # sanity check structure

# 2. subsystem declarations
rg -n "^(SUBSYSTEM_DEF|PROCESSING_SUBSYSTEM_DEF|TIMER_SUBSYSTEM_DEF|MOVEMENT_SUBSYSTEM_DEF|AI_CONTROLLER_SUBSYSTEM_DEF|VERB_MANAGER_SUBSYSTEM_DEF)\(" code/controllers/subsystem -g "*.dm"

# 3. type path extraction (pipe to file, then sort/count by root)
rg -n "^/(datum|mob|obj|turf|area)" code modular_rmh -g "*.dm" | grep -v "//"

# 4. signal defines
rg -rn "^#define COMSIG_" code/__DEFINES -g "*.dm"

# 5. signal call sites
rg -c "SEND_SIGNAL\("     code modular_rmh -g "*.dm"
rg -c "RegisterSignal\("  code modular_rmh -g "*.dm"
rg -c "UnregisterSignal\(" code modular_rmh -g "*.dm"

# 6. hot proc families
rg -n "^/(mob|datum).*/proc/(Initialize|Destroy|process|fire|attack|move)" code -g "*.dm" | head -100

# 7. component / status effect call sites
rg -c "AddComponent\("         code modular_rmh -g "*.dm"
rg -c "apply_status_effect\("  code modular_rmh -g "*.dm"
```

Build stable contracts and runtime owners first. Do not attempt exhaustive file listings.

---

# Part 2 — Migration To Another Codebase

## Core Principle

Preserve the **reasoning model**, not the file names or paths.

The value of this navigation layer is not the specific routes — it is the layered approach: cheap routing first, deep reference second, contracts before exhaustive search.

## Pre-Migration Assessment

Before writing a single file, answer these questions about the target repo:

| Question | If yes | If no |
|---|---|---|
| Does it have a type hierarchy (inheritance tree)? | Build `type_tree` + `type_index` | Replace with nearest registry or class list |
| Does it have a scheduler / subsystem model? | Build `subsystem_map` around it | Replace `subsystem_map` with service-owner map |
| Does it have a signal / event system? | Build `signal_map` around it | Replace with callback/hook/event map |
| Does it have a modular overlay layer? | Build `modular_guide` | Remove overlay-specific guidance entirely |
| Does it have a dominant language? | Use its idioms in all examples | — |
| Does it have a CI pipeline? | Document it in `coding_standards` | Skip CI section |

**Do not invent a contract helper if the target repo has no stable equivalent.** A fake signal_map for a repo without signals wastes more tokens than it saves.

## Migration Order

Build in this sequence. Each stage depends on the previous.

### Stage 1 — Orientation layer
Files: `architecture.md`, `modular_guide.md` (if applicable)

- map the top-level directory structure
- identify the runtime backbone (equivalent of Master + SS*)
- identify the extension/overlay model (equivalent of modular_rmh)
- document the include/build order
- do NOT route anything yet — just describe the shape

### Stage 2 — Ownership layer
Files: `subsystem_map.md` (or equivalent)

- identify every runtime owner (scheduler, service, singleton)
- map each owner to its file and its domain
- this is the single most important file for routing accuracy

### Stage 3 — Routing layer
Files: `system_map.md`, `entrypoints.md`, `router.md`

- build `system_map.md` from the ownership layer
- build `entrypoints.md` as a keyword → directory index
- build `router.md` as a minimal dispatch table (target: under 3 KB)
- verify every route in `router.md` points to a real file

### Stage 4 — Reasoning layer
Files: `runtime_flow.md`, `system_dependencies.md`, `debug_routes.md`

- document the lifecycle (boot → ready → round → teardown or equivalent)
- document cross-system dependencies and handoffs
- build `debug_routes.md` from the most common symptom categories in this repo

### Stage 5 — Contract helpers (only what the target repo actually has)
Files: signal maps, core_procs, processing_hazards, failure_modes

- build only the contracts that have stable equivalents
- name them after the target repo's idioms, not after BYOND/DM terminology
- if the target repo uses events instead of signals, call the file `event_map.md`

### Stage 6 — Workflow helpers
Files: `human_checking.md`, `content_creation.md`, `content_patterns.md`, `coding_standards.md`

- adapt risk tiers to the target repo's scale and team size
- adapt content patterns to the target repo's dominant implementation shapes
- adapt coding standards to the target language and CI pipeline

### Stage 7 — Entry files
Files: `router.md` (final pass), `AGENTS.md`

- do a final pass on `router.md` to ensure every row resolves
- write `AGENTS.md` with the correct start modes for the target repo
- remove any rows or sections that have no equivalent in the target

## Migration Validation Checklist

- [ ] every file in `router.md` dispatch table exists in the migrated layer
- [ ] `subsystem_map` (or equivalent) covers all major runtime owners
- [ ] `entrypoints.md` has at least one row per major gameplay domain
- [ ] `debug_routes.md` covers the 5 most common failure symptom categories
- [ ] no BYOND/DM-specific terminology remains unless the target also uses BYOND
- [ ] `AGENTS.md` reflects the target repo's actual structure, not this one's

## What To Drop, What To Keep

| Element | Keep if | Drop if |
|---|---|---|
| `type_tree.md` / `type_index.md` | Target has deep inheritance | Target is flat or uses composition-only |
| `subsystem_map.md` | Target has a scheduler or service model | Target is purely reactive / event-driven with no owners |
| `signal_map.md` | Target has a publish-subscribe or signal system | Target uses direct calls only |
| `modular_guide.md` | Target has a late-include or plugin overlay | Target is monolithic |
| `spell_signal_map.md` / `combat_signal_map.md` | Target has spell-like and combat-like systems | Target has no equivalent |
| `human_checking.md` | Target has shared hot paths and risk tiers matter | Target is a solo project with no blast-radius concerns |
| `coding_standards.md` | Target has documented or discoverable style rules | Standards are purely external (linter-only) |

## Rule Of Thumb

- Monthly refresh: always do stages 2 and 4. Skip the rest if time is short.
- Migration: always do stages 1–3 before anything else. The routing layer is useless without the ownership layer.
- In both cases: cheap routing first, deep reference second.
