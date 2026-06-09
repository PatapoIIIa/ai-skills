# tgui Components & Styling

Read this when writing or reviewing the React/SCSS side of an interface.

## Contents
- Two component architectures (tgui-core vs in-tree)
- Use components, raw HTML as a rare exception
- The typed data contract
- useBackend / act
- SCSS: scoped, minimal, consistent
- Scaling and absolute pixels
- Theming alignment

## Two component architectures (know which you are in)

The component *vocabulary* is the same everywhere, but it ships two ways:

- **tgui-core forks** (tgstation, Vanderlin, BandaStation): components are an npm dependency, imported from `tgui-core/components`. There is no in-tree component library to edit; styling/scaling/theming live in tgui-core. This is modern /tg/.
- **In-tree ports** (cmss13, and older Azure-derived code): components live in the repo at `tgui/components` (e.g. `Box.tsx`, `Button.tsx`, ...) and are imported from `tgui/components`. There is no `tgui-core` dependency, and component styles live in the codebase — so per-component style edits are a real thing here, unlike in tgui-core forks.

This is exactly what the Great Developer described in review: "azure's tgui port is older... they still have component styles in the codebase while we use tgui-core." **Match the local convention** — grep a neighbor's import line before writing one. The rest of this file assumes you have done that and uses the shared component names.

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

## SCSS: scoped, minimal, consistent

- Scope styles to the interface's root class; keep them minimal.
- Reuse existing interface styles and variables rather than re-declaring colors and spacing.
- A large hand-written stylesheet is a warning sign. The PR #6578 sheet hit ~1100 lines and was flagged as reading "AI gen" with "a lot of redundancy and rewriting of stuff tgui already does." Shrinking it by adopting `Stack`/`Section`/`Box` is usually the right move — most of those lines re-implement layout the components already provide.
- When a codebase has a shared "paper"/theme stylesheet, build on it instead of inventing a parallel palette. (Vanderlin points new paper/guidebook-style interfaces at `RecipeBook.scss` as the base; borrow its variables, override only what you must — ideally it becomes its own theme.)

## Scaling and absolute pixels

- Avoid absolute pixel measurements for layout; they fight TGUI's scaling and responsive conventions ("lots of absolute pixel measurements which also goes against tgui design"). Prefer flex/`Stack`, relative units, and component spacing props.
- Do **not** add a custom scaling control if the codebase already exposes a UI-scaling variable that works with TGUI. Reuse the existing mechanism rather than shipping a bespoke zoom.

## Theming alignment

TGUI theming is generally a global override of the base themes and works automatically *when interfaces are implemented properly* (i.e. using the framework components and not overriding everything by hand). Note that in tgui-core forks the active theme is **not** freely switchable by a global setting — the "light" theme is often just a stub so settings work without disabling things — so do not design an interface that depends on a user toggling themes. Custom per-interface theming is what breaks consistency; the more you lean on the shared system, the more theme-compatible the result. This skill's focus is technical correctness; defer to the codebase owners on final visual direction, but prefer the shared base over a one-off.
