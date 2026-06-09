# Start Matrix

Use this file to choose the cheapest navigation entrypoint for an AI agent working in Azure-Peak.

| Situation | Start with | Then |
|---|---|---|
| Normal implementation/debug task | `ai_navigation/router.md` | Pick one helper from the dispatch table. |
| Symptom-first bug report | `ai_navigation/debug_routes.md` | Escalate to `runtime_flow.md` or `system_dependencies.md` only if needed. |
| Feature/content request with known shape | `ai_navigation/content_creation.md` | Use `entrypoints.md` for source locations. |
| Vague content request | `ai_navigation/content_breakdown.md` | Then choose implementation shape through `content_patterns.md`. |
| Signal-driven or component/element behavior | `ai_navigation/signal_map.md` | Use specialized maps for spell/combat/movement. |
| Exact BYOND type path | `ai_navigation/type_index.md` | Use `type_tree.md` only for inheritance depth. |
| Explicit subsystem question | `ai_navigation/subsystem_map.md` | Verify the SS name against source declarations before using it. |
| Navigation layer migration/refresh | `ai_navigation/update_policy.md` | Regenerate maps from the current repo, not the source repo. |

## Azure-Peak Guardrails

- Current project file: `roguetown.dme`.
- Current modular layer: `modular/**`.
- Keep navigation routes focused on existing `code/**` and `modular/**` paths.
