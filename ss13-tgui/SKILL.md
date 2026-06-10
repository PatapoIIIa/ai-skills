---
name: "ss13-tgui"
description: "Version +1. Use when reviewing, implementing, simplifying, or debugging SS13 TGUI interfaces in BYOND/DM plus React (tgui-core or in-tree tgui) codebases (Vanderlin, /tg/, cmss13, BandaStation, Paradise, Goonstation and forks). Triggers on ui_interact/tgui_interact, ui_data/ui_static_data/ui_assets/ui_act/ui_state, SStgui.try_update_ui/update_uis, tgui components (Button, Box, Section, Stack, Window), React state, tgui SCSS/theming, TGUI performance or first-load delay, duplicate windows, and refactoring overcomplicated TGUI code. Reach for it whenever a task touches a tgui interface even if the user does not say the word TGUI."
---

# SS13 TGUI Interfaces

Review, implement, simplify, and debug TGUI interfaces in BYOND/DM + React codebases. The goal is correct, idiomatic, **codebase-native** TGUI — not bespoke machinery that reimplements what the framework already does.

## The one root cause

Most TGUI mistakes share a single root: **assuming a capability is missing and hand-rolling it.** TGUI already pools windows, dedupes open UIs per user, caches assets in the webview, fans updates out to every viewer, and re-renders on `ui_act`. Before you add a helper, a cache, a counter, a window tracker, or a manual update path, find the framework mechanism you are about to duplicate. In real reviews the answer is almost always "one that already works," and the fix is *deletion plus a one-line framework call*.

When you catch yourself writing infrastructure (window scanners, dirty counters, asset caches, stored UI refs, scaling vars), stop and ask: *what local TGUI mechanism am I duplicating, and why did I assume it wasn't there?* That question prevents the entire class of errors this skill is built around.

## Approach (do these in order)

1. **Learn the local names before writing a line.** TGUI's *concepts* are stable across forks; its *names and import paths are not.* The backend entry proc is `ui_interact` in /tg/, Vanderlin, and BandaStation but `tgui_interact` in cmss13. Components come from `tgui-core/components` in tgui-core forks but from in-tree `tgui/components` in older ports (cmss13, older Azure-derived code). Grep one neighboring interface in *this* repo and copy its proc name, its component import path, and its `useBackend`/`Window` imports. Memory from another fork will not compile here.
2. **Read 2-3 neighboring interfaces** (`.dm` + `.tsx` + `.scss`). Match their `ui_interact` shape, component usage, and styling. Local convention beats any external guide.
3. **Implement data-driven.** Backend sends *data*; frontend decides *presentation*. `ui_data()` for dynamic state; `ui_static_data()` for heavy, rarely-changing metadata (an optimization for big payloads — not mandatory for small UIs, and changing it requires an explicit `update_static_data()` push); `ui_assets()` for static assets.
4. **Keep the update path standard.** `ui_act` returning truthy already fires `SStgui.update_uis(src)`. For state changed *outside* `ui_act`, call `SStgui.update_uis(src)` at the change site. Nothing else.
5. **Style minimally.** Use the local component primitives over raw HTML; keep SCSS proportional to the problem.
6. **Measure before optimizing.** No caches or counters without a demonstrated cost.
7. **Review against the checklist below.**

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

## Review checklist

- Does `ui_interact`/`tgui_interact` follow the local `try_update_ui` pattern, with no extra refs or scanners?
- Is duplicate-window prevention left to TGUI rather than custom code?
- Does `ui_state()` use the local state policy for range, consciousness, access, and remote interaction rather than duplicating those checks in the frontend?
- Does every `ui_act` call its parent first, stop when the parent handled/rejected the action, and validate every client-supplied `params` value before mutation?
- Are updates routed through `ui_act` return + `SStgui.update_uis(src)` (and `update_static_data()` if static data changed) rather than a custom wrapper or stored UI?
- Is the backend sending only data — no CSS classes, layout anchors, or display labels the frontend could derive?
- Does the frontend type the actual JSON shape (DM associative lists become objects; sequential lists become arrays) and avoid storing values in React state when they can be derived directly?
- If autoupdate is off, does the update story collapse to `SStgui.update_uis(src)` at each change site?
- Is any cache justified by *measured* cost? (Caching shared, immutable, same-for-everyone data globally is fine; caching per-user dynamic payloads keyed on a counter is not.)
- Is a slow *first* open diagnosed as framework/WebView/asset transfer (slow on BYOND 516), not blamed on render or payload? Is per-click slowness diagnosed separately as update cost?
- Does the React side use the repo's component primitives (`Button`/`Box`/`Section`/`Stack`/`Window`) instead of raw `div`/`button`/`h3`/`section`? (Raw tags are a rare, deliberate exception for free-form content, not the default.)
- Is SCSS proportional to the problem (not 1000+ lines re-implementing component layout), free of absolute-pixel layout, and reusing the shared theme base rather than a one-off palette or a bespoke scaling control?

## When repo patterns conflict

Pick the closest authority: **local framework source and neighboring interfaces > same TGUI generation (tgui-core vs in-tree) > current /tg/ documentation and source > other external guides.** Search the working repo first: a neighbor in the current codebase wins even over /tg/. If local documentation is absent or incomplete, use the current `/tg/` TGUI docs as the canonical modern fallback, then verify that the fork has not renamed or diverged from the relevant API.

## Reference files (progressive disclosure)

- `references/source-corpus.md` — comparative map across tgstation, Vanderlin, cmss13, BandaStation: what was sampled, and which rules are universal vs fork-local. **Read first when unsure how far a rule generalizes.**
- `references/tgui-workflow.md` — backend/frontend split, the data-vs-presentation contract, full review checklist with rationale.
- `references/performance-and-lifecycle.md` — source-grounded lifecycle (autoupdate loop, `on_act_message`, `update_uis` fan-out, `update_static_data`), first-load vs per-update delay, when caching is and isn't warranted.
- `references/components-and-style.md` — component conventions (tgui-core vs in-tree), typed `Data` contract, SCSS/theming/scaling.
- `references/case-study-overengineered-interface.md` — anonymized, reusable lessons from a reviewed TGUI redesign.
- `references/refactor-timeline.md` — anonymized progression from bespoke machinery to framework-native patterns.

## External references (summarize and link, don't copy; all version-sensitive)

- Current `/tg/` TGUI documentation — canonical modern fallback after local code/docs: https://github.com/tgstation/tgstation/tree/master/tgui/docs
- Paradise TGUI guide — introductory background only; the page warns it predates current TGUI: https://paradisestation.org/wiki/index.php/Guide_to_TGUI
- Goonstation TGUI guide (mostly points at the README): https://hackmd.io/@goonstation/tgui
- Goonstation `/tgui` README: https://github.com/goonstation/goonstation/blob/master/tgui/README.md

Always search local framework source, documentation, and neighboring interfaces before using external material. Treat `/tg/` docs as the first fallback for modern TGUI, not as authority over a fork's verified local behavior.
