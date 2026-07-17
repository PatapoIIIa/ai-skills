# Update Policy

Generated on 2026-07-09.

## Navigation Miss Protocol

1. Do not conclude absence from a missing route.
2. Grep the Twilight-Axis repository directly.
3. Use what code says.
4. Update this base so the miss does not repeat.

## Refresh Order

1. Fast tier: `entrypoints.md`, `subsystem_map.md`, `system_map.md`, `router.md`.
2. Medium tier: `signal_map.md`, focused signal maps, `runtime_flow.md`, `system_dependencies.md`, `debug_routes.md`, `type_index.md`, `type_tree.md`.
3. Slow/policy tier: architecture, modular guide, coding standards, human checking, content docs, visuals, engine/performance docs.
4. Registry: update the workspace registry's row for Twilight-Axis — the registry's own location is local to this machine (see `byond-codemaster-controller`), never hardcode its path here.
5. Installed skill: if Codex should auto-discover this base, maintain a junction from this machine's own Codex skills directory to wherever this ai-skills repository's `ai_navigation_twilight` folder actually lives. Both ends are local to whoever runs this — never hardcode a username or a disk path here.
