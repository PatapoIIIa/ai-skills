# Failure Modes

| Scope | Common break mode | First route |
|---|---|---|
| One object | state var, component, local signal, do_after ref | owner source file |
| One feature family | overlay/core split, duplicated type branch, stale route | entrypoints.md + modular_guide.md |
| Whole subsystem | processing membership, fire loop, init order | subsystem_map.md + processing_hazards.md |
| Whole UI class | TGUI framework/bundle/browser asset issue | tgui_guide.md + $ss13-tgui |
| Whole server/client class | engine/browser/config/environment | runtime_errors.md, engine_limits.md |
