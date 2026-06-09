# Visuals Guide

Generated on 2026-03-14. Derived from the project's official VISUALS.md document.
This file is the AI navigation layer's reference for visual and rendering systems — appearances, overlays, planes, filters, lighting, and related BYOND rendering concepts.

The navigation layer may lag behind the live documents. If this file and the source docs disagree, trust the source docs.
For the authoritative in-depth guide, see the source at `VISUALS.md` (distributed separately). For the rendering system's relay diagram, see `code/_onclick/hud/rendering/_render_readme.md`.

---

## Quick Reference Table

| Topic | Key Type / Var | Notes |
|---|---|---|
| Appearance caching | `mutable_appearance`, `iconstate2appearance()` | Cache as `static`; never recreate per-call |
| Overlay management | `/atom/var/overlays`, `update_overlays()` | Use managed system; `add_overlay`/`cut_overlay` directly = risky |
| Client-only images | `/client/var/images`, `/datum/atom_hud` | HUD system groups images by viewer set |
| Screen objects | `/client/var/screen`, `screen_loc` | Use for HUD elements; `screen_loc` anchors to view size |
| Rendering order | `/atom/var/layer`, `/atom/var/plane` | Plane first, then layer; higher = in front |
| Group shader effects | `PLANE_MASTER` flag + `/client/var/screen` | Applies color/alpha/filter to all objects on that plane |
| Render relays | `render_target` / `render_source` | Links plane masters for advanced pipeline effects |
| Filters (shaders) | `/atom/var/filters` (wrapped) | Client-side; use filter management wrapper, not raw list |
| Particles | `/obj/effect/abstract/particle_holder` | One emitter per atom; use holder for multiple |
| Lighting underlays | Color matrix per tile corner | Our system, not BYOND's built-in light |
| Gliding / movement smoothness | `glide_size`, `set_glide_size()` | Must match actual move rate; use `DELAY_TO_GLIDE_SIZE` |
| Multiz rendering | Plane tree + manual Z offsets | All plane-setting code must accept a turf/context source |
| Invisibility | `/atom/var/invisibility`, `/mob/var/see_invisible` | Scale 0–101; used for ghosts, countdowns |
| Animated transitions | `animate()` | Client-side visual only; server value changes instantly |
| GAGS | Runtime icon composition | See `https://hackmd.io/@tgstation/GAGS-Walkthrough` |

---

## Appearances

Everything rendered on the map has an `/atom/var/appearance` that describes its render recipe. Appearances are **static** (immutable) — you cannot edit one directly.

To modify an appearance, use `/mutable_appearance`:
1. Create a new mutable appearance.
2. Assign the static appearance to it (`temporary_ma.appearance = original`).
3. Edit the mutable appearance's vars.
4. Apply back via the atom's var.

```dm
/proc/mutate_icon_state(mutable_appearance/thing)
    var/mutable_appearance/temp = new()
    temp.appearance = thing
    temp.icon_state += "_variant"
    return temp.appearance
```

> **Warning:** Appearances are unique — only one copy of each hash combination exists globally. Modifying any appearance var re-hashes it. This is why appearance changes have variable cost. BYOND has also been observed to corrupt appearances during mutable-appearance operations; be cautious.

**Performance rule:** Convert icons to appearances once with `iconstate2appearance()` or `icon2appearance()` and store as `static`. Never recreate on every call. See `ai_navigation/coding_standards.md` §Optimization and `ai_navigation/performance_gotchas.md` §7.

---

## Overlays

`/atom/var/overlays` is a list of static appearances rendered on top of the atom. Rendering order within the list follows `layer` and `plane`, with ties broken by list order.

**Important:** overlays are **copies**, not references. Once added, they cannot be edited in-place — they must be removed and re-added.

### Managed overlay system (preferred)

The project wraps overlays through `update_overlays()`:
- Called by `update_icon()`, which is called by `update_appearance()`.
- Returns a list of things to convert to static appearances via `build_appearance_list()`.
- Results are stored in `managed_overlays` on `/atom`, which clears old overlays before each update.
- A dedicated subsystem batches overlay compiles once per tick — this avoids add/remove/add churn for things like humans that mutate overlays frequently.

```dm
/obj/item/my_thing/update_overlays(list/overlays)
    . = ..()
    if (is_on)
        . += emissive_appearance(icon, "on_glow")
```

`add_overlay()` / `cut_overlay()` bypass this system — they give no built-in way to "clear" added overlays later. Use them only when you have an explicit removal strategy.

### Icon state name collision (BYOND hellspawn)

