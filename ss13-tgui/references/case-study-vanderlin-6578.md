# Case Study: Vanderlin PR #6578 (Skills panel / AttributeMenu)

Distilled, reusable lessons from a real TGUI redesign and its review by a Great Developer (the maintainer who reviewed the PR). These are **anchors for recognizing a class of problem**, not AttributeMenu-specific prescriptions. Each entry follows: the assumption, why it looked reasonable, why it was wrong, the codebase-native fix, and the general rule. The general rule is the part to carry to other interfaces.

- PR: https://github.com/Monkestation/Vanderlin/pull/6578 ("New Design for the Skills panel")
- Related: #6659 (a real first-load asset bug — cache-confirmation timeout), #5290 (TG chat port), tgstation #88699 (516 href handling), #6640 (fixed stat shorthands).
- Backend in its corrected state: `code/datums/attributes/__holder_ui.dm`; update site: `code/datums/attributes/attributes/attribute_modifier.dm`.

## 1. `find_active_attribute_menu_ui` — custom duplicate-window prevention

- **Assumption:** "TGUI will happily open two of the same menu, so I must scan open UIs and close duplicates."
- **Looked reasonable:** the author *had* observed a duplicate open (likely via a timeout/alternate path).
- **Why wrong:** `SStgui.try_update_ui(user, src, ui)` looks the UI up per `(user, src)` in `src.open_uis` and refreshes it — duplicates are impossible through the normal path. The scanner masks the real upstream bug. ("They already can't open duplicate menus that's how tgui works... If you can open more of the same menu you broke something.")
- **Fix:** delete the helper; rely on `try_update_ui`.
- **Rule:** never hand-roll window dedupe. If duplicates appear, fix the open path, not the symptom.

## 2. Storing a long-lived `datum/tgui` on the domain datum (`attribute_menu_ui`)

- **Assumption:** "I need a handle to the window so I can update/close it later."
- **Looked reasonable:** imperative habit — keep a reference to the thing you will act on.
- **Why wrong:** open UIs already live in `src.open_uis`; a stored ref couples gameplay state to UI lifecycle, goes stale, and refreshes only the one UI it points at (not observers/admins). /tg/ stores zero such refs on gameplay datums.
- **Fix:** remove the ref; route updates through `SStgui.update_uis(src)`.
- **Rule:** don't store UI refs on domain datums. Let the framework own UI lifecycle.

## 3. Disabling autoupdate + a custom update wrapper

- **Assumption:** "Update only what changed; autoupdate is wasteful."
- **Looked reasonable:** minimizing work sounds like good performance hygiene — and turning autoupdate off *is* a legitimate optimization.
- **Why wrong:** the mistake wasn't disabling autoupdate; it was building a wrapper proc that grabbed a tracked UI to push updates. With autoupdate off you still get click-driven updates free (`ui_act` truthy return -> `update_uis`); you only need to push *external* changes, and the idiomatic push is one line at the change site. ("Tgui updates automatically... having it off could be why there is a delay.")
- **Fix:** delete the wrapper; call `SStgui.update_uis(src)` directly from the attribute-modifier code (now at `attribute_modifier.dm:148`). The autoupdate-off flag stays.
- **Rule:** if you turn autoupdate off, collapse updates to `SStgui.update_uis(src)` at each external change site — no wrapper, no stored UI.

## 4. Generation counter + per-user dirty cache for `ui_data`

- **Assumption:** "Cache the stats/skills payload and only resend when a generation counter bumps."
- **Looked reasonable:** diff-updates are a standard optimization, and the counter felt like a cheap dirty flag.
- **Why wrong:** updates are on-demand already, so the cache earned little. Worse, a "total updates" counter is a bad cache key — it doesn't reflect whether *content* changed and risks stale/over-invalidation. ("That isn't a good metric for caching you want to stringify the stat skill information and compare. Not that I think caching is even required here since updates are on demand anyway.")
- **Fix:** delete the dynamic cache and the counter.
- **Rule:** measure first. If you must cache a dynamic payload, key on serialized content, not a counter.

## 5. Global cache for sanitized CSS class names — and the cache that *correctly survived*

