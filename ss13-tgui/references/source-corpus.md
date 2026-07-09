# Source Corpus: comparative map across five SS13 forks

Read this to calibrate "is this rule universal or fork-local?" before applying any other reference. It records what was actually sampled, classifies findings by how far they generalize, and is the evidence base for the rules in `SKILL.md` and the other references. Paths are read-only references — do not edit application repos.

## Repos sampled (provenance)

| Repo | Role here | Sampled snapshot | tgui-core? | Backend entry proc | Components import |
| --- | --- | --- | --- | --- | --- |
| tgstation | Canonical modern /tg/ baseline | June 2026 | yes (^5.10) | `ui_interact` | `tgui-core/components` |
| Vanderlin | tgui-core fork and reviewed redesign sample | June 2026 | yes (^5.6) | `ui_interact` | `tgui-core/components` |
| Bubberstation | /tg/-derived tgui-core fork with modular preferences examples | June 2026 | yes (^5.10) | `ui_interact` | `tgui-core/components` |
| cmss13-MARINES | Independent codebase, older port | April 2026 | **no** | **`tgui_interact`** | **`tgui/components`** (local) |
| BandaStation-Kagelite_DEV | /tg/-derived fork-of-fork | May 2026 | yes (^5.10) | `ui_interact` | `tgui-core/components` |

The single most important takeaway from this table: **the same component vocabulary and lifecycle ride on top of fork-local names and import paths.** cmss13 renamed the framework entry proc to `tgui_interact` (169 files vs 16 `ui_interact`) and ships its components in-tree at `tgui/components` instead of depending on `tgui-core`. An agent that hardcodes `ui_interact` + `tgui-core/components` from memory will write code that does not compile in cmss13. Always grep a neighboring interface in the *current* repo for the entry-proc name and the component import path before writing.

## Framework source (the ground truth, /tg/)

Lifecycle claims in this skill are verified against /tg/ framework source, not folklore:

- `code/modules/tgui/external.dm` — the `ui_*` proc contracts and their docstrings (`ui_data`, `ui_static_data`, `update_static_data`, `update_static_data_for_all_viewers`, `update_data_for_all_viewers`, `ui_assets`, `ui_act`, `ui_close`).
- `code/modules/tgui/tgui.dm` — `process()` (the autoupdate loop, ~1/sec, re-calls `ui_interact`), `on_act_message()` (`if(ui_act(...)) SStgui.update_uis(src_object)`), `autoupdate` var, `set_autoupdate()`.
- `code/controllers/subsystem/tgui.dm` — `try_update_ui()`, `get_open_ui()` (dedup is per `(user, src_object)` over `src_object.open_uis`), `update_uis()` (fans out to every open UI for the object, including observers/admins).

These files exist with the same shape in Vanderlin and BandaStation. cmss13's equivalents live under `code/modules/tgui/` too but the public proc is `tgui_interact`.

## Backend examples sampled

- tgstation: `code/game/machinery/announcement_system.dm` (clean `ui_interact` + split static/dynamic + `ui_act`), `code/game/machinery/autolathe.dm`, `code/modules/research/machinery/_production.dm` and `code/modules/research/rdconsole.dm` (real `ui_assets` returning spritesheets; rdconsole carries the comment *"heavy data from this proc should be moved to static data when possible"*), `code/game/machinery/computer/operating_computer.dm` (batched `update_static_data_for_all_viewers()`), `code/modules/power/apc/apc_main.dm` (`SStgui.update_uis(src)` on external state change).
- Bubberstation: `modular_skyrat/master_files/code/modules/client/preferences/middleware/languages.dm` (preferences middleware returning a spritesheet from `get_ui_assets()` and sanitized sprite keys in data), `limbs_and_markings.dm` (action delegations, preview body updates, static refresh only when option dependencies change), and one bad-pattern sample where `try_update_ui` was used as a control-flow lookup and called twice.
- Vanderlin: a corrected datum-backed interface using the standard open path, split static/dynamic data, and `SStgui.update_uis(src)` at the external mutation site (see the anonymized case study).
- cmss13: `code/game/machinery/computer/camera_console.dm`, `demo_sim.dm`, `dropship_weapons.dm` (all `tgui_interact`).
- BandaStation: same `ui_interact` shape as /tg/ (430 files); spot-checked against /tg/ equivalents.

