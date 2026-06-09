# Failure Modes

Generated on 2026-03-11. Use this file after the owner subsystem or datum family is known, but the exact break mode is still unclear.

## Use This Helper When

- you know which `SS*` or datum family owns the problem
- the symptom is real, but the cause is still ambiguous
- you need to separate `where it breaks` from `how it breaks`

## Scale First

Classify the scope before picking a cause:

- one effect or object is wrong
- one family of effects is wrong
- all effects in the same subsystem freeze
- the whole subsystem stops firing

Larger scope usually means shared ownership or shared execution failure.

## Common Failure Modes

### Whole subsystem or process family freezes

- blocking call in `process()`, `tick()`, `fire()`, or a directly-called proc
- subsystem no longer firing or stuck in the wrong state
- datums dropped from the processing list
- `PROCESS_KILL` returned too early
- early `return`, `pause()`, or bad resume path
- scheduler pressure or starvation

### Single effect or single object gets stuck

- duration or timer never set correctly
- effect never entered the processing list
- `process()` runs, but expiry logic never reaches `qdel()`
- `on_remove()` or cleanup never runs
- refresh/replace semantics hide the real active instance
- the visual or trait cleanup path differs from the lifecycle path

### Proc aborted silently by the engine

**Symptom:** a proc stops executing mid-way with no runtime in `world.log`, or `world.log` shows `"execution terminated"` / `"too many iterations"`. The owning datum is alive, the subsystem is still firing, but the specific proc never completes.

**Cause:** BYOND's VM auto-kills any proc that runs for too long without yielding (no `sleep()`, `spawn()`, or other yielding instruction inside a loop). This is the engine's last-resort guard against infinite loops. It is not a crash — the rest of the world continues running.

**Distinguishers vs. blocking call:**
- Blocking call → the *entire subsystem* stalls until the blocking op returns.
- Engine abort → only the *specific proc instance* dies; the subsystem keeps firing other datums.

**Fix:** Add `sleep(0)` or `spawn()` inside any long-running loop, or move the work into a subsystem `fire()` budget. Never rely on the engine abort as a safety net.

**Search pattern:**
```
rg -n "for\(|while\(" code modular_rmh -g "*.dm" | rg -v "sleep\|spawn\|INVOKE_ASYNC"
```
Cross-reference `ai_navigation/engine_limits.md` §Threading Model and `ai_navigation/performance_gotchas.md` §1.

## Cheap Distinguishers

- `everything froze at once` points to shared execution, not local logic
- `no runtimes` makes blocking or silent scheduler issues more likely
- `effect exists but never clears` points to expiry or cleanup
- `effect vanishes too early` points to replace/refresh or bad `qdel`
- `one proc stopped mid-way, subsystem still firing` → likely engine abort (loop without sleep); check `world.log` for `"execution terminated"`

## Cheap Search Patterns

- owner subsystem state and calls:
  `rg -n "\bSS[A-Z][A-Za-z0-9_]*\b|PROCESS_KILL|pause\(|currentrun|processing \+=" code modular_rmh -g "*.dm"`
- lifecycle and cleanup:
  `rg -n "qdel\(|Destroy\(|on_remove\(|before_remove\(|refresh\(|be_replaced\(" code modular_rmh -g "*.dm"`
- entry into processing:
  `rg -n "START_PROCESSING\(|STOP_PROCESSING\(" code modular_rmh -g "*.dm"`

## Rule Of Thumb

- First identify the owner.
- Then classify the scale of the failure.
- Then test failure modes in this order:
  blocking → engine abort (loop without sleep) → not firing → dropped from list → wrong cleanup → starvation.
