# TGUI Guide

Updated on 2026-04-24 for Azure-Peak / RogueTown.

TGUI is the primary UI framework in this repository: DM backend objects expose data and actions, and React + TypeScript components render the browser UI. Use the live source paths below.

---

## Architecture Overview

```text
DM backend object/datum              React frontend
-----------------------              --------------
ui_interact() opens/updates       -> tgui/packages/tgui/routes.tsx resolves the interface
ui_data() / ui_static_data()      -> useBackend() reads data/static_data
ui_act(action, params, ui, state) <- act("action", params)
ui_state() / ui_status()          -> access and visibility checks
```

| Owner | Current Azure-Peak path | Notes |
|---|---|---|
| `SStgui` | `code/controllers/subsystem/tgui.dm` | Owns open TGUI instances. |
| `/datum/tgui` | `code/modules/tgui/tgui.dm` | One UI instance per open interface/user. |
| TGUI extension procs | `code/modules/tgui/external.dm` | Defines `ui_interact`, `ui_data`, `ui_static_data`, `ui_act`, `ui_state`, `ui_assets`, etc. |
| UI states | `code/modules/tgui/states.dm`, `code/modules/tgui/states/**` | Access and interaction state datums. |
| Custom HTML window | `code/modules/tgui/tgui_window.dm` | Lower-level BYOND browser wrapper. |
| Modal inputs | `code/modules/tgui_input/**` | `tgui_alert`, `tgui_input_text`, `tgui_input_number`, `tgui_input_list`, etc. |
| TGUI panel/chat | `code/modules/tgui_panel/**`, `tgui/packages/tgui-panel/**` | Chat, audio, telemetry, panel frontend. |

---

## Improved TGUI Development Algorithm (with Localization)

Localization is a design constraint for new TGUI work, not a cleanup step after the React view exists.

Required pipeline for every new user-facing TGUI interface:

1. Define the UI text schema before layout work: window title, section titles, labels, buttons, tooltips, notices, empty states, placeholders, table headers, tab names, confirmation copy, and dynamic formatted messages.
2. Bind the schema to the existing preferred UI language system: `DEFAULT_PREFERRED_UI_LANGUAGE`, `/datum/preferred_ui_language`, `client.preferred_ui_language`, and `client.get_preferred_ui_language()`.
3. Implement a DM localization provider, normally `/datum/ui_localization/<context>`, with English as the complete fallback language.
4. Return localized `texts` from `ui_static_data()` when stable, or `ui_data()` only when the text genuinely changes with frequent dynamic state.
5. Build the TSX view using only `texts.*` and localized DM-provided data fields for user-facing copy.
6. Validate the new interface with review or a future TGUI i18n lint/check path: no raw user-facing JSX strings in new interfaces.

Old flow to avoid:

```text
Create DM datum -> implement ui_data -> build TSX -> add strings directly
```

Required flow:

```text
Text schema -> preferred language binding -> DM localization provider -> ui_static_data/texts -> TSX consumes texts only -> raw string check
```

---

## Backend (DM Side)

### Required and common procs

| Proc | Required | Purpose |
|---|---:|---|
| `ui_interact(mob/user, datum/tgui/ui)` | Yes | Open a new UI or update an already open one via `SStgui.try_update_ui`. |
| `ui_data(mob/user)` | Yes | Dynamic JSON-safe data sent to the frontend. |
| `ui_static_data(mob/user)` | Optional | Large or mostly stable data cached on the frontend side. |
| `ui_act(action, list/params, datum/tgui/ui, datum/ui_state/state)` | For interactive UI | Handles frontend `act()` calls. Treat every param as untrusted. |
| `ui_state(mob/user)` | Optional | Returns a UI state datum. Default is `GLOB.default_state`. |
| `ui_assets(mob/user)` | Optional | Supplies asset datums/file assets needed by the UI. |

### Localized local pattern

