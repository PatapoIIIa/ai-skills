# Signal Map

Generated on 2026-07-09 from `COMSIG_*`, `SEND_SIGNAL`, `SEND_GLOBAL_SIGNAL`, `RegisterSignal`, and `UnregisterSignal` scans.

Signals indexed: 462.

## Hot Signals

| Signal | Send files | Register files | Define files |
|---|---|---|---|
| COMSIG_MOVABLE_MOVED | 1 | 56 | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm |
| COMSIG_PARENT_QDELETING | 1 | 51 | code/__DEFINES/components.dm |
| COMSIG_MOB_SAY | 1 | 47 | code/__DEFINES/components.dm |
| COMSIG_PARENT_EXAMINE | 3 | 28 | code/__DEFINES/components.dm |
| COMSIG_ITEM_DROPPED | 1 | 20 | code/__DEFINES/components.dm |
| COMSIG_LIVING_DEATH | 1 | 20 | code/__DEFINES/components.dm |
| COMSIG_MOB_MODIFY_AGGRO_LINES | 20 | 1 | code/__DEFINES/components.dm |
| COMSIG_ITEM_EQUIPPED | 1 | 19 | code/__DEFINES/components.dm |
| COMSIG_COMPONENT_CLEAN_ACT | 9 | 9 | code/__DEFINES/components.dm |
| COMSIG_SEX_GET_AROUSAL | 17 | 1 | code/__DEFINES/sex.dm |
| COMSIG_MOB_APPLY_DAMGE | 3 | 13 | code/__DEFINES/components.dm |
| COMSIG_TRY_STORAGE_INSERT | 12 | 2 | code/__DEFINES/components.dm |
| COMSIG_QDELETING | 0 | 13 | code/__DEFINES/components.dm |
| COMSIG_ITEM_AFTERATTACK | 1 | 10 | code/__DEFINES/components.dm |
| COMSIG_MOB_ITEM_ATTACK | 2 | 9 | code/__DEFINES/components.dm |
| COMSIG_MOB_DEATH | 1 | 9 | code/__DEFINES/components.dm |
| COMSIG_MOB_EQUIPPED_ITEM | 1 | 9 | code/__DEFINES/components.dm |
| COMSIG_DISGUISE_STATUS | 8 | 1 | code/__DEFINES/components.dm |
| COMSIG_HOSTILE_ATTACKINGTARGET | 5 | 4 | code/__DEFINES/components.dm |
| COMSIG_ATOM_ATTACK_HAND | 3 | 5 | code/__DEFINES/components.dm |
| COMSIG_HUMAN_LIFE | 1 | 7 | code/__DEFINES/components.dm |
| COMSIG_ITEM_ATTACK_SUCCESS | 2 | 6 | code/__DEFINES/components.dm |
| COMSIG_ITEM_PICKUP | 1 | 7 | code/__DEFINES/components.dm |
| COMSIG_MOVABLE_CROSSED | 1 | 6 | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm |
| COMSIG_PARENT_ATTACKBY | 1 | 7 | code/__DEFINES/components.dm |
| COMSIG_ATOM_WAS_ATTACKED | 2 | 5 | code/__DEFINES/components.dm |
| COMSIG_ITEM_ATTACK | 2 | 5 | code/__DEFINES/components.dm |
| COMSIG_ITEM_ATTACK_SELF | 1 | 6 | code/__DEFINES/components.dm |
| COMSIG_MOB_DROPITEM | 1 | 6 | code/__DEFINES/components.dm |
| COMSIG_PROJECTILE_ON_HIT | 1 | 6 | code/__DEFINES/components.dm |
| COMSIG_ATOM_DIR_CHANGE | 1 | 5 | code/__DEFINES/components.dm |
| COMSIG_CONTAINS_STORAGE | 5 | 1 | code/__DEFINES/components.dm |
| COMSIG_ERP_ANATOMY_CHANGED | 5 | 1 | modular_twilight_axis/code/modules/erp_system/_defines.dm |
| COMSIG_HOSTILE_PRE_ATTACKINGTARGET | 6 | 0 | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm |
| COMSIG_HUMAN_MELEE_UNARMED_ATTACK | 1 | 5 | code/__DEFINES/components.dm |
| COMSIG_MOB_ATTACK_HAND | 1 | 5 | code/__DEFINES/components.dm |
| COMSIG_MOB_ITEM_ATTACK_POST_SWINGDELAY | 2 | 4 | code/__DEFINES/components.dm |
| COMSIG_MOVABLE_BUMP | 1 | 4 | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm |
| COMSIG_SEX_SET_AROUSAL | 5 | 1 | code/__DEFINES/sex.dm |
| COMSIG_TRY_STORAGE_TAKE | 5 | 1 | code/__DEFINES/components.dm |


## Full Index

