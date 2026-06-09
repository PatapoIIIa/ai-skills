# Type Index

Generated for Azure-Peak. Use this file when the task gives a BYOND type path and you need the cheapest route before opening the full `ai_navigation/type_tree.md`.

## Major Roots

| Root | Usually means | Open first |
|---|---|---|
| `/datum` | logic/state/controller datums | `code/datums/**`, `code/controllers/**`, feature-local datums under `code/modules/**` |
| `/mob` | player/NPC lifecycle and behavior | `code/modules/mob/**` |
| `/obj` | items, structures, effects, machinery, map objects | `code/game/objects/**`, `code/game/machinery/**`, feature modules in `code/modules/**` |
| `/atom` | shared atom behavior, appearance, interaction glue | `code/game/atoms.dm`, `code/game/atoms_movable.dm` |
| `/area` | area definitions and area-level behavior | `code/game/area/**` |
| `/turf` | world tiles, terrain, map logic | `code/game/turfs/**` |
| `/client` | client hooks and verbs | `code/modules/client/**`, `code/_onclick/**` |
| `/world` | bootstrap and global startup | `code/world.dm`, `code/controllers/master.dm` |

## High-Value Branches

| Type branch | Open first | Then check |
|---|---|---|
| `/datum/controller/subsystem/...` | `code/controllers/subsystem/**`, `modular/code/controllers/subsystem/**` | `ai_navigation/subsystem_map.md`, `code/controllers/master.dm` |
| `/datum/antagonist/...` | `code/modules/antagonists/**` | `code/modules/events/antagonist/**`, `code/datums/migrants/**` |
| `/datum/action/...` | `code/modules/spells/**`, `code/datums/actions/**` | `ai_navigation/spell_signal_map.md`, `code/datums/status_effects/**` |
| `/datum/status_effect/...` | `code/datums/status_effects/**` | `code/modules/spells/**`, `code/datums/components/**`, `code/datums/elements/**` |
| `/datum/component/...` | `code/datums/components/**` | `code/__DEFINES/dcs/**`, `code/__DEFINES/components.dm`, `ai_navigation/signal_map.md` |
| `/datum/element/...` | `code/datums/elements/**` | `code/__DEFINES/dcs/**`, `ai_navigation/signal_map.md` |
| `/datum/ai_controller/...` or `/datum/ai_behavior/...` | `code/datums/ai/**` | `code/modules/mob/**`, `ai_navigation/subsystem_map.md` |
| `/datum/storyteller/...`, `/datum/round_event_control/...`, `/datum/round_event/...` | `code/datums/storytellers/**`, `code/modules/events/**` | `SSgamemode`, `SSevents`, `SSticker` |
| `/datum/migrant_wave/...` or `/datum/migrant_role/...` | `code/datums/migrants/**` | `code/modules/jobs/**`, `SSmigrants` |
| `/datum/skill/...` | `code/datums/skills/**`, `code/datums/skill_holder.dm` | `SSskills`, job spawn files |
| `/datum/patron/...` or god/faith data | `code/datums/gods/**` | `SSskills`, `SSmood` |
| `/datum/quest/...`, `/datum/component/quest_object` | `code/modules/roguetown/roguemachine/questing/**` | `code/__DEFINES/questing.dm` |
| `/datum/special_intent/...` | `code/modules/mob/living/combat/special_intents.dm` | `code/modules/mob/living/combat/azure_combat.dm` |
| `/mob/living/...` | `code/modules/mob/living/**` | feature modules touching that mob family |
| `/mob/dead/new_player` | `code/modules/mob/dead/**` | `SSjob`, `SSticker` |
| `/obj/item/...` | `code/game/objects/items/**` or matching feature module | `code/modules/**`, `modular/**` |
| `/obj/structure/...` | `code/game/objects/structures/**` | mapping, events, or feature module that owns the structure |
| `/obj/effect/...` | `code/game/objects/effects/**` | mapping landmarks, event spawners, temporary visuals |

## Cheap Rules

- Start with this file, not `ai_navigation/type_tree.md`, unless inheritance depth itself is the problem.
- If the branch maps to a row above, open that directory before doing a repo-wide search.
- After locating a core branch in `code/`, check whether `modular` extends the same type path.
- Use `ai_navigation/entrypoints.md` for feature names, and `ai_navigation/subsystem_map.md` for SS ownership.
