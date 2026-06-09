# Azure Modular Guide

`modular/` is a late-included overlay and content-pack layer for Azure-Peak.

## What Late-Included Means

`modular/` is included by `roguetown.dme` after most core `code/**` includes. This means:

- it can add descendants under existing core type paths;
- it can override behavior when a late file defines the same proc path;
- it cannot change the master controller architecture by being in a separate tree;
- core singletons (`SS*`, `Master`) are owned by the core subsystem framework unless a modular file explicitly declares an additional subsystem.

**Agent rule:** locate the core type first in `code/`, then search `modular/` for descendants, overrides, or content that hooks into the same subsystem.

## Directory Map

| Path | What lives here |
|---|---|
| `modular/ambush/**` | Ambush config datums. |
| `modular/code/controllers/configuration/**` | Modular config entries. |
| `modular/code/controllers/subsystem/processing/sex.dm` | `SSsex` processing subsystem. |
| `modular/code/game/objects/**` | Modular objects and items, including lewd/tent/pillory/gallows content. |
| `modular/code/modules/admin/**` | Admin additions. |
| `modular/code/modules/crafting/**` | Modular crafting additions. |
| `modular/code/modules/jobs/**` | Job/role extensions. |
| `modular/code/modules/living/**` | Living speech/emote hooks. |
| `modular/code/modules/maturity-prompt/**` | Maturity prompt code and `SSmaturity_guard`. |
| `modular/Creechers/**` | Creature/content pack. |
| `modular/icons/**` | Modular icon assets. |
| `modular/Mapping/**` | Modular mapping content. |
| `modular/Neu_Farming/**` | Farming content. |
| `modular/Neu_Food/code/**` | Food, cookware, raw/cooked food, drinks, and recipes. |
| `modular/piercing/**` | Piercing content. |
| `modular/ze_genesis_call/**` | Genesis call content. |

## Where New Code Belongs

| Adding... | Put it in |
|---|---|
| New core gameplay behavior | Prefer the owning core path under `code/**`. |
| New modular job extension | `modular/code/modules/jobs/**` if it is genuinely modular; otherwise `code/modules/jobs/**`. |
| New modular crafting addition | `modular/code/modules/crafting/**` or core `code/modules/crafting/**` depending on ownership. |
| New food/cooking item | `modular/Neu_Food/code/**` or `code/modules/food_and_drinks/**`. |
| New ambush config | `modular/ambush/ambush_config/**` or the owning core ambush/threat path if it is not modular content. |
| New modular object/item | `modular/code/game/objects/**`. |
| New subsystem | Avoid unless explicitly approved; add it in the owner layer and update `ai_navigation/subsystem_map.md`. |

## Key Rules

- For overlays/appearance changes, read `ai_navigation/performance_gotchas.md` first; per-tick `overlays +=` changes are expensive.
- After locating a core path, search `modular/` for the same type branch before editing behavior that may be extended late.