```dm
/datum/ui_localization/example_menu
	supported_languages = list(DEFAULT_PREFERRED_UI_LANGUAGE, "ru")

/datum/ui_localization/example_menu/get_language_texts(language_code)
	switch(language_code)
		if("ru")
			return list(
				"window_title" = "Пример меню",
				"sections" = list(
					"status" = "Статус",
				),
				"labels" = list(
					"health" = "Здоровье",
					"color" = "Цвет",
					"action" = "Действие",
				),
				"actions" = list(
					"reset" = "Сбросить",
				),
			)

	return list(
		"window_title" = "Example Menu",
		"sections" = list(
			"status" = "Status",
		),
		"labels" = list(
			"health" = "Health",
			"color" = "Color",
			"action" = "Action",
		),
		"actions" = list(
			"reset" = "Reset",
		),
	)

/datum/example_menu/ui_interact(mob/user, datum/tgui/ui)
	ui = SStgui.try_update_ui(user, src, ui)
	if(!ui)
		var/list/texts = get_ui_texts(user, /datum/ui_localization/example_menu)
		ui = new(user, src, "ExampleMenu", texts["window_title"])
		ui.open()

/datum/example_menu/ui_static_data(mob/user)
	var/list/data = list()
	data["texts"] = get_ui_texts(user, /datum/ui_localization/example_menu)
	data["max_entries"] = max_entries
	return data

/datum/example_menu/ui_data(mob/user)
	var/list/data = list()
	var/list/entries = list()
	for(var/i in 1 to length(src.entries))
		entries += list(list(
			"index" = i,
			"text" = src.entries[i],
		))
	data["entries"] = entries
	return data

/datum/example_menu/ui_act(action, list/params, datum/tgui/ui, datum/ui_state/state)
	if(..())
		return TRUE

	switch(action)
		if("set_entries")
			var/list/new_entries = params["entries"]
			if(!islist(new_entries))
				return FALSE

			src.entries = new_entries
			return TRUE
```

Local examples to copy from:

| Interface | DM owner | Frontend component |
|---|---|---|
| Laws menu | `code/datums/laws.dm` | `tgui/packages/tgui/interfaces/LawsMenu.tsx` |
| Autosmither | `code/game/rotational_objects/autosmither.dm` | `tgui/packages/tgui/interfaces/Autosmither.tsx` |
| Text input | `code/modules/tgui_input/text.dm` | `tgui/packages/tgui/interfaces/TextInputModal.tsx` |
| Sex session | `code/datums/sexcon2/sex_session.dm` | `tgui/packages/tgui/interfaces/SexSession.tsx` |

### Backend rules

- Call `SStgui.try_update_ui(user, src, ui)` in `ui_interact`; only create a new `/datum/tgui` if it returns null.
- The interface name string in `new(user, src, "ExampleMenu")` must match the exported frontend component name.
- Use `get_ui_texts(user, /datum/ui_localization/<context>)` for window titles and frontend `texts`.
- Return only JSON-safe values from `ui_data` and `ui_static_data`: numbers, strings, booleans, nulls, and lists. Do not send atoms or datums directly.
- Prefer arrays/lists of records for frontend `.map()` calls.
- Put large stable lists and `texts` in `ui_static_data`; call `update_static_data()` or `update_static_data_for_all_viewers()` when those values change.
- In `ui_act`, call `..()` first and return if it handled or blocked the action.
- Validate every value in `params`: type-check lists, clamp numbers, restrict strings to known values, and avoid bare `locate(ref)` searches.
- Return `TRUE` only after handling an action that should refresh the UI; return `FALSE` for rejected/no-op actions.

---

## Localization Pattern (DM + TSX)

Use this DM-driven shape for new interfaces. If a shared helper exists in the branch, use it; otherwise keep the same contract locally and avoid frontend-side localization.

Backend contract:

