# Spell Signal Map

Generated for Azure-Peak. Use this file when a spell, miracle, rituos effect, or cooldown-based magical ability is routed through both core procs and DCS signals.

## Canonical Spell Contract

Start from `code/modules/spells/spell_cooldown.dm` for `/datum/action/cooldown/spell`. The legacy `code/modules/spells/spell.dm` still exists, but the cooldown spell lifecycle and current spell COMSIG senders are in `code/modules/spells/spell_cooldown.dm`.

Base proc chain:

1. `Trigger`
2. `set_click_ability`
3. `PreActivate`
4. `Activate`
5. `before_cast`
6. `cast`
7. `after_cast`
8. `reset_spell_cooldown`

## Core Signal Order

| Phase | Sender | Signal(s) | Notes |
|---|---|---|---|
| Click ability armed | `set_click_ability` | `COMSIG_MOB_SPELL_ACTIVATED` | Owner-side veto/retrigger coordination. |
| Pre-cast | `before_cast` | `COMSIG_SPELL_BEFORE_CAST`, `COMSIG_MOB_BEFORE_SPELL_CAST` | Return `SPELL_CANCEL_CAST`, `SPELL_NO_FEEDBACK`, `SPELL_NO_IMMEDIATE_COOLDOWN`, or `SPELL_NO_IMMEDIATE_COST`. |
| Main cast | `cast` | `COMSIG_SPELL_CAST`, `COMSIG_MOB_CAST_SPELL` | Main cast event and owner-side reactions. |
| After-cast | `after_cast` | `COMSIG_SPELL_AFTER_CAST`, `COMSIG_MOB_AFTER_SPELL_CAST` | Cleanup and post-success effects. |
| Cooldown reset | `reset_spell_cooldown` | `COMSIG_SPELL_CAST_RESET` | Explicit cooldown rollback/recovery. |
| Invocation | `invocation` | `COMSIG_MOB_PRE_INVOCATION` | Listener can mutate invocation message/type list. |
| Projectile hit | `code/modules/spells/spell_cooldown_projectile.dm` `on_cast_hit` | `COMSIG_SPELL_PROJECTILE_HIT` | Projectile spell subtype branch. |
| Touch hand hit | `code/modules/spells/spell_touch.dm` `do_hand_hit` | `COMSIG_SPELL_TOUCH_HAND_HIT` | Touch spell subtype branch. |

## Active Spell Signal Defines

| File | Signals |
|---|---|
| `code/__DEFINES/dcs/signals/signals_spell.dm` | `COMSIG_MOB_BEFORE_SPELL_CAST`, `COMSIG_SPELL_BEFORE_CAST`, `COMSIG_MOB_SPELL_ACTIVATED`, `COMSIG_MOB_CAST_SPELL`, `COMSIG_SPELL_CAST`, `COMSIG_MOB_AFTER_SPELL_CAST`, `COMSIG_SPELL_AFTER_CAST`, `COMSIG_SPELL_CAST_RESET`, `COMSIG_MOB_PRE_INVOCATION`, `COMSIG_SPELL_PROJECTILE_HIT`, `COMSIG_SPELL_TOUCH_HAND_HIT` |

## Known Current Listeners / Extensions

| File | Signal use |
|---|---|
| `code/datums/actions/action_cooldown.dm` | Registers `COMSIG_MOB_SPELL_ACTIVATED` for retrigger cancellation. |
| `code/modules/spells/spell_cooldown.dm` | Sends generic spell lifecycle signals. |
| `code/modules/spells/spell_cooldown_projectile.dm` | Sends `COMSIG_SPELL_PROJECTILE_HIT`. |
| `code/modules/spells/spell_touch.dm` | Sends `COMSIG_SPELL_TOUCH_HAND_HIT`. |

## Cheap Search Order

1. Open `code/modules/spells/spell_cooldown.dm`.
2. Open `code/__DEFINES/dcs/signals/signals_spell.dm`.
3. Open the concrete spell subtype under `code/modules/spells/**`.
4. Search `RegisterSignal(` for the relevant `COMSIG_*SPELL*`.
5. Then widen into components, owner mob code, or status effects.

## Fast Search Patterns

```sh
rg -n "COMSIG_.*SPELL|COMSIG_MOB_PRE_INVOCATION" code/__DEFINES/dcs/signals/signals_spell.dm
rg -n "COMSIG_SPELL_|COMSIG_MOB_.*SPELL|COMSIG_MOB_PRE_INVOCATION" code modular -g "*.dm"
rg -n "/(Trigger|set_click_ability|PreActivate|Activate|before_cast|cast|after_cast|reset_spell_cooldown)\(" code/modules/spells code/datums/actions -g "*.dm"
```
