---
name: "tgstation-modular-content"
description: "Use when adding or modifying SS13 content on a /tg/station-derived fork that regularly pulls upstream — new items, mobs, jobs, species, areas, maps, components, signals, traits, crafting, research, reagents, clothing, antagonists, or modular tgui — and the change must stay mergeable when upstream is re-synced. Strong triggers: 'add a modular X', 'without touching upstream', 'keep it mergeable', 'avoid merge conflicts on rebase', repos containing modular_skyrat / modular_zubbers / modular_abel / master_files folders, or BUBBER EDIT / SKYRAT EDIT style comments. Also use to review whether an existing change is properly modular. Do NOT use for PRs intended to be merged into upstream /tg/station itself, or for pure tgui framework/interface work with no modularity concern (use the ss13-tgui skill for that)."
---

# /tg/station Modular Content

Add and extend content on a downstream fork (Bubberstation, Skyrat, Vanderlin, or any codebase that rebases on /tg/station) **without editing upstream files**, so the fork keeps pulling upstream cleanly. The goal is content that lives in a modular folder and survives every upstream re-sync untouched.

## The one root cause

Almost every modularity failure shares a single root: **editing the upstream file when you could have re-opened the type from a modular file.** DM (DreamMaker) lets you re-open any type, proc, or var from *any* file — the compiler merges every declaration of `/obj/item/foo` across the whole codebase into one type. So adding a var, adding a subtype, or wrapping a proc almost never *requires* touching the file that originally defined the parent. Upstream edits are a merge-conflict liability forever; a modular file is invisible to the upstream diff.

Before you touch any file under `code/`, `_maps/` (upstream maps), `icons/`, `sound/`, or `tgui/.../interfaces/` that you did not create, stop and ask: **what modular seam re-opens this type instead?** That question prevents the entire class of problems this skill exists for.

## Activation guard

Use this skill when the work adds or changes gameplay content on a fork that tracks upstream /tg/ and the change must stay mergeable. If the task is a PR *into* upstream /tg/station, the modular rules are inverted — don't apply them. If it is pure tgui framework work, defer to the `ss13-tgui` skill. When unsure, check for a `modular_*` / `master_files` directory and an upstream-edit comment convention; their presence means this skill applies.

## Workflow — before writing a line

The *concepts* below are stable across /tg/ forks; the *folder names, include mechanism, and edit-tag wording are not.* Learn the local convention first — a pattern copied from another fork will not match here.

1. **Find the modular root.** List the repo top level. Look for `modular_<name>/` (Bubberstation: `modular_skyrat/`, `modular_zubbers/`; Vanderlin: `modular_abel/`). That folder, not `code/`, is where your work goes. If there is no modular root, see "When to stop."
2. **Find the override sub-layout.** Most forks split it two ways: a path-mirroring folder for *overrides/extensions of upstream types* (Bubberstation: `master_files/`, mirroring the upstream `code/...` path) and a self-contained-module folder for *net-new content* (`modules/<feature>/`). Read `references/bubberstation-patterns.md` for the exact layout.
3. **Read the fork's own handbook.** Open any `readme.md` / `module_template.md` / `CONTRIBUTING` inside the modular root and obey it — it overrides this skill on naming, tagging, and folder rules. Bubberstation's is `modular_zubbers/readme.md`.
4. **Learn how files get compiled in.** New `.dm` files do nothing until included. Find whether the fork adds `#include` lines to the main `.dme` (Bubberstation, between `// BEGIN_INCLUDE` / `// END_INCLUDE`) or to a per-module aggregator file that the `.dme` includes once (Vanderlin: `modular_abel/_module.dm`). CI usually *enforces* that every `.dm` is included — a new file that compiles locally can still fail the include check.
5. **Read 2–3 neighboring modules** of the same kind. Copy their folder shape, include style, edit-tag wording, and asset-path style. Local neighbors beat this skill.
6. **Decide the seam** using the decision matrix below, then implement.

