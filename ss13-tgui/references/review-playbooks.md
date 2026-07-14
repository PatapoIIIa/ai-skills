# TGUI Review Playbooks

Use this file when the request is broad: "review this TGUI", "find bad practices", "make it faster", "simplify this interface", or "is this idiomatic?" Pick the smallest playbook that matches the task, then read the more specific reference file it names.

## Contents

- Universal review order
- Runtime/platform triage
- Performance review
- Lifecycle/backend review
- Frontend/components review
- Appearance picker review
- BYOND control/devserver review
- Refactor review
- Output format

## Universal review order

1. Identify the local TGUI generation: backend proc name, component import path, route registration, `ui_assets()` pattern, and neighboring interface style.
2. Classify the task: implementation, review, runtime/platform, performance, frontend cleanup, BYOND control, or appearance picker.
3. Search before judging. Use `scripts/tgui_smell_scan.py` when available, then follow with targeted `rg` for the exact proc/component names in the changed files.
4. Separate correctness from taste. Flag bugs, lifecycle breakage, stale data, payload/perf risk, accessibility/native-contract loss, and unbounded complexity before style nits.
5. Prefer deleting redundant machinery over adding wrappers, trackers, caches, or new lifecycle concepts.

## Runtime/platform triage

Read `references/runtime-platform-triage.md`.

Prioritize:

- all browser windows/loading screens white vs one interface blank;
- BYOND 515/516 browser engine path and WebView2/IE runtime;
- DPI/compatibility mode, Wine/Linux, cache/resource download, antivirus/disk blocking;
- `skin.dmf` compiled/loaded and runtime `winset` not writing missing controls;
- only returning to code-level TGUI review after platform symptoms are ruled out.

Good outcome: the agent does not rewrite payload/render code for a client/runtime blank-window failure.

## Performance review

Read `references/performance-and-lifecycle.md`.

Prioritize:

- first-load vs per-update diagnosis;
- `ui_static_data()` size and refresh frequency;
- `icon2base64()` and thumbnail generation in repeated catalogs, while allowing deliberate one-off/dynamic snapshots;
- repeated `update_static_data_for_all_viewers()` calls that should be batched;
- huge static graphs that may need id deduplication, not small lists dressed up with compression machinery;
- heavy BYOND icon/render work on hover/click paths;
- unjustified global/per-user caches;
- temporary loggers and timing counters left after measurement;
- `set_autoupdate(FALSE)` without complete update push sites.

Good outcome: static assets flow through `ui_assets()`/spritesheets, dynamic state stays in `ui_data()`, heavy previews are async and signature-cached, and measurement scaffolding is gone.

## Lifecycle/backend review

Read `references/tgui-workflow.md` and `references/performance-and-lifecycle.md`.

Prioritize:

- canonical `SStgui.try_update_ui(user, src, ui)` open path;
- no `if(SStgui.try_update_ui(...))` lookup predicate or double refresh;
- no stored long-lived `datum/tgui` refs;
- `ui_act()` calls parent first and validates client params;
- truthy `ui_act()` return or explicit `SStgui.update_uis(src)` at external mutation sites;
- `update_static_data()` only when static payload dependencies actually changed;
- no duplicate-window scanners or custom lifecycle wrappers.

Good outcome: the backend exposes data, uses framework lifecycle, and contains no UI bookkeeping outside normal TGUI hooks.

## Frontend/components review

Read `references/components-and-style.md`.

Prioritize:

- local import path and route/wrapper pattern;
- typed backend data shape;
- derived values computed from data instead of mirrored React state;
- `Button` for actions, `Section` for standard titled panels, `Stack`/`Box` for layout;
- raw HTML only for native semantics, attributes, or wrapper ref contracts;
- no mechanical `Box as="<tag>"` replacement;
- SCSS proportional to the task and not reimplementing framework layout.

Good outcome: the frontend is smaller because components replaced bespoke markup/SCSS where they carry behavior, not because tags were mechanically renamed.

## Appearance picker review

Read `references/performance-and-lifecycle.md` and the appearance picker section in `SKILL.md`.

Prioritize:

- option thumbnails delivered by spritesheet assets, not base64 strings;
- static catalog contains ids/classes/names, not generated image data;
- hover replacement previews show the candidate replacing current state, not stacking over it;
- heavy doll renders are async and keyed by a state signature;
- simple choices such as background modes remain enum values.

Good outcome: many-option pickers have tiny data payloads, stable asset keys, and no dead thumbnail/cache path.

Empty/blank preview triage (field-proven order — theorizing about icon pipelines loses to looking at pixels):

1. **Do not trust silent runtime logs until the channel is proven live.** Grep the fork's historical
   logs for ANY "runtime error" ever; some forks ship broken runtime logging, and "no errors" from a
   dead channel proves nothing.
2. **Isolate with a throwaway focused unit test** (`focus = TRUE`, compile `-DUNIT_TESTS`, run
   `dd <game>.dmb -close -trusted`, read `data/unit_tests.json`): call the exact preview proc on an
   allocated mob and `fcopy(flat, "data/probe_[tag].png")` so the actual pixels (content bbox) are
   inspectable; TEST_FAIL strings work as printf. Compare naked vs geared vs forced-dir variants —
   encoded LENGTH alone discriminates (a fully transparent PNG is ~100-300 base64 chars; a real
   render is 500+; content growing while length shrinks means the flatten is losing pixels).
3. **Known fingerprints:** renders naked / transparent while holding an item = the native
   `getFlatIcon` canvas-expansion transposition (SKILL.md picker pitfalls); broken `<img>` showing
   alt text = raw base64 missing its `data:image/png;base64,` prefix (`icon2base64` returns the bare
   string); client "Invalid argument" popup with clean server logs = `RenderIcon` output fed into a
   savefile-based helper (byond-client-api.md).

## BYOND control/devserver review

Read `references/byond-ui-and-devserver.md`.

Prioritize:

- `ByondUi` only for actual BYOND skin controls such as maps/cameras;
- stable `id`, `parent: config.window`, correct control `type`, and nonzero layout box;
- compiled/loaded `skin.dmf` contains the target controls before runtime code mutates them;
- runtime `winset`/theme/window code does not write to missing ids or detached controls;
- route registration and wrapper/theme in old in-tree tgui;
- raw `winset`/`winget` only for BYOND control properties, not normal UI actions;
- no scroll/resize traps that desync the BYOND control from its DOM anchor.

Good outcome: React positions the BYOND control; gameplay state still flows through TGUI actions.

## Refactor review

Read `references/case-study-overengineered-interface.md` and `references/refactor-timeline.md`.

Prioritize:

- custom lifecycle deletion;
- removal of generation counters and per-user dynamic caches unless measured and keyed by content;
- migration from bespoke layout to framework components where it reduces code;
- preserving local visual conventions and user workflows;
- refusing broad rewrites that do not reduce risk or complexity.

Good outcome: fewer concepts, fewer files, less SCSS, smaller payloads, and behavior still follows local framework norms.

## Output format

For code review, lead with findings ordered by severity. Include file/line references and explain the failure mode. Then list open questions and only then a short summary. If no serious issues are found, say that clearly and call out residual risks such as unrun tests or unverified runtime behavior.

For implementation, state the chosen local conventions before editing, keep changes scoped, and report checks that were run or skipped.
