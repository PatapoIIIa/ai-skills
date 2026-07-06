# TGUI Lifecycle, Performance & Caching

Read this when diagnosing TGUI slowness, deciding whether to disable autoupdate, or evaluating a cache. The mechanics below are taken from /tg/ framework source (`code/modules/tgui/external.dm`, `tgui.dm`, `code/controllers/subsystem/tgui.dm`) — verify the equivalent files in your fork, but the shape is the same across tgui-core forks (cmss13 differs only in the public proc name, `tgui_interact`).

## Contents
- How the lifecycle actually works (from source)
- Window pooling / dedup
- Autoupdate and the update path
- The client→server topic budget (rate limiting)
- Static data changes need an explicit push
- First-load delay vs per-update delay (critical diagnosis)
- Asset caching (webview already does it)
- When custom caching is and isn't warranted (shared vs per-user)
- Generation counters / dirty flags
- /tg/ and Bubberstation patterns worth copying
- Review patterns: bad practices vs good replacements

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

## The client→server topic budget (rate limiting)

Every message the webview sends to the server — `act/*`, tgui-panel `ping`, the error relay (`type=log`), `setSharedState`, ByondUi `renderByondUi`/`unmountByondUi` — is a `client/Topic()` call, and tg-family forks rate-limit Topic in `client_procs.dm` via config `SECOND_TOPIC_LIMIT` / `MINUTE_TOPIC_LIMIT` (typical defaults 10/sec, 100/min). These are **fixed-window counters**: once the minute budget is burned, *every* topic from that client is dropped until the window rolls — not just the offending ones. Exemptions are narrow: clients with an admin holder, the `statbrowser` window, and any specially whitelisted handlers (e.g. a native-say datum). Field data: an actively-used live-preview menu (hover previews ~5-8/s while mousing a grid, held-key button autorepeat ~7/s, geometry reports, 3 embedded maps) legitimately exceeds both defaults.

Dropped topics are silent for the UI (a `to_chat` "action was ignored" line + a game.log entry). The symptom set masquerades as lag while server metrics (TiDi, maptick) are healthy:

- dropped `act` → dead/inconsistent clicks ("everything is jerky");
- dropped `renderByondUi` → embedded map controls never get placed/resized (black rectangle where the doll/camera should be);
- dropped tgui-panel `ping` → the chat panel thinks the connection died and stutters through reconnects.

**Diagnose from game.log, not from feel:** grep `topic limit`, split hits per player and per-second vs per-minute, and read the `type=`/payload in each logged line — it names exactly which message class was dying. One field incident: 467 hits looked like "everyone lags", but 429 belonged to a single client whose crashed tgui-panel was flooding `type=log&fatal=1` error relays (see the crash-flood cascade below); the healthy players' ~38 were short bursts during scale/fullscreen storms.

**Budget the interaction at design time.** Count topics per click before shipping: one "scale" click in a reviewed menu cost `act` + geometry report + 3 synthetic `window.resize` dispatches × 3 ByondUi maps × 1 `renderByondUi` each ≈ 11 topics; six clicks in 4s ≈ 66 topics — both limits gone. Mitigations in priority order:

1. **Eliminate framework chatter you don't need.** `ByondUi` sends a `renderByondUi` topic on *every* internal `render()` — mount plus every `window.resize` (100ms debounce) — solely to register the control id for the server-side crash-cleanup fallback (`terminate_byondui_elements`). If your DM already owns the control lifecycle (own teardown proc), pass `phonehome={false}`: topics stop entirely, positioning still works (winset is not a topic), and the component still unparents client-side on unmount and `beforeunload` regardless.
2. **Throttle/debounce the chatty paths client-side** — hover relays, geometry reports, synthetic resize retries (each dispatch multiplies across every mounted ByondUi).
3. **Raise the config limits** for genuinely topic-heavy UIs — a server remedy, not a code fix, and the limiter still guards against runaway floods.

**The crash-flood cascade** (pairs with the shared-packages section in SKILL.md): a fatally-crashed tgui window relays each JS error as a `type=log&fatal=1` topic. The flood burns the client's whole budget, and the limiter then eats their *legitimate* topics — so one broken window makes every window on that client look broken ("player X can't open anything"). Fix the crash (usually an upstream backport or persisted-history data problem), tell the player to clear the client cache; do not chase the phantom lag in your interface code.

## Static data changes need an explicit push