An overlay whose `icon_state` name matches a state on the parent atom's icon will use the **parent's** icon state instead of its own. This caused the "transparent" and "dark" lighting underlay bugs. When adding overlays, verify there are no icon state name collisions with the parent.

---

## Visual Contents (`vis_contents`)

`vis_contents` renders a referenced atom **on** the source atom. Unlike overlays, it is a **reference** (live — changes to the target reflect immediately). This is used for multiz.

Key `vis_flags`:
- `VIS_INHERIT_ID` — clicking the vis_contents'd atom acts as clicking the source atom.
- `VIS_INHERIT_PLANE` — forces the vis_contents'd object to use the source's plane. Useful but destructive — breaks any plane-dependent effects on the contained object.

**Cost warning:** `vis_contents` requires per-tick checks for changes, and this cost scales with player count. Minimize use relative to overlays.

---

## Images and Client Images

`/image` objects are mutable appearances with a location. They can be used in overlays or displayed to specific clients only.

`/client/var/images` — a list of image objects shown only to that client, placed at the image's `loc`.

### atom_hud system

For showing a shared image set to a defined group of clients (e.g. medihud, robot trails), use `/datum/atom_hud`:
- Stores image list (sorted by source Z level for performance) and a client list.
- Images are mirrored into/out of `client.images` based on HUD membership.

---

## Planes and Plane Masters

`/atom/var/plane` controls rendering order (higher = in front) and enables **plane master** grouping.

A plane master is an atom with the `PLANE_MASTER` appearance flag in a client's `screen`. Any atom on the same plane is rendered onto the plane master first. This allows applying color, alpha, or filter effects to an entire logical group (e.g. the lighting plane, the emissive plane).

Planes must be whole integers with absolute value ≤ 10000 (to support `FLOAT_PLANE`).

`FLOAT_PLANE` and `FLOAT_LAYER` offsets work like floating layers — they propagate up until they find a real layer/plane, then offset from it.

### plane_master_controller

`/atom/movable/plane_master_controller` allows grouping plane masters for filter effects. Somewhat superseded by render relays, but still valid for some use cases.

> **Plane masters are map-window-scoped.** For subviews (e.g. cameras), a duplicate set of plane masters with the correct `screen_loc` must be generated.

---

## Render Target / Source

`render_target` and `render_source` create explicit "render onto" relationships between atoms — literally compositing one render output onto another, as a pipeline step.

Prepend `*` to a `render_target` value to suppress the target's normal render and only display it via the relay.

Used in this codebase to link plane masters together ("render relays") for advanced multi-step effects. See `code/_onclick/hud/rendering/_render_readme.md` for the relay diagram.

> **Layer matters with render relays.** The layer of the last plane master in the chain determines render order — plane value alone does not guarantee final order.

In-game debug: run `Edit/Debug Planes` to view relay connections and plane master states.

---

## Layers

`/atom/var/layer` sets render stacking order within the same plane. Higher layer = rendered in front. Objects earlier in a tile's `contents` draw first (rendered lowest).

`TOPDOWN_LAYER` (value `10000`) added to a layer forces that appearance into topdown rendering, locally overriding `side_map` rules. Useful for keeping relative ordering without making all related sources static.

---

## Filters

Filters apply client-side shader effects (blur, color distortion, alpha masking, etc.) to an atom. They run on the client machine — cheap for the server, potentially expensive for the client.

> Do not manipulate `/atom/var/filters` directly. Use the project's filter wrapper system, which handles priority ordering and prevents management conflicts. Raw list manipulation can break `animate()` calls on the same atom.

In-game debug: VV an atom → dropdown → `Edit Filters` (filterrific).

Common uses:
- Alpha masking via render_source input → used for emissive lighting.
- Distortion with render_source → used for gravity anomaly effect.

---

## Particles

`/particles` subtypes attach visual particle emitters to atoms. BYOND natively allows only one emitter per atom.

**Project solution:** `/obj/effect/abstract/particle_holder` — pass the atom to mirror and the particle type. The holder follows the parent and manages the emitter.

In-game debug: VV an atom → dropdown → `Edit Particles`.

---

## Lighting

### BYOND lighting (basic)

Tiles are "lit" or not. Unlit tiles and their contents are hidden (like a wall). Controlled by:
- `/atom/var/luminosity` — range in tiles that the atom lights up; respects sight lines. Also governs what `view()` considers visible.
- `/mob/var/see_in_dark` — square radius around mob that cuts BYOND darkness (why you see yourself in darkness).
- `dview()` — like `view()` but uses a specified mob's sight settings rather than global.

### Project lighting (custom)

Each tile carries a lighting underlay — a color gradient with RGBA values per corner ("lighting corners"). Corner values affect the 4 tiles they touch, applied via color matrices. This produces smooth, colored lighting from a single underlay per tile.

