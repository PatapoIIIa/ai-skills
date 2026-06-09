# Runtime Errors and Deletion

Generated on 2026-03-14. Derived from Crispy's "Code Red" BYOND forum guide (post/37193), the project's HARDDELETES.md, and the qdel design post (post/2984475).
This file covers: how to read runtime errors, the most common error types and their fixes, and the theory behind `qdel()` vs raw `del()`.

The navigation layer may lag behind the live documents. If this file and source docs disagree, trust the source docs.

---

## Reading a Runtime Error

Enable debug mode first: Dream Maker → Build → Preferences → tick **Debug mode**. Without it, errors lack file/line information.

```
runtime error: Cannot read null.x
proc name: dd_get_step (/proc/dd_get_step)
source file: Geography.dm,88
usr: Crispy (/mob)
src: null
call stack:
  dd_get_step(null, 1)
  Crispy (/mob): test()
```

| Field | What it tells you |
|---|---|
| First line | **Error type** — the most important line |
| `proc name` | Which proc crashed; `/proc/` prefix = global proc, `/mob/verb/` = verb on mob, etc. |
| `source file` | **File and line number** — go here first |
| `usr` / `src` | Values at crash time — `null` here is itself a clue |
| `call stack` | Full chain of calls that led to the crash; **read bottom-up** — the bottom is the player action, the top is where it died |

**Workflow:**
1. Read the error type.
2. Go to the source file + line.
3. Read the call stack bottom-up to understand how you got there.
4. Check what was `null`, zero, or the wrong type.

---

## Common Runtime Errors

### `Cannot read null.something` / `Cannot modify null.something`

**Most common runtime error.** You accessed a var or called a proc on an object reference that was `null`.

```dm
O.somevar   // crashes if O is null
```

**Common causes:**

- A proc argument was not passed when calling the proc — the parameter is `null` by default.
- An object was deleted between a `sleep()` and the next line that uses it. Always null-check after any `sleep`.
- `src.somevar` accessed inside `Del()` after `..()` — parent call deletes `src`, so vars become inaccessible. Always put `..()` **last** in `Del()`.
- `src.client` is sometimes `null` in `mob/Logout()` — use `client/Del()` instead if you need client vars.

```dm
// Bad — ..() deletes src, then we try to use it
/obj/my_thing/Del()
    ..()
    GLOB.things -= src   // src is gone

// Good
/obj/my_thing/Del()
    GLOB.things -= src
    ..()
```

**After `sleep()` — always null-check:**
```dm
var/mob/target = get_target()
sleep(10)
if (!target)   // may have been deleted during sleep
    return
target.do_thing()
```

### `Type mismatch`

Attempted a math operation on incompatible types (e.g. number + string). Also occurs when you try to add to a list that was never initialized.

Use `num2text()` / `text2num()` to convert. Initialize lists in `Initialize()`, not at type definition level (see `coding_standards.md` §Optimization).

### `Cannot read null.Find()` / `null.Add()` / `null.len`

Operated on a list that doesn't exist yet. An uninitialized list var is `null`, not an empty list.

```dm
// All three create an actual empty list:
var/list/my_list = new()
var/list/my_list = list()
var/my_list[0]   // the zero matters
```

**Important:** If a list var is on a type (not initialized in `New()`/`Initialize()`), **all instances share the same list**. Always initialize per-instance lists in `Initialize()`.

### `List index out of bounds`

Accessed `my_list[n]` where `n < 1` or `n > my_list.len`. Also fires if `pick()` is called on an empty list.

Always guard: `if (my_list.len > 0)` before `pick()` or index access.

### `Undefined variable` / `Undefined proc or verb`

Used the `:` (colon/lax) operator instead of `.` (dot/strict). The `:` operator suppresses compile-time type checking — it is **banned** in this project (see `coding_standards.md`).

If the dot operator produces a compile error, typecast explicitly:
```dm
var/mob/living/carbon/C = target
C.do_thing()   // compiler now knows the type
```

### `Division by zero`

A divisor variable is `0`. Guard before dividing:
```dm
if (divisor == 0)
    return
result = value / divisor
```

### `Maximum recursion level reached`

A proc calls itself (directly or indirectly) without a base case, or a loop runs without a yield. **Do not set `world.loop_checks = 0`** — that makes things worse.

If a proc genuinely needs to call itself on a timer, use `spawn()` or `addtimer()` to detach from the current call stack:
```dm
// Bad — infinite synchronous recursion
/datum/proc/tick()
    do_work()
    tick()   // calls itself immediately

// Good — yields back to the scheduler
/datum/proc/tick()
    do_work()
    addtimer(CALLBACK(src, PROC_REF(tick)), TICK_INTERVAL)
```

If this fires inside a `Stat()` proc, you've written `Stat()` (uppercase) instead of `stat()` (lowercase) — DM is case-sensitive.

### `Bad client`

Called `alert()` or `input()` directed at a mob with no client. By default these target `usr` — verify `usr` has a client, or direct explicitly to a specific mob/client.

### `Bad del`

Tried to `del()` something that can't be deleted: a number, string, or type path. If you want to delete all objects of a type, use `locate()` or a `for` loop.

