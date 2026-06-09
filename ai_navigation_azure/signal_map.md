# Signal Map

Generated for Azure-Peak from active `COMSIG_*` definitions in `code/__DEFINES/**` and active non-comment references in `code/**` + `modular/**`.

- Active global `COMSIG_*` defines in `code/__DEFINES/**`: **427**
- Local/file-scoped `COMSIG_*` defines outside `code/__DEFINES/**`: **1**
- Signals referenced in active code: **429**
- Signals with `SEND_SIGNAL` call sites: **316**
- Signals with `RegisterSignal` call sites: **232**

## How To Use This Map

| Need | Open |
|---|---|
| Spells, miracles, cooldown actions | `ai_navigation/spell_signal_map.md` |
| Melee, projectiles, attack chains | `ai_navigation/combat_signal_map.md` |
| Movement, pull, buckle, throw, moveloops | `ai_navigation/movement_signal_map.md` |
| Generic component/element behavior | Search the signal below, then inspect defining file and listeners. |

## Definition Files

| File | Active COMSIG defines |
|---|---:|
| `code/__DEFINES/ai/_ai.dm` | 3 |
| `code/__DEFINES/components.dm` | 270 |
| `code/__DEFINES/cooldowns.dm` | 2 |
| `code/__DEFINES/dcs/signals/signals_action.dm` | 8 |
| `code/__DEFINES/dcs/signals/signals_ai.dm` | 5 |
| `code/__DEFINES/dcs/signals/signals_coven_powers.dm` | 10 |
| `code/__DEFINES/dcs/signals/signals_datum.dm` | 1 |
| `code/__DEFINES/dcs/signals/signals_global.dm` | 2 |
| `code/__DEFINES/dcs/signals/signals_mob/signals_client.dm` | 4 |
| `code/__DEFINES/dcs/signals/signals_mob/signals_mind.dm` | 3 |
| `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 16 |
| `code/__DEFINES/dcs/signals/signals_movable.dm` | 6 |
| `code/__DEFINES/dcs/signals/signals_moveloop.dm` | 5 |
| `code/__DEFINES/dcs/signals/signals_objectives.dm` | 19 |
| `code/__DEFINES/dcs/signals/signals_spell.dm` | 11 |
| `code/__DEFINES/dcs/signals/signals_tgui.dm` | 1 |
| `code/__DEFINES/dcs/signals/signals_tram.dm` | 8 |
| `code/__DEFINES/dcs/signals/signals_turf.dm` | 5 |
| `code/__DEFINES/dcs/signals_atoms/appearance.dm` | 8 |
| `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 13 |
| `code/__DEFINES/dcs/signals_atoms/movable_lighting.dm` | 4 |
| `code/__DEFINES/dcs/signals_atoms/signals_atom.dm` | 5 |
| `code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm` | 5 |
| `code/__DEFINES/offer.dm` | 2 |
| `code/__DEFINES/sex.dm` | 12 |
| `code/__DEFINES/spell_defines.dm` | 1 |

## Local / File-Scoped COMSIG Defines

| Signal | File | Notes |
|---|---|---|
| `COMSIG_STORAGE_BLOCK_USER_TAKE` | `code/game/objects/items/storage/new_storage/tetris.dm` | Local storage-grid signal; defined near the top of the file and `#undef`d at EOF. |

## Signal Index