`ui_static_data` is sent on open and then cached frontend-side; it is **not** re-sent by the autoupdate loop. The framework docstring is explicit: static data is "large data that should be sent infrequently... for heavy uis." If something the static payload depends on changes, call `update_static_data(user)` (or `update_static_data_for_all_viewers()`), which sends a full update. Forgetting this is the classic "I split it into static data and now my metadata never refreshes" bug. Corollary: only put genuinely stable data in `ui_static_data` — if it changes often, it belongs in `ui_data`.

When static dependencies can change in bursts (research unlocks, surgery techweb updates, loaded protocols), copy /tg/'s batched pattern: schedule `update_static_data_for_all_viewers()` behind the local unique timer/addtimer mechanism instead of sending a full static refresh for every signal.

## First-load delay vs per-update delay (diagnose before optimizing)

These are different problems with different fixes. Misdiagnosing wastes effort on the wrong layer.

- **First open is slow (~3-4s):** a known BYOND 516 <-> WebView communication + asset-transfer limitation. The bundle, fonts, and spritesheets are pushed and then cached by the webview. It is *not* automatically evidence that the React render or DM payload is slow. Do not rewrite interface render logic before separating this baseline from a genuine asset-path bug such as an asset-cache-confirmation timeout.
- **Per-click / per-update is slow:** your update is doing too much work relative to peers — an oversized `ui_data` payload, recomputing everything every action, or an update fired far too often. This is the layer where payload-shaping and (measured) caching or disabling autoupdate help.

A useful tell: if only the *first* interaction lags and everything after is smooth, suspect assets/WebView. If *every* click lags, suspect your update.

## Asset caching — the webview already does it

Assets sent once are cached by the webview for the session. Do not fight this with ad-hoc base64 blobs or bespoke image caches. Use the project's asset pipeline:

- Spritesheets for many small icons (one CSS + sheet vs. many files); return them from `ui_assets()`. (See /tg/ `rdconsole.dm` / `_production.dm` returning `spritesheet_batched` datums.)
- `ui_assets()` / a simple asset datum / the asset cache for static images.

Base64 is a warning sign, not an automatic bug. It is still reasonable for rare dynamic photos, one-off generated previews, or grayscale/color cases that the normal icon reference cannot express. It becomes a performance smell when the UI sends many stable option images as base64 strings, regenerates them on interaction, or keeps a parallel thumbnail cache after spritesheets exist.

## When custom caching is (and isn't) warranted

Default to **no custom cache.** Add one only when you have measured a real cost. The decisive question is *who the cached value belongs to*:

- **Shared + immutable -> a global cache is fine.** Data that is identical for every user and effectively never changes (e.g. a static metadata payload built once from game definitions) can be built once and stored globally. The reviewed redesign retained this kind of shared metadata cache while removing its per-user dynamic cache.
- **Per-user / dynamic -> almost never.** Updates are on-demand, so the dynamic payload is recomputed only when something changed — a per-user cache usually buys nothing and adds a stale-data surface. "An interface shouldn't care who's using it, only the data it's given," so per-user image/data caches are justified only when the content is genuinely personalized, and even then keyed by player/version, not a shared name.
- **Do not** globally cache tiny static lists or trivial pure ops (e.g. sanitizing ~20 icon names once at menu build). The compute is noise; the cache is pure complexity.
- If you *do* cache a dynamic payload, key on **meaningful serialized state** (stringify the relevant info and diff it), never on a vague "total updates" counter.

## Generation counters / dirty flags — be skeptical

A "generation counter + per-user last-sent generation" scheme is tempting for diff-updating, but:

- It is easy to bump in the wrong place, miss a mutation path, or desync per-user state and ship stale data.
- It reintroduces lifecycle bookkeeping that TGUI's on-demand updates already make unnecessary.
- In a reviewed redesign this exact mechanism was added, then deleted — updates were already on-demand, so the cache did not earn its complexity, and a counter was not a sound cache key because it did not describe whether the content changed.

If you believe you need it, prove the cost first, then key the cache on serialized content, not a counter.

## /tg/ and Bubberstation patterns worth copying

