# tgui Components & Styling

Read this when writing or reviewing the React/SCSS side of an interface.

## Contents
- Two component architectures (tgui-core vs in-tree)
- Choosing an element: semantics first, then components
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

## Choosing an element: semantics first, then components

Start from what the element *is*, not from what tag it currently uses. Ask: is this a user action? a titled panel? a layout block? inline styled text? semantic prose? Then pick the construct whose **behavioral contract** matches:

| The element is... | Use |
| --- | --- |
| a user action (click does something) | `Button` (or `Button.Checkbox`, `Button.Confirm`, ...) |
| a standard titled panel, possibly with header actions | `Section` with `title` / `buttons` |
| a block-level layout/style wrapper | `Box` (renders a `<div>`) |
| inline styled text with no specialized component | `Box as="span"` |
| manual flexbox | `Stack` / `Stack.Item` |
| semantic prose or a tag needing typed native attributes or a wrapper's ref contract | raw HTML (`<p>`, `<strong>`, `<h3>`, `<button>`, SVG) — with a comment when non-obvious |
| unclear | read the component's implementation and 2-3 neighboring interfaces first |

**The anti-pattern this section exists to prevent: mechanical find/replace of HTML tags with `Box as="<tag>"`.** That swap satisfies the letter of "use components" while losing every contract that matters. In ~700 tgstation interfaces, `as="span"` appears dozens of times but `as="button"`, `as="header"`, `as="section"`, `as="strong"`, `as="h3"` appear **zero** times — the ecosystem treats `as` as an inline-text tool, not a tag-preserving wrapper.

### What each component actually is (verify in *your* fork's source)

- **`Box`** is a CSS-utility primitive: it maps style props (`m`, `p`, `color`, `bold`, ...) onto one DOM element, a `<div>` by default. In tgui-core its public type accepts style props and event handlers — **not** `aria-*`, `title`, `type`, or `ref`. So `Box as="button"` produces an untyped pseudo-button: you can no longer (type-safely) restore `type="button"`, `aria-label`, or `title`, and you get none of `Button`'s behavior. Use `Box` when the element's only job is layout/decoration; use `as` only when the *tag itself* must differ for inline flow (`as="span"`) — not to mirror whatever tag the old markup used.
- **`Button`** is behavior, not just chrome. In tgui-core it renders a focusable element with keyboard activation (Space/Enter), `disabled`/`selected` states, icon and ellipsis support, and a built-in `tooltip` prop. A bespoke-looking action should usually still be a `Button` with a `className` whose SCSS overrides the `.Button` chrome (interface styles load after component styles, so equal-specificity overrides win) — *not* a `Box as="button"` that silently re-implements half of this. Note the flip side: in tgui-core `Button` is a styled `div`, so a raw `<button type="button">` can be the *more* accessible choice when you need true native semantics under a fully bespoke skin.
- **`Section`** generates a fixed DOM you must work with, not against: `.Section__title > .Section__titleText + .Section__buttons`, then `.Section__rest > .Section__content`. `title` and `buttons` accept ReactNode; `fill`/`scrollable` handle the common layouts. Use it for standard titled panels. For a heavily art-directed panel, adopting `Section` means restyling its generated wrappers in scoped SCSS (precedent: ListInput restyles `.Section__title` under its own class) — do that when the title/buttons machinery genuinely replaces markup you'd otherwise hand-roll. Do **not** force `Section` onto a design whose DOM, scroll structure, or sticky elements it would break; a `Box` is honest there.
- **Wrappers like `Tooltip`** clone their child and inject a ref plus hover handlers; the child must land that ref on a real DOM node. Native tags always satisfy this. Components satisfy it only if they forward/pass through `ref` — check the implementation (and the wrapper's own docs example) instead of assuming. When a `Tooltip` child must stay a raw `<button>` for this reason, say so in a comment.

### What a careless swap silently loses

`type="button"`, `aria-label`/`aria-hidden`/`title`, native keyboard focus and activation, `:focus`/`:disabled` styling, SCSS element selectors (`.Foo strong { ... }` stops matching when `<strong>` becomes a `<div>`), and test/tutorial selectors. If a replacement drops any of these, it is a regression even when the pixels look identical.

### Raw HTML is a deliberate exception — but a real one

Prefer the framework primitives: they carry spacing, theming, scaling, and consistency with sibling interfaces. Reach for raw tags only with a concrete technical reason, and keep them rare:
- semantic text where the tag *is* the point (`<p>`, `<strong>`, `<h3>` in prose-like content);
- native attributes or behavior the local component types don't expose (`title`, `aria-*`, `type`, form semantics);
- a wrapper's ref contract plus a bespoke skin that component chrome would fight;
- content with no component model (inline SVG, sanitized free-form HTML).

A review should flag raw tags doing what `Button`/`Section`/`Stack` already do — and equally flag `Box as="..."` doing what raw HTML or a specialized component does better.

### Is the abstraction paying rent?

A specialized component earns its place by *deleting* code: CSS you no longer write, keyboard/focus behavior you no longer re-implement, accessibility you get for free. If adopting a component means neutralizing most of its chrome **and** using none of its behavior, it isn't paying — keep the simpler construct. Conversely, if your `Box as="button"` needs onClick, hover styling, focus handling, and a tooltip, you are rebuilding `Button` by hand — switch to it.

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