```dm
/datum/ui_localization/<context>
	supported_languages = list(DEFAULT_PREFERRED_UI_LANGUAGE, "ru")

/datum/ui_localization/<context>/get_language_texts(language_code)
	// Return a structured JSON-safe list for the requested language.
```

DM integration:

```dm
/datum/my_context/ui_static_data(mob/user)
	var/list/data = list()
	data["texts"] = get_ui_texts(user, /datum/ui_localization/my_context)
	return data
```

Frontend contract:

```tsx
type Texts = {
  window_title: string;
  sections: {
    status: string;
  };
  actions: {
    reset: string;
  };
};

type Data = {
  texts: Texts;
};
```

Recommended shared helper shape:

```dm
/proc/get_ui_texts(mob/user, localization_type)
	var/language_code = user?.client?.get_preferred_ui_language() || DEFAULT_PREFERRED_UI_LANGUAGE
	return get_ui_texts_for_language(language_code, localization_type)

/proc/get_ui_texts_for_language(language_code, localization_type)
	// Cache by "[localization_type]|[language_code]".
	// Build /datum/ui_localization/<context>, merge chosen language over English fallback,
	// and return a structured JSON-safe list.
```

Performance rules:

- `get_ui_texts()` should cache by localization datum type and language code, so repeated `ui_data()` calls do not rebuild the text tree.
- Prefer `ui_static_data()` for `texts`, especially in large dynamic UIs such as ContractLedger and FamilyTree.
- Do not localize on every tick. Dynamic lists should carry already localized labels from DM, or stable IDs plus localized labels supplied in `texts`.
- If a user's preferred UI language changes while an interface is open, reopen the UI or call `update_static_data(user)` for that viewer.
- English must be complete. Other languages may omit keys; the shared merge helper should overlay the chosen language onto English fallback.

---

## Analysis of PR #6645 (what to keep / what to improve)

Reference: https://github.com/Azure-Peak/Azure-Peak/pull/6645

What to keep:

- ContractLedger made localization a first-class concern instead of leaving strings scattered across the final JSX.
- It separated text dictionaries from the main view with `ContractLedger.i18n.en.ts` and `ContractLedger.i18n.ru.ts`.
- It reused one `ContractLedgerView` for multiple language variants, reducing layout duplication.
- It introduced language selection through `preferred_ui_language` and used the chosen language when opening the interface.
- It used message keys such as `notice.*` and `preview.*`, which is a good shape for notices and empty states.

What to standardize differently:

- The locale source should be DM, not frontend i18n modules. The existing language preference lives in DM and TGUI already receives DM-owned data.
- Avoid separate route components such as `ContractLedger` and `ContractLedgerRu`; keep one interface name and pass `texts`.
- Avoid frontend `resolveText()`/formatter functions for user-facing copy. Format notices, labels, tier names, and pluralized messages in DM or send ready localized strings.
- Avoid fallback strings like ``Tier ${tier}`` in TSX; fallback belongs in `/datum/ui_localization`.
- Avoid returning only keys for visible text unless TSX is merely indexing `texts`; large dynamic rows should include localized display fields such as `type_label`, `tier_label`, and `status_text`.

---

## Rules & Enforcement

Hard rules for new TGUI interfaces:

- No hardcoded user-facing strings in `.tsx`/`.jsx`.
- No mixed-language UI: a single `texts` object must represent the viewer's chosen language with English fallback.
- No frontend-side localization logic, locale imports, or React i18n libraries for in-game TGUI.
- All visible text must come from DM through `texts` or localized DM-provided row fields.
- Action IDs, CSS class names, icon names, enum values, route names, and test IDs are not user-facing text and may remain literals.

Enforcement strategy:

- Add a lightweight `tgui:lint:i18n` check when enforcement is wired into tooling. It should flag obvious JSX text literals and user-facing string attributes in new or changed interface files.
- Code review checklist: every new TGUI PR must show the `/datum/ui_localization/<context>` schema, `texts` in `ui_static_data()` or justified `ui_data()`, and TSX consuming `texts.*`.
- Structural review signal: if the TSX `Data` type has no `texts` field, the interface is not ready for review unless it is a non-user-facing utility wrapper.

