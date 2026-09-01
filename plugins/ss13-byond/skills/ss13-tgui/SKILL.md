---
name: "ss13-tgui"
description: "Use only for SS13 TGUI/web UI work: implementing, reviewing, or debugging a tgui interface; ui_interact/tgui_interact/ui_data/ui_static_data/ui_assets/ui_act/ui_state; SStgui lifecycle; tgui interfaces/routes/layouts/components/SCSS; tgui-core or in-tree components; the BYOND browser bridge (ByondUi, winset/winget/callByond, config.window/config.ref, embedded maps/camera controls); browser asset cache/CDN delivery (/datum/asset, resolveAsset, get_asset_url, ASSET_TRANSPORT webroot, ASSET_CDN_*); tgui dev-server/HMR; duplicate or blank/white tgui windows; WebView2/IE/DPI/Wine runtime triage; skin.dmf/window-control breakage; first-load or per-update tgui performance; overengineered tgui refactors. Do not use for ordinary SS13 DM gameplay, content, or systems work (mobs, items, icons, balance, admin verbs, database, mapping) or generic BYOND code, unless the request or changed files also touch TGUI or BYOND browser UI integration."
---

# SS13 TGUI Interfaces

Review, implement, simplify, and debug TGUI interfaces in BYOND/DM + React codebases. The goal is correct, idiomatic, **codebase-native** TGUI — not bespoke machinery that reimplements what the framework already does.

## Activation guard

Use this skill only when the request or changed files include a TGUI-specific signal: `tgui/` frontend files, `ui_interact`/`tgui_interact`, `ui_data`, `ui_act`, `SStgui`, tgui components, TGUI SCSS, `ByondUi`, `winset`/`winget`/`callByond`, embedded map/camera controls, tgui dev-server/routing work, or runtime symptoms such as blank/white TGUI windows, WebView2/IE, DPI scaling, Wine/Linux browser issues, client cache/resources, or `skin.dmf`/window-control breakage. If the task is normal SS13 DM content or systems work with no UI/webview bridge, do not apply this skill — that is `byond-ss13-coding`'s domain. This skill owns everything past the `ui_data`/`ui_act` boundary. When more than one skill could apply, `byond-codemaster-controller` settles the order — don't re-derive it here. If the task is ambiguous, inspect the changed paths and nearest procs before leaning on these rules.

**This includes pure ideation/mockup requests, not just code changes.** "Sketch what this panel could look like," "can we show the character live," "mirror their pose in the UI" are this skill's domain from the message that first raises them — a design conversation with no diff yet still anchors the eventual implementation, so the map_view-first hierarchy (below) must be surfaced *before* any alternative is proposed, not retrofitted after the user has to ask "is there something for this in the skill?" Read the triggers loosely during ideation: a misspelling (`ByondUi` → "BYOND UI"), a paraphrase ("their appearance follows their actions"), or a component named only informally all count — don't wait for the exact token.

## The one root cause

Most TGUI mistakes share a single root: **assuming a capability is missing and hand-rolling it.** TGUI already pools windows, dedupes open UIs per user, caches assets in the webview, fans updates out to every viewer, and re-renders on `ui_act`. Before you add a helper, a cache, a counter, a window tracker, or a manual update path, find the framework mechanism you are about to duplicate. In real reviews the answer is almost always "one that already works," and the fix is *deletion plus a one-line framework call*.

When you catch yourself writing infrastructure (window scanners, dirty counters, asset caches, stored UI refs, scaling vars), stop and ask: *what local TGUI mechanism am I duplicating, and why did I assume it wasn't there?* That question prevents the entire class of errors this skill is built around.

## Approach (do these in order)

