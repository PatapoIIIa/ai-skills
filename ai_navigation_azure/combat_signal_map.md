# Combat Signal Map

Generated for Azure-Peak. Use this file when melee, unarmed, projectile, disarm, or combat-target behavior is routed through both core procs and DCS signals.

## Canonical Combat Contracts

Start from these files before opening random weapon or mob subtypes:

| Flow | Open first |
|---|---|
| Held item combat | `code/_onclick/item_attack.dm` |
| Unarmed and hand attacks | `code/_onclick/other_mobs.dm` |
| Living defense / grabs | `code/modules/mob/living/living_defense.dm`, `code/modules/mob/living/grabbing.dm` |
| Human-specific defense/species logic | `code/modules/mob/living/carbon/human/human_defense.dm`, `code/modules/mob/living/carbon/human/species.dm` |
| Projectile combat | `code/modules/projectiles/projectile.dm` |
| Special intents and clash | `code/modules/mob/living/combat/**` |

## Held Item Combat Contract

| Phase | Main proc | Core signals |
|---|---|---|
| Self use | `attack_self` | `COMSIG_ITEM_ATTACK_SELF` |
| Pre attack | `pre_attack` | `COMSIG_ITEM_PRE_ATTACK` |
| Target attackby | target `attackby` | `COMSIG_ATOM_ATTACKBY` |
| Item-side attack | item `attack` | `COMSIG_ITEM_ATTACK`, `COMSIG_MOB_ITEM_ATTACK` |
| After attack | `afterattack` | `COMSIG_ITEM_AFTERATTACK`, `COMSIG_MOB_ITEM_AFTERATTACK` |
| Deleted target cleanup | `attack_qdeleted` | `COMSIG_ITEM_ATTACK_QDELETED` |
| Special attack effect | `do_special_attack_effect` | `COMSIG_ITEM_ATTACK_EFFECT` |

## Unarmed And Hand Attack Contract

| Branch | Core signals |
|---|---|
| Early unarmed gate | `COMSIG_HUMAN_EARLY_UNARMED_ATTACK` |
| Main unarmed melee | `COMSIG_HUMAN_MELEE_UNARMED_ATTACK` |
| Target hand hook | `COMSIG_ATOM_ATTACK_HAND`, `COMSIG_MOB_ATTACK_HAND` |
| Disarm branch | `COMSIG_HUMAN_DISARM_HIT` |
| Animal/living-side attack variants | `COMSIG_ATOM_ATTACK_ANIMAL` |

## Projectile Combat Contract

| Phase | Core signals |
|---|---|
| Projectile fire | `COMSIG_PROJECTILE_BEFORE_FIRE` |
| Pre-hit validation | `COMSIG_PROJECTILE_PREHIT` |
| Hit | `COMSIG_PROJECTILE_ON_HIT`, `COMSIG_PROJECTILE_SELF_ON_HIT` |

Projectile travel overlaps with movement and bump behavior. If pathing or thrown-object travel looks wrong, add `ai_navigation/movement_signal_map.md`.

## Target Selection And AI Combat Coordination

`COMSIG_COMBAT_TARGET_SET` is defined in `code/__DEFINES/components.dm`. Current scan found senders in:

| File | Use |
|---|---|
| `code/datums/ai/subtrees/human_basic_attack.dm` | Sends target-set state during human NPC melee behavior. |
| `code/datums/ai/subtrees/bow_usage.dm` | Sends target-set state during bow behavior. |

## Cheap Search Order

1. Open `code/_onclick/item_attack.dm` for held items or weapon effects.
2. Open `code/_onclick/other_mobs.dm` for punches, bites, hand attacks, and disarms.
3. Open `code/modules/projectiles/projectile.dm` for ranged or spell-projectile behavior.
4. Open `code/modules/mob/living/combat/**` for special intents and clash.
5. Open the exact weapon, mob, or species subtype.
6. Search `RegisterSignal(` for the relevant `COMSIG_*ATTACK*`, `COMSIG_*HIT*`, or projectile family.

## Fast Search Patterns

```sh
rg -n "^#define COMSIG_.*(ATTACK|COMBAT|MELEE|PROJECTILE|HIT|PARRY|BLOCK|DODGE|BULLET|THROW|DISARM)" code/__DEFINES -g "*.dm"
rg -n "COMSIG_.*(ATTACK|COMBAT|MELEE|PROJECTILE|HIT|DISARM)" code modular -g "*.dm"
rg -n "/(attack_self|pre_attack|attackby|attack|afterattack|attack_qdeleted|do_special_attack_effect)\(" code/_onclick code/modules -g "*.dm"
rg -n "/(fire|on_hit)\(" code/modules/projectiles -g "*.dm"
```
