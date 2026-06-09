# TGUI Lifecycle, Performance & Caching

Read this when diagnosing TGUI slowness, deciding whether to disable autoupdate, or evaluating a cache. The mechanics below are taken from /tg/ framework source (`code/modules/tgui/external.dm`, `tgui.dm`, `code/controllers/subsystem/tgui.dm`) — verify the equivalent files in your fork, but the shape is the same across tgui-core forks (cmss13 differs only in the public proc name, `tgui_interact`).

## Contents
- How the lifecycle actually works (from source)
- Window pooling / dedup
- Autoupdate and the update path
- Static data changes need an explicit push
- First-load delay vs per-update delay (critical diagnosis)
- Asset caching (webview already does it)
- When custom caching is and isn't warranted (shared vs per-user)
- Generation counters / dirty flags

## How the lifecycle actually works (from source)

- **One UI per `(user, src_object)`.** `SStgui.try_update_ui(user, src, ui)` looks the UI up via `get_open_ui`, which scans `src_object.open_uis` for a matching user. Found -> it refreshes and returns it; not found -> returns null and you create one. That is the entire dedup mechanism — there is nothing for you to add.
- **`update_uis(src)` fans out to every viewer.** It iterates `src_object.open_uis` and re-`process()`es each open UI for that object — so one call refreshes every player, observer, and admin looking at the thing. A manually tracked single UI cannot do this.
- **`ui_act` truthy return drives updates.** In `on_act_message`: `if(src_object.ui_act(...)) SStgui.update_uis(src_object)`. This runs *regardless of autoupdate*. So a button handler that returns `TRUE` already refreshes all viewers.

## Window pooling / dedup

TGUI keeps every interface a user opens. BYOND does not destroy browser windows — it minimises them — so an "open" is really a refresh of a pooled window. That is why the canonical open is a single `if` starting with `SStgui.try_update_ui`. Consequences:

- You cannot normally open two of the same menu for one user. If you can, an upstream path broke `try_update_ui` (a timeout path, an alternate open path). Fix the root cause; a scanner that closes extras masks the real bug.
- You do not need to store, find, or close UIs yourself; `src.open_uis` already tracks them. /tg/ has **zero** long-lived `datum/tgui` vars on gameplay datums — every `var/datum/tgui/` in the codebase is a loop iterator inside the framework itself.

## Autoupdate and the update path

Autoupdate is a per-UI flag (`var/autoupdate = TRUE`, toggled with `ui.set_autoupdate(FALSE)`).

- **Autoupdate ON (default):** SStgui calls the UI's `process()` ~once per second, which re-calls `ui_interact(user, src)` and re-sends data. Leaving it on is the simplest correct choice. Plus, `ui_act` truthy returns still push immediately.
- **Autoupdate OFF:** there is no periodic refresh. Click-driven updates still work (via the `ui_act` truthy return -> `update_uis`), but **state changed outside `ui_act` will not appear until you push it.** Pair the off-switch with `SStgui.update_uis(src)` at every external change site (a potion edits a stat, a signal fires, another system mutates state).
- Prefer `SStgui.update_uis(src)` over grabbing one interface and calling `send_update()`. The manual approach only refreshes the one UI you happened to track and reintroduces the "store a ref" anti-pattern.

If you disabled autoupdate, the whole update story should collapse to: "on change, call `SStgui.update_uis(src)`." No wrapper proc, no stored UI, no per-user bookkeeping unless a profile proves it is needed. Disabling autoupdate is a legitimate optimization (it stops the per-second re-render of an expensive payload) — but only if the manual path is complete.

## Static data changes need an explicit push

`ui_static_data` is sent on open and then cached frontend-side; it is **not** re-sent by the autoupdate loop. The framework docstring is explicit: static data is "large data that should be sent infrequently... for heavy uis." If something the static payload depends on changes, call `update_static_data(user)` (or `update_static_data_for_all_viewers()`), which sends a full update. Forgetting this is the classic "I split it into static data and now my metadata never refreshes" bug. Corollary: only put genuinely stable data in `ui_static_data` — if it changes often, it belongs in `ui_data`.

## First-load delay vs per-update delay (diagnose before optimizing)

These are different problems with different fixes. Misdiagnosing wastes effort on the wrong layer.

- **First open is slow (~3-4s):** a known BYOND 516 <-> WebView communication + asset-transfer limitation. The bundle (`tgui.bundle.js`, ~780 KB), fonts (~1.2 MB), and spritesheets are pushed and then cached by the webview. It is *not* your React render or your DM payload. You cannot "debug it away" in interface code; it persists until assets shrink or BYOND updates. Do not rewrite render logic chasing it. (A genuine *bug* in the asset path is different — e.g. Vanderlin #6659 was a real asset-cache-confirmation timeout, fixed in the asset code, not the interface.)
- **Per-click / per-update is slow:** your update is doing too much work relative to peers — an oversized `ui_data` payload, recomputing everything every action, or an update fired far too often. This is the layer where payload-shaping and (measured) caching or disabling autoupdate help.

A useful tell: if only the *first* interaction lags and everything after is smooth, suspect assets/WebView. If *every* click lags, suspect your update.

## Asset caching — the webview already does it

Assets sent once are cached by the webview for the session. Do not fight this with ad-hoc base64 blobs or bespoke image caches. Use the project's asset pipeline:

- Spritesheets for many small icons (one CSS + sheet vs. many files); return them from `ui_assets()`. (See /tg/ `rdconsole.dm` / `_production.dm` returning `spritesheet_batched` datums.)
- `ui_assets()` / a simple asset datum / the asset cache for static images.

## When custom caching is (and isn't) warranted

Default to **no custom cache.** Add one only when you have measured a real cost. The decisive question is *who the cached value belongs to*:

- **Shared + immutable -> a global cache is fine.** Data that is identical for every user and effectively never changes (e.g. a static metadata payload built once from game definitions) can be built once and stored globally; it is content-addressed by being the same for everyone. (Vanderlin's `GLOB.attribute_menu_static_payload` is a legitimate example — it caches the shared static menu metadata, not per-user state.)
- **Per-user / dynamic -> almost never.** Updates are on-demand, so the dynamic payload is recomputed only when something changed — a per-user cache usually buys nothing and adds a stale-data surface. "An interface shouldn't care who's using it, only the data it's given," so per-user image/data caches are justified only when the content is genuinely personalized, and even then keyed by player/version, not a shared name.
- **Do not** globally cache tiny static lists or trivial pure ops (e.g. sanitizing ~20 icon names once at menu build). The compute is noise; the cache is pure complexity.
- If you *do* cache a dynamic payload, key on **meaningful serialized state** (stringify the relevant info and diff it), never on a vague "total updates" counter.

## Generation counters / dirty flags — be skeptical

A "generation counter + per-user last-sent generation" scheme is tempting for diff-updating, but:

- It is easy to bump in the wrong place, miss a mutation path, or desync per-user state and ship stale data.
- It reintroduces lifecycle bookkeeping that TGUI's on-demand updates already make unnecessary.
- In PR #6578 this exact mechanism was added, then deleted on review — updates are on-demand anyway, so the cache wasn't earning its complexity, and a counter is not a sound cache key (it doesn't tell you whether the *content* changed).

If you believe you need it, prove the cost first, then key the cache on serialized content, not a counter.
