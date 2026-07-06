# Bubberstation modular patterns (reference)

Grounded in static analysis of `C:\Axis\Bubberstation` (a Skyrat-derived, /tg/-tracking fork). Bubberstation carries **two** modular roots: `modular_skyrat/` (inherited from its Skyrat upstream, ~210 modules) and `modular_zubbers/` (Bubberstation's own, the actively-grown one). Both follow the same internal shape. The authoritative in-repo doc is `modular_zubbers/readme.md` ("The modularization handbook - Bubber style"); `modular_skyrat/module_template.md` is the per-module readme template.

## Table of contents
1. The two-folder split: `master_files/` vs `modules/`
2. Re-opening types (the override mechanism)
3. Per-module folder layout + readme template
4. Defines: the `~~bubber_defines` convention
5. Maps: the automapper
6. Assets: icons & sound
7. tgui marker
8. Unavoidable upstream edits: the `BUBBER EDIT` grammar
9. The include list

## 1. master_files vs modules

Inside a modular root (`modular_zubbers/`):

- **`master_files/`** — for *overriding or extending upstream types*. It **mirrors the upstream path**: to extend `code/datums/outfit.dm` you create `modular_zubbers/master_files/code/datums/outfit.dm`. Same relative path, `modular_zubbers/master_files/` prepended. This makes the override trivially findable and signals "this re-opens an upstream type." Bubberstation keeps a log of shared master files in `modular_skyrat/master_files/readme.md` (clothing sheets, trait files, etc.) so people append to the shared file instead of forking parallel ones.
- **`modules/<feature>/`** — for *net-new, self-contained content*. Everything for one feature lives in one folder: `modules/<feature>/code/*.dm`, `modules/<feature>/icons/*.dmi`, `modules/<feature>/sound/*.ogg`, plus `readme.md`. Example: `modular_skyrat/modules/barsigns/` holds `code/barsigns.dm`, `icons/barsigns.dmi`, `readme.md`.
- Beyond `master_files`/`modules`, `modular_zubbers/` also holds top-level `code/`, `icons/`, `interface/`, `maps/`, `sound/`, `strings/` mirrors for content that does not fit a single module.

Rule of thumb: **new thing → `modules/`. Touching an existing upstream type → `master_files/` at the mirrored path.**

Note Bubberstation's own policy (from the handbook): `modular_skyrat/` files may be edited freely **but new file creation there is discouraged** — they intend to retire that folder. New work goes in `modular_zubbers/`. Always confirm the current target folder from the repo's handbook rather than assuming.

## 2. Re-opening types (the override mechanism)

DM merges all declarations of a type across files. So from a modular file you can:

**Add a var to an existing type** (no upstream edit):
```dm
/datum/outfit
	var/datum/sprite_accessory/clothing/bra = null
```

**Wrap an existing proc** — call the parent, add behavior around it:
```dm
/obj/item/gun/shoot_live_shot(mob/living/user, pointblank, atom/pbtarget, message)
	. = ..()            // run upstream's version first; . holds its return
	if(muzzle_flash)
		spawn_sparks(src)   // your added behavior
```

**Add a subtype** — the normal case for new content; touches nothing upstream:
```dm
/obj/item/gun/ballistic/automatic/my_new_gun
	name = "prototype rifle"
	icon = 'modular_zubbers/icons/obj/guns/my_gun.dmi'
```

**Why same-type overrides work — the hidden include-order rule.** `/obj/item/gun/shoot_live_shot(...)` in a modular file re-defines a proc on the *same type* that upstream declared it on (`/obj/item/gun/proc/shoot_live_shot`). DM resolves this by include order: the later definition in the `.dme` overrides the earlier one, and `..()` inside it calls the earlier (upstream) definition. This is why modular includes always sit at the **tail** of the `.dme` (Bubberstation's modular block after the upstream block; Vanderlin's aggregator is the second-to-last line). If a modular override were included *before* the upstream file, `..()` would not reach the upstream body — and both orders compile silently. Verify when in doubt: `grep -n "upstream_file.dm\|your_module" <project>.dme` and confirm your include comes later. (Compile-verified on Vanderlin, DM 516: wrapper `. = ..()` + full-body same-type override both build clean with the module included last.)

The handbook's explicit warnings:
- Do **not** copy a whole upstream proc to change one line — it shadows upstream and silently drops future upstream changes to that proc. Only wrap (`..()`).
- Watch performance when wrapping **hot procs** (`Life()`, etc.); each override adds a call. There, a tagged upstream edit may be the better trade — a judgment call, not an automatic modular win.
- "It's okay if something isn't fully modular. Sometimes it's the better choice." Modularity is the strong default, not dogma.

## 3. Per-module folder layout + readme template

```
modules/<feature>/
├── readme.md
├── code/<feature>.dm        (+ more .dm as needed)
├── icons/<feature>.dmi      (if it has sprites)
└── sound/<feature>.ogg      (if it has sounds)
```

The `readme.md` template (`modular_skyrat/module_template.md`) records, per module:
- **Module ID** — UPPERCASE_UNDERSCORE tag, used in edit comments and as a case-sensitive search handle.
- **Description** — what it adds.
- **TG Proc/File Changes** — any upstream files touched (ideally `N/A`).
- **Modular Overrides** — any `master_files` overrides added, with the procs/vars changed.
- **Defines** — defines added and where.
- **Included files not contained in this module** — shared icons/sounds/etc. the module depends on. *This is how cross-module dependencies are declared.*
- **Credits**.

Filling this out honestly is what keeps merges and removals safe; the "Included files…" and "Modular Overrides" sections are the dependency map.

## 4. Defines: `~~bubber_defines`

Modular defines live in `code/__DEFINES/~~bubber_defines/` (files like `jobs.dm`, `species.dm`, `combat.dm`). The `~~` prefix makes the folder sort **after** every upstream `__DEFINES` file, so modular defines are appended rather than interleaved — eliminating define-file merge conflicts. Rules from the handbook:
- A define used in **more than one file** *must* be declared in `~~bubber_defines`.
- A define used in **exactly one file**: declare at the top of that file, `#undef` at the bottom (keeps IDE autocomplete/context menus clean).
- These define files are `#include`d in the `__DEFINES` section of the `.dme`, before the code that uses them (load order matters — defines must precede use).

## 5. Maps: the automapper

Never edit upstream `.dmm` (`modular_zubbers/readme.md`: "DO NOT CHANGE TG MAPS, THEY ARE HELD TO THE SAME STANDARD AS ICONS"). Instead:

- **Template automapper** — for a room-sized edit. Add a `.dmm` template under `_maps/bubber/automapper/templates/...` and an entry in `_maps/bubber/automapper/automapper_config.toml`:
  ```toml
  [templates.birdshot_armory]
  map_files = ["birdshot_armory.dmm"]            # template(s); multiple = random pick
  directory = "_maps/bubber/automapper/templates/Birdshot/"
  required_map = "birdshot.dmm"                  # only applies on this base map
  coordinates = [50, 106, 1]                     # X, Y, Z (Z as in SDMM, relative to template)
  trait_name = "Station"                         # Z-level trait: Station / CentCom / Mining
  ```
  The subsystem overlays the template onto the base map at runtime; the base `.dmm` is never modified on disk.
- **Simple area automapper** — for a single object. A datum entry that heatmaps an area and drops one item in a sensible free tile (avoids blocking doors/halls). Implemented in `modular_skyrat/modules/automapper/`.

So a "map edit" is two modular artifacts (a template `.dmm` + a TOML entry, or one area-spawn datum) and zero upstream-map changes.

## 6. Assets: icons & sound

- New `.dmi`/`.ogg` live inside the module folder and are referenced by full modular path:
  ```dm
  /mob/living/basic/mining/new_mob
  	icon = 'modular_zubbers/icons/mob/simple/lavaland/lavaland_monsters.dmi'
  	sound = 'modular_zubbers/sound/items/weapons/bite.ogg'
  ```
- **Never** edit or repath an upstream `.dmi` — binary, unmergeable.
- For shared sheets the fork already maintains (clothing on-mob/in-hand sheets, emoji, HUD), add your icon *states* into the existing shared file listed in `modular_skyrat/master_files/readme.md`, rather than starting a parallel sheet.

## 7. tgui marker

There is no separate modular tgui folder; all interfaces live in `tgui/packages/tgui/interfaces`. A **new** fork interface gets, as line 1:
```js
// THIS IS A BUBBER UI FILE
```
That marks the whole file as modular — no per-line edit tags needed inside it. Editing an **upstream** `.tsx` instead uses the `BUBBER EDIT` grammar (below), with `//` or `/* */` as JSX requires. (Confirmed in-repo: 15 files carry the marker.)

## 8. Unavoidable upstream edits: the `BUBBER EDIT` grammar

When (rarely) an upstream `code/` file must be edited, Bubberstation tags it so the next merge is legible. (Confirmed in-repo: ~403 files under `code/` carry these tags — even a disciplined fork can't reach zero, but every edit is marked.) The grammar:

```dm
// BUBBER EDIT - ADDITION - START - MODULE_ID
var/added = TRUE
// BUBBER EDIT - ADDITION - END

// BUBBER EDIT - CHANGE - START - MODULE_ID
if(new_condition)
// BUBBER EDIT - CHANGE - END

// BUBBER EDIT - REMOVAL - START - MODULE_ID - (Moved to modular_zubbers/.../file.dm)
/* ...original code commented out... */
// BUBBER EDIT - REMOVAL - END
```

`MODULE_ID` ties the edit back to its module. For a general fork, substitute the fork's own tag (`SKYRAT EDIT`, `<FORK> EDIT`, …) — read a neighboring tagged edit to copy the exact wording. **For this skill's purposes, reaching for this grammar is the "stop and ask a human" boundary** — it is the documented escape hatch, not a default.

## 9. The include list

New `.dm` files compile in only when `#include`d. Bubberstation appends modular includes to the main `tgstation.dme` between `// BEGIN_INCLUDE` and `// END_INCLUDE` (a long flat list, kept sorted). CI enforces that every `.dm` is included: `tools/ticked_file_enforcement/schemas/` explicitly lists `modular_skyrat/` and `modular_zubbers/` as scanned directories, so a forgotten include fails CI even if it builds locally. Add the `#include` line in the correct sorted position matching its neighbors. (Contrast: Vanderlin includes one aggregator line and nests the rest — see `fork-comparison.md`.)

**Exception — modular unit tests live inside `code/`.** Tests must sit where the test framework scans: Bubberstation keeps fork tests in `code/modules/unit_tests/~skyrat/` (the `~` prefix again sorting them after upstream tests, and the ticked-file schema special-cases that path). Creating a file under `code/` is acceptable *only* for cases like this where upstream machinery dictates the location — keep the fork-marking prefix.
