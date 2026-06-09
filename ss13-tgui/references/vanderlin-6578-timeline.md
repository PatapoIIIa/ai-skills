# PR #6578 Timeline: mistakes -> review -> corrections

A compact learning path correlating the Great Developer's review conversation with the PR's commit history. The point is not blame — it's to show *when* each over-engineering choice entered, *why* it seemed reasonable, and *which* idiomatic fix retired it. Reconstructed from `git log --oneline` on the PR branch plus the chat logs.

To inspect locally (read-only; do not edit application files):
```
git log --oneline --decorate <merge-base>..<pr-branch>
git show <commit>            # focused reads only
```

## Stage A — initial redesign (heavy custom build)

Commits (early): `First Release`, `Adjust TGUI`, `Another Improve`, `Design adjust`, `Little adjust`, `Some changes`, `Uppder order`, `Big Adjust`, `Commit 1/2`, `Colour Update`, `Improve arts`, `Themes update and optimization`, `Double colour chemes`.

- **What was built:** full custom AttributeMenu — a constellation/seal layout, a hand-written tutorial overlay, a large SCSS sheet (~1100 lines), light+dark themes, and a backend that emitted presentation fields.
- **Why it looked reasonable:** a from-scratch visual design feels like it needs from-scratch infrastructure; doing it "without upstream edits" gave freedom to add anything.
- **Seeds of later problems:** big SCSS, absolute pixels, raw HTML tags, backend `anchor`/`seal_label`, a stored UI ref, a custom window-dedupe helper, disabled autoupdate with a manual update path, and a generation-counter cache.

## Stage B — performance red herring (first-load delay)

Chat: the author reports a "huge data dump" after opening the first interface and suspects the interface/update logic. The Great Developer: *"you can't debug this it's a limitation of 516 and byond - webview communication; the first load always takes 3-4 seconds... assets are then cached in webview2 cache."* Separately, a real asset bug (the cache-confirmation timeout) was found and fixed in **#6659**.

- **Lesson:** distinguish first-load (framework/WebView/assets) from per-update cost. The slow *first* open was not the React render or the DM payload. Chasing it in interface code is wasted effort. The genuine asset fix lived elsewhere (#6659).

## Stage C — review of the lifecycle/caching machinery

Chat (Great Developer): "remove all code related to `find_active_attribute_menu_ui`"; "what's the point of incrementing total updates?"; "They already can't open duplicate menus that's how tgui works"; "If you can open more of the same menu you broke something"; "That isn't a good metric for caching you want to stringify the stat skill information and compare. Not that I think caching is even required here since updates are on demand anyway."

Corrective commits, in order:
- `cut find_active_attribute_menu_ui` — removed the custom dedupe scanner (and, with it, the reliance on a tracked UI). *Lesson: TGUI pools windows; `try_update_ui` dedupes.*
- `Dynamic cashe del` — deleted the generation-counter / per-user dirty cache. *Lesson: on-demand updates rarely need a cache; a counter is a bad cache key.*
- `Move to update_uis` — replaced the custom update wrapper with `SStgui.update_uis(src)` at the change site (in the attribute-modifier code, now `attribute_modifier.dm:148`), then removed the wrapper proc entirely. *Note: autoupdate stayed off — that flag was never the problem; the hand-rolled wrapper around a tracked UI was. Lesson: collapse external-change updates to the idiomatic fan-out.*
- `sanitized_css_cache delete` — removed the global cache for ~20 sanitized icon names; sanitization is inline. *Lesson: don't cache trivial ops on tiny static sets.*

Net effect: a large chunk of bespoke backend infrastructure was *deleted*, replaced by standard one-line calls — without losing functionality.

## Stage D — data-vs-presentation and correctness

Chat (Great Developer): use stat `name` and `shorthand` (after #6640) instead of custom seal-label helpers; presentation anchors/classes should be derived in the frontend; and the value display is wrong — "current/base is not right since the base value gets altered by modifiers... best to just omit it anyway," noting the 20/100 maxima no longer apply.

- **Presentation move:** `anchor` (= `name.toLowerCase()`) and `seal_label` (= `name` + `shorthand`) should leave the backend and be derived in TS.
- **Correctness:** the displayed skill number must match the value the *game* actually uses (the canonical effective-skill calc with default-attribute floors), not a parallel UI-only calc. Don't invent display semantics the system doesn't have.

## Stage E — components and style

Chat (Great Developer): "Use react classes Button, Box (Div/Span), Section, Stack not base HTML classes section, button, h3, etc"; "The scss seems excessive for what it is 1100 lines... lots of absolute pixel measurements which also goes against tgui design"; the scaling option is redundant because a UI-scaling var already exists; and the paper styling should build on `RecipeBook.scss`.

- **Lesson:** adopt tgui-core primitives, shrink the SCSS by deleting what the framework already does, drop absolute-pixel layout and the bespoke scaling control, and base the theme on the shared paper stylesheet.

## Current state (branch `TGUI-fix`, sampled 2026-06-08)

The backend (`code/datums/attributes/__holder_ui.dm`) now reads idiomatically: `try_update_ui` open, `set_autoupdate(FALSE)` paired with `SStgui.update_uis(src)` at the modifier change site, inline sanitize, split static/dynamic data, effective-skill values, and a *legitimate* `GLOB.attribute_menu_static_payload` cache of the shared immutable static payload. The frontend is the lagging half: `AttributeMenu.tsx` is still ~994 lines with ~78 raw tags and a ~1176-line SCSS sheet. **Lesson about pacing:** backend lifecycle corrections are cheap and land fast (delete machinery, add one-line calls); component/SCSS cleanup is slower and is often what remains. Budget review attention accordingly.

## The throughline

Every stage repeats one correction: **a framework mechanism already existed, the PR re-implemented it, and the fix was to delete the re-implementation and call the framework.** When reviewing or building TGUI, your first question on any helper/cache/counter/scaler should be "what local TGUI mechanism does this duplicate?" — because in this codebase, the answer was almost always "one that already works."
