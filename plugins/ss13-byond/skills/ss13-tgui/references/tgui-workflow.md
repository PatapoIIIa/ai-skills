# TGUI Implementation Workflow & Review Checklist

The long-form companion to `SKILL.md`. Read it when implementing a new interface or doing a thorough review.

## Contents
- Step 0: learn the local names
- The data-driven contract
- Backend procs and what belongs in each
- UI state and action security
- The standard entry-proc pattern (and why deviating is usually wrong)
- DM list shapes after JSON
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
| `ui_state(user)` | Interaction policy | Range, consciousness, access, inventory, remote-use policy |
| `ui_act(action, params, ui, state)` | Handle interactions | Call parent, validate hostile input, mutate state, return TRUE when handled |

Splitting `ui_static_data` from `ui_data` keeps each dynamic update small and avoids resending immutable metadata every refresh — /tg/'s `rdconsole.dm` even carries the comment *"heavy data from this proc should be moved to static data when possible."* But it is an **optimization for heavy payloads, not a mandate**: ~210 of tgstation's interfaces use it, far from all of them. Two caveats:

- Static data is sent on open and cached frontend-side; it is **not** re-sent by autoupdate. If it changes, call `update_static_data(user)` (or `update_static_data_for_all_viewers()`). See `references/performance-and-lifecycle.md`.
- Only put genuinely stable data in `ui_static_data`. If a field changes during normal play, it belongs in `ui_data`.
- If **all** of a UI's data does not need live updates, disabling autoupdate can be simpler than inventing a static-data split. Then every external mutation must push `SStgui.update_uis(src)`.
- If static data changes can arrive in bursts, batch `update_static_data_for_all_viewers()` with the repo's unique timer/addtimer pattern.
- If a static payload is techweb-scale and repeats many long ids, consider payload deduplication/compressed ids. Do not add this to small option lists.

## UI state and action security

`ui_state()` decides whether the user may see or interact with the UI. Use the repo's existing state datums and neighboring interfaces for range, consciousness, inventory, access, and remote-use rules. Do not reproduce authorization in React: frontend visibility is presentation, not security.

Treat every `action` and `params` value as client-controlled input:

```dm
/datum/thing/ui_act(action, list/params, datum/tgui/ui, datum/ui_state/state)
	. = ..()
	if(.)
		return

	switch(action)
		if("set_amount")
			var/amount = text2num(params["amount"])
			if(!isnum(amount))
				return FALSE
			amount = clamp(amount, MIN_AMOUNT, MAX_AMOUNT)
			// Mutate only after validation.
			. = TRUE
```

- Always follow the local parent-call pattern. In modern `/tg/`, the parent rejects actions when the UI is not interactive or the caller is not the UI user.
- Validate types, ranges, membership, permissions, and referenced objects on the backend. A disabled or hidden button is not an authorization check.
- Prefer `ui.user` over implicit `usr` when the local `ui_act` signature provides it; it makes the actor explicit and avoids hidden caller coupling.
- Return truthy only for an action that was handled. That return is also the normal signal for TGUI to update the open viewers.
- Copy the local conversion idiom (`text2num`, `text2path`, `locate`, helpers, or native typed params) because payload types differ between TGUI generations. Never assume every param is a string.

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
- **Do not use `try_update_ui` as a lookup predicate.** A pattern like `if(SStgui.try_update_ui(...))` followed by another `try_update_ui()` call refreshes twice and treats the open path as control flow. Assign once inside the entry proc; for unusual close/control behavior, use the framework's explicit open-UI helpers and document why.

## DM list shapes after JSON

Design the DM payload for the TypeScript operation that will consume it:

- A sequential DM list becomes a JavaScript array. Use this for ordered collections that the frontend will `map`, `filter`, or sort.
- An associative DM list becomes a JavaScript object. Use this for records and key-based lookup, and type it as `Record<string, T>` or a named object shape.
- At boundaries, default missing collections to `[]` or `{}` as appropriate. Do not call array methods on an associative-list payload.
- DM booleans arrive as numeric-like values in many forks; type them with the local `BooleanLike` equivalent rather than `boolean`.

