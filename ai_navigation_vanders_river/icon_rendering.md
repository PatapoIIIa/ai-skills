# Icon Smoothing and Appearance Caching

Generated 2026-03-14 from source analysis of `code/controllers/subsystem/icon_smooth.dm`, `overlays.dm`, `vis_overlays.dm`, `code/__DEFINES/icon_smoothing.dm`, `code/__HELPERS/icon_smoothing.dm`.

---

## Part 1 — Icon Smoothing System

### What It Does

Icon smoothing automatically selects the correct icon_state for a tile or object based on which adjacent atoms it should visually connect with. A wall next to another wall shows a joined sprite; isolated, it shows a standalone sprite. This happens at runtime without pre-baking every combination.

### Two Smoothing Modes

**SMOOTH_BITMASK** — the primary mode. Scans cardinal and optionally diagonal neighbors, builds an 8-bit junction bitmask, then sets `icon_state = "[smoothing_icon]-[bitmask]"`. Requires pre-baked icon states for every possible bitmask value in the DMI. Use `smooth_wall.dmi` as a template.

**SMOOTH_EDGE** — turf-only. Instead of changing `icon_state`, adds overlay images at tile edges that visually bridge into adjacent tiles. Uses `neighborlay` and `neighborlay_self` vars. Incompatible with bitmask smoothing.

### smoothing_flags Bitmask

| Flag | Meaning |
|---|---|
| `SMOOTH_BITMASK` | Use bitmask adjacency icon_state selection |
| `SMOOTH_BITMASK_CARDINALS` | Bitmask, but only cardinal directions (no diagonals) |
| `SMOOTH_EDGE` | Turf edge overlay mode — incompatible with bitmask |
| `SMOOTH_BORDER` | Treat map border as an adjacent smoothing match |
| `SMOOTH_OBJ` | Also scan turf contents for anchored movables when checking adjacency |
| `SMOOTH_QUEUED` | Internal — atom is currently in SSicon_smooth queue; do not set manually |

`USES_SMOOTHING = SMOOTH_BITMASK | SMOOTH_BITMASK_CARDINALS | SMOOTH_EDGE` — use this to check if an atom participates in smoothing at all.

### Smoothing Groups

Atoms smooth with atoms that share a group. Groups are string-encoded numeric IDs concatenated into a single string var:

```dm
// turf groups — S_TURF(n) — positive IDs
smoothing_groups = SMOOTH_GROUP_CLOSED_WALL   // "12,"
smoothing_list   = SMOOTH_GROUP_CLOSED_WALL + SMOOTH_GROUP_WALLS  // "12,-1,"

// obj groups — S_OBJ(n) — negative IDs (prefix "-")
smoothing_groups = SMOOTH_GROUP_WALLS         // "-1,"
```

- `smoothing_groups` — what groups this atom **belongs to** (what it is)
- `smoothing_list` — what groups this atom **smooths with** (what it connects to)
- If `smoothing_list` is null, the atom only smooths with its own exact type
- If `smoothing_list` contains any `S_OBJ` entry (negative prefix), `SMOOTH_OBJ` flag is auto-set via `SETUP_SMOOTHING`
- Groups must be sorted ascending — CI test `focus_only/sorted_smoothing_groups` enforces this

### Junction Bitmask Components

```
NORTH_JUNCTION     = NORTH  = 1
SOUTH_JUNCTION     = SOUTH  = 2
EAST_JUNCTION      = EAST   = 4
WEST_JUNCTION      = WEST   = 8
NORTHEAST_JUNCTION = 1<<4   = 16
SOUTHEAST_JUNCTION = 1<<5   = 32
SOUTHWEST_JUNCTION = 1<<6   = 64
NORTHWEST_JUNCTION = 1<<7   = 128
```

Cardinal junctions are checked first. Diagonal junctions are only checked if both adjacent cardinal junctions are set (e.g. NORTHEAST is only checked if NORTH and EAST are both set). This optimises the common case — most tiles are not corner-to-corner.

With `SMOOTH_BITMASK_CARDINALS`, diagonals are never checked. Result icon_state range: 0–15.
With `SMOOTH_BITMASK` (full), result icon_state range: 0–255.

### SSicon_smooth — Runtime Owner

`SSicon_smooth` owns all deferred smoothing. Key design choices:

- `wait = 1`, `flags = SS_TICKER` — fires every tick
- Uses a **static index** pattern to resume across ticks without copying the list:
  ```dm
  var/static/last_index = 0
  for(last_index in 1 to length(cached)):
      ...process...
      if(MC_TICK_CHECK): break
  cached.Cut(1, last_index+1)  // trim processed entries after loop
  ```
- Atoms not yet on a z-level (`!z`) are deferred to a second list and reprocessed after the main queue empties
- `can_fire` is set to FALSE when both queues are empty — subsystem goes idle until `add_to_queue` re-enables it

### Queuing Macros

```dm
// Queue one atom for smoothing (no-op if already queued)
QUEUE_SMOOTH(thing)

// Queue all atoms within 1 tile of thing
QUEUE_SMOOTH_NEIGHBORS(thing)
```