- **Assumption:** "Sanitizing icon names is repeated work; memoize it globally."
- **Looked reasonable:** caching pure functions is a reflex.
- **Why wrong:** the set is ~20 static names sanitized once at menu build. The compute is negligible; the global cache is pure complexity and a stale-data surface.
- **Fix:** delete the cache; sanitize inline (the corrected backend calls `sanitize_css_class_name(...)` inline).
- **Nuance worth keeping:** the redesign *also* has `GLOB.attribute_menu_static_payload`, a global cache of the whole static metadata payload — and that one is **fine**, because the payload is identical for every user and effectively immutable (built once from game definitions). The deleted caches were a *trivial pure op* and a *per-user dynamic* payload. ("tgui already is cached in web cache... an interface shouldn't care who's using it only the data it's given.")
- **Rule:** caching shared, immutable, same-for-everyone data globally is fine; caching trivial ops or per-user dynamic data is not. The dividing question: is the cached value identical for all users and effectively immutable?

## 6. Backend sending presentation: `anchor` and `seal_label`

- **Assumption:** "Compute the layout key and the display label on the backend and ship them."
- **Looked reasonable:** it centralizes the mapping in one place (DM).
- **Why wrong:** it makes the backend aware of frontend layout and hardcodes a name->label map that drifts from the real definitions. `anchor` is just `name.toLowerCase()`; `seal_label` is `name` + `shorthand` (trivial in TS, especially after #6640 fixed the shorthands).
- **Fix:** drop both from the payload; derive in TS. (The corrected backend no longer sends them.)
- **Rule:** presentation classes and display strings belong in the frontend. The backend ships data; the interface decides how to show it. (Gray-area exception: a sanitized *spritesheet class* is the asset-pipeline handle for a sprite, closer to data — acceptable when it mirrors the spritesheet key.)

## 7. Raw HTML tags instead of components

- **Assumption:** "I'll just write `section`/`button`/`h3`/`div`."
- **Looked reasonable:** plain React/HTML is familiar and flexible.
- **Why wrong:** the framework's `Button`/`Box`/`Section`/`Stack` carry theming, spacing, scaling, and consistency. Raw tags opt out and drift from siblings. ("Use react classes Button, Box (Div/Span), Section, Stack not base HTML classes section, button, h3, etc.")
- **Fix:** replace raw tags with components; reserve raw tags for genuine free-form content.
- **Rule:** components are the default; raw tags are a rare, deliberate exception. (As of the WIP branch, `AttributeMenu.tsx` still carries ~78 raw tags — the frontend cleanup is the harder, still-pending half of this PR.)

## 8. Excessive SCSS and absolute-pixel layout

- **Assumption:** "A custom design needs a big custom stylesheet."
- **Looked reasonable:** bespoke visuals feel like they need bespoke CSS, and "nobody likes writing css" so it gets generated in bulk.
- **Why wrong:** ~1100+ lines (still ~1176 on the WIP branch) with heavy redundancy re-implemented layout the components already do, and absolute pixels fight TGUI scaling. ("The scss seems excessive... lots of absolute pixel measurements which also goes against tgui design.")
- **Fix:** adopt `Stack`/`Section`/`Box`, delete what the framework already does, drop absolute pixels and the bespoke scaling control (a UI-scaling var already exists), and base the theme on `RecipeBook.scss`.
- **Rule:** keep SCSS proportional; lean on components and the shared theme base.

## 9. A correctness bug hiding behind the redesign: value/base semantics

- **Symptom:** the UI showed "current / base", but base is altered by modifiers, and the stat/skill maxima (20 / 100) no longer applied cleanly. ("current/base is not right since the base value gets altered by modifiers... best to just omit it anyway.")
- **Deeper issue:** the menu computed skill values with one proc while the *game* used another (an effective-skill calc with default-attribute floors). The displayed number didn't match what the character actually rolled.
- **Fix:** display the value the game actually uses — the corrected backend's `get_attribute_ui_values` returns `return_effective_skill(...)`, the canonical calc. (Showing raw->effective with a modifier breakdown in the *detail* view is meaningful; a blanket "current/base" on every row was not.)
- **Rule:** when showing a derived gameplay value, display the *same* value the game uses (find the canonical calc the rest of the code reads), and don't invent display semantics the underlying system doesn't have.

## Cross-cutting takeaways

- The recurring failure mode is **building infrastructure the framework already provides** (window tracking, dedupe, caches, update fan-out, scaling). The fix is almost always *deletion* plus a one-line idiomatic call.
- Good patterns that survived review: splitting `ui_static_data` from `ui_data`, caching the *shared immutable* static payload, an O(1) name->datum lookup for `inspect` actions, and using the asset/spritesheet pipeline for icons.
- Backend lifecycle is the easy win and was cleaned up quickly; the frontend (components + SCSS) is the harder, slower cleanup. Reviewer feedback was about engineering, not taste: each "remove X" mapped to a concrete framework mechanism that made X redundant.
