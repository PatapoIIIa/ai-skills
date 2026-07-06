# Client-side storage and persistence (chat settings, chat history, panel state)

Read this when the task involves: chat settings or history not saving; "the whole client hitches
every 10–30 seconds while the server is healthy"; fancy-chat crashes right after a player hops
between servers; `byondStorage`/`hubStorage`, `storage.ts`, `Byond.storageCdn`,
`STORAGE_CDN_IFRAME`; or backporting /tg/'s storage stack to a fork.

The rule up front: **client persistence is fork-generational.** Identify the generation by reading
the fork's `tgui/packages/common/storage.ts|js` before touching anything — each generation has a
different failure mode, and a "fix" imported from the wrong generation makes things worse.

## The three generations

**Gen 1 — direct IndexedDB (pre-516 webviews, old tgui).** A `StorageProxy` picks
IndexedDB → localStorage → in-memory, falling back gracefully because IE11 environments randomly
break each backend (tgchat introduced IndexedDB persistence; the proxy and the IE11 localStorage
try/catch dance came right after — see lineage below). Worked because the IE-era webview gave
pages a stable origin.

**Gen 2 — byondstorage backend (BYOND 516 era).** 516 replaced the IE webview and the old origin
died with it, so settings silently stopped saving. BYOND added the `byondstorage` API
(`hubStorage`/`serverStorage`/`domainStorage` — API surface in `byond-client-api.md`), Paradise
wrote the first tgui backend for it, /tg/ ported it. **Mechanics that matter:** byondstorage is
ONE json file per hub entry on the player's disk (`Documents\BYOND\browserstorage\<hub>.json` —
for SS13 that is `Exadv1.spacestation13.json`, shared by **every SS13 server the player visits,
regardless of codebase**), and BYOND flushes it to disk roughly every 10 seconds. Fine for small
settings. Append-forever data (chat logs) grows it without bound → whole-client hitches every
10–30 s with perfectly healthy server metrics, plus foreign servers' chat bleeding into yours.

**Gen 3 — iframe + IndexedDB (current /tg/).** Upstream went back to IndexedDB, solving 516's
"no persistent origin" problem by loading a hidden iframe from a fixed https origin and speaking
postMessage RPC to it (`get`/`set`/`remove`/`clear`; `'ready'` handshake on load; the parent
HEAD-probes the URL and gives up after 5 s). The page is `tgui/public/iframe.html`, hosted on the
server's webroot CDN or the `tgstation/byond-client-storage` GitHub Pages site; configured via
`STORAGE_CDN_IFRAME` → `Byond.storageCdn`. byondstorage remains as failover. Current preference
order (post-rework): a configured, reachable iframe wins even if `hubStorage` is already live;
legacy byondstorage is imported only when the iframe cache is empty; unreadable legacy keys are
skipped instead of blocking the migration.

## Behavior traps (each verified upstream)

- **The iframe origin IS the storage bucket — and iframe.html does not namespace it.** The page
  opens a fixed IndexedDB (`tgui` db, `storage` store) keyed only by whatever the parent sends
  (`chat-messages`, `chat-state`, `panel-settings`). Every codebase pointing at the SAME iframe
  URL shares one bucket — which quietly recreates the cross-codebase contamination byondstorage
  had. A fork adopting Gen 3 must host its OWN iframe page (own origin = own bucket); do not ship
  tg's example `STORAGE_CDN_IFRAME` URL as a fork default.
- **Never migrate chat history between backends or servers — settings only.** /tg/ deliberately
  migrates just `panel-settings` and leaves `chat-messages` behind: persisted foreign chat
  contains `data-component` HTML whose replay is exactly the React #130 burst crash documented in
  SKILL.md ("Shared tgui packages"). The migration rework exists because server-hopping players
  hit this in the wild.
- **`byondstorageupdated` fires BEFORE the storage object exists.** After
  `winset(null, 'browser-options', '+byondstorage')`, wait for the event *and then* defer a tick
  (`setTimeout(..., 1)`) before touching `hubStorage`. /tg/'s `storage.ts` does exactly this, with
  an apologetic comment, in two places.
- **byondstorage is runtime-toggleable:** `winset(null, 'browser-options', '+byondstorage')` /
  `'-byondstorage'`. Upstream enables it just long enough to migrate legacy settings, then turns
  it back off so the disk json stops being touched.
- **Persisted data outlives builds — in every generation.** Renderers of persisted content need
  unknown-shape guards (the chat `data-component` case in SKILL.md).

## Diagnosis map

| Report | First check |
|---|---|
| "Chat settings don't save" on a 516 fork | Which generation is `storage.ts`? Gen 1 code on a 516 client = dead origin; needs a Gen 2/3 backport |
| Whole client hitches every 10–30 s, all windows, server healthy | Size of `Documents\BYOND\browserstorage\*.json`. Local workaround = delete the file; real fix = stop persisting big data on byondstorage (Gen 3 backport) |
| Fancy chat crashes right after switching servers | Foreign persisted chat history replaying — React #130 signature in SKILL.md; check what the storage backend migrated |
| Iframe storage "randomly" falls back to byondstorage | The HEAD probe / 5 s timeout against `Byond.storageCdn` is failing; verify CDN reachability and the current fallback rules before touching chat code |

## Review rules

- Treat `hubStorage`/byondstorage as a SMALL-settings store. Any chat-log-sized or append-forever
  payload aimed at it is a defect (the 10-second disk flush turns it into periodic client-wide
  hitches), not a style preference.
- Backporting the Gen 3 stack is an upstream sync, not a divergence — same policy as
  shared-package fixes in SKILL.md — but it is only complete with a self-hosted iframe page and a
  config entry, not just the `storage.ts` diff.
- When reviewing a migration or import between storage backends, ask what happens to another
  codebase's keys: skip unreadable ones, never replay foreign chat, and gate the whole import on
  the destination being empty.

## Upstream lineage (provenance; all tgstation/tgstation unless noted)

Use these to justify recommendations, not as reading assignments:

- IE11 localStorage try/catch: https://github.com/tgstation/tgstation/pull/52356
- tgchat + IndexedDB persistence: https://github.com/tgstation/tgstation/pull/52426
- StorageProxy graceful fallback: https://github.com/tgstation/tgstation/pull/53294
- First 516 byondstorage backend (Paradise): https://github.com/ParadiseSS13/Paradise/pull/25363
- byondstorage backend ported to /tg/: https://github.com/tgstation/tgstation/pull/88624
- Hitching/bloat evidence: https://github.com/tgstation/tgstation/issues/89988,
  https://github.com/tgstation/tgstation/issues/92035
- iframe + IndexedDB move (`STORAGE_CDN_IFRAME`, byond-client-storage repo):
  https://github.com/tgstation/tgstation/pull/93044
- Post-merge fixes (config unset, spurious failover): https://github.com/tgstation/tgstation/pull/94030
- Preference/migration rework after server-hop crashes: https://github.com/tgstation/tgstation/pull/96167