`QUEUE_SMOOTH` checks `USES_SMOOTHING` before adding — safe to call on any atom.
`remove_from_queues` exists but is expensive (list removal) — prefer unsetting `SMOOTH_QUEUED` flag when possible.

### Smooth Proc Chain

```
QUEUE_SMOOTH(atom)
  → SSicon_smooth.add_to_queue(atom)        sets SMOOTH_QUEUED, adds to smooth_queue
  → SSicon_smooth.fire()                    dequeues, calls atom.smooth_icon()
  → atom.smooth_icon()                      clears SMOOTH_QUEUED, calls smooth()
  → atom.smooth()                           scans neighbors, builds junction bitmask
  → atom.set_smoothed_icon_state(junction)  sets icon_state = "[smoothing_icon]-[junction]"
```

For SMOOTH_EDGE turfs, `smooth()` calls `set_neighborlays(junction)` instead, which adds/removes edge overlay images via `add_neighborlay` / `remove_neighborlays`.

### Diagonal Wall Corners

To smooth diagonally, add `SMOOTH_DIAGONAL_CORNERS_CORNERS` to `smoothing_flags` and provide all diagonal icon states in the DMI. For turfs, the tile under a diagonal corner defaults to the previous turf's appearance. To fix the underlay:

```dm
fixed_underlay = list("icon" = 'icons/turf/floors.dmi', "icon_state" = "plating")
```

### Adding a New Smoothing Atom — Checklist

1. Set `smoothing_flags` — at minimum `SMOOTH_BITMASK` or `SMOOTH_BITMASK_CARDINALS`
2. Set `smoothing_groups` — what this atom is
3. Set `smoothing_list` — what this atom connects to (include own group)
4. Add `SMOOTH_BORDER` if it should connect to map edges
5. Add `SMOOTH_OBJ` (or include any `S_OBJ` group in `smoothing_list`) if it connects to objects
6. Provide all required bitmask icon states in the DMI (`[base]-0` through `[base]-255` for full bitmask)
7. Call `QUEUE_SMOOTH(src)` or `QUEUE_SMOOTH_NEIGHBORS(src)` when the atom is placed or a neighbor changes
8. Keep `smoothing_list` and `smoothing_groups` values sorted ascending — CI will fail otherwise

---

## Part 2 — Appearance Caching System

### The Core Problem

BYOND Appearance objects are immutable engine-side structs. Every unique combination of icon + icon_state + color + transform + overlays + alpha + dir is a distinct Appearance. Creating many identical Appearances wastes memory and causes redundant network sends to clients.

The caching system ensures that identical visual configurations share the same Appearance object.

### iconstate2appearance and icon2appearance

Defined in `code/controllers/subsystem/overlays.dm`:

```dm
/proc/iconstate2appearance(icon, iconstate)
    var/static/image/stringbro = new()
    stringbro.icon = icon
    stringbro.icon_state = iconstate
    return stringbro.appearance  // returns the immutable Appearance object

/proc/icon2appearance(icon)
    var/static/image/iconbro = new()
    iconbro.icon = icon
    return iconbro.appearance
```

**Key mechanism:** `static` — the image datum is created once at first call and reused forever. Setting `.icon` and `.icon_state` on it then reading `.appearance` causes BYOND to return (or create once and cache) the canonical Appearance for that combination. Subsequent calls with the same icon+state return the same Appearance object — no new allocations.

**Use these instead of:** inline `image()` creation in overlay lists, or string icon_state names passed directly to `overlays +=`.

### build_appearance_list

```dm
/atom/proc/build_appearance_list(build_overlays)
```

Converts a mixed list of strings (icon_state names), icon objects, and existing Appearances into a list of proper Appearance objects. Strings are converted via `iconstate2appearance(src.icon, overlay)`. Icon objects are converted via `icon2appearance(overlay)`.

**Always call this before passing overlays to `overlays +=`** — raw strings in the overlay list are valid but bypass the cache and generate new Appearances each time.

### SSoverlays — Overlay Management

`SSoverlays` is `SS_NO_FIRE | SS_NO_INIT` — it never runs. It is a **stat collection and proc host only**:

- Hosts `add_overlay`, `cut_overlay`, `cut_overlays`, `copy_overlays` procs on `/atom`
- Collects timing stats per type into `SSoverlays.stats`, written to `overlay.log` on shutdown
- Provides `overlays2text` debug helper

The actual overlay list is `atom.overlays` — a BYOND built-in. `POST_OVERLAY_CHANGE(src)` (called after every mutation) notifies the engine.

### SSvis_overlays — Vis Contents Cache

`SSvis_overlays` caches `/obj/effect/overlay/vis` objects used in `vis_contents`. These are shared across atoms that need the same visual.

```dm
SSvis_overlays.add_vis_overlay(thing, icon, iconstate, layer, plane, dir, alpha, add_appearance_flags)
```

