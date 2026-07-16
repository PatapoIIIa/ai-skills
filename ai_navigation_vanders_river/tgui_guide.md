# TGUI Guide

Updated 2026-07-16. Framework knowledge (ui_interact/ui_data/ui_act contract, update strategy, React components/hooks/state rules, JSX, interface splitting, security checklist, runtime triage) lives in the **ss13-tgui** skill — read it for any TGUI implementation or review work. This file keeps only this repository's local facts.

The navigation layer may lag behind the live code. If this file and the source disagree, trust the source.

## Repo layout

| Path | Contents |
|---|---|
| `tgui/packages/tgui/interfaces/` | All in-game UI components — one file per interface |
| `tgui/packages/tgui/components/` | Reusable building blocks (Button, Section, LabeledList, …) |
| `tgui/packages/tgui/layouts/` | Root window wrappers (Window, etc.) |
| `tgui/packages/tgui/routes.ts` | Auto-routes component name → file |
| `tgui/packages/tgui/styles/` | SCSS: `atomic/` (utility), `interfaces/` (per-UI), `themes/` |
| `tgui/packages/common/` | Shared helpers across packages |
| `tgui/packages/tgui/index.ts` | App entry point; theme registration |

Interface filename must match the string passed to `new /datum/tgui(user, src, "MyThing")` → `tgui/packages/tgui/interfaces/MyThing.tsx`.

## Multilingual RMH interfaces (fork-specific)

- One shared implementation: `tgui/packages/tgui/interfaces/MyThingView.tsx`.
- Thin route wrappers per language: `MyThing.tsx` (EN locale) and `MyThingRu.tsx` (RU locale) both render `MyThingView`.
- DM side picks the interface name before opening: `get_preferred_ui_language(user) == "ru" ? "MyThingRu" : "MyThing"`. The setting lives on `client.preferred_ui_language`; changed by `modular_rmh/code/modules/client/preferred_language.dm`.

## Build and dev workflow (local commands)

Always run a full build before submitting a PR — same checks as CI, faster locally:

```
bun tgui:build        # production build + full CI checks
bun tgui:dev          # dev server with hot reload
bun tgui:dev --reload # reload BYOND cache once
bun tgui:lint         # lint + auto-fix
bun tgui:tsc          # TypeScript type check
bun tgui:test         # unit tests (Jest)
bun tgui:clean        # fix cryptic webpack-cache errors, then rebuild
```

- Dev server won't attach? Open a TGUI window in-game first, then start the server; F5 to refresh.
- Browser DevTools: in-game → Debug tab → "Allow Browser Inspection" → F12.
- Dev-only tools: `F12`/green bug → KitchenSink playground; `F11` → Layout Debugger; `--debug` flag prints render timing (keep re-renders under 16 ms).

## Testing

Jest unit tests as `.test.ts`/`.spec.ts` alongside the tested file. No UI integration tests yet — test pure logic functions.

## Chat embedded components

TGUI components embed in chat via HTML data attributes: `data-component` must be whitelisted in `TGUI_CHAT_COMPONENTS` (`tgui-panel/chat/renderer.js`); `data-*` props map per `TGUI_CHAT_ATTRIBUTES_TO_PROPS`; booleans encode as `"$true"`/`"$false"`.

## Custom HTML popups

`/datum/tgui_window` exists for non-standard popups (stat panel, chat, background music) that need BYOND skin API access without a full TGUI interface — find current usage examples by grepping `tgui_window` before adding one.

*Cross-references: → `coding_standards.md` (repo conventions), → `signal_map.md`, → the ss13-tgui skill for everything framework-level.*
