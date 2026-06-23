# Runtime and Platform Triage

Read this before code-level performance review when the symptom is "white screen", "blank TGUI", "all popups blank", "TGUI does not load", "menus are huge/tiny", Wine/Linux issues, WebView2/IE trouble, `skin.dmf`, or broad BYOND browser-window breakage.

## Contents

- Classify the symptom first
- Client/runtime checks
- Repo/build/skin checks
- When to return to TGUI code review
- Community evidence to remember

## Classify the symptom first

Do not start by optimizing React render or `ui_data()` when the report is a blank browser window. Separate these cases:

- **All browser windows/loading screens are white or blank** - likely client/runtime: BYOND browser engine, WebView2/IE, DPI scaling, Wine/Linux, cache, antivirus/disk blocking, or graphics/runtime configuration.
- **Only one interface is blank while others work** - check route registration, frontend bundle, runtime JS errors, asset delivery, `ui_assets()`, `config.window`, and local wrapper/theme.
- **A BYOND map/camera/control inside TGUI is blank or misplaced** - use `references/byond-ui-and-devserver.md`; likely `ByondUi`, `winset`, `config.window`, control id/type, size, clipping, scroll, or backing DM setup.
- **First open is slow but later actions are smooth** - likely framework/WebView/asset transfer. Do not treat this as per-click payload cost.
- **Every click/update is slow after the window is loaded** - return to `references/performance-and-lifecycle.md`.

## Client/runtime checks

Ask for or inspect the environment before changing code:

- BYOND version: 515/older used the IE/Trident path; 516 uses WebView2. WebView2 must exist separately from Edge in some installs.
- OS and compatibility: Windows DPI scaling, Dreamseeker compatibility mode, "System (Enhanced)" DPI overrides, high-DPI monitor scaling, and per-monitor scaling can cause blank/oversized/odd windows.
- Wine/Linux: older 514/515 Wine paths often fail newer TGUI because IE11 is incomplete; 516/WebView2 changes the failure mode and depends on the Wine/Proton/Lutris setup.
- Client cache/resources: clearing cache or reconnecting can change symptoms; weird windows while resources download after joining an active round may be normal transient behavior.
- Antivirus/disk blocking: old embedded-browser white-window reports were tied to disk-access delays; check whether BYOND/Dreamseeker, the BYOND install directory, and user BYOND data/cache paths are being blocked.
- Graphics/runtime: if symptoms include graphical corruption outside browser windows, treat DirectX/GPU/runtime configuration as separate from TGUI.

## Repo/build/skin checks

If the symptom is reproducible for developers or on a test server, check the repo/runtime setup:

- TGUI bundle built and present. Missing `tgui.bundle.js` / public chunks is a build pipeline problem, not an interface implementation problem.
- Dev server/cache reload follows the repo's documented order; do not run build/watch commands unless the user approved checks.
- `skin.dmf` is included and actually compiled/loaded by the build path. A build wrapper can silently produce a DMB without the expected skin.
- Runtime `winset`/theme/window code does not mutate controls that are absent from the compiled skin. BYOND may create detached/misparented controls when code writes to missing ids.
- Local skin cache can differ from the current skin. Repro with a clean client/cache before blaming TGUI.

## When to return to TGUI code review

Move back to normal `ss13-tgui` review only after platform symptoms are ruled out or the failure is isolated to one interface. Then inspect:

- local route registration and interface key;
- frontend runtime errors and import paths;
- `ui_interact` standard open path;
- asset registration and delivery;
- static/dynamic data split and explicit static refreshes;
- `ByondUi` bridge details for embedded controls.

For performance complaints, require a specific timing shape: first-open delay, per-click delay, static refresh cost, hover/click preview cost, or bundle/build failure. Each has a different fix.

## Community evidence to remember

- BYOND forum reports for blank TGUI/WebView2/DPI often resolve outside the codebase: installing WebView2, changing Dreamseeker DPI compatibility, or fixing monitor scaling.
- Older white-window reports around SS13 popups often pointed at embedded IE/client cache/disk-blocking behavior, not a broken individual UI.
- Linux/Wine reports are usually browser-engine compatibility problems first; do not blame TGUI code without a Windows/native repro or interface-specific failure.
- `skin.dmf`/`winset` issues can masquerade as TGUI breakage. If TGUI works but mainwindow/verb panels detach or inputs stop, inspect skin build/loading and runtime window mutation.

## Source anchors

Use these as starting points for fresh verification; do not treat old posts as version-stable truth:

- BYOND 516/WebView2/DPI blank-window reports: `https://www.byond.com/forum/post/2968096`, `https://www.byond.com/forum/post/2967934`, `https://www.byond.com/forum/post/2966737`
- Older embedded-browser white-window report: `https://www.byond.com/forum/post/2286804`
- `skin.dmf`/runtime window-control failure mode: `https://www.byond.com/forum/post/2916260`
- Linux/Wine BYOND/TGUI context: `https://lutris.net/games/byond/`, `https://www.reddit.com/r/SS13/comments/1hiiy6m/516_beta_new_era_for_linux/`
- Community blank-window examples: `https://forums.beestation13.com/t/windows-dont-work/2031`, `https://github.com/tgstation/tgstation/issues/31745`
