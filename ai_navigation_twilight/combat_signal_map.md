# Combat Signal Map

Generated on 2026-07-09.

| Signal | Defined in | Send file count | Register file count | Sample usage files |
|---|---|---|---|---|
| COMSIG_ATOM_ATTACKBY | code/__DEFINES/dcs/signals_atoms/signals_atom.dm | 0 | 4 | code/datums/elements/relay_attackers.dm, code/datums/slapcrafting.dm, code/modules/vampire_neu/covens/coven_powers/_base_power.dm |
| COMSIG_ATOM_ATTACK_ANIMAL | code/__DEFINES/components.dm | 1 | 2 | code/_onclick/other_mobs.dm, code/datums/elements/relay_attackers.dm, modular_twilight_axis/code/modules/spells/pantheon/divine/necra/shroud.dm |
| COMSIG_ATOM_ATTACK_GHOST | code/__DEFINES/components.dm | 1 | 1 | code/_onclick/observer.dm, code/datums/components/storage/storage.dm |
| COMSIG_ATOM_ATTACK_HAND | code/__DEFINES/components.dm | 3 | 5 | code/_onclick/other_mobs.dm, code/modules/mob/living/carbon/human/species.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/melee/soundbreaker_proxy.dm |
| COMSIG_ATOM_ATTACK_RIGHT | code/__DEFINES/components.dm | 1 | 3 | code/_onclick/other_mobs.dm, code/game/objects/items/holster_component.dm, code/game/objects/items/rogueweapons/melee/special.dm |
| COMSIG_ATOM_WAS_ATTACKED | code/__DEFINES/components.dm | 2 | 5 | code/datums/elements/relay_attackers.dm, code/modules/spells/spell_types/classunique/spellblade/anime_spells_helper.dm, code/datums/ai/_ai_controller.dm |
| COMSIG_ATTACK_TRY_CONSUME | modular_twilight_axis/code/_signals.dm | 2 | 3 | modular_twilight_axis/code/datums/combo/combo_core.dm, modular_twilight_axis/code/game/objects/items/rogueweapons/intents.dm, modular_twilight_axis/code/datums/combo/combo_ronin.dm |
| COMSIG_COMBAT_TARGET_SET | code/__DEFINES/components.dm | 2 | 0 | code/datums/ai/subtrees/bow_usage.dm, code/datums/ai/subtrees/human_basic_attack.dm |
| COMSIG_GLOB_MOB_CREATED | code/__DEFINES/components.dm | 0 | 1 | modular_twilight_axis/familytree_module/familytree_subsystem_core.dm |
| COMSIG_GLOB_MOB_DEATH | code/__DEFINES/components.dm | 0 | 1 | modular_twilight_axis/code/modules/vampire_neu/ascended_covens.dm |
| COMSIG_HOSTILE_ATTACKINGTARGET | code/__DEFINES/components.dm | 5 | 4 | code/modules/mob/living/simple_animal/hostile/hostile.dm, code/modules/mob/living/simple_animal/hostile/retaliate/summons/elemental/behemoth.dm, code/modules/mob/living/simple_animal/hostile/retaliate/summons/fae/glimmerwing.dm |
| COMSIG_HOSTILE_POST_ATTACKINGTARGET | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 0 | 0 | - |
| COMSIG_HOSTILE_PRE_ATTACKINGTARGET | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 6 | 0 | code/datums/ai/_ai_controller.dm, code/modules/mob/living/simple_animal/hostile/hostile.dm, code/modules/mob/living/simple_animal/hostile/retaliate/summons/elemental/behemoth.dm |
| COMSIG_HUMAN_EARLY_UNARMED_ATTACK | code/__DEFINES/components.dm | 1 | 1 | code/_onclick/other_mobs.dm, modular_twilight_axis/code/modules/mob/living/carbon/human/table_crawl.dm |
| COMSIG_HUMAN_MELEE_UNARMED_ATTACK | code/__DEFINES/components.dm | 1 | 5 | code/_onclick/other_mobs.dm, code/datums/components/riding.dm, code/datums/status_effects/rogue/roguebuff.dm |
| COMSIG_HUMAN_MELEE_UNARMED_ATTACKBY | code/__DEFINES/components.dm | 0 | 0 | - |
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
| COMSIG_LIVING_STOPPED_OFFERING_ITEM | code/__DEFINES/offer.dm | 1 | 1 | code/modules/mob/living/living.dm, code/game/objects/effects/temporary_visuals/offered_item_effect.dm |
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
| COMSIG_PARENT_ATTACKBY | code/__DEFINES/components.dm | 1 | 7 | code/_onclick/item_attack.dm, code/datums/components/construction.dm, code/datums/components/explodable.dm |
| COMSIG_PROJECTILE_ATTACK_EFFECT | code/__DEFINES/components.dm | 1 | 0 | code/game/objects/items/rogueweapons/ranged/_ammo.dm |
| COMSIG_PROJECTILE_ATTACK_EFFECT_SELF | code/__DEFINES/components.dm | 1 | 0 | code/game/objects/items/rogueweapons/ranged/_ammo.dm |
| COMSIG_SIMPLEMOB_POST_ATTACK_RANGED | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 0 | 0 | - |
| COMSIG_SIMPLEMOB_PRE_ATTACK_RANGED | code/__DEFINES/dcs/signals/signals_mob/signals_mob.dm | 0 | 0 | - |
| COMSIG_SOUNDBREAKER_KICK_SUCCESS | modular_twilight_axis/code/_signals.dm | 1 | 1 | modular_twilight_axis/code/game/objects/items/rogueweapons/intents.dm, modular_twilight_axis/code/datums/combo/soundbreaker/combo_soundbreaker.dm |
| COMSIG_STRUCTURE_ATTACKBY | code/__DEFINES/components.dm | 1 | 1 | code/game/objects/items/rogueweapons/integrity.dm, code/game/objects/items/rogueweapons/melee/special.dm |
| COMSIG_TICKER_RULERMOB_SET | code/__DEFINES/dcs/signals/signals_global.dm | 0 | 1 | code/game/objects/structures/crates_lockers/roguetown.dm |


Open `code/_onclick/**`, rogue weapon files, and overlay rogueweapon modules for combat routing.