There is also a separate overlay lighting system; derive specifics from the lighting subsystem code.

---

## Animate()

`animate()` visually transitions between appearance values on the client side. The server value changes immediately; the client interpolates the visual.

Supports: alpha, color, transform, pixel offsets, filter variables, and more.

Works in parallel mode for simultaneous animations on the same atom, but this mode is finicky. Filters and their vars are supported, enabling effects like pulsing glow.

---

## Invisibility

`/atom/var/invisibility` (0–101) hides atoms from mobs whose `see_invisible` is lower than the atom's value.

Used for: ghosts, ghost-visible objects, timers, countdowns, some lighting backdrop effects.

---

## Gliding and Movement Smoothness

`/atom/movable/var/glide_size` controls pixels-per-server-tick for smooth visual movement. Must be kept in sync with actual movement rate to avoid jitter.

- Set via `set_glide_size()`, which propagates to carried atoms.
- Use `DELAY_TO_GLIDE_SIZE` for client movement (caps at 32 px/tick).
- Use `MOVEMENT_ADJUSTED_GLIDE_SIZE` for subsystem-driven movement.

> Time dilation spikes can cause visual jumping because glide rate is computed simply. Delays not evenly divisible by the tick rate (0.5 deciseconds) will produce occasional stutter — this is a known engine limitation.

---

## Color Matrices

`/atom/var/color` accepts either an `rrggbbaa` HTML string (simple tint + alpha override) or a 20-element list acting as a 4×5 color matrix.

Matrix format: `list(rr,br,gr,ar, rb,bb,gb,ab, rg,bg,gg,ag, ra,ba,ga,aa, cr,cb,cg,ca)` where each entry is a multiplier/offset for color channel routing.

Allows full color channel shifting — used for per-plane tinting and lighting effects.

In-game debug: VV an atom → dropdown → `Edit Color as Matrix`.

---

## Transform

`/atom/var/transform` applies visual shift, scale, and rotation via a matrix. Helper procs exist for all common operations.

> The transform var is **copied** on read — always write back the full modified value, not just modify the intermediate.

---

## Pixel Offsets

`pixel_x/y` — "real" offset: changes both visual and physical position (affects renderer layering in positional formats).
`pixel_w/z` — "fake" offset: changes only visual position (physical layering position unchanged).

For the current `SIDE_MAP` format, physical position (`pixel_x/y`) affects rendering order. Combining real and fake offsets allows fine control over layering vs. visual placement.

Physical position snaps to tile increments of `world.icon_size / 2` (due to `LEGACY_MOVEMENT_MODE`).

---

## Map Format — SIDE_MAP (current)

The project currently uses `SIDE_MAP`. Key properties:
- Layering is based on physical proximity to the front of the screen (not purely layer/plane values).
- `pixel_y + y` determine physical depth. `bound_width/height/x/y` describe the physical footprint.
- Objects closer to the front layer on top.
- All plane-setting code must accept a turf/context source to support Z-offset calculation.
- Physical bounds can only change in multiples of 32 (engine limitation from `LEGACY_MOVEMENT_MODE`).
- These constraints frequently cause layering conflicts that cascade — hard to debug, no pixel-level resolution available.

---

## Multiz

Current implementation uses a duplicated plane master tree per Z level. All objects on the map have their plane manually offset based on Z layer. Edge cases require explicit plane offsets rather than context-derived ones.

Avoid the old `vis_contents`-based multiz pattern — it destroys plane effects and breaks `side_map`.

---

## GAGS (Greyscale Auto-Generated Sprites)

Runtime icon composition system. Generates colored sprites at runtime by combining greyscale layer sprites with color arguments. Use when an item or mob needs recolorable sprites without pre-baking every color variant.

### How It Works

Three parts must exist for GAGS to function:

1. **DMI file** — contains the layer sprites (greyscale icon states, one per visual layer)
2. **JSON config** (`code/datums/greyscale/json_configs/`) — defines how layers are combined and which color IDs apply to each
3. **Config type** (`/datum/greyscale_config`) — DM datum that ties the DMI and JSON together

The atom then sets `greyscale_config` and `greyscale_colors` vars. `SSgreyscale` owns the runtime generation.

### JSON Config Structure

```json
{
    "icon_state_name": [
        {
            "type": "icon_state",
            "icon_state": "cloth",
            "blend_mode": "overlay",
            "color_ids": [ 1 ]
        },
        {
            "type": "icon_state",
            "icon_state": "ornamentation",
            "blend_mode": "overlay",
            "color_ids": [ 2 ]
        },
        {
            "type": "icon_state",
            "icon_state": "plate",
            "blend_mode": "overlay"
        }
    ]
}
```