## Don't-touch-upstream rules

- **Never edit a file you did not create** under `code/`, upstream `_maps/`, `icons/`, `sound/`, `interface/`, or the upstream `.dme` body — except the auto-managed include list, and even that follows the local mechanism.
- **Never edit upstream binary assets** (`.dmi`, `.ogg`, `.png`). Git cannot merge them; a conflict is unrecoverable. Ship your own asset in the module and reference it by full modular path.
- **Never edit upstream map files** (`_maps/**/*.dmm`). Use the modular map system (automapper / area-spawn). See the maps rule below.
- **Prefer to upstream a fix.** If the change is a generic bug or improvement with no fork-specific flavor, the right move is often a PR to upstream /tg/, not a modular patch. Say so.
- If editing upstream is genuinely unavoidable, that is a **stop-and-ask boundary** (see last section) — not something to do silently.

## Choosing the seam (decision matrix)

| You want to… | Modular seam | Edit upstream? |
|---|---|---|
| Add a brand-new item/mob/structure/reagent/recipe/design | New subtype in a self-contained `modules/<feature>/` folder | No |
| Add a var or a subtype to an existing upstream type | Re-open the type in a modular file (`/obj/item/existing\n\tvar/...`) | No |
| Run code before/after an existing proc | Re-open the proc in a modular file, call `. = ..()`, add your logic around it | No |
| Add a job, species, antagonist, area | New datum/subtype in a module; register via existing upstream API (lists, subsystem `Initialize`, `New()` hooks), not by editing the upstream registry file | No |
| Place objects on an existing station map | Automapper template or area-spawn entry (data/coords), never the `.dmm` | No |
| New tgui interface | New `.tsx` in `tgui/.../interfaces/`, marked as a fork file per local convention | No |
| Change the *body* of an upstream proc you cannot wrap, or a hardcoded value with no API | Tagged upstream edit — **stop and ask** | Yes (last resort) |

Re-opening a proc is for *wrapping* — tack logic on after `..()`, or weave a `..()` call into a small new override. **Never copy a whole upstream proc into a modular file to change one line:** it silently shadows upstream, so future upstream improvements to that proc vanish here and no one notices until something breaks. If you cannot achieve the effect by wrapping, that is a signal to stop, not to copy-paste.

If a core helper has a real generic bug but the downstream project is operating under a modular-only rule, stop and ask before touching `code/`. A modular prefixed copy can be acceptable only after the human chooses that tradeoff; keep it narrowly scoped, name it with the module prefix, comment the upstream source and exact reason, and state when it should be deleted after the upstream helper is fixed.

When an iteration replaces an earlier modular path, delete the old path in the same pass. Examples: a spritesheet makes per-accessory base64 thumbnail procs and caches dead; a `None` / `White` / `Dark` background picker makes turf-thumbnail renderers and option caches dead; a helper that now returns an `icon` directly makes a separate direction-sprite cache dead.

## Per-domain rules

- **DM code** — Content goes in the modular root. Mirror the upstream path under the override folder for type extensions; use `modules/<feature>/code/` for new content. Add new vars/subtypes/procs by re-opening types. Register your `.dm` in the include list or aggregator.
- **Defines** — Modular defines need a dedicated, late-loading location (Bubberstation: `code/__DEFINES/~~bubber_defines/`; the `~~` sorts the folder last so upstream define files are never interleaved → no conflicts). A define used in >1 file goes there. A define used in exactly one file: declare it at the top of that file and `#undef` it at the bottom.
- **Maps** — Do not edit upstream `.dmm`. Use the fork's automapper: a TOML/config entry naming a template `.dmm`, the required base map, and placement coordinates (Bubberstation: `_maps/.../automapper/automapper_config.toml`), or the simple area-spawn datum for a single object. Your template `.dmm` and its config entry are modular; the base map stays untouched.
- **Icons / sound / assets** — New `.dmi`/`.ogg` live inside the module and are referenced by full modular path (`icon = 'modular_x/icons/.../thing.dmi'`). Never repath into or edit an upstream `.dmi`. If a fork keeps shared "master" icon files (e.g. clothing sheets), add your states there per its log/readme rather than starting a parallel sheet.
- **tgui** — Interfaces live in the shared `tgui/packages/tgui/interfaces` tree (there is usually no separate modular tgui folder). Mark a *new* fork interface with the local first-line marker (Bubberstation: `// THIS IS A BUBBER UI FILE`). Editing an *upstream* `.tsx` follows the same tag rules as upstream DM edits. For interface internals, defer to the `ss13-tgui` skill.
- **Config** — Add fork config as new entries/files via the fork's config-entry system; do not rewrite upstream `config/` defaults inline.

