# Source Index

Where this skill's claims come from, what was verified, and how to consult the sources yourself. This skill runs on whatever machine installs it — never assume any particular local file layout. If a task needs a source below and its location isn't known, ask the user rather than guessing a path.

## Contents

- [Source hierarchy](#source-hierarchy)
- [Verification results](#verification-results)
- [Consulting the DM Reference](#consulting-the-dm-reference)
- [Consulting the Discord developer logs](#consulting-the-discord-developer-logs)
- [Repository checkouts](#repository-checkouts)

## Source hierarchy

When sources conflict, higher wins for its own domain:

1. **Official DM Reference** — engine semantics. A copy ships with every BYOND install, typically under `<BYOND install directory>\help\ref\info.html` on Windows (e.g. under `Program Files (x86)\BYOND\`, but confirm on the machine at hand rather than assuming). Online: `https://www.byond.com/docs/ref/` (note: automated fetching may be blocked; the local copy is often the more reliable path).
2. **BYOND forum** (`https://www.byond.com/forum/`) — developer clarifications; date and BYOND version matter.
3. **Live repo code** — ground truth for what a codebase actually does; outranks any doc *about* the codebase.
4. **tgstation `.github/guides/`** — normative for tg conventions (tier 3); descriptive only for other forks.
5. **Fork guides** (`AGENTS.md`, CONTRIBUTING.md, local standards) — normative for their repo (tier 5 > 4).
6. **BYOND Discord developer logs** — heuristic grade: engine-developer statements are strong hints about internals, not documentation. Confirm against the reference or reproducible code when a decision hangs on one.
7. **Semantic bases (`ai_navigation*`)** — navigation aids; regenerable, never authoritative over code.

Tag discipline used throughout the references: `[DM Ref]`, `[tg]`, `[dev YYYY-MM-DD]` (the engine developer, on Discord), `[community YYYY-MM-DD]` (another experienced Discord participant — corroborating, not authoritative on internals), `[heuristic]`, `[measure]`. Keep the tags when editing; never promote a `[dev]`/`[community]`/`[heuristic]` claim to untagged fact without a documented source. **Never attach a real username/handle to a claim** — the tag records the *role* (engine developer vs. community participant), not identity; see Consulting the Discord developer logs below for why.

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

If the user has a local export of the official BYOND Discord (DiscordChatExporter JSON, one file per channel — dev-support, dev-chat, engine-insights, 516-migration, bugs-and-issues, dev-design, dev-showcase, and others are the ones known to carry engine content), ask them for its location rather than assuming a path — this is local, user-provided data, never something to hardcode or bake into the skill.

- **Highest-value channel**: `engine-insights` is the densest on undocumented internals (garbage-scan order, associative-list tree structure, string interning, SendMaps cost model, appearance behavior, flick internals, istype/locate costs, scheduler mechanics); `dev-support`/`dev-chat`/`bugs-and-issues`/`dev-design`/`516-migration` are higher-volume but lower-density.
- **Filter by role, not by identity.** The export's `author.name` field lets you isolate the engine developer's own messages from everyone else's — that authorship distinction is exactly what makes a statement `[dev]`-grade vs `[community]`-grade. Never surface, store, or write down the literal handle anywhere in the skill's output: the tag records the *role*, and a work product should never carry a third party's username. Do the identity filtering only transiently, in a throwaway script, while producing de-personalized, role-tagged notes.
- **Citation discipline**: `[dev YYYY-MM-DD]` for the engine developer's own statements (heuristic grade — see Source hierarchy above); `[community YYYY-MM-DD]` for another participant whose message content demonstrates real expertise (production experience, implementation-level detail, corroborated by other sources) — still not authoritative on engine internals; anything less clearly grounded is not citable at all, regardless of how many messages that participant has posted. Message *volume* is not a signal of expertise — a prolific poster can still be a beginner thinking out loud. Judge each message by its content, not its author's post count. Check message dates against the BYOND version in play (pre/post 515/516 changes especially).
- **Privacy, always**: read-only; never copy a username, handle, or any other personally-identifying detail into skill content, notes, or any other work product — extract only the technical claim itself, tagged by role and date. Never upload the logs anywhere.

## Repository checkouts

This skill's repository-profiles.md was authored by statically reading read-only checkouts of six named codebases: tgstation, BandaStation, cmss13, CEV-Eris, Twilight-Axis, Vanderlin. Where those checkouts live — if they exist at all — is entirely local to whatever machine and workspace this skill runs in; never assume a fixed layout or hardcode a path. If a semantic base (`ai_navigation/`) is available for the repo at hand, find it via the `semantic-controller` skill's discovery protocol rather than by name-guessing a folder.
