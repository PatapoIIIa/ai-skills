# Integrity — keeping bases honest

A base drifts from the moment it is written. Integrity control has four parts: validation (paths resolve), freshness (drift-tiered refresh), sync (master = deployed), parity (base has the files its repo deserves).

## Validation

```bash
python scripts/validate_semantic_base.py <base-dir> --repo <repo-root> [--repo <root2>] [--strict]
```

Checks every backtick path reference in the base against the base dir and the repo root(s); knows to skip BYOND type paths (`/datum/...`), define alternatives, and placeholder names. Treat hits as **leads, not lint failures** — a MISSING route is either real drift (fix the doc) or intentional shorthand (leave it). Run after every refresh, every bootstrap, and whenever a base is suspected stale. `--strict` also lists bare filenames it could not resolve.

## Post-task feedback (mandatory)

Drift is discovered by tasks, not by calendars. Every task that used a base ends by flushing the binding brief's `Conflicts/gaps` line to the registry's "Known drift / parity backlog" (one dated line each). Fix trivial one-liners in the base immediately in the same task; batch the rest. Trigger a fast-tier refresh when a base accumulates several backlog entries or any load-bearing miss (a fact that would have produced non-compiling code) — that base is actively lying, and the next agent may not verify as carefully.

The freshness spot-check at discovery (SKILL.md §Discovery, step 6) is the other half of this loop: backlog entries tell the next session to distrust literals from that base before it even starts.

## Drift tiers and refresh

| Speed | Files | Refresh trigger |
|---|---|---|
| Fast | `entrypoints.md`, `subsystem_map.md`, `system_map.md` | every refresh — this trio is ~80% of routing value for ~20% of effort |
| Medium | signal maps, `runtime_flow.md`, `system_dependencies.md`, `debug_routes.md`, `type_index/tree`, `tgui_guide.md`, deep maps | when the domain changed |
| Slow | `architecture.md`, `router.md`, `core_procs.md`, `engine_limits.md`, `failure_modes.md`, `processing_hazards.md` | structural change only |
| Policy | `human_checking.md`, `coding_standards.md`, content trio, `task_templates.md`, `update_policy.md`, `DEVELOPER_GUIDE.md` | policy change only |

Refresh procedure:

1. Regenerate generated files from their stamped commands (never hand-edit counts/indexes).
2. Re-verify authored routes in the fast tier; walk each row, confirm targets exist.
3. Run validation; fix real drift it surfaces.
4. Update "Last validated YYYY-MM-DD" stamps.
5. Re-sync deployed copy; `diff -rq <master> <deployed>` must be empty.
6. If files were added/removed: update the base's own `router.md` dispatch, its `SKILL.md` entry table, and the controller registry.

During any refresh, existing base docs are **not** ground truth — the code is. If a doc and code disagree, the doc changes.

## Navigation Miss Protocol (applies during ALL work)

When a base lookup fails or looks suspicious:

1. Do not conclude the thing doesn't exist — say "navigation may be stale here".
2. Grep the source directly; if found, use the real file, not the base entry.
3. Tell the user the base was stale and what was found.
4. Fix the base entry (or propose the fix if out of scope) so the same miss doesn't repeat.

The failure this prevents: a thin `SSatoms` entry once led an agent to invent a workaround instead of reading `atoms.dm` and finding `INITIALIZE_HINT_LATELOAD`. Thin entry → grep → read → use the mechanism.

## Sync protocol

- Default layout: a single copy at `<repo>/ai_navigation/` — nothing to sync.
- If the workspace registry records a master copy outside the repo (legacy/multi-repo layouts): every edit lands in the master first, then re-deploys. A deployed-only edit will be silently overwritten at next sync — treat any `diff -rq` noise as an incident: reconcile before continuing, never blind-overwrite either side.
- A base whose docs self-reference `ai_navigation/...` but which is not deployed at that path inside the repo has broken self-links — either deploy it or record the gap explicitly in the registry.

## Parity audit

Bases built at different times have uneven file sets. Audit against `file-specs.md`: for each spec file, either the base has it, or the repo lacks the underlying system (fine — note it), or it is a genuine gap (backlog it). Uneven parity is acceptable; *undocumented* parity gaps are not, because an agent that trusts the taxonomy will search for a file that was never built.

Record audit findings (drift, parity gaps, dates) in the workspace registry's "Known drift / parity backlog" section — findings are machine state and never belong in this skill.

## Retirement

When a repo leaves the workspace: remove the base's registry row, archive or delete the base copies. A registry row pointing at a dead repo poisons dispatch.