Prefer sending a clean array of records when ordering and iteration are the primary use. Prefer an object when stable keyed lookup is the actual contract; do not mechanically convert every associative list.

## Frontend split

- `useBackend()` (from the local backend module) for `data` and `act`.
- Type the payload: `type Data = { ... }`, `const { act, data } = useBackend<Data>();`, with `BooleanLike` for DM booleans. This is the standard idiom across tgui-core forks and cmss13 alike.
- Render from `data`. Treat fields as optional and tolerate omitted keys — TGUI shallow-merges `data` between updates, so a `ui_data` that omits an unchanged block leaves the previous value intact frontend-side. Guard with `|| {}` / `|| []` defaults.
- Split a large interface into focused components with explicit props. Keep backend access near the interface boundary unless a child genuinely needs to dispatch/read shared backend state.
- Memoize derived structures (`useMemo`) and heavy components (`memo`) when a profile shows churn — not preemptively.

## Deriving presentation in the frontend

If a value can be computed from data already present, compute it in TS — don't add a backend field. Examples from a reviewed redesign:

- `anchor` (which CSS position class a stat seal uses) was sent from DM. It is just `name.toLowerCase()` — derive it in TS.
- `seal_label` (the "Strength (STR)" string) was hand-built in DM with a hardcoded name->label map. After the stat `shorthand` values were fixed upstream, the label is simply `name` + `shorthand` — build it in TS.

Sending these from the backend made the DM aware of frontend layout and created a hardcoded mapping that drifted from the real definitions. The rule: **presentation classes and display labels live in the frontend.**

## Full review checklist (with rationale)

Add these performance-specific checks to the list below when relevant:

- Repeated static changes are batched instead of firing full static refreshes per signal.
- Repeated icon catalogs use `ui_assets()`/spritesheets; base64 is reserved for deliberate one-off or dynamic cases.
- Huge static graphs may dedupe repeated ids; small option lists should not grow compression machinery.

1. **Local names** — entry proc (`ui_interact`/`tgui_interact`) and component imports match the repo's neighbors?
2. **Entry-proc shape** — matches the local `try_update_ui` pattern? Anything extra (refs, scanners) is suspect.
3. **Duplicate windows** — handled by TGUI, not custom code? Custom dedupe usually masks a broken open path.
4. **Interaction policy** — `ui_state()` matches the intended range, consciousness, access, inventory, and remote-use behavior?
5. **Action security** — parent `ui_act` called first, rejected/handled actions stopped, and every client param validated before mutation?
6. **Update routing** — `ui_act` return value + `SStgui.update_uis(src)` instead of manually grabbing a UI and `send_update()`? If static data changed, is `update_static_data()` called?
7. **Autoupdate** — if off, is there a complete manual update path (`SStgui.update_uis(src)` at every external change site)?
8. **Static vs dynamic** — heavy metadata in `ui_static_data`, volatile state in `ui_data`, split only where the payload justifies it?
9. **JSON shape** — sequential DM lists typed as arrays, associative lists typed as objects, with matching `[]`/`{}` defaults?
10. **Data, not presentation** — backend free of CSS classes / layout anchors / display labels that TS or CSS can derive?
11. **Assets** — icons via the project's spritesheet/asset pipeline through `ui_assets`?
12. **Caching** — justified by *measured* cost, and shared-immutable (OK to cache globally) vs per-user-dynamic (usually not)?
13. **Delay diagnosis** — first-load (framework/WebView/assets) distinguished from per-click/update delays (your payload/render)?
14. **State** — React state reserved for real interaction/asynchrony, with derived values computed directly from props/backend data?
15. **Components** — each element chosen by semantics (`Button` for actions, `Section` for titled panels, `Box` for layout blocks, `Box as="span"` for inline text; raw HTML only with a concrete technical reason — never a blanket `Box as="..."` tag swap; see `references/components-and-style.md`), with large interfaces split into focused components?
16. **SCSS size** — proportional to the problem, not re-implementing component layout? No absolute-pixel layout or bespoke scaling when a UI-scaling var exists?
17. **Guide currency** — external guides treated as version-sensitive (Paradise's is for older TGUI; old `/tg/` tgui-next and migration guides are historical)?
