# Case Study: An Over-engineered TGUI Redesign

This anonymized case study distills reusable lessons from a reviewed TGUI redesign. It is an aid for recognizing classes of mistakes, not a prescription for one interface or codebase.

## 1. Custom duplicate-window prevention

- **Assumption:** TGUI may open duplicate copies, so the implementation must scan open UIs and close extras.
- **Why it looked reasonable:** a duplicate had been observed through an abnormal open path.
- **Why it was wrong:** `SStgui.try_update_ui(user, src, ui)` already finds the UI for `(user, src)` and refreshes it. A scanner masks the broken open path.
- **Framework-native fix:** delete the helper and rely on `try_update_ui`.
- **General rule:** never hand-roll window deduplication. If duplicates appear, diagnose the open path.

## 2. Storing a long-lived `datum/tgui`

- **Assumption:** the domain datum needs a UI handle for later updates or closure.
- **Why it was wrong:** open UIs already live in `src.open_uis`; a stored reference can go stale and updates only the one viewer it points at.
- **Framework-native fix:** remove the reference and route updates through `SStgui.update_uis(src)`.
- **General rule:** gameplay datums should not own TGUI lifecycle references.

## 3. Disabling autoupdate with a custom update wrapper

- **Assumption:** manual updates require a wrapper that finds a tracked UI and pushes to it.
- **Why it was wrong:** truthy `ui_act` returns already update viewers. External state changes need only `SStgui.update_uis(src)` at the mutation site.
- **Framework-native fix:** delete the wrapper and call the subsystem directly.
- **General rule:** turning autoupdate off can be valid, but the manual path should remain small and complete.

## 4. Generation counter and per-user dynamic cache

- **Assumption:** cache the dynamic payload and resend only after a generation counter changes.
- **Why it was wrong:** updates were already on-demand, and a counter did not describe whether the payload content changed. The bookkeeping added stale-data risks without measured benefit.
- **Framework-native fix:** remove the dynamic cache and counter.
- **General rule:** measure first. If dynamic caching is justified, key it on meaningful serialized state rather than a vague update count.

## 5. Trivial cache versus useful shared cache

- Caching a tiny pure operation over a small static set added complexity with negligible savings.
- A cache of shared, immutable, same-for-everyone metadata was defensible because it avoided rebuilding a genuinely stable payload.
- **General rule:** classify a proposed cache by ownership and mutability. Shared immutable data may justify a global cache; trivial operations and per-user dynamic state usually do not.

## 6. Backend sending presentation

- The backend emitted layout anchors and display labels that could be derived from existing domain fields.
- This coupled DM to the current visual design and duplicated mappings that could drift from canonical definitions.
- **Framework-native fix:** send domain values and derive presentation in TypeScript.
- **General rule:** layout classes and display composition belong in the frontend. An asset-pipeline handle is a possible exception when it represents a sprite key rather than layout.

## 7. Raw HTML instead of components

- Plain `section`, `button`, heading, and wrapper tags bypassed the component system.
- Replacing them with `Button`, `Box`, `Section`, `Stack`, and `Window` restored shared spacing, theming, scaling, and interaction behavior.
- **General rule:** framework components are the default; raw tags are a deliberate exception for content they do not model.

## 8. Excessive SCSS and absolute layout

- A thousand-plus-line stylesheet reimplemented layout already available through TGUI components and relied heavily on absolute pixel measurements.
- **Framework-native fix:** adopt component layout primitives, reuse the codebase's shared theme base, and remove bespoke scaling controls when a standard scaling mechanism exists.
- **General rule:** keep interface SCSS proportional to the remaining visual requirements after components do their work.

## 9. Displaying a parallel gameplay calculation

- The UI showed a derived value computed differently from the value used by gameplay systems.
- The presentation also implied a current/base relationship that did not match modifier semantics.
- **Framework-native fix:** locate and display the canonical calculation used by the game; show breakdowns only where their meaning is accurate.
- **General rule:** a UI must not invent an alternate gameplay truth.

## Cross-cutting takeaways

- The recurring failure mode was rebuilding framework capabilities: lifecycle tracking, deduplication, update fan-out, caching, layout, and scaling.
- The recurring fix was deletion plus a small framework-native call or component.
- Patterns that remained useful included splitting heavy static data from dynamic data, caching genuinely shared immutable metadata, using efficient domain lookups for actions, and delivering icons through the asset pipeline.
