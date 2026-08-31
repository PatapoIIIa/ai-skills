# Refactor Timeline: Bespoke Machinery to Framework-native TGUI

This anonymized progression shows how an over-engineered interface can be simplified in stages. The sequence matters because backend lifecycle corrections are usually cheaper and lower-risk than a large frontend rewrite.

## Stage A: Initial custom redesign

The first version combined a bespoke visual layout with custom lifecycle and performance machinery:

- large hand-written SCSS and absolute positioning;
- raw HTML for controls and layout;
- backend-generated presentation fields;
- a stored UI reference and duplicate-window scanner;
- disabled autoupdate with a custom push wrapper;
- a generation-counter cache for dynamic data.

The common assumption was that a custom visual design also required custom framework infrastructure.

## Stage B: Separate first-load delay from update cost

A slow first open was initially attributed to payload or render work. Investigation separated two classes of delay:

- baseline first-load cost from BYOND/WebView communication and asset transfer;
- genuine per-click or per-update cost from interface data and rendering.

The interface was not rewritten to solve a transport-layer baseline. A separate asset-path fault, when present, belonged in the asset subsystem.

## Stage C: Remove lifecycle and caching machinery

The backend cleanup proceeded in small deletions:

- remove custom duplicate-window scanning and rely on `try_update_ui`;
- remove the stored `datum/tgui` reference;
- replace a tracked-UI update wrapper with `SStgui.update_uis(src)` at external mutation sites;
- remove the generation counter and per-user dynamic cache;
- remove caching around trivial transformations.

Autoupdate could remain disabled because click-driven updates and explicit external-change pushes formed a complete standard update path.

## Stage D: Restore the data/presentation boundary

Layout anchors and composed labels were removed from the DM payload when they could be derived from existing fields in TypeScript. The displayed gameplay number was changed to use the same canonical calculation as the game rather than a UI-only approximation.

The result was a smaller contract with less duplicated meaning.

## Stage E: Adopt components and shared styling

The remaining work moved to the frontend:

- replace raw controls and wrappers with TGUI components;
- split the large interface into focused components;
- delete SCSS that duplicated `Stack`, `Section`, `Box`, and shared theme behavior;
- replace absolute measurements with component layout and relative sizing;
- reuse the codebase's existing theme and scaling mechanisms.

## Pacing lesson

Backend lifecycle cleanup is often fast because it removes helpers and substitutes standard calls. Frontend component and SCSS cleanup is slower because it changes structure and visual behavior. Review and implementation plans should budget for those phases separately.

## Throughline

For every helper, cache, counter, window tracker, or scaling control, ask which local TGUI mechanism it duplicates. If the framework already owns the behavior, deletion is usually the safer refactor.
