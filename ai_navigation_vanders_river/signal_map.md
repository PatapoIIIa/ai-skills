# Signal Map

Generated on 2026-03-11. Last full rebuild 2026-03-14. Use this file when behavior is indirect, component-driven, or routed through DCS signals instead of obvious proc calls.

## Disambiguation: Debug vs. Implement

- **Debugging** indirect behavior → start here, then `ai_navigation/combat_signal_map.md`, `spell_signal_map.md`, or `movement_signal_map.md`.
- **Implementing** a new component, element, or signal listener → start at `ai_navigation/content_patterns.md` to pick the right shape, then return here for the signal contract.

## Why This Matters

This repository has a large signal layer:

- `685` `COMSIG_*` defines across `code/__DEFINES/dcs/**` and `code/__DEFINES/components.dm`
- `991` `SEND_SIGNAL(` call sites
- `1209` `RegisterSignal(` call sites
- `668` `UnregisterSignal(` call sites

Signals are a first-class behavior path here, not an edge case.

## Contract-First Helpers

Some systems have stable proc-and-signal contracts and should be read through those contracts first.

- spells and miracles: `ai_navigation/spell_signal_map.md`
- combat and hit chains: `ai_navigation/combat_signal_map.md`
- doll movement, collisions, and moveloops: `ai_navigation/movement_signal_map.md`
- generic hook families: `ai_navigation/core_procs.md`

If a system has a dedicated contract helper, prefer that over this generic map.

## Signal Definition Locations