- Cache key: `"[icon]|[iconstate]|[layer]|[plane]|[dir]|[alpha]|[add_appearance_flags]"`
- If a matching overlay exists and is still in use (`unused = 0`), it is reused — the vis object is shared across all atoms that need it
- `unique = TRUE` bypasses the cache — use for per-instance overlays that differ between atoms
- Fires every 1 minute to GC expired overlays (those with `vis_locs` empty for longer than `cache_expiration`)
- `managed_vis_overlays` list on the atom tracks which vis overlays it currently holds, for clean removal

### SSdamoverlays — Damage Overlay Processing

`SSdamoverlays` processes human damage overlays asynchronously. Mobs call `START_PROCESSING(SSdamoverlays, src)` when damage state changes; the subsystem calls `update_damage_overlays_real()` on them in batches with tick-checking, then calls `STOP_PROCESSING` to remove them from the queue.

Pattern: damage overlay updates are deferred out of the damage proc itself to avoid per-hit overlay churn.

### Layer and Plane Constants

All layer and plane values are defined in `code/__DEFINES/layers.dm`. Key rules:

- Layers control draw order within a plane (higher = on top). Keep sorted ascending.
- Planes are integer buckets. All atoms on the same plane are composited together before being drawn over lower planes.
- Plane masters (`PLANE_MASTER` flag) apply shaders/effects to their entire plane group.
- **Never use raw numbers** — always use the named defines. The layer table has 70+ entries; collisions are common when using magic numbers.

Key plane ranges:

| Range | Purpose |
|---|---|
| −200 to −10 | World geometry (space, floor, wall, game plane) |
| −9 to −1 | Game plane variants (upper, lower, FOV hidden) |
| 0 | Blackness / darkness |
| 50–110 | Landmarks, area, massive objects, ghosts, weather, indoor |
| 120–200 | Lighting, reflections, fog, emissives |
| 250–251 | Chat (runechat, balloon) |
| 500 | Fullscreen effects |
| 1000–1100 | HUD |
| 5000 | Lobby |
| 9999 | Splash screen |

### Appearance Caching — Rules for Developers

**Always:**
- Use `iconstate2appearance(icon, state)` for static overlay icons — one Appearance per unique combo
- Use `build_appearance_list()` before assigning to `overlays +=`
- Use `SSvis_overlays.add_vis_overlay()` for vis_contents entries — never create raw `/obj/effect/overlay/vis` manually
- Use named layer/plane defines from `layers.dm` — never magic numbers
- Cache appearance results as `var/static` in proc scope when the same overlay is applied repeatedly:
  ```dm
  /atom/proc/add_fire_overlay()
      var/static/fire_appearance = iconstate2appearance('icons/effects/fire.dmi', "fire")
      overlays += fire_appearance
  ```

**Never:**
- Call `overlays +=` with a string icon_state name in a per-tick or high-frequency context
- Create `new /image(...)` inline in a processing loop for each atom
- Use raw `vis_contents +=` with manually created overlay objects — always go through `SSvis_overlays`
- Use `overlays +=` / `overlays -=` on many atoms per tick — batch or use `managed_overlays` pattern

### Performance Relationship

Icon smoothing and appearance caching interact directly with the performance hazards documented in `ai_navigation/performance_gotchas.md` §7:

- Every `overlays +=` with a non-cached Appearance registers a new Appearance in the engine and sends it to all nearby clients
- `QUEUE_SMOOTH_NEIGHBORS` on a busy tile queues up to 8 atoms — if this happens in a loop, 8× the smoothing cost per iteration
- `smooth_zlevel(z, now=TRUE)` — the `now=TRUE` variant blocks the current proc until all smoothing is done; only safe in `Initialize()` or admin tools, never in `fire()` or player-triggered procs

---

## File Map

| File | Purpose |
|---|---|
| `code/controllers/subsystem/icon_smooth.dm` | SSicon_smooth — queue owner, fire loop |
| `code/controllers/subsystem/overlays.dm` | SSoverlays — `iconstate2appearance`, `icon2appearance`, `build_appearance_list`, `add_overlay`, `cut_overlay` |
| `code/controllers/subsystem/vis_overlays.dm` | SSvis_overlays — vis_contents overlay cache |
| `code/controllers/subsystem/damoverlays.dm` | SSdamoverlays — async damage overlay updates |
| `code/__DEFINES/icon_smoothing.dm` | `SMOOTH_*` flags, smoothing groups, `QUEUE_SMOOTH`, `QUEUE_SMOOTH_NEIGHBORS`, `SETUP_SMOOTHING` |
| `code/__HELPERS/icon_smoothing.dm` | `smooth()`, `set_smoothed_icon_state()`, `set_neighborlays()`, `smooth_zlevel()` |
| `code/__DEFINES/layers.dm` | All layer and plane constants |

*Cross-references:*
- *Overlay performance hazards: `ai_navigation/performance_gotchas.md` §7*
- *Appearance accumulation and network cost: `ai_navigation/engine_limits.md` §Overlays and Appearance*
- *GAGS runtime icon generation: `ai_navigation/visuals_guide.md` §GAGS*
- *Planes, filters, render relays: `ai_navigation/visuals_guide.md`*