1. **Learn the local names before writing a line.** TGUI's *concepts* are stable across forks; its *names and import paths are not.* The backend entry proc is `ui_interact` in /tg/, Vanderlin, and BandaStation but `tgui_interact` in cmss13. Components come from `tgui-core/components` in tgui-core forks but from in-tree `tgui/components` in older ports (cmss13, older Azure-derived code, old tgstation tgui). Grep one neighboring interface in *this* repo and copy its proc name, route registration pattern, component import path, and its `useBackend`/`Window` imports. Memory from another fork will not compile here.
2. **Read 2-3 neighboring interfaces** (`.dm` + `.tsx` + `.scss`). Match their `ui_interact` shape, component usage, and styling. Local convention beats any external guide.
3. **Register the frontend where this generation requires it.** Older in-tree tgui uses a central `routes.js` table keyed by the DM interface name; missing route entries render a "Route entry missing" fallback. Modern forks may auto-discover or use a different routing table. Copy the local route/import/wrapper/theme pattern.
4. **Implement data-driven.** Backend sends *data*; frontend decides *presentation*. `ui_data()` for dynamic state; `ui_static_data()` for heavy, rarely-changing metadata (an optimization for big payloads — not mandatory for small UIs, and changing it requires an explicit `update_static_data()` push); `ui_assets()` for static assets.
5. **Keep the update path standard.** `ui_act` returning truthy already fires `SStgui.update_uis(src)`. For state changed *outside* `ui_act`, call `SStgui.update_uis(src)` at the change site. Nothing else.
   **Autoupdate is a per-tick tax, not a convenience default.** With `set_autoupdate(TRUE)`, `ui_data()` runs every SStgui tick for *every* open viewer — any catalog building, text cleaning, or icon work inside it burns CPU between user actions and re-serializes the full payload each tick. Prefer autoupdate OFF with pushes at change sites; if something genuinely needs ticking (a countdown), send one timestamp and count down client-side. If autoupdate must stay on, cache every expensive `ui_data` block and invalidate at the single funnel all mutations already pass through — the cache is then one null-assignment, not a signature zoo.
6. **Treat BYOND controls as a bridge, not React.** If the interface embeds a map/camera/control with `ByondUi`, inspect the local `ByondUi` and BYOND bridge source before changing it. Read `references/byond-ui-and-devserver.md`.
7. **Pick elements by semantics, then style minimally.** Decide what each element *is* (action, titled panel, layout block, inline text) and pick the construct whose behavioral contract matches — see the decision matrix below. Never blanket-replace HTML tags with `Box as="..."`; keep SCSS proportional to the problem.
8. **Triage runtime blank-window failures before code optimization.** If the report is white/blank windows, all popups broken, WebView2/IE, DPI scaling, Wine/Linux, client cache/resources, antivirus/disk blocking, or `skin.dmf`/window-control breakage, read `references/runtime-platform-triage.md` before blaming React render, `ui_data()`, or payload size.
9. **Measure before optimizing — and before theorizing.** No caches or counters without a demonstrated cost. For rendering/geometry mysteries, get one hard number (a `winget` probe, a frontend `getBoundingClientRect` report logged server-side) before building a model; one measurement outranks any number of consistent-looking screenshots, and stacked unverified assumptions were the root of the longest debugging saga this skill records (`references/embedded-map-geometry.md`).
10. **Fingerprint both build artifacts when field-testing.** A tgui fork ships a `.dmb` AND a tgui bundle; they go stale independently, and testing new DM against an old bundle fabricates false engine facts ("param X doesn't stick") that then poison notes and handoffs. Make the frontend echo a version marker into the backend log, check it before believing any "still broken" report, and record which build produced every conclusion you write down.
11. **Delete measurement scaffolding after it answers the question.** Temporary disk loggers, render counters, timing vars, and per-action traces are useful while diagnosing TGUI latency, but they are not part of the feature. Once performance is confirmed, remove the proc definitions, globals, call sites, and dead cache plumbing in the same cleanup pass.
12. **For broad reviews, run the read-only smell scan when it will save time.** `scripts/tgui_smell_scan.py` flags likely hotspots (`icon2base64`, manual UI refs, autoupdate off, temporary loggers, `useLocalState`, suspicious `Box as`, etc.). Treat hits as leads for inspection, not as linter failures.
13. **Review against the checklist below.**

## Standard backend pattern

```dm
// Entry proc name is fork-local: ui_interact (/tg/, Vanderlin, BandaStation) or tgui_interact (cmss13).
/datum/thing/ui_interact(mob/user, datum/tgui/ui)
	ui = SStgui.try_update_ui(user, src, ui)
	if(!ui)
		ui = new(user, src, "InterfaceName")
		ui.open()

/datum/thing/ui_static_data(mob/user)   // heavy/rarely-changing: names, descs, icon ids, structure
/datum/thing/ui_data(mob/user)          // dynamic: values, state, selection
/datum/thing/ui_assets(mob/user)        // spritesheets / simple assets via the asset pipeline
/datum/thing/ui_state(mob/user)         // interaction policy: range, consciousness, access, remote use
/datum/thing/ui_act(action, list/params, datum/tgui/ui, datum/ui_state/state)
	. = ..()
	if(.)
		return
	// Treat params as hostile: validate type/range/membership before mutation.
	// Handle actions; returning TRUE triggers SStgui.update_uis(src).
```

