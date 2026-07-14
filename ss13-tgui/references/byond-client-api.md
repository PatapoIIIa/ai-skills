# BYOND client API for TGUI work

Curated from the official BYOND Reference (local copy ships with every BYOND install at
`BYOND/help/ref/info.html`; web copy at byond.com/docs/ref — note the site 403s generic fetchers)
and from /tg/'s bridge implementation (`tgui/packages/tgui-setup/helpers.js`, `tgui/docs/`).
Everything here is TGUI-relevant; the reference's game-side DM (atoms, procs, datums) is out of scope.

## The three bridge layers (pick the highest that fits)

1. **tgui proper** — `SStgui` + `/datum/tgui` + React. Use for any real interface. Everything below
   is plumbing that tgui already wraps.
2. **`/datum/tgui_window` custom popups** — tgui's window layer without React: `initialize(inline_html/inline_js/inline_css, assets, strict_mode)`, re-`initialize()` to swap content, `send_message(type, list)` / `window.subscribe(src, PROC_REF(on_message))` for typed DM↔JS messaging, `send_asset(asset)` for live asset delivery with retry. Use for static/bespoke client pages (stat panel, chat, music player). It is heavier than a dumb `browse()` page — don't use it for throwaway one-shot popups.
3. **Raw BYOND primitives** — `browse()`, `browse_rsc()`, `output()`, `link()`, `winset()`/`winget()`, Topic hrefs. Use only in framework/bridge code or when the fork predates tgui_window.

## The `Byond` JS object (tgui's, lowercase-b) — full surface

Defined by tgui itself in `tgui-setup/helpers.js` (served inline in every tgui page). Not to be
confused with the **native `BYOND` object (uppercase)** that BYOND 516 injects into every browser
control — same idea (`BYOND.winset/winget/command`, camelCase param aliases, Promise winget), but
only the native one exists in plain non-tgui `browse()` pages, and only the tgui one exists in
older webviews. Check which one your page actually has before calling.

- `Byond.call(path, params)` — the transport primitive: builds `byond://...?params`. Three routes
  under the hood: `cef_to_byond()` (516 BLINK webview), `location.href` (older IE), and **XHR when
  the URL exceeds 2048 chars** — the classic href length limit does not apply to tgui messages.
- `Byond.topic(params)` — `client/Topic()` call. `Byond.command(cmd)` — run a client verb/command
  as if typed (`winset` with `command`).
- `Byond.winset(id, prop, value)` / `Byond.winset(id, {props})` / `Byond.winget(id, prop|[props]|'*')`
  (async, Promise). `id = null` targets **global client parameters** — e.g.
  `Byond.winget(null, 'url')` returns the server address (usable for reconnect flows together with
  `Byond.command('.quit')`).
- `Byond.sendMessage(type, payload)` — the tgui message protocol (adds `tgui=1`, `window_id`,
  JSON-encodes payload). Extra top-level fields skip JSON and arrive in DM's `href_list` — cheaper
  for high-frequency messages (`{type, ref}` instead of a payload decode). Every send is a
  `client/Topic()` call and counts against the client's `SECOND_TOPIC_LIMIT`/`MINUTE_TOPIC_LIMIT`
  budget (see "The client→server topic budget" in `references/performance-and-lifecycle.md`).
- `Byond.subscribe(fn)` / `Byond.subscribeTo(type, fn)` — receive DM→JS `send_message()` traffic
  (queued until first subscriber; `window.update` is the wire).
- `Byond.parseJson(text)` — JSON.parse with the `__number__` reviver (BYOND encodes some numbers
  as `{"__number__": "..."}`); use it instead of raw `JSON.parse` for anything DM-sent.
- `Byond.loadJs(url)` / `Byond.loadCss(url)` — asset injection with retry/backoff (5 attempts);
  detects the empty-stylesheet failure mode. `Byond.saveBlob(blob, name, ext)` — client file save.
