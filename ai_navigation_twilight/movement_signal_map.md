# Movement Signal Map

Generated on 2026-07-09.

| Signal | Defined in | Send file count | Register file count | Sample usage files |
|---|---|---|---|---|
| COMSIG_ACTION_REMOVED | code/__DEFINES/dcs/signals/signals_action.dm | 1 | 0 | code/datums/actions/action.dm |
| COMSIG_AFTER_STORAGE_REMOVE | code/__DEFINES/components.dm | 1 | 1 | code/game/objects/items/storage/new_storage/tetris.dm, code/datums/item_equipped_movement_rustle.dm |
| COMSIG_AI_MOVEMENT_SET | code/__DEFINES/dcs/signals/signals_ai.dm | 0 | 0 | - |
| COMSIG_ATOM_BUMPED | code/__DEFINES/components.dm | 1 | 1 | code/game/atoms.dm, code/game/objects/minecart_system/minecart.dm |
| COMSIG_ATOM_DIR_CHANGE | code/__DEFINES/components.dm | 1 | 5 | code/game/atoms.dm, code/datums/components/after_image.dm, code/datums/components/decal.dm |
| COMSIG_ATOM_REMOVE_TRAIT | code/__DEFINES/components.dm | 0 | 0 | - |
| COMSIG_CLIENT_VERB_REMOVED | code/__DEFINES/dcs/signals/signals_mob/signals_client.dm | 1 | 0 | code/__HELPERS/verbs.dm |
| COMSIG_INFESTATION_CHARGE_REMOVE | code/__DEFINES/components.dm | 1 | 1 | code/modules/spells/roguetown/acolyte/pestra/pestra_components.dm, code/modules/spells/roguetown/acolyte/pestra/pestra_components.dm |
| COMSIG_MOB_MOVESPEED_UPDATED | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 1 | 1 | code/modules/mob/mob_movespeed.dm, code/datums/ai/controllers/human_npc.dm |
| COMSIG_MOB_ORGAN_REMOVED | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 1 | 1 | code/modules/surgery/organs/organ_internal.dm, code/modules/vampire_neu/clan/_base_clan.dm |
| COMSIG_MOB_OVERLAY_FORCE_REMOVE | code/__DEFINES/dcs/signals/signals_movable.dm | 0 | 1 | code/datums/elements/mob_overlay_effect.dm |
| COMSIG_MOB_REMOVED_ACTION | code/__DEFINES/dcs/signals/signals_action.dm | 0 | 0 | - |
| COMSIG_MOB_THROW | code/__DEFINES/components.dm | 1 | 0 | code/modules/mob/living/carbon/carbon.dm |
| COMSIG_MOVABLE_BUCKLE | code/__DEFINES/dcs/signals/signals_movable.dm | 1 | 1 | code/game/objects/buckling.dm, code/datums/components/riding.dm |
| COMSIG_MOVABLE_BUMP | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 4 | code/game/atoms_movable.dm, code/datums/components/explodable.dm, code/datums/components/squeak.dm |
| COMSIG_MOVABLE_BUMP_PUSHED | code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 0 | 1 | code/game/objects/minecart_system/minecart.dm |
| COMSIG_MOVABLE_MOVED | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 56 | code/game/atoms_movable.dm, code/controllers/subsystem/movement/movement_types.dm, code/controllers/subsystem/rogue/fog_event/fog_component.dm |
| COMSIG_MOVABLE_POST_THROW | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 2 | code/game/atoms_movable.dm, code/datums/components/storage/storage.dm, code/modules/roguetown/roguemachine/heartbeast/heart_quirks/quirk_hoarder.dm |
| COMSIG_MOVABLE_PREBUCKLE | code/__DEFINES/dcs/signals/signals_movable.dm | 1 | 1 | code/game/objects/buckling.dm, code/datums/ai/hostile/_hostile_controller.dm |
| COMSIG_MOVABLE_PRE_MOVE | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 3 | code/game/atoms_movable.dm, code/datums/components/tether.dm, code/modules/mob/living/living.dm |
| COMSIG_MOVABLE_PRE_THROW | code/__DEFINES/components.dm, code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 1 | 1 | code/game/atoms_movable.dm, code/datums/components/magnetic_catch.dm |
| COMSIG_MOVABLE_THROW_LANDED | code/__DEFINES/dcs/signals_atoms/signals_atom_movable.dm | 0 | 1 | code/datums/components/after_image.dm |
| COMSIG_MOVABLE_UNBUCKLE | code/__DEFINES/dcs/signals/signals_movable.dm | 1 | 1 | code/game/objects/buckling.dm, code/datums/components/riding.dm |
| COMSIG_MOVELOOP_JPS_REPATH | code/__DEFINES/dcs/signals/signals_moveloop.dm | 0 | 0 | - |
| COMSIG_MOVELOOP_POSTPROCESS | code/__DEFINES/dcs/signals/signals_moveloop.dm | 1 | 1 | code/controllers/subsystem/movement/movement_types.dm, code/game/objects/minecart_system/minecart.dm |
| COMSIG_MOVELOOP_PREPROCESS_CHECK | code/__DEFINES/dcs/signals/signals_moveloop.dm | 1 | 2 | code/controllers/subsystem/movement/movement_types.dm, code/datums/components/conveyor_movement.dm, code/game/objects/minecart_system/minecart.dm |
| COMSIG_MOVELOOP_START | code/__DEFINES/dcs/signals/signals_moveloop.dm | 1 | 0 | code/controllers/subsystem/movement/movement_types.dm |
| COMSIG_MOVELOOP_STOP | code/__DEFINES/dcs/signals/signals_moveloop.dm | 1 | 0 | code/controllers/subsystem/movement/movement_types.dm |
| COMSIG_MULTITOOL_REMOVE_BUFFER | code/__DEFINES/components.dm | 1 | 0 | code/game/objects/items/contraption.dm |
| COMSIG_RIDDEN_DRIVER_MOVE | code/__DEFINES/dcs/signals/signals_movable.dm | 0 | 1 | code/datums/ai/hostile/_hostile_controller.dm |
| COMSIG_SEX_REMOVE_KNOT | code/__DEFINES/sex.dm | 1 | 1 | code/datums/sexcon2/sex_status.dm, code/modules/sexcon/components/knotting.dm |


Open `code/controllers/subsystem/movement/**` and movement-heavy overlay modules.