Do **not**: store a long-lived `datum/tgui` ref on the domain datum (zero such vars exist in /tg/ outside framework loops), scan/dedupe open windows with a custom helper, or grab one UI and `send_update()` manually when `SStgui.update_uis(src)` exists. `try_update_ui` already finds and refreshes the pooled UI for `(user, src)` — BYOND never truly closes windows, it minimises them. If duplicate windows can open, the standard open path is broken upstream; fix that, don't paper over it.

## Browser asset delivery

For static browser/TGUI assets, prefer the repo's asset pipeline over hardcoded file paths or ad-hoc `browse_rsc()` sends. Define a `/datum/asset/simple`, `/datum/asset/spritesheet`, or existing local equivalent, return it from `ui_assets()`, and reference it through transport-neutral URL helpers: TGUI `resolveAsset()` after `asset/mappings`, `asset.get_url_mappings()` for browse HTML, or `SSassets.transport.get_asset_url()` when DM composes HTML/data. This keeps the same UI working with both the default `browse_rsc` transport and `ASSET_TRANSPORT webroot` / `ASSET_CDN_*` deployments.

Use `/datum/asset/simple/namespaced` when CSS/HTML depends on relative `url(...)` files. Do not route everything through this subsystem: BYOND game resources (`.dmi`, sounds, maps) still belong to the normal resource/.rsc path; live doll/camera/minimap previews should use `ByondUi` map_view where available; per-change dynamic photos, debug icons, and rare one-offs can stay base64 or direct `browse_rsc()`. When adding one interface, register only the files it owns rather than creating a broad catch-all asset datum.

## Appearance preview pickers
Delivery mechanism is a hierarchy — pick by how the image changes, not by habit:

1. **Live, per-player, frequently-changing scene (character doll, camera, minimap): `ByondUi` map_view FIRST.** This is the priority target, not an exotic option. A `/atom/movable/screen/map_view` shows the preview mob natively (appearance streaming): zero encoding, zero payload in `ui_data`, instant updates, free rotation via `setDir`. `/tg/`'s `char_preview` is the canonical shape: the screen object owns a per-preferences dummy, `update_body()` sets `appearance = render_preview(body)`, tgui embeds it by `mapRef`. Fall back to flattened base64 only when the infra genuinely can't apply (no map_view in the fork, headless render, image must leave the client).
2. **High-cardinality static catalogs (style cards): `ui_assets()` + spritesheet** and a small static catalog of stable CSS class names. Do not send one base64 thumbnail per option through `ui_static_data()` once the spritesheet is authoritative; delete the old thumbnail proc and global cache instead of leaving a parallel path.
3. **Single un-composed icons (one `icon` + `icon_state`: item art, loadout cards): `DmIcon`** — tgui-core ships it (verified present in 5.6.0: icon ref + state + dir + frame + `fallback`); it renders straight from the icon resource with zero server flattening and zero data payload. It does NOT compose overlays — a dressed mob/character appearance is out of its reach (that is map_view's or a flatten's job). Verify the fork's tgui-core exports it and the backend hands out icon refs before recommending.
4. **Dynamic one-offs (photos, rare previews): base64 is fine** — and for *per-change dynamic* images the asset system is actively WORSE than base64: assets are generated and transported once by design, so a per-click preview would mean a new asset + a new client round-trip per change. Do not "migrate previews to assets" as a blanket rule; migrate catalogs to assets and live scenes to map_view. When a flattened single image is genuinely required and the fork is on BYOND 515+, `client.RenderIcon(atom)` beats server-side `getFlatIcon` on fidelity — it is the client renderer itself, so overlays, transforms, and filters can't drift — **but it composites without plane masters**, so emissive blockers baked into appearances render as literal grey/black overlays; /tg/ itself ships zero RenderIcon call sites for exactly this reason (caveat and workarounds in `references/byond-client-api.md`). **And its return is a cache-file reference, not an /icon datum** — savefile-based helpers (`icon2base64`-style `WRITE_FILE`) reject it with a client-side "Invalid argument" dialog and zero server runtime, and `icon(raw)` does not normalize it; deliver via `fcopy()`/asset transport only (field-tested; details in `references/byond-client-api.md`). Keep `getFlatIcon` for headless/CI paths and for atoms wearing emissive blockers.