- Environment flags: `Byond.windowId`, `Byond.storageCdn`, `Byond.IS_BYOND`,
  `Byond.BLINK` (Chrome major version if webview2/CEF, else null — THE webview detection),
  `Byond.strictMode` (unhandled JS errors → visible FatalError bluescreen + `type: 'log'` message
  to DM; those are the `Error:` lines in tgui.log — grep them when triaging client crashes).

## Running JS from DM without the message protocol

`usr << output(url_encode(json_encode(data)), "browserid:jsFunctionName")` calls a JS function in
a browser control directly; args are URL-parameter parsed (that's why `url_encode` wraps it).
Works on any browser control including non-tgui popups. For a popup created by
`browse(content, "window=mypopup")`, BYOND actually creates a window control `mypopup` containing
a browser control named `browser` — the decorated id for winset/output targeting is
**`mypopup.browser`**.

## byondStorage (516) — persistence beyond the page

`localStorage` in BYOND browser controls behaves like `sessionStorage` (page-scoped). For real
persistence enable `byondstorage` via browser-options winset, then use (same API as localStorage):

- `hubStorage` — shared across all servers under the same hub entry;
- `serverStorage` — same hub path + same server address;
- `domainStorage` — same but ignoring port.

**Treat byondstorage as a small-settings store, not a database.** It is one json file per hub
entry on the player's disk (for SS13: `Documents\BYOND\browserstorage\Exadv1.spacestation13.json`,
shared by every SS13 server the player visits, regardless of codebase), flushed roughly every
10 seconds — large payloads (chat logs) turn that flush into whole-client hitches, which is why
current /tg/ moved chat persistence to an iframe+IndexedDB stack and demoted byondstorage to a
fallback. Generations, behavior traps, and fork guidance: `references/client-storage.md`.

Chat persistence rode on this in the 516 era and still does on many forks. Practical implication
from the field: persisted data **outlives builds** — client-side stores replay old payloads into
new bundles, so renderers of persisted content need unknown-shape guards (see the chat
`data-component` crash case in SKILL.md).

## Skin controls and the parameters worth knowing

Control types: `main` (window/pane), `child` (splitter host), `tab`, `browser`, `map`, `output`,
`input`, `button`, `label`, `grid`, `bar`, `info` (stat panel), `macro`, `menu`. The reference's
"parameters (skin)" section catalogs ~120 params; the ones that matter for TGUI work:

- **window (`main`)**: `size`, `pos`, `is-visible`, `is-maximized`, `is-minimized`, `is-fullscreen`,
  `can-close`, `can-resize`, `can-minimize`, `titlebar`, `title`, `statusbar`, `alpha`,
  `is-transparent` + `transparent-color` (click-through cutouts), `is-pane`, `inner-size`/`outer-size`,
  `on-close`, `on-size`, `on-status`, `focus`, `flash`, `macro`, `menu`, `icon`. tgui's `Window`
  layout drives exactly these (drag.ts does manual `pos`/`size` winsets because default titlebars
  are off).
- **browser**: `show-url`, `show-history`, `use-title` (page `<title>` renames the window!),
  `on-show`/`on-hide`, `enable-http-images`, plus `byondstorage` via browser-options.
- **map** (ByondUi embeds): `view-size`, `icon-size` (client-side upscale), `zoom`, `zoom-mode`
  (`normal|distort|blur`), `letterbox`, `text-mode`, `style` (CSS for maptext). These are the knobs
  for a map_view character preview's crispness — `zoom-mode=distort` for pixel-perfect scaling.
- **output** (chat-adjacent): `max-lines`, `link-color`/`visited-color`, `enable-http-images`,
  `image` (background), `style`.
- **input**: `command`, `no-command`, `is-password`, `multi-line`, `show-history`.
- **global (null id)**: `url` (current server), `dpi`, `screen-size`/`screen-pos`,
  `outer-mouse-pos` — read via `winget(null, ...)`; the DPI answer feeds scaling triage.
