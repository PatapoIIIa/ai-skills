# Human Checking

| Tier | Examples |
|---|---|
| No approval needed | Read-only inspection; updating this navigation snapshot. |
| Low risk | Single localized DM/TGUI file with obvious owner and no compile/test run. |
| Medium risk | Shared type branches, combat/movement/spells, economy, jobs, mapload, TGUI framework, or core `code/**` edits. |
| High risk | Subsystem scheduler, master controller, global signals, qdel/GC, project include order, database schema, deployment, broad refactors. |

Unclear scope defaults to medium. Ask the human what blast radius they approve before edits.
