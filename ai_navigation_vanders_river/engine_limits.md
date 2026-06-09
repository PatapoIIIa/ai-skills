# Engine Limits

Extracted from the BYOND/Dream Maker Designer's Guide. These are hard constraints of the Dream Daemon runtime — not project conventions.

## Tick System

| Variable | Default | Notes |
|---|---|---|
| `world.tick_lag` | `1` (= 0.1 sec) | Smallest meaningful time unit. Decreasing it costs CPU; below a viable threshold the overhead makes the server *slower*, not faster. |
| `world.cpu` | — | Percentage of tick budget consumed. **≥100 = server is in overtime; player input backlogs.** |
| Client command rate | 1 cmd/tick | Clients are hard-limited to one command per tick. Increasing `tick_lag` reduces input flood at the cost of responsiveness. |
| Minimum sleep/spawn | 1 tick | `sleep(0)` and `spawn(0)` still cost at least one tick. Use them to yield, not for zero-delay work. |

**Rule of thumb:** `world.cpu` is the single best real-time health gauge. Values routinely above 80 are a warning; above 100 means the game is visibly lagging.

## Threading Model

- DM is **single-threaded**. Only one procedure runs at a time.
- `sleep` and `spawn` are the only ways to yield control back to the scheduler.
- An infinite loop that **never sleeps** is detected by the engine and **aborted automatically** to prevent the world from locking up. Do not rely on this as a safety net — it is a last resort, not a feature.
- After any `sleep`, assume any object reference may have become `null` (the object could have been deleted during the pause). Always null-check after resuming. Exception: if the sleeping proc's `src` is deleted, the proc is **cancelled automatically**.

## View and Map

| Limit | Value |
|---|---|
| Default view range (`world.view`) | `5` → 11×11 viewport |
| Maximum view range | `10` → 21×21 viewport |
| Map coordinates | `world.maxx`, `world.maxy`, `world.maxz` (default 0; any nonzero sets others to 1) |
| `luminosity` range | `0–6` (areas only are luminous by default) |
| `walk_to` / `step_to` effective range | **≤ `world.view * 2 + 1` tiles (default: 11).** Silent no-op if the target is farther — no error, no log entry, the mob simply does not move. |

`view()` is a high-level built-in optimised inside the VM — calling it is cheap relative to manually iterating the same region. Prefer it over manual coordinate sweeps.

## Numeric Limits

| Limit | Value |
|---|---|
| Bitwise integer range | 0–65535 (16-bit unsigned). Values outside this range are **truncated silently**. |
| `world.time` / `world.realtime` | Measured in **tenths of seconds**. All `sleep`/`spawn` delays use the same unit. |

## Memory and Garbage Collection

- DM variables hold either **numbers** (copied by value) or **references** (pointer-like; copying only copies the reference, not the data).
- The engine provides **automatic garbage collection**: when no variable references a piece of data, it is freed. There is no manual `free()`.
- GC is not instantaneous. Large numbers of short-lived objects (e.g. temporary lists, spawned datums) can create GC pressure between ticks.
- Special lists (`contents`, `overlays`, `underlays`) are managed by the engine and **do not support associative values**.

## Lists

- Accessing an index beyond `list.len` **crashes the procedure** (runtime error to `world.log`).
- `list + list2` creates a **new list** (allocation cost). `list += list2` modifies in place (cheaper when a new reference is not needed).
- `for(X in list)` internally takes a **temporary copy** of the list at loop start — safe for most cases but has a copy cost.
- **Exception:** `world.contents` is explicitly excluded from the auto-copy behavior. Do **not** iterate `world.contents` while simultaneously creating or destroying objects.

## Overlays and Appearance

- `overlays` and `underlays` are engine-managed lists on every atom. They hold icon references or object type paths.
- Each distinct combination of icon/state/color/transform that the engine tracks is an internal **Appearance object**. The guide does not give a numeric cap, but Appearance objects accumulate in the server's memory until GC cycles. Excessive unique overlay combinations (e.g. per-player dynamic overlays that vary by many parameters) pressure both memory and network — each changed Appearance must be sent to every client that can see it.
- `flick()` triggers a temporary icon-state transition. It does not change `icon_state` permanently and does not create a new persistent Appearance object.

## Network

- The BYOND client/server protocol transmits resource files automatically on demand. Large icon files sent to many clients simultaneously create bandwidth spikes.
- `world << output` broadcasts to all connected clients. Prefer targeted sends (`mob << output`) where possible.
- Network lag and server lag are distinct: check `world.cpu` to distinguish. High CPU → server lag. Low CPU but sluggish → network lag.

## Virtual Machine Overhead

- DM compiles to **virtual byte code** (not native machine code). Every instruction carries a small VM overhead vs. C/C++.
- High-level built-ins (`view()`, type introspection, path operations) are internally optimised in the VM and can be *faster* in practice than equivalent DM loops.
- This means: prefer built-ins over hand-rolled loops for spatial/type queries.

## Object Lifecycle and `del`

- Calling `del object` (or `qdel()` in tgstation-style code) destroys the object and **automatically sets all existing variable references to it to `null`**. There are no dangling pointers in DM.
- This is why null-checks after `sleep()` are necessary: the object you held a reference to may have been deleted during the pause, leaving the variable as `null`.
- The inverse also applies: after a `del`, code elsewhere that still holds a reference will silently get `null` on next access rather than crashing outright — but then accessing a variable *on* that null reference **will** crash the proc. Always guard with `if(!myobj) return` after any sleep or async gap.
- `Del()` proc (the DM hook) is called *before* the object is actually destroyed. The parent `..()` call performs the real deletion. If you override `Del()`, always call `..()` at the end.
- **Areas are singletons:** the same area object is shared across all turfs it covers. `New()` fires only once, not once per turf placement.

```dm
// Pattern: safe reference use after sleep
var/obj/myitem = get_item()
sleep(10)
if(!myitem) return   // deleted during sleep — bail out
myitem.do_thing()
```

---

*Cross-references: → `performance_gotchas.md` for situation-by-situation hazards. → `router.md` for task dispatch. → `processing_hazards.md` for subsystem freeze diagnosis. → `visuals_guide.md` for appearance/overlay/plane/filter system details. → `coding_standards.md` for GC patterns, harddel fixes, and `Destroy()` contract.*