Counts (proc definitions found): `try_update_ui` present in essentially every interface; `ui_static_data` used in ~210 (tgstation), ~209 (BandaStation), ~86 (cmss13), ~11 (Vanderlin) files — i.e. common in large mature codebases, used where payloads are heavy, **not** in every interface.

## Frontend examples sampled

- tgstation: `interfaces/Canister.tsx` (typed `Data` with `BooleanLike`, `useBackend<Data>()`, `Window` layout — the canonical idiom), `interfaces/AntagInfoHeretic.tsx` (one of the ~18/299 files that deliberately use a raw `<div>` for free-form text).
- Vanderlin: a large custom skills interface (imports from `tgui-core/components`; the sampled version still had extensive raw HTML and a thousand-plus-line SCSS file, making frontend cleanup the remaining work).
- cmss13: `interfaces/Vending.tsx`, `interfaces/PowerMonitor.tsx` (import `Box/Button/Section/Stack/Table` from local `tgui/components`, `useBackend` from `tgui/backend`, `Window` from `tgui/layouts` — same vocabulary, local source).
- BandaStation: `interfaces/Vending.tsx`, `interfaces/AirAlarm.tsx` (`tgui-core/components`, /tg/-identical idiom).
- Bubberstation: `tgui/packages/tgui/interfaces/PreferencesMenu/**` and neighboring core interfaces (`tgui-core/components`, `useBackend` from local `tgui/backend`, same modern route/component vocabulary as /tg/).

Observed everywhere: components from a single import (`Box`, `Button`, `Section`, `Stack`, plus `Window` layout), `const { act, data } = useBackend<Data>()`, a TypeScript `type Data = {...}` contract using `BooleanLike` for DM booleans. Raw `<div>/<span>/<button>` is the rare exception (~6% of /tg/ interfaces), reserved for free-form content no component models well.

## Browser asset delivery / CDN notes

July 2026 pass over tgstation, Bubberstation, and BandaStation-Kagelite_DEV found the same browser-asset pattern in all three: `config/resources.txt` exposes the optional `ASSET_TRANSPORT webroot`, `ASSET_CDN_WEBROOT`, and `ASSET_CDN_URL` settings; `/datum/asset_transport/webroot` serves files through `SSassets.transport.get_asset_url()`; `/datum/asset/*/get_url_mappings()` serializes `asset/mappings`; and TGUI resolves those mappings through `resolveAsset()`. Static UI images, JSON catalogs, fonts, CSS, and spritesheets therefore go through `/datum/asset` plus `ui_assets()` instead of hardcoded browser paths.

Bubberstation and BandaStation modular examples follow the same rule rather than inventing fork-local delivery: modular preference/language spritesheets, minesweeper assets, nanomap/navigator assets, and title-screen browser files all use the asset cache or `SSassets.transport.get_asset_url()`. The important negative example is also consistent: `browse_rsc()` remains in all three for generated/ephemeral images such as photos, admin/debug icons, and preview images. That is not a CDN gap; it is the right shape for data that is created per interaction or is not worth registering as a static asset.

Twilight-Axis spot-check (July 2026, not part of the original corpus table) supports the same concept. It has asset transport config entries, `asset/mappings` handling in `tgui/packages/tgui/assets.ts`, and TGUI screens such as `ManorPanel` and `OriginPicker` register `/datum/asset/simple` datums in `modular_twilight_axis` while frontend code references those names with `resolveAsset()`. It also retains older direct browser/resource paths in non-TGUI browse popups, so treat it as partially modernized rather than evidence that every browser file should be routed through TGUI assets.

## Classification of findings