- **events**: `on-close`, `on-size`, `on-show`, `on-hide`, `on-focus`/`on-blur`, `on-change`,
  `on-tab`, `on-status` — each runs a client command string; embedded `[[*]]` expands params.

Client dot-commands usable via `Byond.command()`: `.output control:data` (514+), `.winset`,
`.sound file` (516), `.add-particles` (516), `.quit`, `.screenshot`, `.profile`.

## DM-side procs (one line each, for orientation)

`browse(body, "window=id;size=WxH;...")` — show HTML (winset-style options string);
`browse(null, "window=id")` closes. `browse_rsc(file, name)` — push a resource into the client
cache for later reference by name (the pre-asset-datum transport; asset datums wrap it).
`output(thing, "control")` — send text/atom to a named control (or `control:jsFunc`).
`link(url)` — client navigation (`byond://` reconnects). `winset/winget(player, id, params)` —
skin control I/O; `winclone(player, source_id, clone_id)` — clone skin controls at runtime.

## Client procs relevant to UI work

- **`client.RenderIcon(object)` (515+)** — renders an atom or appearance into a single icon
  **client-side, with all overlays, vis_contents, transforms and filter effects applied**. This is
  the native answer to "flatten a doll for a preview image": unlike server-side `getFlatIcon`
  clones it cannot drift from what the player actually sees (it IS the client renderer). It's a
  client proc (server can't render), so it needs a connected client and a round-trip — fine for
  previews, wrong for headless/CI paths. **SS13 caveat that keeps it from being a drop-in:** it
  composites the appearance **as if no plane masters existed**, and /tg/-style codebases bake
  emissive blockers into appearances as plain overlays (tg PR #57934, a maptick optimization) —
  so anything emissive-adjacent renders its blocker literally, a grey/black silhouette stamped
  over the sprite (same failure family as PR #91616's "black character previews" inside the
  render-plate pipeline). Current tgstation ships **zero** RenderIcon call sites; live previews go
  through map_view, where the real plane pipeline runs. Reserve RenderIcon for atoms whose
  appearance carries no plane-dependent overlays, or strip the emissive overlays off a copy
  first. Preview hierarchy therefore reads: ByondUi map_view (live, zero encoding, planes work) >
  `RenderIcon` (client-exact single image, plane-master caveat above) > server `getFlatIcon`
  (no client needed) > hand-rolled flatteners (never).
  **Delivery caveat (field-tested on a 516 fork):** the official doc's note "the returned icon is
  a cache file, *not* an /icon datum" has teeth — savefile serialization rejects the value, so an
  `icon2base64()` built on `WRITE_FILE(savefile[...], icon)` fails with a **client-side "Invalid
  argument" dialog and ZERO server runtime** (symptom: popup on every UI open, runtime logs
  clean), and wrapping the result in `icon(raw_render)` does NOT normalize it. Deliver via
  `fcopy()` to a served file / asset transport — the pattern the only real-world consumers use
  (painting canvases `fcopy` it straight to PNG) — never through savefile-based base64 helpers.
  Related fork idiom: tg-family `icon2base64()` returns the RAW base64 string without the
  `data:image/png;base64,` prefix — every caller wraps it manually; a "broken image with alt
  text" in tgui is usually a missing prefix, not a bad icon.
- **`client.MeasureText(text, style, width)` (513+)** — returns rendered `"WxH"` for maptext/CSS
  text; the correct way to size maptext popups instead of guessing character widths.
- **`client.control_freak`** — server-set flags (`CONTROL_FREAK_ALL`, `_SKIN`, `_MACROS`) that lock
  user skin customization/macros/F2. If a player's client ignores winset-driven UI or macros,
  check this var before debugging the interface.

## Fork reality check

Every fact above is version-sensitive: `byondStorage`, `.sound`, `.add-particles`, native `BYOND`
object are 516+; `.output` is 514+; older forks (or forks pinned to 515) have none of them. The
fork's `helpers.js`/`byond.js` equivalent is the ground truth for what the JS side actually
provides — read it before using anything listed here, exactly like any other "learn the local
names first" step.
