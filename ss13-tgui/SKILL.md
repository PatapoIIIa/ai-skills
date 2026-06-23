---
name: "ss13-tgui"
description: "Use only for SS13 TGUI/web UI work: implementing, reviewing, simplifying, or debugging a tgui interface; DM procs ui_interact/tgui_interact/ui_data/ui_static_data/ui_assets/ui_act/ui_state; SStgui lifecycle; files under tgui interfaces/routes/layouts/components/SCSS; tgui-core or in-tree tgui components; BYOND browser bridge work involving ByondUi, winset/winget/callByond, config.window/config.ref, embedded maps/camera controls; tgui dev-server/HMR; duplicate tgui windows; first-load/per-update tgui performance; or overengineered tgui refactors. Do not use for ordinary SS13 DM gameplay/content/systems work, mobs/items/icons/balance/admin verbs/database/mapping, or generic BYOND code unless the request or changed files also touch TGUI or BYOND browser UI integration."
---

# SS13 TGUI Interfaces

Review, implement, simplify, and debug TGUI interfaces in BYOND/DM + React codebases. The goal is correct, idiomatic, **codebase-native** TGUI — not bespoke machinery that reimplements what the framework already does.

## Activation guard

Use this skill only when the request or changed files include a TGUI-specific signal: `tgui/` frontend files, `ui_interact`/`tgui_interact`, `ui_data`, `ui_act`, `SStgui`, tgui components, TGUI SCSS, `ByondUi`, `winset`/`winget`/`callByond`, embedded map/camera controls, or tgui dev-server/routing work. If the task is normal SS13 DM content or systems work with no UI/webview bridge, do not apply this skill. If the task is ambiguous, inspect the changed paths and nearest procs before leaning on these rules.

## The one root cause

Most TGUI mistakes share a single root: **assuming a capability is missing and hand-rolling it.** TGUI already pools windows, dedupes open UIs per user, caches assets in the webview, fans updates out to every viewer, and re-renders on `ui_act`. Before you add a helper, a cache, a counter, a window tracker, or a manual update path, find the framework mechanism you are about to duplicate. In real reviews the answer is almost always "one that already works," and the fix is *deletion plus a one-line framework call*.

When you catch yourself writing infrastructure (window scanners, dirty counters, asset caches, stored UI refs, scaling vars), stop and ask: *what local TGUI mechanism am I duplicating, and why did I assume it wasn't there?* That question prevents the entire class of errors this skill is built around.

## Approach (do these in order)

1. **Learn the local names before writing a line.** TGUI's *concepts* are stable across forks; its *names and import paths are not.* The backend entry proc is `ui_interact` in /tg/, Vanderlin, and BandaStation but `tgui_interact` in cmss13. Components come from `tgui-core/components` in tgui-core forks but from in-tree `tgui/components` in older ports (cmss13, older Azure-derived code, old tgstation tgui). Grep one neighboring interface in *this* repo and copy its proc name, route registration pattern, component import path, and its `useBackend`/`Window` imports. Memory from another fork will not compile here.
2. **Read 2-3 neighboring interfaces** (`.dm` + `.tsx` + `.scss`). Match their `ui_interact` shape, component usage, and styling. Local convention beats any external guide.
3. **Register the frontend where this generation requires it.** Older in-tree tgui uses a central `routes.js` table keyed by the DM interface name; missing route entries render a "Route entry missing" fallback. Modern forks may auto-discover or use a different routing table. Copy the local route/import/wrapper/theme pattern.
4. **Implement data-driven.** Backend sends *data*; frontend decides *presentation*. `ui_data()` for dynamic state; `ui_static_data()` for heavy, rarely-changing metadata (an optimization for big payloads — not mandatory for small UIs, and changing it requires an explicit `update_static_data()` push); `ui_assets()` for static assets.
5. **Keep the update path standard.** `ui_act` returning truthy already fires `SStgui.update_uis(src)`. For state changed *outside* `ui_act`, call `SStgui.update_uis(src)` at the change site. Nothing else.
6. **Treat BYOND controls as a bridge, not React.** If the interface embeds a map/camera/control with `ByondUi`, inspect the local `ByondUi` and BYOND bridge source before changing it. Read `references/byond-ui-and-devserver.md`.
7. **Pick elements by semantics, then style minimally.** Decide what each element *is* (action, titled panel, layout block, inline text) and pick the construct whose behavioral contract matches — see the decision matrix below. Never blanket-replace HTML tags with `Box as="..."`; keep SCSS proportional to the problem.
8. **Measure before optimizing.** No caches or counters without a demonstrated cost.
9. **Delete measurement scaffolding after it answers the question.** Temporary disk loggers, render counters, timing vars, and per-action traces are useful while diagnosing TGUI latency, but they are not part of the feature. Once performance is confirmed, remove the proc definitions, globals, call sites, and dead cache plumbing in the same cleanup pass.
10. **For broad reviews, run the read-only smell scan when it will save time.** `scripts/tgui_smell_scan.py` flags likely hotspots (`icon2base64`, manual UI refs, autoupdate off, temporary loggers, `useLocalState`, suspicious `Box as`, etc.). Treat hits as leads for inspection, not as linter failures.
11. **Review against the checklist below.**

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

