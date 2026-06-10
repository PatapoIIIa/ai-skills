# tgui Components & Styling

Read this when writing or reviewing the React/SCSS side of an interface.

## Contents
- Two component architectures (tgui-core vs in-tree)
- Use components, raw HTML as a rare exception
- The typed data contract
- useBackend / act
- Component boundaries
- React state: local, shared, and derived
- Testable frontend logic
- SCSS: scoped, minimal, consistent
- Scaling and absolute pixels
- Theming alignment

## Two component architectures (know which you are in)

The component *vocabulary* is the same everywhere, but it ships two ways:

- **tgui-core forks** (tgstation, Vanderlin, BandaStation): components are an npm dependency, imported from `tgui-core/components`. There is no in-tree component library to edit; styling/scaling/theming live in tgui-core. This is modern /tg/.
- **In-tree ports** (cmss13, and older Azure-derived code): components live in the repo at `tgui/components` (e.g. `Box.tsx`, `Button.tsx`, ...) and are imported from `tgui/components`. There is no `tgui-core` dependency, and component styles live in the codebase — so per-component style edits are a real thing here, unlike in tgui-core forks.

Older ports may still keep component styles in-tree while modern forks consume `tgui-core`. **Match the local convention** — grep a neighbor's import line before writing one. The rest of this file assumes you have done that and uses the shared component names.

## Use components, raw HTML as a rare exception

Prefer the framework primitives over raw HTML tags:

| Instead of | Use |
| --- | --- |
| `<div>` / `<span>` | `Box` |
| `<button>` | `Button` |
| a titled block / `<h3>` + wrapper | `Section` |
| manual flexbox via `<div>` | `Stack` (and `Stack.Item`) |
| the window shell | `Window` (+ `Window.Content`) |

Why it matters beyond style: these components carry the framework's spacing, theming hooks, scaling behavior, and consistency. Hand-rolled `section`/`button`/`h3`/`div` opt out of all of that, so they drift from sibling interfaces and ignore the theme/scale system.

Raw tags are not *forbidden* — they are a **deliberate exception, not the default**. Only ~6% of tgstation interfaces use a raw `<div>`, and where they do it is for free-form content a component does not model well (e.g. rendering arbitrary text lines). If you reach for a raw tag, it should be because no component fits, not because raw HTML is more familiar. A review that finds raw tags doing what `Button`/`Box`/`Section`/`Stack` already do should flag them.

## The typed data contract

The standard frontend idiom across tgui-core forks and cmss13 alike:

```tsx
type Data = {
  valveOpen: BooleanLike;   // DM booleans -> BooleanLike, not boolean
  releasePressure: number;
  holdingTank: { name: string; tankPressure: number };
};

export const Thing = (props) => {
  const { act, data } = useBackend<Data>();
  const { valveOpen, releasePressure } = data;
  return <Window>...</Window>;
};
```

Typing `Data` documents the backend contract, catches missing-field bugs, and makes "is this field presentation or data?" obvious. Use `BooleanLike` (from `tgui-core/react` or the local equivalent) for values that arrive as DM `TRUE`/`FALSE`.

## useBackend / act

Use the project's established `useBackend()` and `act(...)` style. Read `data`, call `act('verb', { ... })`. Keep the component reading data and dispatching actions; don't smuggle gameplay logic into the frontend.

## Component boundaries

When an interface grows, split it into focused components with explicit typed props. Keep each component responsible for one section, repeated row, modal, or detail view rather than allowing a single render function to accumulate hundreds of lines.

Prefer passing already-selected domain data into presentational children. Repeating `useBackend()` in every child is valid when the local codebase uses that pattern or the child genuinely needs `act`, but it can hide dependencies and make extraction/testing harder. Follow neighboring modern interfaces rather than old examples that require a `context` argument.

## React state: local, shared, and derived

- In modern TGUI v5, use React's `useState` and `useEffect` for genuine local interaction or asynchronous lifecycle work.
- Treat `useLocalState` as deprecated unless the current fork still requires it. Do not migrate an older fork blindly; verify its TGUI generation first.
- Use `useSharedState` only when UI-local input is intentionally shared by everyone viewing the same in-character machine or object. Do not use it as a general replacement for local state or authoritative DM state.
- Do not mirror backend data, props, or another state value into extra state. Compute derived values directly during render.
- Do not add an effect merely to keep one state variable synchronized with another. If `isEven` is `count % 2 === 0`, it is a variable, not state.
- Keep authoritative gameplay state in DM. React state may control presentation such as tabs, filters, expanded rows, drafts, or transient animation, but must not become the security or game-state source of truth.

## Testable frontend logic

Extract non-trivial pure transforms from JSX when they encode meaningful behavior: filtering/sorting payloads, grouping records, formatting derived labels, or mapping backend state to a view model. These functions can receive focused `.test.ts`/`.spec.ts` coverage when the repository's test setup supports it.

Do not add tests for trivial markup or restate TypeScript's type checks. UI integration support varies by fork, so copy the local test runner and conventions rather than assuming `/tg/`'s current Jest setup exists everywhere.

## SCSS: scoped, minimal, consistent

- Scope styles to the interface's root class; keep them minimal.
- Reuse existing interface styles and variables rather than re-declaring colors and spacing.
- A large hand-written stylesheet is a warning sign. One reviewed redesign exceeded a thousand lines of SCSS, largely reimplementing layout already provided by TGUI. Shrinking it by adopting `Stack`/`Section`/`Box` is usually the right move.
- When a codebase has a shared "paper"/theme stylesheet, build on it instead of inventing a parallel palette. Borrow its variables and override only what the interface actually needs.

## Scaling and absolute pixels

- Avoid absolute pixel measurements for layout; they fight TGUI's scaling and responsive conventions ("lots of absolute pixel measurements which also goes against tgui design"). Prefer flex/`Stack`, relative units, and component spacing props.
- Do **not** add a custom scaling control if the codebase already exposes a UI-scaling variable that works with TGUI. Reuse the existing mechanism rather than shipping a bespoke zoom.

## Theming alignment

TGUI theming is generally a global override of the base themes and works automatically *when interfaces are implemented properly* (i.e. using the framework components and not overriding everything by hand). Note that in tgui-core forks the active theme is **not** freely switchable by a global setting — the "light" theme is often just a stub so settings work without disabling things — so do not design an interface that depends on a user toggling themes. Custom per-interface theming is what breaks consistency; the more you lean on the shared system, the more theme-compatible the result. This skill's focus is technical correctness; defer to the codebase owners on final visual direction, but prefer the shared base over a one-off.