| Signal | Define file(s) | SEND files | Register files |
|---|---|---:|---:|
| `COMSIG_ABYSSOID_CREATED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 1 |
| `COMSIG_ACTION_COOLDOWN_ENDED` | `code/__DEFINES/dcs/signals/signals_action.dm` | 1 | 0 |
| `COMSIG_ACTION_GRANTED` | `code/__DEFINES/dcs/signals/signals_action.dm` | 1 | 0 |
| `COMSIG_ACTION_OVERLAY_APPLY` | `code/__DEFINES/dcs/signals/signals_action.dm` | 1 | 1 |
| `COMSIG_ACTION_REMOVED` | `code/__DEFINES/dcs/signals/signals_action.dm` | 1 | 0 |
| `COMSIG_ACTION_TRIGGER` | `code/__DEFINES/dcs/signals/signals_action.dm` | 1 | 0 |
| `COMSIG_AFTER_STORAGE_INSERT` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_AFTER_STORAGE_REMOVE` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_AI_BLACKBOARD_KEY_CLEARED` | `code/__DEFINES/ai/_ai.dm` | 1 | 2 |
| `COMSIG_AI_BLACKBOARD_KEY_SET` | `code/__DEFINES/ai/_ai.dm` | 1 | 3 |
| `COMSIG_AI_CONTROLLER_PICKED_BEHAVIORS` | `code/__DEFINES/ai/_ai.dm` | 1 | 2 |
| `COMSIG_AI_FUTURE_PATH_GENERATED` | `code/__DEFINES/dcs/signals/signals_ai.dm` | 1 | 0 |
| `COMSIG_AI_GENERAL_CHANGE` | `code/__DEFINES/dcs/signals/signals_ai.dm` | 2 | 0 |
| `COMSIG_AI_MOVEMENT_SET` | `code/__DEFINES/dcs/signals/signals_ai.dm` | 0 | 0 |
| `COMSIG_AI_PATH_GENERATED` | `code/__DEFINES/dcs/signals/signals_ai.dm` | 1 | 0 |
| `COMSIG_AI_PATH_SWAPPED` | `code/__DEFINES/dcs/signals/signals_ai.dm` | 1 | 0 |
| `COMSIG_ANIMAL_TAMED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 1 |
| `COMSIG_AREA_ENTERED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_AREA_EXITED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ATOM_ACID_ACT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ATOM_ADD_TRAIT` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_ATOM_AFTER_SUCCESSFUL_INITIALIZE` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ATOM_AFTER_SUCCESSFUL_INITIALIZED_ON` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_ANALYSER_ACT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ATOM_ATTACKBY` | `code/__DEFINES/dcs/signals_atoms/signals_atom.dm` | 0 | 3 |
| `COMSIG_ATOM_ATTACK_ANIMAL` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_ATTACK_GHOST` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_ATTACK_HAND` | `code/__DEFINES/components.dm` | 2 | 5 |
| `COMSIG_ATOM_ATTACK_PAW` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_ATOM_ATTACK_RIGHT` | `code/__DEFINES/components.dm` | 1 | 3 |
| `COMSIG_ATOM_BLOB_ACT` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_ATOM_BLOCKS_BSA_BEAM` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_ATOM_BSA_BEAM` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_ATOM_BULLET_ACT` | `code/__DEFINES/components.dm` | 2 | 2 |
| `COMSIG_ATOM_BUMPED` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_CANREACH` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_CONTENTS_DEL` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_CROWBAR_ACT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ATOM_DIR_CHANGE` | `code/__DEFINES/components.dm` | 1 | 5 |
| `COMSIG_ATOM_EMAG_ACT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ATOM_EMP_ACT` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_ENTERED` | `code/__DEFINES/components.dm` | 1 | 5 |
| `COMSIG_ATOM_EXAMINE` | `code/__DEFINES/dcs/signals_atoms/signals_atom.dm` | 0 | 0 |
| `COMSIG_ATOM_EXAMINE_MORE` | `code/__DEFINES/dcs/signals_atoms/signals_atom.dm` | 0 | 1 |
| `COMSIG_ATOM_EXAMINE_TAGS` | `code/__DEFINES/dcs/signals_atoms/signals_atom.dm` | 0 | 1 |
| `COMSIG_ATOM_EXIT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ATOM_EXITED` | `code/__DEFINES/components.dm` | 1 | 3 |
| `COMSIG_ATOM_EX_ACT` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_FIRE_ACT` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_GET_EXAMINE_NAME` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_HITBY` | `code/__DEFINES/dcs/signals_atoms/signals_atom.dm` | 2 | 1 |
| `COMSIG_ATOM_INITIALIZED_ON` | active reference in `code/datums/proximity_monitor/proximity_monitor.dm`; no local define in `code/__DEFINES/**` | 0 | 0 |
| `COMSIG_ATOM_INTERCEPT_TELEPORT` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_INTERCEPT_Z_FALL` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ATOM_MULTITOOL_ACT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ATOM_NARSIE_ACT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ATOM_NO_UPDATE_DESC` | `code/__DEFINES/dcs/signals_atoms/appearance.dm` | 0 | 0 |
| `COMSIG_ATOM_NO_UPDATE_ICON` | `code/__DEFINES/dcs/signals_atoms/appearance.dm` | 0 | 0 |
| `COMSIG_ATOM_NO_UPDATE_ICON_STATE` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_ATOM_NO_UPDATE_NAME` | `code/__DEFINES/dcs/signals_atoms/appearance.dm` | 0 | 0 |
| `COMSIG_ATOM_NO_UPDATE_OVERLAYS` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_ATOM_ORBIT_BEGIN` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_ORBIT_STOP` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_REMOVE_TRAIT` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_ATOM_SCREWDRIVER_ACT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ATOM_SET_LIGHT` | `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 1 | 0 |
| `COMSIG_ATOM_SET_LIGHT_COLOR` | `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 2 | 1 |
| `COMSIG_ATOM_SET_LIGHT_CURVE` | `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 1 | 0 |
| `COMSIG_ATOM_SET_LIGHT_FLAGS` | `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 0 | 1 |
| `COMSIG_ATOM_SET_LIGHT_ON` | `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 1 | 1 |
| `COMSIG_ATOM_SET_LIGHT_POWER` | `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 2 | 1 |
| `COMSIG_ATOM_SET_LIGHT_RANGE` | `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 2 | 1 |
| `COMSIG_ATOM_UPDATED_ICON` | `code/__DEFINES/dcs/signals_atoms/appearance.dm` | 0 | 1 |
| `COMSIG_ATOM_UPDATE_APPEARANCE` | `code/__DEFINES/dcs/signals_atoms/appearance.dm` | 1 | 0 |
| `COMSIG_ATOM_UPDATE_DESC` | `code/__DEFINES/dcs/signals_atoms/appearance.dm` | 1 | 0 |
| `COMSIG_ATOM_UPDATE_ICON` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_UPDATE_ICON_STATE` | `code/__DEFINES/dcs/signals_atoms/appearance.dm` | 0 | 0 |
| `COMSIG_ATOM_UPDATE_LIGHT_COLOR` | `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 1 | 0 |
| `COMSIG_ATOM_UPDATE_LIGHT_CURVE` | `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 1 | 0 |
| `COMSIG_ATOM_UPDATE_LIGHT_FLAGS` | `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 0 | 0 |
| `COMSIG_ATOM_UPDATE_LIGHT_ON` | `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 1 | 0 |
| `COMSIG_ATOM_UPDATE_LIGHT_POWER` | `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 1 | 0 |
| `COMSIG_ATOM_UPDATE_LIGHT_RANGE` | `code/__DEFINES/dcs/signals_atoms/lighting.dm` | 1 | 0 |
| `COMSIG_ATOM_UPDATE_NAME` | `code/__DEFINES/dcs/signals_atoms/appearance.dm` | 1 | 0 |
| `COMSIG_ATOM_UPDATE_OVERLAYS` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ATOM_WAS_ATTACKED` | `code/__DEFINES/components.dm` | 2 | 5 |
| `COMSIG_ATOM_WELDER_ACT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ATOM_WIRECUTTER_ACT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ATOM_WRENCH_ACT` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_BORG_SAFE_DECONSTRUCT` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_CARBON_PRAY` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 1 | 0 |
| `COMSIG_CARBON_SOUNDBANG` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_CARBON_SWAPHANDS` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_CD_RESET` | `code/__DEFINES/cooldowns.dm` | 1 | 0 |
| `COMSIG_CD_STOP` | `code/__DEFINES/cooldowns.dm` | 1 | 0 |
| `COMSIG_CLICK` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_CLICK_ALT` | `code/__DEFINES/components.dm` | 1 | 3 |
| `COMSIG_CLICK_CTRL` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_CLICK_CTRL_SHIFT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_CLICK_RIGHT_SHIFT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_CLICK_SHIFT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_CLIENT_MOUSEDOWN` | `code/__DEFINES/dcs/signals/signals_mob/signals_client.dm` | 1 | 1 |
| `COMSIG_CLIENT_MOUSEDRAG` | `code/__DEFINES/dcs/signals/signals_mob/signals_client.dm` | 1 | 0 |
| `COMSIG_CLIENT_MOUSEUP` | `code/__DEFINES/dcs/signals/signals_mob/signals_client.dm` | 1 | 1 |
| `COMSIG_CLOTHING_STEP_ACTION` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_COMBAT_TARGET_SET` | `code/__DEFINES/components.dm` | 2 | 0 |
| `COMSIG_COMPONENT_ADDED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_COMPONENT_CLEAN_ACT` | `code/__DEFINES/components.dm` | 9 | 7 |
| `COMSIG_COMPONENT_CLEAN_FACE_ACT` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_COMPONENT_NTNET_RECEIVE` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_COMPONENT_REMOVING` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_CONTAINS_STORAGE` | `code/__DEFINES/components.dm` | 5 | 1 |
| `COMSIG_DISGUISE_STATUS` | `code/__DEFINES/components.dm` | 7 | 1 |
| `COMSIG_DISPATCH_CARGO` | `code/__DEFINES/dcs/signals/signals_tram.dm` | 0 | 1 |
| `COMSIG_DIVINE_REBIRTH_CAST` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_DO_AFTER_BEGAN` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 1 | 1 |
| `COMSIG_DO_AFTER_ENDED` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 1 | 1 |
| `COMSIG_DRUG_SNIFFED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 2 |
| `COMSIG_ELEMENT_ATTACH` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ELEMENT_DETACH` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ENTER_AREA` | `code/__DEFINES/components.dm` | 1 | 3 |
| `COMSIG_EXIT_AREA` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_FOG_END` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_FOOD_EATEN` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_FORCE_UNDISGUISE` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_GIBS_STREAK` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_GLOBAL_FISH_RELEASED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 0 | 1 |
| `COMSIG_GLOB_EXPANDED_WORLD_BOUNDS` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_GLOB_JOB_AFTER_LATEJOIN_SPAWN` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_GLOB_JOB_AFTER_SPAWN` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_GLOB_LIVING_SAY_SPECIAL` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_GLOB_MOB_CREATED` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_GLOB_MOB_DEATH` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_GLOB_NEW_Z` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_GLOB_ROLE_CONVERTED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 1 |
| `COMSIG_GLOB_VAR_EDIT` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_GRAVE_CONSECRATED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 1 |
| `COMSIG_HAS_NANITES` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_HEAD_PUNCHED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 1 |
| `COMSIG_HEART_BEAST_HEAR` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_HOSTILE_ATTACKINGTARGET` | `code/__DEFINES/components.dm` | 4 | 4 |
| `COMSIG_HOSTILE_FOUND_TARGET` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 0 | 0 |
| `COMSIG_HOSTILE_POST_ATTACKINGTARGET` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 0 | 0 |
| `COMSIG_HOSTILE_PRE_ATTACKINGTARGET` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 5 | 0 |
| `COMSIG_HUMAN_DISARM_HIT` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_HUMAN_EARLY_UNARMED_ATTACK` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_HUMAN_LIFE` | `code/__DEFINES/components.dm` | 1 | 5 |
| `COMSIG_HUMAN_MELEE_UNARMED_ATTACK` | `code/__DEFINES/components.dm` | 1 | 4 |
| `COMSIG_HUMAN_MELEE_UNARMED_ATTACKBY` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_IMPLANT_ACTIVATED` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_IMPLANT_EXISTING_UPLINK` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_IMPLANT_IMPLANTING` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_IMPLANT_OTHER` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_INFESTATION_CHARGE_ADD` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_INFESTATION_CHARGE_REMOVE` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_IS_STORAGE_LOCKED` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_ITEM_AFTERATTACK` | `code/__DEFINES/components.dm` | 1 | 9 |
| `COMSIG_ITEM_ATTACK` | `code/__DEFINES/components.dm` | 1 | 5 |
| `COMSIG_ITEM_ATTACKED_SUCCESS` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ITEM_ATTACK_EFFECT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ITEM_ATTACK_EFFECT_SELF` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ITEM_ATTACK_OBJ` | `code/__DEFINES/components.dm` | 1 | 4 |
| `COMSIG_ITEM_ATTACK_QDELETED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ITEM_ATTACK_SELF` | `code/__DEFINES/components.dm` | 1 | 6 |
| `COMSIG_ITEM_ATTACK_SUCCESS` | `code/__DEFINES/components.dm` | 1 | 3 |
| `COMSIG_ITEM_ATTACK_TURF` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_ITEM_ATTACK_ZONE` | `code/__DEFINES/components.dm` | 2 | 0 |
| `COMSIG_ITEM_BROKEN` | `code/__DEFINES/components.dm` | 1 | 3 |
| `COMSIG_ITEM_CRAFTED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 2 | 2 |
| `COMSIG_ITEM_DROPPED` | `code/__DEFINES/components.dm` | 0 | 23 |
| `COMSIG_ITEM_EQUIPPED` | `code/__DEFINES/components.dm` | 1 | 23 |
| `COMSIG_ITEM_GUN_PROCESS_FIRE` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ITEM_HIT_REACT` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_ITEM_HIT_RESPONSE` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_ITEM_IMBUE_SOUL` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_ITEM_MARK_RETRIEVAL` | `code/__DEFINES/components.dm` | 2 | 0 |
| `COMSIG_ITEM_OBJFIX` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_ITEM_PICKUP` | `code/__DEFINES/components.dm` | 0 | 6 |
| `COMSIG_ITEM_POST_UNEQUIP` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_ITEM_PRE_ATTACK` | `code/__DEFINES/components.dm` | 1 | 3 |
| `COMSIG_ITEM_STOLEN` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 1 |
| `COMSIG_ITEM_WEARERCROSSED` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_JOB_RECEIVED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_LIFT_SET_DIRECTION` | `code/__DEFINES/dcs/signals/signals_tram.dm` | 1 | 0 |
| `COMSIG_LIVING_CAN_TRACK` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_LIVING_DEATH` | `code/__DEFINES/components.dm` | 1 | 11 |
| `COMSIG_LIVING_DRINKED_LIMB_BLOOD` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 1 | 1 |
| `COMSIG_LIVING_ELECTROCUTE_ACT` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_LIVING_EXTINGUISHED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_LIVING_GRAB_SELF_ATTEMPT` | `code/__DEFINES/components.dm` | 2 | 1 |
| `COMSIG_LIVING_HEALTH_UPDATE` | `code/__DEFINES/components.dm` | 2 | 1 |
| `COMSIG_LIVING_IGNITED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_LIVING_IMPACT_ZONE` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_LIVING_LIFE` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 1 | 2 |
| `COMSIG_LIVING_MINOR_SHOCK` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_LIVING_MIRACLE_HEAL_APPLY` | `code/__DEFINES/components.dm` | 2 | 2 |
| `COMSIG_LIVING_ONJUMP` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_LIVING_RESIST` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_LIVING_REVIVE` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_LIVING_SET_RESTING` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_LIVING_STATUS_IMMOBILIZE` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_LIVING_STATUS_KNOCKDOWN` | `code/__DEFINES/components.dm` | 1 | 3 |
| `COMSIG_LIVING_STATUS_OFFBALANCED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_LIVING_STATUS_PARALYZE` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_LIVING_STATUS_SLEEP` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_LIVING_STATUS_STUN` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_LIVING_STATUS_UNCONSCIOUS` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_LIVING_STOPPED_OFFERING_ITEM` | `code/__DEFINES/offer.dm` | 1 | 1 |
| `COMSIG_LIVING_SWINGDELAY_MOD` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_LUX_EXTRACTED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 1 |
| `COMSIG_LUX_TASTED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 1 |
| `COMSIG_MACHINERY_BROKEN` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MACHINERY_POWER_LOST` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_MACHINERY_POWER_RESTORED` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_MECHA_ACTION_ACTIVATE` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_MIND_TRANSFER` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_MIND_TRANSFERRED` | `code/__DEFINES/dcs/signals/signals_mob/signals_mind.dm` | 1 | 1 |
| `COMSIG_MOB_ABILITY_FINISHED` | `code/__DEFINES/dcs/signals/signals_action.dm` | 1 | 0 |
| `COMSIG_MOB_ABILITY_STARTED` | `code/__DEFINES/dcs/signals/signals_action.dm` | 1 | 0 |
| `COMSIG_MOB_AFTERATTACK_SUCCESS` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOB_AFTER_SPELL_CAST` | `code/__DEFINES/dcs/signals/signals_spell.dm` | 1 | 0 |
| `COMSIG_MOB_ALLOWED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOB_ALTCLICKON` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOB_APPLY_DAMGE` | `code/__DEFINES/components.dm` | 3 | 6 |
| `COMSIG_MOB_ATTACKED_BY_HAND` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOB_ATTACK_HAND` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOB_ATTACK_RANGED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOB_BEFORE_SPELL_CAST` | `code/__DEFINES/dcs/signals/signals_spell.dm` | 1 | 0 |
| `COMSIG_MOB_BREAK_SNEAK` | `code/__DEFINES/components.dm` | 2 | 0 |
| `COMSIG_MOB_CANCEL_CLICKON` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOB_CAST_SPELL` | `code/__DEFINES/dcs/signals/signals_spell.dm` | 1 | 0 |
| `COMSIG_MOB_CLICKON` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_MOB_CLIENT_LOGIN` | `code/__DEFINES/dcs/signals/signals_mob/signals_client.dm` | 1 | 1 |
| `COMSIG_MOB_DEADSAY` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_MOB_DEATH` | `code/__DEFINES/components.dm` | 1 | 10 |
| `COMSIG_MOB_DISMEMBER` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 1 | 0 |
| `COMSIG_MOB_DROPITEM` | `code/__DEFINES/components.dm` | 0 | 2 |
| `COMSIG_MOB_EQUIPPED_ITEM` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_MOB_EXAMINATE` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOB_HUD_CREATED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOB_HUGGED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 1 |
| `COMSIG_MOB_ITEM_AFTERATTACK` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOB_ITEM_ATTACK` | `code/__DEFINES/components.dm` | 1 | 6 |
| `COMSIG_MOB_ITEM_ATTACK_POST_SWINGDELAY` | `code/__DEFINES/components.dm` | 1 | 4 |
| `COMSIG_MOB_ITEM_ATTACK_QDELETED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOB_ITEM_BEING_ATTACKED` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOB_ITEM_POST_SWINGDELAY_ATTACKED` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOB_KICKED` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOB_KICKED_SUCCESSFUL` | `code/__DEFINES/spell_defines.dm` | 1 | 1 |
| `COMSIG_MOB_LOGIN` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 1 | 1 |
| `COMSIG_MOB_LOGOUT` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 1 | 4 |
| `COMSIG_MOB_MIDDLECLICKON` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOB_MIND_TRANSFERRED_INTO` | `code/__DEFINES/dcs/signals/signals_mob/signals_mind.dm` | 1 | 0 |
| `COMSIG_MOB_MIND_TRANSFERRED_OUT_OF` | `code/__DEFINES/dcs/signals/signals_mob/signals_mind.dm` | 1 | 0 |
| `COMSIG_MOB_MODIFY_AGGRO_LINES` | `code/__DEFINES/components.dm` | 16 | 1 |
| `COMSIG_MOB_MODIFY_DEATH_LINES` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_MOB_MOVESPEED_UPDATED` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 1 | 1 |
| `COMSIG_MOB_ON_KICK` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOB_ORGAN_REMOVED` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 1 | 1 |
| `COMSIG_MOB_OVERLAY_FORCE_REMOVE` | `code/__DEFINES/dcs/signals/signals_movable.dm` | 0 | 1 |
| `COMSIG_MOB_OVERLAY_FORCE_UPDATE` | `code/__DEFINES/dcs/signals/signals_movable.dm` | 0 | 1 |
| `COMSIG_MOB_POINTED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOB_PRE_INVOCATION` | `code/__DEFINES/dcs/signals/signals_spell.dm` | 1 | 0 |
| `COMSIG_MOB_RECEIVE_MAGIC` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOB_REMOVED_ACTION` | `code/__DEFINES/dcs/signals/signals_action.dm` | 0 | 0 |
| `COMSIG_MOB_SAY` | `code/__DEFINES/components.dm` | 1 | 40 |
| `COMSIG_MOB_SAY_POSTPROCESS` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOB_SPELL_ACTIVATED` | `code/__DEFINES/dcs/signals/signals_spell.dm` | 1 | 1 |
| `COMSIG_MOB_STATCHANGE` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 2 | 2 |
| `COMSIG_MOB_THROW` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOB_TRY_BARK` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOB_TRY_EMOTE` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_MOB_UNEQUIPPED_ITEM` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOB_UPDATE_SIGHT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOUSEDROPPED_ONTO` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOUSEDROP_ONTO` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOVABLE_BUCKLE` | `code/__DEFINES/dcs/signals/signals_movable.dm` | 1 | 1 |
| `COMSIG_MOVABLE_BUMP` | `code/__DEFINES/components.dm` | 1 | 3 |
| `COMSIG_MOVABLE_BUMP_PUSHED` | `code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm` | 0 | 1 |
| `COMSIG_MOVABLE_CROSS` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOVABLE_CROSSED` | `code/__DEFINES/components.dm` | 1 | 6 |
| `COMSIG_MOVABLE_DISPOSING` | `code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm` | 0 | 0 |
| `COMSIG_MOVABLE_HEAR` | `code/__DEFINES/components.dm` | 1 | 3 |
| `COMSIG_MOVABLE_IMPACT` | `code/__DEFINES/components.dm` | 2 | 3 |
| `COMSIG_MOVABLE_IMPACT_ZONE` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOVABLE_LIGHT_OVERLAY_SET_COLOR` | `code/__DEFINES/dcs/signals_atoms/movable_lighting.dm` | 0 | 0 |
| `COMSIG_MOVABLE_LIGHT_OVERLAY_SET_POWER` | `code/__DEFINES/dcs/signals_atoms/movable_lighting.dm` | 0 | 0 |
| `COMSIG_MOVABLE_LIGHT_OVERLAY_SET_RANGE` | `code/__DEFINES/dcs/signals_atoms/movable_lighting.dm` | 0 | 0 |
| `COMSIG_MOVABLE_LIGHT_OVERLAY_TOGGLE_ON` | `code/__DEFINES/dcs/signals_atoms/movable_lighting.dm` | 0 | 0 |
| `COMSIG_MOVABLE_MOVED` | `code/__DEFINES/components.dm` | 1 | 43 |
| `COMSIG_MOVABLE_POST_THROW` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_MOVABLE_PREBUCKLE` | `code/__DEFINES/dcs/signals/signals_movable.dm` | 1 | 1 |
| `COMSIG_MOVABLE_PRE_MOVE` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOVABLE_PRE_THROW` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_MOVABLE_SECLUDED_LOCATION` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_MOVABLE_SET_GRAB_STATE` | `code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm` | 0 | 0 |
| `COMSIG_MOVABLE_THROW_LANDED` | `code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm` | 0 | 1 |
| `COMSIG_MOVABLE_TURF_ENTERED` | `code/__DEFINES/dcs/signals/signals_turf.dm` | 1 | 1 |
| `COMSIG_MOVABLE_TURF_EXITED` | `code/__DEFINES/dcs/signals/signals_turf.dm` | 1 | 0 |
| `COMSIG_MOVABLE_UNBUCKLE` | `code/__DEFINES/dcs/signals/signals_movable.dm` | 1 | 1 |
| `COMSIG_MOVABLE_UNCROSSED` | `code/__DEFINES/components.dm` | 0 | 2 |
| `COMSIG_MOVABLE_UPDATE_GLIDE_SIZE` | `code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm` | 1 | 2 |
| `COMSIG_MOVABLE_Z_CHANGED` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_MOVELOOP_JPS_REPATH` | `code/__DEFINES/dcs/signals/signals_moveloop.dm` | 0 | 0 |
| `COMSIG_MOVELOOP_POSTPROCESS` | `code/__DEFINES/dcs/signals/signals_moveloop.dm` | 1 | 1 |
| `COMSIG_MOVELOOP_PREPROCESS_CHECK` | `code/__DEFINES/dcs/signals/signals_moveloop.dm` | 1 | 2 |
| `COMSIG_MOVELOOP_START` | `code/__DEFINES/dcs/signals/signals_moveloop.dm` | 1 | 0 |
| `COMSIG_MOVELOOP_STOP` | `code/__DEFINES/dcs/signals/signals_moveloop.dm` | 1 | 0 |
| `COMSIG_MULTITOOL_REMOVE_BUFFER` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_NANITE_ADD_PROGRAM` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_ADJUST_VOLUME` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_COMM_SIGNAL` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_DELETE` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_GET_PROGRAMS` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_GET_VOLUME` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_IS_STEALTHY` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_SCAN` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_SET_CLOUD` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_SET_CLOUD_SYNC` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_SET_MAX_VOLUME` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_SET_REGEN` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_SET_SAFETY` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_SET_VOLUME` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_SIGNAL` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_SYNC` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NANITE_UI_DATA` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_NEW_ICHOR_FANG_SPAWNED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 0 | 1 |
| `COMSIG_OBJ_DECONSTRUCT` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_OBJ_DEFAULT_UNFASTEN_WRENCH` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_OBJ_HANDED_OVER` | `code/__DEFINES/offer.dm` | 1 | 3 |
| `COMSIG_OBJ_SETANCHORED` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_OBJ_TAKE_DAMAGE` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_ORGAN_CONSUMED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 1 |
| `COMSIG_PARENT_ATTACKBY` | `code/__DEFINES/components.dm` | 1 | 9 |
| `COMSIG_PARENT_EXAMINE` | `code/__DEFINES/components.dm` | 3 | 21 |
| `COMSIG_PARENT_PREQDELETED` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_PARENT_QDELETING` | `code/__DEFINES/components.dm` | 1 | 44 |
| `COMSIG_PDA_CHANGE_RINGTONE` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_PDA_CHECK_DETONATE` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_PEN_ROTATED` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_POWER_ACTIVATE` | `code/__DEFINES/dcs/signals/signals_coven_powers.dm` | 1 | 1 |
| `COMSIG_POWER_ACTIVATE_ON` | `code/__DEFINES/dcs/signals/signals_coven_powers.dm` | 1 | 0 |
| `COMSIG_POWER_DEACTIVATE` | `code/__DEFINES/dcs/signals/signals_coven_powers.dm` | 1 | 0 |
| `COMSIG_POWER_DEACTIVATE_ON` | `code/__DEFINES/dcs/signals/signals_coven_powers.dm` | 1 | 0 |
| `COMSIG_POWER_PRE_ACTIVATION` | `code/__DEFINES/dcs/signals/signals_coven_powers.dm` | 1 | 0 |
| `COMSIG_POWER_PRE_ACTIVATION_ON` | `code/__DEFINES/dcs/signals/signals_coven_powers.dm` | 1 | 0 |
| `COMSIG_POWER_TRY_ACTIVATE` | `code/__DEFINES/dcs/signals/signals_coven_powers.dm` | 1 | 0 |
| `COMSIG_POWER_TRY_ACTIVATE_ON` | `code/__DEFINES/dcs/signals/signals_coven_powers.dm` | 1 | 0 |
| `COMSIG_POWER_TRY_DEACTIVATE` | `code/__DEFINES/dcs/signals/signals_coven_powers.dm` | 1 | 0 |
| `COMSIG_POWER_TRY_DEACTIVATE_ON` | `code/__DEFINES/dcs/signals/signals_coven_powers.dm` | 1 | 0 |
| `COMSIG_PREQDELETED` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_PROCESS_BORGCHARGER_OCCUPANT` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_PROJECTILE_BEFORE_FIRE` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_PROJECTILE_ON_HIT` | `code/__DEFINES/components.dm` | 1 | 6 |
| `COMSIG_PROJECTILE_PREHIT` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_PROJECTILE_SELF_ON_HIT` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_QDELETING` | `code/__DEFINES/components.dm` | 0 | 10 |
| `COMSIG_RADIO_NEW_FREQUENCY` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_RIDDEN_DRIVER_MOVE` | `code/__DEFINES/dcs/signals/signals_movable.dm` | 0 | 1 |
| `COMSIG_ROTTEN_FOOD_EATEN` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 1 |
| `COMSIG_SACRED_TREE_DAMAGED` | `code/__DEFINES/dcs/signals/signals_global.dm` | 0 | 1 |
| `COMSIG_SEX_ADJUST_AROUSAL` | `code/__DEFINES/sex.dm` | 1 | 1 |
| `COMSIG_SEX_AROUSAL_CHANGED` | `code/__DEFINES/sex.dm` | 1 | 2 |
| `COMSIG_SEX_CAN_USE_PENIS` | `code/__DEFINES/sex.dm` | 0 | 0 |
| `COMSIG_SEX_CLIMAX` | `code/__DEFINES/sex.dm` | 1 | 1 |
| `COMSIG_SEX_CONSIDERED_LIMP` | `code/__DEFINES/sex.dm` | 0 | 0 |
| `COMSIG_SEX_FREEZE_AROUSAL` | `code/__DEFINES/sex.dm` | 1 | 1 |
| `COMSIG_SEX_GET_AROUSAL` | `code/__DEFINES/sex.dm` | 5 | 1 |
| `COMSIG_SEX_JOSTLE` | `code/__DEFINES/sex.dm` | 1 | 1 |
| `COMSIG_SEX_RECEIVE_ACTION` | `code/__DEFINES/sex.dm` | 1 | 1 |
| `COMSIG_SEX_REMOVE_KNOT` | `code/__DEFINES/sex.dm` | 1 | 1 |
| `COMSIG_SEX_SET_AROUSAL` | `code/__DEFINES/sex.dm` | 2 | 1 |
| `COMSIG_SEX_TRY_KNOT` | `code/__DEFINES/sex.dm` | 2 | 1 |
| `COMSIG_SIMPLEMOB_POST_ATTACK_RANGED` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 0 | 0 |
| `COMSIG_SIMPLEMOB_PRE_ATTACK_RANGED` | `code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm` | 0 | 0 |
| `COMSIG_SKILL_RANK_INCREASED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 3 |
| `COMSIG_SLEEPY_TIME` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_SPECIES_GAIN` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_SPECIES_LOSS` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_SPELL_AFTER_CAST` | `code/__DEFINES/dcs/signals/signals_spell.dm` | 1 | 0 |
| `COMSIG_SPELL_BEFORE_CAST` | `code/__DEFINES/dcs/signals/signals_spell.dm` | 1 | 0 |
| `COMSIG_SPELL_CAST` | `code/__DEFINES/dcs/signals/signals_spell.dm` | 1 | 0 |
| `COMSIG_SPELL_CAST_RESET` | `code/__DEFINES/dcs/signals/signals_spell.dm` | 1 | 0 |
| `COMSIG_SPELL_PROJECTILE_HIT` | `code/__DEFINES/dcs/signals/signals_spell.dm` | 1 | 0 |
| `COMSIG_SPELL_TOUCH_HAND_HIT` | `code/__DEFINES/dcs/signals/signals_spell.dm` | 1 | 0 |
| `COMSIG_STATUS_EFFECT_HAG_CURSE_CLEARED` | `code/__DEFINES/components.dm` | 2 | 1 |
| `COMSIG_STORAGE_ADDED` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_STORAGE_BLOCK_USER_TAKE` | `code/game/objects/items/storage/new_storage/tetris.dm` | 0 | 1 |
| `COMSIG_STRUCTURE_ATTACKBY` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_TGUI_WINDOW_VISIBLE` | `code/__DEFINES/dcs/signals/signals_tgui.dm` | 1 | 0 |
| `COMSIG_TICKER_RULERMOB_SET` | `code/__DEFINES/dcs/signals/signals_global.dm` | 0 | 1 |
| `COMSIG_TOPIC` | `code/__DEFINES/components.dm` | 1 | 2 |
| `COMSIG_TORTURE_PERFORMED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 0 | 1 |
| `COMSIG_TRAIT_GAIN` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_TRAIT_LOSS` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_TRAM_COLLISION` | `code/__DEFINES/dcs/signals/signals_tram.dm` | 0 | 0 |
| `COMSIG_TRAM_EMPTY` | `code/__DEFINES/dcs/signals/signals_tram.dm` | 1 | 1 |
| `COMSIG_TRAM_REACHED_PLATFORM` | `code/__DEFINES/dcs/signals/signals_tram.dm` | 1 | 1 |
| `COMSIG_TRAM_SET_TRAVELLING` | `code/__DEFINES/dcs/signals/signals_tram.dm` | 2 | 0 |
| `COMSIG_TRAM_TRAVEL` | `code/__DEFINES/dcs/signals/signals_tram.dm` | 1 | 0 |
| `COMSIG_TREE_TRANSFORMED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 1 | 1 |
| `COMSIG_TRY_STORAGE_CAN_INSERT` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_TRY_STORAGE_FILL_TYPE` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_TRY_STORAGE_HIDE_ALL` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_TRY_STORAGE_HIDE_FROM` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_TRY_STORAGE_INSERT` | `code/__DEFINES/components.dm` | 10 | 2 |
| `COMSIG_TRY_STORAGE_QUICK_EMPTY` | `code/__DEFINES/components.dm` | 3 | 1 |
| `COMSIG_TRY_STORAGE_RETURN_INVENTORY` | `code/__DEFINES/components.dm` | 3 | 1 |
| `COMSIG_TRY_STORAGE_SET_LOCKSTATE` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_TRY_STORAGE_SHOW` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_TRY_STORAGE_TAKE` | `code/__DEFINES/components.dm` | 4 | 1 |
| `COMSIG_TRY_STORAGE_TAKE_TYPE` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_TURF_CHANGE` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_TURF_ENTER` | `code/__DEFINES/dcs/signals/signals_turf.dm` | 0 | 0 |
| `COMSIG_TURF_ENTERED` | `code/__DEFINES/dcs/signals/signals_turf.dm` | 1 | 1 |
| `COMSIG_TURF_EXITED` | `code/__DEFINES/dcs/signals/signals_turf.dm` | 1 | 1 |
| `COMSIG_TURF_INDUSTRIAL_LIFT_ENTER` | `code/__DEFINES/dcs/signals/signals_tram.dm` | 1 | 0 |
| `COMSIG_TURF_IS_WET` | `code/__DEFINES/components.dm` | 0 | 1 |
| `COMSIG_TURF_MAKE_DRY` | `code/__DEFINES/components.dm` | 1 | 1 |
| `COMSIG_TURF_MULTIZ_NEW` | `code/__DEFINES/components.dm` | 1 | 0 |
| `COMSIG_UI_ACT` | `code/__DEFINES/dcs/signals/signals_datum.dm` | 1 | 0 |
| `COMSIG_VICIOUSLY_MOCKED` | `code/__DEFINES/dcs/signals/signals_objectives.dm` | 2 | 1 |
| `COMSIG_WARDED_TRAIT_CHANGE` | `code/__DEFINES/components.dm` | 2 | 1 |
| `COMSIG_XENO_MONKEY_CLICK_CTRL` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_XENO_SLIME_CLICK_ALT` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_XENO_SLIME_CLICK_CTRL` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_XENO_SLIME_CLICK_SHIFT` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_XENO_TURF_CLICK_CTRL` | `code/__DEFINES/components.dm` | 0 | 0 |
| `COMSIG_XENO_TURF_CLICK_SHIFT` | `code/__DEFINES/components.dm` | 0 | 0 |

## Fast Search Patterns

```sh
rg -n "COMSIG_SPELL_|COMSIG_MOB_.*SPELL" code modular -g "*.dm"
rg -n "COMSIG_.*(ATTACK|COMBAT|MELEE|PROJECTILE|HIT|DISARM)" code modular -g "*.dm"
rg -n "COMSIG_(MOVABLE|MOVELOOP|RIDDEN_DRIVER_MOVE)" code modular -g "*.dm"
rg -n "RegisterSignal\(|SEND_SIGNAL\(" code modular -g "*.dm"
```
