---
name: "ss13-tgui"
description: "Use only for SS13 TGUI/web UI work: implementing, reviewing, simplifying, or debugging a tgui interface; DM procs ui_interact/tgui_interact/ui_data/ui_static_data/ui_assets/ui_act/ui_state; SStgui lifecycle; files under tgui interfaces/routes/layouts/components/SCSS; tgui-core or in-tree tgui components; BYOND browser bridge work involving ByondUi, winset/winget/callByond, config.window/config.ref, embedded maps/camera controls; tgui dev-server/HMR; duplicate tgui windows; blank/white TGUI windows, WebView2/IE/DPI/Wine runtime triage, skin.dmf/window-control breakage; first-load/per-update tgui performance; or overengineered tgui refactors. Do not use for ordinary SS13 DM gameplay/content/systems work, mobs/items/icons/balance/admin verbs/database/mapping, or generic BYOND code unless the request or changed files also touch TGUI or BYOND browser UI integration."
---

# SS13 TGUI Interfaces

Review, implement, simplify, and debug TGUI interfaces in BYOND/DM + React codebases. The goal is correct, idiomatic, **codebase-native** TGUI — not bespoke machinery that reimplements what the framework already does.

## Activation guard

Use this skill only when the request or changed files include a TGUI-specific signal: `tgui/` frontend files, `ui_interact`/`tgui_interact`, `ui_data`, `ui_act`, `SStgui`, tgui components, TGUI SCSS, `ByondUi`, `winset`/`winget`/`callByond`, embedded map/camera controls, tgui dev-server/routing work, or runtime symptoms such as blank/white TGUI windows, WebView2/IE, DPI scaling, Wine/Linux browser issues, client cache/resources, or `skin.dmf`/window-control breakage. If the task is normal SS13 DM content or systems work with no UI/webview bridge, do not apply this skill. If the task is ambiguous, inspect the changed paths and nearest procs before leaning on these rules.

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

## Appearance preview pickers

Delivery mechanism is a hierarchy — pick by how the image changes, not by habit:

1. **Live, per-player, frequently-changing scene (character doll, camera, minimap): `ByondUi` map_view FIRST.** This is the priority target, not an exotic option. A `/atom/movable/screen/map_view` shows the preview mob natively (appearance streaming): zero encoding, zero payload in `ui_data`, instant updates, free rotation via `setDir`. `/tg/`'s `char_preview` is the canonical shape: the screen object owns a per-preferences dummy, `update_body()` sets `appearance = render_preview(body)`, tgui embeds it by `mapRef`. Fall back to flattened base64 only when the infra genuinely can't apply (no map_view in the fork, headless render, image must leave the client).
2. **High-cardinality static catalogs (style cards): `ui_assets()` + spritesheet** and a small static catalog of stable CSS class names. Do not send one base64 thumbnail per option through `ui_static_data()` once the spritesheet is authoritative; delete the old thumbnail proc and global cache instead of leaving a parallel path.
3. **Dynamic one-offs (photos, rare previews): base64 is fine** — and for *per-change dynamic* images the asset system is actively WORSE than base64: assets are generated and transported once by design, so a per-click preview would mean a new asset + a new client round-trip per change. Do not "migrate previews to assets" as a blanket rule; migrate catalogs to assets and live scenes to map_view. When a flattened single image is genuinely required and the fork is on BYOND 515+, `client.RenderIcon(atom)` beats server-side `getFlatIcon`: it is the client renderer itself, so overlays, transforms, and filters can't drift (see `references/byond-client-api.md`); keep `getFlatIcon` for headless/CI paths.

The performance smell is **repeated base64 option catalogs** and synchronous thumbnail generation in hot paths; for many stable options, use assets/spritesheets plus ids.

Two base64-preview pitfalls proven in the field:

- **Custom icon flatteners drift from native rendering.** A hand-rolled `getFlatIcon` clone will not read `appearance.transform` (matrix scales silently do nothing in the preview while working in-game) and its canvas-growth math diverges once several pixel-offset overlays stack. Prefer the native flattener whenever sprites fit its bounds; if you must scale for a flattener, resize the icon itself (`icon.Scale`), never the transform.
- **Preview-only state must bypass validated preferences.** `write_preference()` silently returns FALSE for out-of-domain values (`is_valid()`), so "force the dummy nude for the preview" via a pref write can silently not happen. Set preview-only state directly on the dummy after `apply_prefs_to()` and rebuild its body — never through the validated pref pipeline.

