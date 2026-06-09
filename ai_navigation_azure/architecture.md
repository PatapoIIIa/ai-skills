# Architecture Overview

Generated for Azure-Peak. This file explains how the repository is put together and where runtime ownership lives.

## Composition Model

- The project is a BYOND/Dream Maker codebase with a TG-derived linear `.dme` include graph.
- The active project file is `roguetown.dme`.
- The high-level include order is maps/templates, defines, helpers, globalvars, controllers, datums, modules, game atoms/objects, interface, then late modular includes.
- `modular/` is the current overlay/pack layer.
- `modular/` can extend existing type paths and add late content, but it does not replace `Master`, `SS*`, or the core subsystem architecture.

## Runtime Backbone

- `code/world.dm` defines `/world`.
- `code/controllers/master.dm` owns the master controller loop and discovers `/datum/controller/subsystem` subtypes.
- `code/controllers/subsystem.dm` defines the scheduler contract: `init_order`, `wait`, `priority`, flags, runlevels, `Initialize()`, and `fire()`.
- `code/__DEFINES/MC.dm` turns subsystem macros into `SS*` globals and type declarations.
- `SSatoms` is the atom initialization bridge for `Initialize()`, `LateInitialize()`, and mapload diagnostics.

## Domain Layers

| Layer | Current path |
|---|---|
| Compile-time constants, macros, signals | `code/__DEFINES/**` |
| Shared helpers | `code/__HELPERS/**` |
| Global caches and singleton vars | `code/_globalvars/**` |
| Bootstrap and subsystems | `code/controllers/**` |
| Reusable state/logic datums | `code/datums/**` |
| Feature-sliced gameplay | `code/modules/**` |
| Concrete atoms, objects, turfs, areas | `code/game/**` |
| Maps and templates | `_maps/**` |
| BYOND interface files | `interface/**` |
| TypeScript/React frontend | `tgui/**` |
| Late modular overlay and packs | `modular/**` |
| Config/schema/tooling | `config/**`, `SQL/**`, `tools/**`, `bin/**` |

## Core Patterns

- Type-tree inheritance is the main structural unit. Start from `/datum`, `/obj`, `/mob`, `/turf`, `/area`, and `/atom` paths.
- DCS signal-driven composition is pervasive. If behavior appears indirect, search `RegisterSignal`, `SEND_SIGNAL`, `AddComponent`, and `RemoveElement` before assuming a direct proc chain.
- Feature ownership is usually split between `code/datums` for reusable state and `code/modules` for feature logic/content/UI.
- Status effects are common state containers; inspect status effect callers and process hooks directly.
- Map/world behavior is split across `_maps`, mapping modules, `SSmapping`, `SSminor_mapping`, `SSdungeon_generator`, `SSmapgen`, and related environment subsystems.

## Azure Modular Layer

| Current path | Role |
|---|---|
| `modular/ambush/**` | Ambush config pack. |
| `modular/code/controllers/**` | Modular config/subsystem additions, including `SSsex`. |
| `modular/code/game/**` | Modular object/item additions. |
| `modular/code/modules/admin/**` | Admin additions. |
| `modular/code/modules/crafting/**` | Modular crafting additions. |
| `modular/code/modules/jobs/**` | Modular job extensions. |
| `modular/code/modules/living/**` | Living mob speech/emote hooks. |
| `modular/code/modules/maturity-prompt/**` | Maturity prompt and `SSmaturity_guard`. |
| `modular/Creechers/**` | Creature/content pack. |
| `modular/Mapping/**` | Modular mapping content. |
| `modular/Neu_Farming/**` | Modular farming content. |
| `modular/Neu_Food/**` | Food/cooking content. |
| `modular/piercing/**` | Piercing content. |
| `modular/ze_genesis_call/**` | Genesis call content. |

## Frontend and External Integration

- DM-side TGUI backends live under `code/modules/tgui/**`, `code/modules/tgui_input/**`, and `code/modules/tgui_panel/**`.
- TypeScript frontend packages live under `tgui/packages/**`.
- Current UI work routes through TGUI and interface paths.
- Runtime configuration lives under `config/**`; SQL/schema data lives under `SQL/**`; developer tooling lives under `tools/**`, `bin/**`, and root scripts.

## Runtime Ownership Quick Reference

| Domain | Primary owner | Key files |
|---|---|---|
| Combat, hit chain, signals | `SSdcs`, direct combat procs | `code/_onclick/item_attack.dm`, `code/_onclick/other_mobs.dm`, `code/modules/mob/living/combat/**` |
| Movement, collisions, moveloops | `SSmovement`, `SSmove_manager`, `SSdcs` | `code/modules/mob/mob_movement.dm`, `code/game/atoms_movable.dm`, `code/controllers/subsystem/movement/**` |
| Spells, actions, cooldowns | direct action/spell code, `SSskills`, `SSmood` | `code/modules/spells/**`, `code/datums/actions/**`, `code/datums/status_effects/**` |
| AI controllers and NPC behavior | `SSai_controllers`, `SSai_behaviors`, `SSai_movement` | `code/datums/ai/**`, `code/controllers/subsystem/processing/ai_behaviours.dm` |
| Jobs, roles, migrants | `SSjob`, `SSmigrants`, `SSrole_class_handler` | `code/modules/jobs/**`, `code/datums/migrants/**` |
| Antagonists and events | `SSgamemode`, `SSevents`, `SSticker` | `code/modules/antagonists/**`, `code/modules/events/**`, `code/datums/storytellers/**` |
| Economy, treasury, merchants | `SSeconomy`, `SStreasury`, `SSmerchant` | `code/modules/economy/**`, `code/controllers/subsystem/rogue/treasury.dm` |
| Questing | `SSdcs`, `SSroguemachine`, player/ledger flow | `code/modules/roguetown/roguemachine/questing/**`, `code/__DEFINES/questing.dm` |
| Mapping and worldgen | `SSmapping`, `SSminor_mapping`, `SSdungeon_generator`, `SSmapgen` | `_maps/**`, `code/modules/mapping/**`, `code/modules/procedural_mapping/**` |
| UI, browser, TGUI | `SStgui`, `SSchat`, `SSstatpanel` | `code/modules/tgui/**`, `tgui/packages/**`, `interface/**` |
| Overlays and icon smoothing | `SSoverlays`, `SSvis_overlays`, `SSicon_smooth` | `code/controllers/subsystem/overlays.dm`, `code/controllers/subsystem/vis_overlays.dm`, `code/controllers/subsystem/icon_smooth.dm` |
| GC and harddel cleanup | `SSgarbage` | `code/controllers/subsystem/garbage.dm` |
| Round bootstrap and tick loop | `Master`, `SSticker` | `code/controllers/master.dm`, `code/controllers/subsystem/ticker.dm`, `code/world.dm` |
