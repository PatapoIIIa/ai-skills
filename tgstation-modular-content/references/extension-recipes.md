# Extension recipes (reference)

Per-content-type modular recipes. Each is a **copy-the-neighbor checklist**, not a fixed template — the strongest move for every type is "find 2–3 existing modular examples of this type in the fork and match them." Paths use Bubberstation's `modular_zubbers/`; substitute the local modular root. None of these requires editing an upstream file.

## Universal pre-flight (every recipe)
1. Confirm the modular root and the override sub-layout (`master_files/` vs `modules/`).
2. `rg` for an existing modular example of this content type; read it.
3. Decide: net-new (→ `modules/<feature>/`) or extension of an upstream type (→ `master_files/` mirrored path, by re-opening the type).
4. Put assets in the module, reference by full modular path.
5. Register every new `.dm` in the include list / aggregator.
6. Fill the module `readme.md`, especially overrides + outside dependencies.

---

## New item / structure / clothing
- Net-new → `modules/<feature>/code/<feature>.dm`, subtype the closest upstream parent (`/obj/item/...`).
- Icons in `modules/<feature>/icons/`, referenced by full path. For clothing on-mob/in-hand sprites, add states to the fork's shared clothing sheets (see `master_files/readme.md` log) rather than a parallel sheet.
- No upstream edit: a new subtype is pure addition.

## New mob
- Subtype `/mob/living/basic/...` (or the relevant base) in `modules/<feature>/code/`.
- `icon`/`sound` point at module assets by full path.
- AI/behavior via existing components/elements (see below) rather than overriding core mob procs.

## New crafting recipe
- Subtype the crafting datum (`/datum/crafting_recipe/...`) in a module file. Recipes self-register through the upstream crafting subsystem's type-collection — no upstream registry edit.
- If the recipe needs a new define (e.g. a category), put it in the modular defines folder.

## New research design / node
- Subtype `/datum/design/...` (and `/datum/techweb_node/...`) in a module. These are gathered by type at init; adding a subtype is enough.
- Bubberstation example: `modular_zubbers/master_files/code/modules/research/designs/weapon_designs.dm`.

## New reagent
- Subtype `/datum/reagent/...` in a module; reagents register by type. Reference any new icon/overlay by modular path.

## New job
- New `/datum/job/...` subtype in `modules/<feature>/`. Register through the upstream job-subsystem's collection mechanism (type-based) and the outfit datum — **not** by editing the upstream job list file.
- Outfit: subtype `/datum/outfit/job/...`; add new clothing as new subtypes/assets.
- Access/IDs and HUD may need a modular define (jobs define file). Map presence (a spawn point) goes through the automapper/area-spawn, not a `.dmm` edit.
- Watch for hidden registries (department lists, PDA/console assignments). If any sit behind a hardcoded upstream list with no API, that part is a **stop-and-ask** boundary.

## New species
- New `/datum/species/...` subtype + sprite-accessory/bodypart datums, all in a module.
- Bubberstation example: `modular_zubbers/master_files/code/modules/mob/living/carbon/human/species_types/plasmamen.dm`.
- Species frequently need modular defines (species traits/flags) → defines folder. Bodypart/feature sprites → module icons by full path.
- This is a type where partial upstream coupling is common (feature lists, preference menus). Check whether preference registration has an extension hook before assuming it's fully modular.

## New area
- Subtype `/area/...` in a module; reference any area-specific icon/ambience by modular path. Placing the area on a map is a **map edit** → automapper, not a `.dmm` change.

## Map edit (objects/rooms on an existing station map)
- Single object → simple **area-spawn** datum entry (heatmaps a sensible free tile).
- Room-sized → **template automapper**: a template `.dmm` under `_maps/.../automapper/templates/...` + a TOML entry (`map_files`, `directory`, `required_map`, `coordinates [X,Y,Z]`, `trait_name`). See `bubberstation-patterns.md` §5.
- Never edit the base `.dmm`.

## New component / element / signal
- New `/datum/component/...` or `/datum/element/...` in a module; attach via `AddComponent`/`AddElement` from your modular code or a modular proc-wrap on the target type. Components are the *preferred* way to add behavior to existing types without overriding their procs.
- New **signals**: define the signal name in the modular defines folder; send/register from modular code. Listening to an *upstream* signal from modular code is fully modular and is often the cleanest seam — prefer it over wrapping a proc when upstream already sends a relevant signal.
- New **trait**: define in the modular defines (traits) file; reference the fork's trait-source convention. Bubberstation logs trait files in `master_files/readme.md`.

## Extending an existing upstream type (vars / behavior)
- Mirror the upstream path under `master_files/` and re-open the type:
  ```dm
  // modular_zubbers/master_files/code/datums/outfit.dm
  /datum/outfit
  	var/datum/sprite_accessory/clothing/bra = null
  ```
- For behavior, wrap a proc with `. = ..()`. Do **not** copy the whole proc. If you can't reach the effect by wrapping/signals/components, stop and ask.

## New tgui interface
- New `.tsx` in `tgui/packages/tgui/interfaces/<Name>.tsx`, with the fork's first-line marker (`// THIS IS A BUBBER UI FILE`).
- Backend: the DM datum's `ui_interact`/`ui_data`/`ui_act` live in your modular `.dm`. For interface implementation details, switch to the `ss13-tgui` skill.
- Editing an *upstream* interface uses the upstream-edit tag grammar, in JSX-legal comment form.

---

## Quick "is this modular?" self-check
- Did I edit any file I didn't create under `code/`, upstream `_maps/`, `icons/`, `sound/`, `interface/`? → If yes, justify or stop.
- Are all my assets under the modular root and referenced by full modular path?
- Are multi-file defines in the shared modular defines folder?
- Is every new `.dm` in the include list / aggregator?
- Does the module readme list overrides + outside dependencies?
- Would this survive an upstream re-sync with zero conflicts in upstream files? If not, which file conflicts and is that truly unavoidable?
