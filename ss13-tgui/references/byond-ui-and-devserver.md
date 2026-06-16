# ByondUi, BYOND Bridge, and Legacy TGUI Dev Workflow

Read this when a task mentions `ByondUi`, embedded maps/camera controls, `winset`, `winget`, `callByond`, `config.window`, `config.ref`, old in-tree tgui routing, or the tgui dev server.

This reference is based on old in-tree `/tg/` tgui (`packages/tgui/...`) and is version-sensitive. Verify the equivalent files in the current repo first. Modern tgui-core forks may move, rename, or remove these APIs.

## Activation boundary

Use this material only for browser UI bridge work. Do not apply it to ordinary SS13 DM systems, items, mobs, icons, balance, admin verbs, mapping, databases, or generic BYOND code unless the request also touches tgui or browser/BYOND UI integration.

## What ByondUi is

`ByondUi` displays a real BYOND skin control on top of the browser window and uses the browser layout engine only to decide where that control belongs. The React element is a positioning anchor; the visible control is still BYOND-owned.

Old in-tree `/tg/` mechanics:

- `ByondUi` allocates an id (`params.id` or an auto-generated `byondui_N`).
- On mount/update, it reads `getBoundingClientRect()` from its DOM container.
- It calls `callByond('winset', { ...params, id, pos: 'x,y', size: 'wxh' })`.
- On unmount and `beforeunload`, it clears the BYOND control by setting `parent: ''`.
- It ignores very old Trident/IE engines (`tridentVersion <= 4` in the sampled source).
- It supports normal `Box` layout props, because the DOM container is still a tgui element.

Use it for actual BYOND controls such as an embedded map/camera view. Do not use it for ordinary buttons, inputs, panels, or layout; use normal tgui components for those.

## Correct usage shape

Use the local component import path. In old in-tree tgui this was:

```jsx
import { ByondUi } from '../components';
```

Camera-console style usage:

```jsx
const { data, config } = useBackend(props);

<ByondUi
  className="CameraConsole__map"
  params={{
    id: data.mapRef,
    parent: config.window,
    type: 'map',
  }} />
```

Rules:

- Pass `parent: config.window`; this attaches the BYOND control to the active tgui window.
- Pass the BYOND skin control `type` (`map`, `button`, etc.) and any other skin params required by the repo's BYOND control setup.
- Use a stable backend-provided `id` when DM or another control must refer to the same control. Auto-generated ids are fine only for throwaway controls that no backend code addresses.
- Keep the container visible and nonzero-sized. If the source only updates on render and debounced window resize, avoid placing the control in a scrolling or constantly reflowing region unless the local implementation explicitly handles scroll/reposition.
- Keep gameplay mutations on the normal `act()` -> `ui_act` path. Use raw `winset`/`winget`/`callByond` for BYOND window/control properties and framework bridge code, not as a replacement for backend action validation.

## Debug checklist for blank or misplaced controls

Check these before rewriting the UI:

- The frontend route is registered and the component is actually rendered.
- `config.window` is present and matches the current tgui window.
- `params.id` is unique, stable when needed, and matches any DM-side map/control ref.
- The DOM container has nonzero width/height and is not clipped by wrapper/scroll CSS.
- The BYOND control `type` and params are valid for the local skin params.
- The backing DM code creates or selects the map/control target expected by the frontend.
- The local `ByondUi` implementation updates position on the events your layout needs; old code handles render/update and debounced resize, not arbitrary scrolling.
- Browser/engine support is adequate for the local implementation.

## Routes in old in-tree tgui

Old in-tree tgui has a central `routes.js`. New interface work needs both:

- An import from `./interfaces/InterfaceName`.
- A `ROUTES` entry keyed by the DM interface name.

Example:

```js
import { SampleInterface } from './interfaces/SampleInterface';

const ROUTES = {
  sample_interface: {
    component: () => SampleInterface,
    scrollable: true,
  },
};
```

Route entries may also set a wrapper and theme. Copy neighboring interfaces. If the key does not match the DM interface name, the layout falls back to a missing-route message instead of rendering the interface.

## Bridge helpers

Old in-tree tgui bridge helpers:

- `callByond(path, params)` builds a `byond://...` URL and assigns `location.href`.
- `callByondAsync(url, params)` adds a BYJAX callback and returns a promise.
- `act(src, action, params)` calls the backend `ui_act` endpoint for the current UI ref.
- `winget(win, key)` and `winset(win, key, value)` read and write BYOND window/control properties.
- `runCommand(command)` sends a BYOND command via `winset`.

Keep the distinction clear: `act` is for validated gameplay/UI actions; `winset`/`winget` are for window/control plumbing.

## Dev-server workflow

Old `/tg/` tgui README documents two equivalent paths:

- `bin/tgui --dev` for the dev server with incremental compilation, hot module replacement, and client logging.
- `yarn run watch` or the batch file wrapper for Windows users.

The documented order is: start the game server, connect, wait until the world is loaded and the client is out of the lobby, then start the tgui dev server. A good connection dumps data to the dev-server log when tgui windows open. Useful options include `--reload` for a one-time BYOND cache reload, `--debug` for debug logging, and `--no-hot` to disable HMR.

Do not assume these commands are safe in every workspace. Follow the repo's user/agent policy before running build, lint, watch, dev-server, cache reload, or bundle-analysis commands.

## Sources to inspect

- `tgui/README.md` for usage, dev-server, routing, component reference, and `ByondUi` examples.
- `tgui/packages/tgui/components/ByondUi.js` for `winset`, id allocation, bounding-box positioning, resize, and cleanup mechanics.
- `tgui/packages/tgui/byond.js` for `callByond`, `act`, `winget`, and `winset`.
- `tgui/packages/tgui/interfaces/CameraConsole.js` for real `ByondUi` map usage.
- `tgui/packages/tgui/routes.js` and `layout.js` for route keys, wrappers, themes, scrollability, and missing-route behavior.