### `Cannot remove from list`

Tried to remove a type path from a contents list directly. Use `locate()` to get the actual object first:
```dm
// Bad
src.contents -= /mob/living/target_type

// Good
src.contents -= locate(/mob/living/target_type) in src
```

### `Bad icon operation`

Tried an invalid operation on an `/icon` object. Due to a BYOND quirk, this error often lacks file/line info — use the call stack to find the owning proc.

### `Cannot create objects of type /type/path`

Passed a non-type-path value to `new()`. The variable holding the type path is an object, string, or number instead of an actual DM type path literal.

---

## `del()` vs `qdel()` — Why Raw `del()` Is Dangerous

### How BYOND object deletion works

Every object has a reference count. When the count reaches 0, BYOND frees it automatically (GC). The problem is *getting* the count to 0.

`del(obj)` tries to destroy an object immediately. If the object has references BYOND can't clear cheaply (nulling `loc`, clearing `vis_contents`, removing `tag`/`key`, killing sleeping procs, etc.), it falls back to a **brute-force scan of all live memory** — every var on every object, every list index, every sleeping proc's local heap. This is extremely expensive and can silently break code elsewhere that didn't expect the object to disappear mid-execution.

### The three strategies (and why only one is right)

**Strategy 1 — Don't use `del()`, manage refs manually.**
Easy at first, produces hard-to-find memory leaks later. Accumulates indefinitely.

**Strategy 2 — Use `del()` without managing refs.**
Easy for a long time. Eventually causes hard deletions and server performance degradation. Very hard to diagnose because the mess compounds over time.

**Strategy 3 — `qdel()` with a destructor pattern (what this project uses).**
- Calls `Destroy()` on the object, which is responsible for clearing all known references.
- Keeps a soft reference to the object for a known window (~5 minutes).
- If the object still exists after that window, hard-deletes it and **logs the hard deletion** for later investigation.
- Hard deletions are detectable and diagnosable rather than silent.

### The `Destroy()` contract

`Destroy()` has exactly one job: **clear all references to `src`**. No side effects, no game logic.

```dm
/obj/item/my_thing/Destroy()
    GLOB.my_things -= src       // clear global list reference
    if (my_paired_object)
        my_paired_object.partner = null   // clear paired reference
    return ..()                 // ALWAYS call parent, ALWAYS last
```

`qdel()` calls `Destroy()`, then queues the object for GC. If GC can't free it within the soft-delete window, a hard deletion is forced and logged to `[log_dir]/harddels.log`.

### `del()` leaves holes in lists

```dm
// Before del:  list(obj1, obj2, obj3)
del(obj2)
// After del:   list(obj1, null, obj3)  ← hole
```

Any code that assumes `list.len == number of live objects` will now be wrong. **Use `qdel()` and manage references in `Destroy()`** — the list ref gets cleared properly via `Destroy()` before deletion.

### Reference types and when to use each

| Situation | Tool |
|---|---|
| Object you "own" (you created it, you destroy it) | Clear ref in `Destroy()` |
| Two objects own each other | Paired ref pattern — each clears the other's ref in `Destroy()` |
| Object you reference but don't own | `WEAKREF()` — resolves to `null` automatically after deletion |
| Hot reference that can't be weakref'd | `RegisterSignal(target, COMSIG_QDELETING, PROC_REF(clear_ref))` |

Full patterns with code examples: `coding_standards.md` §Garbage Collection and Hard Deletes.

### Diagnosing hard deletes

Enable `REFERENCE_TRACKING_STANDARD` in `_compile_options.dm`. When a hard deletion would occur, the runtime instead performs the memory scan and prints findings to `[log_dir]/harddels.log`. Output identifies:
- Which object holds the surviving reference (if in a var)
- The list traversal path to reach the reference (if in a list)
- Remaining reference count

---

## Quick Reference

| Error | Most likely cause | First thing to check |
|---|---|---|
| `Cannot read null.X` | Object deleted or never assigned | Null-check after `sleep()`; check `Del()` parent call order |
| `Type mismatch` | Math on wrong types or null list | List initialized? Types compatible? |
| `null.Find/Add/len` | List never created | Initialize in `Initialize()` with `list()` or `new()` |
| `List index out of bounds` | Index < 1 or > len | Guard `list.len > 0` before access |
| `Undefined variable/proc` | Colon `:` operator used | Replace `:` with `.`; typecast if needed |
| `Division by zero` | Divisor var is 0 | Guard before dividing |
| `Maximum recursion` | Proc calls itself without yield | Use `addtimer`/`spawn` for self-calling procs |
| Hard deletion logged | `Destroy()` missed a reference | Enable reference tracking; check `Destroy()` coverage |

---

*Cross-references:*
- *Full GC patterns and harddel techniques: `coding_standards.md` §Garbage Collection*
- *Engine-level object lifecycle: `engine_limits.md` §Object Lifecycle and del*
- *`walk()` procs leaving GC references: `coding_standards.md` §BYOND walk procs*
- *Signal-based cleanup pattern: `coding_standards.md` §Garbage Collection*