Keep picker state simple. If a background picker has become `None` / `White` / `Dark`, send those values directly and remove turf thumbnail renderers and option caches. If a helper now returns an `icon` directly, remove any stale cache that used to wrap that helper.

When filtering an option catalog by whitelists (gender, species, coverage), guard the empty result: on modular forks the core whitelist macros routinely omit modular content ids, and an emptied list can cascade — validation marks the entry permanently disabled, the enable toggle silently re-disables every pass, and the feature looks "broken" for exactly the modular species. Give bypass flags to content that must be universal, and fall back to a less-filtered list instead of returning empty.

For hover previews that replace an existing sprite accessory, render the base doll with the current customizer temporarily disabled, cache it by `(customizer, current preview signature)`, and overlay the candidate on that base. Do not stack the candidate over the already-equipped current accessory; it gives plausible screenshots while hiding the actual replacement bug.

## ByondUi / BYOND controls

Use `ByondUi` only for actual BYOND skin controls that must be layered over the browser, most commonly embedded maps/camera views — including the **map_view live-preview pattern above, which should be your default for character/scene previews** when the fork has the infra (check `_onclick/hud/map_popups.dm` for `/atom/movable/screen/map_view`/`assigned_map` and grep for an existing `ByondUi` consumer such as a color-matrix editor or camera console to copy). It is not a replacement for normal tgui `Button`, `Input`, `Section`, or HTML layout. In old in-tree tgui, `ByondUi` computes its DOM bounding box and calls BYOND `winset` with `id`, `parent`, `type`, `pos`, and `size`; on unmount/beforeunload it clears the control's `parent`. That means the React element is a positioning anchor, while the visible control is still BYOND-owned.

When using or reviewing it:

- Verify the repo actually has `ByondUi` or an equivalent component; modern/forked tgui may differ.
- Pass `parent: config.window` and the BYOND control `type` required by the skin params. Use a stable `id` from backend data when DM or another control must address the same control, as camera consoles do with a map ref.
- Keep it in a stable, nonzero-sized container; old implementations update position on render and debounced window resize, not every scroll event.
- Use `act()`/`ui_act` for gameplay mutations. Use raw `winset`/`winget`/`callByond` only for BYOND window/control properties or framework bridge code.
- Debug blank controls by checking route registration, `config.window`, id uniqueness, CSS/container size, clipping/scrolling, backing DM map/control setup, and local browser support before rewriting the interface.
- **If embedded map content renders tiny, off-center, or vanishes: read `references/embedded-map-geometry.md` before changing any code.** Dynamically-created secondary maps choose their world canvas by rules you don't control (field data: a skin-default 640×480 in most configurations, silently flipping to the object bounding box after an unrelated layout change) — so PIN the canvas with an invisible background spanning your whole intended frame, size via the `zoom` skin param (disables auto-fit; viewport centers on the canvas center), and measure with `winget view-size / zoom`. Never put volatile params like zoom in the ByondUi React `key` (remount = visible flash); update them via DM `winset` instead.
- For the skin-parameter vocabulary (map `zoom-mode`/`view-size`/`icon-size`, window `is-transparent`, global `winget(null, ...)`, `byondStorage`, client dot-commands) consult `references/byond-client-api.md` before inventing a workaround — the client usually already has the knob.

## Choosing frontend elements (decision matrix)

The same "don't hand-roll what the framework provides" rule applies to markup — and so does its inverse: don't strip contracts the platform provides. **Never mechanically find/replace HTML tags with `Box as="<tag>"`** — that loses native keyboard behavior, `type`/`aria-*`/`title` attributes, and SCSS element selectors while gaining nothing. Decide by what the element *is*:

- a user action → `Button` (custom look = `className` + SCSS over its chrome, not a rebuilt pseudo-button);
- a standard titled panel → `Section` with `title` / `buttons`;
- a block-level layout/style wrapper → `Box` (it renders a `<div>`; it is a CSS-utility primitive, not a universal HTML replacement);
- inline styled text with no specialized component → `Box as="span"` (the only `as` value common in /tg/ interfaces);
- semantic prose, typed native attributes, or a wrapper's ref contract (e.g. `Tooltip` clones its child and injects a `ref` that must land on a DOM node) → raw HTML, with a comment when non-obvious;
- unsure → read the component's implementation and 2-3 neighboring interfaces before choosing.