| Signal | Defined in | Send file count | Register file count | Sample usage files |
|---|---|---|---|---|
| COMSIG_ABYSSOID_CREATED | code/__DEFINES/dcs/signals/signals_objectives.dm | 1 | 1 | code/modules/spells/roguetown/create_abyssoid.dm, code/game/gamemodes/personal_objectives/pantheon/abyssor/abyssoid_creation.dm |
| COMSIG_ACTION_COOLDOWN_ENDED | code/__DEFINES/dcs/signals/signals_action.dm | 1 | 0 | code/datums/actions/action_cooldown.dm |
| COMSIG_ACTION_GRANTED | code/__DEFINES/dcs/signals/signals_action.dm | 1 | 0 | code/datums/actions/action.dm |
| COMSIG_ACTION_OVERLAY_APPLY | code/__DEFINES/dcs/signals/signals_action.dm | 2 | 1 | code/datums/actions/action.dm, modular_twilight_axis/code/modules/vampire_neu/ascended_covens.dm, code/datums/components/action_item_overlay.dm |
| COMSIG_ACTION_REMOVED | code/__DEFINES/dcs/signals/signals_action.dm | 1 | 0 | code/datums/actions/action.dm |
| COMSIG_ACTION_TRIGGER | code/__DEFINES/dcs/signals/signals_action.dm | 1 | 1 | code/datums/actions/action.dm, modular_twilight_axis/code/modules/mob/living/carbon/human/table_crawl.dm |
| COMSIG_AFTER_STORAGE_INSERT | code/__DEFINES/components.dm | 1 | 1 | code/game/objects/items/storage/new_storage/tetris.dm, code/datums/item_equipped_movement_rustle.dm |
| COMSIG_AFTER_STORAGE_REMOVE | code/__DEFINES/components.dm | 1 | 1 | code/game/objects/items/storage/new_storage/tetris.dm, code/datums/item_equipped_movement_rustle.dm |
| COMSIG_AI_BLACKBOARD_KEY_CLEARED | code/__DEFINES/ai/_ai.dm | 1 | 0 | code/datums/ai/_ai_controller.dm |
| COMSIG_AI_BLACKBOARD_KEY_SET | code/__DEFINES/ai/_ai.dm | 1 | 2 | code/datums/ai/_ai_controller.dm, code/datums/components/combat_vocalizer.dm, modular_twilight_axis/code/modules/spells/pantheon/divine/necra/garden_skeleton.dm |
| COMSIG_AI_CONTROLLER_PICKED_BEHAVIORS | code/__DEFINES/ai/_ai.dm | 1 | 0 | code/datums/ai/_ai_controller.dm |
| COMSIG_AI_FUTURE_PATH_GENERATED | code/__DEFINES/dcs/signals/signals_ai.dm | 1 | 0 | code/datums/ai/ai_movement/hybrid_movement.dm |
| COMSIG_AI_GENERAL_CHANGE | code/__DEFINES/dcs/signals/signals_ai.dm | 2 | 0 | code/datums/ai/ai_movement/hybrid_movement.dm, code/datums/components/aggro_board.dm |
| COMSIG_AI_MOVEMENT_SET | code/__DEFINES/dcs/signals/signals_ai.dm | 0 | 0 | - |
| COMSIG_AI_PATH_GENERATED | code/__DEFINES/dcs/signals/signals_ai.dm | 1 | 0 | code/datums/ai/ai_movement/hybrid_movement.dm |
| COMSIG_AI_PATH_SWAPPED | code/__DEFINES/dcs/signals/signals_ai.dm | 1 | 0 | code/datums/ai/ai_movement/hybrid_movement.dm |
| COMSIG_ANIMAL_TAMED | code/__DEFINES/dcs/signals/signals_objectives.dm | 1 | 1 | code/modules/mob/living/simple_animal/simple_animal.dm, code/game/gamemodes/personal_objectives/pantheon/dendor/tame.dm |
| COMSIG_AREA_ENTERED | code/__DEFINES/components.dm | 1 | 0 | code/game/area/areas.dm |
| COMSIG_AREA_EXITED | code/__DEFINES/components.dm | 1 | 0 | code/game/area/areas.dm |
| COMSIG_ATOM_ACID_ACT | code/__DEFINES/components.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_ADD_TRAIT | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_ATOM_AFTER_SUCCESSFUL_INITIALIZE | code/__DEFINES/components.dm | 1 | 0 | code/controllers/subsystem/atoms.dm |
| COMSIG_ATOM_AFTER_SUCCESSFUL_INITIALIZED_ON | code/__DEFINES/components.dm | 1 | 0 | code/controllers/subsystem/atoms.dm |
| COMSIG_ATOM_ANALYSER_ACT | code/__DEFINES/components.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_ATTACKBY | code/__DEFINES/dcs/signals_atoms/signals_atom.dm | 0 | 4 | code/datums/elements/relay_attackers.dm, code/datums/slapcrafting.dm, code/modules/vampire_neu/covens/coven_powers/_base_power.dm |
| COMSIG_ATOM_ATTACK_ANIMAL | code/__DEFINES/components.dm | 1 | 2 | code/_onclick/other_mobs.dm, code/datums/elements/relay_attackers.dm, modular_twilight_axis/code/modules/spells/pantheon/divine/necra/shroud.dm |
| COMSIG_ATOM_ATTACK_GHOST | code/__DEFINES/components.dm | 1 | 1 | code/_onclick/observer.dm, code/datums/components/storage/storage.dm |
| COMSIG_ATOM_ATTACK_HAND | code/__DEFINES/components.dm | 3 | 5 | code/_onclick/other_mobs.dm, code/modules/mob/living/carbon/human/species.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/melee/soundbreaker_proxy.dm |
| COMSIG_ATOM_ATTACK_RIGHT | code/__DEFINES/components.dm | 1 | 3 | code/_onclick/other_mobs.dm, code/game/objects/items/holster_component.dm, code/game/objects/items/rogueweapons/melee/special.dm |
| COMSIG_ATOM_BLOB_ACT | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_ATOM_BLOCKS_BSA_BEAM | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_ATOM_BSA_BEAM | code/__DEFINES/components.dm | 0 | 1 | code/datums/elements/bsa_blocker.dm |
| COMSIG_ATOM_BULLET_ACT | code/__DEFINES/components.dm | 2 | 3 | code/game/atoms.dm, code/modules/mob/living/living_defense.dm, code/datums/elements/relay_attackers.dm |
| COMSIG_ATOM_BUMPED | code/__DEFINES/components.dm | 1 | 1 | code/game/atoms.dm, code/game/objects/minecart_system/minecart.dm |
| COMSIG_ATOM_CANREACH | code/__DEFINES/components.dm | 1 | 1 | code/_onclick/click.dm, code/datums/components/storage/storage.dm |
| COMSIG_ATOM_CONTENTS_DEL | code/__DEFINES/components.dm | 1 | 1 | code/game/atoms.dm, code/datums/components/storage/concrete/_concrete.dm |
| COMSIG_ATOM_CROWBAR_ACT | code/__DEFINES/components.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_DIR_CHANGE | code/__DEFINES/components.dm | 1 | 5 | code/game/atoms.dm, code/datums/components/after_image.dm, code/datums/components/decal.dm |
| COMSIG_ATOM_EMAG_ACT | code/__DEFINES/components.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_EMP_ACT | code/__DEFINES/components.dm | 1 | 1 | code/game/atoms.dm, code/datums/components/empprotection.dm |
| COMSIG_ATOM_ENTERED | code/__DEFINES/components.dm | 1 | 4 | code/game/atoms.dm, code/datums/components/magnetic_catch.dm, code/datums/components/squeak.dm |
| COMSIG_ATOM_EXAMINE | code/__DEFINES/dcs/signals_atoms/signals_atom.dm | 0 | 0 | - |
| COMSIG_ATOM_EXAMINE_MORE | code/__DEFINES/dcs/signals_atoms/signals_atom.dm | 0 | 1 | code/datums/slapcrafting.dm |
| COMSIG_ATOM_EXAMINE_TAGS | code/__DEFINES/dcs/signals_atoms/signals_atom.dm | 0 | 1 | code/datums/slapcrafting.dm |
| COMSIG_ATOM_EXIT | code/__DEFINES/components.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_EXITED | code/__DEFINES/components.dm | 1 | 3 | code/game/atoms.dm, code/datums/components/magnetic_catch.dm, code/datums/components/storage/storage.dm |
| COMSIG_ATOM_EX_ACT | code/__DEFINES/components.dm | 1 | 1 | code/game/atoms.dm, code/datums/components/explodable.dm |
| COMSIG_ATOM_FIRE_ACT | code/__DEFINES/components.dm | 1 | 1 | code/game/atoms.dm, code/game/objects/items/rogueweapons/melee/special.dm |
| COMSIG_ATOM_GET_EXAMINE_NAME | code/__DEFINES/components.dm | 1 | 1 | code/game/atoms.dm, code/datums/components/decals/blood.dm |
| COMSIG_ATOM_HITBY | code/__DEFINES/dcs/signals_atoms/signals_atom.dm | 2 | 2 | code/game/atoms.dm, code/game/objects/items.dm, code/datums/elements/relay_attackers.dm |
| COMSIG_ATOM_INTERCEPT_TELEPORT | code/__DEFINES/components.dm | 1 | 1 | code/datums/helper_datums/teleport.dm, code/game/objects/effects/blessing.dm |
| COMSIG_ATOM_INTERCEPT_Z_FALL | code/__DEFINES/components.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_MULTITOOL_ACT | code/__DEFINES/components.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_NARSIE_ACT | code/__DEFINES/components.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_NO_UPDATE_DESC | code/__DEFINES/dcs/signals_atoms/appearance.dm | 0 | 0 | - |
| COMSIG_ATOM_NO_UPDATE_ICON | code/__DEFINES/dcs/signals_atoms/appearance.dm | 0 | 0 | - |
| COMSIG_ATOM_NO_UPDATE_ICON_STATE | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/appearance.dm | 0 | 0 | - |
| COMSIG_ATOM_NO_UPDATE_NAME | code/__DEFINES/dcs/signals_atoms/appearance.dm | 0 | 0 | - |
| COMSIG_ATOM_NO_UPDATE_OVERLAYS | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/appearance.dm | 0 | 0 | - |
| COMSIG_ATOM_ORBIT_BEGIN | code/__DEFINES/components.dm | 1 | 1 | code/datums/components/orbiter.dm, code/datums/components/deadchat_control.dm |
| COMSIG_ATOM_ORBIT_STOP | code/__DEFINES/components.dm | 1 | 1 | code/datums/components/orbiter.dm, code/datums/components/deadchat_control.dm |
| COMSIG_ATOM_REMOVE_TRAIT | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_ATOM_SCREWDRIVER_ACT | code/__DEFINES/components.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_SET_LIGHT | code/__DEFINES/dcs/signals_atoms/lighting.dm | 1 | 0 | code/modules/lighting/lighting_atom.dm |
| COMSIG_ATOM_SET_LIGHT_COLOR | code/__DEFINES/dcs/signals_atoms/lighting.dm | 2 | 1 | code/datums/magic_items/mundane_items/mundane.dm, code/modules/lighting/lighting_atom.dm, code/datums/components/movable_lighting.dm |
| COMSIG_ATOM_SET_LIGHT_CURVE | code/__DEFINES/dcs/signals_atoms/lighting.dm | 1 | 0 | code/modules/lighting/lighting_atom.dm |
| COMSIG_ATOM_SET_LIGHT_FLAGS | code/__DEFINES/dcs/signals_atoms/lighting.dm | 0 | 1 | code/datums/components/movable_lighting.dm |
| COMSIG_ATOM_SET_LIGHT_ON | code/__DEFINES/dcs/signals_atoms/lighting.dm | 1 | 1 | code/modules/lighting/lighting_atom.dm, code/datums/components/movable_lighting.dm |
| COMSIG_ATOM_SET_LIGHT_POWER | code/__DEFINES/dcs/signals_atoms/lighting.dm | 2 | 1 | code/datums/magic_items/mundane_items/mundane.dm, code/modules/lighting/lighting_atom.dm, code/datums/components/movable_lighting.dm |
| COMSIG_ATOM_SET_LIGHT_RANGE | code/__DEFINES/dcs/signals_atoms/lighting.dm | 2 | 1 | code/datums/magic_items/mundane_items/mundane.dm, code/modules/lighting/lighting_atom.dm, code/datums/components/movable_lighting.dm |
| COMSIG_ATOM_UPDATED_ICON | code/__DEFINES/dcs/signals_atoms/appearance.dm | 0 | 1 | code/datums/actions/action.dm |
| COMSIG_ATOM_UPDATE_APPEARANCE | code/__DEFINES/dcs/signals_atoms/appearance.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_UPDATE_DESC | code/__DEFINES/dcs/signals_atoms/appearance.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_UPDATE_ICON | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/appearance.dm | 1 | 1 | code/game/atoms.dm, code/game/objects/items/holster_component.dm |
| COMSIG_ATOM_UPDATE_ICON_STATE | code/__DEFINES/dcs/signals_atoms/appearance.dm | 0 | 0 | - |
| COMSIG_ATOM_UPDATE_LIGHT_COLOR | code/__DEFINES/dcs/signals_atoms/lighting.dm | 1 | 0 | code/modules/lighting/lighting_atom.dm |
| COMSIG_ATOM_UPDATE_LIGHT_CURVE | code/__DEFINES/dcs/signals_atoms/lighting.dm | 1 | 0 | code/modules/lighting/lighting_atom.dm |
| COMSIG_ATOM_UPDATE_LIGHT_FLAGS | code/__DEFINES/dcs/signals_atoms/lighting.dm | 0 | 0 | - |
| COMSIG_ATOM_UPDATE_LIGHT_ON | code/__DEFINES/dcs/signals_atoms/lighting.dm | 1 | 0 | code/modules/lighting/lighting_atom.dm |
| COMSIG_ATOM_UPDATE_LIGHT_POWER | code/__DEFINES/dcs/signals_atoms/lighting.dm | 1 | 0 | code/modules/lighting/lighting_atom.dm |
| COMSIG_ATOM_UPDATE_LIGHT_RANGE | code/__DEFINES/dcs/signals_atoms/lighting.dm | 1 | 0 | code/modules/lighting/lighting_atom.dm |
| COMSIG_ATOM_UPDATE_NAME | code/__DEFINES/dcs/signals_atoms/appearance.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_UPDATE_OVERLAYS | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/appearance.dm | 1 | 1 | code/game/atoms.dm, code/datums/status_effects/firestacker.dm |
| COMSIG_ATOM_WAS_ATTACKED | code/__DEFINES/components.dm | 2 | 5 | code/datums/elements/relay_attackers.dm, code/modules/spells/spell_types/classunique/spellblade/anime_spells_helper.dm, code/datums/ai/_ai_controller.dm |
| COMSIG_ATOM_WELDER_ACT | code/__DEFINES/components.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_WIRECUTTER_ACT | code/__DEFINES/components.dm | 1 | 0 | code/game/atoms.dm |
| COMSIG_ATOM_WRENCH_ACT | code/__DEFINES/components.dm | 1 | 1 | code/game/atoms.dm, code/datums/components/rotation.dm |
| COMSIG_ATTACK_TRY_CONSUME | modular_twilight_axis/code/_signals.dm | 2 | 3 | modular_twilight_axis/code/datums/combo/combo_core.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/intents.dm, modular_twilight_axis/code/datums/combo/combo_ronin.dm |
| COMSIG_BATH_TAKEN | - | 1 | 0 | code/datums/stress/positive_events.dm |
| COMSIG_BORG_SAFE_DECONSTRUCT | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_CARBON_PRAY | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 2 | 0 | code/modules/mob/living/emote.dm, modular_twilight_axis/lore/code/mob/emote.dm |
| COMSIG_CARBON_SOUNDBANG | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/living/carbon/carbon_defense.dm |
| COMSIG_CARBON_SWAPHANDS | code/__DEFINES/components.dm | 1 | 1 | code/modules/mob/living/carbon/carbon.dm, code/datums/status_effects/rogue/roguebuff.dm |
| COMSIG_CD_RESET | code/__DEFINES/cooldowns.dm | 1 | 0 | code/datums/datum.dm |
| COMSIG_CD_STOP | code/__DEFINES/cooldowns.dm | 1 | 0 | code/datums/datum.dm |
| COMSIG_CLICK | code/__DEFINES/components.dm | 1 | 1 | code/_onclick/click.dm, code/datums/components/crafting/crafting.dm |
| COMSIG_CLICK_ALT | code/__DEFINES/components.dm | 1 | 4 | code/_onclick/click.dm, code/datums/ai/hostile/_hostile_controller.dm, code/datums/components/rotation.dm |
| COMSIG_CLICK_CTRL | code/__DEFINES/components.dm | 1 | 0 | code/_onclick/click.dm |
| COMSIG_CLICK_CTRL_SHIFT | code/__DEFINES/components.dm | 1 | 0 | code/_onclick/click.dm |
| COMSIG_CLICK_RIGHT_SHIFT | code/__DEFINES/components.dm | 1 | 0 | code/_onclick/click.dm |
| COMSIG_CLICK_SHIFT | code/__DEFINES/components.dm | 1 | 0 | code/_onclick/click.dm |
| COMSIG_CLIENT_MOUSEDOWN | code/__DEFINES/dcs/signals/signals_mob/signals_client.dm | 1 | 3 | code/_onclick/drag_drop.dm, code/modules/spells/spell.dm, code/modules/spells/spell_cooldown.dm |
| COMSIG_CLIENT_MOUSEDRAG | code/__DEFINES/dcs/signals/signals_mob/signals_client.dm | 1 | 0 | code/_onclick/drag_drop.dm |
| COMSIG_CLIENT_MOUSEUP | code/__DEFINES/dcs/signals/signals_mob/signals_client.dm | 1 | 1 | code/_onclick/drag_drop.dm, code/modules/spells/spell_cooldown.dm |
| COMSIG_CLIENT_VERB_ADDED | code/__DEFINES/dcs/signals/signals_mob/signals_client.dm | 1 | 0 | code/__HELPERS/verbs.dm |
| COMSIG_CLIENT_VERB_REMOVED | code/__DEFINES/dcs/signals/signals_mob/signals_client.dm | 1 | 0 | code/__HELPERS/verbs.dm |
| COMSIG_CLOTHING_STEP_ACTION | code/__DEFINES/components.dm | 1 | 1 | code/modules/clothing/clothing.dm, code/datums/components/squeak.dm |
| COMSIG_COMBAT_TARGET_SET | code/__DEFINES/components.dm | 2 | 0 | code/datums/ai/subtrees/bow_usage.dm, code/datums/ai/subtrees/human_basic_attack.dm |
| COMSIG_COMBO_CORE_CLEAR | modular_twilight_axis/code/_signals.dm | 0 | 1 | modular_twilight_axis/code/datums/combo/combo_core.dm |
| COMSIG_COMBO_CORE_REGISTER_INPUT | modular_twilight_axis/code/_signals.dm | 1 | 2 | modular_twilight_axis/code/modules/spells/ronin.dm, modular_twilight_axis/code/datums/combo/combo_core.dm, modular_twilight_axis/code/datums/combo/combo_ronin.dm |
| COMSIG_COMPONENT_ADDED | code/__DEFINES/components.dm | 1 | 0 | code/datums/components/_component.dm |
| COMSIG_COMPONENT_CLEAN_ACT | code/__DEFINES/components.dm | 9 | 9 | code/__HELPERS/unsorted.dm, code/datums/elements/cleaning.dm, code/game/objects/items/rogueitems/natural/clothfibersthorn.dm |
| COMSIG_COMPONENT_CLEAN_FACE_ACT | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_COMPONENT_NTNET_RECEIVE | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_COMPONENT_REMOVING | code/__DEFINES/components.dm | 1 | 0 | code/datums/components/_component.dm |
| COMSIG_CONTAINS_STORAGE | code/__DEFINES/components.dm | 5 | 1 | code/datums/components/storage/storage.dm, code/game/objects/items.dm, code/modules/clothing/outfits/vv_outfit.dm |
| COMSIG_DISGUISE_STATUS | code/__DEFINES/components.dm | 8 | 1 | code/modules/antagonists/roguetown/roleobjs/skeleton.dm, code/modules/antagonists/roguetown/villain/lich.dm, code/modules/antagonists/roguetown/villain/zombie/zombie.dm |
| COMSIG_DISPATCH_CARGO | code/__DEFINES/dcs/signals/signals_tram.dm | 0 | 1 | code/game/machinery/trams_and_elevators/tram/cargo_line.dm |
| COMSIG_DIVINE_REBIRTH_CAST | code/__DEFINES/components.dm | 1 | 1 | code/modules/spells/roguetown/acolyte/pestra.dm, code/modules/spells/roguetown/acolyte/pestra/pestra_components.dm |
| COMSIG_DO_AFTER_BEGAN | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 1 | 1 | code/__HELPERS/mobs.dm, code/datums/elements/interrupt_on_damage.dm |
| COMSIG_DO_AFTER_ENDED | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 1 | 1 | code/__HELPERS/mobs.dm, code/datums/elements/interrupt_on_damage.dm |
| COMSIG_DRUG_SNIFFED | code/__DEFINES/dcs/signals/signals_objectives.dm | 1 | 2 | code/modules/reagents/reagent_containers/powderspice.dm, code/datums/gods/patrons/inhumen/resurrect_inhumen.dm, code/game/gamemodes/personal_objectives/ascendants/baotha/snort_drugs.dm |
| COMSIG_ELEMENT_ATTACH | code/__DEFINES/components.dm | 1 | 0 | code/datums/elements/_element.dm |
| COMSIG_ELEMENT_DETACH | code/__DEFINES/components.dm | 1 | 0 | code/datums/elements/_element.dm |
| COMSIG_ENTER_AREA | code/__DEFINES/components.dm | 1 | 3 | code/game/area/areas.dm, code/controllers/subsystem/rogue/fog_event/fog_entity_component.dm, code/datums/components/area_ambience.dm |
| COMSIG_ERP_ANATOMY_CHANGED | modular_twilight_axis/code/modules/erp_system/_defines.dm | 5 | 1 | modular_twilight_axis/code/modules/erp_system/organs/types/breasts.dm, modular_twilight_axis/code/modules/erp_system/organs/types/penis.dm, modular_twilight_axis/code/modules/erp_system/organs/types/vagina.dm |
| COMSIG_ERP_GET_LINKS | modular_twilight_axis/code/modules/erp_system/_defines.dm | 3 | 1 | modular_twilight_axis/code/modules/erp_system/core/knot/erp_knot_service.dm, modular_twilight_axis/code/modules/erp_system/core/services/erp_climax_service.dm, modular_twilight_axis/code/modules/erp_system/patches/arousal.dm |
| COMSIG_ERP_LOCATION_ACCESSIBLE | - | 0 | 1 | code/modules/mob/living/carbon/human/species_types/roguetown/dullahan/dullahan.dm |
| COMSIG_EXIT_AREA | code/__DEFINES/components.dm | 1 | 1 | code/game/area/areas.dm, code/datums/components/beauty.dm |
| COMSIG_FOG_END | code/__DEFINES/components.dm | 1 | 1 | code/controllers/subsystem/rogue/scheduled_event_subsytem.dm, code/controllers/subsystem/rogue/fog_event/fog_entity_component.dm |
| COMSIG_FOOD_EATEN | code/__DEFINES/components.dm | 1 | 3 | code/modules/food_and_drinks/food/snacks.dm, code/modules/jobs/job_types/roguetown/adventurer/types/antag/hag_class/hag_boons/hag_boons_spells.dm, code/modules/spells/roguetown/acolyte/eora.dm |
| COMSIG_FORCE_UNDISGUISE | code/__DEFINES/components.dm | 3 | 1 | code/_onclick/item_attack.dm, code/game/objects/items/rogueweapons/ranged/_ammo.dm, modular_twilight_axis/code/modules/vampire_neu/overrides/transfix.dm |
| COMSIG_GIBS_STREAK | code/__DEFINES/components.dm | 1 | 0 | code/game/objects/effects/decals/cleanable/humans.dm |
| COMSIG_GLOBAL_FISH_RELEASED | code/__DEFINES/dcs/signals/signals_objectives.dm | 0 | 1 | code/game/gamemodes/personal_objectives/pantheon/abyssor/fish_release.dm |
| COMSIG_GLOB_EXPANDED_WORLD_BOUNDS | code/__DEFINES/components.dm | 0 | 1 | code/controllers/subsystem/spatial_gridmap.dm |
| COMSIG_GLOB_JOB_AFTER_LATEJOIN_SPAWN | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_GLOB_JOB_AFTER_SPAWN | code/__DEFINES/components.dm | 0 | 1 | code/modules/events/god_intervention/schism.dm |
| COMSIG_GLOB_LIVING_SAY_SPECIAL | code/__DEFINES/components.dm | 0 | 1 | code/datums/components/beetlejuice.dm |
| COMSIG_GLOB_MOB_CREATED | code/__DEFINES/components.dm | 0 | 1 | modular_twilight_axis/familytree_module/familytree_subsystem_core.dm |
| COMSIG_GLOB_MOB_DEATH | code/__DEFINES/components.dm | 0 | 1 | modular_twilight_axis/code/modules/vampire_neu/ascended_covens.dm |
| COMSIG_GLOB_NEW_Z | code/__DEFINES/components.dm | 0 | 1 | code/controllers/subsystem/spatial_gridmap.dm |
| COMSIG_GLOB_ROLE_CONVERTED | code/__DEFINES/dcs/signals/signals_objectives.dm | 2 | 1 | code/modules/jobs/job_types/roguetown/nobility/lord.dm, modular_deserttown/jobs/desertjobs.dm, code/game/gamemodes/personal_objectives/pantheon/astrata/recruit_retainer.dm |
| COMSIG_GLOB_VAR_EDIT | code/__DEFINES/components.dm | 0 | 1 | code/datums/components/edit_complainer.dm |
| COMSIG_GRAVE_CONSECRATED | code/__DEFINES/dcs/signals/signals_objectives.dm | 1 | 1 | code/modules/roguetown/roguejobs/gravedigger/hole.dm, code/game/gamemodes/personal_objectives/pantheon/necra/bury.dm |
| COMSIG_HABITABLE_HOME | - | 1 | 0 | code/datums/ai/behaviors/find_and_set.dm |
| COMSIG_HAS_NANITES | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_HEADHOOK_CONTENTS_CHANGED | modular_twilight_axis/code/_signals.dm | 1 | 1 | modular_twilight_axis/code/modules/clothing/rogueclothes/storage/storage.dm, modular_twilight_axis/code/datums/trophy_hunter.dm |
| COMSIG_HEADHOOK_EQUIPPED | modular_twilight_axis/code/_signals.dm | 1 | 0 | modular_twilight_axis/code/modules/clothing/rogueclothes/storage/storage.dm |
| COMSIG_HEADHOOK_UNEQUIPPED | modular_twilight_axis/code/_signals.dm | 1 | 1 | modular_twilight_axis/code/modules/clothing/rogueclothes/storage/storage.dm, modular_twilight_axis/code/datums/trophy_hunter.dm |
| COMSIG_HEAD_PUNCHED | code/__DEFINES/dcs/signals/signals_objectives.dm | 2 | 1 | code/modules/mob/living/carbon/human/species.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/melee/soundbreaker_proxy.dm, code/game/gamemodes/personal_objectives/ascendants/graggar/punch_targets.dm |
| COMSIG_HEART_BEAST_HEAR | code/__DEFINES/components.dm | 1 | 1 | code/modules/roguetown/roguemachine/heartbeast/heart_beast.dm, code/modules/roguetown/roguemachine/heartbeast/heart_component.dm |
| COMSIG_HOSTILE_ATTACKINGTARGET | code/__DEFINES/components.dm | 5 | 4 | code/modules/mob/living/simple_animal/hostile/hostile.dm, code/modules/mob/living/simple_animal/hostile/retaliate/summons/elemental/behemoth.dm, code/modules/mob/living/simple_animal/hostile/retaliate/summons/fae/glimmerwing.dm |
| COMSIG_HOSTILE_FOUND_TARGET | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 0 | 0 | - |
| COMSIG_HOSTILE_POST_ATTACKINGTARGET | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 0 | 0 | - |
| COMSIG_HOSTILE_PRE_ATTACKINGTARGET | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 6 | 0 | code/datums/ai/_ai_controller.dm, code/modules/mob/living/simple_animal/hostile/hostile.dm, code/modules/mob/living/simple_animal/hostile/retaliate/summons/elemental/behemoth.dm |
| COMSIG_HUD_LOBBY_COLLAPSED | code/__DEFINES/dcs/signals/signals_hud.dm | 1 | 1 | code/_onclick/hud/new_player.dm, code/_onclick/hud/new_player.dm |
| COMSIG_HUD_LOBBY_EXPANDED | code/__DEFINES/dcs/signals/signals_hud.dm | 1 | 1 | code/_onclick/hud/new_player.dm, code/_onclick/hud/new_player.dm |
| COMSIG_HUD_PLAYER_READY_TOGGLE | code/__DEFINES/dcs/signals/signals_hud.dm | 1 | 0 | code/_onclick/hud/new_player.dm |
| COMSIG_HUMAN_BURNING | - | 1 | 0 | code/modules/mob/living/carbon/human/human_defense.dm |
| COMSIG_HUMAN_DISARM_HIT | code/__DEFINES/components.dm | 1 | 1 | code/modules/mob/living/carbon/human/species.dm, code/datums/components/knockoff.dm |
| COMSIG_HUMAN_EARLY_UNARMED_ATTACK | code/__DEFINES/components.dm | 1 | 1 | code/_onclick/other_mobs.dm, modular_twilight_axis/code/modules/mob/living/carbon/human/table_crawl.dm |
| COMSIG_HUMAN_FORCESAY | - | 1 | 0 | code/modules/tgui_input/say_modal/speech.dm |
| COMSIG_HUMAN_LIFE | code/__DEFINES/components.dm | 1 | 7 | code/modules/mob/living/carbon/human/life.dm, code/datums/components/hideous_face.dm, code/datums/components/sun_hater.dm |
| COMSIG_HUMAN_MELEE_UNARMED_ATTACK | code/__DEFINES/components.dm | 1 | 5 | code/_onclick/other_mobs.dm, code/datums/components/riding.dm, code/datums/status_effects/rogue/roguebuff.dm |
| COMSIG_HUMAN_MELEE_UNARMED_ATTACKBY | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_IMPLANT_ACTIVATED | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_IMPLANT_EXISTING_UPLINK | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_IMPLANT_IMPLANTING | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_IMPLANT_OTHER | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_INFESTATION_CHARGE_ADD | code/__DEFINES/components.dm | 1 | 1 | code/modules/spells/roguetown/acolyte/pestra.dm, code/modules/spells/roguetown/acolyte/pestra/pestra_components.dm |
| COMSIG_INFESTATION_CHARGE_REMOVE | code/__DEFINES/components.dm | 1 | 1 | code/modules/spells/roguetown/acolyte/pestra/pestra_components.dm, code/modules/spells/roguetown/acolyte/pestra/pestra_components.dm |
| COMSIG_IS_STORAGE_LOCKED | code/__DEFINES/components.dm | 0 | 1 | code/datums/components/storage/storage.dm |
| COMSIG_ITEM_AFTERATTACK | code/__DEFINES/components.dm | 1 | 10 | code/_onclick/item_attack.dm, code/datums/components/igniter.dm, code/datums/components/knockback.dm |
| COMSIG_ITEM_ATTACK | code/__DEFINES/components.dm | 2 | 5 | code/_onclick/item_attack.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/melee/soundbreaker_proxy.dm, code/datums/components/explodable.dm |
| COMSIG_ITEM_ATTACKED_SUCCESS | code/__DEFINES/components.dm | 2 | 1 | code/_onclick/item_attack.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/melee/soundbreaker_proxy.dm, modular_twilight_axis/code/modules/vampire_neu/overrides/death_gifts.dm |
| COMSIG_ITEM_ATTACK_EFFECT | code/__DEFINES/components.dm | 1 | 0 | code/_onclick/item_attack.dm |
| COMSIG_ITEM_ATTACK_EFFECT_SELF | code/__DEFINES/components.dm | 1 | 4 | code/_onclick/item_attack.dm, code/datums/elements/one_time_poison.dm, code/datums/elements/tipped_item.dm |
| COMSIG_ITEM_ATTACK_OBJ | code/__DEFINES/components.dm | 1 | 2 | code/_onclick/item_attack.dm, code/datums/elements/bed_tuckable.dm, code/datums/magic_items/magic_item.dm |
| COMSIG_ITEM_ATTACK_QDELETED | code/__DEFINES/components.dm | 1 | 0 | code/_onclick/item_attack.dm |
| COMSIG_ITEM_ATTACK_SELF | code/__DEFINES/components.dm | 1 | 6 | code/_onclick/item_attack.dm, code/datums/components/art.dm, code/datums/components/punchcooldown.dm |
| COMSIG_ITEM_ATTACK_SUCCESS | code/__DEFINES/components.dm | 2 | 6 | code/_onclick/item_attack.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/melee/soundbreaker_proxy.dm, code/game/objects/items/rogueweapons/melee/blunt.dm |
| COMSIG_ITEM_ATTACK_TURF | code/__DEFINES/components.dm | 1 | 2 | code/_onclick/item_attack.dm, code/datums/magic_items/magic_item.dm, code/game/objects/items/holster_component.dm |
| COMSIG_ITEM_ATTACK_ZONE | code/__DEFINES/components.dm | 2 | 0 | code/modules/mob/living/carbon/carbon_defense.dm, code/modules/mob/living/carbon/human/human_defense.dm |
| COMSIG_ITEM_BROKEN | code/__DEFINES/components.dm | 1 | 2 | code/game/objects/obj_defense.dm, code/modules/jobs/job_types/roguetown/adventurer/types/antag/hag_class/hag_boons/hag_item_repair.dm, code/modules/spells/spell_types/familiar_abilities.dm |
| COMSIG_ITEM_CRAFTED | code/__DEFINES/dcs/signals/signals_objectives.dm | 2 | 2 | code/datums/components/crafting/crafting.dm, code/game/objects/structures/stairs.dm, code/game/gamemodes/personal_objectives/ascendants/zizo/profane_shrines.dm |
| COMSIG_ITEM_DROPPED | code/__DEFINES/components.dm | 1 | 20 | code/game/objects/items.dm, code/datums/components/anti_magic.dm, code/datums/components/armour_filtering.dm |
| COMSIG_ITEM_EQUIPPED | code/__DEFINES/components.dm | 1 | 19 | code/game/objects/items.dm, code/datums/components/anti_magic.dm, code/datums/components/armour_filtering.dm |
| COMSIG_ITEM_GUN_PROCESS_FIRE | code/__DEFINES/components.dm | 1 | 1 | code/modules/projectiles/gun.dm, code/datums/status_effects/rogue/roguebuff.dm |
| COMSIG_ITEM_HIT_REACT | code/__DEFINES/components.dm | 2 | 0 | code/game/objects/items.dm, code/game/objects/items/rogueweapons/shields.dm |
| COMSIG_ITEM_HIT_RESPONSE | code/__DEFINES/components.dm | 1 | 1 | code/game/objects/items.dm, code/datums/magic_items/magic_item.dm |
| COMSIG_ITEM_IMBUE_SOUL | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_ITEM_MARK_RETRIEVAL | code/__DEFINES/components.dm | 2 | 0 | code/modules/spells/spell_types/summonitem.dm, code/modules/spells/spell_types/wizard/utility/summon_weapon.dm |
| COMSIG_ITEM_OBJFIX | code/__DEFINES/components.dm | 1 | 2 | code/game/objects/obj_defense.dm, code/datums/components/psyblessed.dm, code/modules/spells/components/fit_clothing.dm |
| COMSIG_ITEM_PICKUP | code/__DEFINES/components.dm | 1 | 7 | code/game/objects/items.dm, code/datums/components/storage/storage.dm, code/datums/elements/bed_tuckable.dm |
| COMSIG_ITEM_POST_UNEQUIP | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/inventory.dm |
| COMSIG_ITEM_PRE_ATTACK | code/__DEFINES/components.dm | 1 | 3 | code/_onclick/item_attack.dm, code/datums/components/storage/storage.dm, code/datums/elements/tipped_item.dm |
| COMSIG_ITEM_STOLEN | code/__DEFINES/dcs/signals/signals_objectives.dm | 1 | 1 | code/modules/mob/living/carbon/human/steal.dm, code/game/gamemodes/personal_objectives/ascendants/matthios/theft.dm |
| COMSIG_ITEM_WEARERCROSSED | code/__DEFINES/components.dm | 1 | 2 | code/modules/mob/living/living.dm, code/datums/components/slippery.dm, code/datums/components/squeak.dm |
| COMSIG_JOB_RECEIVED | code/__DEFINES/components.dm | 1 | 1 | code/controllers/subsystem/job.dm, modular_twilight_axis/familytree_module/familytree_subsystem_core.dm |
| COMSIG_LIFT_SET_DIRECTION | code/__DEFINES/dcs/signals/signals_tram.dm | 1 | 0 | code/game/machinery/trams_and_elevators/lift_master.dm |
| COMSIG_LIVING_CAN_TRACK | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/living/living.dm |
| COMSIG_LIVING_DEATH | code/__DEFINES/components.dm | 1 | 20 | code/modules/mob/living/death.dm, code/datums/components/familial_bond.dm, code/datums/components/obsession.dm |
| COMSIG_LIVING_DRINKED_LIMB_BLOOD | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 2 | 2 | code/modules/vampire_neu/bloodsuck.dm, modular_twilight_axis/code/modules/vampire_neu/overrides/bloodsuck.dm, code/datums/gods/patrons/inhumen/graggar.dm |
| COMSIG_LIVING_ELECTROCUTE_ACT | code/__DEFINES/components.dm | 1 | 1 | code/modules/mob/living/living_defense.dm, code/modules/surgery/organs/stomach.dm |
| COMSIG_LIVING_EXTINGUISHED | code/__DEFINES/components.dm | 1 | 0 | code/datums/status_effects/firestacker.dm |
| COMSIG_LIVING_GRAB_SELF_ATTEMPT | code/__DEFINES/components.dm | 2 | 1 | code/modules/mob/living/grabbing.dm, code/modules/mob/living/living.dm, code/modules/roguetown/roguemachine/heartbeast/fleshcrafting/flesh_tick.dm |
| COMSIG_LIVING_HEALTH_UPDATE | code/__DEFINES/components.dm | 2 | 2 | code/modules/mob/living/carbon/carbon.dm, code/modules/mob/living/living.dm, code/datums/elements/ai_flee_when_hurt.dm |
| COMSIG_LIVING_IGNITED | code/__DEFINES/components.dm | 1 | 0 | code/datums/status_effects/firestacker.dm |
| COMSIG_LIVING_IMPACT_ZONE | code/__DEFINES/components.dm | 1 | 1 | code/modules/mob/living/living_defense.dm, code/datums/status_effects/rogue/roguebuff.dm |
| COMSIG_LIVING_LIFE | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 1 | 2 | code/modules/mob/living/life.dm, code/datums/status_effects/rogue/debuff.dm, code/datums/status_effects/rogue/roguebuff.dm |
| COMSIG_LIVING_MINOR_SHOCK | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_LIVING_MIRACLE_HEAL_APPLY | code/__DEFINES/components.dm | 2 | 3 | code/datums/status_effects/rogue/roguebuff.dm, code/modules/spells/roguetown/acolyte/pestra/pestra_status_effects.dm, code/modules/spells/roguetown/acolyte/astrata.dm |
| COMSIG_LIVING_ONJUMP | code/__DEFINES/components.dm | 1 | 1 | code/game/objects/items/rogueweapons/mmb/jump.dm, code/datums/status_effects/rogue/roguebuff.dm |
| COMSIG_LIVING_ON_WABBAJACKED | modular_twilight_axis/code/modules/roguetown/rogueantagonists/zizo_cult/thingsforcult.dm | 0 | 0 | - |
| COMSIG_LIVING_PRE_WABBAJACKED | modular_twilight_axis/code/modules/roguetown/rogueantagonists/zizo_cult/thingsforcult.dm | 1 | 0 | modular_twilight_axis/code/modules/roguetown/rogueantagonists/zizo_cult/thingsforcult.dm |
| COMSIG_LIVING_RESIST | code/__DEFINES/components.dm | 1 | 1 | code/modules/mob/living/living.dm, code/datums/status_effects/gas.dm |
| COMSIG_LIVING_REVIVE | code/__DEFINES/components.dm | 1 | 4 | code/modules/mob/living/living.dm, code/datums/components/obsession.dm, code/modules/mob/living/carbon/human/species_types/roguetown/dullahan/dullahan.dm |
| COMSIG_LIVING_SET_RESTING | code/__DEFINES/components.dm | 0 | 1 | code/game/objects/items/bedsheets.dm |
| COMSIG_LIVING_STATUS_IMMOBILIZE | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/living/status_procs.dm |
| COMSIG_LIVING_STATUS_KNOCKDOWN | code/__DEFINES/components.dm | 1 | 4 | code/modules/mob/living/status_procs.dm, code/datums/components/spill.dm, code/modules/spells/pantheon/inhumen/_inhumen_spell_utils.dm |
| COMSIG_LIVING_STATUS_OFFBALANCED | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/living/status_procs.dm |
| COMSIG_LIVING_STATUS_PARALYZE | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/living/status_procs.dm |
| COMSIG_LIVING_STATUS_SLEEP | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/living/status_procs.dm |
| COMSIG_LIVING_STATUS_STUN | code/__DEFINES/components.dm | 1 | 3 | code/modules/mob/living/status_procs.dm, code/modules/spells/pantheon/inhumen/_inhumen_spell_utils.dm, code/modules/spells/spell_types/classunique/desertrider/zeybek_momentum.dm |
| COMSIG_LIVING_STATUS_UNCONSCIOUS | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/living/status_procs.dm |
| COMSIG_LIVING_STOPPED_OFFERING_ITEM | code/__DEFINES/offer.dm | 1 | 1 | code/modules/mob/living/living.dm, code/game/objects/effects/temporary_visuals/offered_item_effect.dm |
| COMSIG_LIVING_SWINGDELAY_MOD | code/__DEFINES/components.dm | 2 | 1 | code/_onclick/item_attack.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/melee/soundbreaker_proxy.dm, code/datums/status_effects/rogue/roguebuff.dm |
| COMSIG_LIVING_TAKE_DAMAGE | modular_twilight_axis/code/_signals.dm | 0 | 0 | - |
| COMSIG_LUX_EXTRACTED | code/__DEFINES/dcs/signals/signals_objectives.dm | 4 | 1 | code/modules/spells/roguetown/necromancer/lacrima.dm, code/modules/surgery/surgeries_hearth/extract_lux.dm, modular_twilight_axis/code/modules/roguetown/rogueantagonists/zizo_cult/thingsforcult.dm |
| COMSIG_LUX_TASTED | code/__DEFINES/dcs/signals/signals_objectives.dm | 1 | 1 | code/datums/status_effects/rogue/roguebuff.dm, code/game/gamemodes/personal_objectives/ascendants/baotha/taste_lux.dm |
| COMSIG_MACHINERY_BROKEN | code/__DEFINES/components.dm | 1 | 0 | code/game/machinery/_machinery.dm |
| COMSIG_MACHINERY_POWER_LOST | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_MACHINERY_POWER_RESTORED | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_MECHA_ACTION_ACTIVATE | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_MIND_TRANSFER | code/__DEFINES/components.dm | 0 | 1 | code/datums/skill_holder.dm |
| COMSIG_MIND_TRANSFERRED | code/__DEFINES/dcs/signals/signals_mob/signals_mind.dm | 1 | 1 | code/datums/mind.dm, code/datums/actions/action.dm |
| COMSIG_MOB_ABILITY_FINISHED | code/__DEFINES/dcs/signals/signals_action.dm | 1 | 0 | code/datums/actions/action_cooldown.dm |
| COMSIG_MOB_ABILITY_STARTED | code/__DEFINES/dcs/signals/signals_action.dm | 1 | 0 | code/datums/actions/action_cooldown.dm |
| COMSIG_MOB_AFTERATTACK_SUCCESS | code/__DEFINES/components.dm | 1 | 1 | code/modules/mob/living/carbon/human/human_defense.dm, code/modules/mob/living/simple_animal/rogue/creacher/undead_animal_helpers.dm |
| COMSIG_MOB_AFTER_SPELL_CAST | code/__DEFINES/dcs/signals/signals_spell.dm | 1 | 0 | code/modules/spells/spell_cooldown.dm |
| COMSIG_MOB_ALLOWED | code/__DEFINES/components.dm | 1 | 0 | code/modules/jobs/access.dm |
| COMSIG_MOB_ALTCLICKON | code/__DEFINES/components.dm | 1 | 0 | code/_onclick/click.dm |
| COMSIG_MOB_APPLY_DAMGE | code/__DEFINES/components.dm | 3 | 13 | code/modules/mob/living/carbon/damage_procs.dm, code/modules/mob/living/carbon/human/species.dm, code/modules/mob/living/damage_procs.dm |
| COMSIG_MOB_ATTACKED_BY_HAND | code/__DEFINES/components.dm | 1 | 3 | code/modules/mob/living/carbon/human/species.dm, code/datums/status_effects/rogue/roguebuff.dm, code/modules/clothing/rogueclothes/armor/regenerating.dm |
| COMSIG_MOB_ATTACK_HAND | code/__DEFINES/components.dm | 1 | 5 | code/modules/mob/living/carbon/human/species.dm, code/modules/spells/roguetown/acolyte/ravox.dm, code/modules/spells/spell_types/wizard/misc/fly.dm |
| COMSIG_MOB_ATTACK_RANGED | code/__DEFINES/components.dm | 1 | 0 | code/_onclick/click.dm |
| COMSIG_MOB_BEFORE_SPELL_CAST | code/__DEFINES/dcs/signals/signals_spell.dm | 1 | 0 | code/modules/spells/spell_cooldown.dm |
| COMSIG_MOB_BREAK_SNEAK | code/__DEFINES/components.dm | 3 | 0 | code/datums/ai/subtrees/human_basic_attack.dm, code/modules/mob/living/living_movement.dm, code/modules/mob/mob_movement.dm |
| COMSIG_MOB_CANCEL_CLICKON | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_MOB_CAST_SPELL | code/__DEFINES/dcs/signals/signals_spell.dm | 1 | 1 | code/modules/spells/spell_cooldown.dm, code/modules/spells/spell_types/wizard/misc/fly.dm |
| COMSIG_MOB_CLICKON | code/__DEFINES/components.dm | 1 | 4 | code/_onclick/click.dm, code/datums/status_effects/debuffs.dm, code/modules/vampire_neu/coven_action.dm |
| COMSIG_MOB_CLIENT_LOGIN | code/__DEFINES/dcs/signals/signals_mob/signals_client.dm | 1 | 2 | code/modules/mob/login.dm, code/datums/components/crafting/crafting.dm, code/modules/sexcon/components/arousal.dm |
| COMSIG_MOB_DEADSAY | code/__DEFINES/components.dm | 0 | 1 | code/datums/components/deadchat_control.dm |
| COMSIG_MOB_DEATH | code/__DEFINES/components.dm | 1 | 9 | code/modules/mob/death.dm, code/datums/components/aggro_board.dm, code/datums/components/combat_vocalizer.dm |
| COMSIG_MOB_DISMEMBER | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 1 | 0 | code/modules/surgery/bodyparts/bodypart_dismemberment.dm |
| COMSIG_MOB_DROPITEM | code/__DEFINES/components.dm | 1 | 6 | code/game/objects/items.dm, code/datums/components/inventory_manager.dm, code/modules/antagonists/roguetown/villain/dreamwalker/dreamwalker_gear.dm |
| COMSIG_MOB_EQUIPPED_ITEM | code/__DEFINES/components.dm | 1 | 9 | code/game/objects/items.dm, code/datums/components/inventory_manager.dm, code/datums/gods/patrons/inhumen/resurrect_inhumen.dm |
| COMSIG_MOB_EXAMINATE | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/mob.dm |
| COMSIG_MOB_GET_STATUS_TAB_ITEMS | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 1 | 0 | code/modules/mob/mob.dm |
| COMSIG_MOB_HUD_CREATED | code/__DEFINES/components.dm | 1 | 0 | code/_onclick/hud/hud.dm |
| COMSIG_MOB_HUGGED | code/__DEFINES/dcs/signals/signals_objectives.dm | 1 | 1 | code/modules/mob/living/emote.dm, code/game/gamemodes/personal_objectives/pantheon/eora/hug.dm |
| COMSIG_MOB_ITEM_AFTERATTACK | code/__DEFINES/components.dm | 1 | 1 | code/_onclick/item_attack.dm, code/datums/status_effects/rogue/roguebuff.dm |
| COMSIG_MOB_ITEM_ATTACK | code/__DEFINES/components.dm | 2 | 9 | code/_onclick/item_attack.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/melee/soundbreaker_proxy.dm, code/datums/status_effects/rogue/roguebuff.dm |
| COMSIG_MOB_ITEM_ATTACK_POST_SWINGDELAY | code/__DEFINES/components.dm | 2 | 4 | code/_onclick/item_attack.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/melee/soundbreaker_proxy.dm, code/modules/spells/spell_types/bardic/crescendo.dm |
| COMSIG_MOB_ITEM_ATTACK_QDELETED | code/__DEFINES/components.dm | 1 | 0 | code/_onclick/item_attack.dm |
| COMSIG_MOB_ITEM_BEING_ATTACKED | code/__DEFINES/components.dm | 2 | 3 | code/_onclick/item_attack.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/melee/soundbreaker_proxy.dm, code/datums/status_effects/rogue/roguebuff.dm |
| COMSIG_MOB_ITEM_POST_SWINGDELAY_ATTACKED | code/__DEFINES/components.dm | 1 | 2 | code/_onclick/item_attack.dm, code/datums/status_effects/rogue/roguebuff.dm, code/modules/spells/pantheon/inhumen/_inhumen_spell_utils.dm |
| COMSIG_MOB_KICKED | code/__DEFINES/components.dm | 2 | 1 | code/game/objects/items/rogueweapons/mmb/kick.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/intents.dm, code/datums/status_effects/rogue/roguebuff.dm |
| COMSIG_MOB_KICKED_SUCCESSFUL | code/__DEFINES/spell_defines.dm | 1 | 0 | code/game/objects/items/rogueweapons/mmb/kick.dm |
| COMSIG_MOB_KICK_ATTACK | code/__DEFINES/_alc_def.dm | 1 | 0 | code/modules/mob/living/carbon/human/species.dm |
| COMSIG_MOB_LOGIN | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 1 | 2 | code/modules/mob/login.dm, code/datums/ai/_ai_controller.dm, modular_twilight_axis/familytree_module/familytree_subsystem_core.dm |
| COMSIG_MOB_LOGOUT | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 1 | 4 | code/modules/mob/logout.dm, code/datums/ai/_ai_controller.dm, code/modules/sexcon/components/arousal.dm |
| COMSIG_MOB_MIDDLECLICKON | code/__DEFINES/components.dm | 1 | 0 | code/_onclick/click.dm |
| COMSIG_MOB_MIND_TRANSFERRED_INTO | code/__DEFINES/dcs/signals/signals_mob/signals_mind.dm | 1 | 0 | code/datums/mind.dm |
| COMSIG_MOB_MIND_TRANSFERRED_OUT_OF | code/__DEFINES/dcs/signals/signals_mob/signals_mind.dm | 1 | 0 | code/datums/mind.dm |
| COMSIG_MOB_MODIFY_AGGRO_LINES | code/__DEFINES/components.dm | 20 | 1 | code/modules/mob/living/carbon/human/npc/bum.dm, code/modules/mob/living/carbon/human/npc/deranged_knight.dm, code/modules/mob/living/carbon/human/npc/drow.dm |
| COMSIG_MOB_MODIFY_DEATH_LINES | code/__DEFINES/components.dm | 0 | 1 | code/datums/components/combat_vocalizer.dm |
| COMSIG_MOB_MOVESPEED_UPDATED | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 1 | 1 | code/modules/mob/mob_movespeed.dm, code/datums/ai/controllers/human_npc.dm |
| COMSIG_MOB_ON_KICK | code/__DEFINES/components.dm | 2 | 1 | code/game/objects/items/rogueweapons/mmb/kick.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/intents.dm, code/datums/status_effects/rogue/roguebuff.dm |
| COMSIG_MOB_ORGAN_REMOVED | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 1 | 1 | code/modules/surgery/organs/organ_internal.dm, code/modules/vampire_neu/clan/_base_clan.dm |
| COMSIG_MOB_OVERLAY_FORCE_REMOVE | code/__DEFINES/dcs/signals/signals_movable.dm | 0 | 1 | code/datums/elements/mob_overlay_effect.dm |
| COMSIG_MOB_OVERLAY_FORCE_UPDATE | code/__DEFINES/dcs/signals/signals_movable.dm | 0 | 1 | code/datums/elements/mob_overlay_effect.dm |
| COMSIG_MOB_PARRY_SUCCESS | modular_twilight_axis/code/_signals.dm | 1 | 2 | modular_twilight_axis/code/datums/combo/combo_ronin.dm, modular_twilight_axis/code/datums/combo/combo_ronin.dm, modular_twilight_axis/code/modules/erp_system/patches/wanderer.dm |
| COMSIG_MOB_POINTED | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/point.dm |
| COMSIG_MOB_PRE_INVOCATION | code/__DEFINES/dcs/signals/signals_spell.dm | 1 | 0 | code/modules/spells/spell_cooldown.dm |
| COMSIG_MOB_QUERY_PARRY_WEAPON | modular_twilight_axis/code/_signals.dm | 1 | 1 | modular_twilight_axis/code/datums/combo/combo_ronin.dm, modular_twilight_axis/code/datums/combo/combo_ronin.dm |
| COMSIG_MOB_RECEIVE_MAGIC | code/__DEFINES/components.dm | 1 | 1 | code/modules/mob/mob.dm, code/datums/components/anti_magic.dm |
| COMSIG_MOB_REMOVED_ACTION | code/__DEFINES/dcs/signals/signals_action.dm | 0 | 0 | - |
| COMSIG_MOB_SAY | code/__DEFINES/components.dm | 1 | 47 | code/modules/mob/living/say.dm, code/datums/ai/hostile/_hostile_controller.dm, code/datums/brain_damage/brain_trauma.dm |
| COMSIG_MOB_SAY_POSTPROCESS | code/__DEFINES/components.dm | 1 | 1 | code/modules/mob/living/say.dm, code/modules/mob/living/carbon/human/species_types/roguetown/dullahan/dullahan.dm |
| COMSIG_MOB_SPELL_ACTIVATED | code/__DEFINES/dcs/signals/signals_spell.dm | 1 | 1 | code/modules/spells/spell_cooldown.dm, code/datums/actions/action_cooldown.dm |
| COMSIG_MOB_STATCHANGE | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 2 | 3 | code/modules/mob/living/simple_animal/simple_animal.dm, code/modules/mob/mob.dm, code/datums/actions/action.dm |
| COMSIG_MOB_THROW | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/living/carbon/carbon.dm |
| COMSIG_MOB_TRY_BARK | code/__DEFINES/components.dm | 1 | 1 | code/datums/ai/subtrees/human_basic_attack.dm, code/datums/components/combat_vocalizer.dm |
| COMSIG_MOB_TRY_EMOTE | code/__DEFINES/components.dm | 0 | 1 | code/datums/components/combat_vocalizer.dm |
| COMSIG_MOB_TWIST_LIMB | code/__DEFINES/_alc_def.dm | 1 | 0 | code/modules/mob/living/grabbing.dm |
| COMSIG_MOB_UNEQUIPPED_ITEM | code/__DEFINES/components.dm | 1 | 2 | code/modules/mob/inventory.dm, code/datums/components/inventory_manager.dm, modular_twilight_axis/code/datums/trophy_hunter.dm |
| COMSIG_MOB_UPDATE_SIGHT | code/__DEFINES/components.dm | 1 | 1 | code/modules/mob/mob.dm, modular_twilight_axis/code/modules/vampire_neu/overrides/death_gifts.dm |
| COMSIG_MOUSEDROPPED_ONTO | code/__DEFINES/components.dm | 1 | 1 | code/_onclick/drag_drop.dm, code/datums/components/storage/storage.dm |
| COMSIG_MOUSEDROP_ONTO | code/__DEFINES/components.dm | 1 | 1 | code/_onclick/drag_drop.dm, code/datums/components/storage/storage.dm |
| COMSIG_MOVABLE_BUCKLE | code/__DEFINES/dcs/signals/signals_movable.dm | 1 | 1 | code/game/objects/buckling.dm, code/datums/components/riding.dm |
| COMSIG_MOVABLE_BUMP | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 4 | code/game/atoms_movable.dm, code/datums/components/explodable.dm, code/datums/components/squeak.dm |
| COMSIG_MOVABLE_BUMP_PUSHED | code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 0 | 1 | code/game/objects/minecart_system/minecart.dm |
| COMSIG_MOVABLE_CROSS | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 0 | code/game/atoms_movable.dm |
| COMSIG_MOVABLE_CROSSED | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 6 | code/game/atoms_movable.dm, code/datums/components/caltrop.dm, code/datums/components/magnetic_catch.dm |
| COMSIG_MOVABLE_DISPOSING | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 0 | 0 | - |
| COMSIG_MOVABLE_HEAR | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 3 | code/game/say.dm, code/datums/brain_damage/brain_trauma.dm, code/datums/status_effects/debuffs.dm |
| COMSIG_MOVABLE_IMPACT | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 2 | 2 | code/game/atoms_movable.dm, code/game/objects/items.dm, code/datums/components/explodable.dm |
| COMSIG_MOVABLE_IMPACT_ZONE | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 0 | code/modules/mob/living/living_defense.dm |
| COMSIG_MOVABLE_LIGHT_OVERLAY_SET_COLOR | code/__DEFINES/dcs/signals_atoms/movable_lighting.dm | 0 | 0 | - |
| COMSIG_MOVABLE_LIGHT_OVERLAY_SET_POWER | code/__DEFINES/dcs/signals_atoms/movable_lighting.dm | 0 | 0 | - |
| COMSIG_MOVABLE_LIGHT_OVERLAY_SET_RANGE | code/__DEFINES/dcs/signals_atoms/movable_lighting.dm | 0 | 0 | - |
| COMSIG_MOVABLE_LIGHT_OVERLAY_TOGGLE_ON | code/__DEFINES/dcs/signals_atoms/movable_lighting.dm | 0 | 0 | - |
| COMSIG_MOVABLE_MOVED | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 56 | code/game/atoms_movable.dm, code/controllers/subsystem/movement/movement_types.dm, code/controllers/subsystem/rogue/fog_event/fog_component.dm |
| COMSIG_MOVABLE_POST_THROW | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 2 | code/game/atoms_movable.dm, code/datums/components/storage/storage.dm, code/modules/roguetown/roguemachine/heartbeast/heart_quirks/quirk_hoarder.dm |
| COMSIG_MOVABLE_PREBUCKLE | code/__DEFINES/dcs/signals/signals_movable.dm | 1 | 1 | code/game/objects/buckling.dm, code/datums/ai/hostile/_hostile_controller.dm |
| COMSIG_MOVABLE_PRE_MOVE | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 3 | code/game/atoms_movable.dm, code/datums/components/tether.dm, code/modules/mob/living/living.dm |
| COMSIG_MOVABLE_PRE_THROW | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 1 | code/game/atoms_movable.dm, code/datums/components/magnetic_catch.dm |
| COMSIG_MOVABLE_SECLUDED_LOCATION | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 0 | code/datums/brain_damage/special.dm |
| COMSIG_MOVABLE_SET_GRAB_STATE | code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 0 | 0 | - |
| COMSIG_MOVABLE_THROW_LANDED | code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 0 | 1 | code/datums/components/after_image.dm |
| COMSIG_MOVABLE_TURF_ENTERED | code/__DEFINES/dcs/signals/signals_turf.dm | 1 | 1 | code/game/turfs/turf.dm, code/game/objects/structures/artstuff.dm |
| COMSIG_MOVABLE_TURF_EXITED | code/__DEFINES/dcs/signals/signals_turf.dm | 1 | 0 | code/game/turfs/turf.dm |
| COMSIG_MOVABLE_UNBUCKLE | code/__DEFINES/dcs/signals/signals_movable.dm | 1 | 1 | code/game/objects/buckling.dm, code/datums/components/riding.dm |
| COMSIG_MOVABLE_UNCROSSED | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 0 | 2 | code/datums/components/magnetic_catch.dm, code/datums/components/swarming.dm |
| COMSIG_MOVABLE_UPDATE_GLIDE_SIZE | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 2 | code/game/atoms_movable.dm, code/datums/components/orbiter.dm, code/game/machinery/trams_and_elevators/industrial_lift.dm |
| COMSIG_MOVABLE_Z_CHANGED | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 2 | code/game/atoms_movable.dm, code/datums/ai/_ai_controller.dm, code/modules/spells/spell_cooldown.dm |
| COMSIG_MOVELOOP_JPS_REPATH | code/__DEFINES/dcs/signals/signals_moveloop.dm | 0 | 0 | - |
| COMSIG_MOVELOOP_POSTPROCESS | code/__DEFINES/dcs/signals/signals_moveloop.dm | 1 | 1 | code/controllers/subsystem/movement/movement_types.dm, code/game/objects/minecart_system/minecart.dm |
| COMSIG_MOVELOOP_PREPROCESS_CHECK | code/__DEFINES/dcs/signals/signals_moveloop.dm | 1 | 2 | code/controllers/subsystem/movement/movement_types.dm, code/datums/components/conveyor_movement.dm, code/game/objects/minecart_system/minecart.dm |
| COMSIG_MOVELOOP_START | code/__DEFINES/dcs/signals/signals_moveloop.dm | 1 | 0 | code/controllers/subsystem/movement/movement_types.dm |
| COMSIG_MOVELOOP_STOP | code/__DEFINES/dcs/signals/signals_moveloop.dm | 1 | 0 | code/controllers/subsystem/movement/movement_types.dm |
| COMSIG_MULTITOOL_REMOVE_BUFFER | code/__DEFINES/components.dm | 1 | 0 | code/game/objects/items/contraption.dm |
| COMSIG_NANITE_ADD_PROGRAM | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_ADJUST_VOLUME | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_COMM_SIGNAL | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_DELETE | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_GET_PROGRAMS | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_GET_VOLUME | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_IS_STEALTHY | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_SCAN | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_SET_CLOUD | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_SET_CLOUD_SYNC | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_SET_MAX_VOLUME | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_SET_REGEN | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_SET_SAFETY | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_SET_VOLUME | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_SIGNAL | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_SYNC | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NANITE_UI_DATA | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_NEW_ICHOR_FANG_SPAWNED | code/__DEFINES/dcs/signals/signals_objectives.dm | 0 | 1 | code/game/objects/items/rogueweapons/melee/swords.dm |
| COMSIG_OBJ_DECONSTRUCT | code/__DEFINES/components.dm | 1 | 1 | code/game/objects/obj_defense.dm, code/datums/components/storage/concrete/_concrete.dm |
| COMSIG_OBJ_DEFAULT_UNFASTEN_WRENCH | code/__DEFINES/components.dm | 1 | 0 | code/game/machinery/_machinery.dm |
| COMSIG_OBJ_HANDED_OVER | code/__DEFINES/offer.dm | 1 | 3 | code/modules/mob/living/living.dm, code/game/objects/effects/temporary_visuals/offered_item_effect.dm, code/modules/jobs/job_types/roguetown/adventurer/types/antag/hag_class/hag_boon_item.dm |
| COMSIG_OBJ_SETANCHORED | code/__DEFINES/components.dm | 1 | 0 | code/game/objects/objs.dm |
| COMSIG_OBJ_TAKE_DAMAGE | code/__DEFINES/components.dm | 1 | 2 | code/game/objects/obj_defense.dm, code/datums/components/layer_armor.dm, code/modules/antagonists/roguetown/villain/dreamwalker/dreamwalker_gear.dm |
| COMSIG_ORGAN_CONSUMED | code/__DEFINES/dcs/signals/signals_objectives.dm | 1 | 1 | code/modules/surgery/organs/organ_internal.dm, code/game/gamemodes/personal_objectives/ascendants/graggar/eat_organs.dm |
| COMSIG_PARENT_ATTACKBY | code/__DEFINES/components.dm | 1 | 7 | code/_onclick/item_attack.dm, code/datums/components/construction.dm, code/datums/components/explodable.dm |
| COMSIG_PARENT_EXAMINE | code/__DEFINES/components.dm | 3 | 28 | code/game/atoms.dm, code/modules/mob/living/carbon/examine.dm, code/modules/mob/living/carbon/human/examine.dm |
| COMSIG_PARENT_PREQDELETED | code/__DEFINES/components.dm | 1 | 1 | code/controllers/subsystem/garbage.dm, code/datums/ai/_ai_controller.dm |
| COMSIG_PARENT_QDELETING | code/__DEFINES/components.dm | 1 | 51 | code/controllers/subsystem/garbage.dm, code/_onclick/drag_drop.dm, code/controllers/admin.dm |
| COMSIG_PDA_CHANGE_RINGTONE | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_PDA_CHECK_DETONATE | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_PEN_ROTATED | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_POWER_ACTIVATE | code/__DEFINES/dcs/signals/signals_coven_powers.dm | 1 | 1 | code/modules/vampire_neu/covens/coven_powers/_base_power.dm, code/modules/vampire_neu/covens/coven_powers/_base_power.dm |
| COMSIG_POWER_ACTIVATE_ON | code/__DEFINES/dcs/signals/signals_coven_powers.dm | 1 | 0 | code/modules/vampire_neu/covens/coven_powers/_base_power.dm |
| COMSIG_POWER_DEACTIVATE | code/__DEFINES/dcs/signals/signals_coven_powers.dm | 1 | 0 | code/modules/vampire_neu/covens/coven_powers/_base_power.dm |
| COMSIG_POWER_DEACTIVATE_ON | code/__DEFINES/dcs/signals/signals_coven_powers.dm | 1 | 0 | code/modules/vampire_neu/covens/coven_powers/_base_power.dm |
| COMSIG_POWER_PRE_ACTIVATION | code/__DEFINES/dcs/signals/signals_coven_powers.dm | 1 | 0 | code/modules/vampire_neu/covens/coven_powers/_base_power.dm |
| COMSIG_POWER_PRE_ACTIVATION_ON | code/__DEFINES/dcs/signals/signals_coven_powers.dm | 1 | 0 | code/modules/vampire_neu/covens/coven_powers/_base_power.dm |
| COMSIG_POWER_TRY_ACTIVATE | code/__DEFINES/dcs/signals/signals_coven_powers.dm | 1 | 0 | code/modules/vampire_neu/covens/coven_powers/_base_power.dm |
| COMSIG_POWER_TRY_ACTIVATE_ON | code/__DEFINES/dcs/signals/signals_coven_powers.dm | 1 | 0 | code/modules/vampire_neu/covens/coven_powers/_base_power.dm |
| COMSIG_POWER_TRY_DEACTIVATE | code/__DEFINES/dcs/signals/signals_coven_powers.dm | 1 | 0 | code/modules/vampire_neu/covens/coven_powers/_base_power.dm |
| COMSIG_POWER_TRY_DEACTIVATE_ON | code/__DEFINES/dcs/signals/signals_coven_powers.dm | 1 | 0 | code/modules/vampire_neu/covens/coven_powers/_base_power.dm |
| COMSIG_PREQDELETED | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_PROCESS_BORGCHARGER_OCCUPANT | code/__DEFINES/components.dm | 0 | 1 | code/modules/surgery/organs/stomach.dm |
| COMSIG_PROJECTILE_ATTACK_EFFECT | code/__DEFINES/components.dm | 1 | 0 | code/game/objects/items/rogueweapons/ranged/_ammo.dm |
| COMSIG_PROJECTILE_ATTACK_EFFECT_SELF | code/__DEFINES/components.dm | 1 | 0 | code/game/objects/items/rogueweapons/ranged/_ammo.dm |
| COMSIG_PROJECTILE_BEFORE_FIRE | code/__DEFINES/components.dm | 1 | 0 | code/modules/projectiles/projectile.dm |
| COMSIG_PROJECTILE_ON_HIT | code/__DEFINES/components.dm | 1 | 6 | code/modules/projectiles/projectile.dm, code/datums/components/igniter.dm, code/datums/components/knockback.dm |
| COMSIG_PROJECTILE_PREHIT | code/__DEFINES/components.dm | 1 | 0 | code/modules/projectiles/projectile.dm |
| COMSIG_PROJECTILE_SELF_ON_HIT | code/__DEFINES/components.dm | 1 | 1 | code/modules/projectiles/projectile.dm, code/modules/spells/spell_cooldown_projectile.dm |
| COMSIG_QDELETING | code/__DEFINES/components.dm | 0 | 13 | code/controllers/subsystem/spatial_gridmap.dm, code/controllers/subsystem/ticker.dm, code/datums/components/conveyor_movement.dm |
| COMSIG_RADIO_NEW_FREQUENCY | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_RIDDEN_DRIVER_MOVE | code/__DEFINES/dcs/signals/signals_movable.dm | 0 | 1 | code/datums/ai/hostile/_hostile_controller.dm |
| COMSIG_ROTTEN_FOOD_EATEN | code/__DEFINES/dcs/signals/signals_objectives.dm | 1 | 1 | code/modules/food_and_drinks/food/snacks.dm, code/game/gamemodes/personal_objectives/pantheon/pestra/eat_rotten_food.dm |
| COMSIG_SACRED_TREE_DAMAGED | code/__DEFINES/dcs/signals/signals_global.dm | 0 | 1 | code/datums/components/druids/wise_tree.dm |
| COMSIG_SEX_ADJUST_AROUSAL | code/__DEFINES/sex.dm | 4 | 1 | code/datums/sexcon2/sex_session.dm, modular_twilight_axis/code/datums/sexcon/sexcon_reagents.dm, modular_twilight_axis/code/modules/erp_system/components/erp_relations.dm |
| COMSIG_SEX_AROUSAL_CHANGED | code/__DEFINES/sex.dm | 1 | 4 | code/modules/sexcon/components/arousal.dm, code/datums/sexcon2/sex_session.dm, code/modules/sexcon/sex_organs/penis.dm |
| COMSIG_SEX_CAN_USE_PENIS | code/__DEFINES/sex.dm | 0 | 0 | - |
| COMSIG_SEX_CLIMAX | code/__DEFINES/sex.dm | 2 | 2 | code/modules/sexcon/components/arousal.dm, modular_twilight_axis/code/modules/erp_system/patches/arousal.dm, code/datums/sexcon2/sex_session.dm |
| COMSIG_SEX_CONSIDERED_LIMP | code/__DEFINES/sex.dm | 0 | 0 | - |
| COMSIG_SEX_FREEZE_AROUSAL | code/__DEFINES/sex.dm | 3 | 1 | code/datums/sexcon2/sex_session.dm, modular_twilight_axis/code/datums/sexcon/sexcon_reagents.dm, modular_twilight_axis/code/modules/erp_system/core/controller/erp_controller.dm |
| COMSIG_SEX_GET_AROUSAL | code/__DEFINES/sex.dm | 17 | 1 | code/datums/mob_descriptors/descriptors/other.dm, code/datums/sexcon2/sex_session.dm, code/datums/sexcon2/sex_status.dm |
| COMSIG_SEX_JOSTLE | code/__DEFINES/sex.dm | 1 | 1 | code/datums/sexcon2/sex_procs.dm, code/datums/item_equipped_movement_rustle.dm |
| COMSIG_SEX_MODIFY_EFFECT | modular_twilight_axis/code/modules/erp_system/_defines.dm | 1 | 1 | modular_twilight_axis/code/modules/erp_system/patches/arousal.dm, modular_twilight_axis/code/modules/erp_system/additionals/erp_modifiers.dm |
| COMSIG_SEX_RECEIVE_ACTION | code/__DEFINES/sex.dm | 4 | 1 | code/datums/sexcon2/sex_session.dm, modular_twilight_axis/code/modules/erp_system/actor/erp_actor.dm, modular_twilight_axis/code/modules/erp_system/additionals/erp_emotes.dm |
| COMSIG_SEX_REMOVE_KNOT | code/__DEFINES/sex.dm | 1 | 1 | code/datums/sexcon2/sex_status.dm, code/modules/sexcon/components/knotting.dm |
| COMSIG_SEX_SET_AROUSAL | code/__DEFINES/sex.dm | 5 | 1 | code/datums/sexcon2/sex_session.dm, code/modules/sexcon/components/arousal.dm, modular_twilight_axis/code/datums/sexcon/sexcon_reagents.dm |
| COMSIG_SEX_TRY_KNOT | code/__DEFINES/sex.dm | 2 | 1 | code/datums/sexcon2/actions/_base_action.dm, code/datums/sexcon2/actions/sex/other/_base.dm, code/modules/sexcon/components/knotting.dm |
| COMSIG_SIMPLEMOB_POST_ATTACK_RANGED | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 0 | 0 | - |
| COMSIG_SIMPLEMOB_PRE_ATTACK_RANGED | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 0 | 0 | - |
| COMSIG_SKILL_RANK_INCREASED | code/__DEFINES/dcs/signals/signals_objectives.dm | 1 | 3 | code/datums/skill_holder.dm, code/game/gamemodes/personal_objectives/pantheon/malum/improve_craft.dm, code/game/gamemodes/personal_objectives/pantheon/noc/get_literate.dm |
| COMSIG_SLEEPING_ON_BED | code/__DEFINES/components.dm | 1 | 1 | code/modules/mob/living/carbon/life.dm, code/modules/spells/roguetown/acolyte/eora/eora_bed.dm |
| COMSIG_SLEEPY_TIME | code/__DEFINES/components.dm | 1 | 1 | code/controllers/subsystem/nightshift.dm, code/modules/jobs/job_types/roguetown/adventurer/types/antag/hag_class/hag_curses/hag_curses_effects.dm |
| COMSIG_SOUNDBREAKER_COMBO_CLEARED | modular_twilight_axis/code/_signals.dm | 1 | 1 | modular_twilight_axis/code/datums/status_effects/rogue/soundbreaker.dm, modular_twilight_axis/code/datums/combo/soundbreaker/combo_soundbreaker.dm |
| COMSIG_SOUNDBREAKER_KICK_SUCCESS | modular_twilight_axis/code/_signals.dm | 1 | 1 | modular_twilight_axis/code/game/objects/items/rogueweapons/intents.dm, modular_twilight_axis/code/datums/combo/soundbreaker/combo_soundbreaker.dm |
| COMSIG_SOUNDBREAKER_NOTE_PROJECTILE_HIT | modular_twilight_axis/code/_signals.dm | 0 | 1 | modular_twilight_axis/code/datums/combo/soundbreaker/combo_soundbreaker.dm |
| COMSIG_SOUNDBREAKER_PRIME_NOTE | modular_twilight_axis/code/_signals.dm | 0 | 1 | modular_twilight_axis/code/datums/combo/soundbreaker/combo_soundbreaker.dm |
| COMSIG_SOUNDBREAKER_RIFF_DEFENSE_SUCCESS | modular_twilight_axis/code/_signals.dm | 1 | 1 | modular_twilight_axis/code/datums/combo/soundbreaker/combo_soundbreaker.dm, modular_twilight_axis/code/datums/combo/soundbreaker/combo_soundbreaker.dm |
| COMSIG_SPECIES_GAIN | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/living/carbon/human/species.dm |
| COMSIG_SPECIES_LOSS | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/living/carbon/human/species.dm |
| COMSIG_SPELL_AFTER_CAST | code/__DEFINES/dcs/signals/signals_spell.dm | 1 | 0 | code/modules/spells/spell_cooldown.dm |
| COMSIG_SPELL_BEFORE_CAST | code/__DEFINES/dcs/signals/signals_spell.dm | 1 | 0 | code/modules/spells/spell_cooldown.dm |
| COMSIG_SPELL_CAST | code/__DEFINES/dcs/signals/signals_spell.dm | 1 | 0 | code/modules/spells/spell_cooldown.dm |
| COMSIG_SPELL_CAST_RESET | code/__DEFINES/dcs/signals/signals_spell.dm | 1 | 0 | code/modules/spells/spell_cooldown.dm |
| COMSIG_SPELL_PROJECTILE_HIT | code/__DEFINES/dcs/signals/signals_spell.dm | 1 | 0 | code/modules/spells/spell_cooldown_projectile.dm |
| COMSIG_SPELL_TOUCH_HAND_HIT | code/__DEFINES/dcs/signals/signals_spell.dm | 1 | 0 | code/modules/spells/spell_touch.dm |
| COMSIG_STATUS_EFFECT_HAG_CURSE_CLEARED | code/__DEFINES/components.dm | 2 | 1 | code/modules/jobs/job_types/roguetown/adventurer/types/antag/hag_class/hag_boons/hag_buffs.dm, code/modules/jobs/job_types/roguetown/adventurer/types/antag/hag_class/hag_debuffs.dm, code/modules/jobs/job_types/roguetown/adventurer/types/antag/hag_class/hag_component.dm |
| COMSIG_STORAGE_ADDED | code/__DEFINES/components.dm | 1 | 1 | code/game/objects/items/storage/new_storage/tetris.dm, code/datums/components/inventory_manager.dm |
| COMSIG_STORAGE_BLOCK_USER_TAKE | code/game/objects/items/storage/new_storage/tetris.dm | 0 | 1 | code/game/objects/items/storage/new_storage/tetris.dm |
| COMSIG_STRUCTURE_ATTACKBY | code/__DEFINES/components.dm | 1 | 1 | code/game/objects/items/rogueweapons/integrity.dm, code/game/objects/items/rogueweapons/melee/special.dm |
| COMSIG_SUBSYSTEM_POST_INITIALIZE | code/__DEFINES/dcs/signals/signals_subsystems.dm | 1 | 1 | code/controllers/subsystem.dm, code/_onclick/hud/new_player.dm |
| COMSIG_TGUI_WINDOW_VISIBLE | code/__DEFINES/dcs/signals/signals_tgui.dm | 1 | 0 | code/modules/tgui/tgui_window.dm |
| COMSIG_TICKER_ENTER_PREGAME | code/__DEFINES/dcs/signals/signals_subsystems.dm | 1 | 0 | code/controllers/subsystem/ticker.dm |
| COMSIG_TICKER_ENTER_SETTING_UP | code/__DEFINES/dcs/signals/signals_subsystems.dm | 1 | 1 | code/controllers/subsystem/ticker.dm, code/_onclick/hud/new_player.dm |
| COMSIG_TICKER_ERROR_SETTING_UP | code/__DEFINES/dcs/signals/signals_subsystems.dm | 1 | 1 | code/controllers/subsystem/ticker.dm, code/_onclick/hud/new_player.dm |
| COMSIG_TICKER_ROUND_STARTING | code/__DEFINES/dcs/signals/signals_subsystems.dm | 0 | 0 | - |
| COMSIG_TICKER_RULERMOB_SET | code/__DEFINES/dcs/signals/signals_global.dm | 0 | 1 | code/game/objects/structures/crates_lockers/roguetown.dm |
| COMSIG_TOPIC | code/__DEFINES/components.dm | 1 | 2 | code/datums/datum.dm, code/datums/components/storage/storage.dm, code/datums/slapcrafting.dm |
| COMSIG_TORTURE_PERFORMED | code/__DEFINES/dcs/signals/signals_objectives.dm | 0 | 1 | code/game/gamemodes/personal_objectives/ascendants/zizo/torture.dm |
| COMSIG_TRAIT_GAIN | code/__DEFINES/components.dm | 1 | 0 | code/__DEFINES/traits.dm |
| COMSIG_TRAIT_LOSS | code/__DEFINES/components.dm | 1 | 0 | code/__DEFINES/traits.dm |
| COMSIG_TRAM_COLLISION | code/__DEFINES/dcs/signals/signals_tram.dm | 0 | 0 | - |
| COMSIG_TRAM_EMPTY | code/__DEFINES/dcs/signals/signals_tram.dm | 1 | 2 | code/game/machinery/trams_and_elevators/industrial_lift.dm, code/controllers/subsystem/merchant.dm, code/game/machinery/trams_and_elevators/tram/cargo_line.dm |
| COMSIG_TRAM_REACHED_PLATFORM | code/__DEFINES/dcs/signals/signals_tram.dm | 1 | 1 | code/game/machinery/trams_and_elevators/tram/tram_lift_master.dm, code/game/machinery/trams_and_elevators/tram/tram_landmark_setnext.dm |
| COMSIG_TRAM_SET_TRAVELLING | code/__DEFINES/dcs/signals/signals_tram.dm | 2 | 0 | code/game/machinery/trams_and_elevators/industrial_lift.dm, code/game/machinery/trams_and_elevators/tram/tram_lift_master.dm |
| COMSIG_TRAM_TRAVEL | code/__DEFINES/dcs/signals/signals_tram.dm | 1 | 0 | code/game/machinery/trams_and_elevators/tram/tram_lift_master.dm |
| COMSIG_TREE_TRANSFORMED | code/__DEFINES/dcs/signals/signals_objectives.dm | 1 | 1 | code/modules/spells/roguetown/create_wise_tree.dm, code/game/gamemodes/personal_objectives/pantheon/dendor/make_wise_trees.dm |
| COMSIG_TRY_STORAGE_CAN_INSERT | code/__DEFINES/components.dm | 1 | 1 | code/modules/mob/living/carbon/human/species.dm, code/datums/components/storage/storage.dm |
| COMSIG_TRY_STORAGE_FILL_TYPE | code/__DEFINES/components.dm | 1 | 1 | code/game/objects/items/storage/fancy.dm, code/datums/components/storage/storage.dm |
| COMSIG_TRY_STORAGE_HIDE_ALL | code/__DEFINES/components.dm | 0 | 1 | code/datums/components/storage/storage.dm |
| COMSIG_TRY_STORAGE_HIDE_FROM | code/__DEFINES/components.dm | 0 | 1 | code/datums/components/storage/storage.dm |
| COMSIG_TRY_STORAGE_INSERT | code/__DEFINES/components.dm | 12 | 2 | code/datums/outfit.dm, code/game/objects/items/rogueitems/keyrings.dm, code/game/objects/items/storage/new_storage/tetris.dm |
| COMSIG_TRY_STORAGE_QUICK_EMPTY | code/__DEFINES/components.dm | 3 | 1 | code/game/objects/items/storage/bags.dm, code/game/objects/structures/tables_racks.dm, code/modules/roguetown/roguejobs/artificer/artificer_table.dm |
| COMSIG_TRY_STORAGE_RETURN_INVENTORY | code/__DEFINES/components.dm | 3 | 1 | code/datums/components/storage/storage.dm, code/modules/clothing/outfits/vv_outfit.dm, code/modules/mob/living/living.dm |
| COMSIG_TRY_STORAGE_SET_LOCKSTATE | code/__DEFINES/components.dm | 0 | 1 | code/datums/components/storage/storage.dm |
| COMSIG_TRY_STORAGE_SHOW | code/__DEFINES/components.dm | 0 | 1 | code/datums/components/storage/storage.dm |
| COMSIG_TRY_STORAGE_TAKE | code/__DEFINES/components.dm | 5 | 1 | code/game/objects/items.dm, code/game/objects/items/storage/fancy.dm, code/game/objects/items/storage/new_storage/tetris.dm |
| COMSIG_TRY_STORAGE_TAKE_TYPE | code/__DEFINES/components.dm | 0 | 1 | code/datums/components/storage/storage.dm |
| COMSIG_TURF_CHANGE | code/__DEFINES/components.dm | 1 | 0 | code/game/turfs/change_turf.dm |
| COMSIG_TURF_ENTER | code/__DEFINES/dcs/signals/signals_turf.dm | 0 | 0 | - |
| COMSIG_TURF_ENTERED | code/__DEFINES/dcs/signals/signals_turf.dm | 1 | 1 | code/game/turfs/turf.dm, code/datums/elements/mob_overlay_effect.dm |
| COMSIG_TURF_EXITED | code/__DEFINES/dcs/signals/signals_turf.dm | 1 | 1 | code/game/turfs/turf.dm, code/datums/elements/mob_overlay_effect.dm |
| COMSIG_TURF_INDUSTRIAL_LIFT_ENTER | code/__DEFINES/dcs/signals/signals_tram.dm | 1 | 0 | code/game/machinery/trams_and_elevators/industrial_lift.dm |
| COMSIG_TURF_IS_WET | code/__DEFINES/components.dm | 0 | 1 | code/datums/components/wet_floor.dm |
| COMSIG_TURF_MAKE_DRY | code/__DEFINES/components.dm | 1 | 1 | code/game/turfs/open/_open.dm, code/datums/components/wet_floor.dm |
| COMSIG_TURF_MULTIZ_NEW | code/__DEFINES/components.dm | 1 | 0 | code/game/turfs/turf.dm |
| COMSIG_TURF_PREPARE_STEP_SOUND | code/__DEFINES/dcs/signals/signals_turf.dm | 0 | 0 | - |
| COMSIG_UI_ACT | code/__DEFINES/dcs/signals/signals_datum.dm | 1 | 0 | code/modules/tgui/external.dm |
| COMSIG_VICIOUSLY_MOCKED | code/__DEFINES/dcs/signals/signals_objectives.dm | 2 | 1 | code/modules/spells/pantheon/divine/undivided.dm, code/modules/spells/spell_types/bardic/vicious_mockery.dm, code/game/gamemodes/personal_objectives/pantheon/xylix/mock.dm |
| COMSIG_WARDED_TRAIT_CHANGE | code/__DEFINES/components.dm | 2 | 1 | code/controllers/subsystem/rogue/fog_event/fog_grace_effect.dm, code/controllers/subsystem/rogue/fog_event/fog_ward_effect.dm, code/controllers/subsystem/rogue/fog_event/fog_component.dm |