## Anti-patterns

- Copy-pasting a whole upstream proc to change one line (shadows upstream; rots silently).
- Editing an upstream `.dmi`/`.ogg`/`.dmm` — unmergeable, breaks on every pull.
- A modular file path that does not mirror its upstream counterpart (override folders) — makes the override invisible to the next maintainer.
- A define used across files declared in a single module file instead of the shared defines folder — load-order and conflict landmine.
- A new `.dm` left out of the include list — compiles for you, fails CI / the next clean build.
- Cross-module dependencies (module A silently needs module B's defines/files) without declaring them in the module readme — breaks when one is removed.
- Untagged upstream edits — invisible at the next merge, the exact thing the whole system prevents.
- Forcing one fork's machinery (Vanderlin's temp-DME build pipeline, cmss13's heavy-fork layout) onto a different fork. Match the local convention; see `references/fork-comparison.md`.
- Leaving iteration scaffolding behind after a modular UI/content path changes: temporary loggers, base64 thumbnail caches replaced by spritesheets, option caches for hardcoded choices, and helper caches for helpers that no longer need them.

## When to stop and ask a human

Some tasks cannot be done modularly. Recognize the boundary, stop, and surface it rather than editing upstream silently:

- The change needs the **body of an upstream proc** altered, and there is no hook, signal, or `..()` wrap that reaches it.
- It needs a **hardcoded upstream value** (a `define`, a literal, a `var` default with no setter) that nothing modular can override.
- It requires **editing an upstream binary** (`.dmi`/`.ogg`) or an **upstream `.dmm`** in a way the automapper can't express.
- It depends on **upstream load order** changing, or on a type/proc that does not yet expose any extension point.
- The fork has **no modular root** at all (a heavy fork like cmss13-MARINES that edits `code/` directly) — here "modular" may not be the local norm; confirm the intended workflow before proceeding.

When you hit one, report: what you wanted to do, why no modular seam reaches it, and the options (tagged upstream edit with the fork's edit-comment grammar; an upstream PR; or a design change). Let the human choose — a tagged upstream edit is sometimes the right call, but it is the human's call, not a silent default.

## Reference files (progressive disclosure)

- `references/bubberstation-patterns.md` — Bubberstation modular layout in detail: `master_files/` vs `modules/`, the per-module `readme.md` template, the `BUBBER EDIT` comment grammar for unavoidable upstream edits, the `~~bubber_defines` convention, the automapper config schema, and the tgui file marker. **Read when working in a Bubberstation/Skyrat-style fork.**
- `references/fork-comparison.md` — Bubberstation vs Vanderlin vs cmss13-MARINES: which patterns to borrow (Vanderlin's single-line aggregator include, the `upstream_fixes.dm` override-from-module idea), which are architecture-specific and must not leak into a general fork (Vanderlin's temp-DME build, its map-import pipeline; cmss13's heavy-fork direct edits), and which rules are universal. **Read when the fork is not Bubberstation, or to judge how far a pattern generalizes.**
- `references/extension-recipes.md` — step-by-step modular recipes per content type (item, mob, job, species, area, map edit, component, crafting recipe, research design, reagent, tgui), each as a copy-the-neighbor checklist. **Read when you need a concrete starting point for a specific content type.**