Adopting `Section`/`Button` must *delete* markup, CSS, or behavior code. If it would break a bespoke panel's DOM/scroll/sticky structure, or you'd neutralize all of the component's chrome while using none of its behavior, keep the simpler construct. Details and the lost-contract checklist: `references/components-and-style.md`.

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
- For a crash inside a shared package (tgui-panel/tgui-say/common), was the site diffed against current /tg/ first, and is the fix an upstream backport rather than an invented local variant?
- Is any cache justified by *measured* cost? (Caching shared, immutable, same-for-everyone data globally is fine; caching per-user dynamic payloads keyed on a counter is not.)
- Were temporary performance loggers, timing locals, render counters, and obsolete thumbnail/base64 caches removed after the final approach was chosen?
- For appearance pickers, are large option catalogs delivered as assets/spritesheets plus ids instead of repeated base64 strings in static data?
- Is a slow *first* open diagnosed as framework/WebView/asset transfer (slow on BYOND 516), not blamed on render or payload? Is per-click slowness diagnosed separately as update cost?
- If the symptom is white/blank TGUI or all browser popups failing, were BYOND version, WebView2/IE, DPI/compatibility mode, Wine/Linux, client cache/resources, antivirus/disk blocking, and `skin.dmf`/`winset` checked before changing interface code?
- Is each frontend element chosen by semantics per the decision matrix — `Button` for actions, `Section` for titled panels, `Box` for layout blocks, `Box as="span"` for inline text — rather than raw tags doing a component's job **or** `Box as="..."` impersonating native tags? Are remaining raw tags justified (semantics, native attributes, wrapper ref contracts) and commented where non-obvious?
- If `ByondUi` is present, is it reserved for real BYOND controls, anchored to `config.window`, given a stable id when needed, and kept out of scrolling/zero-size layout traps? Are volatile params (zoom, sizes) kept OUT of the React `key` and updated via DM `winset` instead of remounts?
- For embedded-map sizing/positioning work, were the canvas and viewport MEASURED (`winget view-size` at fixed zoom, frontend geometry report) rather than modeled from screenshots, and do the logs carry a bundle/dmb fingerprint so stale-build reports can't fabricate false conclusions?
- Is SCSS proportional to the problem (not 1000+ lines re-implementing component layout), free of absolute-pixel layout, and reusing the shared theme base rather than a one-off palette or a bespoke scaling control?

## Shared tgui packages (tgui-panel, tgui-say, common chat code)

When a crash lives in a package shared with upstream (`tgui-panel`, `tgui-say`, `common/`), **diff the crash site against current /tg/ before writing any fix** — forks routinely lag, and the guard you are about to invent often already exists upstream. Backporting the upstream hunk 1:1 is a sync, not a divergence, and is acceptable even under strict "don't touch upstream files" policies; an original fix in the same file is not. Field case: a fork's chat renderer lacked upstream's `if (!Element) { log; removeAttribute; continue; }` guard around `TGUI_CHAT_COMPONENTS[targetName]` — every replayed history message with an unknown `data-component` threw minified React #130.

Diagnostic signatures for shared-package crashes: **minified React error #130** = rendering `undefined` as a component (unknown name in a component map, or a broken import after a tgui-core bump); **a burst of hundreds of identical errors within seconds of one player connecting** = persisted chat history replaying incompatible messages — a client-side data problem masquerading as "player X overloads the server". (Persistence rides `byondStorage`, which outlives builds by design — see `references/byond-client-api.md`.)

Chat-embedded components are a documented protocol, not ad-hoc HTML (`tgui/docs/chat-embedded-components.md` in /tg/): DM emits `<span data-component="Name" data-yourprop="...">`; the renderer only instantiates names whitelisted in `TGUI_CHAT_COMPONENTS` and only maps attributes listed in `TGUI_CHAT_ATTRIBUTES_TO_PROPS` (attributes are lowercase-only, hence the map). Values arrive as strings with fixed coercion rules: `"$true"`/`"$false"` → booleans (the `$` exists so literal "true" stays a string), parseable numbers → numbers, everything else → string. Adding a component = import + both maps; emitting one from DM without whitelisting it is exactly the React #130 crash above.

## When repo patterns conflict

Pick the closest authority: **local framework source and neighboring interfaces > same TGUI generation (tgui-core vs in-tree) > current /tg/ documentation and source > other external guides.** Search the working repo first: a neighbor in the current codebase wins even over /tg/. If local documentation is absent or incomplete, use the current `/tg/` TGUI docs as the canonical modern fallback, then verify that the fork has not renamed or diverged from the relevant API.

