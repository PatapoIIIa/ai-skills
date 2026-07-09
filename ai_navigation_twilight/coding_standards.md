# Coding Standards

- Code wins over this guide.
- Prefer `modular_twilight_axis/**` for Twilight-local changes.
- Destroy/qdel: unregister signals, stop processing, clear refs, then call parent as local pattern requires.
- `ui_act` params are hostile; validate type/range/membership server-side.
- Per-tick/process/fire paths must not block on `sleep`, `do_after`, `input`, `alert`, `browse`, or long synchronous icon work.
- For browser/TGUI assets, use `/datum/asset` + `ui_assets()` + `resolveAsset()`/`get_asset_url()`; bind with `$ss13-tgui`.

Tooling facts: `roguetown.dme`, `BUILD.cmd`, `tgui/package.json` using Bun scripts. Compile/build/checks are human-controlled in this workspace.