| Location | What lives there |
|---|---|
| `code/__DEFINES/dcs/signals_atoms/signals_atom.dm` | atom attackby, attack_hand, destruction, integrity, lighting, steam/water hooks |
| `code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm` | pre_move, moved, cross, bump, throw, pull, grab, hear, dispose |
| `code/__DEFINES/dcs/signals_atoms/signals_atom_movement.dm` | moveloop, moveloop step phases |
| `code/__DEFINES/dcs/signals_atoms/signals_atom_mouse.dm` | Click, ShiftClick, CtrlClick, AltClick, MouseDrop, MouseWheel |
| `code/__DEFINES/dcs/signals_atoms/signals_obj.dm` | item equip, item attack self/pre/attack/afterattack, gun fired, quality |
| `code/__DEFINES/dcs/signals_atoms/signals_fuse.dm` | fuse lit/extinguished/cut/end |
| `code/__DEFINES/dcs/signals_atoms/appearance.dm` | update_appearance, update_name, update_icon, update_overlays, set_dir |
| `code/__DEFINES/dcs/signals_atoms/lighting.dm` | set_light, set_light_power/range/color/on/flags/curve |
| `code/__DEFINES/dcs/signals_atoms/movable_lighting.dm` | movable dynamic light overlays |
| `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | login, logout, stat_change, do_after, phase_change, restrict_magic, swap_hand |
| `code/__DEFINES/dcs/signals/signals_mob/signals_living.dm` | buckle, resting, resist, ignite, electrocute, stun/knockdown/paralyze, health, death, mana, devotion, life-tick, wabbajack, shapeshift |
| `code/__DEFINES/dcs/signals/signals_mob/signals_carbon.dm` | pray, regenerate_limbs |
| `code/__DEFINES/dcs/signals/signals_mob/signals_mind.dm` | mind_transferred |
| `code/__DEFINES/dcs/signals/signals_mob/signals_broodmother.dm` | biomass_change |
| `code/__DEFINES/dcs/signals/signals_action.dm` | action trigger/grant/remove, cooldown start/finish/end, specific spell actions |
| `code/__DEFINES/dcs/signals/signals_ai.dm` | ai path generation, path swap, worker task lifecycle |
| `code/__DEFINES/dcs/signals/signals_beam.dm` | beam draw, beam entered/exited/turfs changed |
| `code/__DEFINES/dcs/signals/signals_client.dm` | client verb add/remove |
| `code/__DEFINES/dcs/signals/signals_coven_powers.dm` | coven power try/pre/activate/deactivate |
| `code/__DEFINES/dcs/signals/signals_datum.dm` | ui_act, divine punishment hooks |
| `code/__DEFINES/dcs/signals/signals_divine.dm` | (extends signals_datum — divine punishment categories) |
| `code/__DEFINES/dcs/signals/signals_global.dm` | new_z, mob_created, mob_death, job_after_spawn, lord_colors_set, marriage, fish_released, role_converted |
| `code/__DEFINES/dcs/signals/signals_hud.dm` | lobby collapse/expand/ready |
| `code/__DEFINES/dcs/signals/signals_leash.dm` | leash force teleport, path start/complete |
| `code/__DEFINES/dcs/signals/signals_movable.dm` | buckle/unbuckle, ridden driver move, overlay force remove/update, mob client pre_move/moved, food eat |
| `code/__DEFINES/dcs/signals/signals_moveloop.dm` | moveloop start/stop/preprocess/postprocess/jps_repath |
| `code/__DEFINES/dcs/signals/signals_objectives.dm` | various gameplay milestone signals (mocked, baptism, lux, skill rank, craft, torture, grave, taming, hug, etc.) |
| `code/__DEFINES/dcs/signals/signals_organ.dm` | organ removed/inserted, chimeric organ failure/trigger, devour, infusion |
| `code/__DEFINES/dcs/signals/signals_rage.dm` | rage changed/bottomed/overrage |
| `code/__DEFINES/dcs/signals/signals_spatial_grid.dm` | spatial_grid_cell_entered/exited (parameterized) |
| `code/__DEFINES/dcs/signals/signals_spell.dm` | before_cast, spell cast phases, cooldown, projectile hit, aoe/cone/touch variants, jaunt, lichdom, instant summons, charge |
| `code/__DEFINES/dcs/signals/signals_subsystems.dm` | ticker pregame/setting_up/round_starting, subsystem post_initialize |
| `code/__DEFINES/dcs/signals/signals_tgui.dm` | tgui window visible |
| `code/__DEFINES/dcs/signals/signals_tram.dm` | tram travelling/travel/collision/platform/empty, lift direction, dispatch cargo |
| `code/__DEFINES/dcs/signals/signals_turf.dm` | turf_enter/entered/exited, movable_turf_entered/exited, footstep sound, industrial lift |
| `code/__DEFINES/dcs/signals/signals_twohand.dm` | two_handed wield/unwield |
| `code/__DEFINES/components.dm` | item attack chain, human unarmed, projectile, combat target, mob attack hand, gun fire, movespeed, keybindings, and ~100 more component-attached signals |

## Full Signal Family Reference

### Atom — Core Interaction

| Signal | Source proc | Key args | Notes |
|---|---|---|---|
| `COMSIG_ATOM_ATTACKBY` | `atom/attackby()` | item, mob, modifiers | Main target-side hit signal |
| `COMSIG_ATOM_ATTACKBY_SECONDARY` | `atom/attackby_secondary()` | item, mob, modifiers | Secondary (right-click attack) |
| `COMSIG_ATOM_ATTACK_HAND` | `atom/attack_hand()` | mob | Unarmed hand hit |
| `COMSIG_ATOM_ATTACK_HAND_SECONDARY` | `atom/attack_hand_secondary()` | mob | |
| `COMSIG_ATOM_ATTACK_ANIMAL` | `atom/animal_attack()` | mob | Animal bite/claw hit |
| `COMSIG_ATOM_ATTACK_GHOST` | `atom/attack_ghost()` | ghost | |
| `COMSIG_ATOM_ATTACK_PAW` | `atom/attack_paw()` | mob | |
| `COMSIG_ATOM_WAS_ATTACKED` | relay_attackers element | attacker, flags | Post-attack notification |
| `COMSIG_ATOM_HITBY` | `atom/hitby()` | movable, skipcatch, hitpush, blocked, thrownthing | Thrown object impact |
| `COMSIG_ATOM_TAKE_DAMAGE` | `atom/take_damage()` | amount, type, flag, sound, dir, pen | Return `COMPONENT_NO_TAKE_DAMAGE` to block |
| `COMSIG_ATOM_INTEGRITY_CHANGED` | `atom/update_integrity()` | old_value, new_value | |
| `COMSIG_ATOM_BREAK` | `atom/atom_break()` | damage_flag | |
| `COMSIG_ATOM_FIX` | `atom/atom_fix()` | — | |
| `COMSIG_ATOM_DESTRUCTION` | `atom/atom_destruction()` | damage_flag | |
| `COMSIG_ATOM_GET_RESISTANCE` | — | — | Resistance query hook |
| `COMSIG_ATOM_GET_MAX_RESISTANCE` | — | — | |
| `COMSIG_ATOM_GET_STATUS_MOD` | — | — | |
| `COMSIG_ATOM_MAGICALLY_UNLOCKED` | `spell/aoe/knock/cast()` | spell, caster | Connect-loc: nearby turf unlock |
| `COMSIG_ATOM_CAN_BE_PULLED` | pull check | — | Return `COMSIG_ATOM_CANT_PULL` to block |

### Atom — Appearance

| Signal | Notes |
|---|---|
| `COMSIG_ATOM_UPDATE_APPEARANCE` | Return flags to suppress name/desc/icon update |
| `COMSIG_ATOM_UPDATE_NAME` | |
| `COMSIG_ATOM_UPDATE_DESC` | |
| `COMSIG_ATOM_UPDATE_ICON` | Return flags to suppress icon_state/overlays update |
| `COMSIG_ATOM_UPDATE_ICON_STATE` | |
| `COMSIG_ATOM_UPDATE_OVERLAYS` | list/new_overlays |
| `COMSIG_ATOM_UPDATED_ICON` | signalOut, did_anything |
| `COMSIG_ATOM_POST_DIR_CHANGE` | old_dir, new_dir |

### Atom — Lighting

| Signal | Notes |
|---|---|
| `COMSIG_ATOM_SET_LIGHT` | l_range, l_power, l_color, l_on — Return `COMPONENT_BLOCK_LIGHT_UPDATE` to block all light changes |
| `COMSIG_ATOM_SET_LIGHT_POWER` / `COMSIG_ATOM_UPDATE_LIGHT_POWER` | Before/after power change |
| `COMSIG_ATOM_SET_LIGHT_RANGE` / `COMSIG_ATOM_UPDATE_LIGHT_RANGE` | Before/after range change |
| `COMSIG_ATOM_SET_LIGHT_COLOR` / `COMSIG_ATOM_UPDATE_LIGHT_COLOR` | Before/after color change |
| `COMSIG_ATOM_SET_LIGHT_ON` / `COMSIG_ATOM_UPDATE_LIGHT_ON` | Before/after on-flag change |
| `COMSIG_ATOM_SET_LIGHT_FLAGS` / `COMSIG_ATOM_UPDATE_LIGHT_FLAGS` | Before/after flags change |
| `COMSIG_ATOM_SET_LIGHT_CURVE` / `COMSIG_ATOM_UPDATE_LIGHT_CURVE` | Before/after falloff curve change |
| `COMSIG_MOVABLE_LIGHT_OVERLAY_SET_RANGE` | Dynamic light color |
| `COMSIG_MOVABLE_LIGHT_OVERLAY_SET_POWER` | Dynamic light power |
| `COMSIG_MOVABLE_LIGHT_OVERLAY_SET_COLOR` | Dynamic light range (note: name/purpose mismatch in source) |
| `COMSIG_MOVABLE_LIGHT_OVERLAY_TOGGLE_ON` | Dynamic light on-state |

### Atom/Movable — Movement and Location

| Signal | Source | Key args | Return flags |
|---|---|---|---|
| `COMSIG_MOVABLE_PRE_MOVE` | `atom/movable/Moved()` | atom | `COMPONENT_MOVABLE_BLOCK_PRE_MOVE` |
| `COMSIG_MOVABLE_MOVED` | `atom/movable/Moved()` | atom, dir | |
| `COMSIG_MOVABLE_CROSS` | `atom/movable/Cross()` | atom/movable | |
| `COMSIG_MOVABLE_CROSSED` | `atom/movable/Crossed()` | atom/movable | |
| `COMSIG_MOVABLE_UNCROSSED` | `atom/movable/Uncrossed()` | atom/movable | |
| `COMSIG_MOVABLE_BUMP` | `atom/movable/Bump()` | atom | |
| `COMSIG_MOVABLE_BUMP_PUSHED` | living mob bump push | mob, force | `COMPONENT_NO_PUSH` |
| `COMSIG_MOVABLE_IMPACT` | `throw_impact()` | atom/hit_atom, thrownthing | |
| `COMSIG_MOVABLE_IMPACT_ZONE` | `mob/living/hitby()` | target, hit_zone | |
| `COMSIG_MOVABLE_PRE_THROW` | `atom/movable/throw_at()` | list/args | `COMPONENT_CANCEL_THROW` |
| `COMSIG_MOVABLE_POST_THROW` | `atom/movable/throw_at()` | thrownthing, spin | |
| `COMSIG_MOVABLE_THROW_LANDED` | `datum/thrownthing/finalize()` | thrown_object, thrownthing | |
| `COMSIG_MOVABLE_Z_CHANGED` | `atom/movable/onTransitZ()` | old_z, new_z | |
| `COMSIG_MOVABLE_SECLUDED_LOCATION` | inaccessible placement | — | |
| `COMSIG_MOVABLE_HEAR` | `atom/movable/Hear()` | message, speaker, language, raw_message, radio_freq, spans, mods | |
| `COMSIG_MOVABLE_DISPOSING` | disposal holder add | holder, source | |
| `COMSIG_MOVABLE_UPDATE_GLIDE_SIZE` | glide update | new_glide_size | |
| `COMSIG_MOVABLE_SET_GRAB_STATE` | `atom/movable/setGrabState()` | newstate | |
| `COMSIG_LIVING_START_PULL` | pull start | pulled, state, force | |
| `COMSIG_ATOM_NO_LONGER_PULLED` | pull end | puller | |
| `COMSIG_ATOM_NO_LONGER_PULLING` | stop pulling | pulling | |
| `COMSIG_MOVABLE_BUCKLE` | `atom/movable/buckle_mob()` | mob, force | |
| `COMSIG_MOVABLE_UNBUCKLE` | `atom/movable/unbuckle_mob()` | mob, force | |
| `COMSIG_MOVABLE_PREBUCKLE` | `atom/movable/buckle_mob()` | mob, force, check_loc, flags | `COMPONENT_BLOCK_BUCKLE` |
| `COMSIG_RIDDEN_DRIVER_MOVE` | `/obj/vehicle` driver_move | — | `COMPONENT_DRIVER_BLOCK_MOVE` |

### MoveLoop Signals

| Signal | Notes |
|---|---|
| `COMSIG_MOVELOOP_START` | `datum/move_loop/start_loop()` |
| `COMSIG_MOVELOOP_STOP` | `datum/move_loop/stop_loop()` |
| `COMSIG_MOVELOOP_PREPROCESS_CHECK` | `datum/move_loop/process()` — Return `MOVELOOP_SKIP_STEP` to skip |
| `COMSIG_MOVELOOP_POSTPROCESS` | `datum/move_loop/process()` — (succeeded, visual_delay) |
| `COMSIG_MOVELOOP_JPS_REPATH` | JPS pathfinder recalculate |

### Mouse / Click Signals

| Signal | Source | Notes |
|---|---|---|
| `COMSIG_CLIENT_CLICK` | `client/Click()` | target, location, control, params, mob |
| `COMSIG_CLICK` | `atom/Click()` | location, control, params, mob |
| `COMSIG_CLICK_SHIFT` | `atom/ShiftClick()` | mob — Return `COMPONENT_ALLOW_EXAMINATE` |
| `COMSIG_CLICK_CTRL` | `atom/CtrlClickOn()` | mob |
| `COMSIG_CLICK_ALT` | `atom/AltClick()` | mob — Return `COMPONENT_CANCEL_CLICK_ALT` |
| `COMSIG_CLICK_ALT_SECONDARY` | `atom/alt_click_secondary()` | mob |
| `COMSIG_CLICK_CTRL_SHIFT` | `atom/CtrlShiftClick()` | mob |
| `COMSIG_CLICK_RIGHT_SHIFT` | `atom/ShiftRightClick()` | mob |
| `COMSIG_MOUSEDROP_ONTO` | `atom/MouseDrop()` | over, mob — Return `COMPONENT_NO_MOUSEDROP` |
| `COMSIG_MOUSEDROPPED_ONTO` | `atom/MouseDrop_T()` | from, mob |
| `COMSIG_MOUSE_SCROLL_ON` | `mob/MouseWheelOn()` | atom, delta_x, delta_y, params |
| `COMSIG_LOCKPICK_ONMOUSEDOWN` | lockpick | — |

### Item / Object Signals (in `code/__DEFINES/dcs/signals_atoms/signals_obj.dm`)

| Signal | Source | Notes |
|---|---|---|
| `COMSIG_ITEM_ATTACK_SELF` | `obj/item/attack_self()` | mob |
| `COMSIG_ITEM_ATTACK_SELF_SECONDARY` | `obj/item/attack_self_secondary()` | mob |
| `COMSIG_ITEM_PRE_ATTACK` | `obj/item/pre_attack()` | target, mob, mods — Return `COMPONENT_NO_ATTACK` |
| `COMSIG_ITEM_PRE_ATTACK_SECONDARY` | `obj/item/pre_attack_secondary()` | target, mob, mods |
| `COMSIG_ITEM_ATTACK` | `obj/item/attack()` | target, mob, mods |
| `COMSIG_ITEM_ATTACK_SECONDARY` | `obj/item/attack_secondary()` | target, mob, mods |
| `COMSIG_ITEM_ATTACK_OBJ` | `obj/item/attack_obj()` | obj, mob |
| `COMSIG_ITEM_AFTERATTACK` | `obj/item/afterattack()` | target, mob, proximity, mods |
| `COMSIG_ITEM_AFTERATTACK_SECONDARY` | `obj/item/afterattack_secondary()` | target, mob, mods |
| `COMSIG_ITEM_ATTACK_QDELETED` | `obj/item/attack_qdeleted()` | target, mob, mods |
| `COMSIG_ITEM_SPEC_ATTACKEDBY` | `datum/species/spec_attacked_by()` | target, mob, mods |
| `COMSIG_ITEM_EQUIPPED` | `obj/item/equipped()` | mob, slot |
| `COMSIG_QUALITY_ADD_MATERIAL` / `COMSIG_QUALITY_MODIFY` / etc. | quality system | craft/material hooks |
| `COMSIG_MOB_FIRED_GUN` | `obj/item/gun/process_fire()` | src, target, mods, zone |
| `COMSIG_GUN_FIRED` | `obj/item/gun/process_fire()` | user, target, mods, zone |

### Item / Object Signals (in `code/__DEFINES/components.dm`)

| Signal | Notes |
|---|---|
| `COMSIG_ITEM_ATTACK_EFFECT` | `do_special_attack_effect()` — end of held-item combat chain |
| `COMSIG_MOB_ITEM_ATTACK` | `obj/item/attack()` — also sent to mob: (mob/target, mob/user) |
| `COMSIG_MOB_ITEM_AFTERATTACK` | `obj/item/afterattack()` — also sent to mob |
| `COMSIG_ITEM_IMBUE_SOUL` | lichdom soul imbue — Return `COMPONENT_BLOCK_IMBUE` |
| `COMSIG_ITEM_MARK_RETRIEVAL` | instant summons mark — Return `COMPONENT_BLOCK_MARK_RETRIEVAL` |
| `COMSIG_ITEM_MAGICALLY_CHARGED` | spell charge recharge — Return flags for charged/burnt |
| `COMSIG_ITEM_CRAFTED` | `atom/OnCrafted()` — user, craft_path |
| `COMSIG_ITEM_STOLEN` | `mob/living/MiddleClickOn()` |

### Fuse Signals

| Signal | Notes |
|---|---|
| `COMSIG_FUSE_LIT` | fuse lit |
| `COMSIG_FUSE_EXTINGUISHED` | fuse extinguished |
| `COMSIG_FUSE_CUT` | fuse cut |
| `COMSIG_FUSE_REACHED_END` | fuse burned to end |

### Combat Signals (see `ai_navigation/combat_signal_map.md` for proc chain context)

Most live in `code/__DEFINES/components.dm`.

| Signal | Source | Notes |
|---|---|---|
| `COMSIG_HUMAN_EARLY_UNARMED_ATTACK` | `human/UnarmedAttack()` | Early gate — block unarmed before main chain |
| `COMSIG_HUMAN_MELEE_UNARMED_ATTACK` | `human/UnarmedAttack()` | Main unarmed execution |
| `COMSIG_HUMAN_MELEE_UNARMED_ATTACKBY` | `human/UnarmedAttack()` | Sent to target mob |
| `COMSIG_MOB_ATTACK_HAND` | `atom/attack_hand()` | Also sent to mob |
| `COMSIG_HUMAN_DISARM_HIT` | disarm branch | |
| `COMSIG_COMBAT_TARGET_SET` | AI/combat target selection | Widely listened to by AI behaviors |
| `COMSIG_PROJECTILE_BEFORE_FIRE` | `gun/process_fire()` | Return to cancel fire |
| `COMSIG_PROJECTILE_PREHIT` | projectile pre-hit | |
| `COMSIG_PROJECTILE_ON_HIT` | `projectile/on_hit()` | |
| `COMSIG_PROJECTILE_SELF_ON_HIT` | projectile self-hit | |

### Mob Signals — Base (`signals_mob.dm`)

| Signal | Notes |
|---|---|
| `COMSIG_MOB_LOGIN` / `COMSIG_MOB_LOGOUT` | login/logout |
| `COMSIG_MOB_CLIENT_LOGIN` | after mob/login() completes with client |
| `COMSIG_MOB_STATCHANGE` | stat change (conscious/unconscious/dead) |
| `COMSIG_DO_AFTER_BEGAN` / `COMSIG_DO_AFTER_ENDED` | do_after action bar start/end |
| `COMSIG_PHASE_CHANGE` | phase (ghost/living) change |
| `COMSIG_MOB_PREPARE_STEP_SOUND` | footstep sound override — list/steps |
| `COMSIG_MOB_RESTRICT_MAGIC` | `mob/can_cast_magic()` — magic gate |
| `COMSIG_MOB_RECEIVE_MAGIC` | `mob/can_block_magic()` — Return `COMPONENT_MAGIC_BLOCKED` |
| `COMSIG_MOB_SWAPPING_HANDS` | `mob/swap_hand()` — Return `COMPONENT_BLOCK_SWAP` |
| `COMSIG_MOB_GET_STATUS_TAB_ITEMS` | status tab content hook — list/items |
| `COMSIG_PRE_MOB_CHANGED_TYPE` | `mob/change_mob_type()` — Return `COMPONENT_BLOCK_MOB_CHANGE` |
| `COMSIG_MOB_CHANGED_TYPE` | after type change |
| `COMSIG_MOB_MOVESPEED_UPDATED` | movespeed recalc |
| `COMSIG_MOB_OVERLAY_FORCE_REMOVE` / `COMSIG_MOB_OVERLAY_FORCE_UPDATE` | overlay management |
| `COMSIG_MOB_CLIENT_PRE_MOVE` | `client/Move()` — Return `COMSIG_MOB_CLIENT_BLOCK_PRE_MOVE` |
| `COMSIG_MOB_CLIENT_MOVED` | after client move — direction, old_direction |
| `COMSIG_MOB_FOOD_EAT` | food eaten |
| `COMSIG_MOB_ACTIVE_PERCEPTION` | `mob/living/look_around()` — perception event |
| `COMSIG_MOB_PRE_SPECIAL_MIDDLE` | `mob/living/MiddleClickOn()` — before middle-click intent |

### Mob Signals — Living (`signals_living.dm`)

| Signal | Notes |
|---|---|
| `COMSIG_LIVING_SET_BUCKLED` | `mob/living/set_buckled()` — new_buckled |
| `COMSIG_LIVING_SET_RESTING` | `mob/living/set_resting()` |
| `COMSIG_LIVING_SET_BODY_POSITION` | new_position, old_position |
| `COMSIG_LIVING_RESIST` | `mob/living/resist()` |
| `COMSIG_LIVING_RESIST_GRAB` | `mob/living/resist_grab()` |
| `COMSIG_LIVING_IGNITED` | `mob/living/IgniteMob()` |
| `COMSIG_LIVING_EXTINGUISHED` | `mob/living/ExtinguishMob()` |
| `COMSIG_LIVING_ELECTROCUTE_ACT` | `mob/living/electrocute_act()` — damage, source, siemens, flags |
| `COMSIG_LIVING_MINOR_SHOCK` | stun batons, tasers |
| `COMSIG_LIVING_REVIVE` | `mob/living/revive()` — full_heal, admin_revive |
| `COMSIG_LIVING_DEATH` | `mob/living/death()` — gibbed |
| `COMSIG_LIVING_TRY_ENTER_AFTERLIFE` | death → afterlife transition |
| `COMSIG_LIVING_BEFRIENDED` / `COMSIG_LIVING_UNFRIENDED` | friend add/remove |
| `COMSIG_LIVING_HEALTH_UPDATE` | `mob/living/updatehealth()` — amount |
| `COMSIG_LIVING_POST_FULLY_HEAL` | `fully_heal()` — heal_flags |
| `COMSIG_LIVING_STATUS_STUN` | `mob/living/Stun()` — amount, ignore_canstun |
| `COMSIG_LIVING_STATUS_KNOCKDOWN` | `mob/living/Knockdown()` |
| `COMSIG_LIVING_STATUS_PARALYZE` | `mob/living/Paralyze()` |
| `COMSIG_LIVING_STATUS_IMMOBILIZE` | `mob/living/Immobilize()` |
| `COMSIG_LIVING_STATUS_UNCONSCIOUS` | `mob/living/Unconscious()` |
| `COMSIG_LIVING_STATUS_SLEEP` | `mob/living/Sleeping()` |
| `COMSIG_LIVING_STATUS_OFFBALANCED` | `mob/living/OffBalance()` |
| `COMSIG_LIVING_CAN_TRACK` | `mob/living/can_track()` — Return `COMPONENT_CANT_TRACK` |
| `COMSIG_LIVING_MANA_CHANGED` | `datum/mana_pool/adjust_mana()` |
| `COMSIG_LIVING_DEVOTION_CHANGED` | `datum/devotion/cleric_holder/update_devotion()` |
| `COMSIG_LIVING_DREAM_END` | sleep advancement end |
| `COMSIG_LIVING_TRY_PUT_IN_HAND` | `mob/living/put_in_hand_check()` — Return `COMPONENT_LIVING_CANT_PUT_IN_HAND` |
| `COMSIG_LIVING_PRE_WABBAJACKED` | `mob/living/wabbajack()` — Return `STOP_WABBAJACK` |
| `COMSIG_LIVING_ON_WABBAJACKED` | after wabbajack — new mob |
| `COMSIG_LIVING_SHAPESHIFTED` | `status_effect/shapechange_mob/on_apply()` |
| `COMSIG_LIVING_UNSHAPESHIFTED` | `status_effect/shapechange_mob/after_unchange()` |
| `COMSIG_LIVING_LIMBLESS_MOVESPEED_UPDATE` | limbless movespeed modifier — list/modifiers |
| `COMSIG_LIVING_LIFE` | `mob/living/Life()` — deltatime, times_fired — Return `COMPONENT_LIVING_CANCEL_LIFE_PROCESSING` |
| `COMSIG_LIVING_ADJUSTED` | `mob/living/damage_adjusted()` |
| `COMSIG_LIVING_PREBITE_SELF` / `COMSIG_LIVING_POSTBITE_SELF` | bite self |
| `COMSIG_LIVING_WOUND_GAINED` | wound gain |
| `COMSIG_LIVING_TRY_SYRINGE` | syringe injection check — mob/user |
| `COMSIG_LIVING_APPLY_OVERLAY` / `COMSIG_LIVING_REMOVE_OVERLAY` | living overlay cache |
| `COMSIG_LIVING_POST_UPDATE_TRANSFORM` | `mob/update_transform()` |

### Mob Signals — Carbon / Human

| Signal | Notes |
|---|---|
| `COMSIG_CARBON_PRAY` | `emote/living/pray/run_emote()` — message — Return `CARBON_PRAY_CANCEL` |
| `COMSIG_CARBON_REGENERATE_LIMBS` | `mob/living/carbon/regenerate_limbs()` — excluded_limbs |
| `COMSIG_KB_LIVING_*` | keybinding signals for living mobs (pixelshift, pet commands) |

### Mob Signals — Mind

| Signal | Notes |
|---|---|
| `COMSIG_MIND_TRANSFERRED` | `mind/transfer_to()` — previous_body |
| `COMSIG_MOB_MIND_TRANSFERRED_INTO` | sent to receiving mob |
| `COMSIG_MOB_MIND_TRANSFERRED_OUT_OF` | sent to departing mob |

### Organ Signals

| Signal | Notes |
|---|---|
| `COMSIG_ORGAN_REMOVED` | organ removal |
| `COMSIG_ORGAN_INSERTED` | organ insertion |
| `COMSIG_CHIMERIC_ORGAN_FAILURE` | chimeric organ failure event |
| `COMSIG_CHIMERIC_ORGAN_TRIGGER` | chimeric organ trigger |
| `COMSIG_DEVOUR_OVERDRIVE` | devour overdrive |
| `COMSIG_HANDLE_INFUSION` | infusion handling |
| `COMSIG_ORGAN_CONSUMED` | organ-meat eaten — organ_type, organ_inside |

### Spell / Action Signals (see `ai_navigation/spell_signal_map.md` for proc chain context)

| Signal | Notes |
|---|---|
| `COMSIG_ACTION_TRIGGER` | `datum/action/Trigger()` — Return `COMPONENT_ACTION_BLOCK_TRIGGER` |
| `COMSIG_ACTION_GRANTED` / `COMSIG_MOB_GRANTED_ACTION` | action granted |
| `COMSIG_ACTION_REMOVED` / `COMSIG_MOB_REMOVED_ACTION` | action removed |
| `COMSIG_ACTION_OVERLAY_APPLY` | overlay applied to button |
| `COMSIG_MOB_ABILITY_STARTED` / `COMSIG_MOB_ABILITY_FINISHED` | cooldown action PreActivate |
| `COMSIG_ACTION_COOLDOWN_ENDED` | `CooldownEnded()` |
| `COMSIG_STARTED_CHARGE` / `COMSIG_FINISHED_CHARGE` | charge-type action |
| `COMSIG_MOB_BEFORE_SPELL_CAST` | sent to caster before_cast |
| `COMSIG_SPELL_BEFORE_CAST` | sent to spell before_cast — Return `SPELL_CANCEL_CAST`, `SPELL_NO_FEEDBACK`, etc. |
| `COMSIG_MOB_SPELL_ACTIVATED` | set_click_ability — spell activation |
| `COMSIG_MOB_CAST_SPELL` / `COMSIG_SPELL_CAST` | sent to caster/spell during cast() |
| `COMSIG_MOB_AFTER_SPELL_CAST` / `COMSIG_SPELL_AFTER_CAST` | post-cast |
| `COMSIG_SPELL_CAST_RESET` | cooldown reset |
| `COMSIG_MOB_PRE_INVOCATION` | before invocation message — list/invocation |
| `COMSIG_SPELL_PROJECTILE_HIT` | pointed projectile hit |
| `COMSIG_SPELL_AOE_ON_CAST` | AOE cast — list/atoms_affected, caster |
| `COMSIG_SPELL_CONE_ON_CAST` / `COMSIG_SPELL_CONE_ON_LAYER_EFFECT` | cone cast |
| `COMSIG_SPELL_TOUCH_HAND_HIT` | touch spell hand hit |
| `COMSIG_MOB_ENTER_JAUNT` / `COMSIG_MOB_EJECTED_FROM_JAUNT` / `COMSIG_MOB_AFTER_EXIT_JAUNT` | jaunt lifecycle |
| `COMSIG_LIVING_BLOOD_CRAWL_PRE_CONSUMED` / `COMSIG_LIVING_BLOOD_CRAWL_CONSUMED` | bloodcrawl consume |

### AI / Worker Signals

| Signal | Notes |
|---|---|
| `COMSIG_AI_PATH_GENERATED` | path found |
| `COMSIG_AI_MOVEMENT_SET` | AI movement target set |
| `COMSIG_AI_GENERAL_CHANGE` | general AI state change |
| `COMSIG_AI_FUTURE_PATH_GENERATED` | future path precomputed |
| `COMSIG_AI_PATH_SWAPPED` | path swapped |
| `COMSIG_WORKER_TASK_STARTED` / `COMSIG_WORKER_TASK_FINISHED` / `COMSIG_WORKER_TASK_FAILED` | RTS worker task lifecycle |
| `COMSIG_WORKER_STAMINA_CHANGED` | worker stamina |
| `COMSIG_WORKER_MOVEMENT_SET` / `COMSIG_WORKER_PAUSED_CHANGED` | worker movement/pause state |
| `COMSIG_WORKER_GEAR_CHANGED` | worker gear |
| `COMSIG_WORKER_IDLE_START` | worker enters idle |
| `COMSIG_WORKER_ATTACK_START` / `COMSIG_WORKER_ATTACK_END` | worker combat |

### Coven Power Signals

| Signal | Notes |
|---|---|
| `COMSIG_POWER_TRY_ACTIVATE` / `COMSIG_POWER_TRY_ACTIVATE_ON` | `can_activate()` — Return `POWER_PREVENT_ACTIVATE` |
| `COMSIG_POWER_PRE_ACTIVATION` / `COMSIG_POWER_PRE_ACTIVATION_ON` | `pre_activation()` — Return `POWER_CANCEL_ACTIVATION` |
| `COMSIG_POWER_ACTIVATE` / `COMSIG_POWER_ACTIVATE_ON` | `activate()` |
| `COMSIG_POWER_TRY_DEACTIVATE` / `COMSIG_POWER_TRY_DEACTIVATE_ON` | `can_deactivate()` — Return `POWER_PREVENT_DEACTIVATE` |
| `COMSIG_POWER_DEACTIVATE` / `COMSIG_POWER_DEACTIVATE_ON` | `deactivate()` |

### Rage Signals

| Signal | Notes |
|---|---|
| `COMSIG_RAGE_CHANGED` | `datum/rage/update_rage()` — amount |
| `COMSIG_RAGE_BOTTOMED` | rage hit zero |
| `COMSIG_RAGE_OVERRAGE` | rage exceeded max |

### Global Signals (listen with `GLOB` registration)

| Signal | Notes |
|---|---|
| `COMSIG_GLOB_NEW_Z` | new z-level added — list/args |
| `COMSIG_GLOB_EXPANDED_WORLD_BOUNDS` | world.maxx/maxy expanded |
| `COMSIG_GLOB_VAR_EDIT` | successful var edit anywhere |
| `COMSIG_GLOB_MOB_CREATED` | mob created anywhere |
| `COMSIG_GLOB_MOB_DEATH` | mob died anywhere — mob, gibbed |
| `COMSIG_GLOB_LIVING_SAY_SPECIAL` | living mob said something (use sparingly) |
| `COMSIG_GLOB_HUMAN_ENTER_CRYO` | human entered cryo — mob, admin |
| `COMSIG_GLOB_JOB_AFTER_SPAWN` | job subsystem spawned a new mob |
| `COMSIG_GLOB_JOB_AFTER_LATEJOIN_SPAWN` | latejoin spawn aftermath |
| `COMSIG_GLOB_SOUND_PLAYED` | sound played — sound_player, sound_file |
| `COMSIG_LORD_COLORS_SET` | monarch set lord colors — primary, secondary |
| `COMSIG_GLOBAL_MARRIAGE` | marriage event — bride, groom |
| `COMSIG_GLOBAL_FISH_RELEASED` | fish released into water — fish_type, fish_rarity |
| `COMSIG_GLOBAL_ROLE_CONVERTED` | role converted — recruiter, recruit, newrole |

### Subsystem / Round Flow Signals

| Signal | Notes |
|---|---|
| `COMSIG_TICKER_ENTER_PREGAME` | ticker enters pre-game phase |
| `COMSIG_TICKER_ENTER_SETTING_UP` | ticker begins round setup |
| `COMSIG_TICKER_ERROR_SETTING_UP` | round setup failed |
| `COMSIG_TICKER_ROUND_STARTING` | round started, before GAME_STATE_PLAYING |
| `COMSIG_SUBSYSTEM_POST_INITIALIZE` | subsystem finished Initialize() |

### Turf and Environment Signals

| Signal | Notes |
|---|---|
| `COMSIG_TURF_ENTER` | turf enter attempt — Return `COMPONENT_TURF_ALLOW_MOVEMENT` or `COMPONENT_TURF_DENY_MOVEMENT` |
| `COMSIG_TURF_ENTERED` | entered turf |
| `COMSIG_TURF_EXITED` | exited turf |
| `COMSIG_MOVABLE_TURF_ENTERED` | movable entered a turf |
| `COMSIG_MOVABLE_TURF_EXITED` | movable exited a turf |
| `COMSIG_TURF_PREPARE_STEP_SOUND` | footstep sound prepare — list/steps |
| `COMSIG_TURF_INDUSTRIAL_LIFT_ENTER` | industrial lift entered this turf |

### Tram / Lift Signals

| Signal | Notes |
|---|---|
| `COMSIG_TRAM_SET_TRAVELLING` | tram travelling status changed |
| `COMSIG_TRAM_TRAVEL` | tram starts to travel — idle_platform, to_where |
| `COMSIG_TRAM_COLLISION` | tram hit someone |
| `COMSIG_TRAM_REACHED_PLATFORM` | tram reached destination |
| `COMSIG_TRAM_EMPTY` | tram emptied |
| `COMSIG_LIFT_SET_DIRECTION` | normal lift started/stopped — direction or 0 |
| `COMSIG_DISPATCH_CARGO` | cargo boat dispatch |

### HUD / Client / UI Signals

| Signal | Notes |
|---|---|
| `COMSIG_HUD_LOBBY_COLLAPSED` / `COMSIG_HUD_LOBBY_EXPANDED` | lobby button state |
| `COMSIG_HUD_PLAYER_READY_TOGGLE` | ready button toggled |
| `COMSIG_CLIENT_VERB_ADDED` / `COMSIG_CLIENT_VERB_REMOVED` | verb list changed — list of verbs |
| `COMSIG_CLIENT_MOUSEDOWN` / `COMSIG_CLIENT_MOUSEUP` / `COMSIG_CLIENT_MOUSEDRAG` | low-level mouse events |
| `COMSIG_TGUI_WINDOW_VISIBLE` | tgui window fully visible |
| `COMSIG_UI_ACT` | `datum/ui_act()` |

### Leash / Follow Signals

| Signal | Notes |
|---|---|
| `COMSIG_LEASH_FORCE_TELEPORT` | leash force teleport — fired on the leashed object |
| `COMSIG_LEASH_PATH_STARTED` | leash starts pathfinding |
| `COMSIG_LEASH_PATH_COMPLETE` | leash pathfinding complete |

### Spatial Grid Signals

| Signal | Notes |
|---|---|
| `SPATIAL_GRID_CELL_ENTERED(contents_type)` | parameterized signal — cell entry |
| `SPATIAL_GRID_CELL_EXITED(contents_type)` | parameterized signal — cell exit |

### Two-Handed Signals

| Signal | Notes |
|---|---|
| `COMSIG_TWOHANDED_WIELD` | `datum/component/two_handed/wield()` — mob — Return `COMPONENT_TWOHANDED_BLOCK_WIELD` |
| `COMSIG_TWOHANDED_UNWIELD` | `datum/component/two_handed/unwield()` — mob |

### Beam Signals

| Signal | Notes |
|---|---|
| `COMSIG_BEAM_BEFORE_DRAW` | before beam redraw — Return `BEAM_CANCEL_DRAW` |
| `COMSIG_BEAM_ENTERED` | atom entered beam — atom/movable/entered |
| `COMSIG_BEAM_EXITED` | atom exited beam |
| `COMSIG_BEAM_TURFS_CHANGED` | beam turfs changed — list/callbacks |

### Movetype / Float Signals

| Signal | Notes |
|---|---|
| `COMSIG_PAUSE_FLOATING_ANIM` | float animation temporarily stopped — timer |
| `COMSIG_MOVETYPE_FLAG_ENABLED` | movement type flag gained — flag, old_movement_type |
| `COMSIG_MOVETYPE_FLAG_DISABLED` | movement type flag lost |

### Objectives / Gameplay Milestone Signals (in `signals_objectives.dm`)

These are fired when specific gameplay events happen and are typically listened to by faith, devotion, quirk, stress, and skill systems.

| Signal | Source |
|---|---|
| `COMSIG_VICIOUSLY_MOCKED` | spell/mockery cast |
| `COMSIG_BAPTISM_RECEIVED` | mana fountain baptism |
| `COMSIG_LUX_EXTRACTED` | surgery lux extract |
| `COMSIG_DRUG_SNIFFED` | powder drug sniffed |
| `COMSIG_ITEM_STOLEN` | MiddleClickOn item theft |
| `COMSIG_SKILL_RANK_CHANGE` | `adjust_skillrank()` — skill_reference, new_rank, old_rank |
| `COMSIG_ITEM_CRAFTED` | `atom/OnCrafted()` — user, craft_path |
| `COMSIG_ORGAN_CONSUMED` | organ meat consumed |
| `COMSIG_TORTURE_PERFORMED` | `mob/living/carbon/human/torture_victim()` |
| `COMSIG_GRAVE_CONSECRATED` | gravemarker OnCrafted |
| `COMSIG_ANIMAL_TAMED` | `simple_animal/tamed()` |
| `COMSIG_MOB_HUGGED` | emote hug |
| `COMSIG_ABYSSOID_CREATED` | abyssoid creation spell |
| `COMSIG_ROTTEN_FOOD_EATEN` | rotten food consumed |
| `COMSIG_LUX_TASTED` | lux status effect on apply |
| `COMSIG_HEAD_PUNCHED` | monkey attack_hand |
| `COMSIG_TREE_TRANSFORMED` | tree transform spell |
| `COMSIG_SPAT_ON` | spit emote |
| `COMSIG_APPRENTICE_MADE` | attack_hand_secondary |
| `COMSIG_ORPHAN_ADOPTED` | adopt_child spell |
| `COMSIG_PAIN_TRANSFERRED` | transfer_pain spell |
| `COMSIG_COIN_FLIPPED` | `obj/item/coin/attack_self()` — user, coin, outcome |
| `COMSIG_SPLASHED_MOB` | liquid glass thrown — user, target, reagents |
| `COMSIG_BATH_TAKEN` | stress_event/bathwater |
| `COMSIG_MOB_ENERGY_SPENT` | `mob/living/adjust_energy()` — user, amount_spent |
| `COMSIG_MOB_BUTCHERED` | `simple_animal/butcher()` |
| `COMSIG_MOB_KICK` / `COMSIG_MOB_KICKED` | `datum/species/kicked()` |
| `COMSIG_GRAVE_ROBBED` | `obj/structure/closet/dirthole/attackby()` |
| `COMSIG_FLAW_FOUND` | `spell/find_flaw/cast()` |

## Fast Search Order

1. Find the trigger event or user-visible moment.
2. Search for the nearest `COMSIG_*` family name in the tables above.
3. Find `SEND_SIGNAL(` call sites for the event source.
4. Find `RegisterSignal(` listeners on the target or shared subsystem.
5. Check whether a component or element is the real receiver.
6. If the system is spell-like, switch to `ai_navigation/spell_signal_map.md` before widening further.
7. If the system is combat-like, switch to `ai_navigation/combat_signal_map.md`.
8. If the system is movement-like, switch to `ai_navigation/movement_signal_map.md`.

## Cheap Search Patterns

- find a signal family:
  `rg -n "^#define COMSIG_" code/__DEFINES -g "*.dm"`
- find senders:
  `rg -n "\bSEND_SIGNAL\(" code modular_rmh -g "*.dm"`
- find listeners:
  `rg -n "\bRegisterSignal\(" code modular_rmh -g "*.dm"`
- find cleanup:
  `rg -n "\bUnregisterSignal\(" code modular_rmh -g "*.dm"`
- find all combat-related defines:
  `rg -n "^#define COMSIG_.*(ATTACK|COMBAT|PROJECTILE|HIT|DISARM)" code/__DEFINES -g "*.dm"`
- find signals on a specific system:
  `rg -n "COMSIG_LIVING_" code/__DEFINES -g "*.dm"`

## Rule Of Thumb

- If the proc chain looks too short for the observed behavior, assume signals are involved.
- If a component or element exists, assume it probably enters through signals.
- If a feature changes state "by itself", search signals before tracing every proc by hand.
- Combat and item signals live in `code/__DEFINES/components.dm`, not the DCS subfolder — check both.
- Global signals (prefixed `!`) must be registered on `GLOB` rather than a specific atom or datum.