## Reference files (progressive disclosure)

- `references/source-corpus.md` — comparative map across tgstation, Vanderlin, cmss13, BandaStation: what was sampled, and which rules are universal vs fork-local. **Read first when unsure how far a rule generalizes.**
- `references/tgui-workflow.md` — backend/frontend split, the data-vs-presentation contract, full review checklist with rationale.
- `references/performance-and-lifecycle.md` — source-grounded lifecycle (autoupdate loop, `on_act_message`, `update_uis` fan-out, `update_static_data`), first-load vs per-update delay, when caching is and isn't warranted.
- `references/runtime-platform-triage.md` — blank/white TGUI windows, WebView2/IE, DPI scaling, Wine/Linux, client cache/resources, antivirus/disk blocking, `skin.dmf`, and runtime `winset` failures. **Read before code-level performance review when the symptom is broad browser-window failure.**
- `references/components-and-style.md` — element choice in depth (`Box`/`Button`/`Section`/`Tooltip` contracts, what careless tag swaps lose, when raw HTML is right), component conventions (tgui-core vs in-tree), typed `Data` contract, SCSS/theming/scaling.
- `references/byond-ui-and-devserver.md` — `ByondUi`, `winset`/`winget`/`callByond`, embedded map/camera controls (incl. the map_view live-preview recipe), legacy route registration, and old in-tree tgui dev-server workflow. **Read when the task mentions BYOND controls, maps inside tgui, routes, or dev-server/HMR.**
- `references/embedded-map-geometry.md` — the geometry contract for tgui-embedded secondary maps (the unstable engine-chosen canvas and how to PIN it with a background frame, `zoom` as the sizing knob, canvas-center viewport, screen_loc rules), the live-appearance vs runtime-icon repaint reality, measurement instruments, two-artifact build fingerprinting, and the catalog of field-proven false conclusions with prevention rules (build-scoped constants included). **Read whenever embedded map content is tiny/off-center/invisible, or field reports contradict each other.**
- `references/byond-client-api.md` — the applied BYOND↔TGUI catalog distilled from the official BYOND Reference + /tg/'s bridge: the three bridge layers (tgui / tgui_window popups / raw browse-output-Topic), the full `Byond` JS object surface (incl. the 2048-char href limit and XHR fallback, `__number__` JSON reviver, strictMode FatalError logging), native 516 `BYOND` object vs tgui's `Byond`, `byondStorage` (hub/server/domain) persistence, calling JS from DM via `output("...", "browser:func")`, skin control/parameter cheat sheet (window/browser/map/output/input/global params), and client dot-commands. **Read when touching the DM↔JS bridge, custom popups, skin params, or client persistence.**
- `references/review-playbooks.md` — task-specific review order for performance, lifecycle/backend, frontend/components, appearance pickers, BYOND controls, and refactors. **Read for broad review requests or when asked to find bad practices.**
- `references/case-study-overengineered-interface.md` — anonymized, reusable lessons from a reviewed TGUI redesign.
- `references/refactor-timeline.md` — anonymized progression from bespoke machinery to framework-native patterns.

Bundled script: `scripts/tgui_smell_scan.py` is a read-only first-pass scanner for broad reviews. Run it on changed TGUI files or a narrow directory, then inspect each hit against the references above.

For blank/white window reports, read `references/runtime-platform-triage.md` before performance review. For code-level performance reviews, read `references/performance-and-lifecycle.md`; it includes the lifecycle rules plus concrete bad/good patterns from appearance preview and picker work.

## External references (summarize and link, don't copy; all version-sensitive)

- Current `/tg/` TGUI documentation — canonical modern fallback after local code/docs: https://github.com/tgstation/tgstation/tree/master/tgui/docs
- Old in-tree `/tg/` tgui README and source — useful for legacy Inferno/routes/`ByondUi` details, not authority over modern forks: https://github.com/Giacom/-tg-station/blob/master/tgui/README.md
- Paradise TGUI guide — introductory background only; the page warns it predates current TGUI: https://paradisestation.org/wiki/index.php/Guide_to_TGUI
- Goonstation TGUI guide (mostly points at the README): https://hackmd.io/@goonstation/tgui
- Goonstation `/tgui` README: https://github.com/goonstation/goonstation/blob/master/tgui/README.md

Always search local framework source, documentation, and neighboring interfaces before using external material. Treat `/tg/` docs as the first fallback for modern TGUI, not as authority over a fork's verified local behavior.
