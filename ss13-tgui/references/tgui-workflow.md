# TGUI Implementation Workflow & Review Checklist

The long-form companion to `SKILL.md`. Read it when implementing a new interface or doing a thorough review.

## Contents
- Step 0: learn the local names
- The data-driven contract
- Backend procs and what belongs in each
- The standard entry-proc pattern (and why deviating is usually wrong)
- Frontend split
- Deriving presentation in the frontend
- Full review checklist with rationale

## Step 0: learn the local names

TGUI's concepts are stable across forks; its identifiers are not. Before writing anything, grep one neighboring interface in the *current* repo and copy:

- **The backend entry proc.** `ui_interact` in /tg/, Vanderlin, BandaStation; `tgui_interact` in cmss13. (`git grep -l "tgui_interact" code/` vs `ui_interact` tells you instantly.)
- **The component import path.** `tgui-core/components` in tgui-core forks; in-tree `tgui/components` in older ports. Same with `useBackend` (`../backend` vs `tgui/backend`) and `Window` (`../layouts` vs `tgui/layouts`).
- **The asset pipeline call** the repo uses for icons (spritesheet datums, `ui_assets`).

Skipping this is the fastest way to write code that does not compile in the repo you are actually in. See `references/source-corpus.md` for the per-repo table.

## The data-driven contract

An interface should care about **the data it is given, not who is using it.** This single idea drives most good TGUI decisions:

- The backend computes domain values and ships them as plain data.
- The frontend decides how to lay them out, color them, label them, and arrange them.
- "Personalized for this player" is a property of the *data* (different numbers), not of the *interface code* (which stays generic).

If you find the backend emitting CSS classes, layout anchor keys, or display labels, that is a smell — move it to TS/CSS where it belongs. The backend should not know the interface arranges things in, say, a ring. (Edge case: a sanitized *spritesheet class* that is the asset-pipeline handle for a sprite is closer to data than styling — acceptable when it mirrors the spritesheet key, not when it encodes layout.)

## Backend procs

| Proc | Purpose | Put here |
| --- | --- | --- |
| `ui_interact(user, ui)` / `tgui_interact` | Open/refresh the window | The `try_update_ui` dance, nothing else |
| `ui_static_data(user)` | Heavy, rarely-changing metadata | Names, descriptions, icon ids, category structure |
| `ui_data(user)` | Dynamic state | Current values, toggles, selection |
| `ui_assets(user)` | Static assets | Spritesheets, simple assets via the asset cache |
| `ui_act(action, params, ui, state)` | Handle interactions | Mutate state; return TRUE to signal handled -> triggers `update_uis` |

Splitting `ui_static_data` from `ui_data` keeps each dynamic update small and avoids resending immutable metadata every refresh — /tg/'s `rdconsole.dm` even carries the comment *"heavy data from this proc should be moved to static data when possible."* But it is an **optimization for heavy payloads, not a mandate**: ~210 of tgstation's interfaces use it, far from all of them. Two caveats:

- Static data is sent on open and cached frontend-side; it is **not** re-sent by autoupdate. If it changes, call `update_static_data(user)` (or `update_static_data_for_all_viewers()`). See `references/performance-and-lifecycle.md`.
- Only put genuinely stable data in `ui_static_data`. If a field changes during normal play, it belongs in `ui_data`.

## The standard entry-proc pattern

```dm
/datum/thing/ui_interact(mob/user, datum/tgui/ui)   // or tgui_interact in cmss13
	ui = SStgui.try_update_ui(user, src, ui)
	if(!ui)
		ui = new(user, src, "InterfaceName")
		ui.open()
```

Why this is the whole pattern, and why custom machinery around it is a mistake:

- **TGUI pools windows.** `try_update_ui` finds the existing pooled UI for `(user, src)` and refreshes it instead of creating a duplicate. BYOND minimises browser windows rather than closing them.
- **You do not need to track the UI yourself.** Open UIs live in `src.open_uis`. Storing a long-lived `datum/tgui` reference on a domain datum couples gameplay state to UI lifecycle and goes stale — /tg/ never does it.
- **You do not need to dedupe windows.** If a user can open two of the same menu, something upstream of `try_update_ui` is broken. Fix the root cause; do not add a scanner.

## Frontend split

- `useBackend()` (from the local backend module) for `data` and `act`.
- Type the payload: `type Data = { ... }`, `const { act, data } = useBackend<Data>();`, with `BooleanLike` for DM booleans. This is the standard idiom across tgui-core forks and cmss13 alike.
- Render from `data`. Treat fields as optional and tolerate omitted keys — TGUI shallow-merges `data` between updates, so a `ui_data` that omits an unchanged block leaves the previous value intact frontend-side. Guard with `|| {}` / `|| []` defaults.
- Memoize derived structures (`useMemo`) and heavy components (`memo`) when a profile shows churn — not preemptively.

## Deriving presentation in the frontend

If a value can be computed from data already present, compute it in TS — don't add a backend field. Concrete examples from PR #6578:

- `anchor` (which CSS position class a stat seal uses) was sent from DM. It is just `name.toLowerCase()` — derive it in TS.
- `seal_label` (the "Strength (STR)" string) was hand-built in DM with a hardcoded name->label map. After the stat `shorthand` values were fixed upstream, the label is simply `name` + `shorthand` — build it in TS.

Sending these from the backend made the DM aware of frontend layout and created a hardcoded mapping that drifted from the real definitions. The rule: **presentation classes and display labels live in the frontend.**

## Full review checklist (with rationale)

1. **Local names** — entry proc (`ui_interact`/`tgui_interact`) and component imports match the repo's neighbors?
2. **Entry-proc shape** — matches the local `try_update_ui` pattern? Anything extra (refs, scanners) is suspect.
3. **Duplicate windows** — handled by TGUI, not custom code? Custom dedupe usually masks a broken open path.
4. **Update routing** — `ui_act` return value + `SStgui.update_uis(src)` instead of manually grabbing a UI and `send_update()`? If static data changed, is `update_static_data()` called?
5. **Autoupdate** — if off, is there a complete manual update path (`SStgui.update_uis(src)` at every external change site)?
6. **Static vs dynamic** — heavy metadata in `ui_static_data`, volatile state in `ui_data`, split only where the payload justifies it?
7. **Data, not presentation** — backend free of CSS classes / layout anchors / display labels that TS or CSS can derive?
8. **Assets** — icons via the project's spritesheet/asset pipeline through `ui_assets`?
9. **Caching** — justified by *measured* cost, and shared-immutable (OK to cache globally) vs per-user-dynamic (usually not)?
10. **Delay diagnosis** — first-load (framework/WebView/assets) distinguished from per-click/update delays (your payload/render)?
11. **Components** — the repo's primitives (`Button`/`Box`/`Section`/`Stack`/`Window`) over raw `div`/`button`/`h3`/`section`, with raw tags only as a deliberate exception?
12. **SCSS size** — proportional to the problem, not re-implementing component layout? No absolute-pixel layout or bespoke scaling when a UI-scaling var exists?
13. **Guide currency** — external guides treated as version-sensitive (Paradise's is for older TGUI)?