- **Static/dynamic split only when payload size earns it.** /tg/'s conversion docs call `ui_static_data()` a heavy-UI optimization, and explicitly note that a UI whose data does not need live updates can disable autoupdate instead of forcing a static-data split.
- **Spritesheets plus ids/classes for repeated icon catalogs.** /tg/ fabrication, techweb, crafting, and Bubberstation preferences middleware send asset ids or sanitized spritesheet class names, not per-option base64 thumbnails.
- **Deduplicate huge static graphs.** /tg/ research consoles compress repeated ids before sending static techweb/design graphs. This is a targeted payload optimization, not a reason to add caches to small UIs.
- **Batch static refreshes.** /tg/ operating computer batches repeated static changes with a unique timer before calling `update_static_data_for_all_viewers()`.
- **Preferences middleware keeps preview updates local.** Bubberstation middleware delegates actions, updates preference data, calls `character_preview_view.update_body()` for visual-only body changes, and calls `preferences.update_static_data(user)` only when static dependencies such as quirks/options actually change.

## Review patterns: bad practices vs good replacements

Use this section when reviewing a TGUI change for "bad practices" and "good patterns." Treat it as a search checklist, not as a rule to reject all heavy UI work. Heavy work is acceptable when it is deliberate, measured, and kept off the hot path.

### Bad patterns to flag

- **Base64 option catalogs in `ui_static_data()`.** Many small `icon2base64()` strings in static data bloat the initial payload and make every `update_static_data()` expensive. Search for `icon2base64`, `thumbnail`, `thumb_cache`, and `ui_static_data` together.
- **Custom thumbnail caches after a spritesheet exists.** Once a picker uses `ui_assets()` and a spritesheet, old `*_thumbnail()` procs and global `*_thumb_cache` lists are dead complexity.
- **Image generation for simple enum state.** If a picker has become values like `None`, `White`, `Dark`, or simple modes, remove tile/icon renderers and option caches.
- **Full preview render in the click/hover hot path.** Dummy generation, `apply_prefs_to`, outfit equip, flattening, and `icon2base64` are BYOND-side heavy operations. Do not run them synchronously on every hover/click without a cache key and async path.
- **Replacement previews that stack over the current item.** For hair/accessory/body replacement, showing the candidate on top of the already-equipped current sprite gives plausible but wrong screenshots and often leads to extra rendering work.
- **Static data that depends on frequent state.** `ui_static_data()` is cached frontend-side. If a payload changes often, putting it there forces full static refreshes or stale UI.
- **Temporary instrumentation left in production code.** Disk loggers, timing locals using `world.timeofday`, render counters, and per-action traces are useful only while measuring. Remove them after they answer the question.
- **Vague generation counters as cache keys.** A counter says "something happened," not whether this payload changed. It is easy to desync and hard to review.
- **`try_update_ui` as control-flow lookup.** Code like `if(SStgui.try_update_ui(...))` followed by a second `try_update_ui()` call uses the open path as a UI finder and duplicates work. In normal code, assign once inside `ui_interact`; for exceptional close/control cases, inspect the local framework API instead of probing by refresh.

### Good replacements

- **Spritesheet plus stable ids/classes for large pickers.** Send sprites through `ui_assets()` and send only small ids/CSS classes in static data.
- **Simple enum values for simple modes.** Backgrounds, filters, and toggles should usually be values, not generated images.
- **Cache expensive preview output by meaningful serialized state.** Use a signature that includes the state that changes the rendered result: species, gender, clothing flags, direction, relevant feature data, colors, etc.
- **Render heavy previews asynchronously.** Let the UI update immediately with existing/placeholder state, build the expensive image in a `waitfor = FALSE` proc, then call `SStgui.update_uis(src)` if the signature still matches.
- **For replacement hover previews, render a base without the current customizer.** Temporarily disable the current entry, render/cache that base by `(customizer, preview signature)`, then overlay the candidate on the base.
- **Keep `ui_static_data()` genuinely static.** Put catalogs and immutable metadata there; put selected values, preview images, hover state, and anything frequently changing in `ui_data()`.
- **Batch repeated static refreshes.** If many signals mutate static metadata in one burst, use the local `addtimer(..., TIMER_UNIQUE)` or equivalent to coalesce `update_static_data_for_all_viewers()`.
- **Compress only truly huge repeated payloads.** ID compression is appropriate for techweb-scale static graphs; it is overengineering for small option lists.
- **Delete obsolete paths in the same iteration.** When a new path supersedes old code, remove the old proc, global cache, counters, and call sites before considering the feature done.

### Fast grep pass

Useful suspicious terms:

```text
icon2base64
ui_static_data
update_static_data
thumbnail
thumb_cache
GLOBAL_LIST_EMPTY.*cache
world.timeofday
WRITE_LOG
pref_log
set_autoupdate(FALSE)
if(SStgui.try_update_ui
getFlatIcon
render_preview
useLocalState
```
