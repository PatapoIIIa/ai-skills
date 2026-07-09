# TGUI Guide

Generated on 2026-07-09. This file contains Twilight-Axis local facts. For framework invariants and review rules, bind with `$ss13-tgui`.

## Binding With `$ss13-tgui`

Local facts:

- Backend entry proc is `ui_interact(mob/user, datum/tgui/ui)`; `tgui_interact` is not the normal path here.
- TGUI backend framework lives in `code/modules/tgui/**`; subsystem owner is `SStgui` in `code/controllers/subsystem/tgui.dm`.
- Frontend interfaces live in `tgui/packages/tgui/interfaces/**`.
- Components usually import from `tgui-core/components`; a few low-level widgets import from local `tgui/components`.
- Static browser/TGUI assets use `/datum/asset`, `ui_assets()`, `asset/mappings`, and frontend `resolveAsset()`; optional webroot CDN config is in `config/resources.txt`.

Verify first:

```powershell
rg -n "ui_interact\(|ui_assets|resolveAsset|asset/mappings" code modular_twilight_axis tgui -g "*.dm" -g "*.tsx" -g "*.ts"
rg -n "tgui-core/components|tgui/components" tgui/packages/tgui/interfaces -g "*.tsx" -g "*.jsx"
```

## Owners and Paths

| Owner | Path |
|---|---|
| SStgui subsystem | code/controllers/subsystem/tgui.dm |
| /datum/tgui | code/modules/tgui/tgui.dm |
| /datum/tgui_window | code/modules/tgui/tgui_window.dm |
| ui_* proc contracts | code/modules/tgui/external.dm |
| TGUI frontend app/store | tgui/packages/tgui/store.ts |
| Asset resolver | tgui/packages/tgui/assets.ts |
| Interface files | tgui/packages/tgui/interfaces/** |
| Asset cache backend | code/modules/asset_cache/** |
| CDN config | config/resources.txt |


## Observed Counts

| Signal | Files containing it |
|---|---|
| ui_interact | 120 |
| ui_assets | 10 |
| resolveAsset | 17 |
| asset/mappings | 3 |
| ByondUi | 5 |


## Local Examples

- Manor UI: backend `modular_twilight_axis/manors/code/manor_tgui.dm`, frontend `tgui/packages/tgui/interfaces/ManorPanel.tsx`, assets registered as `/datum/asset/simple/manor`.
- Origin picker: backend `modular_twilight_axis/code/modules/client/preferences.dm`, frontend `tgui/packages/tgui/interfaces/OriginPicker.tsx`, map image registered as `/datum/asset/simple/origin_picker`.
- Family tree UI: backend `modular_twilight_axis/familytree_module/familytree_prefs_ui.dm`, frontend `tgui/packages/tgui/interfaces/FamilyDisplayPanel.tsx`, `tgui/packages/tgui/interfaces/FamilyDisplayPanel/**`, and `tgui/packages/tgui/interfaces/FamilySettingsPanel.tsx`.