---

## Migration Strategy

Practical upgrade path for existing hardcoded interfaces:

1. Extract every visible TSX string into a text inventory: window title, sections, labels, buttons, tabs, notices, empty states, tooltips, placeholders, and formatted messages.
2. Create `/datum/ui_localization/<context>` with a complete English fallback tree and any available translated overlays.
3. Add `data["texts"] = get_ui_texts(user, /datum/ui_localization/<context>)` to `ui_static_data()` for stable UI copy.
4. For dynamic records, replace IDs that TSX localizes with DM-provided localized fields such as `name_text`, `status_text`, `tier_text`, or `description_text`.
5. Replace JSX literals with `texts.*` access.
6. Run the i18n check on the migrated files and review any remaining literals as either non-user-facing technical identifiers or real violations.

---

## Frontend (React/TypeScript Side)

### File location and routing

Put in-game interfaces under:

```text
tgui/packages/tgui/interfaces/MyThing.tsx
```

Azure-Peak routes components through:

```text
tgui/packages/tgui/routes.tsx
```

`routes.tsx` uses `require.context('./interfaces')` and attempts these names:

| Route candidate | Meaning |
|---|---|
| `./MyThing.tsx` | Preferred TypeScript React component. |
| `./MyThing.jsx` | JSX component. |
| `./MyThing.js` | JavaScript component. |
| `./MyThing/index.tsx` | Folder component entrypoint. |
| `./MyThing/index.jsx` | JSX folder entrypoint. |
| `./MyThing/index.js` | JavaScript folder entrypoint. |

The component must be exported by the same name used by DM:

```tsx
export const MyThing = () => {
  // ...
};
```

### Minimal component

Current interfaces generally import shared components from `tgui-core/components`, `useBackend` from `../backend`, and `Window` from `../layouts`.

```tsx
import { Button, LabeledList, Section } from 'tgui-core/components';

import { useBackend } from '../backend';
import { Window } from '../layouts';

type Data = {
  texts: {
    window_title: string;
    sections: {
      status: string;
    };
    labels: {
      health: string;
      color: string;
      action: string;
    };
    actions: {
      reset: string;
    };
  };
  health: number;
  color: string;
};

export const MyThing = () => {
  const { act, data } = useBackend<Data>();
  const { texts, health, color } = data;

  return (
    <Window width={420} height={260} title={texts.window_title}>
      <Window.Content scrollable>
        <Section title={texts.sections.status}>
          <LabeledList>
            <LabeledList.Item label={texts.labels.health}>{health}</LabeledList.Item>
            <LabeledList.Item label={texts.labels.color}>{color}</LabeledList.Item>
            <LabeledList.Item label={texts.labels.action}>
              <Button onClick={() => act('reset')}>
                {texts.actions.reset}
              </Button>
            </LabeledList.Item>
          </LabeledList>
        </Section>
      </Window.Content>
    </Window>
  );
};
```

### Frontend rules

- Type `useBackend<Data>()` for new TypeScript interfaces.
- Include a typed `texts` field in `Data` for any user-facing interface.
- Render user-facing copy from `texts.*` or localized DM-provided data fields only.
- Keep server state in DM; use React local state only for UI-only drafts, toggles, search filters, and confirmation state.
- Prefer derived values over extra `useState`.
- Always provide `key` when rendering arrays.
- Keep action names stable and validate them in DM `ui_act`.
- Follow existing imports and component idioms from nearby current files before copying older TG examples.

---

## Project Structure

