# Movement Signal Map

Generated for Azure-Peak from active `COMSIG_*` defines and real `SEND_SIGNAL`/`RegisterSignal` references in `code/**` and `modular/**`.

- Movement-related signals detected: **42**
- Signals with real `SEND_SIGNAL` senders: **23**
- Signals used by `RegisterSignal`/`UnregisterSignal`: **21**
- Use direct procs for client input, pull/grab state, and movetype changes.

## Canonical Entry Files

| Flow | Open first | Notes |
|---|---|---|
| Client input | `code/modules/mob/mob_movement.dm` | `/client/Move` gates input directly; no client movement COMSIGs are emitted. |
| Movable movement | `code/game/atoms_movable.dm` | `Move`, `Moved`, `Cross`, `Crossed`, `Bump`, throw setup, pull helpers. |
| Living movement | `code/modules/mob/living/living_movement.dm` | Living-side movement consequences. |
| Pull/grab state | `code/game/atoms_movable.dm`, `code/modules/mob/living/living.dm`, `code/modules/mob/living/grabbing.dm` | Pulling is direct proc state, not a pull COMSIG family. |
| Buckle/riding | `code/game/objects/buckling.dm`, `code/datums/components/riding.dm` | Buckle uses active movable buckle COMSIGs. |
| Throwing | `code/controllers/subsystem/throwing.dm`, `code/game/atoms_movable.dm` | `SSthrowing` processes `datum/thrownthing`; pre/post throw emit, throw landed is not emitted in current code. |
| Moveloops | `code/controllers/subsystem/movement/movement_loop.dm`, `code/controllers/subsystem/movement/move_manager.dm`, `code/controllers/subsystem/movement/movement_types.dm` | `SSmovement` owns loop-driven movement. |

## Core Signal Status

| Signal | Azure-Peak status | Primary files |
|---|---|---|
| `COMSIG_MOVABLE_PRE_MOVE` | defined + emitted | `code/__DEFINES/components.dm` |
| `COMSIG_MOVABLE_MOVED` | defined + emitted | `code/__DEFINES/components.dm` |
| `COMSIG_MOVABLE_CROSS` | defined + emitted | `code/__DEFINES/components.dm` |
| `COMSIG_MOVABLE_CROSSED` | defined + emitted | `code/__DEFINES/components.dm` |
| `COMSIG_MOVABLE_UNCROSSED` | defined/listened; no sender in current scan | `code/__DEFINES/components.dm` |
| `COMSIG_MOVABLE_BUMP` | defined + emitted | `code/__DEFINES/components.dm` |
| `COMSIG_MOVABLE_UPDATE_GLIDE_SIZE` | defined + emitted | `code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm` |
| `COMSIG_MOVABLE_Z_CHANGED` | defined + emitted | `code/__DEFINES/components.dm` |
| `COMSIG_MOVABLE_IMPACT` | defined + emitted | `code/__DEFINES/components.dm` |
| `COMSIG_MOVABLE_IMPACT_ZONE` | defined + emitted | `code/__DEFINES/components.dm` |
| `COMSIG_MOVABLE_PRE_THROW` | defined + emitted | `code/__DEFINES/components.dm` |
| `COMSIG_MOVABLE_POST_THROW` | defined + emitted | `code/__DEFINES/components.dm` |
| `COMSIG_MOVABLE_THROW_LANDED` | defined/listened; no sender in current scan | `code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm` |
| `COMSIG_MOVABLE_PREBUCKLE` | defined + emitted | `code/__DEFINES/dcs/signals/signals_movable.dm` |
| `COMSIG_MOVABLE_BUCKLE` | defined + emitted | `code/__DEFINES/dcs/signals/signals_movable.dm` |
| `COMSIG_MOVABLE_UNBUCKLE` | defined + emitted | `code/__DEFINES/dcs/signals/signals_movable.dm` |
| `COMSIG_RIDDEN_DRIVER_MOVE` | defined/listened; no sender in current scan | `code/__DEFINES/dcs/signals/signals_movable.dm` |
| `COMSIG_MOVELOOP_START` | defined + emitted | `code/__DEFINES/dcs/signals/signals_moveloop.dm` |
| `COMSIG_MOVELOOP_STOP` | defined + emitted | `code/__DEFINES/dcs/signals/signals_moveloop.dm` |
| `COMSIG_MOVELOOP_PREPROCESS_CHECK` | defined + emitted | `code/__DEFINES/dcs/signals/signals_moveloop.dm` |
| `COMSIG_MOVELOOP_POSTPROCESS` | defined + emitted | `code/__DEFINES/dcs/signals/signals_moveloop.dm` |
| `COMSIG_MOVELOOP_JPS_REPATH` | defined; no sender in current scan | `code/__DEFINES/dcs/signals/signals_moveloop.dm` |