For high-cardinality appearance pickers, prefer `ui_assets()` plus a spritesheet and a small static catalog of stable CSS class names. Do not send one base64 thumbnail per option through `ui_static_data()` once the spritesheet is authoritative; delete the old thumbnail proc and global cache instead of leaving a parallel path.

Base64 is not banned. `/tg/` still uses it for rare dynamic photos, one-off previews, or cases where a sprite cannot be represented by the normal icon reference. The performance smell is **repeated base64 option catalogs** and synchronous thumbnail generation in hot paths; for many stable options, use assets/spritesheets plus ids.

Keep picker state simple. If a background picker has become `None` / `White` / `Dark`, send those values directly and remove turf thumbnail renderers and option caches. If a helper now returns an `icon` directly, remove any stale cache that used to wrap that helper.

For hover previews that replace an existing sprite accessory, render the base doll with the current customizer temporarily disabled, cache it by `(customizer, current preview signature)`, and overlay the candidate on that base. Do not stack the candidate over the already-equipped current accessory; it gives plausible screenshots while hiding the actual replacement bug.

## ByondUi / BYOND controls

Use `ByondUi` only for actual BYOND skin controls that must be layered over the browser, most commonly embedded maps/camera views. It is not a replacement for normal tgui `Button`, `Input`, `Section`, or HTML layout. In old in-tree tgui, `ByondUi` computes its DOM bounding box and calls BYOND `winset` with `id`, `parent`, `type`, `pos`, and `size`; on unmount/beforeunload it clears the control's `parent`. That means the React element is a positioning anchor, while the visible control is still BYOND-owned.

When using or reviewing it:

- Verify the repo actually has `ByondUi` or an equivalent component; modern/forked tgui may differ.
- Pass `parent: config.window` and the BYOND control `type` required by the skin params. Use a stable `id` from backend data when DM or another control must address the same control, as camera consoles do with a map ref.
- Keep it in a stable, nonzero-sized container; old implementations update position on render and debounced window resize, not every scroll event.
- Use `act()`/`ui_act` for gameplay mutations. Use raw `winset`/`winget`/`callByond` only for BYOND window/control properties or framework bridge code.
- Debug blank controls by checking route registration, `config.window`, id uniqueness, CSS/container size, clipping/scrolling, backing DM map/control setup, and local browser support before rewriting the interface.

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
- Is any cache justified by *measured* cost? (Caching shared, immutable, same-for-everyone data globally is fine; caching per-user dynamic payloads keyed on a counter is not.)
- Were temporary performance loggers, timing locals, render counters, and obsolete thumbnail/base64 caches removed after the final approach was chosen?
- For appearance pickers, are large option catalogs delivered as assets/spritesheets plus ids instead of repeated base64 strings in static data?
- Is a slow *first* open diagnosed as framework/WebView/asset transfer (slow on BYOND 516), not blamed on render or payload? Is per-click slowness diagnosed separately as update cost?
- Is each frontend element chosen by semantics per the decision matrix — `Button` for actions, `Section` for titled panels, `Box` for layout blocks, `Box as="span"` for inline text — rather than raw tags doing a component's job **or** `Box as="..."` impersonating native tags? Are remaining raw tags justified (semantics, native attributes, wrapper ref contracts) and commented where non-obvious?
- If `ByondUi` is present, is it reserved for real BYOND controls, anchored to `config.window`, given a stable id when needed, and kept out of scrolling/zero-size layout traps?
- Is SCSS proportional to the problem (not 1000+ lines re-implementing component layout), free of absolute-pixel layout, and reusing the shared theme base rather than a one-off palette or a bespoke scaling control?