| Path | Contents |
|---|---|
| `code/controllers/subsystem/tgui.dm` | `SStgui` subsystem. |
| `code/modules/tgui/**` | DM TGUI core, states, helpers, window wrapper. |
| `code/modules/tgui_input/**` | Modal input helpers and their DM datums. |
| `code/modules/tgui_panel/**` | DM side for panel/chat/audio/telemetry. |
| `tgui/package.json` | Bun workspace and TGUI scripts. |
| `tgui/packages/tgui/routes.tsx` | Auto-routing for interface component names. |
| `tgui/packages/tgui/interfaces/**` | In-game UI components. |
| `tgui/packages/tgui/components/**` | Local UI helper components. |
| `tgui/packages/tgui/layouts/**` | Root layout wrappers such as `Window`. |
| `tgui/packages/tgui/styles/interfaces/**` | Per-interface styles. |
| `tgui/packages/tgui/styles/layouts/**` | Layout styles. |
| `tgui/packages/tgui/styles/themes/**` | Theme styles. |
| `tgui/packages/tgui-panel/**` | Chat/stat panel frontend. |
| `tgui/packages/common/**` | Shared frontend helpers. |
| `tgui/docs/**` | Upstream-style TGUI docs copied with this repo. |

---

## Build and Dev Workflow

Use the Windows scripts from repo root:

```powershell
bin\tgui-build.cmd
bin\tgui-dev.cmd
bin\tgui-dev.cmd --reload
bin\test.cmd
```

Or use Bun from the `tgui/` directory:

```powershell
Set-Location tgui
bun install
bun tgui:build
bun tgui:dev
bun tgui:dev --reload
bun tgui:dev --debug
bun tgui:lint
bun tgui:tsc
bun tgui:test
bun tgui:analyze
```

Use the repo build tooling target if a clean is needed:

```powershell
tools\build\build.bat tgui-clean
```

If the dev server does not attach, open a TGUI window in-game first, then start or refresh the dev server. Browser inspection is enabled in-game through the Debug tab.

---

## Chat Embedded Components

Chat embedded components are handled by:

```text
tgui/packages/tgui-panel/chat/renderer.tsx
```

DM-side helper macros include:

```text
code/__DEFINES/spans.dm
```

Example:

```html
<span data-component="Tooltip" data-content="Hover text">Visible text</span>
```

| Attribute | Purpose |
|---|---|
| `data-component` | Component name whitelisted in `TGUI_CHAT_COMPONENTS`. |
| `data-*` | Props mapped by the renderer; see `TGUI_CHAT_ATTRIBUTES_TO_PROPS` behavior in the renderer. |

The Azure-Peak chat renderer source file is `tgui/packages/tgui-panel/chat/renderer.tsx`.

---

## Custom HTML Popups

Use `/datum/tgui_window` only for non-standard long-lived browser windows that need direct BYOND browser/window behavior. Standard gameplay UI should use `/datum/tgui`.

```dm
var/datum/tgui_window/window = new(usr.client, "custom_popup")
window.initialize(
	inline_html = "<h1>Hello</h1>",
	inline_js = "window.alert('hi')",
	inline_css = "h1 { color: red }",
	strict_mode = TRUE,
)
```

References:

| Need | Path |
|---|---|
| TGUI window wrapper | `code/modules/tgui/tgui_window.dm` |
| Custom popup docs | `tgui/docs/tgui-for-custom-html-popups.md` |
| BYOND skin API types | `tgui/global.d.ts` |

---

## Security Checklist

Every `ui_act` implementation should:

- Call `..()` first and return when it returns truthy.
- Validate every `params` value before use.
- Clamp numeric inputs with local constants.
- Scope object refs instead of using bare global `locate(ref)`.
- Reject unknown action strings.
- Return `TRUE` only after a handled state change.
- Keep client-side checks as convenience only; never rely on them for access or authority.

---

## Cross-References

- Backend TGUI core: `code/modules/tgui/**`
- TGUI subsystem: `code/controllers/subsystem/tgui.dm`
- Frontend router: `tgui/packages/tgui/routes.tsx`
- UI ownership map: `ai_navigation/subsystem_map.md`
- UI routing table: `ai_navigation/entrypoints.md`