- `type` — required. `"icon_state"` loads from the DMI. `"reference"` loads from another `/datum/greyscale_config` subtype.
- `icon_state` — icon state name inside the DMI file.
- `blend_mode` — how this layer merges with the result so far. Common values: `"overlay"` (standard), `"add"`, `"multiply"`.
- `color_ids` — which color argument slot to use (1-indexed). Omit for uncolored layers (e.g. transparent overlay plates).
- Inner lists `[ [...], [...] ]` — process as a sub-group before merging; useful for complex blend pipelines.
- `MAX_SANE_LAYERS = 50` — hard limit.

### Config Type (DM)

```dm
/datum/greyscale_config/my_item
    name = "My Item"
    icon_file = 'icons/obj/clothing/head/my_item.dmi'
    json_config = 'code/datums/greyscale/json_configs/my_item.json'

// Subtype for worn icon — reuses icon_file from parent
/datum/greyscale_config/my_item/worn
    json_config = 'code/datums/greyscale/json_configs/my_item_worn.json'
```

### Atom Vars

```dm
/obj/item/clothing/head/my_item
    greyscale_config             = /datum/greyscale_config/my_item
    greyscale_colors             = "#ff0000"           // one hex per color_id, space-separated
    greyscale_config_worn        = /datum/greyscale_config/my_item/worn
    greyscale_config_inhand_left  = /datum/greyscale_config/my_item/lefthand
    greyscale_config_inhand_right = /datum/greyscale_config/my_item/righthand
```

`greyscale_colors` is a space-separated string of hex colors, one per `color_id` slot: `"#ff0000 #00ff00"` for two color IDs.

### Greyscale Sprite Authoring Rules

- **Pure white** in the greyscale layer = full color from `greyscale_colors`.
- **Darker grey** = progressively darker tint of the color.
- **Pure black** = always black regardless of color.
- Layers without `color_ids` are applied as-is (useful for semi-transparent overlays, detail plates, etc.).
- Only the layers that actually differ by direction need multi-directional sprites — if ornamentation is the same from all sides, sprite only one direction.

### Debug Workflow (no recompile needed)

1. Spawn the item in-game.
2. VV the item → top-right dropdown → **Greyscale Debugging**.
3. The debug menu shows:
   - **Config selector** — switch between greyscale configs live.
   - **Color pickers** — one per color_id slot; blue button opens color picker.
   - **Apply** — pushes current colors to the in-world object.
   - **Refresh** — reloads DMI and JSON from disk without restarting the server.
   - **Preview** — shows each generation step: left column = layer input, right column = cumulative result.
4. Iterate: edit JSON or DMI → Refresh → Apply → inspect in preview.
5. Only recompile when adding new DM code (new config type, new atom vars).

### File Locations

| What | Where |
|---|---|
| JSON configs | `code/datums/greyscale/json_configs/` |
| Config type definitions | `code/datums/greyscale/` (add to existing file or new file) |
| Base config datum | `code/datums/greyscale/_greyscale_config.dm` |
| Layer datum | `code/datums/greyscale/layer.dm` |
| Existing configs (reference) | `code/datums/greyscale/greyscale_configs.dm` |
| Runtime owner | `SSgreyscale` (`code/controllers/subsystem/greyscale.dm`) |

### Common Mistakes

- **Forgetting to include new DM files in the `.dme`** — GAGS config types are not auto-included.
- **color_ids out of range** — if `greyscale_colors` has 1 color but a layer references `color_ids: [2]`, generation silently fails.
- **Leaving gaps in the sprite** — layers without full coverage leave transparent holes; fill with a nearby color or use a base layer.
- **Using GAGS for non-recolorable sprites** — unnecessary overhead; use normal icon_states if no recoloring is needed.

---

## Debug Tools Summary

| Tool | Access |
|---|---|
| Color matrix editor | VV atom → dropdown → `Edit Color as Matrix` |
| Filter editor (filterrific) | VV atom → dropdown → `Edit Filters` |
| Particle editor | VV atom → dropdown → `Edit Particles` |
| Plane/relay debugger | In-game command: `Edit/Debug Planes` |

---

*Cross-references:*
- *Appearance performance hazards: `ai_navigation/performance_gotchas.md` §7*
- *Appearance object accumulation / overlay cost: `ai_navigation/engine_limits.md` §Overlays and Appearance*
- *Coding standards for overlay caching: `ai_navigation/coding_standards.md` §Optimization*
- *Render relay diagram: `code/_onclick/hud/rendering/_render_readme.md`*