## When repo patterns conflict

Pick the closest authority: **local framework source and neighboring interfaces > same TGUI generation (tgui-core vs in-tree) > current /tg/ documentation and source > other external guides.** Search the working repo first: a neighbor in the current codebase wins even over /tg/. If local documentation is absent or incomplete, use the current `/tg/` TGUI docs as the canonical modern fallback, then verify that the fork has not renamed or diverged from the relevant API.

## Reference files (progressive disclosure)

- `references/source-corpus.md` — comparative map across tgstation, Vanderlin, cmss13, BandaStation: what was sampled, and which rules are universal vs fork-local. **Read first when unsure how far a rule generalizes.**
- `references/tgui-workflow.md` — backend/frontend split, the data-vs-presentation contract, full review checklist with rationale.
- `references/performance-and-lifecycle.md` — source-grounded lifecycle (autoupdate loop, `on_act_message`, `update_uis` fan-out, `update_static_data`), first-load vs per-update delay, when caching is and isn't warranted.
- `references/components-and-style.md` — element choice in depth (`Box`/`Button`/`Section`/`Tooltip` contracts, what careless tag swaps lose, when raw HTML is right), component conventions (tgui-core vs in-tree), typed `Data` contract, SCSS/theming/scaling.
- `references/byond-ui-and-devserver.md` — `ByondUi`, `winset`/`winget`/`callByond`, embedded map/camera controls, legacy route registration, and old in-tree tgui dev-server workflow. **Read when the task mentions BYOND controls, maps inside tgui, routes, or dev-server/HMR.**
- `references/review-playbooks.md` — task-specific review order for performance, lifecycle/backend, frontend/components, appearance pickers, BYOND controls, and refactors. **Read for broad review requests or when asked to find bad practices.**
- `references/case-study-overengineered-interface.md` — anonymized, reusable lessons from a reviewed TGUI redesign.
- `references/refactor-timeline.md` — anonymized progression from bespoke machinery to framework-native patterns.

Bundled script: `scripts/tgui_smell_scan.py` is a read-only first-pass scanner for broad reviews. Run it on changed TGUI files or a narrow directory, then inspect each hit against the references above.

For performance reviews, read `references/performance-and-lifecycle.md`; it includes the lifecycle rules plus concrete bad/good patterns from appearance preview and picker work.

## External references (summarize and link, don't copy; all version-sensitive)

- Current `/tg/` TGUI documentation — canonical modern fallback after local code/docs: https://github.com/tgstation/tgstation/tree/master/tgui/docs
- Old in-tree `/tg/` tgui README and source — useful for legacy Inferno/routes/`ByondUi` details, not authority over modern forks: https://github.com/Giacom/-tg-station/blob/master/tgui/README.md
- Paradise TGUI guide — introductory background only; the page warns it predates current TGUI: https://paradisestation.org/wiki/index.php/Guide_to_TGUI
- Goonstation TGUI guide (mostly points at the README): https://hackmd.io/@goonstation/tgui
- Goonstation `/tgui` README: https://github.com/goonstation/goonstation/blob/master/tgui/README.md

Always search local framework source, documentation, and neighboring interfaces before using external material. Treat `/tg/` docs as the first fallback for modern TGUI, not as authority over a fork's verified local behavior.
