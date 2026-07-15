# Source Index

Where this skill's claims come from, what was verified, and how to consult the sources yourself. Machine-specific paths noted here (and only here) reflect the workspace where the skill was authored (2026-07); if a path is gone, fall back to the public source.

## Contents

- [Source hierarchy](#source-hierarchy)
- [Verification results](#verification-results)
- [Consulting the DM Reference](#consulting-the-dm-reference)
- [Consulting the Discord developer logs](#consulting-the-discord-developer-logs)
- [Repository checkouts](#repository-checkouts)

## Source hierarchy

When sources conflict, higher wins for its own domain:

1. **Official DM Reference** — engine semantics. Local copy: `C:\Program Files (x86)\BYOND\help\ref\info.html` (ships with BYOND; matches the installed version). Online: `https://www.byond.com/docs/ref/` (note: automated fetching may be blocked; the local copy is the practical path).
2. **BYOND forum** (`https://www.byond.com/forum/`) — developer clarifications; date and BYOND version matter.
3. **Live repo code** — ground truth for what a codebase actually does; outranks any doc *about* the codebase.
4. **tgstation `.github/guides/`** — normative for tg conventions (tier 3); descriptive only for other forks.
5. **Fork guides** (`AGENTS.md`, CONTRIBUTING.md, local standards) — normative for their repo (tier 5 > 4).
6. **BYOND Discord developer logs** — heuristic grade: engine-developer statements are strong hints about internals, not documentation. Confirm against the reference or reproducible code when a decision hangs on one.
7. **Semantic bases (`ai_navigation*`)** — navigation aids; regenerable, never authoritative over code.

Tag discipline used throughout the references: `[DM Ref]`, `[tg]`, `[dev YYYY-MM-DD]` (Discord), `[heuristic]`, `[measure]`. Keep the tags when editing; never promote a `[dev]`/`[heuristic]` claim to untagged fact without a documented source.

## Verification results

Checked against the local official DM Reference during authoring (2026-07-15):

**Corrections to prior local material** (`ai_navigation_vanders_river/engine_limits.md` and siblings derived from the old Designer's Guide):

| Old claim | Verified reality | Ref section |
|---|---|---|
| Bitwise ops are 16-bit (max 65535) | **24-bit, max 16,777,215** | operators |
| Max view range 10 (21×21) | **~5000 tiles, roughly 70×70** | view / client.view |
| `sleep(0)`/`spawn(0)` "cost at least one tick" | **Not supported.** `sleep(0)` sleeps "as short a time as possible"; `spawn(0)` runs after currently-pending events — sub-tick resumption is possible | sleep, spawn |

**Confirmed by the Reference**: `for(x in list)` iterates a copy (except `world`); `walk_to`/`step_to` silently no-op beyond 2×`world.view` steps; `world.cpu` ≥100 = tick overrun; the GC reference list (vars, lists, tag, map, contents, vis_contents, running/sleeping procs, keyed mobs, attached images); circular references never GC'd; `world.contents` is not a reference; turfs/areas not GC'd; `del` clears obvious refs then searches all memory; `spawn` copies plain locals; `set waitfor` semantics; `sleep(-1)` backlog-check semantics.

**Left unverified / heuristic** (do not present as engine fact): `luminosity` 0–6 range; "GC pressure between ticks" phrasing; relative VM cost of built-ins vs DM loops (directionally supported by tg guidance and dev statements, but unmeasured here); all `[measure]`-tagged performance claims.

## Consulting the DM Reference

The local `info.html` is one large file with `<a name=...>` anchors. Effective queries (PowerShell/bash + grep):

- Find a section: `grep -o '<a name=[^>]*sleep[^>]*>' info.html`
- Extract a section: `awk '/<a name=\/proc\/sleep>/,/<a name=\/proc\/next-entry>/' info.html | sed 's/<[^>]*>//g'`
- Anchors follow `/proc/name`, `/statement/...` (`for` lives at `/proc/for/list`), `/world/var/name`, `/DM/topic` (e.g. `/DM/garbage`).

Always note the installed BYOND version when citing (the ref documents *that* version).

## Consulting the Discord developer logs

Location (machine-specific): `C:\Users\patap\OneDrive\Рабочий стол\BYOND GUIDE\` — DiscordChatExporter JSON dumps of the official BYOND Discord (channels: dev-support 272 MB, dev-chat 163 MB, engine-insights 12 MB, 516-migration, bugs-and-issues, …; coverage into 2026).

- **Highest-value channel**: `engine-insights` — ~1200 messages by `lummoxjr` (the engine developer) on internals: garbage-scan order, assoc-list structure (array + binary tree), string interning trees, SendMaps threading and cost model, appearance behavior, flick internals.
- Query pattern (files are large — filter, never load whole):
  ```python
  import json
  data = json.load(open(FILE, encoding="utf-8"))
  hits = [m for m in data["messages"]
          if m["author"]["name"] == "lummoxjr" and KEYWORD in m.get("content", "")]
  ```
- **Citation discipline**: engine-developer messages → cite as `[dev YYYY-MM-DD]`, heuristic grade; other participants' messages are opinions — usable as leads only. Check message dates against the BYOND version in play (pre/post 515/516 changes especially).
- **Privacy**: read-only; don't copy usernames or personal content beyond the technical statement; never upload the logs anywhere.

## Repository checkouts

Authoring-time read-only checkouts (see repository-profiles.md for content): `C:\Axis\tgstation`, `C:\Axis\BandaStation-Kagelite_DEV`, `C:\Axis\cmss13-MARINES`, `C:\Axis\CEV-Eris`, `C:\Axis\Twilight-Axis`, `C:\Axis\Vanderlin`. Workspace semantic bases live alongside them in `C:\Axis\ai-skills\` (`ai_navigation_tg_banda_kaga`, `ai_navigation_twilight`, `ai_navigation_vanders_river`) plus one in-repo base (`BandaStation-Kagelite_DEV/ai_navigation/`). Discover bases via the `semantic-controller` skill's protocol rather than hardcoding these names elsewhere.