The performance smell is **repeated base64 option catalogs** and synchronous thumbnail generation in hot paths; for many stable options, use assets/spritesheets plus ids.

**When a preview misbehaves, the symptom names the cause** — full diagnosis in
[references/appearance-previews.md](references/appearance-previews.md):
a flatten that returns **fully transparent** the moment the mob holds an item (the tg-family
`getFlatIcon` canvas-expansion bug, inherited by every tg-derived fork);
a preview where **matrix scales silently do nothing** (a hand-rolled flattener that never reads
`appearance.transform`); a dummy that **won't go nude or won't face south** (preview-only state
pushed through the validated preference pipeline, or `defdir` being ignored); and an option
catalog that **empties itself and stays disabled** on modular species.

## ByondUi / BYOND controls

Use `ByondUi` only for actual BYOND skin controls that must be layered over the browser, most commonly embedded maps/camera views — including the **map_view live-preview pattern above, which should be your default for character/scene previews** when the fork has the infra (grep the repo for `/atom/movable/screen/map_view` and `assigned_map` by **name, not path** — in current tgstation they sit in `code/_onclick/hud/screen_objects/map_view.dm` + `…/screen_objects/map_popups.dm`, and forks place them differently — then copy an existing `ByondUi` consumer such as a color-matrix editor or camera console). It is not a replacement for normal tgui `Button`, `Input`, `Section`, or HTML layout. In old in-tree tgui, `ByondUi` computes its DOM bounding box and calls BYOND `winset` with `id`, `parent`, `type`, `pos`, and `size`; on unmount/beforeunload it clears the control's `parent`. That means the React element is a positioning anchor, while the visible control is still BYOND-owned.

When using or reviewing it:

- Verify the repo actually has `ByondUi` or an equivalent component; modern/forked tgui may differ.
- Pass the BYOND control `type` required by the skin params, and a stable `id` from backend data when DM or another control must address the same control (camera consoles use a map ref). **Do not pass `parent: config.window` on tgui-core — it is legacy in-tree syntax.** The component itself calls `render({ parent: Byond.windowId, ...params })`, i.e. it supplies the current window automatically (and because your `params` spread lands *after*, an explicit `parent` still wins if you genuinely need a different one). Its own typings say so: `parent` — *"optional, defaults to the current window."* Confirmed across **tgstation (tgui-core 6.1.1, 10 ByondUi call sites, zero `parent`)** and **a Vanderlin-family fork (tgui-core 5.6.0, 2 call sites, zero `parent`)**. Canonical modern shape — tg's `common/CharacterPreview.tsx`: `<ByondUi width=… height=… params={{ id, type: 'map' }} />` and nothing more.
- Keep it in a stable, nonzero-sized container; old implementations update position on render and debounced window resize, not every scroll event.
- It is an OS-level child control composited OVER the WebView, not a DOM element: it cannot be made transparent, no CSS applies (filters, border-radius, textures), and it occludes every browser-drawn layer that intersects its rect — tooltips, tutorial/modal overlays, dimmers. "Zero visual degradation" is not achievable; plan the design around the rectangle instead: match its `background-color` param to the surrounding theme, and unmount the ByondUi while DOM overlays are open (unmount tears the control down, so the rectangle vanishes for the overlay's lifetime) rather than trying to z-index past it.
- Use `act()`/`ui_act` for gameplay mutations. Use raw `winset`/`winget`/`callByond` only for BYOND window/control properties or framework bridge code.
- Debug blank controls by checking route registration, `config.window`, id uniqueness, CSS/container size, clipping/scrolling, backing DM map/control setup, and local browser support before rewriting the interface.
- **If embedded map content renders tiny, off-center, or vanishes: read `references/embedded-map-geometry.md` before changing any code.** Dynamically-created secondary maps choose their world canvas by rules you don't control (field data: a skin-default 640×480 in most configurations, silently flipping to the object bounding box after an unrelated layout change) — so PIN the canvas with an invisible background spanning your whole intended frame, size via the `zoom` skin param (disables auto-fit; viewport centers on the canvas center), and measure with `winget view-size / zoom`. Never put volatile params like zoom in the ByondUi React `key` (remount = visible flash); update them via DM `winset` instead.
- For the skin-parameter vocabulary (map `zoom-mode`/`view-size`/`icon-size`, window `is-transparent`, global `winget(null, ...)`, `byondStorage`, client dot-commands) consult `references/byond-client-api.md` before inventing a workaround — the client usually already has the knob.
- **`ByondUi` phones home by default.** Verified in `tgui-core` source (`dist/components/ByondUi.js`, **byte-identical in 5.6.0 and 6.1.1**): `phonehome` defaults to on; each `render()` sends a `renderByondUi` Topic and each teardown sends `unmountByondUi`, registering/releasing the control for the server's crash-cleanup fallback. Synthetic `window.dispatchEvent(new Event('resize'))` retries multiply this across every mounted map (3 retries × 3 maps = 9 topics per interaction), eating the client's Topic rate budget. If DM owns the control lifecycle, pass `phonehome={false}` — positioning still works and the component still unparents on unmount/`beforeunload`. Not theoretical: a production Vanderlin-family fork ships `phonehome={false}` on all three of its character-preview maps. See "The client→server topic budget" in `references/performance-and-lifecycle.md`.
- **The component re-winsets on mount and window-resize only — never on prop change.** Its effect hook carries an *empty* dependency array (again identical in 5.6.0 and 6.1.1), so mutating `params` (zoom, size, id) after mount does nothing: no re-`winset`, no error, no visual change. This is the mechanical reason volatile params must be driven from DM by `winset` (or, worse, by a remount) — see the geometry-report recipe below and `references/embedded-map-geometry.md`. Position itself refreshes only via the 100 ms-debounced `resize` listener.

## Choosing frontend elements (decision matrix)

The same "don't hand-roll what the framework provides" rule applies to markup — and so does its inverse: don't strip contracts the platform provides. **Never mechanically find/replace HTML tags with `Box as="<tag>"`** — that loses native keyboard behavior, `type`/`aria-*`/`title` attributes, and SCSS element selectors while gaining nothing. Decide by what the element *is*:

- a user action → `Button` (custom look = `className` + SCSS over its chrome, not a rebuilt pseudo-button);
- a standard titled panel → `Section` with `title` / `buttons`;
- a block-level layout/style wrapper → `Box` (it renders a `<div>`; it is a CSS-utility primitive, not a universal HTML replacement);
- inline styled text with no specialized component → `Box as="span"` (the only `as` value common in /tg/ interfaces);
- semantic prose, typed native attributes, or a wrapper's ref contract (e.g. `Tooltip` clones its child and injects a `ref` that must land on a DOM node) → raw HTML, with a comment when non-obvious;
- unsure → read the component's implementation and 2-3 neighboring interfaces before choosing.

Adopting `Section`/`Button` must *delete* markup, CSS, or behavior code. If it would break a bespoke panel's DOM/scroll/sticky structure, or you'd neutralize all of the component's chrome while using none of its behavior, keep the simpler construct. Details and the lost-contract checklist: `references/components-and-style.md`.

## React patterns that survive tgui's render model

tgui is React, so general React advice applies — but only the part that survives this render model, and most published guidance does not. A tgui interface has **no data fetching, no router, no SSR/RSC, no Suspense, and no bundler splitting per route**: the backend pushes a whole payload and the tree re-renders. Measured against a live Vanderlin-family fork (2026-09-01, React 19.1, 111 interfaces): zero occurrences of `next/dynamic`, SWR, `Suspense`, `use client` or RSC. So **discard waterfall/bundle/server-tier advice outright** when it arrives from a general React source — it is not merely lower priority here, it has no referent.

What is left is the re-render tier, and even that is conditional. **With autoupdate OFF (the default this skill recommends) an interface re-renders on user action, not per tick** — so inline arrow props and unmemoised children usually cost nothing measurable, and “fix” commits that add `useCallback` everywhere are churn. The same fork carries 403 inline `onClick={() => …}` handlers with no evidence any of them matter. Apply the measure-first rule from the Approach section before optimising any of this.

Four rules earn their place because they are correctness or startup issues rather than micro-optimisation:

- **Never define a component inside another component.** Each parent render creates a new component *type*, so React unmounts and remounts the subtree — state is lost, effects re-run, and any `ByondUi` inside is torn down and re-created (see the remount-flash warning in the ByondUi section). Hoist it to module scope, or make it a plain function returning JSX only if it takes no state.
- **Derive during render; do not mirror backend data into state via `useEffect`.** `const sorted = useMemo(() => sort(data.items), [data.items])` — not a `useState` + `useEffect` that copies `data.items` on every push. The mirrored copy is stale for one render after every `ui_data` update and desynchronises the moment an action changes data without changing the effect's dependency. This is the single most valuable rule here because the backend-push model makes the bug easy to write and hard to see.
- **Initialise expensive `useState` lazily**: `useState(() => buildCatalog(data))`, not `useState(buildCatalog(data))` — the eager form runs the builder on *every* render and throws the result away.
- **Use functional `setState`** (`setX(x => x + 1)`) when the next value depends on the previous one; it keeps handlers stable and avoids stale-closure bugs across an async `act()` round-trip.

React 19 features are available on forks pinned to it (`useDeferredValue`, `startTransition`, `Activity`, `useEffectEvent`) — check `tgui/packages/tgui/package.json` before reaching for one, exactly as with any tgui-core-versioned claim.

*Rule selection informed by Vercel's `react-best-practices` skill (MIT); ~40% of it — the two CRITICAL tiers and the server tier — was rejected as having no surface in tgui, and its “ternary not `&&`” rule was dropped after checking: the fork's 323 `&&` conditionals all guard on explicit comparisons (`x.length > 0`, `x !== undefined`), so the falsy-number bug it targets does not occur.*

## Review checklist

- Does `ui_interact`/`tgui_interact` follow the local `try_update_ui` pattern, with no extra refs or scanners?
- Is the interface registered in the local routing mechanism (`routes.js` or equivalent) with the DM interface key, wrapper, theme, and scrollability matching neighboring interfaces?
- Is duplicate-window prevention left to TGUI rather than custom code?
- Does `ui_state()` use the local state policy for range, consciousness, access, and remote interaction rather than duplicating those checks in the frontend?
- Does every `ui_act` call its parent first, stop when the parent handled/rejected the action, and validate every client-supplied `params` value before mutation?
- Are updates routed through `ui_act` return + `SStgui.update_uis(src)` (and `update_static_data()` if static data changed) rather than a custom wrapper or stored UI?
- If several static dependencies can change in a burst, is `update_static_data_for_all_viewers()` batched with the local timer/unique pattern instead of spammed per signal?
- Is the backend sending only data — no CSS classes, layout anchors, or display labels the frontend could derive?
- Does the frontend type the actual JSON shape (DM associative lists become objects; sequential lists become arrays) and avoid storing values in React state when they can be derived directly?
- If autoupdate is off, does the update story collapse to `SStgui.update_uis(src)` at each change site?
- If autoupdate is ON, is it actually needed (timer → client-side countdown instead)? Is every expensive `ui_data` block cached with invalidation at the single mutation funnel, so per-tick refreshes reuse the cache?
- Are live previews (doll/camera/minimap) delivered via `ByondUi` map_view where the fork has the infra, spritesheet assets reserved for static catalogs, and base64 reserved for dynamic one-offs — with no "migrate dynamic previews to assets" regressions?
- Are static browser/TGUI files registered as `/datum/asset` and returned from `ui_assets()`, then referenced via `resolveAsset()`, `get_url_mappings()`, or `SSassets.transport.get_asset_url()` instead of hardcoded `html/...` or `icons/...` paths that bypass `ASSET_TRANSPORT`? If CSS uses relative `url(...)`, is the asset namespaced?
- For a crash inside a shared package (tgui-panel/tgui-say/common), was the site diffed against current /tg/ first, and is the fix an upstream backport rather than an invented local variant?
- Is client-side persistence sized for its backend — small settings only on byondstorage (one disk json shared across every server under the hub entry, flushed ~10 s), append-forever data (chat logs) on the iframe+IndexedDB stack or not persisted at all — and does any backend migration import settings only, never foreign chat history (`references/client-storage.md`)?
- Is any cache justified by *measured* cost? (Caching shared, immutable, same-for-everyone data globally is fine; caching per-user dynamic payloads keyed on a counter is not.)
- Were temporary performance loggers, timing locals, render counters, and obsolete thumbnail/base64 caches removed after the final approach was chosen?
- For appearance pickers, are large option catalogs delivered as assets/spritesheets plus ids instead of repeated base64 strings in static data?
- Is a slow *first* open diagnosed as framework/WebView/asset transfer (slow on BYOND 516), not blamed on render or payload? Is per-click slowness diagnosed separately as update cost?
- If the symptom is white/blank TGUI or all browser popups failing, were BYOND version, WebView2/IE, DPI/compatibility mode, Wine/Linux, client cache/resources, antivirus/disk blocking, and `skin.dmf`/`winset` checked before changing interface code?
- Is each frontend element chosen by semantics per the decision matrix — `Button` for actions, `Section` for titled panels, `Box` for layout blocks, `Box as="span"` for inline text — rather than raw tags doing a component's job **or** `Box as="..."` impersonating native tags? Are remaining raw tags justified (semantics, native attributes, wrapper ref contracts) and commented where non-obvious?
- If `ByondUi` is present, is it reserved for real BYOND controls, anchored to `config.window`, given a stable id when needed, and kept out of scrolling/zero-size layout traps? Are volatile params (zoom, sizes) kept OUT of the React `key` and updated via DM `winset` instead of remounts? Is `phonehome={false}` set when DM owns the control lifecycle?
- Does one user interaction stay within the client's Topic rate budget (count acts + geometry reports + per-map `renderByondUi` × synthetic resize dispatches + hover relays against `SECOND_TOPIC_LIMIT`/`MINUTE_TOPIC_LIMIT`)? For "player X lags but the server is healthy" reports, was game.log grepped for `topic limit` before touching interface code?
- For embedded-map sizing/positioning work, were the canvas and viewport MEASURED (`winget view-size` at fixed zoom, frontend geometry report) rather than modeled from screenshots, and do the logs carry a bundle/dmb fingerprint so stale-build reports can't fabricate false conclusions?
- Is any component defined **inside** another component (remount-per-render, and it tears down any `ByondUi` in that subtree)? Is backend data **derived during render** rather than mirrored into `useState` via `useEffect`? Are expensive `useState` initialisers lazy (`useState(() => …)`)?
- Conversely: is a `useCallback`/`useMemo`/`memo` being added without a demonstrated cost? With autoupdate off, re-renders follow user actions, so inline handlers are usually not the problem — don't accept general-React micro-optimisation as a substitute for measurement.
- Is SCSS proportional to the problem (not 1000+ lines re-implementing component layout), free of absolute-pixel layout, and reusing the shared theme base rather than a one-off palette or a bespoke scaling control?

## Shared tgui packages (tgui-panel, tgui-say, common chat code)

When a crash lives in a package shared with upstream (`tgui-panel`, `tgui-say`, `common/`), **diff the crash site against current /tg/ before writing any fix** — forks routinely lag, and the guard you are about to invent often already exists upstream. Backporting the upstream hunk 1:1 is a sync, not a divergence, and is acceptable even under strict "don't touch upstream files" policies; an original fix in the same file is not. Field case: a fork's chat renderer lacked upstream's `if (!Element) { log; removeAttribute; continue; }` guard around `TGUI_CHAT_COMPONENTS[targetName]` — every replayed history message with an unknown `data-component` threw minified React #130.

Diagnostic signatures for shared-package crashes: **minified React error #130** = rendering `undefined` as a component (unknown name in a component map, or a broken import after a tgui-core bump); **a burst of hundreds of identical errors within seconds of one player connecting** = persisted chat history replaying incompatible messages — a client-side data problem masquerading as "player X overloads the server". (Persistence rides the fork's client-storage backend — IndexedDB, `byondStorage`, or /tg/'s current iframe+IndexedDB stack — and outlives builds by design; generations and migration traps in `references/client-storage.md`.) The crash also **cascades**: each fatal error is relayed to the server as a `type=log&fatal=1` Topic, the flood burns the client's Topic rate budget (`SECOND_TOPIC_LIMIT`/`MINUTE_TOPIC_LIMIT`), and the limiter then drops their *legitimate* topics — one crashed panel makes every window on that client look broken ("can't open anything"). The tell is game.log `topic limit` lines whose logged href is the error text itself.

Chat-embedded components are a documented protocol, not ad-hoc HTML (`tgui/docs/chat-embedded-components.md` in /tg/): DM emits `<span data-component="Name" data-yourprop="...">`; the renderer only instantiates names whitelisted in `TGUI_CHAT_COMPONENTS` and only maps attributes listed in `TGUI_CHAT_ATTRIBUTES_TO_PROPS` (attributes are lowercase-only, hence the map). Values arrive as strings with fixed coercion rules: `"$true"`/`"$false"` → booleans (the `$` exists so literal "true" stays a string), parseable numbers → numbers, everything else → string. Adding a component = import + both maps; emitting one from DM without whitelisting it is exactly the React #130 crash above.

## When repo patterns conflict

Pick the closest authority: **local framework source and neighboring interfaces > same TGUI generation (tgui-core vs in-tree) > current /tg/ documentation and source > other external guides.** Search the working repo first: a neighbor in the current codebase wins even over /tg/. If local documentation is absent or incomplete, use the current `/tg/` TGUI docs as the canonical modern fallback, then verify that the fork has not renamed or diverged from the relevant API.

## Reference dispatch

Thirteen reference files exist; a task needs two or three. Start from exactly **one anchor**, chosen by the task's primary shape. Add a conditional file only when its trigger is actually present in the diff or the question — not because it "might be relevant." A task that genuinely spans domains earns its extra files one trigger at a time.

**Anchor — pick one:**

| Task's primary shape | Anchor |
|---|---|
| Blank/white windows, all browser popups failing, platform or client-runtime symptom | [references/runtime-platform-triage.md](references/runtime-platform-triage.md) |
| Broad review, "find the bad practices", judging a refactor | [references/review-playbooks.md](references/review-playbooks.md) |
| Implementing or changing an interface — the backend/frontend split and data-vs-presentation contract | [references/tgui-workflow.md](references/tgui-workflow.md) |
| "It's slow" — first-load vs per-update latency, autoupdate/`update_uis` cost, whether to cache | [references/performance-and-lifecycle.md](references/performance-and-lifecycle.md) |
| "Does this rule hold on our fork?" — how far a pattern generalizes | [references/source-corpus.md](references/source-corpus.md) |

**Conditional add-ons — open only when this specific trigger fires:**

| Trigger actually present in the diff/question | Add |
|---|---|
| `ByondUi`, `winset`/`winget`/`callByond`, skin params, embedded map or camera controls, legacy routes, dev-server/HMR | [references/byond-ui-and-devserver.md](references/byond-ui-and-devserver.md) |
| Embedded map content is tiny, off-center, or invisible — or two field reports contradict each other | [references/embedded-map-geometry.md](references/embedded-map-geometry.md) |
| The DM↔JS bridge itself: custom `browse` popups, the `Byond` JS surface, `byondStorage`, client dot-commands, `RenderIcon`/icon delivery | [references/byond-client-api.md](references/byond-client-api.md) |
| A character doll / camera / minimap / option-catalog preview renders wrong — transparent, mis-scaled, wrong facing, a grey silhouette, or a list that empties itself; or you are migrating a preview off base64 | [references/appearance-previews.md](references/appearance-previews.md) |
| Chat settings or history not saving, client hitching every 10–30 s while the server is healthy, chat breaking after server-hopping, a storage backport | [references/client-storage.md](references/client-storage.md) |
| Choosing between `Box`/`Button`/`Section`/`Tooltip`, a proposed tag swap, SCSS/theming scope, the typed `Data` contract | [references/components-and-style.md](references/components-and-style.md) |

**Case material — read only when a comparable situation is live**, never as background: [references/case-study-overengineered-interface.md](references/case-study-overengineered-interface.md) (a reviewed redesign that overshot) and [references/refactor-timeline.md](references/refactor-timeline.md) (the progression from bespoke machinery to framework-native patterns). Both are anonymized.

**Bundled script:** `scripts/tgui_smell_scan.py` is a read-only first-pass scanner for broad reviews. Run it on changed TGUI files or a narrow directory, then inspect each hit against the anchor above. Its hits are leads, not linter failures.

Two orderings override the table when they collide with it, because getting them backwards wastes the most time: for a blank/white-window report, triage the platform **before** any code-level performance review; and for appearance-preview work, the map_view hierarchy in "Appearance preview pickers" above comes before any reference file.

## External references (summarize and link, don't copy; all version-sensitive)

- Current `/tg/` TGUI documentation — canonical modern fallback after local code/docs: https://github.com/tgstation/tgstation/tree/master/tgui/docs
- Old in-tree `/tg/` tgui README and source — useful for legacy Inferno/routes/`ByondUi` details, not authority over modern forks: https://github.com/Giacom/-tg-station/blob/master/tgui/README.md
- Paradise TGUI guide — introductory background only; the page warns it predates current TGUI: https://paradisestation.org/wiki/index.php/Guide_to_TGUI
- Goonstation TGUI guide (mostly points at the README): https://hackmd.io/@goonstation/tgui
- Goonstation `/tgui` README: https://github.com/goonstation/goonstation/blob/master/tgui/README.md

Always search local framework source, documentation, and neighboring interfaces before using external material. Treat `/tg/` docs as the first fallback for modern TGUI, not as authority over a fork's verified local behavior.