### Stable cross-repo principles (true in all sampled forks; safest defaults)
- Open with `ui = SStgui.try_update_ui(user, src, ui)` then `if(!ui)` create+`open()`. (Entry proc is `ui_interact` everywhere except cmss13's `tgui_interact`.)
- One UI per `(user, src_object)`; the framework pools/dedupes via `src_object.open_uis`. No custom dedup, no stored UI ref on the datum.
- `ui_act` returning truthy triggers `SStgui.update_uis(src_object)` — independent of autoupdate.
- For state changed outside `ui_act`, call `SStgui.update_uis(src)` at the change site.
- Backend ships domain data; frontend owns presentation.
- Component vocabulary: `Box`, `Button`, `Section`, `Stack`, `Window`, `useBackend` — same names, same roles.
- Typed `Data` contract on the frontend with `BooleanLike` for DM bools.
- Assets go through the asset/spritesheet pipeline (`ui_assets`); webview caches them per session.

### /tg/-canonical patterns (true in tgstation, mirrored by BandaStation; adopt when the local repo uses tgui-core)
- Components imported from `tgui-core/components`; no in-tree component library.
- `ui_static_data` for heavy/rarely-changing payloads (and call `update_static_data()` to push changes); `ui_data` for dynamic state. Used widely but selectively — heavy UIs, not every UI.
- `Window` + `Window.Content` layout wrapper.
- Light theming is a global override of the base tgui-core theme and "just works" when interfaces use tgui-core correctly.

### Bubberstation-local conventions
- tgui-core fork (^5.10), `ui_interact`, `tgui-core/components`; most /tg/ lifecycle and component rules transfer directly.
- Modular preferences work often routes through `datum/preference_middleware` with `action_delegations`, `get_ui_data()`, `get_ui_assets()`, and targeted `character_preview_view.update_body()` calls.
- Spritesheet asset keys are often sanitized CSS class names from backend data. Treat these as asset handles, not arbitrary presentation classes.
- Do not copy examples blindly: fork-local modules can contain local bugs or one-off patterns. Use them to learn conventions, then verify against framework docs/source.

### Vanderlin-local conventions
- tgui-core fork (^5.6), `ui_interact`, `tgui-core/components` — tracks /tg/.
- New "paper"/guidebook-style interfaces should build on the existing shared stylesheet rather than invent a parallel palette (see the anonymized case study).
- Small interface set (~22), so "read the neighbors" means a smaller sample — widen to /tg/ when local examples are thin.

### cmss13-local conventions (do NOT transfer to tgui-core forks)
- Entry proc is `tgui_interact`, not `ui_interact`.
- Components/`useBackend`/`Window` come from local `tgui/components`, `tgui/backend`, `tgui/layouts` — there is no `tgui-core` dependency. Styling lives in-tree, so per-component style edits are a thing here in a way they are not in tgui-core forks.
- Same lifecycle and same component vocabulary otherwise — patterns transfer at the *concept* level, not the *import* level.

### BandaStation-local conventions
- Essentially /tg/-aligned (`ui_interact`, `tgui-core/components`, `Window`). Its "advanced" work is additive on top of the /tg/ baseline rather than a divergent convention, so /tg/ patterns transfer directly. Still diff against /tg/ before assuming a given helper is upstream — it is a fork-of-fork.

### Anti-patterns (seen or warned against; all have a one-line framework-native fix)
- Custom open-UI scanner / duplicate-window guard (framework dedupes via `try_update_ui`).
- Calling `SStgui.try_update_ui()` in an `if` guard and then calling it again to get a UI; assign once in the entry proc or use an explicit framework helper for exceptional control flow.
- Long-lived `datum/tgui` ref stored on a gameplay datum (zero such vars in /tg/ outside framework loop iterators; updates go through `update_uis`).
- Autoupdate off **without** a clean update path; custom update wrapper proc instead of `SStgui.update_uis(src)`.
- Generation counter / per-user "dirty" cache keyed on an update count (bad cache key; on-demand updates rarely need it).
- Global cache of a trivial pure op over a tiny static set (e.g. ~20 sanitized icon names).
- Backend emitting presentation (CSS classes, layout anchors, display labels derivable in TS).
- Raw HTML where a component fits; ~1000+ line SCSS re-implementing layout tgui-core already does; absolute-pixel layout; a bespoke scaling control duplicating an existing UI-scaling var.

### Uncertain / verify-locally
- **Caching shared immutable static data globally is acceptable; per-user dynamic data is not.** In the reviewed redesign, a same-for-everyone metadata payload cache survived while a per-user dynamic cache and generation counter were removed. The dividing line: is the cached value identical for all users and effectively immutable? Then a global cache is fine. Verify the value really is shared and immutable before trusting one.
- **Sending a sanitized spritesheet CSS-class string from the backend** sits on the data/presentation boundary: the class is the asset-pipeline handle for a sprite, not arbitrary styling. Acceptable when it mirrors the spritesheet key; reconsider if it encodes layout. Verify against how sibling interfaces reference spritesheet sprites.
- Whether a given interface *needs* the static/dynamic split: depends on payload size. Don't add it reflexively to a small UI.