## Additional Movable/Moveloop Signals

| Signal | Azure-Peak status | Primary files |
|---|---|---|
| `COMSIG_MOVABLE_BUMP_PUSHED` | defined/listened; no sender in current scan | `code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm` |
| `COMSIG_MOVABLE_DISPOSING` | defined; no sender in current scan | `code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm` |
| `COMSIG_MOVABLE_HEAR` | defined + emitted | `code/__DEFINES/components.dm` |
| `COMSIG_MOVABLE_LIGHT_OVERLAY_SET_COLOR` | defined; no sender in current scan | `code/__DEFINES/dcs/signals_atoms/movable_lighting.dm` |
| `COMSIG_MOVABLE_LIGHT_OVERLAY_SET_POWER` | defined; no sender in current scan | `code/__DEFINES/dcs/signals_atoms/movable_lighting.dm` |
| `COMSIG_MOVABLE_LIGHT_OVERLAY_SET_RANGE` | defined; no sender in current scan | `code/__DEFINES/dcs/signals_atoms/movable_lighting.dm` |
| `COMSIG_MOVABLE_LIGHT_OVERLAY_TOGGLE_ON` | defined; no sender in current scan | `code/__DEFINES/dcs/signals_atoms/movable_lighting.dm` |
| `COMSIG_MOVABLE_SECLUDED_LOCATION` | defined + emitted | `code/__DEFINES/components.dm` |
| `COMSIG_MOVABLE_SET_GRAB_STATE` | defined; no sender in current scan | `code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm` |
| `COMSIG_MOVABLE_TURF_ENTERED` | defined + emitted | `code/__DEFINES/dcs/signals/signals_turf.dm` |
| `COMSIG_MOVABLE_TURF_EXITED` | defined + emitted | `code/__DEFINES/dcs/signals/signals_turf.dm` |

## Practical Routing

- For player input bugs, start at `/client/Move` in `code/modules/mob/mob_movement.dm`.
- For successful-step side effects, use `COMSIG_MOVABLE_MOVED` listeners and the `Moved()` sender in `code/game/atoms_movable.dm`.
- For pull/drag behavior, inspect `start_pulling`, `stop_pulling`, `Move_Pulled`, and `can_be_pulled`.
- For movetype changes, inspect `setMovetype()` and direct `movement_type` bitfield writes.
- Treat `COMSIG_MOVABLE_THROW_LANDED` and `COMSIG_MOVABLE_UNCROSSED` carefully: they are defined/listened in places, but this scan did not find a core `SEND_SIGNAL` sender in Azure-Peak.

## Fast Search Patterns

```sh
rg -n "COMSIG_(MOVABLE|MOVELOOP|RIDDEN_DRIVER_MOVE)" code modular -g "*.dm"
rg -n "start_pulling|stop_pulling|Move_Pulled|can_be_pulled" code modular -g "*.dm"
rg -n "SEND_SIGNAL\(.*COMSIG_MOVABLE|RegisterSignal\(.*COMSIG_MOVABLE" code modular -g "*.dm"
```
