# Type Tree

Generated for Azure-Peak on 2026-04-11 from strict type declarations in `code/**` and `modular/**`.

- Unique type branches detected: **19923**
- Only bare `/datum`, `/mob`, `/obj`, `/turf`, and `/area` type declaration paths are included.
- Proc/verb/var declarations and inline var assignments are intentionally omitted; use ripgrep for exact proc ownership.

```text
+- area
|  +- abductor_ship
|  +- ai_monitored
|  |  +- nuke_storage
|  |  +- security
|  |  |  `- armory
|  |  +- storage
|  |  |  +- eva
|  |  |  `- satellite
|  |  `- turret_protected
|  |     +- ai
|  |     +- ai_upload
|  |     +- ai_upload_foyer
|  |     +- aisat
|  |     |  +- atmos
|  |     |  +- foyer
|  |     |  +- hallway
|  |     |  `- service
|  |     +- aisat_interior
|  |     +- AIsatextAP
|  |     `- AIsatextAS
|  +- aisat
|  +- asteroid
|  |  `- nearstation
|  |     `- bomb_site
|  +- bridge
|  |  +- meeting_room
|  |  |  `- council
|  |  `- showroom
|  |     `- corporate
|  +- centcom
|  |  +- control
|  |  +- evac
|  |  +- ferry
|  |  +- holding
|  |  +- prison
|  |  +- supply
|  |  `- supplypod
|  |     +- flyMeToTheMoon
|  |     +- loading
|  |     |  +- ert
|  |     |  +- four
|  |     |  +- one
|  |     |  +- three
|  |     |  `- two
|  |     `- podStorage
|  +- chapel
|  |  +- asteroid
|  |  |  `- monastery
|  |  +- dock
|  |  +- main
|  |  |  `- monastery
|  |  `- office
|  +- comms
|  +- construction
|  |  +- mining
|  |  |  `- aux_base
|  |  `- storage_wing
|  +- crew_quarters
|  |  +- abandoned_gambling_den
|  |  |  `- secondary
|  |  +- bar
|  |  |  `- atrium
|  |  +- cafeteria
|  |  +- dorms
|  |  +- electronic_marketing_den
|  |  +- fitness
|  |  |  +- locker_room
|  |  |  `- recreation
|  |  +- heads
|  |  |  +- captain
|  |  |  |  `- private
|  |  |  +- chief
|  |  |  +- cmo
|  |  |  +- hop
|  |  |  +- hor
|  |  |  `- hos
|  |  +- kitchen
|  |  |  `- coldroom
|  |  +- locker
|  |  +- lounge
|  |  +- theatre
|  |  |  `- abandoned
|  |  `- toilet
|  |     +- auxiliary
|  |     +- locker
|  |     `- restrooms
|  +- ctf
|  |  +- central
|  |  +- control_room
|  |  +- control_room2
|  |  +- corridor
|  |  +- corridor2
|  |  +- flag_room
|  |  +- flag_room2
|  |  +- main_hall
|  |  `- main_hall2
|  +- engine
|  |  +- atmos
|  |  +- atmospherics_engine
|  |  +- break_room
|  |  +- engine_room
|  |  |  `- external
|  |  +- engine_smes
|  |  +- engineering
|  |  +- gravity_generator
|  |  +- storage
|  |  +- storage_shared
|  |  +- supermatter
|  |  `- transit_tube
|  +- gateway
|  +- hallway
|  |  +- primary
|  |  |  +- aft
|  |  |  +- central
|  |  |  +- fore
|  |  |  +- port
|  |  |  `- starboard
|  |  `- secondary
|  |     +- command
|  |     +- construction
|  |     +- entry
|  |     +- exit
|  |     |  `- departure_lounge
|  |     `- service
|  +- hydroponics
|  |  `- garden
|  |     +- abandoned
|  |     `- monastery
|  +- janitor
|  +- lawoffice
|  +- library
|  |  +- abandoned
|  |  `- lounge
|  +- maintenance
|  |  +- aft
|  |  |  `- secondary
|  |  +- central
|  |  |  `- secondary
|  |  +- department
|  |  |  +- bridge
|  |  |  +- cargo
|  |  |  +- chapel
|  |  |  |  `- monastery
|  |  |  +- crew_quarters
|  |  |  |  +- bar
|  |  |  |  `- dorms
|  |  |  +- electrical
|  |  |  +- engine
|  |  |  |  `- atmos
|  |  |  +- eva
|  |  |  +- medical
|  |  |  |  +- central
|  |  |  |  `- morgue
|  |  |  +- science
|  |  |  |  +- central
|  |  |  |  `- xenobiology
|  |  |  `- security
|  |  |     `- brig
|  |  +- disposal
|  |  |  `- incinerator
|  |  +- fore
|  |  |  `- secondary
|  |  +- port
|  |  |  +- aft
|  |  |  +- central
|  |  |  `- fore
|  |  +- solars
|  |  |  +- port
|  |  |  |  +- aft
|  |  |  |  `- fore
|  |  |  `- starboard
|  |  |     +- aft
|  |  |     `- fore
|  |  `- starboard
|  |     +- aft
|  |     |  `- secondary
|  |     +- central
|  |     +- fore
|  |     `- secondary
|  +- medical
|  |  +- abandoned
|  |  +- apothecary
|  |  +- chemistry
|  |  +- cryo
|  |  +- exam_room
|  |  +- genetics
|  |  |  `- cloning
|  |  +- medbay
|  |  |  +- aft
|  |  |  +- central
|  |  |  +- lobby
|  |  |  `- zone2
|  |  +- morgue
|  |  +- patients_rooms
|  |  |  +- room_a
|  |  |  `- room_b
|  |  +- sleeper
|  |  +- storage
|  |  +- surgery
|  |  |  `- room_b
|  |  `- virology
|  +- misc
|  |  `- testroom
|  +- quartermaster
|  |  +- miningdock
|  |  +- miningoffice
|  |  +- office
|  |  +- qm
|  |  +- sorting
|  |  +- storage
|  |  `- warehouse
|  +- rogue
|  |  +- druidsgrove
|  |  +- indoors
|  |  |  +- abandonedhotsprings
|  |  |  +- banditcamp
|  |  |  +- cave
|  |  |  |  +- central
|  |  |  |  +- east
|  |  |  |  +- northern
|  |  |  |  +- southern
|  |  |  |  +- underhamlet
|  |  |  |  `- west
|  |  |  +- deathsedge
|  |  |  +- eventarea
|  |  |  |  `- multiz
|  |  |  +- inq
|  |  |  |  +- basement
|  |  |  |  +- import
|  |  |  |  `- office
|  |  |  +- ravoxarena
|  |  |  +- sanctuary
|  |  |  +- shelter
|  |  |  |  +- bog
|  |  |  |  +- bog_hag
|  |  |  |  |  `- root_maze
|  |  |  |  +- mountains
|  |  |  |  |  `- decap
|  |  |  |  +- rtfield
|  |  |  |  +- town
|  |  |  |  |  +- dwarf
|  |  |  |  |  +- roofs
|  |  |  |  |  `- sargoth
|  |  |  |  `- woods
|  |  |  +- town
|  |  |  |  +- bath
|  |  |  |  +- cell
|  |  |  |  +- church
|  |  |  |  |  +- basement
|  |  |  |  |  `- chapel
|  |  |  |  +- dwarfin
|  |  |  |  +- entrance
|  |  |  |  +- fire_chamber
|  |  |  |  +- garrison
|  |  |  |  +- magician
|  |  |  |  +- manor
|  |  |  |  +- pestra_sanctum
|  |  |  |  +- physician
|  |  |  |  +- shop
|  |  |  |  +- steward
|  |  |  |  +- tavern
|  |  |  |  +- vault
|  |  |  |  `- warehouse
|  |  |  `- vampire_manor
|  |  +- outdoors
|  |  |  +- abisland
|  |  |  +- banditcamp
|  |  |  +- beach
|  |  |  |  +- central
|  |  |  |  +- forest
|  |  |  |  |  +- hamlet
|  |  |  |  |  +- north
|  |  |  |  |  `- south
|  |  |  |  +- north
|  |  |  |  `- south
|  |  |  +- bog
|  |  |  |  +- north
|  |  |  |  `- south
|  |  |  +- caves
|  |  |  +- exposed
|  |  |  |  +- bath
|  |  |  |  |  `- vault
|  |  |  |  +- church
|  |  |  |  +- decap
|  |  |  |  +- dwarf
|  |  |  |  +- magiciantower
|  |  |  |  +- manorgarri
|  |  |  |  +- shop
|  |  |  |  +- tavern
|  |  |  |  +- town
|  |  |  |  |  `- keep
|  |  |  |  |     `- unbuildable
|  |  |  |  `- under
|  |  |  |     +- basement
|  |  |  |     +- caves
|  |  |  |     +- sewer
|  |  |  |     `- town
|  |  |  +- mountains
|  |  |  |  `- decap
|  |  |  |     +- gunduzirak
|  |  |  |     |  `- bossarena
|  |  |  |     +- minotaurfort
|  |  |  |     `- stepbelow
|  |  |  +- rtfield
|  |  |  |  +- abandonedhotsprings
|  |  |  |  `- eora
|  |  |  +- spidercave
|  |  |  +- town
|  |  |  |  +- dwarf
|  |  |  |  +- roofs
|  |  |  |  |  `- keep
|  |  |  |  `- sargoth
|  |  |  `- woods
|  |  |     +- north
|  |  |     +- northeast
|  |  |     +- northwest
|  |  |     +- south
|  |  |     +- southeast
|  |  |     +- southwest
|  |  |     +- vampire_lair
|  |  |     `- wretch_lair
|  |  +- under
|  |  |  +- cave
|  |  |  |  +- dragonden
|  |  |  |  +- dukecourt
|  |  |  |  +- dungeon1
|  |  |  |  |  `- gethsmane
|  |  |  |  |     `- inner
|  |  |  |  +- fishmandungeon
|  |  |  |  +- goblindungeon
|  |  |  |  +- goblinfort
|  |  |  |  +- his_vault
|  |  |  |  |  +- four
|  |  |  |  |  +- one
|  |  |  |  |  +- puzzle
|  |  |  |  |  +- three
|  |  |  |  |  `- two
|  |  |  |  +- inhumen
|  |  |  |  +- licharena
|  |  |  |  |  `- bossroom
|  |  |  |  +- mazedungeon
|  |  |  |  +- orcdungeon
|  |  |  |  +- peace
|  |  |  |  +- scarymaze
|  |  |  |  +- skeletoncrypt
|  |  |  |  +- spider
|  |  |  |  `- undeadmanor
|  |  |  +- cavelava
|  |  |  +- cavewet
|  |  |  |  `- bogcaves
|  |  |  |     +- camp
|  |  |  |     +- central
|  |  |  |     +- coastcaves
|  |  |  |     +- north
|  |  |  |     +- south
|  |  |  |     `- west
|  |  |  +- lake
|  |  |  +- spiderbase
|  |  |  +- tomb
|  |  |  |  +- cave
|  |  |  |  |  +- lava
|  |  |  |  |  +- spider
|  |  |  |  |  `- wet
|  |  |  |  +- indoors
|  |  |  |  |  +- church
|  |  |  |  |  +- magic
|  |  |  |  |  +- rest
|  |  |  |  |  `- royal
|  |  |  |  +- lake
|  |  |  |  +- sewer
|  |  |  |  `- wilds
|  |  |  |     +- ambush
|  |  |  |     `- bog
|  |  |  +- town
|  |  |  |  +- basement
|  |  |  |  |  `- keep
|  |  |  |  +- caverogue
|  |  |  |  `- sewer
|  |  |  `- underdark
|  |  |     +- north
|  |  |     `- south
|  |  `- underworld
|  |     `- dream
|  +- ruin
|  |  +- powered
|  |  |  `- shuttle
|  |  |     +- medium_1
|  |  |     +- medium_2
|  |  |     +- medium_3
|  |  |     `- medium_4
|  |  `- unpowered
|  +- science
|  |  +- explab
|  |  +- lab
|  |  +- misc_lab
|  |  |  `- range
|  |  +- mixing
|  |  |  `- chamber
|  |  +- nanite
|  |  +- research
|  |  |  `- abandoned
|  |  +- robotics
|  |  |  +- lab
|  |  |  `- mechbay
|  |  +- server
|  |  +- storage
|  |  +- test_area
|  |  `- xenobiology
|  +- security
|  |  +- brig
|  |  +- checkpoint
|  |  |  +- auxiliary
|  |  |  +- customs
|  |  |  |  `- auxiliary
|  |  |  +- engineering
|  |  |  +- escape
|  |  |  +- medical
|  |  |  +- science
|  |  |  |  `- research
|  |  |  `- supply
|  |  +- courtroom
|  |  +- detectives_office
|  |  |  `- private_investigators_office
|  |  +- execution
|  |  |  +- education
|  |  |  `- transfer
|  |  +- main
|  |  +- nuke_storage
|  |  +- prison
|  |  +- processing
|  |  |  `- cremation
|  |  +- range
|  |  `- warden
|  +- server
|  +- solar
|  |  +- aft
|  |  +- aux
|  |  |  +- port
|  |  |  `- starboard
|  |  +- fore
|  |  +- port
|  |  |  +- aft
|  |  |  `- fore
|  |  `- starboard
|  |     +- aft
|  |     `- fore
|  +- space
|  |  `- nearstation
|  +- start
|  +- storage
|  |  +- art
|  |  +- emergency
|  |  |  +- port
|  |  |  `- starboard
|  |  +- eva
|  |  +- primary
|  |  +- tcom
|  |  +- tech
|  |  `- tools
|  +- syndicate_mothership
|  |  +- control
|  |  `- elite_squad
|  +- tcommsat
|  |  +- computer
|  |  `- server
|  +- tdome
|  |  +- arena
|  |  +- arena_source
|  |  +- tdome1
|  |  +- tdome2
|  |  +- tdomeadmin
|  |  `- tdomeobserve
|  +- teleporter
|  +- template_noop
|  +- testroom
|  +- underwater
|  +- vacant_room
|  |  +- commissary
|  |  `- office
|  `- wizard_station
+- datum
|  +- achievement_data
|  +- action
|  |  +- boss
|  |  |  `- lich_summon_minions
|  |  +- clan_hierarchy
|  |  |  +- command_subordinate
|  |  |  +- locate_subordinate
|  |  |  +- mass_command
|  |  |  `- summon_subordinate
|  |  +- clan_menu
|  |  +- cooldown
|  |  |  +- mob_cooldown
|  |  |  |  +- bear_swipe
|  |  |  |  +- dragon_leap
|  |  |  |  +- fire_breath
|  |  |  |  |  +- cone
|  |  |  |  |  `- mass_fire
|  |  |  |  `- stone_throw
|  |  |  +- spell
|  |  |  |  +- advance
|  |  |  |  +- air_strike
|  |  |  |  +- arcyne_forge
|  |  |  |  |  `- miracle
|  |  |  |  +- arcyne_fortress
|  |  |  |  +- arrow_ward
|  |  |  |  +- ascension
|  |  |  |  +- azurean_phalanx
|  |  |  |  +- battle_ward
|  |  |  |  +- bestow_ward
|  |  |  |  +- bind_weapon
|  |  |  |  +- blade_burst
|  |  |  |  +- blade_dance
|  |  |  |  +- blade_of_psydon
|  |  |  |  +- blink
|  |  |  |  |  +- glimmer_hare
|  |  |  |  |  `- shadowstep
|  |  |  |  +- caedo
|  |  |  |  +- cataclysm
|  |  |  |  +- charge
|  |  |  |  +- chill_food
|  |  |  |  +- conjure_aegis
|  |  |  |  +- conjure_arcyne_ward
|  |  |  |  |  +- crystalhide
|  |  |  |  |  `- dragonhide
|  |  |  |  +- create_campfire
|  |  |  |  +- crescendo
|  |  |  |  +- crush
|  |  |  |  +- darkvision
|  |  |  |  |  `- miracle
|  |  |  |  |     `- undivided
|  |  |  |  +- earthen_wall
|  |  |  |  +- emergence
|  |  |  |  +- empower_weapon
|  |  |  |  +- enlarge
|  |  |  |  +- ensnare
|  |  |  |  |  `- kinesis
|  |  |  |  +- featherfall
|  |  |  |  +- find_familiar
|  |  |  |  +- fire_blast
|  |  |  |  +- fire_curtain
|  |  |  |  +- fist_of_psydon
|  |  |  |  +- forcewall
|  |  |  |  +- fortitude
|  |  |  |  +- frost_blast
|  |  |  |  +- frozen_mist
|  |  |  |  +- gate_of_reckoning
|  |  |  |  +- giants_strength
|  |  |  |  +- grasp_of_psydon
|  |  |  |  +- gravity
|  |  |  |  +- gravity_anchor
|  |  |  |  +- great_shelter
|  |  |  |  +- greater_cleaning
|  |  |  |  +- greater_thunderstrike
|  |  |  |  +- guidance
|  |  |  |  +- haste
|  |  |  |  +- hawks_eyes
|  |  |  |  +- heavens_strike
|  |  |  |  +- iron_skin
|  |  |  |  +- leap
|  |  |  |  +- learnspell
|  |  |  |  +- lesser_knock
|  |  |  |  |  `- miracle
|  |  |  |  +- leyline_anchor
|  |  |  |  +- light
|  |  |  |  +- magicians_brick
|  |  |  |  +- magicians_stone
|  |  |  |  +- mass_crush
|  |  |  |  +- mass_gravity
|  |  |  |  +- mending
|  |  |  |  |  `- lesser
|  |  |  |  +- message
|  |  |  |  +- message_familiar
|  |  |  |  +- message_summoner
|  |  |  |  +- meteor_strike
|  |  |  |  +- mindlink
|  |  |  |  +- miracle
|  |  |  |  |  `- necra_consecrate
|  |  |  |  +- mirror_transform
|  |  |  |  +- nondetection
|  |  |  |  +- projectile
|  |  |  |  |  +- arc_bolt
|  |  |  |  |  +- arcyne_lance
|  |  |  |  |  +- azurean_pilum
|  |  |  |  |  +- blade_storm
|  |  |  |  |  +- blood_bolt
|  |  |  |  |  +- boulder_strike
|  |  |  |  |  +- fetch
|  |  |  |  |  +- fireball
|  |  |  |  |  |  +- artillery
|  |  |  |  |  |  `- greater
|  |  |  |  |  +- frost_bolt
|  |  |  |  |  +- gravel_blast
|  |  |  |  |  +- greater_arcyne_bolt
|  |  |  |  |  +- ice_burst
|  |  |  |  |  +- iron_tempest
|  |  |  |  |  +- lesser_fetch
|  |  |  |  |  +- lesser_repel
|  |  |  |  |  +- lightning_bolt
|  |  |  |  |  +- repel
|  |  |  |  |  +- sawblade_volley
|  |  |  |  |  +- soulshot
|  |  |  |  |  +- spitfire
|  |  |  |  |  +- stygian_efflorescence
|  |  |  |  |  `- vicious_mockery
|  |  |  |  +- raise_deadite
|  |  |  |  +- recall_weapon
|  |  |  |  +- repulse
|  |  |  |  |  +- voiddragon
|  |  |  |  |  `- werewolf
|  |  |  |  +- reversion
|  |  |  |  +- reversion_trigger
|  |  |  |  +- rhythm
|  |  |  |  |  +- concussive
|  |  |  |  |  +- frigid
|  |  |  |  |  +- regenerating
|  |  |  |  |  `- resonating
|  |  |  |  +- shatter
|  |  |  |  +- snap_freeze
|  |  |  |  +- song
|  |  |  |  |  +- accelakathist
|  |  |  |  |  +- discordant_dirge
|  |  |  |  |  +- enervating_elegy
|  |  |  |  |  +- fervor_song
|  |  |  |  |  +- furtive_fortissimo
|  |  |  |  |  +- intellectual_interval
|  |  |  |  |  +- rattling_requiem
|  |  |  |  |  +- recovery_song
|  |  |  |  |  +- rejuvenation_song
|  |  |  |  |  `- resolute_refrain
|  |  |  |  +- stoneskin
|  |  |  |  +- storm_of_psydon
|  |  |  |  +- thunderstrike
|  |  |  |  +- touch
|  |  |  |  |  +- prestidigitation
|  |  |  |  |  `- rune_ward
|  |  |  |  +- tremor
|  |  |  |  `- wither
|  |  |  `- vomit
|  |  +- coven
|  |  +- innate
|  |  |  +- flight
|  |  |  `- megafauna_attack
|  |  +- item_action
|  |  |  +- displayDetectiveScanResults
|  |  |  +- organ_action
|  |  |  |  +- colossus
|  |  |  |  +- cursed_heart
|  |  |  |  +- toggle
|  |  |  |  `- use
|  |  |  `- toggle_voice_box
|  |  +- report
|  |  +- spell_action
|  |  |  `- spell
|  |  +- vehicle
|  |  |  `- ridden
|  |  `- vote
|  +- admin_help
|  +- admin_help_tickets
|  +- admin_rank
|  +- admins
|  +- advclass
|  |  +- absolver
|  |  +- acolyte
|  |  +- apothecary
|  |  +- archivist
|  |  +- assassin_hitman
|  |  +- assassin_poisoner
|  |  +- assassin_ranger
|  |  +- barbersurgeon
|  |  +- bathmaster
|  |  +- bathworker
|  |  |  +- courtesan
|  |  |  `- harlot
|  |  +- bishop
|  |  +- blacksmith
|  |  +- brigand
|  |  +- cheesemaker
|  |  +- cleric
|  |  |  +- cantor
|  |  |  +- missionary
|  |  |  `- paladin
|  |  +- clerk
|  |  +- confessor
|  |  +- cook
|  |  +- councillor
|  |  |  +- advisor
|  |  |  +- cofferer
|  |  |  `- herald
|  |  +- courtmage
|  |  +- crusader
|  |  +- disciple
|  |  +- druid
|  |  +- drunkard
|  |  +- elder
|  |  +- farmermaster
|  |  +- fisher
|  |  +- fishermaster
|  |  +- foreigner
|  |  |  +- bronzeclad
|  |  |  +- fencerguy
|  |  |  +- lesserblackoak
|  |  |  +- refugee
|  |  |  +- repentant
|  |  |  +- shepherd
|  |  |  +- slaver
|  |  |  `- yoruku
|  |  +- gnoll
|  |  |  +- berserker
|  |  |  +- knight
|  |  |  +- shaman
|  |  |  `- templar
|  |  +- gnoll_impure
|  |  +- greater_skeleton
|  |  |  +- lich
|  |  |  |  +- ballistiares
|  |  |  |  +- bulwark
|  |  |  |  +- bulwarkrare
|  |  |  |  +- legionnaire
|  |  |  |  +- rareballistiares
|  |  |  |  +- sapper
|  |  |  |  `- spellblade
|  |  |  `- necro
|  |  |     `- shambler
|  |  +- grenzel_envoy
|  |  +- grenzel_guard
|  |  +- grenzel_priest
|  |  +- guildmaster
|  |  +- guildsman
|  |  |  +- architect
|  |  |  +- artificer
|  |  |  `- blacksmith
|  |  +- hag
|  |  +- hand
|  |  |  +- advisor
|  |  |  +- blademaster
|  |  |  `- spymaster
|  |  +- heartfelt
|  |  |  +- hand
|  |  |  |  +- advisor
|  |  |  |  +- marshal
|  |  |  |  `- steward
|  |  |  +- knight
|  |  |  +- lord
|  |  |  |  +- archmage
|  |  |  |  +- chief
|  |  |  |  `- lord
|  |  |  `- retinue
|  |  |     +- armorer
|  |  |     +- courtier
|  |  |     +- housearb
|  |  |     +- houseguard
|  |  |     +- jester
|  |  |     +- magos
|  |  |     +- physician
|  |  |     +- prior
|  |  |     +- servant
|  |  |     `- squire
|  |  +- hedgealchemist
|  |  +- hedgeknight
|  |  +- hedgemage
|  |  +- heir
|  |  |  +- aristocrat
|  |  |  +- bookworm
|  |  |  +- daring
|  |  |  +- inbred
|  |  |  `- scamp
|  |  +- homesteader
|  |  +- hunter
|  |  |  `- spear
|  |  +- iconoclast
|  |  +- innkeeper
|  |  +- inquisitor
|  |  |  +- inspector
|  |  |  `- ordinator
|  |  +- keeper
|  |  +- kj_knight
|  |  +- kj_squire
|  |  +- knave
|  |  +- knight
|  |  |  +- footknight
|  |  |  +- heavy
|  |  |  +- irregularknight
|  |  |  +- knightchampion
|  |  |  `- mountedknight
|  |  +- levy
|  |  +- lord
|  |  |  +- inbred
|  |  |  +- mage
|  |  |  +- merchant
|  |  |  `- warrior
|  |  +- lunatic
|  |  +- mage
|  |  |  +- spellblade
|  |  |  +- spellfist
|  |  |  `- spellsinger
|  |  +- manorguard
|  |  |  +- bailiff
|  |  |  +- cavalry
|  |  |  +- footsman
|  |  |  +- skirmisher
|  |  |  `- standard_bearer
|  |  +- marshal
|  |  |  +- classic
|  |  |  `- kcommander
|  |  +- martyr
|  |  +- masterblacksmith
|  |  +- masterchef
|  |  +- mercenary
|  |  |  +- anthrax
|  |  |  +- anthrax_assassin
|  |  |  +- atgervi
|  |  |  |  `- shaman
|  |  |  +- blackoak
|  |  |  |  +- adept
|  |  |  |  `- ranger
|  |  |  +- chonin
|  |  |  +- desert_rider
|  |  |  |  +- almah
|  |  |  |  +- sahir
|  |  |  |  `- zeybek
|  |  |  +- etrusca
|  |  |  |  +- balestrieri
|  |  |  |  `- condottiero
|  |  |  +- forlorn
|  |  |  +- freelancer
|  |  |  |  +- lancer
|  |  |  |  `- sabrist
|  |  |  +- grenzelhoft
|  |  |  |  +- crossbowman
|  |  |  |  +- halberdier
|  |  |  |  `- mage
|  |  |  +- gronn
|  |  |  +- gronnheavy
|  |  |  +- grudgebearer
|  |  |  |  `- soldier
|  |  |  +- hangyaku
|  |  |  +- lirvanmerc
|  |  |  +- routier
|  |  |  +- rumaclan
|  |  |  |  `- sasu
|  |  |  +- seonjang
|  |  |  +- steppesman
|  |  |  +- trollslayer
|  |  |  +- underdweller
|  |  |  +- vaquero
|  |  |  `- warscholar
|  |  |     +- pontifex
|  |  |     `- vizier
|  |  +- merchant
|  |  +- miner
|  |  +- minermaster
|  |  +- minstrel
|  |  +- mystic
|  |  |  +- holyblade
|  |  |  +- resilientsoul
|  |  |  `- theurgist
|  |  +- noble
|  |  |  +- knighte
|  |  |  `- squire
|  |  +- nudist
|  |  +- peasant
|  |  +- physician
|  |  +- pick_everything
|  |  +- potter
|  |  +- psyaltrist
|  |  +- psydoniantemplar
|  |  +- ranesheni_advisor
|  |  +- ranesheni_amirah
|  |  +- ranesheni_emir
|  |  +- ranesheni_janissary
|  |  +- ranger
|  |  |  +- bombadier
|  |  |  +- bwanderer
|  |  |  `- wayfarer
|  |  +- rogue
|  |  |  +- bard
|  |  |  +- swashbuckler
|  |  |  `- thief
|  |  +- runaway_prisoner_commoner
|  |  +- runaway_prisoner_mage
|  |  +- runaway_prisoner_noble
|  |  +- seamstress
|  |  +- sellsword
|  |  +- seneschal
|  |  |  +- chiefbutler
|  |  |  +- headmaid
|  |  |  `- seneschal
|  |  +- sergeant
|  |  |  `- sergeant
|  |  +- servant
|  |  |  +- maid
|  |  |  +- manservant
|  |  |  `- servant
|  |  +- sexton
|  |  |  +- gravetender
|  |  |  `- groundskeeper
|  |  +- sfighter
|  |  |  +- barbarian
|  |  |  +- deprived
|  |  |  +- duelist
|  |  |  +- ironclad
|  |  |  `- mhunter
|  |  +- shophand
|  |  +- soilson
|  |  +- sojourner
|  |  +- squire
|  |  |  +- footman
|  |  |  +- lancer
|  |  |  `- skirmisher
|  |  +- steward
|  |  +- suitor
|  |  |  +- envoy
|  |  |  +- gallant
|  |  |  `- schemer
|  |  +- tailor
|  |  +- tapster
|  |  +- templar
|  |  |  +- crusader
|  |  |  +- monk
|  |  |  `- noc_spellblade
|  |  +- thug
|  |  |  +- bigman
|  |  |  +- goon
|  |  |  `- wiseguy
|  |  +- torso
|  |  +- towncrier
|  |  +- trader
|  |  |  +- brewer
|  |  |  +- cuisiner
|  |  |  +- doomsayer
|  |  |  +- harlequin
|  |  |  +- jeweler
|  |  |  +- peddler
|  |  |  +- scholar
|  |  |  `- servant
|  |  +- vagabond_beggar
|  |  +- vagabond_courier
|  |  +- vagabond_excommunicated
|  |  +- vagabond_goatherd
|  |  +- vagabond_mage
|  |  +- vagabond_original
|  |  +- vagabond_runner
|  |  +- vagabond_scholar
|  |  +- vagabond_unraveled
|  |  +- vagabond_wanted
|  |  +- vampire_spawn
|  |  +- veteran
|  |  |  +- battlemaster
|  |  |  +- calvaryman
|  |  |  +- footman
|  |  |  +- merc
|  |  |  +- scout
|  |  |  `- spy
|  |  +- wapprentice
|  |  |  +- alchemist
|  |  |  +- apprentice
|  |  |  +- associate
|  |  |  `- spellblade
|  |  +- warden
|  |  |  `- warden
|  |  +- witch
|  |  +- woodworker
|  |  `- wretch
|  |     +- ancient_deathknight
|  |     +- ancient_spellblade
|  |     +- berserker
|  |     +- deserter
|  |     |  `- generic
|  |     +- heretic
|  |     |  `- spy
|  |     +- heretic_spellblade
|  |     +- heretic_spellfist
|  |     +- licker
|  |     +- mistwalker
|  |     +- munitioneer
|  |     +- necromancer
|  |     +- outlaw
|  |     +- pariah
|  |     +- plaguebearer
|  |     +- poacher
|  |     +- pyromaniac
|  |     +- roguemage
|  |     +- slasher
|  |     `- vigilante
|  +- ai_behavior
|  |  +- apply_bandage
|  |  +- attack_obstructions
|  |  +- basic_melee_attack
|  |  |  +- abyssal
|  |  |  +- human_npc
|  |  |  `- opportunistic
|  |  +- basic_ranged_attack
|  |  +- break_restraints
|  |  +- call_for_help
|  |  +- call_reinforcements
|  |  +- cocoon_target
|  |  +- consume_healing_drink
|  |  +- cover_minimum_distance
|  |  +- eat_dead_body
|  |  +- eat_food
|  |  +- eat_food_from_ground
|  |  +- equip_target
|  |  +- find_aggro_targets
|  |  +- find_and_set
|  |  |  +- armor
|  |  |  +- better_weapon
|  |  |  +- cocoon_target
|  |  |  +- conscious_person
|  |  |  +- dead_bodies
|  |  |  +- edible
|  |  |  +- human_beg
|  |  |  +- in_hands
|  |  |  |  `- given_list
|  |  |  +- in_list
|  |  |  |  +- closest_turf
|  |  |  |  +- saiga
|  |  |  |  `- turf_types
|  |  |  +- nearby_friends
|  |  |  +- nearest_wall
|  |  |  `- pawn_must_hold_item
|  |  +- find_next_deadite_migration_step
|  |  +- find_potential_targets
|  |  |  +- bog_troll
|  |  |  +- human
|  |  |  +- mimic
|  |  |  +- mole
|  |  |  +- nearest
|  |  |  +- rat
|  |  |  +- spider
|  |  |  `- troll
|  |  +- follow
|  |  +- follow_friend
|  |  |  `- mirespider
|  |  +- human_npc_climb_tree
|  |  +- human_npc_leap
|  |  +- human_npc_move_to_flank
|  |  +- kick
|  |  +- loot_pick_up
|  |  +- loot_strip_body
|  |  +- move_to_cardinal
|  |  +- move_to_target
|  |  +- npc_kick_attack
|  |  +- perform_emote
|  |  +- perform_speech
|  |  +- pursue_to_range
|  |  +- ranged_attack_bow
|  |  +- retrieve_arrow
|  |  +- run_away_from_target
|  |  |  `- until_destination
|  |  +- simple_rest_and_recuperate
|  |  +- static_melee_attack
|  |  +- step_away
|  |  +- target_from_retaliate_list
|  |  |  `- nearest
|  |  +- targeted_mob_ability
|  |  |  +- and_clear_target
|  |  |  `- min_range
|  |  +- travel_towards
|  |  |  `- stop_on_arrival
|  |  +- travel_towards_atom
|  |  +- use_in_hand
|  |  +- use_on_object
|  |  +- use_powder
|  |  `- use_throwable
|  +- ai_controller
|  |  +- air_primordial
|  |  +- assassin
|  |  |  `- ancient
|  |  +- big_rat
|  |  +- deepone
|  |  +- deepone_ranged
|  |  +- direbear
|  |  +- dragger
|  |  +- dragon
|  |  +- dreamfiend_unbound
|  |  +- dreamfiend_unbound_ancient
|  |  +- elite_orc
|  |  |  `- event
|  |  +- flame_primordial
|  |  +- fretensis
|  |  +- generic
|  |  |  `- goat
|  |  +- haunt
|  |  +- headless
|  |  +- hostile_friend
|  |  +- human_npc
|  |  +- mimic
|  |  +- minotaur
|  |  +- mirespider
|  |  +- mirespider_lurker
|  |  +- mirespider_paralytic
|  |  +- mole
|  |  +- mossback
|  |  +- mudcrab
|  |  +- orc
|  |  |  `- event
|  |  +- orc_ranged
|  |  |  `- event
|  |  +- reiver_crossbow
|  |  +- reiver_rider
|  |  |  `- lance
|  |  +- simple_skeleton
|  |  |  `- event
|  |  +- skeleton_ranged
|  |  |  `- event
|  |  +- skeleton_spear
|  |  |  `- event
|  |  +- spear_orc
|  |  +- spider
|  |  |  `- honeyspider
|  |  +- spirit_vengeance
|  |  +- troll
|  |  +- troll_cave
|  |  +- undead
|  |  |  `- wolf
|  |  +- volf
|  |  `- water_primordial
|  +- ai_movement
|  |  +- astar
|  |  +- basic_avoidance
|  |  |  `- backstep
|  |  +- dumb
|  |  `- hybrid_pathing
|  |     `- gnome
|  +- ai_planning_subtree
|  |  +- aggro_find_target
|  |  |  +- bum
|  |  |  `- species_hostile
|  |  +- attack_obstacle_in_path
|  |  +- basic_melee_attack_subtree
|  |  |  +- abyssal
|  |  |  +- bog_troll
|  |  |  +- human_npc
|  |  |  +- mimic
|  |  |  +- opportunistic
|  |  |  |  `- event_loc
|  |  |  `- spear
|  |  +- basic_ranged_attack_subtree
|  |  |  `- mirespider_lurker
|  |  +- being_a_minion
|  |  |  `- mirespider
|  |  +- blink_if_far
|  |  +- call_for_help
|  |  +- call_reinforcements
|  |  +- cocoon_target
|  |  +- deadite_migration
|  |  +- eat_dead_body
|  |  |  +- bog_troll
|  |  |  `- mimic
|  |  +- eat_food
|  |  |  `- farm_animals
|  |  +- equip_item
|  |  +- find_cocoon_target
|  |  +- find_dead_bodies
|  |  |  +- mimic
|  |  |  +- mole
|  |  |  `- troll
|  |  +- find_food
|  |  |  +- mole
|  |  |  +- rat
|  |  |  +- spider
|  |  |  `- troll
|  |  +- find_nearest_thing_which_attacked_me_to_flee
|  |  +- find_weapon
|  |  +- flee_target
|  |  |  +- from_flee_key
|  |  |  `- until_destination
|  |  +- kick
|  |  +- kick_attack
|  |  +- leap_attack
|  |  +- loot
|  |  +- move_to_cardinal
|  |  +- random_speech
|  |  +- ranged_attack_subtree
|  |  +- retrieve_arrows
|  |  +- simple_find_nearest_target_to_flee
|  |  +- simple_find_target
|  |  |  +- bog_troll
|  |  |  +- closest
|  |  |  +- mimic
|  |  |  +- mole
|  |  |  +- rat
|  |  |  +- spider
|  |  |  `- troll
|  |  +- simple_self_recovery
|  |  |  +- dragon
|  |  |  +- genericanimal
|  |  |  `- humanoid
|  |  +- spacing
|  |  |  +- cover_minimum_distance
|  |  |  +- melee
|  |  |  +- ranged
|  |  |  `- spear
|  |  +- squad_flank
|  |  +- stamina_disengage
|  |  +- target_retaliate
|  |  |  `- to_flee
|  |  +- targeted_mob_ability
|  |  |  `- continue_planning
|  |  +- travel_to_point
|  |  |  `- and_clear_target
|  |  |     +- reinforce
|  |  |     `- wander
|  |  +- tree_climb
|  |  +- use_bandage
|  |  +- use_powder
|  |  |  `- bum
|  |  `- use_throwable
|  +- alch_cauldron_recipe
|  |  +- antidote
|  |  +- berrypoison
|  |  +- big_health_potion
|  |  +- big_mana_potion
|  |  +- big_stam_poison
|  |  +- big_stamina_potion
|  |  +- con_potion
|  |  +- doompoison
|  |  +- end_potion
|  |  +- fire_potion
|  |  +- health_potion
|  |  +- int_potion
|  |  +- lck_potion
|  |  +- mana_potion
|  |  +- per_potion
|  |  +- spd_potion
|  |  +- stam_poison
|  |  +- stamina_potion
|  |  +- str_potion
|  |  `- strong_antidote
|  +- alch_grind_recipe
|  |  +- artemisia_seed
|  |  +- atropa_seed
|  |  +- benedictus_seed
|  |  +- berrypowder
|  |  +- blessed_silver_bar
|  |  +- bone
|  |  +- calendula_seed
|  |  +- coal_ore
|  |  +- crow
|  |  +- dry_westleach
|  |  +- euphrasia_seed
|  |  +- fish
|  |  +- fyritius
|  |  +- gold_bar
|  |  +- gold_ore
|  |  +- horn
|  |  +- hypericum_seed
|  |  +- infernaldust
|  |  +- iron_bar
|  |  +- iron_ore
|  |  +- manabloompowder
|  |  +- matricaria_seed
|  |  +- mentha_seed
|  |  +- mineraldustblue
|  |  +- mineraldustdiamond
|  |  +- mineraldustgreen
|  |  +- mineraldustriddle
|  |  +- mineraldustviolet
|  |  +- mineraldustyellow
|  |  +- ozium
|  |  +- paris_seed
|  |  +- poppy
|  |  +- puresalt
|  |  +- rosa_seed
|  |  +- salvia_seed
|  |  +- scrap
|  |  +- seeds
|  |  +- seedsherb
|  |  +- silver_bar
|  |  +- silver_ore
|  |  +- sinew
|  |  +- sunflower
|  |  +- swampweed
|  |  +- swampweed_dried
|  |  +- symphitum_seed
|  |  +- taraxacum_seed
|  |  +- urtica_seed
|  |  +- valeriana_seed
|  |  `- westleach
|  +- alt_grip
|  |  +- halfsword
|  |  |  +- frei
|  |  |  `- greatsword
|  |  +- mordhau
|  |  |  +- broadsword
|  |  |  |  +- dream_broadsword
|  |  |  |  `- forgotten_blade
|  |  |  +- greatsword
|  |  |  `- sword
|  |  |     `- frei
|  |  `- roof_guard
|  +- ambush_config
|  |  +- bog_guard_deserters
|  |  |  `- hard
|  |  +- deepone_party
|  |  +- duo_minotaur
|  |  +- duo_treasure_hunter
|  |  +- heavy_skeleton_party
|  |  +- medium_skeleton_party
|  |  +- mirespiders_ambush
|  |  +- mirespiders_aragn
|  |  +- mirespiders_crawlers
|  |  +- mirespiders_unfair
|  |  +- pair_of_direbear
|  |  +- singular_minotaur
|  |  +- solo_treasure_hunter
|  |  +- treasure_hunter_posse
|  |  +- trio_of_highwaymen
|  |  `- triple_deepone
|  +- ambush_entry
|  |  +- mob
|  |  `- group
|  +- antag_retainer
|  +- antagonist
|  |  +- ascendant
|  |  +- aspirant
|  |  |  +- ruler
|  |  |  `- supporter
|  |  +- assassin
|  |  +- bandit
|  |  +- brainwashed
|  |  +- chosen
|  |  +- custom
|  |  +- dreamwalker
|  |  +- gnoll
|  |  +- greentext
|  |  +- hag
|  |  +- heartbreaker
|  |  +- lich
|  |  +- maniac
|  |  +- prebel
|  |  |  `- head
|  |  +- separatist
|  |  +- skeleton
|  |  |  `- knight
|  |  +- space_dragon
|  |  +- traitor
|  |  +- unbound_death_knight
|  |  +- unbound_spellblade
|  |  +- valentine
|  |  +- vampire
|  |  |  +- ancillae
|  |  |  +- licker
|  |  |  +- lord
|  |  |  `- thinblood
|  |  +- werewolf
|  |  |  `- lesser
|  |  +- wretch
|  |  +- zizo_knight
|  |  |  `- squire
|  |  `- zombie
|  +- anvil_recipe
|  |  +- armor
|  |  |  +- aalloy
|  |  |  |  +- barbute
|  |  |  |  +- bascinet
|  |  |  |  +- boots
|  |  |  |  +- bracers
|  |  |  |  +- chaingaunts
|  |  |  |  +- chainkilt
|  |  |  |  +- chainmail
|  |  |  |  +- coif
|  |  |  |  +- cuirass
|  |  |  |  +- gorget
|  |  |  |  +- halfplate
|  |  |  |  +- hauberk
|  |  |  |  +- mask
|  |  |  |  +- plategaunts
|  |  |  |  +- platelegs
|  |  |  |  +- sandals
|  |  |  |  `- savoyard
|  |  |  +- blacksteel
|  |  |  |  +- bucket
|  |  |  |  +- cuirass
|  |  |  |  +- halfplatechest
|  |  |  |  +- modern
|  |  |  |  |  +- armet
|  |  |  |  |  +- halfplatechest
|  |  |  |  |  +- plateboots
|  |  |  |  |  +- platechest
|  |  |  |  |  +- plategloves
|  |  |  |  |  +- platelegs
|  |  |  |  |  `- sugarloaf
|  |  |  |  +- plateboots
|  |  |  |  +- platechest
|  |  |  |  +- plategloves
|  |  |  |  `- platelegs
|  |  |  +- blessedsilver
|  |  |  |  +- armetpsy
|  |  |  |  |  `- inq
|  |  |  |  +- helmbucketpsy
|  |  |  |  |  `- inq
|  |  |  |  +- helmetabso
|  |  |  |  |  `- inq
|  |  |  |  +- helmsallpsy
|  |  |  |  |  `- inq
|  |  |  |  +- psychestplate
|  |  |  |  |  `- inq
|  |  |  |  +- psycuirass
|  |  |  |  |  `- inq
|  |  |  |  +- psyfullplate
|  |  |  |  |  `- inq
|  |  |  |  +- psyfullplatealt
|  |  |  |  |  `- inq
|  |  |  |  `- psyhalfplate
|  |  |  |     `- inq
|  |  |  +- bronze
|  |  |  |  +- barbute
|  |  |  |  +- bevor
|  |  |  |  +- bracers
|  |  |  |  +- cuirass
|  |  |  |  +- fullplate
|  |  |  |  +- gorget
|  |  |  |  +- greaves
|  |  |  |  +- halfplate
|  |  |  |  +- illyria
|  |  |  |  +- mask
|  |  |  |  +- maskclassic
|  |  |  |  +- murmillo
|  |  |  |  +- protector
|  |  |  |  `- skirt
|  |  |  +- copper
|  |  |  |  +- bracers
|  |  |  |  +- cap
|  |  |  |  +- chest
|  |  |  |  +- gorget
|  |  |  |  `- mask
|  |  |  +- decorated
|  |  |  |  +- belt
|  |  |  |  +- helmetbuc
|  |  |  |  +- helmetbucalt
|  |  |  |  +- horseshoes
|  |  |  |  +- mask
|  |  |  |  `- maskc
|  |  |  +- gold
|  |  |  |  +- armet
|  |  |  |  +- armetcrown
|  |  |  |  +- bracers
|  |  |  |  +- cuirass
|  |  |  |  +- cuirasshero
|  |  |  |  +- gorget
|  |  |  |  +- greaves
|  |  |  |  +- helmet
|  |  |  |  `- helmetcrown
|  |  |  +- helmetgoblin
|  |  |  +- holysteel
|  |  |  |  +- abyssorhelm
|  |  |  |  +- astratahelm
|  |  |  |  +- astratahelmtemplar
|  |  |  |  +- dendorhelm
|  |  |  |  +- eorahelm
|  |  |  |  +- eorahelmtemplar
|  |  |  |  +- malumhelmtemplar
|  |  |  |  +- necrahelm
|  |  |  |  +- necrahelmtemplar
|  |  |  |  +- nochelm
|  |  |  |  +- pestrahelmtemplar
|  |  |  |  +- ravoxhelm
|  |  |  |  `- xylixhelm
|  |  |  +- iron
|  |  |  |  +- bevor
|  |  |  |  +- boot
|  |  |  |  +- bracers
|  |  |  |  +- breastplate
|  |  |  |  +- bucket
|  |  |  |  +- chaincoif
|  |  |  |  +- chainglove
|  |  |  |  +- chainleg
|  |  |  |  |  `- kilt
|  |  |  |  +- cursed_collar
|  |  |  |  +- fullplate
|  |  |  |  +- gorget
|  |  |  |  +- halfplate
|  |  |  |  +- haubergeon
|  |  |  |  +- hauberk
|  |  |  |  +- helmethorned
|  |  |  |  +- horseshoes
|  |  |  |  +- jackchain
|  |  |  |  +- kettle
|  |  |  |  +- knightarmet
|  |  |  |  +- knightarmetgreatplume
|  |  |  |  +- knighthelmet
|  |  |  |  +- lbrigandine
|  |  |  |  +- mask
|  |  |  |  +- plategauntlets
|  |  |  |  +- platelegs
|  |  |  |  +- sallet
|  |  |  |  |  `- visor
|  |  |  |  +- skullcap
|  |  |  |  +- splintarms
|  |  |  |  +- splintlegs
|  |  |  |  `- wildguard
|  |  |  +- paalloy
|  |  |  |  +- barbute
|  |  |  |  +- bascinet
|  |  |  |  +- boots
|  |  |  |  +- bracers
|  |  |  |  +- chaingaunts
|  |  |  |  +- chainkilt
|  |  |  |  +- chainmail
|  |  |  |  +- coif
|  |  |  |  +- cuirass
|  |  |  |  +- gorget
|  |  |  |  +- halfplate
|  |  |  |  +- hauberk
|  |  |  |  +- mask
|  |  |  |  +- plategaunts
|  |  |  |  +- platelegs
|  |  |  |  +- sandals
|  |  |  |  `- savoyard
|  |  |  +- plategoblin
|  |  |  +- silver
|  |  |  |  +- belt
|  |  |  |  `- horseshoes
|  |  |  `- steel
|  |  |     +- barding
|  |  |     |  `- fogbeast
|  |  |     +- barredhelm
|  |  |     +- bascinet
|  |  |     +- beakhelm
|  |  |     +- belt
|  |  |     |  `- tasset
|  |  |     +- bevor
|  |  |     +- bogman
|  |  |     +- brayette
|  |  |     +- chaincoif
|  |  |     +- chainglove
|  |  |     +- chainkini
|  |  |     +- chainleg
|  |  |     +- chainlegs
|  |  |     |  `- kilt
|  |  |     +- chainmantle
|  |  |     +- chainskirt
|  |  |     +- coatplates
|  |  |     +- cuirass
|  |  |     |  +- fluted
|  |  |     |  `- legacy
|  |  |     +- etruscanbascinet
|  |  |     +- frogmouth
|  |  |     +- frogmouthgreatplume
|  |  |     +- fullchaincoif
|  |  |     +- fullplate
|  |  |     |  +- fluted
|  |  |     |  |  `- legacy
|  |  |     |  `- legacy
|  |  |     +- fullplatebikini
|  |  |     +- halfplate
|  |  |     |  +- fluted
|  |  |     |  `- legacy
|  |  |     +- haubergeon
|  |  |     +- hauberk
|  |  |     +- helmetarmet
|  |  |     +- helmetbarbute
|  |  |     +- helmetbarbutedunk
|  |  |     +- helmetbarbutevisor
|  |  |     +- helmetbuc
|  |  |     +- helmetbucalt
|  |  |     +- helmethounskull
|  |  |     +- helmetkettle
|  |  |     +- helmetknight
|  |  |     +- helmetknightarmet
|  |  |     +- helmetknightarmetgreatplume
|  |  |     +- helmetnasal
|  |  |     +- helmetpig
|  |  |     +- helmetsall
|  |  |     +- helmetsallv
|  |  |     +- helmetwinged
|  |  |     +- horseshoes
|  |  |     +- lightcuirass
|  |  |     +- lighthaubergeon
|  |  |     +- mask
|  |  |     +- platebikini
|  |  |     +- plateboot
|  |  |     +- platebracer
|  |  |     +- plateglove
|  |  |     +- platelegs
|  |  |     +- plateskirt
|  |  |     +- savoyard
|  |  |     +- scalemail
|  |  |     +- sgorget
|  |  |     +- slittedkettle
|  |  |     +- splintarms
|  |  |     +- splintlegs
|  |  |     +- steel
|  |  |     |  `- brigandine
|  |  |     `- widehelmetkettle
|  |  +- engineering
|  |  |  +- artificerarmor
|  |  |  +- bronze
|  |  |  |  +- autoshears
|  |  |  |  +- cog
|  |  |  |  +- coolingbackpack
|  |  |  |  +- grappler
|  |  |  |  +- headhook
|  |  |  |  +- keys
|  |  |  |  +- lamptern
|  |  |  |  +- lockimprover
|  |  |  |  +- locks
|  |  |  |  +- metalizer
|  |  |  |  +- mobilestove
|  |  |  |  +- orestore
|  |  |  |  +- prosthetic
|  |  |  |  |  +- bronzeprosthetic
|  |  |  |  |  +- goldprosthetic
|  |  |  |  |  +- ironprosthetic
|  |  |  |  |  `- steelprosthetic
|  |  |  |  +- smokebomb
|  |  |  |  +- tools
|  |  |  |  |  `- drill
|  |  |  |  +- waterpurifier
|  |  |  |  `- wrench
|  |  |  +- chains
|  |  |  +- emeraldchoker
|  |  |  +- flint
|  |  |  +- folding_alchcauldron
|  |  |  +- folding_alchstation_stored
|  |  |  +- folding_table
|  |  |  +- houndstone
|  |  |  +- ironscissors
|  |  |  +- jingle_bells
|  |  |  +- lockpickring
|  |  |  +- lockpicks
|  |  |  +- mess_kit
|  |  |  +- nails
|  |  |  +- scomstone
|  |  |  +- serfstone
|  |  |  +- steamshield
|  |  |  +- steelscissors
|  |  |  `- volticgauntlet
|  |  +- gold_dildo
|  |  +- iron_dildo
|  |  +- silver_dildo
|  |  +- steel_dildo
|  |  +- tools
|  |  |  +- aalloy
|  |  |  |  +- agobs
|  |  |  |  +- amugs
|  |  |  |  +- bowl
|  |  |  |  +- fork
|  |  |  |  +- hammer
|  |  |  |  +- hoe
|  |  |  |  +- pan
|  |  |  |  +- pick
|  |  |  |  +- pitchfork
|  |  |  |  +- platter
|  |  |  |  +- pot
|  |  |  |  +- sewingneedle
|  |  |  |  +- shovel
|  |  |  |  +- sickle
|  |  |  |  +- spoon
|  |  |  |  +- thresher
|  |  |  |  `- tongs
|  |  |  +- aspect_canisters
|  |  |  +- blacksteel
|  |  |  |  +- hammer
|  |  |  |  +- pick
|  |  |  |  `- tongs
|  |  |  +- bowl
|  |  |  |  `- aalloy
|  |  |  +- bronze
|  |  |  |  +- amugs
|  |  |  |  +- bowl
|  |  |  |  +- chisel
|  |  |  |  +- fork
|  |  |  |  +- gobs
|  |  |  |  +- hammer
|  |  |  |  +- handsaw
|  |  |  |  +- hoe
|  |  |  |  +- lamptern
|  |  |  |  +- pan
|  |  |  |  +- pick
|  |  |  |  +- pitchfork
|  |  |  |  +- platter
|  |  |  |  +- pot
|  |  |  |  +- sewingneedle
|  |  |  |  +- shovel
|  |  |  |  +- sickle
|  |  |  |  +- spoon
|  |  |  |  +- thresher
|  |  |  |  `- tongs
|  |  |  +- copper
|  |  |  |  +- hammer
|  |  |  |  +- lamptern
|  |  |  |  +- pick
|  |  |  |  +- pitchfork
|  |  |  |  +- platter
|  |  |  |  +- pot
|  |  |  |  `- sickle
|  |  |  +- gold
|  |  |  |  +- cups
|  |  |  |  `- platter
|  |  |  +- heartbeast_canisters
|  |  |  +- heartbeast_vials
|  |  |  +- iron
|  |  |  |  +- blowrod
|  |  |  |  +- bowl
|  |  |  |  +- chisel
|  |  |  |  +- cups
|  |  |  |  +- fork
|  |  |  |  +- hammer
|  |  |  |  +- handsaw
|  |  |  |  +- headhook
|  |  |  |  +- hoe
|  |  |  |  +- kettle
|  |  |  |  +- keyring
|  |  |  |  +- lamptern
|  |  |  |  +- lamptern_fog
|  |  |  |  +- lamptern_fog_blacksteel
|  |  |  |  +- pan
|  |  |  |  +- pick
|  |  |  |  +- pitchfork
|  |  |  |  +- pot
|  |  |  |  +- scrap
|  |  |  |  +- sewingneedle
|  |  |  |  +- shovel
|  |  |  |  +- sickle
|  |  |  |  +- spoon
|  |  |  |  +- surgerytools
|  |  |  |  +- thresher
|  |  |  |  +- tongs
|  |  |  |  `- torch
|  |  |  +- silver
|  |  |  |  +- cups
|  |  |  |  +- platter
|  |  |  |  `- shovel
|  |  |  +- steel
|  |  |  |  +- chefknife
|  |  |  |  +- cleaver
|  |  |  |  +- cups
|  |  |  |  +- hammer
|  |  |  |  +- metalrepairkit
|  |  |  |  `- pick
|  |  |  `- tin
|  |  |     +- fork
|  |  |     +- platter
|  |  |     `- spoon
|  |  +- valuables
|  |  |  +- aalloy
|  |  |  +- anointedberserksword
|  |  |  +- astcrossbronze
|  |  |  +- blacksteel
|  |  |  +- daemonslayer
|  |  |  +- deprivedshortsword
|  |  |  +- deprivedsword
|  |  |  +- diamondg
|  |  |  +- diamonds
|  |  |  +- dragon
|  |  |  +- duelring
|  |  |  +- emeringg
|  |  |  +- emerings
|  |  |  +- gold
|  |  |  +- graggar
|  |  |  +- graggarbronze
|  |  |  +- hope
|  |  |  +- iron
|  |  |  |  +- berserksword
|  |  |  |  +- berserkswordalt
|  |  |  |  +- berserkswordblade
|  |  |  |  +- berserkswordgrip
|  |  |  |  +- execution
|  |  |  |  `- rawheapofiron
|  |  |  +- malumcrossbronze
|  |  |  +- matthios
|  |  |  +- noccrossaalloy
|  |  |  +- noccrossbronze
|  |  |  +- noccrosspaalloy
|  |  |  +- ornateamulet
|  |  |  +- psicrossbronze
|  |  |  +- psycrossaalloy
|  |  |  +- psycrosspaalloy
|  |  |  +- quartzg
|  |  |  +- quartzs
|  |  |  +- ravoxbronze
|  |  |  +- ringa
|  |  |  +- ringb
|  |  |  +- ringbs
|  |  |  +- ringg
|  |  |  +- rings
|  |  |  +- rubyg
|  |  |  +- rubys
|  |  |  +- sapphireg
|  |  |  +- sapphires
|  |  |  +- signet
|  |  |  |  `- silver
|  |  |  |     `- inq
|  |  |  +- signetalt
|  |  |  +- silver
|  |  |  +- skullamulet
|  |  |  +- statuebronze
|  |  |  +- steel
|  |  |  +- terminus
|  |  |  +- topazg
|  |  |  +- topazs
|  |  |  +- weddingringb
|  |  |  +- weddingringg
|  |  |  +- weddingringp
|  |  |  +- weddingrings
|  |  |  +- zcross_iron
|  |  |  +- zcrossaalloy
|  |  |  +- zcrossbronze
|  |  |  `- zcrosspaalloy
|  |  `- weapons
|  |     +- aalloy
|  |     |  +- arrows
|  |     |  +- bardiche
|  |     |  +- bolts
|  |     |  +- dagger
|  |     |  +- flail
|  |     |  +- flamberge
|  |     |  +- gladius
|  |     |  +- grandmace
|  |     |  +- gsw
|  |     |  +- handaxe
|  |     |  +- heavybolts
|  |     |  +- javelin
|  |     |  +- khopesh
|  |     |  +- knuckles
|  |     |  +- mace
|  |     |  +- shortsword
|  |     |  +- slingbullets
|  |     |  +- spear
|  |     |  +- tossblade
|  |     |  `- warhammer
|  |     +- alloy
|  |     |  `- shield
|  |     +- blacksteel
|  |     |  +- arming
|  |     |  +- decsword
|  |     |  `- flamberge
|  |     +- bronze
|  |     |  +- arrows
|  |     |  +- axe
|  |     |  +- axegauntlet
|  |     |  +- battleaxe
|  |     |  +- battlemace
|  |     |  +- bolts
|  |     |  +- broadsword
|  |     |  +- bronzegreatshield
|  |     |  +- bronzeknuckle
|  |     |  +- bronzeshield
|  |     |  +- combatknife
|  |     |  +- dagger
|  |     |  +- falchion
|  |     |  +- gladius
|  |     |  +- greataxe
|  |     |  +- greatkhopesh
|  |     |  +- heavybolts
|  |     |  +- javelin
|  |     |  +- katar
|  |     |  +- mace
|  |     |  +- messer
|  |     |  +- sabre
|  |     |  +- slingbullets
|  |     |  +- spear
|  |     |  +- spearwinged
|  |     |  +- sword
|  |     |  +- trident
|  |     |  `- whip
|  |     +- copper
|  |     |  +- caxe
|  |     |  +- cbludgeon
|  |     |  +- cdagger
|  |     |  +- cmesser
|  |     |  +- crhomphaia
|  |     |  `- cspears
|  |     +- decorated
|  |     |  +- axe
|  |     |  +- dagger
|  |     |  +- elfdagger
|  |     |  +- elfsaber
|  |     |  +- gladius
|  |     |  +- longsword
|  |     |  +- macesil
|  |     |  +- rapier
|  |     |  +- saber
|  |     |  +- scabbard
|  |     |  +- sheath
|  |     |  +- sword
|  |     |  +- swordsil
|  |     |  `- warclub
|  |     +- gold
|  |     |  +- arming
|  |     |  +- mace
|  |     |  `- shield
|  |     +- holysteel
|  |     |  +- church_longsword
|  |     |  +- church_spear
|  |     |  +- decashield
|  |     |  +- decasword
|  |     |  `- malum_sword
|  |     +- iron
|  |     |  +- arrows
|  |     |  +- axe
|  |     |  +- axelegacy
|  |     |  +- bardiche
|  |     |  +- bluntbolts
|  |     |  +- bolts
|  |     |  |  `- light
|  |     |  +- broadsword
|  |     |  +- claymore
|  |     |  +- combatknife
|  |     |  +- cudgel
|  |     |  +- dagger
|  |     |  +- dory
|  |     |  +- flail
|  |     |  +- flailalt
|  |     |  +- greataxe
|  |     |  +- greatflail
|  |     |  +- greatsword
|  |     |  +- hatchet
|  |     |  +- heavybolts
|  |     |  +- huntknife
|  |     |  +- javelin
|  |     |  +- lucerne
|  |     |  +- mace
|  |     |  +- maul
|  |     |  +- messer
|  |     |  +- polemace
|  |     |  +- roundshield
|  |     |  +- sabre
|  |     |  +- slingbullets
|  |     |  +- spear
|  |     |  +- spear_trainer
|  |     |  +- sword
|  |     |  +- swordshort
|  |     |  +- tossblade
|  |     |  +- towershield
|  |     |  `- warhammer
|  |     +- lithmyc
|  |     |  `- mace
|  |     +- paalloy
|  |     |  +- arrows
|  |     |  +- bardiche
|  |     |  +- bolts
|  |     |  +- dagger
|  |     |  +- flamberge
|  |     |  +- gladius
|  |     |  +- grandmace
|  |     |  +- gsw
|  |     |  +- handaxe
|  |     |  +- heavybolts
|  |     |  +- javelin
|  |     |  +- khopesh
|  |     |  +- knuckles
|  |     |  +- mace
|  |     |  +- shortsword
|  |     |  +- slingbullets
|  |     |  +- spear
|  |     |  +- tossblade
|  |     |  `- warhammer
|  |     +- psy
|  |     |  +- axe
|  |     |  |  `- inq
|  |     |  +- cudgelmace
|  |     |  |  `- inq
|  |     |  +- dagger
|  |     |  |  `- inq
|  |     |  +- gsword
|  |     |  |  `- inq
|  |     |  +- halberd
|  |     |  |  `- inq
|  |     |  +- katar
|  |     |  |  `- inq
|  |     |  +- knuckles
|  |     |  |  `- inq
|  |     |  +- mace
|  |     |  |  `- inq
|  |     |  +- shortsword
|  |     |  |  `- inq
|  |     |  +- spear
|  |     |  |  `- inq
|  |     |  +- sword
|  |     |  |  `- inq
|  |     |  `- whip
|  |     |     `- inq
|  |     +- silver
|  |     |  +- broadsword
|  |     |  +- claws
|  |     |  +- dagger
|  |     |  +- exec
|  |     |  +- flangedmace
|  |     |  +- greatsword
|  |     |  +- javelin
|  |     |  +- katar
|  |     |  +- longsword
|  |     |  +- mace
|  |     |  +- morningstar
|  |     |  +- poleaxe
|  |     |  +- quarterstaff
|  |     |  +- rapier
|  |     |  +- scabbard
|  |     |  +- sheath
|  |     |  +- shortsword
|  |     |  +- spear
|  |     |  +- stake
|  |     |  +- sword
|  |     |  +- tossblade
|  |     |  +- waraxe
|  |     |  +- warhammer
|  |     |  `- whip
|  |     `- steel
|  |        +- aplongsword
|  |        +- arrows
|  |        +- axe
|  |        +- battleaxe
|  |        +- billhook
|  |        +- boarspear
|  |        +- broadsword
|  |        +- buckler
|  |        +- combatknife
|  |        +- combatknifemesser
|  |        +- cutlass
|  |        +- dagger
|  |        +- dagger_trainer
|  |        +- daggerparrying
|  |        +- daggerrondel
|  |        +- eaglebeak
|  |        +- estoc
|  |        +- falchion
|  |        +- falx
|  |        +- fishspear
|  |        +- flail
|  |        +- flamb
|  |        +- grandmace
|  |        +- greataxe
|  |        |  +- doublehead
|  |        |  `- knight
|  |        +- greatsword
|  |        +- halberd
|  |        +- heavybolts
|  |        +- hurlbat
|  |        +- javelin
|  |        +- katar
|  |        +- kiteshield
|  |        +- kriegmesser
|  |        +- lance
|  |        +- longsword
|  |        +- mace
|  |        +- maul
|  |        +- messer
|  |        +- messeralt
|  |        +- naginata
|  |        +- partizan
|  |        +- punchdagger
|  |        +- rapier
|  |        +- rhomphaia
|  |        +- saber
|  |        +- sflangedmace
|  |        +- slingbullets
|  |        +- steelknuckle
|  |        +- swarhammer
|  |        +- sword
|  |        +- swordshort
|  |        +- tossblade
|  |        +- trainingsword
|  |        `- xbow
|  +- armor
|  +- aspect_picker
|  +- aspect_viewer
|  +- asset
|  |  +- changelog_item
|  |  +- group
|  |  +- json
|  |  |  `- icon_ref_map
|  |  +- simple
|  |  |  +- blackedstone_class_menu_slop_layout
|  |  |  +- blackedstone_triumph_buy_menu_slop_layout
|  |  |  +- headshot_imgs
|  |  |  +- icon_states
|  |  |  |  `- multiple_icons
|  |  |  +- jquery
|  |  |  +- namespaced
|  |  |  |  +- common
|  |  |  |  +- fontawesome
|  |  |  |  `- tgfont
|  |  |  +- roguefonts
|  |  |  +- tgui
|  |  |  `- tgui_panel
|  |  +- spritesheet
|  |  |  +- anvil_recipes
|  |  |  +- pumpkin_carvings
|  |  |  `- simple
|  |  `- spritesheet_batched
|  +- asset_cache_item
|  +- asset_transport
|  |  `- webroot
|  +- atom_hud
|  |  +- alternate_appearance
|  |  |  `- basic
|  |  |     +- blessedAware
|  |  |     +- everyone
|  |  |     +- observers
|  |  |     +- onePerson
|  |  |     `- People
|  |  `- antag
|  |     `- hidden
|  +- autosmither_queue_entry
|  +- award
|  |  +- achievement
|  |  |  +- boss
|  |  |  |  +- blood_miner_crusher
|  |  |  |  +- blood_miner_kill
|  |  |  |  +- boss_killer
|  |  |  |  +- bubblegum_crusher
|  |  |  |  +- bubblegum_kill
|  |  |  |  +- colussus_crusher
|  |  |  |  +- colussus_kill
|  |  |  |  +- drake_crusher
|  |  |  |  +- drake_kill
|  |  |  |  +- hierophant_crusher
|  |  |  |  +- hierophant_kill
|  |  |  |  +- legion_crusher
|  |  |  |  +- legion_kill
|  |  |  |  +- swarmer_beacon_crusher
|  |  |  |  +- swarmer_beacon_kill
|  |  |  |  `- tendril_exterminator
|  |  |  `- misc
|  |  |     +- feat_of_strength
|  |  |     +- getting_an_upgrade
|  |  |     +- helbitaljanken
|  |  |     +- meteor_examine
|  |  |     +- pulse
|  |  |     +- round_and_full
|  |  |     +- the_best_driver
|  |  |     `- time_waste
|  |  `- score
|  +- bank_account
|  |  +- department
|  |  `- remote
|  +- beam
|  +- bitfield
|  +- body_marking
|  |  +- backspots
|  |  +- bangs
|  |  +- belly
|  |  +- bellyscale
|  |  +- bellyscaleslim
|  |  +- bellyscaleslimsmooth
|  |  +- bellyscalesmooth
|  |  +- bellyslim
|  |  +- bun
|  |  +- butt
|  |  +- buttscale
|  |  +- construct_head_round
|  |  +- construct_head_standard
|  |  +- construct_plating_heavy
|  |  +- construct_plating_light
|  |  +- construct_plating_medium
|  |  +- construct_psyclops_eye
|  |  +- construct_standard_eyes
|  |  +- construct_visor_eyes
|  |  +- drake_eyes
|  |  +- eyeliner
|  |  +- flushed_cheeks
|  |  +- front
|  |  +- gradient
|  |  +- harlequin
|  |  +- harlequinreversed
|  |  +- kobold_scale
|  |  +- moth
|  |  |  +- burnt_off
|  |  |  +- deathhead
|  |  |  +- gothic
|  |  |  +- grayscale
|  |  |  |  +- burnt_off
|  |  |  |  +- deathhead
|  |  |  |  +- gothic
|  |  |  |  +- jungle
|  |  |  |  +- lovers
|  |  |  |  +- moonfly
|  |  |  |  +- oakworm
|  |  |  |  +- poison
|  |  |  |  +- ragged
|  |  |  |  +- reddish
|  |  |  |  +- royal
|  |  |  |  +- whitefly
|  |  |  |  `- witchwing
|  |  |  +- jungle
|  |  |  +- lovers
|  |  |  +- moonfly
|  |  |  +- oakworm
|  |  |  +- poison
|  |  |  +- ragged
|  |  |  +- reddish
|  |  |  +- royal
|  |  |  +- whitefly
|  |  |  `- witchwing
|  |  +- nose
|  |  +- plain
|  |  +- small
|  |  |  +- backspots
|  |  |  +- bangs
|  |  |  +- belly
|  |  |  +- bellyslim
|  |  |  +- bun
|  |  |  +- butt
|  |  |  +- front
|  |  |  +- nose
|  |  |  +- plain
|  |  |  +- sock
|  |  |  |  `- tertiary
|  |  |  +- socklonger
|  |  |  +- spotted
|  |  |  +- tie
|  |  |  +- tiesmall
|  |  |  `- tips
|  |  +- sock
|  |  |  `- tertiary
|  |  +- socklonger
|  |  +- spotted
|  |  +- tie
|  |  +- tiesmall
|  |  +- tiger
|  |  |  `- dark
|  |  +- tips
|  |  `- tonage
|  +- body_marking_set
|  |  +- belly
|  |  +- bellyscale
|  |  +- bellysocks
|  |  +- bellysockstertiary
|  |  +- construct_plating_heavy
|  |  +- construct_plating_light
|  |  +- construct_plating_medium
|  |  +- gradient
|  |  +- kobold_scale
|  |  +- moth
|  |  |  +- burnt_off
|  |  |  +- deathhead
|  |  |  +- gothic
|  |  |  +- jungle
|  |  |  +- lovers
|  |  |  +- moonfly
|  |  |  +- oakworm
|  |  |  +- poison
|  |  |  +- ragged
|  |  |  +- reddish
|  |  |  +- royal
|  |  |  +- whitefly
|  |  |  `- witchwing
|  |  +- none
|  |  +- socks
|  |  +- tiger
|  |  `- tiger_dark
|  +- bodypart_feature
|  |  +- accessory
|  |  +- crest
|  |  +- face_detail
|  |  +- hair
|  |  |  +- facial
|  |  |  `- head
|  |  +- legwear
|  |  +- piercing
|  |  `- underwear
|  +- book_entry
|  |  +- brewing
|  |  +- magic1
|  |  `- magic2
|  +- boss_active_timed_battle
|  +- bounty
|  +- brain_trauma
|  |  +- hypnosis
|  |  +- magic
|  |  |  +- antimagic
|  |  |  +- lumiphobia
|  |  |  `- poltergeist
|  |  +- mild
|  |  |  +- concussion
|  |  |  +- dumbness
|  |  |  +- expressive_aphasia
|  |  |  +- hallucinations
|  |  |  +- healthy
|  |  |  +- mind_echo
|  |  |  +- muscle_spasms
|  |  |  +- muscle_weakness
|  |  |  +- nervous_cough
|  |  |  +- phobia
|  |  |  |  +- anime
|  |  |  |  +- authority
|  |  |  |  +- birds
|  |  |  |  +- clowns
|  |  |  |  +- conspiracies
|  |  |  |  +- doctors
|  |  |  |  +- falling
|  |  |  |  +- greytide
|  |  |  |  +- lizards
|  |  |  |  +- robots
|  |  |  |  +- security
|  |  |  |  +- skeletons
|  |  |  |  +- snakes
|  |  |  |  +- space
|  |  |  |  +- spiders
|  |  |  |  +- strangers
|  |  |  |  `- supernatural
|  |  |  +- speech_impediment
|  |  |  `- stuttering
|  |  +- severe
|  |  |  +- aphasia
|  |  |  +- blindness
|  |  |  +- discoordination
|  |  |  +- hypnotic_stupor
|  |  |  +- monophobia
|  |  |  +- mute
|  |  |  +- narcolepsy
|  |  |  +- pacifism
|  |  |  +- paralysis
|  |  |  |  `- paraplegic
|  |  |  `- split_personality
|  |  |     `- brainwashing
|  |  `- special
|  |     +- beepsky
|  |     +- bluespace_prophet
|  |     +- death_whispers
|  |     +- existential_crisis
|  |     +- godwoken
|  |     `- tenacity
|  +- brewing_recipe
|  |  +- aqua_vitae
|  |  |  +- pear
|  |  |  +- plum
|  |  |  +- strawberry
|  |  |  `- tangerine
|  |  +- beer
|  |  |  +- oat
|  |  |  `- rice
|  |  +- blackberry_wine
|  |  +- brandy
|  |  |  +- pear
|  |  |  +- plum
|  |  |  +- strawberry
|  |  |  `- tangerine
|  |  +- cabbage
|  |  +- cider
|  |  |  +- ambrosia
|  |  |  +- pear
|  |  |  `- strawberry
|  |  +- fermentedcrab
|  |  +- golden_calendula_tea
|  |  +- jack_wine
|  |  +- limoncello
|  |  +- liquor
|  |  |  `- ricespirit
|  |  +- luxintenebre
|  |  +- mead
|  |  +- molasses
|  |  +- onion
|  |  +- plum_wine
|  |  +- raspberry_wine
|  |  +- rum
|  |  +- soothing_valerian_tea
|  |  +- spidermead
|  |  +- tangerine_wine
|  |  +- voddena
|  |  +- whipwine
|  |  +- winespiced
|  |  `- zarum
|  +- browser
|  |  +- modal
|  |  |  +- listpicker
|  |  |  `- preflikepicker
|  |  `- noclose
|  +- buildmode
|  +- buildmode_mode
|  |  +- advanced
|  |  +- area_edit
|  |  +- basic
|  |  +- boom
|  |  +- copy
|  |  +- fill
|  |  +- mapgen
|  |  +- throwing
|  |  `- varedit
|  +- callback
|  +- callback_select
|  +- cell_tracker
|  +- changelog
|  +- charflaw
|  |  +- addiction
|  |  |  +- alcoholic
|  |  |  +- caffiend
|  |  |  +- clamorous
|  |  |  +- godfearing
|  |  |  +- junkie
|  |  |  +- kleptomaniac
|  |  |  +- lovefiend
|  |  |  +- masochist
|  |  |  +- paranoid
|  |  |  +- sadist
|  |  |  +- smoker
|  |  |  +- thrillseeker
|  |  |  `- voyeur
|  |  +- averse
|  |  +- badsight
|  |  +- clingy
|  |  +- colorblind
|  |  +- critweakness
|  |  +- eznoflaw
|  |  +- finicky
|  |  +- greedy
|  |  +- hunted
|  |  +- indebted
|  |  +- leprosy
|  |  +- limbloss
|  |  |  +- arm_l
|  |  |  `- arm_r
|  |  +- lonely
|  |  +- mind_broken
|  |  +- mute
|  |  +- narcoleptic
|  |  +- noeyeall
|  |  +- noeyel
|  |  +- noeyer
|  |  +- noflaw
|  |  +- paranoid
|  |  +- randflaw
|  |  +- sleepless
|  |  `- unintelligible
|  +- chat_payload
|  +- chatmessage
|  +- chemical_reaction
|  |  +- acetaldehyde
|  |  +- acetone
|  |  +- acetone_oxide
|  |  +- alch
|  |  |  +- acoffee
|  |  |  `- vitae_essence
|  |  +- ammonia
|  |  +- ash
|  |  +- bonehurtingjuice
|  |  +- candlefication
|  |  +- carbondioxide
|  |  +- chloralhydrate
|  |  +- concentrated_barbers_aid
|  |  +- cryptobiolin
|  |  +- cyanide
|  |  +- diethylamine
|  |  +- drying_agent
|  |  +- facid
|  |  +- fentanyl
|  |  +- foam
|  |  +- foaming_agent
|  |  +- formaldehyde
|  |  +- graintopowder
|  |  +- grosswaterboil
|  |  +- grosswaterify
|  |  +- hair_dye
|  |  +- heparin
|  |  +- impedrezene
|  |  +- ironfoam
|  |  +- lube
|  |  +- lye
|  |  +- lye2
|  |  +- meatification
|  |  +- metalfoam
|  |  +- monkey
|  |  +- mulligan
|  |  +- mutetoxin
|  |  +- nitracid
|  |  +- nitrous_oxide
|  |  +- oil
|  |  +- pentaerythritol
|  |  +- pestkiller
|  |  +- phenol
|  |  +- plantbgone
|  |  +- randomized
|  |  +- reagent_explosion
|  |  |  `- potassium_explosion
|  |  |     `- holyboom
|  |  +- royal_bee_jelly
|  |  +- salglu_solution
|  |  +- saltpetre
|  |  +- saltwaterboil
|  |  +- saltwaterify
|  |  +- smart_foam
|  |  +- smart_foaming_agent
|  |  +- sodiumchloride
|  |  +- space_cleaner
|  |  +- space_drugs
|  |  +- sulfonal
|  |  +- surfactant
|  |  `- weedkiller
|  +- chimeric_tech_node
|  |  +- awaken_healing
|  |  +- awaken_resurrection
|  |  +- black_rose
|  |  +- corpse_ticks
|  |  +- enhanced_healing
|  |  +- enhanced_resurrection
|  |  +- infestation_attack_vector
|  |  +- infestation_capacity_1
|  |  +- infestation_capacity_2
|  |  +- infestation_capacity_3
|  |  +- infestation_rot_multiple_1
|  |  +- infestation_rot_multiple_2
|  |  +- infestation_rot_snacks
|  |  +- meat_decoy
|  |  +- residual_frankenbrew
|  |  `- viscera_decoy
|  +- cinematic
|  |  +- clownop
|  |  +- cult
|  |  +- cult_nuke
|  |  +- fake
|  |  +- malf
|  |  +- no_core
|  |  +- nuke_annihilation
|  |  +- nuke_far
|  |  +- nuke_miss
|  |  +- nuke_selfdestruct
|  |  +- nuke_selfdestruct_miss
|  |  `- nuke_win
|  +- clan
|  |  +- abyss
|  |  +- crimson_fang
|  |  +- custom
|  |  +- eoran
|  |  +- nosferatu
|  |  `- thronleer
|  +- clan_hierarchy_interface
|  +- clan_hierarchy_node
|  +- clan_leader
|  |  +- eoran
|  |  +- lord
|  |  +- nosferatu
|  |  +- thronleer
|  |  `- wretch
|  +- clan_menu_interface
|  +- class_age_mod
|  |  +- acolyte
|  |  +- adv_mage
|  |  +- apprentice_alchemist
|  |  +- apprentice_apprentice
|  |  +- apprentice_associate
|  |  +- archivist
|  |  +- bandit
|  |  |  `- hedgealchemist
|  |  +- barber_surgeon
|  |  +- cook
|  |  +- court_magician
|  |  +- court_physician
|  |  +- cuisiner
|  |  +- druid
|  |  +- exorcist
|  |  +- fisher
|  |  +- grand_duke
|  |  +- grenzel_mage
|  |  +- guildmaster
|  |  +- hand_advisor
|  |  +- hand_blademaster
|  |  +- hand_spymaster
|  |  +- innkeeper
|  |  +- mystic
|  |  +- pontifex
|  |  +- priest
|  |  +- seneschal
|  |  +- servant
|  |  +- soilson
|  |  +- tapster
|  |  +- veteran
|  |  |  +- battlemaster
|  |  |  +- cavalryman
|  |  |  +- footman
|  |  |  +- mercenary
|  |  |  +- scout
|  |  |  `- spy
|  |  +- vizier
|  |  +- war_scholar
|  |  +- witch
|  |  `- wretch
|  |     `- rogue_mage
|  +- class_register
|  +- class_select_handler
|  +- cleave_pattern
|  |  +- adjacent
|  |  +- forward_cleave
|  |  +- frontal_arc
|  |  +- horizontal_sweep
|  |  +- lance
|  |  `- wide_sweep
|  +- client_colour
|  |  +- cursed_heart_blood
|  |  +- glass_colour
|  |  |  +- blue
|  |  |  +- darkred
|  |  |  +- gray
|  |  |  +- green
|  |  |  +- lightblue
|  |  |  +- lightgreen
|  |  |  +- lightorange
|  |  |  +- orange
|  |  |  +- purple
|  |  |  +- red
|  |  |  `- yellow
|  |  +- maniac_marked
|  |  +- monochrome
|  |  |  +- blind
|  |  |  `- trance
|  |  +- nocshaded
|  |  +- stress_fade
|  |  +- test1
|  |  +- test2
|  |  +- test3
|  |  `- underwater
|  +- collective_message
|  +- combat_music
|  |  +- aavshepherd
|  |  +- acolyte
|  |  +- adjudicator
|  |  +- adventurer_2
|  |  +- adventurer_3
|  |  +- adventurer_4
|  |  +- adventurer_default
|  |  +- ascended
|  |  +- ascendedsavior
|  |  +- astrata
|  |  +- bandit_default
|  |  +- bandit_rogue
|  |  +- bandit_soldier
|  |  +- barbarian
|  |  +- beggar
|  |  +- blackoak
|  |  +- combat
|  |  +- combat_old_2
|  |  +- conddottiero
|  |  +- cultic
|  |  +- darkstar
|  |  +- deadite
|  |  +- default
|  |  +- dendor
|  |  +- desertrider
|  |  +- dungeoneer
|  |  +- dwarf
|  |  +- dying_world
|  |  +- dying_world_instrumental
|  |  +- eora
|  |  +- firestorm
|  |  +- forlorn
|  |  +- freifencer
|  |  +- freilancer
|  |  +- freisabrist
|  |  +- grenzelhoft
|  |  +- heretic_baotha
|  |  +- heretic_graggar
|  |  +- heretic_matthios
|  |  +- heretic_zizo
|  |  +- iconoclast
|  |  +- inquis_ordinator
|  |  +- inquisitor
|  |  +- jester
|  |  +- kazengite
|  |  +- knight
|  |  +- magician
|  |  +- man_at_arms
|  |  +- maniac
|  |  +- maniac_old
|  |  +- martyr
|  |  +- monastic
|  |  +- necra
|  |  +- noble
|  |  +- overlord
|  |  +- ozium
|  |  +- physician
|  |  +- poacher
|  |  +- ready_to_die
|  |  +- reckoning
|  |  +- routier
|  |  +- runaway_chariot
|  |  +- shaman
|  |  +- spymaster
|  |  +- squire
|  |  +- starsugar
|  |  +- steppe
|  |  +- thespian
|  |  +- town_dirt
|  |  +- town_heavyweights
|  |  +- town_leaders
|  |  +- town_skilled
|  |  +- vampire
|  |  +- vampire_old
|  |  +- vaquero
|  |  +- varangian
|  |  +- veteran
|  |  `- warscholar
|  +- component
|  |  +- action_item_overlay
|  |  +- adjustable_clothing
|  |  +- after_image
|  |  +- ai_aggro_system
|  |  +- ai_inventory_manager
|  |  +- anti_magic
|  |  +- arcyne_conduit
|  |  +- area_ambience
|  |  +- armour_filtering
|  |  |  +- negative
|  |  |  `- positive
|  |  +- arousal
|  |  +- art
|  |  |  `- rev
|  |  +- baotha_joyride
|  |  |  `- partner
|  |  +- beauty
|  |  +- beetlejuice
|  |  +- blessed_food
|  |  +- butchering
|  |  +- caltrop
|  |  +- chimeric_heart_beast
|  |  +- combat_vocalizer
|  |  +- conjured_item
|  |  +- connect_containers
|  |  +- connect_loc_behalf
|  |  +- connect_range
|  |  +- construction
|  |  +- convey
|  |  +- creamed
|  |  +- cursed_item
|  |  +- deadchat_control
|  |  +- deadite_animal_reanimation
|  |  +- debt_collector
|  |  +- decal
|  |  |  `- blood
|  |  +- dejavu
|  |  +- dream_echo
|  |  +- dream_weapon
|  |  +- dreamwalker_mark
|  |  +- dreamwalker_repair
|  |  +- edit_complainer
|  |  +- empathic_obsession
|  |  +- empprotection
|  |  +- eora_bond
|  |  |  `- partner
|  |  +- explodable
|  |  +- familial_bond
|  |  +- fit_clothing
|  |  +- fog_entity
|  |  +- fogged
|  |  +- footstep
|  |  +- forensics
|  |  +- gnoll_combat_tracker
|  |  +- hag_artifact_repair
|  |  +- hag_boon_manifestation
|  |  +- hag_curio_tracker
|  |  +- hag_enchanted_item
|  |  +- hag_magical_item
|  |  +- hag_magical_item_affinity
|  |  +- hideous_face
|  |  +- hoarded_item
|  |  +- holster
|  |  |  `- gwstrap
|  |  +- ignitable
|  |  |  +- fluff
|  |  |  |  +- sci_flame
|  |  |  |  `- sci_sand
|  |  |  `- warspear
|  |  +- igniter
|  |  +- immolation
|  |  |  `- partner
|  |  +- infection_spreader
|  |  +- infestation_black_rot
|  |  +- infestation_charges
|  |  +- item_equipped_movement_rustle
|  |  +- item_on_drop
|  |  |  `- dust
|  |  +- jousting
|  |  +- knockback
|  |  +- knockoff
|  |  +- knotting
|  |  +- layeredarmor
|  |  +- leechtick_attachment
|  |  +- lifesteal
|  |  +- lockon_aiming
|  |  +- magic_item
|  |  +- martyrweapon
|  |  +- mirage_border
|  |  +- mushroom_mace
|  |  +- orbiter
|  |  +- overlay_lighting
|  |  +- peaceflower_tracker
|  |  +- personal_crafting
|  |  +- pestilent_blade_enchant
|  |  +- pollutant
|  |  +- precious_creature
|  |  +- profaned
|  |  +- quest_object
|  |  |  +- courier
|  |  |  +- kill
|  |  |  +- mob_spawner
|  |  |  `- retrieval
|  |  +- riding
|  |  |  +- cyborg
|  |  |  `- human
|  |  +- rift_bound
|  |  +- rot
|  |  |  `- gibs
|  |  +- shrapnel
|  |  +- shrink
|  |  +- silverbless
|  |  +- simple_rotation
|  |  +- sizzle
|  |  +- skill_blessed
|  |  +- slippery
|  |  +- soulstoned
|  |  +- spawner
|  |  +- spill
|  |  +- spire_fiend
|  |  +- squeak
|  |  +- storage
|  |  |  `- concrete
|  |  |     +- grid
|  |  |     |  +- anvil_bin
|  |  |     |  +- headhook
|  |  |     |  |  `- bronze
|  |  |     |  +- magebag
|  |  |     |  +- meatsack
|  |  |     |  `- orestore
|  |  |     |     `- bronze
|  |  |     +- roguetown
|  |  |     |  +- backpack
|  |  |     |  +- belt
|  |  |     |  |  +- assassin
|  |  |     |  |  +- cloth
|  |  |     |  |  `- knife_belt
|  |  |     |  +- bin
|  |  |     |  +- cloak
|  |  |     |  |  `- lord
|  |  |     |  +- coin_pouch
|  |  |     |  |  +- cloth
|  |  |     |  |  `- merchant
|  |  |     |  +- dice_pouch
|  |  |     |  +- hat
|  |  |     |  +- keyring
|  |  |     |  +- mailmaster
|  |  |     |  +- messkit
|  |  |     |  +- sack
|  |  |     |  |  `- bag
|  |  |     |  +- saddle
|  |  |     |  +- satchel
|  |  |     |  |  `- cloth
|  |  |     |  +- surgery_bag
|  |  |     |  +- zig_bandolier
|  |  |     |  `- zig_box
|  |  |     `- tray
|  |  +- summoning
|  |  +- sunlight_vulnerability
|  |  +- swarming
|  |  +- tactical
|  |  +- temporary_pollution_emission
|  |  +- tether
|  |  +- twisted_food
|  |  +- vampire_disguise
|  |  |  `- nosferatu
|  |  +- waddling
|  |  +- wearertargeting
|  |  |  +- earprotection
|  |  |  `- punchcooldown
|  |  +- wet_floor
|  |  +- wise_tree_alert
|  |  `- wrestle_combat_tracker
|  +- config_entry
|  |  +- flag
|  |  |  +- admin_legacy_system
|  |  |  +- age_prompt_system
|  |  |  +- aggressive_changelog
|  |  |  +- allow_admin_asaycolor
|  |  |  +- allow_admin_ooccolor
|  |  |  +- allow_ai
|  |  |  +- allow_ai_multicam
|  |  |  +- allow_holidays
|  |  |  +- allow_latejoin_antagonists
|  |  |  +- allow_map_voting
|  |  |  +- allow_metadata
|  |  |  +- allow_random_events
|  |  |  +- allow_storyteller_pop_scaling
|  |  |  +- allow_vote_map
|  |  |  +- allow_vote_mode
|  |  |  +- allow_vote_restart
|  |  |  +- allow_webclient
|  |  |  +- announce_admin_login
|  |  |  +- announce_admin_logout
|  |  |  +- arrivals_shuttle_require_safe_latejoin
|  |  |  +- arrivals_shuttle_require_undocked
|  |  |  +- asset_simple_preload
|  |  |  +- assistants_have_maint_access
|  |  |  +- auto_deadmin_antagonists
|  |  |  +- auto_deadmin_heads
|  |  |  +- auto_deadmin_players
|  |  |  +- auto_deadmin_security
|  |  |  +- auto_deadmin_silicons
|  |  |  +- autoadmin
|  |  |  +- autoconvert_notes
|  |  |  +- automute_on
|  |  |  +- bsql_debug
|  |  |  +- byond_member_bypass_popcap
|  |  |  +- cache_assets
|  |  |  +- check_randomizer
|  |  |  +- client_warn_popup
|  |  |  +- debug_admin_hrefs
|  |  |  +- default_no_vote
|  |  |  +- disable_peaceborg
|  |  |  +- disable_secborg
|  |  |  +- dynamic_config_enabled
|  |  |  +- economy
|  |  |  +- elastic_middleware_enabled
|  |  |  +- emojis
|  |  |  +- enable_localhost_rank
|  |  |  +- enable_night_shifts
|  |  |  +- enforce_human_authority
|  |  |  +- everyone_has_maint_access
|  |  |  +- forbid_singulo_possession
|  |  |  +- force_random_names
|  |  |  +- ghost_interaction
|  |  |  +- grey_assistants
|  |  |  +- guest_ban
|  |  |  +- guest_jobban
|  |  |  +- hub
|  |  |  +- humans_need_surnames
|  |  |  +- ic_printing
|  |  |  +- irc_announce_new_game
|  |  |  +- irc_first_connection_alert
|  |  |  +- jobs_have_minimal_access
|  |  |  +- join_with_mutant_humans
|  |  |  +- kick_inactive
|  |  |  +- load_jobs_from_txt
|  |  |  +- load_legacy_ranks_only
|  |  |  +- log_access
|  |  |  +- log_admin
|  |  |  +- log_adminchat
|  |  |  +- log_attack
|  |  |  +- log_cloning
|  |  |  +- log_emote
|  |  |  +- log_game
|  |  |  +- log_job_debug
|  |  |  +- log_law
|  |  |  +- log_looc
|  |  |  +- log_manifest
|  |  |  +- log_mecha
|  |  |  +- log_npc_say
|  |  |  +- log_ooc
|  |  |  +- log_pda
|  |  |  +- log_pictures
|  |  |  +- log_prayer
|  |  |  +- log_say
|  |  |  +- log_telecomms
|  |  |  +- log_timers_on_bucket_reset
|  |  |  +- log_twitter
|  |  |  +- log_virus
|  |  |  +- log_vote
|  |  |  +- log_whisper
|  |  |  +- log_world_topic
|  |  |  +- maprotation
|  |  |  +- near_death_experience
|  |  |  +- no_dead_vote
|  |  |  +- no_intercept_report
|  |  |  +- norespawn
|  |  |  +- ooc_during_round
|  |  |  +- panic_bunker
|  |  |  +- picture_logging_camera
|  |  |  +- popup_admin_pm
|  |  |  +- preference_map_voting
|  |  |  +- protect_assistant_from_antagonist
|  |  |  +- protect_legacy_admins
|  |  |  +- protect_legacy_ranks
|  |  |  +- protect_roles_from_antagonist
|  |  |  +- randomize_shift_time
|  |  |  +- reactionary_explosions
|  |  |  +- reopen_roundstart_suicide_roles
|  |  |  +- reopen_roundstart_suicide_roles_command_positions
|  |  |  +- reopen_roundstart_suicide_roles_command_report
|  |  |  +- resume_after_initializations
|  |  |  +- revival_cloning
|  |  |  +- revival_pod_plants
|  |  |  +- roundstart_away
|  |  |  +- roundstart_traits
|  |  |  +- sandbox_autoclose
|  |  |  +- save_spritesheets
|  |  |  +- sec_start_brig
|  |  |  +- security_has_maint_access
|  |  |  +- see_own_notes
|  |  |  +- shift_time_realtime
|  |  |  +- show_game_type_odds
|  |  |  +- show_irc_name
|  |  |  +- silent_ai
|  |  |  +- silent_borg
|  |  |  +- smart_cache_assets
|  |  |  +- sql_enabled
|  |  |  +- starlight
|  |  |  +- use_account_age_for_jobs
|  |  |  +- use_age_restriction_for_jobs
|  |  |  +- use_antag_rep
|  |  |  +- use_exp_restrictions_admin_bypass
|  |  |  +- use_exp_restrictions_heads
|  |  |  +- use_exp_restrictions_heads_department
|  |  |  +- use_exp_restrictions_other
|  |  |  +- use_exp_tracking
|  |  |  +- useblacklist
|  |  |  +- usewhitelist
|  |  |  `- webclient_only_byond_members
|  |  +- keyed_list
|  |  |  +- antag_rep
|  |  |  +- continuous
|  |  |  +- cross_server
|  |  |  +- external_rsc_urls
|  |  |  +- law_weight
|  |  |  +- max_pop
|  |  |  +- midround_antag
|  |  |  +- min_pop
|  |  |  +- multiplicative_movespeed
|  |  |  +- probability
|  |  |  +- random_laws
|  |  |  +- roundstart_no_hard_check
|  |  |  `- roundstart_races
|  |  +- number
|  |  |  +- abductor_scaling_coeff
|  |  |  +- afk_period
|  |  |  +- antag_rep_maximum
|  |  |  +- arrivals_shuttle_dock_window
|  |  |  +- async_query_timeout
|  |  |  +- blocking_query_timeout
|  |  |  +- bombcap
|  |  |  +- border_control
|  |  |  +- brother_objectives_amount
|  |  |  +- brother_scaling_coeff
|  |  |  +- bsql_thread_limit
|  |  |  +- changeling_scaling_coeff
|  |  |  +- client_error_build
|  |  |  +- client_error_version
|  |  |  +- client_warn_version
|  |  |  +- damage_multiplier
|  |  |  +- default_antag_tickets
|  |  |  +- default_laws
|  |  |  +- emergency_shuttle_autocall_threshold
|  |  |  +- error_cooldown
|  |  |  +- error_limit
|  |  |  +- error_msg_delay
|  |  |  +- error_silence_time
|  |  |  +- events_min_players_mul
|  |  |  +- events_min_time_mul
|  |  |  +- extreme_popcap
|  |  |  +- fog_event_hour
|  |  |  +- fps
|  |  |  +- gateway_delay
|  |  |  +- githubrepoid
|  |  |  +- hard_popcap
|  |  |  +- id_console_jobslot_delay
|  |  |  +- inactivity_period
|  |  |  +- ipintel_rating_bad
|  |  |  +- ipintel_save_bad
|  |  |  +- ipintel_save_good
|  |  |  +- lavaland_budget
|  |  |  +- lobby_countdown
|  |  |  +- major_min_pop
|  |  |  +- major_point_gain_multiplier
|  |  |  +- major_point_threshold
|  |  |  +- major_pop_scale_penalty
|  |  |  +- major_pop_scale_threshold
|  |  |  +- major_roundstart_point_multiplier
|  |  |  +- maprotatechancedelta
|  |  |  +- max_law_len
|  |  |  +- max_tickets_per_roll
|  |  |  +- mc_tick_rate
|  |  |  |  +- base_mc_tick_rate
|  |  |  |  +- disable_high_pop_mc_mode_amount
|  |  |  |  +- high_pop_mc_mode_amount
|  |  |  |  `- high_pop_mc_tick_rate
|  |  |  +- mice_roundstart
|  |  |  +- midround_antag_life_check
|  |  |  +- midround_antag_time_check
|  |  |  +- minimal_access_threshold
|  |  |  +- minute_click_limit
|  |  |  +- minute_topic_limit
|  |  |  +- moderate_min_pop
|  |  |  +- moderate_point_gain_multiplier
|  |  |  +- moderate_point_threshold
|  |  |  +- moderate_pop_scale_penalty
|  |  |  +- moderate_pop_scale_threshold
|  |  |  +- moderate_roundstart_point_multiplier
|  |  |  +- monkeycap
|  |  |  +- movedelay
|  |  |  |  +- run_delay
|  |  |  |  `- walk_delay
|  |  |  +- mundane_min_pop
|  |  |  +- mundane_point_gain_multiplier
|  |  |  +- mundane_point_threshold
|  |  |  +- mundane_pop_scale_penalty
|  |  |  +- mundane_pop_scale_threshold
|  |  |  +- mundane_roundstart_point_multiplier
|  |  |  +- note_fresh_days
|  |  |  +- note_stale_days
|  |  |  +- notify_new_player_account_age
|  |  |  +- notify_new_player_age
|  |  |  +- objectives_min_pop
|  |  |  +- objectives_point_gain_multiplier
|  |  |  +- objectives_point_threshold
|  |  |  +- objectives_pop_scale_penalty
|  |  |  +- objectives_pop_scale_threshold
|  |  |  +- objectives_roundstart_point_multiplier
|  |  |  +- outdated_movedelay
|  |  |  |  +- animal_delay
|  |  |  |  +- human_delay
|  |  |  |  `- monkey_delay
|  |  |  +- overflow_cap
|  |  |  +- port
|  |  |  +- query_debug_log_timeout
|  |  |  +- reopen_roundstart_suicide_roles_delay
|  |  |  +- revival_brain_life
|  |  |  +- roleset_min_pop
|  |  |  +- roleset_point_gain_multiplier
|  |  |  +- roleset_point_threshold
|  |  |  +- roleset_pop_scale_penalty
|  |  |  +- roleset_pop_scale_threshold
|  |  |  +- roleset_roundstart_point_multiplier
|  |  |  +- round_end_countdown
|  |  |  +- rounds_until_hard_restart
|  |  |  +- second_click_limit
|  |  |  +- second_topic_limit
|  |  |  +- security_scaling_coeff
|  |  |  +- shuttle_refuel_delay
|  |  |  +- silicon_max_law_amount
|  |  |  +- soft_popcap
|  |  |  +- space_budget
|  |  |  +- tick_limit_mc_init
|  |  |  +- ticklag
|  |  |  +- traitor_objectives_amount
|  |  |  +- traitor_scaling_coeff
|  |  |  +- use_exp_restrictions_heads_hours
|  |  |  +- vote_delay
|  |  |  `- vote_period
|  |  +- number_list
|  |  |  +- fog_event_days
|  |  |  `- repeated_mode_adjust
|  |  `- string
|  |     +- address
|  |     +- alert_blue_downto
|  |     +- alert_blue_upto
|  |     +- alert_delta
|  |     +- alert_green
|  |     +- alert_red_downto
|  |     +- alert_red_upto
|  |     +- asset_cdn_url
|  |     +- asset_cdn_webroot
|  |     +- asset_transport
|  |     +- autoadmin_rank
|  |     +- banappeals
|  |     +- channel_announce_new_game_message
|  |     +- chat_announce_donator
|  |     +- chat_announce_new_game
|  |     +- chat_announce_verify
|  |     +- chat_announce_whitelist
|  |     +- chat_command_whitelist
|  |     +- client_error_message
|  |     +- client_warn_message
|  |     +- comms_key
|  |     +- cross_comms_name
|  |     +- default_view
|  |     +- default_view_square
|  |     +- discordurl
|  |     +- elastic_endpoint
|  |     +- extreme_popcap_message
|  |     +- feedback_database
|  |     +- feedback_login
|  |     +- feedback_password
|  |     +- feedback_tableprefix
|  |     +- gamelogurl
|  |     +- githuburl
|  |     +- hard_popcap_message
|  |     +- hostedby
|  |     +- invoke_youtubedl
|  |     +- ipintel_domain
|  |     +- ipintel_email
|  |     +- medal_hub_address
|  |     +- medal_hub_password
|  |     +- metrics_api_token
|  |     +- overflow_job
|  |     +- panic_bunker_message
|  |     +- panic_server_address
|  |     +- panic_server_name
|  |     +- roundstatsurl
|  |     +- rulesurl
|  |     +- server
|  |     +- servername
|  |     +- serversqlname
|  |     +- servertagline
|  |     +- soft_popcap_message
|  |     +- stationname
|  |     `- wikiurl
|  +- controller
|  |  +- configuration
|  |  +- failsafe
|  |  +- global_vars
|  |  +- master
|  |  `- subsystem
|  |     `- ticker
|  +- coven
|  |  +- auspex
|  |  +- bloodheal
|  |  +- celerity
|  |  +- demonic
|  |  +- eora
|  |  +- fae_trickery
|  |  +- obfuscate
|  |  +- potence
|  |  +- presence
|  |  +- quietus
|  |  `- siren
|  +- coven_power
|  |  +- auspex
|  |  |  +- ear_for_lies
|  |  |  +- heightened_senses
|  |  |  +- psychic_projection
|  |  |  `- spirit_touch
|  |  +- bloodheal
|  |  |  +- five
|  |  |  +- four
|  |  |  +- one
|  |  |  +- three
|  |  |  `- two
|  |  +- celerity
|  |  |  +- five
|  |  |  +- four
|  |  |  +- one
|  |  |  +- three
|  |  |  `- two
|  |  +- demonic
|  |  |  +- conflagration
|  |  |  +- deny_the_mother
|  |  |  +- fear_of_the_void_below
|  |  |  +- psychomachia
|  |  |  `- wall_of_fire
|  |  +- eora
|  |  |  +- artistic_inspiration
|  |  |  +- beautys_restoration
|  |  |  +- empathic_bond
|  |  |  `- familial_bond
|  |  +- fae_trickery
|  |  |  +- chanjelin_ward
|  |  |  +- darkling_trickery
|  |  |  +- fae_wrath
|  |  |  +- goblinism
|  |  |  `- riddle_phantastique
|  |  +- obfuscate
|  |  |  +- cloak_of_shadows
|  |  |  +- cloak_the_gathering
|  |  |  +- unseen_presence
|  |  |  `- vanish_from_the_minds_eye
|  |  +- potence
|  |  |  +- five
|  |  |  +- four
|  |  |  +- one
|  |  |  +- three
|  |  |  `- two
|  |  +- presence
|  |  |  +- awe
|  |  |  +- dread_gaze
|  |  |  +- fall
|  |  |  +- majesty
|  |  |  `- summon
|  |  +- quietus
|  |  |  +- baals_caress
|  |  |  +- dagons_call
|  |  |  +- scorpions_touch
|  |  |  +- silence_of_death
|  |  |  `- taste_of_death
|  |  `- siren
|  |     +- madrigal
|  |     +- phantom_speaker
|  |     +- shattering_crescendo
|  |     +- sirens_beckoning
|  |     `- the_missing_voice
|  +- coven_research_interface
|  +- coven_research_node
|  +- crafting_recipe
|  |  +- example
|  |  +- food
|  |  +- hair_dye
|  |  `- roguetown
|  |     +- alch
|  |     |  +- feaudust
|  |     |  `- magicdust
|  |     +- alchemy
|  |     |  +- abyss
|  |     |  +- applezig
|  |     |  +- b2app
|  |     |  +- bandage
|  |     |  +- bbomb
|  |     |  +- blackberryzig
|  |     |  +- c2irn
|  |     |  +- c2sto
|  |     |  +- calendulazig
|  |     |  +- carrotzig
|  |     |  +- cd2coa
|  |     |  +- chocolatezig
|  |     |  +- cl2st2copp
|  |     |  +- curerot
|  |     |  +- d2cla
|  |     |  +- d2ros
|  |     |  +- distill
|  |     |  +- f2gra
|  |     |  +- fog_oil
|  |     |  +- fog_oil_simple
|  |     |  +- frankenbrew
|  |     |  +- frankenbrew_small
|  |     |  +- g2saf
|  |     |  +- g2top
|  |     |  +- g2wes
|  |     |  +- gd2gol
|  |     |  +- glassbottles
|  |     |  +- glassbottles2
|  |     |  +- glut
|  |     |  +- gnoll_flesh
|  |     |  +- hag
|  |     |  |  +- caring_moss
|  |     |  |  +- corrosive_moss
|  |     |  |  +- crawling_moss
|  |     |  |  +- creeping_moss
|  |     |  |  +- drowned_moss
|  |     |  |  +- faded_moss
|  |     |  |  +- gilded_moss
|  |     |  |  +- lustrous_moss
|  |     |  |  +- prismatic_moss
|  |     |  |  +- rooted_moss
|  |     |  |  +- stormy_moss
|  |     |  |  +- synth_base
|  |     |  |  +- synth_shiny
|  |     |  |  +- varnish
|  |     |  |  +- wyrd_axe
|  |     |  |  +- wyrd_cross
|  |     |  |  +- wyrd_spear
|  |     |  |  `- wyrd_sword
|  |     |  +- i2gol
|  |     |  +- id2irn
|  |     |  +- jacksberries
|  |     |  +- jacksberriespoison
|  |     |  +- limezig
|  |     |  +- menthaapplezig
|  |     |  +- menthazig
|  |     |  +- moon
|  |     |  +- moon_3x
|  |     |  +- mortar
|  |     |  +- ozium
|  |     |  +- ozium_3x
|  |     |  +- paralytic_venom
|  |     |  +- pestle
|  |     |  +- qsabsolution
|  |     |  +- quicksilver
|  |     |  +- r2dia
|  |     |  +- revival_potion
|  |     |  +- revival_potion_spider
|  |     |  +- s2blo
|  |     |  +- s2coa
|  |     |  +- salt
|  |     |  +- salt_2
|  |     |  +- salviavalerianazig
|  |     |  +- salviazig
|  |     |  +- skysugar
|  |     |  +- skysugarbase
|  |     |  +- st2di2tin
|  |     |  +- strawberryzig
|  |     |  +- t2gem
|  |     |  +- transisdust
|  |     |  +- viscera
|  |     |  +- viscera_3x
|  |     |  +- w2swa
|  |     |  +- w2w
|  |     |  `- ziggara
|  |     +- arcana
|  |     |  +- amethyst
|  |     |  +- arcyne_dagger
|  |     |  +- binding
|  |     |  +- bindingt2
|  |     |  +- bindingt3
|  |     |  +- bindingt4
|  |     |  +- bindingt5
|  |     |  +- blacksteel_upgrade
|  |     |  +- chalk
|  |     |  +- fission_elemental_grand
|  |     |  +- fission_elemental_greater
|  |     |  +- fission_elemental_lesser
|  |     |  +- fission_fae_grand
|  |     |  +- fission_fae_greater
|  |     |  +- fission_fae_lesser
|  |     |  +- fission_infernal_grand
|  |     |  +- fission_infernal_greater
|  |     |  +- fission_infernal_lesser
|  |     |  +- forge
|  |     |  +- fusion_elemental_grand
|  |     |  +- fusion_elemental_greater
|  |     |  +- fusion_elemental_lesser
|  |     |  +- fusion_fae_grand
|  |     |  +- fusion_fae_greater
|  |     |  +- fusion_fae_lesser
|  |     |  +- fusion_infernal_grand
|  |     |  +- fusion_infernal_greater
|  |     |  +- fusion_infernal_lesser
|  |     |  +- infernalfeather
|  |     |  +- meldt1
|  |     |  +- meldt2
|  |     |  +- meldt3
|  |     |  +- meldt4
|  |     |  +- meldt5
|  |     |  +- mimictrinket
|  |     |  +- nomagiccollar
|  |     |  +- nomagicglove
|  |     |  +- nullring
|  |     |  +- pre_arcyne_spellbook
|  |     |  +- runed_artifact_replication
|  |     |  +- sendingstone
|  |     |  +- shimmeringlens
|  |     |  +- staff
|  |     |  |  +- grand_diamond
|  |     |  |  +- grand_riddle
|  |     |  |  +- greater_emerald
|  |     |  |  +- greater_quartz
|  |     |  |  +- greater_ruby
|  |     |  |  +- greater_sapphire
|  |     |  |  +- lesser_amethyst
|  |     |  |  `- lesser_toper
|  |     |  +- temporalhourglass
|  |     |  +- voidlamptern
|  |     |  `- wand
|  |     |     +- grand_diamond
|  |     |     +- grand_riddle
|  |     |     +- greater_emerald
|  |     |     +- greater_quartz
|  |     |     +- greater_ruby
|  |     |     +- greater_sapphire
|  |     |     +- lesser_amethyst
|  |     |     `- lesser_toper
|  |     +- ceramics
|  |     |  +- clay
|  |     |  |  +- claybottle
|  |     |  |  +- claybottleclassic
|  |     |  |  +- claybrick
|  |     |  |  +- claybrick3
|  |     |  |  +- claycup
|  |     |  |  +- claycup3
|  |     |  |  +- claycup3classic3
|  |     |  |  +- claycupclassic
|  |     |  |  +- clayfancyvase
|  |     |  |  +- clayfancyvaseclassic
|  |     |  |  +- claystatue
|  |     |  |  +- clayvase
|  |     |  |  +- clayvaseclassic
|  |     |  |  +- teacup
|  |     |  |  `- teapot
|  |     |  +- glass
|  |     |  |  `- statue
|  |     |  `- glassraw
|  |     +- cooking
|  |     |  +- allspice
|  |     |  +- brothbrique
|  |     |  +- brothbriquealt
|  |     |  +- coppiette
|  |     |  +- dryleaf
|  |     |  +- dryrosa
|  |     |  +- drytea
|  |     |  +- dryweed
|  |     |  +- fish
|  |     |  +- frybirdbucket
|  |     |  +- lemonystickets
|  |     |  +- mobilestove_tallow
|  |     |  +- raisins
|  |     |  +- raisinsblackberry
|  |     |  +- raisinslemon
|  |     |  +- raisinslime
|  |     |  +- raisinspear
|  |     |  +- raisinsplum
|  |     |  +- raisinsraspberry
|  |     |  +- raisinsstrawberry
|  |     |  +- raisinstangerine
|  |     |  +- rocknutdry
|  |     |  +- salami
|  |     |  +- salo
|  |     |  +- salotack
|  |     |  +- sigdry
|  |     |  |  `- cheroot
|  |     |  +- sigsweet
|  |     |  |  `- cheroot
|  |     |  +- spicechocolate
|  |     |  +- spicecoffee
|  |     |  +- spicerosa
|  |     |  +- spicetea
|  |     |  +- sugarblackberry
|  |     |  +- sugarrocknut
|  |     |  +- sugarrocknutalt
|  |     |  +- sugarshapedarch
|  |     |  +- sugarshapedarchway
|  |     |  +- sugarshapedcastle
|  |     |  +- sugarshapedflag
|  |     |  +- sugarshapedhouse
|  |     |  +- sugarshapedmarka
|  |     |  +- sugarshapedmarkd
|  |     |  +- sugarshapedmarkh
|  |     |  +- sugarshapedmarkp
|  |     |  +- sugarshapedmarks
|  |     |  +- sugarshapedmarkz
|  |     |  +- sugarshapedstatuek
|  |     |  +- sugarshapedstatuel
|  |     |  +- sugarshapedstatuer
|  |     |  +- sugarshapedstatuey
|  |     |  +- sugarshapedtower
|  |     |  +- sugarshapedtowers
|  |     |  +- sugarshapedtree
|  |     |  +- sugartangerine
|  |     |  `- trailmix
|  |     +- engineering
|  |     |  +- activator
|  |     |  +- art_table
|  |     |  +- bars
|  |     |  +- bombtrap
|  |     |  +- cog
|  |     |  +- coolingtable
|  |     |  +- crossbow
|  |     |  +- distiller
|  |     |  +- flametrap
|  |     |  +- floorgrille
|  |     |  +- freedomchair
|  |     |  +- gate
|  |     |  +- gearbox
|  |     |  +- heavyboltsmajor
|  |     |  +- heavyboltsmajorblunt
|  |     |  +- heavyboltsmajorbronze
|  |     |  +- heavyboltsminor
|  |     |  +- heavyboltsminorblunt
|  |     |  +- heavyboltsminorbronze
|  |     |  +- heavycrossbow
|  |     |  +- impactblindingsmoke
|  |     |  +- impactexplosive
|  |     |  +- impactfiresmoke
|  |     |  +- impacthealingsmoke
|  |     |  +- impactmutesmoke
|  |     |  +- impactpoisonsmoke
|  |     |  +- impactsmoke
|  |     |  +- infernalengine
|  |     |  +- large_cog
|  |     |  +- lever
|  |     |  +- minecart
|  |     |  +- poisonarrow_five
|  |     |  +- poisonarrow_ten
|  |     |  +- poisonbolt_five
|  |     |  +- polishbrush
|  |     |  +- polishcream
|  |     |  +- potionseller
|  |     |  +- pressure_plate
|  |     |  +- pyrobolt
|  |     |  +- pyrobolt_five
|  |     |  +- railbreak
|  |     |  +- rails
|  |     |  +- rocktrap
|  |     |  +- roller
|  |     |  +- satchelbomb
|  |     |  +- sawbladetrap
|  |     |  +- shaft
|  |     |  +- shocktrap
|  |     |  +- shopbars
|  |     |  +- shutters
|  |     |  +- smither
|  |     |  +- stickshaft
|  |     |  +- tntbomb
|  |     |  +- trapdoor
|  |     |  +- twentybolts
|  |     |  +- twentyboltsbronze
|  |     |  +- vertical_gearbox
|  |     |  `- waterwheel
|  |     +- farming
|  |     |  `- fertilizer
|  |     +- fleshcrafting
|  |     |  +- black_rose
|  |     |  +- decoy
|  |     |  +- decoy_alt
|  |     |  +- eyes
|  |     |  +- flesh_node
|  |     |  +- heart
|  |     |  +- imperfect_gnoll
|  |     |  +- imperfect_gnoll_alt
|  |     |  +- leechbait
|  |     |  +- leechbaitcloth
|  |     |  +- liver
|  |     |  +- lungs
|  |     |  `- tongue
|  |     +- gemcarving
|  |     |  +- amber
|  |     |  |  +- amulet
|  |     |  |  +- beaver
|  |     |  |  +- bowl
|  |     |  |  +- bracelet
|  |     |  |  +- bust
|  |     |  |  +- cameo
|  |     |  |  +- circlet
|  |     |  |  +- comb
|  |     |  |  +- cup
|  |     |  |  +- duck
|  |     |  |  +- fancycup
|  |     |  |  +- fancyvase
|  |     |  |  +- figurine
|  |     |  |  +- fish
|  |     |  |  +- fork
|  |     |  |  +- mask
|  |     |  |  +- obelisk
|  |     |  |  +- platter
|  |     |  |  +- ring
|  |     |  |  +- spoon
|  |     |  |  +- statue
|  |     |  |  +- sun
|  |     |  |  +- tablet
|  |     |  |  +- teapot
|  |     |  |  +- urn
|  |     |  |  `- vase
|  |     |  +- coral
|  |     |  |  +- amulet
|  |     |  |  +- bowl
|  |     |  |  +- bracelet
|  |     |  |  +- bust
|  |     |  |  +- cameo
|  |     |  |  +- circlet
|  |     |  |  +- comb
|  |     |  |  +- cup
|  |     |  |  +- duck
|  |     |  |  +- fancycup
|  |     |  |  +- fancyvase
|  |     |  |  +- figurine
|  |     |  |  +- fish
|  |     |  |  +- fork
|  |     |  |  +- jaw
|  |     |  |  +- mask
|  |     |  |  +- obelisk
|  |     |  |  +- platter
|  |     |  |  +- ring
|  |     |  |  +- shark
|  |     |  |  +- spoon
|  |     |  |  +- statue
|  |     |  |  +- tablet
|  |     |  |  +- teapot
|  |     |  |  +- urn
|  |     |  |  `- vase
|  |     |  +- jade
|  |     |  |  +- bracelet
|  |     |  |  +- bust
|  |     |  |  +- circlet
|  |     |  |  +- comb
|  |     |  |  +- duck
|  |     |  |  +- fancycup
|  |     |  |  +- fancyvase
|  |     |  |  +- fish
|  |     |  |  +- kukri
|  |     |  |  +- mask
|  |     |  |  +- obelisk
|  |     |  |  +- statue
|  |     |  |  +- tablet
|  |     |  |  +- teapot
|  |     |  |  +- urn
|  |     |  |  `- wyrm
|  |     |  +- jadeamulet
|  |     |  +- jadebowl
|  |     |  +- jadecameo
|  |     |  +- jadecup
|  |     |  +- jadefigurine
|  |     |  +- jadefork
|  |     |  +- jadeplatter
|  |     |  +- jadering
|  |     |  +- jadespoon
|  |     |  +- jadevase
|  |     |  +- onyxa
|  |     |  |  +- amulet
|  |     |  |  +- bowl
|  |     |  |  +- bracelet
|  |     |  |  +- bust
|  |     |  |  +- cameo
|  |     |  |  +- circlet
|  |     |  |  +- comb
|  |     |  |  +- cup
|  |     |  |  +- duck
|  |     |  |  +- fancycup
|  |     |  |  +- fancyvase
|  |     |  |  +- figurine
|  |     |  |  +- fish
|  |     |  |  +- fork
|  |     |  |  +- mask
|  |     |  |  +- obelisk
|  |     |  |  +- platter
|  |     |  |  +- ring
|  |     |  |  +- snake
|  |     |  |  +- spider
|  |     |  |  +- spoon
|  |     |  |  +- statue
|  |     |  |  +- tablet
|  |     |  |  +- teapot
|  |     |  |  +- urn
|  |     |  |  `- vase
|  |     |  +- opal
|  |     |  |  +- amulet
|  |     |  |  +- bowl
|  |     |  |  +- bracelet
|  |     |  |  +- bust
|  |     |  |  +- cameo
|  |     |  |  +- circlet
|  |     |  |  +- comb
|  |     |  |  +- crab
|  |     |  |  +- cup
|  |     |  |  +- duck
|  |     |  |  +- fancycup
|  |     |  |  +- fancyvase
|  |     |  |  +- figurine
|  |     |  |  +- fish
|  |     |  |  +- fork
|  |     |  |  +- knife
|  |     |  |  +- mask
|  |     |  |  +- obelisk
|  |     |  |  +- platter
|  |     |  |  +- ring
|  |     |  |  +- spoon
|  |     |  |  +- statue
|  |     |  |  +- tablet
|  |     |  |  +- teapot
|  |     |  |  +- urn
|  |     |  |  `- vase
|  |     |  +- rose
|  |     |  |  +- amulet
|  |     |  |  +- bowl
|  |     |  |  +- bracelet
|  |     |  |  +- bust
|  |     |  |  +- cameo
|  |     |  |  +- carp
|  |     |  |  +- circlet
|  |     |  |  +- comb
|  |     |  |  +- cup
|  |     |  |  +- duck
|  |     |  |  +- fancycup
|  |     |  |  +- fancyvase
|  |     |  |  +- figurine
|  |     |  |  +- fish
|  |     |  |  +- flower
|  |     |  |  +- fork
|  |     |  |  +- mask
|  |     |  |  +- obelisk
|  |     |  |  +- platter
|  |     |  |  +- ring
|  |     |  |  +- spoon
|  |     |  |  +- statue
|  |     |  |  +- tablet
|  |     |  |  +- teapot
|  |     |  |  +- urn
|  |     |  |  `- vase
|  |     |  +- shell
|  |     |  |  +- amulet
|  |     |  |  +- bowl
|  |     |  |  +- bracelet
|  |     |  |  +- bust
|  |     |  |  +- cameo
|  |     |  |  +- circlet
|  |     |  |  +- comb
|  |     |  |  +- cup
|  |     |  |  +- duck
|  |     |  |  +- fancycup
|  |     |  |  +- fancyvase
|  |     |  |  +- figurine
|  |     |  |  +- fish
|  |     |  |  +- fork
|  |     |  |  +- mask
|  |     |  |  +- obelisk
|  |     |  |  +- openclam
|  |     |  |  +- platter
|  |     |  |  +- rawshell
|  |     |  |  +- ring
|  |     |  |  +- rungu
|  |     |  |  +- spoon
|  |     |  |  +- statue
|  |     |  |  +- tablet
|  |     |  |  +- teapot
|  |     |  |  +- turtle
|  |     |  |  +- urn
|  |     |  |  `- vase
|  |     |  `- turq
|  |     |     +- amulet
|  |     |     +- bowl
|  |     |     +- bracelet
|  |     |     +- bust
|  |     |     +- cameo
|  |     |     +- circlet
|  |     |     +- comb
|  |     |     +- cup
|  |     |     +- duck
|  |     |     +- fancycup
|  |     |     +- fancyvase
|  |     |     +- figurine
|  |     |     +- fish
|  |     |     +- fork
|  |     |     +- ka
|  |     |     +- mask
|  |     |     +- obelisk
|  |     |     +- platter
|  |     |     +- ring
|  |     |     +- scarab
|  |     |     +- spoon
|  |     |     +- statue
|  |     |     +- tablet
|  |     |     +- urn
|  |     |     `- vase
|  |     +- gravemarker
|  |     +- leather
|  |     |  +- apron
|  |     |  |  `- blacksmith
|  |     |  +- armor
|  |     |  |  +- armor
|  |     |  |  +- bracers
|  |     |  |  +- cuirass
|  |     |  |  +- freivest
|  |     |  |  +- heavy_leather_armor
|  |     |  |  |  +- coat
|  |     |  |  |  |  `- tailcoat
|  |     |  |  |  `- jacket
|  |     |  |  +- heavy_leather_pants
|  |     |  |  |  `- shorts
|  |     |  |  +- heavybracers
|  |     |  |  +- helmet
|  |     |  |  |  `- advanced
|  |     |  |  +- hidearmor
|  |     |  |  +- lgorget
|  |     |  |  +- pants
|  |     |  |  +- saigahelm
|  |     |  |  +- volfhelm
|  |     |  |  `- volfmantle
|  |     |  +- bandana
|  |     |  +- bearcloak
|  |     |  +- bedroll
|  |     |  +- belt
|  |     |  +- bikini
|  |     |  +- cloak
|  |     |  +- cloakfur
|  |     |  +- container
|  |     |  |  +- backpack
|  |     |  |  +- bandolier
|  |     |  |  +- belt
|  |     |  |  |  +- black
|  |     |  |  |  +- double
|  |     |  |  |  +- knifebelt
|  |     |  |  |  `- surgicalbag
|  |     |  |  +- boltpouch
|  |     |  |  +- grenstrap
|  |     |  |  +- gwstrap
|  |     |  |  +- heavyboltpouch
|  |     |  |  +- javelinbag
|  |     |  |  +- magepouch
|  |     |  |  +- meatbag
|  |     |  |  +- pouch
|  |     |  |  +- quiver
|  |     |  |  +- satchel
|  |     |  |  +- satchelshort
|  |     |  |  +- scabbard
|  |     |  |  |  +- dagger
|  |     |  |  |  `- sword
|  |     |  |  +- twstrap
|  |     |  |  `- waterskin
|  |     |  +- corset
|  |     |  +- darkcloak
|  |     |  +- doctormask
|  |     |  +- doublepeltbedsheet
|  |     |  +- drum
|  |     |  +- fingerless_leather_gloves
|  |     |  +- footwear
|  |     |  |  +- boots
|  |     |  |  |  +- dark
|  |     |  |  |  +- furlinedboots
|  |     |  |  |  +- noble
|  |     |  |  |  `- short
|  |     |  |  +- boots_heavy
|  |     |  |  +- boots_heavy_b
|  |     |  |  `- shoes
|  |     |  +- gloves
|  |     |  +- heavygloves
|  |     |  +- hidebikini
|  |     |  +- leathertights
|  |     |  +- lightbearcloak
|  |     |  +- papakha
|  |     |  +- peltbedsheet
|  |     |  +- reinforcement
|  |     |  |  +- crafteast
|  |     |  |  `- studded
|  |     |  |     +- bikini
|  |     |  |     +- chestplate
|  |     |  |     +- cuirbouilli
|  |     |  |     +- forester
|  |     |  |     `- hood
|  |     |  +- saddle
|  |     |  +- sanguinecoat
|  |     |  +- sanguinegloves
|  |     |  +- sanguineheels
|  |     |  +- sanguinejacket
|  |     |  +- sanguineshoes
|  |     |  +- sanguinesleeves
|  |     |  +- skillbook
|  |     |  +- tricorn
|  |     |  +- unique
|  |     |  |  +- artipants
|  |     |  |  +- baggyleatherpants
|  |     |  |  +- buckleshoes
|  |     |  |  +- fencingbreeches
|  |     |  |  +- furlinedjacket
|  |     |  |  +- grenzelboots
|  |     |  |  +- grenzelgloves
|  |     |  |  +- gronnboots
|  |     |  |  +- gronngloves
|  |     |  |  +- gronnpants
|  |     |  |  +- monkleather
|  |     |  |  +- monkrobes
|  |     |  |  +- openrobes
|  |     |  |  +- otavanboots
|  |     |  |  +- otavanleathergloves
|  |     |  |  +- otavanleatherpants
|  |     |  |  `- winterjacket
|  |     |  +- vest
|  |     |  |  `- sailor
|  |     |  `- whip
|  |     +- leatherunique
|  |     |  `- gladsandals
|  |     +- roguebin
|  |     +- sewing
|  |     |  +- abyssor
|  |     |  +- abyssortemplar
|  |     |  +- allwrappings
|  |     |  +- anklets
|  |     |  +- apothpants
|  |     |  +- apothshirt
|  |     |  +- apron
|  |     |  |  +- blacksmith
|  |     |  |  `- cook
|  |     |  +- apron_waist
|  |     |  +- archer
|  |     |  +- archivist
|  |     |  +- armingcap
|  |     |  +- armingjacket
|  |     |  +- armordress
|  |     |  +- articap
|  |     |  +- artificer
|  |     |  +- astrata
|  |     |  +- astratahoodstonekeep
|  |     |  +- astratahoodstonekeepalt
|  |     |  +- astratahoodstonekeeptri
|  |     |  +- astratahoodstonekeeptrialt
|  |     |  +- astratatemplar
|  |     |  +- athletic_leotard
|  |     |  +- bandage
|  |     |  +- bandithood
|  |     |  +- bardhat
|  |     |  +- barding
|  |     |  |  `- fogbeast
|  |     |  +- bardress
|  |     |  +- basichood
|  |     |  +- battlenun
|  |     |  +- battleskirt
|  |     |  +- beekeeper
|  |     |  +- bikini
|  |     |  +- braies
|  |     |  +- breechclothbelt
|  |     |  +- breechclothbeltalt
|  |     |  +- breechclothbeltaltimprovised
|  |     |  +- breechclothbeltimprovised
|  |     |  +- brimmed
|  |     |  +- brownloincloth
|  |     |  +- bucklehat
|  |     |  +- burial_shroud
|  |     |  +- buttonedlongcoat
|  |     |  +- caparison
|  |     |  |  +- astrata
|  |     |  |  +- eora
|  |     |  |  +- fogbeast
|  |     |  |  `- psy
|  |     |  +- cape
|  |     |  |  +- desert
|  |     |  |  +- half
|  |     |  |  `- rider
|  |     |  +- chaperon
|  |     |  |  `- noble
|  |     |  +- clothbedsheet
|  |     |  +- clothblindfold
|  |     |  +- clothgloves
|  |     |  +- clothknapsack
|  |     |  +- clothpouch
|  |     |  +- clothshirt
|  |     |  +- clothtrou
|  |     |  +- coif
|  |     |  +- cotehardie
|  |     |  +- dendor
|  |     |  +- desert_skirt
|  |     |  +- desertbra
|  |     |  +- doublefabricbedsheet
|  |     |  +- duelist
|  |     |  +- duelmask
|  |     |  +- eora
|  |     |  +- eoratemplar
|  |     |  +- exoticcarpet
|  |     |  +- fabricbedsheet
|  |     |  +- fancyhat
|  |     |  +- fauldedbelt
|  |     |  +- fineparasol
|  |     |  +- formalbreeches
|  |     |  +- formalshirt
|  |     |  +- formalsilkjacket
|  |     |  +- formalsilks
|  |     |  +- formaltrousers
|  |     |  +- furovercoat
|  |     |  +- gambeson
|  |     |  +- gbandages
|  |     |  +- gerkit
|  |     |  +- grenzelblack
|  |     |  |  `- triumph
|  |     |  +- grenzelhelm
|  |     |  |  +- off
|  |     |  |  `- triumph
|  |     |  |     `- off
|  |     |  +- grenzelklapper
|  |     |  |  +- off
|  |     |  |  `- triumph
|  |     |  |     `- off
|  |     |  +- guildedjacket
|  |     |  +- gweightedbandages
|  |     |  +- gweightedbandagesalt
|  |     |  +- harmingjacket
|  |     |  +- hatfur
|  |     |  +- headband
|  |     |  +- heavyhood
|  |     |  +- heavypadded
|  |     |  +- hgambeson
|  |     |  |  `- fencer
|  |     |  +- hijab
|  |     |  +- hoodfeld
|  |     |  +- hoodphys
|  |     |  +- hoodwhite
|  |     |  +- hunterheadband
|  |     |  +- jesterchest
|  |     |  +- jesterhead
|  |     |  +- jestershoes
|  |     |  +- jupon
|  |     |  +- jupon_short
|  |     |  +- keffiyeh
|  |     |  +- knitcap
|  |     |  +- ladycloak
|  |     |  +- leotard
|  |     |  +- Leyepatch
|  |     |  +- lgambeson
|  |     |  +- linedanklet
|  |     |  +- loincloth
|  |     |  +- longcoat
|  |     |  +- lordlycloak
|  |     |  +- lowcut_shirt
|  |     |  +- maidapron
|  |     |  +- maidband
|  |     |  +- maiddress
|  |     |  +- maidhead
|  |     |  +- maidsash
|  |     |  +- malum
|  |     |  +- malumtemplar
|  |     |  +- monkheadband
|  |     |  +- monkwraps
|  |     |  +- necra
|  |     |  +- necramask
|  |     |  +- necratemplar
|  |     |  +- nemes
|  |     |  +- noblecoat
|  |     |  +- noc
|  |     |  +- nocwrappings
|  |     |  +- nunhabit
|  |     |  +- nunveil
|  |     |  +- nurseveil
|  |     |  +- paddedcap
|  |     |  +- paddedcoif
|  |     |  +- panties
|  |     |  +- paperparasol
|  |     |  +- peasantcap
|  |     |  +- pestra
|  |     |  +- pestratemplar
|  |     |  +- poncho
|  |     |  +- psydon
|  |     |  +- puritanhat
|  |     |  +- ragmask
|  |     |  +- rags
|  |     |  +- ravox
|  |     |  +- ravoxgorget
|  |     |  +- ravoxtemplar
|  |     |  +- regalrobes
|  |     |  +- Reyepatch
|  |     |  +- robe
|  |     |  +- royaldress
|  |     |  +- royalgown
|  |     |  +- royalshirt
|  |     |  +- royalsleeves
|  |     |  +- sack
|  |     |  +- sailorspants
|  |     |  +- sanguineblouse
|  |     |  +- sanguinecap
|  |     |  +- sanguinehat
|  |     |  +- sanguineskirt
|  |     |  +- sanguinetrousers
|  |     |  +- sanguinevest
|  |     |  +- servantdress
|  |     |  +- sexydress
|  |     |  +- shadowpants
|  |     |  +- shadowshirt
|  |     |  +- shawl
|  |     |  +- silkbelt
|  |     |  +- silkbra
|  |     |  +- silkdress
|  |     |  +- silkmask
|  |     |  +- silktunic
|  |     |  +- silkydress
|  |     |  +- skirt
|  |     |  +- sleevelessrobefeld
|  |     |  +- sleevelessrobephys
|  |     |  +- sleevelessrobewhite
|  |     |  +- slitdress
|  |     |  +- spellsingerhat
|  |     |  +- spellsingerrobes
|  |     |  +- stabard
|  |     |  |  +- bog
|  |     |  |  +- guard
|  |     |  |  `- guardhood
|  |     |  +- stabardheavy
|  |     |  +- standardcarpet
|  |     |  +- stockdress
|  |     |  +- stockings_knee_silk_white
|  |     |  +- stockings_knee_white
|  |     |  +- stockings_thigh_silk_white
|  |     |  +- stockings_thigh_white
|  |     |  +- stockings_white
|  |     |  +- stockings_white_fishnet
|  |     |  +- stockings_white_silk
|  |     |  +- strapless_dress
|  |     |  +- strapless_dress_alt
|  |     |  +- strawhat
|  |     |  +- surcoatblacksteel
|  |     |  +- surcoatgold
|  |     |  +- surcoatgoldast
|  |     |  +- surcoatgoldlegacy
|  |     |  +- surcoatgolduni
|  |     |  +- surcoatsilver
|  |     |  +- surcoatsilverast
|  |     |  +- surcoatsilverlegacy
|  |     |  +- surcoatsilveruni
|  |     |  +- tabard
|  |     |  +- tailor
|  |     |  |  +- desertgown
|  |     |  |  +- grenzelhat
|  |     |  |  +- grenzelpants
|  |     |  |  +- grenzelshirt
|  |     |  |  +- halfrobe
|  |     |  |  +- hgambeson
|  |     |  |  |  `- fencer
|  |     |  |  +- monkrobe
|  |     |  |  +- naledisash
|  |     |  |  `- otavangambeson
|  |     |  +- tentkit
|  |     |  +- tights
|  |     |  +- trousershorts
|  |     |  +- tunic
|  |     |  +- undervestments
|  |     |  +- undies
|  |     |  +- undies_eoran
|  |     |  +- weaving
|  |     |  |  +- fallgown
|  |     |  |  +- springgown
|  |     |  |  +- summergown
|  |     |  |  `- wintergown
|  |     |  +- weddingdress
|  |     |  +- winterdress
|  |     |  +- witchhat
|  |     |  +- wizhatblack
|  |     |  +- wizhatblue
|  |     |  +- wizhatgreen
|  |     |  +- wizhatred
|  |     |  +- wizhatyellow
|  |     |  +- woolencollar
|  |     |  +- workervest
|  |     |  +- wrappings
|  |     |  +- xylix
|  |     |  +- xylixian
|  |     |  `- yurtkit
|  |     +- structure
|  |     |  +- alch
|  |     |  +- altcouchleft
|  |     |  +- altcouchright
|  |     |  +- anvil
|  |     |  |  `- bronze
|  |     |  +- apiary
|  |     |  +- ascendant
|  |     |  +- baotha_cross_meat
|  |     |  +- baotha_cross_stone
|  |     |  +- barrel
|  |     |  +- bearrug
|  |     |  +- bed
|  |     |  +- blackcouchleft
|  |     |  +- blackcouchright
|  |     |  +- blackpillows
|  |     |  +- bluepillows
|  |     |  +- bobcatrug
|  |     |  +- booth
|  |     |  +- booth02
|  |     |  +- booth_green
|  |     |  +- booth_green_02
|  |     |  +- border
|  |     |  +- bordercorner
|  |     |  +- brazier
|  |     |  +- brownpillows
|  |     |  +- campfire
|  |     |  +- cauldronalchemy
|  |     |  +- ceramicswheel
|  |     |  +- ceramicswheelalt
|  |     |  +- chair
|  |     |  +- chairthrone
|  |     |  +- chest
|  |     |  +- closet
|  |     |  +- coffin
|  |     |  +- composter
|  |     |  +- cookpit
|  |     |  +- couchleft
|  |     |  +- couchright
|  |     |  +- curtain
|  |     |  +- curtainblack
|  |     |  +- curtainblue
|  |     |  +- curtainbrown
|  |     |  +- curtaingreen
|  |     |  +- curtainmagenta
|  |     |  +- curtainpurple
|  |     |  +- curtainred
|  |     |  +- densefire
|  |     |  +- display_booth01
|  |     |  +- display_booth02
|  |     |  +- display_stand
|  |     |  +- door
|  |     |  +- doorbolt
|  |     |  +- doublebed
|  |     |  +- dummy
|  |     |  +- dyestation
|  |     |  +- fancychair
|  |     |  +- fancydoor
|  |     |  +- fancymirror
|  |     |  +- fancytableblack
|  |     |  +- fancytableblue
|  |     |  +- fancytablecyan
|  |     |  +- fancytablegreen
|  |     |  +- fancytableorange
|  |     |  +- fancytablepurple
|  |     |  +- fancytablered
|  |     |  +- fancytableroyalblack
|  |     |  +- fancytableroyalblue
|  |     |  +- fence
|  |     |  +- fencealt
|  |     |  +- finestonetable
|  |     |  +- fireplace
|  |     |  +- forge
|  |     |  +- foxrug
|  |     |  +- graggar_cross_meat
|  |     |  +- graggar_cross_stone
|  |     |  +- greatsmelter
|  |     |  +- greenpillows
|  |     |  +- handcart
|  |     |  +- headstake
|  |     |  +- largetable
|  |     |  +- littlebanners
|  |     |  |  +- bluered
|  |     |  |  +- bluewhite
|  |     |  |  +- greenblue
|  |     |  |  +- greenred
|  |     |  |  `- greenwhite
|  |     |  +- longtable
|  |     |  +- longtablealt
|  |     |  +- loom
|  |     |  +- magentacouchleft
|  |     |  +- magentacouchright
|  |     |  +- magentapillows
|  |     |  +- mannequin_female
|  |     |  +- mannequin_male
|  |     |  +- matthios_cross_meat
|  |     |  +- matthios_cross_stone
|  |     |  +- meathook
|  |     |  +- millstone
|  |     |  +- mirror
|  |     |  +- noose
|  |     |  +- operatingtable
|  |     |  +- oven
|  |     |  +- parkbenchleft
|  |     |  +- parkbenchmiddle
|  |     |  +- parkbenchright
|  |     |  +- pillory
|  |     |  +- plough
|  |     |  +- psycrss
|  |     |  +- psycruci
|  |     |  +- purplepillows
|  |     |  +- rack
|  |     |  +- railing
|  |     |  +- rcom
|  |     |  +- redpillows
|  |     |  +- sharpwheel
|  |     |  +- sign
|  |     |  +- silverpsycruci
|  |     |  +- sleepcoffin
|  |     |  +- smelter
|  |     |  +- smelterbronze
|  |     |  +- smelterhiron
|  |     |  +- spike_pit
|  |     |  +- stairs
|  |     |  +- stairsd
|  |     |  +- standing
|  |     |  +- standingblue
|  |     |  +- statue
|  |     |  +- stonedoor
|  |     |  +- stonelantern
|  |     |  +- stonelanternstanding
|  |     |  +- stonenecrapsycrss
|  |     |  +- stonenecrapsycrsscloth
|  |     |  +- stonepsycrss
|  |     |  +- stonepsycruci
|  |     |  +- stonestairsd
|  |     |  +- stonetable
|  |     |  +- stonewalldeco
|  |     |  +- stool
|  |     |  +- strawbed
|  |     |  +- swing_door
|  |     |  +- table
|  |     |  +- tanningrack
|  |     |  +- torchholder
|  |     |  +- ultimacouchleft
|  |     |  +- ultimacouchright
|  |     |  +- wallcandle
|  |     |  +- wallcandleblue
|  |     |  +- wallladder
|  |     |  +- wicker
|  |     |  +- wonder
|  |     |  |  +- first
|  |     |  |  +- fourth
|  |     |  |  +- second
|  |     |  |  `- third
|  |     |  +- woolbed
|  |     |  +- wooldoublebed
|  |     |  +- zizo_cross_gold
|  |     |  +- zizo_cross_stone
|  |     |  `- zizo_shrine
|  |     +- survival
|  |     |  +- abyssoramulet
|  |     |  +- ancientmailledhauberk
|  |     |  |  `- off
|  |     |  +- antlerhood
|  |     |  +- autumnwoadarmor
|  |     |  +- autumnwoadhelmet
|  |     |  +- bag
|  |     |  +- bait
|  |     |  +- bandage
|  |     |  +- bell_collar
|  |     |  +- billhook
|  |     |  +- blcktankard
|  |     |  +- blessedbolt
|  |     |  +- bloodbait
|  |     |  +- bluntarrow
|  |     |  +- bluntarrow_five
|  |     |  +- boat
|  |     |  +- boneaxe
|  |     |  +- bonespear
|  |     |  +- book_crafting_kit
|  |     |  +- bouquet_calendula
|  |     |  +- bouquet_matricaria
|  |     |  +- bouquet_rosa
|  |     |  +- bouquet_salvia
|  |     |  +- bow
|  |     |  +- bowpartial
|  |     |  +- bowstring
|  |     |  +- bpearlcross
|  |     |  +- briarthorns
|  |     |  +- broom
|  |     |  +- candle
|  |     |  |  `- eora
|  |     |  +- cheele
|  |     |  +- cloth
|  |     |  +- clothbelt
|  |     |  +- clothsash
|  |     |  +- collar
|  |     |  +- d10
|  |     |  +- d12
|  |     |  +- d20
|  |     |  +- d4
|  |     |  +- d6
|  |     |  +- d8
|  |     |  +- dye_brush
|  |     |  +- feldcollar
|  |     |  +- fire_pot
|  |     |  +- fishingcage
|  |     |  +- flint
|  |     |  +- flowercrown_briar
|  |     |  +- flowercrown_calendula
|  |     |  +- flowercrown_manabloom
|  |     |  +- flowercrown_matricaria
|  |     |  +- flowercrown_rosa
|  |     |  +- flowercrown_salvia
|  |     |  +- fork
|  |     |  +- goedendag
|  |     |  +- goodluckcharm
|  |     |  +- handmirror
|  |     |  +- heatershield
|  |     |  +- heavy_sling_bullet
|  |     |  +- improvisedclamp
|  |     |  +- improvisedhemo
|  |     |  +- improvisedsaw
|  |     |  +- iron_slingbullets
|  |     |  +- ironmailledhauberk
|  |     |  |  `- off
|  |     |  +- longbow
|  |     |  +- longbow_warden
|  |     |  +- longbowpartial
|  |     |  +- lumberjacking
|  |     |  |  +- cart_upgrade
|  |     |  |  `- cart_upgrade2
|  |     |  +- mailledhauberk
|  |     |  |  `- off
|  |     |  +- net
|  |     |  +- oar
|  |     |  +- paperscroll
|  |     |  +- pearlcross
|  |     |  +- peasantry
|  |     |  |  +- goedendag
|  |     |  |  +- hoe
|  |     |  |  |  `- whetstone
|  |     |  |  +- maciejowski_knife
|  |     |  |  +- maciejowski_messer
|  |     |  |  +- peasantwarflail
|  |     |  |  +- pitchfork
|  |     |  |  |  `- whetstone
|  |     |  |  +- scythe
|  |     |  |  +- shovel
|  |     |  |  |  `- whetstone
|  |     |  |  +- thresher
|  |     |  |  |  `- whetstone
|  |     |  |  +- waraxe
|  |     |  |  |  `- silver
|  |     |  |  |     `- preblessed
|  |     |  |  +- warflail
|  |     |  |  +- warpick
|  |     |  |  +- warpick_steel
|  |     |  |  +- warspear_hoe
|  |     |  |  `- warspear_pitchfork
|  |     |  +- peppermill
|  |     |  +- pipe
|  |     |  +- platter
|  |     |  +- poisonarrow
|  |     |  +- poisonarrow_five
|  |     |  +- poisonarrow_five_stone
|  |     |  +- poisonarrow_stone
|  |     |  +- pot
|  |     |  +- prosthetic
|  |     |  |  +- woodleftarm
|  |     |  |  +- woodleftleft
|  |     |  |  +- woodrightarm
|  |     |  |  `- woodrightleg
|  |     |  +- purify_lux
|  |     |  +- purify_lux_vials
|  |     |  +- quarterstaff
|  |     |  +- quarterstaff_iron
|  |     |  +- quarterstaff_psydonic
|  |     |  |  `- bullion
|  |     |  +- quarterstaff_silver
|  |     |  +- quarterstaff_steel
|  |     |  +- ration_wrapper
|  |     |  +- recurvebow
|  |     |  +- recurvepartial
|  |     |  +- repairkitcloth
|  |     |  +- repairkitclothbad
|  |     |  +- repairkitmetalingot
|  |     |  +- repairkitmetalscrap
|  |     |  +- rod
|  |     |  +- rollingpin
|  |     |  +- rope
|  |     |  +- ropebelt
|  |     |  +- rucksack
|  |     |  |  `- crafted
|  |     |  +- runicflask
|  |     |  +- sbait
|  |     |  +- sbaita
|  |     |  +- sharpenedstake
|  |     |  +- shellbracelet
|  |     |  +- shellnecklace
|  |     |  +- shillelagh
|  |     |  +- silvtankard
|  |     |  +- skullmask
|  |     |  +- slingcraft
|  |     |  +- slingpouchcraft
|  |     |  +- soap
|  |     |  +- spoon
|  |     |  +- steel_scattershot
|  |     |  +- stonearrow
|  |     |  +- stonearrow_five
|  |     |  +- stoneaxe
|  |     |  +- stonebullets
|  |     |  +- stonebullets10x
|  |     |  +- stonehammer
|  |     |  +- stonehoe
|  |     |  +- stoneknife
|  |     |  +- stonepick
|  |     |  +- stonespear
|  |     |  +- stonesword
|  |     |  +- stonetongs
|  |     |  +- strucrepairkit
|  |     |  +- surgcollar
|  |     |  +- tarot_deck
|  |     |  +- tneedle
|  |     |  +- torch
|  |     |  +- tribalrags
|  |     |  +- unclothbelt
|  |     |  +- unropebelt
|  |     |  +- waterarrow_ten
|  |     |  +- waterarrow_twenty
|  |     |  +- waterbolt_ten
|  |     |  +- waterbolt_twenty
|  |     |  +- whetstone
|  |     |  +- wickercloak
|  |     |  +- wood_dagger
|  |     |  +- wood_stake
|  |     |  +- woodbowl
|  |     |  +- woodbucket
|  |     |  +- woodclub
|  |     |  +- woodcross
|  |     |  +- woodcup
|  |     |  +- woodhammer
|  |     |  +- woodshield
|  |     |  +- woodspade
|  |     |  +- woodstaff
|  |     |  +- woodsword
|  |     |  +- woodtankard
|  |     |  `- woodtray
|  |     +- tallow
|  |     |  +- campfire_tallow
|  |     |  `- hearth_tallow
|  |     +- trapmaking
|  |     |  +- bombtrap
|  |     |  +- flametrap
|  |     |  +- mantrap
|  |     |  +- mantrapscrap
|  |     |  +- rocktrap
|  |     |  +- sawbladetrap
|  |     |  `- shocktrap
|  |     +- turfs
|  |     |  +- brick
|  |     |  |  +- floor
|  |     |  |  +- wall
|  |     |  |  `- window
|  |     |  |     `- openclose
|  |     |  +- carpet
|  |     |  |  +- purple
|  |     |  |  +- red
|  |     |  |  +- royalblack
|  |     |  |  `- stellar
|  |     |  +- fancywindow
|  |     |  |  `- openclose
|  |     |  +- hay
|  |     |  +- reinforcedwindow
|  |     |  |  `- openclose
|  |     |  +- roguewindow
|  |     |  |  +- dynamic
|  |     |  |  +- reinforced
|  |     |  |  `- stone
|  |     |  +- stone
|  |     |  |  +- block
|  |     |  |  +- brick
|  |     |  |  +- cobble
|  |     |  |  +- cobblerock
|  |     |  |  +- craft
|  |     |  |  +- decorated
|  |     |  |  +- herringbone
|  |     |  |  +- hexstone
|  |     |  |  +- newstone
|  |     |  |  +- platform
|  |     |  |  +- redstone
|  |     |  |  +- tinyredstone
|  |     |  |  +- wall
|  |     |  |  `- window
|  |     |  +- tentdoor
|  |     |  +- tentwall
|  |     |  +- twig
|  |     |  +- twigplatform
|  |     |  `- wood
|  |     |     +- fancy
|  |     |     +- floor
|  |     |     +- floorhl
|  |     |     +- floorhs
|  |     |     +- floorhw
|  |     |     +- floorslanted
|  |     |     +- murderhole
|  |     |     |  `- alt
|  |     |     +- platform
|  |     |     `- wall
|  |     |        `- alt
|  |     +- weaving
|  |     |  +- abyssorhood
|  |     |  +- abyssorrobe
|  |     |  +- astratahood
|  |     |  +- astratarobe
|  |     |  +- cloak
|  |     |  +- dendorrobe
|  |     |  +- eorahood
|  |     |  +- eoramask
|  |     |  +- eorarobes
|  |     |  +- innkeeper
|  |     |  +- necrahood
|  |     |  +- necrarobe
|  |     |  +- nochood
|  |     |  +- nocrobe
|  |     |  +- puritan
|  |     |  +- rags
|  |     |  +- ravoxhood
|  |     |  +- ravoxrobe
|  |     |  +- shepardmask
|  |     |  +- shirt
|  |     |  +- silkcoat
|  |     |  +- silkdress
|  |     |  +- undividedhood
|  |     |  +- undividedrobe
|  |     |  `- webbing
|  |     `- wood_dildo
|  +- culling_duel
|  +- curse
|  |  +- abyssor
|  |  +- astrata
|  |  +- baotha
|  |  +- dendor
|  |  +- eora
|  |  +- graggar
|  |  +- malum
|  |  +- matthios
|  |  +- necra
|  |  +- noc
|  |  +- pestra
|  |  +- ravox
|  |  +- xylix
|  |  `- zizo
|  +- custom_descriptor_entry
|  +- customizer
|  |  +- bodypart_feature
|  |  |  +- accessory
|  |  |  +- crest
|  |  |  +- face_detail
|  |  |  +- hair
|  |  |  |  +- facial
|  |  |  |  |  +- humanoid
|  |  |  |  |  |  `- shaved_default
|  |  |  |  |  `- vox
|  |  |  |  `- head
|  |  |  |     +- humanoid
|  |  |  |     |  +- bald_default
|  |  |  |     |  `- vulpkian
|  |  |  |     `- vox
|  |  |  +- legwear
|  |  |  +- piercing
|  |  |  `- underwear
|  |  `- organ
|  |     +- antennas
|  |     |  `- moth
|  |     +- back_feature
|  |     +- breasts
|  |     |  +- animal
|  |     |  `- human
|  |     +- ears
|  |     |  +- anthro
|  |     |  +- axian
|  |     |  +- cat
|  |     |  +- demihuman
|  |     |  +- dullahan
|  |     |  +- elf
|  |     |  +- goblin
|  |     |  +- halforc
|  |     |  +- lizard
|  |     |  +- lupian
|  |     |  +- tajaran
|  |     |  +- tiefling
|  |     |  `- vulpkanin
|  |     +- eyes
|  |     |  +- humanoid
|  |     |  `- moth
|  |     +- frills
|  |     |  +- anthro
|  |     |  `- lizard
|  |     +- head_feature
|  |     |  +- skrell_hair
|  |     |  `- xeno_head
|  |     +- horns
|  |     |  +- anthro
|  |     |  +- demihuman
|  |     |  +- humanoid
|  |     |  |  `- zardman
|  |     |  `- tusks
|  |     +- neck_feature
|  |     |  +- anthro
|  |     |  `- moth_fluff
|  |     +- penis
|  |     |  +- anthro
|  |     |  +- canine
|  |     |  +- equine
|  |     |  +- feline
|  |     |  +- human
|  |     |  `- lizard
|  |     +- snout
|  |     |  +- akula
|  |     |  +- anthro
|  |     |  |  `- dullahan
|  |     |  +- anthrosmall
|  |     |  +- lizard
|  |     |  +- lupian
|  |     |  +- tabaxi
|  |     |  +- tajaran
|  |     |  `- vulpkanin
|  |     +- soul
|  |     |  `- fire
|  |     +- tail
|  |     |  +- anthro
|  |     |  +- axian
|  |     |  +- demihuman
|  |     |  +- dullahan
|  |     |  +- lizard
|  |     |  +- lupian
|  |     |  +- tabaxi
|  |     |  +- tiefling
|  |     |  `- vulpkanin
|  |     +- tail_feature
|  |     |  +- anthro
|  |     |  +- lizard_spines
|  |     |  `- vox_markings
|  |     +- testicles
|  |     |  +- anthro
|  |     |  +- external
|  |     |  +- human
|  |     |  `- internal
|  |     +- vagina
|  |     |  +- animal
|  |     |  +- anthro
|  |     |  +- human
|  |     |  `- human_anthro
|  |     `- wings
|  |        +- anthro
|  |        +- dracon
|  |        `- moth
|  +- customizer_choice
|  |  +- bodypart_feature
|  |  |  +- accessory
|  |  |  +- crest
|  |  |  +- face_detail
|  |  |  +- hair
|  |  |  |  +- facial
|  |  |  |  |  +- humanoid
|  |  |  |  |  `- vox
|  |  |  |  `- head
|  |  |  |     +- humanoid
|  |  |  |     |  `- vulpkian
|  |  |  |     `- vox
|  |  |  +- legwear
|  |  |  +- piercing
|  |  |  `- underwear
|  |  `- organ
|  |     +- antennas
|  |     |  `- moth
|  |     +- back_feature
|  |     +- breasts
|  |     |  +- animal
|  |     |  `- human
|  |     +- ears
|  |     |  +- anthro
|  |     |  +- axian
|  |     |  +- cat
|  |     |  +- demihuman
|  |     |  +- dullahan
|  |     |  +- elf
|  |     |  +- goblin
|  |     |  +- halforc
|  |     |  +- lizard
|  |     |  +- lupian
|  |     |  +- tajaran
|  |     |  +- tiefling
|  |     |  `- vulpkanin
|  |     +- eyes
|  |     |  +- humanoid
|  |     |  `- moth
|  |     +- frills
|  |     |  +- anthro
|  |     |  `- lizard
|  |     +- head_feature
|  |     |  +- skrell_hair
|  |     |  `- xeno_head
|  |     +- horns
|  |     |  +- anthro
|  |     |  +- demihuman
|  |     |  +- humanoid
|  |     |  `- tusks
|  |     +- neck_feature
|  |     |  +- anthro_fluff
|  |     |  `- moth_fluff
|  |     +- penis
|  |     |  +- barbed
|  |     |  +- barbed_knotted
|  |     |  +- equine
|  |     |  +- human
|  |     |  +- human_anthro
|  |     |  +- knotted
|  |     |  +- tapered
|  |     |  +- tapered_double
|  |     |  +- tapered_double_knot
|  |     |  +- tapered_mammal
|  |     |  `- tentacle
|  |     +- snout
|  |     |  +- akula
|  |     |  +- anthro
|  |     |  |  `- dullahan
|  |     |  +- lizard
|  |     |  +- lupian
|  |     |  +- tabaxi
|  |     |  +- tajaran
|  |     |  `- vulpkanin
|  |     +- soul
|  |     |  `- fire
|  |     +- tail
|  |     |  +- anthro
|  |     |  +- axian
|  |     |  +- demihuman
|  |     |  +- dullahan
|  |     |  +- lizard
|  |     |  +- lupian
|  |     |  +- tabaxi
|  |     |  +- tiefling
|  |     |  `- vulpkanin
|  |     +- tail_feature
|  |     |  +- lizard_spines
|  |     |  `- vox_markings
|  |     +- testicles
|  |     |  +- external
|  |     |  +- human
|  |     |  `- internal
|  |     +- vagina
|  |     |  +- animal
|  |     |  +- anthro
|  |     |  +- human
|  |     |  `- human_anthro
|  |     `- wings
|  |        +- anthro
|  |        +- dracon
|  |        `- moth
|  +- customizer_entry
|  |  +- hair
|  |  |  `- facial
|  |  `- organ
|  |     +- breasts
|  |     +- eyes
|  |     +- penis
|  |     +- testicles
|  |     `- vagina
|  +- data
|  |  +- crime
|  |  `- record
|  +- datacore
|  +- DBQuery
|  +- descriptor_choice
|  |  +- body
|  |  +- chitin
|  |  +- face
|  |  +- face_exp
|  |  +- feathers
|  |  +- fur
|  |  +- height
|  |  +- prominent_four
|  |  +- prominent_four_wild
|  |  +- prominent_one
|  |  +- prominent_one_wild
|  |  +- prominent_three
|  |  +- prominent_three_wild
|  |  +- prominent_two
|  |  +- prominent_two_wild
|  |  +- scales
|  |  +- skin
|  |  +- skin_all
|  |  +- stature
|  |  +- trait
|  |  `- voice
|  +- descriptor_entry
|  +- devotion
|  +- dna
|  |  `- stored
|  +- dog_fashion
|  |  +- back
|  |  |  `- deathsquad
|  |  `- head
|  |     +- beret
|  |     +- blue_wizard
|  |     +- captain
|  |     +- cardborg
|  |     +- cargo_tech
|  |     +- chef
|  |     +- clown
|  |     +- deathsquad
|  |     +- detective
|  |     +- ghost
|  |     +- helmet
|  |     +- hop
|  |     +- kitty
|  |     +- nurse
|  |     +- pirate
|  |     +- rabbit
|  |     +- red_wizard
|  |     +- reindeer
|  |     +- santa
|  |     +- sombrero
|  |     +- ushanka
|  |     `- warden
|  +- duel
|  +- effect_system
|  |  +- expl_particles
|  |  +- explosion
|  |  |  `- smoke
|  |  +- foam_spread
|  |  |  +- long
|  |  |  `- metal
|  |  |     `- smart
|  |  +- lightning_spread
|  |  +- reagents_explosion
|  |  +- smoke_spread
|  |  |  +- bad
|  |  |  +- blind_gas
|  |  |  +- chem
|  |  |  +- fast
|  |  |  +- fire_gas
|  |  |  +- healing_gas
|  |  |  +- mute_gas
|  |  |  +- poison_gas
|  |  |  +- sleeping
|  |  |  `- transparent
|  |  +- spark_spread
|  |  |  `- quantum
|  |  +- steam_spread
|  |  `- trail_follow
|  |     +- ion
|  |     `- steam
|  +- element
|  |  +- ai_flee_while_injured
|  |  +- ai_retaliate
|  |  +- bed_tuckable
|  |  +- connect_loc
|  |  +- earhealing
|  |  +- firestacker
|  |  +- holy_weakness
|  |  +- interrupt_on_damage
|  |  +- mob_overlay_effect
|  |  +- noisy_movement
|  |  +- one_time_poison
|  |  +- relay_attackers
|  |  +- slapcrafting
|  |  +- snailcrawl
|  |  `- tipped_item
|  +- embedding_behavior
|  +- emote
|  |  +- beep
|  |  +- brain
|  |  |  +- alarm
|  |  |  +- alert
|  |  |  +- flash
|  |  |  +- notice
|  |  |  `- whistle
|  |  +- flip
|  |  +- living
|  |  |  +- aggro
|  |  |  +- attack
|  |  |  +- attnwhistle
|  |  |  +- bark
|  |  |  +- bleat
|  |  |  +- blink
|  |  |  +- blush
|  |  |  +- bow
|  |  |  +- breathgasp
|  |  |  +- burp
|  |  |  +- cackle
|  |  |  +- carbon
|  |  |  |  +- airguitar
|  |  |  |  +- blink
|  |  |  |  +- blink_r
|  |  |  |  +- clap
|  |  |  |  +- deathgurgle
|  |  |  |  +- gnarl
|  |  |  |  +- human
|  |  |  |  |  +- cry
|  |  |  |  |  +- eyebrow
|  |  |  |  |  +- grumble
|  |  |  |  |  +- handshake
|  |  |  |  |  +- mumble
|  |  |  |  |  +- pale
|  |  |  |  |  +- psst
|  |  |  |  |  +- raise
|  |  |  |  |  +- salute
|  |  |  |  |  +- sexmoanhvy
|  |  |  |  |  +- sexmoanlight
|  |  |  |  |  +- shrug
|  |  |  |  |  +- wag
|  |  |  |  |  `- wing
|  |  |  |  +- roll
|  |  |  |  +- scratch
|  |  |  |  +- screech
|  |  |  |  +- sign
|  |  |  |  |  `- signal
|  |  |  |  +- tail
|  |  |  |  `- wink
|  |  |  +- caw
|  |  |  +- chitter
|  |  |  +- choke
|  |  |  +- chuckle
|  |  |  +- circle
|  |  |  +- clearthroat
|  |  |  +- collapse
|  |  |  +- cough
|  |  |  +- cross
|  |  |  +- custom
|  |  |  +- dance
|  |  |  +- death
|  |  |  +- deathgasp
|  |  |  +- drool
|  |  |  +- drown
|  |  |  +- embed
|  |  |  +- emote_lizard_thump
|  |  |  +- faint
|  |  |  +- fatigue
|  |  |  +- ffsalute
|  |  |  +- flap
|  |  |  |  `- aflap
|  |  |  +- flutter
|  |  |  +- frown
|  |  |  +- fsalute
|  |  |  +- fwhine
|  |  |  +- gag
|  |  |  +- gasp
|  |  |  +- giggle
|  |  |  +- glare
|  |  |  +- grimace
|  |  |  +- grin
|  |  |  +- groan
|  |  |  +- groin
|  |  |  +- growl
|  |  |  +- haltyell
|  |  |  +- help
|  |  |  +- hiss
|  |  |  +- hmm
|  |  |  +- hmph
|  |  |  +- holdbreath
|  |  |  +- hoot
|  |  |  +- howl
|  |  |  +- hug
|  |  |  +- huh
|  |  |  +- hum
|  |  |  +- idle
|  |  |  +- jump
|  |  |  +- kiss
|  |  |  +- laugh
|  |  |  +- leap
|  |  |  +- lick
|  |  |  +- lizard_bellow
|  |  |  +- lizard_hiss
|  |  |  +- lizard_squeal
|  |  |  +- look
|  |  |  +- meditate
|  |  |  +- meow
|  |  |  +- moan
|  |  |  +- moo
|  |  |  +- mrrp
|  |  |  +- nod
|  |  |  +- oink
|  |  |  +- pain
|  |  |  +- paincrit
|  |  |  +- painmoan
|  |  |  +- peep
|  |  |  +- phiss
|  |  |  +- pinch
|  |  |  +- pleased
|  |  |  +- point
|  |  |  +- pout
|  |  |  +- pray
|  |  |  +- prbt
|  |  |  +- psnort
|  |  |  +- purr
|  |  |  +- rage
|  |  |  +- roar
|  |  |  +- scowl
|  |  |  +- scream
|  |  |  |  +- agony
|  |  |  |  +- firescream
|  |  |  |  +- painscream
|  |  |  |  `- strain
|  |  |  +- shake
|  |  |  +- shakehead
|  |  |  +- shh
|  |  |  +- shiver
|  |  |  +- sigh
|  |  |  +- slap
|  |  |  +- smile
|  |  |  +- smug
|  |  |  +- snap
|  |  |  +- snap2
|  |  |  +- snap3
|  |  |  +- sneeze
|  |  |  +- sniff
|  |  |  +- snore
|  |  |  +- spit
|  |  |  +- squeak
|  |  |  +- squint
|  |  |  +- standard_position
|  |  |  +- standard_rally
|  |  |  +- stare
|  |  |  +- stat_roll
|  |  |  |  +- charisma
|  |  |  |  +- constitution
|  |  |  |  +- fortune
|  |  |  |  +- intelligence
|  |  |  |  +- perception
|  |  |  |  +- speed
|  |  |  |  +- strength
|  |  |  |  `- willpower
|  |  |  +- stomp
|  |  |  +- strech
|  |  |  +- subtle
|  |  |  +- sulk
|  |  |  +- sway
|  |  |  +- tremble
|  |  |  +- trill
|  |  |  +- twitch
|  |  |  +- twitch_s
|  |  |  +- warcry
|  |  |  +- wave
|  |  |  +- whimper
|  |  |  +- whine
|  |  |  +- whisper
|  |  |  +- whistle
|  |  |  +- wsmile
|  |  |  +- yawn
|  |  |  `- yip
|  |  `- spin
|  +- error_viewer
|  |  +- error_cache
|  |  +- error_entry
|  |  `- error_source
|  +- event_group
|  +- events
|  +- examine_panel
|  |  `- familiar
|  +- explosion
|  +- export
|  +- export_report
|  +- faith
|  |  +- divine
|  |  +- godless
|  |  +- inhumen
|  |  +- mossmother
|  |  `- old_god
|  +- familiar_prefs
|  +- feedback_variable
|  +- flesh_archetype
|  |  +- aggressive
|  |  +- arbitrary
|  |  +- authoritarian
|  |  +- fearful
|  |  +- inquisitive
|  |  `- split_personality
|  +- flesh_concept
|  |  +- beauty
|  |  +- blood
|  |  +- bondage
|  |  +- chaos
|  |  +- companionship
|  |  +- courage
|  |  +- cowardice
|  |  +- creation
|  |  +- death
|  |  +- decay
|  |  +- despair
|  |  +- destruction
|  |  +- dreams
|  |  +- fear
|  |  +- freedom
|  |  +- greed
|  |  +- growth
|  |  +- hope
|  |  +- hunger
|  |  +- identity
|  |  +- ignorance
|  |  +- justice
|  |  +- lies
|  |  +- loneliness
|  |  +- love
|  |  +- memory
|  |  +- mercy
|  |  +- order
|  |  +- pain
|  |  +- power
|  |  +- sacrifice
|  |  +- time
|  |  +- transformation
|  |  +- truth
|  |  +- ugliness
|  |  +- unity
|  |  +- weakness
|  |  `- wisdom
|  +- flesh_quirk
|  |  +- affectionate
|  |  +- ambitious
|  |  +- curious
|  |  +- discharge
|  |  +- forgetful
|  |  +- hoarder
|  |  +- impatient
|  |  +- mimic
|  |  +- obedient
|  |  +- patient
|  |  +- repetitive
|  |  +- royal
|  |  +- stubborn
|  |  +- territorial
|  |  `- timid
|  +- flesh_task
|  |  `- knowledge
|  +- flesh_trait
|  |  +- ambitious
|  |  +- analytical
|  |  +- cautious
|  |  +- chaotic
|  |  +- creative
|  |  +- curious
|  |  +- deception
|  |  +- destructive
|  |  +- dominant
|  |  +- honest
|  |  +- impulsive
|  |  +- logical
|  |  +- observant
|  |  +- orderly
|  |  +- peaceful
|  |  +- philosophical
|  |  +- playful
|  |  +- territorial
|  |  `- violent
|  +- flowcache
|  +- forced_movement
|  +- getrev
|  +- grid_set
|  +- hag_boon
|  |  +- buff
|  |  |  +- creeping_moss
|  |  |  +- curse
|  |  |  |  +- choking_moss
|  |  |  |  +- slumber
|  |  |  |  `- waterlogged
|  |  |  +- natural_communion
|  |  |  `- storm_rebirth
|  |  +- curse
|  |  |  +- rotting_touch
|  |  |  `- storm_weakness
|  |  +- curse_scar
|  |  +- item
|  |  |  +- hag_axe
|  |  |  +- hag_spear
|  |  |  +- hag_sword
|  |  |  `- wyrd_cross
|  |  +- item_debt
|  |  +- revival_debt
|  |  +- spell
|  |  |  +- banish
|  |  |  +- find_riches
|  |  |  +- spider_speak
|  |  |  `- twist_food
|  |  `- trait
|  |     +- armor_heavy
|  |     +- armor_medium
|  |     +- azure_native
|  |     +- battleready
|  |     +- beautiful
|  |     +- beautiful_uncanny
|  |     +- bleed_resistance
|  |     +- civil_barbarian
|  |     +- combat_aware
|  |     +- counter_counterspell
|  |     +- crackhead
|  |     +- curse
|  |     |  +- critical_weakness
|  |     |  +- mute
|  |     |  +- no_defense
|  |     |  +- no_run
|  |     |  +- no_spells
|  |     |  +- silver_weakness
|  |     |  `- ugly
|  |     +- dark_vision
|  |     +- dodge_expert
|  |     +- expert_alchemy
|  |     +- expert_homestead
|  |     +- expert_medicine
|  |     +- expert_sewing
|  |     +- expert_smithing
|  |     +- expert_survival
|  |     +- good_trainer
|  |     +- grab_immunity
|  |     +- guidance
|  |     +- hard_dismember
|  |     +- ignoreslowdown
|  |     +- jack_of_all_trades
|  |     +- keen_ears
|  |     +- leaper
|  |     +- matthios_eyes
|  |     +- nightowl
|  |     +- no_pain
|  |     +- ritualist
|  |     +- self_sustenance
|  |     +- sharper_blades
|  |     +- unbound_strength
|  |     +- water_breathing
|  |     +- webwalk
|  |     +- wood_walker
|  |     `- wyrd_labourer
|  +- hag_rite
|  |  `- ugly
|  +- hair_gradient
|  |  +- _split
|  |  +- fadedown
|  |  +- fadeup
|  |  +- long_fade_down
|  |  +- long_fade_up
|  |  +- none
|  |  +- reflected
|  |  +- reflected_inverse
|  |  +- short_fade_down
|  |  +- short_fade_up
|  |  +- streaks
|  |  +- vertical_split
|  |  +- wavy
|  |  `- wavy_spike
|  +- hallucination
|  |  +- battle
|  |  +- chasing_mob
|  |  +- chat
|  |  +- dangerflash
|  |  +- death
|  |  +- delusion
|  |  +- fake_alert
|  |  +- fake_heartattack
|  |  +- fire
|  |  +- floor_shift
|  |  +- husks
|  |  +- items
|  |  +- message
|  |  +- self_delusion
|  |  +- shock
|  |  +- sounds
|  |  +- townannouncement
|  |  +- voices
|  |  `- weird_sounds
|  +- Heap
|  +- holiday
|  |  +- animal
|  |  +- april_fools
|  |  +- bee
|  |  +- beer
|  |  +- birthday
|  |  +- boss
|  |  +- boxing
|  |  +- columbus
|  |  +- doctor
|  |  +- doomsday
|  |  +- earth
|  |  +- easter
|  |  +- father
|  |  +- festive_season
|  |  +- firefighter
|  |  +- flowers
|  |  +- fourtwenty
|  |  +- france
|  |  +- friday_thirteenth
|  |  +- friendship
|  |  +- groundhog
|  |  +- halloween
|  |  +- hello
|  |  +- human_rights
|  |  +- ianbirthday
|  |  +- kindness
|  |  +- labor
|  |  +- leap
|  |  +- lifeday
|  |  +- monkey
|  |  +- moth
|  |  +- mother
|  |  +- new_year
|  |  +- no_this_is_patrick
|  |  +- october_revolution
|  |  +- pi
|  |  +- pirate
|  |  +- programmers
|  |  +- questions
|  |  +- ramadan
|  |  |  `- end
|  |  +- random_kindness
|  |  +- smile
|  |  +- spess
|  |  +- summersolstice
|  |  +- tea
|  |  +- thanksgiving
|  |  |  `- canada
|  |  +- UFO
|  |  +- USA
|  |  +- valentines
|  |  +- vegan
|  |  +- writer
|  |  `- xmas
|  +- hSB
|  +- http_request
|  +- http_response
|  +- hud
|  |  `- constructs
|  +- icon_snapshot
|  +- icon_transformer
|  +- idle_behavior
|  |  +- idle_crab_walk
|  |  +- idle_random_walk
|  |  |  +- hostile_tameable
|  |  |  `- less_walking
|  |  `- nothing
|  +- inqports
|  |  +- articles
|  |  |  +- accusations
|  |  |  +- bmirror
|  |  |  +- confessions
|  |  |  +- crankbox
|  |  |  +- indexaccused
|  |  |  +- indexers
|  |  |  +- stamppot
|  |  |  +- stampstuff
|  |  |  `- superbow
|  |  +- equipment
|  |  |  +- blackbags
|  |  |  +- chains
|  |  |  +- climbinggear
|  |  |  +- garrote
|  |  |  +- inqcordage
|  |  |  +- listener
|  |  |  +- nocshades
|  |  |  +- psybles
|  |  |  +- silvarrow
|  |  |  +- silvbolt
|  |  |  +- silverstake
|  |  |  +- silvheavybolt
|  |  |  `- whisperer
|  |  +- supplies
|  |  |  +- blessedbolts
|  |  |  +- bottlebombs
|  |  |  +- bullion
|  |  |  +- extrafunding
|  |  |  +- lifeblood
|  |  |  +- manna
|  |  |  +- medical
|  |  |  +- psybuns
|  |  |  +- quicksilver
|  |  |  +- smokes
|  |  |  +- tnt
|  |  |  `- tntsatchel
|  |  `- wardrobe
|  |     +- confessionalcombo
|  |     +- fencerset
|  |     +- fencersthree
|  |     +- inspector
|  |     +- inspectorcoat
|  |     +- nobledressup
|  |     +- otavansatchel
|  |     +- psycross
|  |     +- psycrosssilver
|  |     +- psydonhelms
|  |     +- psydonianstandard
|  |     +- psydonthorns
|  |     +- psysack
|  |     +- satchelbelted
|  |     `- strangemask
|  +- inspiration
|  +- intent
|  |  +- arc
|  |  |  +- bow
|  |  |  |  +- heavy
|  |  |  |  `- short
|  |  |  +- crossbow
|  |  |  |  +- heavy
|  |  |  |  `- slurbow
|  |  |  `- sling
|  |  +- attach
|  |  +- axe
|  |  |  +- bash
|  |  |  |  +- battle
|  |  |  |  `- martyr
|  |  |  +- chop
|  |  |  |  +- arbelos
|  |  |  |  +- frost
|  |  |  |  +- halberd
|  |  |  |  +- long
|  |  |  |  |  `- martyr
|  |  |  |  +- martyr
|  |  |  |  +- scythe
|  |  |  |  `- stone
|  |  |  +- cut
|  |  |  |  +- arbelos
|  |  |  |  +- frost
|  |  |  |  +- handaxe
|  |  |  |  +- long
|  |  |  |  |  `- martyr
|  |  |  |  +- lunge
|  |  |  |  `- martyr
|  |  |  +- sweep
|  |  |  `- thrust
|  |  +- bite
|  |  +- bless
|  |  +- buttstroke
|  |  |  `- heavy
|  |  +- cast
|  |  +- chisel
|  |  +- claw
|  |  |  +- cut
|  |  |  |  +- gronn
|  |  |  |  +- iron
|  |  |  |  `- steel
|  |  |  +- lunge
|  |  |  |  +- gronn
|  |  |  |  +- iron
|  |  |  |  `- steel
|  |  |  `- rend
|  |  |     `- steel
|  |  +- dagger
|  |  |  +- chop
|  |  |  |  +- bronze
|  |  |  |  +- cleaver
|  |  |  |  `- wood
|  |  |  +- cut
|  |  |  |  +- blunt
|  |  |  |  +- heavy
|  |  |  |  +- rend
|  |  |  |  `- wood
|  |  |  +- sucker_punch
|  |  |  `- thrust
|  |  |     +- blunt
|  |  |     +- bronze
|  |  |     +- combat
|  |  |     +- fork
|  |  |     +- pick
|  |  |     |  `- blunt
|  |  |     +- weak
|  |  |     `- wood
|  |  +- drill
|  |  +- effect
|  |  |  +- daze
|  |  |  |  +- freisabre
|  |  |  |  +- longsword
|  |  |  |  |  `- clinch
|  |  |  |  +- longsword2h
|  |  |  |  +- martyr
|  |  |  |  `- shield
|  |  |  `- hobble
|  |  |     `- martyr
|  |  +- fill
|  |  +- flail
|  |  |  +- bash
|  |  |  +- smash
|  |  |  |  +- golgotha
|  |  |  |  +- matthiosflail
|  |  |  |  +- militia
|  |  |  |  `- ranged
|  |  |  +- strike
|  |  |  |  `- matthiosflail
|  |  |  +- strikerange
|  |  |  +- sweep
|  |  |  `- thresh
|  |  +- food
|  |  +- garrote
|  |  |  +- choke
|  |  |  `- grab
|  |  +- give
|  |  +- grab
|  |  |  +- choke
|  |  |  +- disarm
|  |  |  +- hostage
|  |  |  +- move
|  |  |  +- remove
|  |  |  +- shove
|  |  |  +- smash
|  |  |  +- twist
|  |  |  +- twistitem
|  |  |  `- upgrade
|  |  +- grapple
|  |  +- hit
|  |  +- jump
|  |  +- katar
|  |  |  +- cut
|  |  |  `- thrust
|  |  |     `- arbelos
|  |  +- kick
|  |  +- knuckles
|  |  |  `- strike
|  |  |     `- wallop
|  |  +- lance
|  |  |  `- onehand
|  |  +- lord_electrocute
|  |  +- lord_silence
|  |  +- lordbash
|  |  +- mace
|  |  |  +- bash
|  |  |  |  `- ranged
|  |  |  +- boom
|  |  |  +- rangedthrust
|  |  |  +- smash
|  |  |  |  +- astrata
|  |  |  |  +- crush
|  |  |  |  +- eaglebeak
|  |  |  |  +- grand
|  |  |  |  +- lesser
|  |  |  |  +- martyr
|  |  |  |  +- shield
|  |  |  |  |  `- metal
|  |  |  |  |     `- great
|  |  |  |  +- werewolf
|  |  |  |  |  `- gnoll
|  |  |  |  `- wood
|  |  |  |     `- ranged
|  |  |  +- strike
|  |  |  |  +- astrata
|  |  |  |  +- dislocate
|  |  |  |  +- gnoll
|  |  |  |  +- grand
|  |  |  |  +- martyr
|  |  |  |  +- pan
|  |  |  |  +- shovel
|  |  |  |  +- wallop
|  |  |  |  `- wood
|  |  |  +- sweep
|  |  |  `- warhammer
|  |  |     +- pick
|  |  |     `- stab
|  |  |        `- lesser
|  |  +- magos_electrocute
|  |  +- maul
|  |  |  `- spiked
|  |  +- peculate
|  |  +- pforkdump
|  |  +- pick
|  |  |  +- bad
|  |  |  +- good
|  |  |  `- ranged
|  |  +- pour
|  |  +- reel
|  |  +- rend
|  |  |  +- apophis
|  |  |  +- krieg
|  |  |  `- reach
|  |  |     `- partizan
|  |  |        `- martyr
|  |  +- shield
|  |  |  +- bash
|  |  |  |  `- metal
|  |  |  `- block
|  |  |     `- metal
|  |  +- shoot
|  |  |  +- bow
|  |  |  |  +- heavy
|  |  |  |  `- short
|  |  |  `- crossbow
|  |  |     +- heavy
|  |  |     `- slurbow
|  |  +- shovelscoop
|  |  +- simple
|  |  |  +- axe
|  |  |  |  +- orc
|  |  |  |  `- skeleton
|  |  |  +- baroness
|  |  |  +- bear
|  |  |  +- bite
|  |  |  |  +- bear
|  |  |  |  +- bigrat
|  |  |  |  +- dragon_bite
|  |  |  |  +- honeyspider
|  |  |  |  +- mirespider
|  |  |  |  +- mirespider_lurker
|  |  |  |  +- mirespider_paralytic
|  |  |  |  `- volf
|  |  |  +- cabbit
|  |  |  +- cat
|  |  |  +- claw
|  |  |  |  +- deepone_boss
|  |  |  |  +- deepone_unarmed
|  |  |  |  +- mole
|  |  |  |  +- mossback
|  |  |  |  +- primordial
|  |  |  |  +- simplewwnpc
|  |  |  |  +- skeleton
|  |  |  |  +- skeleton_unarmed
|  |  |  |  `- witch_cat
|  |  |  +- dragger
|  |  |  +- dreamfiend_ancient
|  |  |  +- elemental_unarmed
|  |  |  +- elementalt2_unarmed
|  |  |  +- fogbeast
|  |  |  +- fox
|  |  |  +- gnoll_cut
|  |  |  +- hag
|  |  |  +- headbutt
|  |  |  |  `- saiga
|  |  |  +- lich
|  |  |  +- minotaur_axe
|  |  |  +- minotaur_unarmed
|  |  |  +- mole
|  |  |  |  `- dig
|  |  |  +- reiver_rider_sabre
|  |  |  +- saiga
|  |  |  +- slam
|  |  |  +- slash
|  |  |  +- spear
|  |  |  |  +- reiver_rider_lancer
|  |  |  |  `- skeleton
|  |  |  +- spider
|  |  |  |  `- mire
|  |  |  +- troll_axe
|  |  |  +- volf
|  |  |  `- werewolf
|  |  |     `- gnoll
|  |  +- smoke
|  |  +- snip
|  |  +- spear
|  |  |  +- bash
|  |  |  |  +- martyr
|  |  |  |  +- polehammer
|  |  |  |  `- ranged
|  |  |  |     `- quarterstaff
|  |  |  +- cast
|  |  |  +- cut
|  |  |  |  +- bardiche
|  |  |  |  |  `- cleave
|  |  |  |  +- glaive
|  |  |  |  |  `- sweep
|  |  |  |  +- martyr
|  |  |  |  +- naginata
|  |  |  |  |  `- sweep
|  |  |  |  +- oneh
|  |  |  |  +- scythe
|  |  |  |  `- short
|  |  |  `- thrust
|  |  |     +- azurean
|  |  |     |  +- oneh
|  |  |     |  `- pick
|  |  |     +- bad
|  |  |     +- lance
|  |  |     +- martyr
|  |  |     +- militia
|  |  |     +- oneh
|  |  |     |  +- martyr
|  |  |     |  `- training
|  |  |     +- orcthrust
|  |  |     +- pike
|  |  |     |  `- skewer
|  |  |     +- quarterstaff
|  |  |     +- short
|  |  |     `- training
|  |  +- special
|  |  +- spell
|  |  +- splash
|  |  +- stab
|  |  |  `- militia
|  |  +- swing
|  |  |  `- sling
|  |  +- sword
|  |  |  +- bash
|  |  |  +- chop
|  |  |  |  +- cleave
|  |  |  |  |  `- super
|  |  |  |  +- falx
|  |  |  |  +- heavy
|  |  |  |  +- long
|  |  |  |  +- martyr
|  |  |  |  +- militia
|  |  |  |  +- sabre
|  |  |  |  `- short
|  |  |  +- cut
|  |  |  |  +- arming
|  |  |  |  +- exe
|  |  |  |  |  +- cleave
|  |  |  |  |  `- sweep
|  |  |  |  +- falx
|  |  |  |  +- krieg
|  |  |  |  +- light
|  |  |  |  +- long
|  |  |  |  +- martyr
|  |  |  |  +- master
|  |  |  |  +- militia
|  |  |  |  +- rapier
|  |  |  |  +- rend
|  |  |  |  +- sabre
|  |  |  |  |  `- master
|  |  |  |  +- short
|  |  |  |  `- zwei
|  |  |  |     +- cleave
|  |  |  |     `- sweep
|  |  |  +- disarm
|  |  |  +- lunge
|  |  |  +- strike
|  |  |  |  +- bad
|  |  |  |  `- martyr
|  |  |  `- thrust
|  |  |     +- arming
|  |  |     +- blunt
|  |  |     +- estoc
|  |  |     |  `- lunge
|  |  |     +- exe
|  |  |     +- heavy
|  |  |     +- hook
|  |  |     +- krieg
|  |  |     +- long
|  |  |     |  +- halfsword
|  |  |     |  |  +- frei
|  |  |     |  |  +- jab
|  |  |     |  |  `- lesser
|  |  |     |  `- master
|  |  |     +- martyr
|  |  |     +- rapier
|  |  |     +- sabre
|  |  |     +- short
|  |  |     `- zwei
|  |  +- tie
|  |  +- till
|  |  +- unarmed
|  |  |  +- claw
|  |  |  |  `- troll
|  |  |  +- dragonclaw
|  |  |  +- grab
|  |  |  +- help
|  |  |  +- punch
|  |  |  `- shove
|  |  +- use
|  |  +- weep
|  |  +- whip
|  |  |  +- crack
|  |  |  |  `- blunt
|  |  |  +- lash
|  |  |  |  `- master
|  |  |  `- punish
|  |  `- whips
|  +- ipintel
|  +- job
|  |  +- priest
|  |  |  `- vice
|  |  +- roguetown
|  |  |  +- absolver
|  |  |  +- adventurer
|  |  |  |  `- courtagent
|  |  |  +- apothecary
|  |  |  +- archivist
|  |  |  +- assassin
|  |  |  +- bandit
|  |  |  +- bathmaster
|  |  |  +- bathworker
|  |  |  +- clerk
|  |  |  +- cook
|  |  |  +- councillor
|  |  |  +- crier
|  |  |  +- druid
|  |  |  +- exlady
|  |  |  +- farmer
|  |  |  +- gnoll
|  |  |  +- goblin
|  |  |  +- greater_skeleton
|  |  |  |  `- lich
|  |  |  +- guildmaster
|  |  |  +- guildsman
|  |  |  +- hag
|  |  |  +- hand
|  |  |  +- heartfelt
|  |  |  |  +- hand
|  |  |  |  +- knight
|  |  |  |  +- lord
|  |  |  |  `- retinue
|  |  |  +- innkeeper
|  |  |  +- inquisitor
|  |  |  +- jester
|  |  |  +- keeper
|  |  |  +- knight
|  |  |  +- lady
|  |  |  +- lord
|  |  |  +- lunatic
|  |  |  +- magician
|  |  |  +- manorguard
|  |  |  +- marshal
|  |  |  +- martyr
|  |  |  +- mercenary
|  |  |  +- merchant
|  |  |  +- migrant
|  |  |  +- monk
|  |  |  +- orthodoxist
|  |  |  +- physician
|  |  |  +- pilgrim
|  |  |  +- priest
|  |  |  +- prince
|  |  |  +- seneschal
|  |  |  +- sergeant
|  |  |  +- servant
|  |  |  +- sexton
|  |  |  +- shophand
|  |  |  +- squire
|  |  |  +- steward
|  |  |  +- suitor
|  |  |  +- tailor
|  |  |  +- tapster
|  |  |  +- templar
|  |  |  +- tester
|  |  |  +- trader
|  |  |  +- vagabond
|  |  |  +- vampire_guard
|  |  |  +- vampire_servant
|  |  |  +- vampire_spawn
|  |  |  +- veteran
|  |  |  +- villager
|  |  |  +- wapprentice
|  |  |  +- warden
|  |  |  +- watchman
|  |  |  `- wretch
|  |  `- unassigned
|  +- keybinding
|  |  +- mob
|  |  |  +- face_east
|  |  |  +- face_north
|  |  |  +- face_south
|  |  |  +- face_west
|  |  |  +- pixel_shift
|  |  |  +- stop_pulling
|  |  |  +- target_body_chest
|  |  |  +- target_body_groin
|  |  |  +- target_eye_nose
|  |  |  +- target_head_cycle
|  |  |  +- target_left_arm
|  |  |  +- target_left_leg
|  |  |  +- target_mouth_ears
|  |  |  +- target_r_arm
|  |  |  +- target_right_leg
|  |  |  +- toggle_move_intent
|  |  |  `- toggle_move_intent_alternative
|  |  +- admin
|  |  |  +- admin_ghost
|  |  |  +- admin_say
|  |  |  +- deadsay
|  |  |  +- invisimin
|  |  |  +- player_panel_new
|  |  |  +- rmbcontext
|  |  |  +- stealthmode
|  |  |  `- toggle_buildmode_self
|  |  +- carbon
|  |  |  +- actions
|  |  |  |  +- action_1
|  |  |  |  +- action_2
|  |  |  |  +- action_3
|  |  |  |  +- action_4
|  |  |  |  +- action_5
|  |  |  |  +- action_6
|  |  |  |  +- action_7
|  |  |  |  +- action_8
|  |  |  |  `- action_9
|  |  |  +- bite_intent
|  |  |  +- cycle_rmb_intent
|  |  |  +- give_intent
|  |  |  +- guard
|  |  |  +- intent_four
|  |  |  +- intent_one
|  |  |  +- intent_three
|  |  |  +- intent_two
|  |  |  +- jump_intent
|  |  |  +- kick_intent
|  |  |  +- rmb_intent_1
|  |  |  +- rmb_intent_2
|  |  |  +- rmb_intent_3
|  |  |  +- rmb_intent_4
|  |  |  +- rmb_intent_5
|  |  |  +- rmb_intent_6
|  |  |  +- select_disarm_intent
|  |  |  +- select_grab_intent
|  |  |  +- select_harm_intent
|  |  |  +- select_help_intent
|  |  |  +- special_intent
|  |  |  +- toggle_arc_mode
|  |  |  `- toggle_throw_mode
|  |  +- client
|  |  |  +- admin_help
|  |  |  +- communication
|  |  |  |  +- me
|  |  |  |  +- me_big
|  |  |  |  `- say
|  |  |  +- minimal_hud
|  |  |  `- screenshot
|  |  +- dsay
|  |  +- emote
|  |  +- human
|  |  |  +- bag_equip_backl
|  |  |  +- bag_equip_backr
|  |  |  +- bag_equip_beltl
|  |  |  +- bag_equip_beltr
|  |  |  +- fixeye
|  |  |  +- quick_equipbelt
|  |  |  +- quick_equipcloak
|  |  |  `- set_pose
|  |  +- living
|  |  |  +- activate_inhand
|  |  |  +- alt_grip
|  |  |  +- defendtoggle
|  |  |  +- dodgeparry
|  |  |  +- drop_item
|  |  |  +- lookup
|  |  |  +- pixel_shift_layerdown
|  |  |  +- pixel_shift_layerup
|  |  |  +- resist
|  |  |  +- rest
|  |  |  +- restd
|  |  |  +- search
|  |  |  +- sneak
|  |  |  +- sprint
|  |  |  +- standu
|  |  |  +- submit
|  |  |  +- swap_hands
|  |  |  +- swap_left
|  |  |  +- swap_right
|  |  |  `- toggle_compliance
|  |  +- movement
|  |  |  +- east
|  |  |  +- north
|  |  |  +- south
|  |  |  `- west
|  |  `- robot
|  |     +- intent_cycle
|  |     +- moduleone
|  |     +- modulethree
|  |     +- moduletwo
|  |     `- unequip_module
|  +- language
|  |  +- aavnic
|  |  +- abyssal
|  |  +- aphasia
|  |  +- beachbum
|  |  +- beast
|  |  +- celestial
|  |  +- codespeak
|  |  +- common
|  |  +- draconic
|  |  +- drone
|  |  +- dwarvish
|  |  +- elvish
|  |  +- etruscan
|  |  +- grenzelhoftian
|  |  +- gronnic
|  |  +- hellspeak
|  |  +- kazengunese
|  |  +- lingyuese
|  |  +- machine
|  |  +- monkey
|  |  +- mushroom
|  |  +- narsie
|  |  +- oldazurian
|  |  +- orcish
|  |  +- otavan
|  |  +- piratespeak
|  |  +- raneshi
|  |  +- slime
|  |  +- swarmer
|  |  +- thievescant
|  |  +- undead
|  |  +- undercommon
|  |  `- xenocommon
|  +- language_holder
|  |  +- abyssal
|  |  +- alien
|  |  +- basic
|  |  +- construct
|  |  +- drone
|  |  |  `- syndicate
|  |  +- empty
|  |  +- lightbringer
|  |  +- monkey
|  |  +- slime
|  |  +- swarmer
|  |  `- synthetic
|  +- language_menu
|  +- laws_menu
|  +- lift_master
|  |  `- tram
|  +- light_source
|  +- lighting_corner
|  +- loadout_item
|  |  +- allwrappings
|  |  +- ankletscloth
|  |  +- ankletsfur
|  |  +- aproncook
|  |  +- archercap
|  |  +- babouche
|  |  +- bandages
|  |  +- bardhat
|  |  +- bardress
|  |  +- baredrobe
|  |  +- bases
|  |  +- bell_collar
|  |  +- bottomtunic
|  |  +- breechclothbelt
|  |  +- breechclothbeltalt
|  |  +- briar_crown
|  |  +- briarthorns
|  |  +- buckled_hat
|  |  +- calendula_crown
|  |  +- caparison
|  |  |  +- astrata
|  |  |  +- eora
|  |  |  +- fogbeast
|  |  |  `- psy
|  |  +- cape
|  |  +- card_deck
|  |  +- chaperon
|  |  |  +- alt
|  |  |  `- burgher
|  |  +- chefhat
|  |  +- chemise
|  |  +- cloth_blindfold
|  |  +- collar
|  |  +- cotehardie
|  |  +- crusadercloak
|  |  +- cursed_collar
|  |  +- custom_book
|  |  +- darkboots
|  |  +- darkcloak
|  |  +- dendormask
|  |  +- desertbra
|  |  +- deserthood
|  |  +- desertskirt
|  |  +- direcloak
|  |  +- donator
|  |  |  +- aeternum
|  |  |  +- aisuwand
|  |  |  +- bat
|  |  |  +- bigfoot
|  |  |  +- bigfoot_axe
|  |  |  +- dakken
|  |  |  |  `- sword
|  |  |  +- dasfox
|  |  |  |  +- cuirass
|  |  |  |  +- lance
|  |  |  |  `- periapt
|  |  |  +- drd
|  |  |  |  +- caparison
|  |  |  |  `- shield
|  |  |  +- eekasqueak
|  |  |  +- eiren
|  |  |  +- eiren2
|  |  |  +- eiren3
|  |  |  +- eiren4
|  |  |  +- eiren5
|  |  |  +- eiren6
|  |  |  +- eiren7
|  |  |  +- funky
|  |  |  +- inverserun
|  |  |  +- koruu
|  |  |  |  +- glaive
|  |  |  |  `- kukri
|  |  |  |     `- warden
|  |  |  +- lmwevil
|  |  |  |  `- brassbeak
|  |  |  +- maesune
|  |  |  |  +- sabre
|  |  |  |  `- shield
|  |  |  +- mansa
|  |  |  +- nerocavalier
|  |  |  +- plex
|  |  |  +- porcelainmask
|  |  |  +- rebel
|  |  |  +- regnum
|  |  |  +- ryan
|  |  |  |  `- psy_helm
|  |  |  +- sci_flamesword
|  |  |  +- sci_sandsword
|  |  |  +- shudderfly
|  |  |  |  `- eoranspike
|  |  |  +- sru
|  |  |  +- stinketh
|  |  |  |  `- pike
|  |  |  +- strudel1
|  |  |  +- strudel2
|  |  |  +- strudel3
|  |  |  +- strudel4
|  |  |  +- waff
|  |  |  +- waff2
|  |  |  +- walkthewaste
|  |  |  +- willmbrink
|  |  |  |  `- sleeves
|  |  |  +- zoe
|  |  |  +- zoe_shovel
|  |  |  +- zydrasgreataxe
|  |  |  `- zydrasiconocrown
|  |  +- doublebelt
|  |  +- dress
|  |  +- duelist_hat
|  |  +- duelmask
|  |  +- eastcloak2
|  |  +- eastshirt1
|  |  +- eastshirt2
|  |  +- eorahood
|  |  +- explorerhat
|  |  +- explorerpants
|  |  +- explorervest
|  |  +- fake_blindfold
|  |  +- fancycoat
|  |  +- fancyhat
|  |  +- farkle_dice
|  |  +- fauldedbelt
|  |  +- feather
|  |  +- feld_robe
|  |  +- fine_parasol
|  |  +- fingerless
|  |  +- folded_hat
|  |  +- forlon_collar
|  |  +- formalsilks
|  |  +- furcloak
|  |  +- furhat
|  |  +- gladsandals
|  |  +- goldenordercloak
|  |  +- gown
|  |  |  +- fall
|  |  |  +- silkydress
|  |  |  +- summer
|  |  |  `- winter
|  |  +- halfcloak
|  |  +- halfmask
|  |  +- headband
|  |  +- heavyhood
|  |  +- hijab
|  |  +- hood
|  |  +- jesterhat
|  |  +- jestermask
|  |  +- jestershoes
|  |  +- jestertunick
|  |  +- jupon
|  |  +- jupon_short
|  |  +- leathershorts
|  |  +- leathertights
|  |  +- leathertrou
|  |  +- leathervest
|  |  +- lightdirecloak
|  |  +- loincloth
|  |  +- longcoat
|  |  +- longshirt
|  |  +- manabloom_crown
|  |  +- matricaria_crown
|  |  +- nobleboots
|  |  +- noblecoat
|  |  +- nun_habit
|  |  +- nunveil
|  |  +- nurseveil
|  |  +- papakha
|  |  +- paper_parasol
|  |  +- phys_robe
|  |  +- pipe
|  |  +- pipewestman
|  |  +- poncho
|  |  +- priestrobe
|  |  +- psicross
|  |  |  +- abyssor
|  |  |  +- astrata
|  |  |  +- baotha
|  |  |  +- decrepit
|  |  |  +- dendor
|  |  |  +- eora
|  |  |  +- graggar
|  |  |  +- gronnabyssor
|  |  |  +- gronnbaotha
|  |  |  +- gronndendor
|  |  |  +- gronngraggar
|  |  |  +- gronnmatthios
|  |  |  +- gronnzizo
|  |  |  +- malum
|  |  |  +- matthios
|  |  |  +- naledi
|  |  |  +- necra
|  |  |  +- noc
|  |  |  +- pestra
|  |  |  +- ravox
|  |  |  +- reform
|  |  |  +- undivided
|  |  |  +- xylix
|  |  |  `- zizo
|  |  +- ragmask
|  |  +- raincloak
|  |  +- ridercloak
|  |  +- ridingboots
|  |  +- robe
|  |  +- rosa_crown
|  |  +- rumaclanshoes
|  |  +- sailorjacket
|  |  +- sailorpants
|  |  +- sailorshirt
|  |  +- salvia_crown
|  |  +- sandals
|  |  +- scaledcloak
|  |  +- sexydress
|  |  +- shadowmask
|  |  +- shalal
|  |  +- shortboots
|  |  +- shortshirt
|  |  +- shroudblack
|  |  +- shroudscarlet
|  |  +- shroudwhite
|  |  +- silkanklets
|  |  +- silkbelt
|  |  +- silkbra
|  |  +- silkmask
|  |  +- skirt
|  |  +- sleevedtabard
|  |  +- slitteddress
|  |  +- smokingcap
|  |  +- spectacles
|  |  +- straplessdress
|  |  |  `- alt
|  |  +- strawhat
|  |  +- stripedtunic
|  |  +- surcoat
|  |  +- surcoatgoldenorder
|  |  +- surcoatgoldenorderast
|  |  +- surcoatgoldenorderuni
|  |  +- surcoatheavy
|  |  +- surcoatsilverorder
|  |  +- surcoatsilverorderast
|  |  +- surcoatsilverorderuni
|  |  +- tabard
|  |  +- tabardblack
|  |  +- tabardscarlet
|  |  +- tabardwhite
|  |  +- tarot_deck
|  |  +- thief_cloak
|  |  +- tights
|  |  +- tricorn
|  |  +- triumph_armorkit
|  |  +- triumph_armorkit_drow
|  |  +- triumph_astcross
|  |  +- triumph_bedroll
|  |  +- triumph_buttpack
|  |  +- triumph_circlet
|  |  +- triumph_foldtable
|  |  +- triumph_gdorpelring
|  |  +- triumph_gildedshirt
|  |  +- triumph_goldfullmask
|  |  +- triumph_goldfullmaskc
|  |  +- triumph_goldhalfmask
|  |  +- triumph_grenzhat
|  |  +- triumph_heavyboots
|  |  +- triumph_heavygloves
|  |  +- triumph_knife
|  |  +- triumph_ladycloak
|  |  +- triumph_lordcloak
|  |  +- triumph_lunchpouch
|  |  +- triumph_messkit
|  |  +- triumph_necklace
|  |  +- triumph_pristinedress
|  |  +- triumph_psycross
|  |  +- triumph_ring
|  |  +- triumph_royalsleeves
|  |  +- triumph_satchel
|  |  +- triumph_scabbardnoble
|  |  +- triumph_scabbardroyal
|  |  +- triumph_sheathnoble
|  |  +- triumph_sheathroyal
|  |  +- triumph_shortsatchel
|  |  +- triumph_signet
|  |  +- triumph_waterskin
|  |  +- triumph_weaponkit_ada
|  |  +- triumph_weaponkit_alloywhip
|  |  +- triumph_weaponkit_axe
|  |  +- triumph_weaponkit_axealt
|  |  +- triumph_weaponkit_dadao
|  |  +- triumph_weaponkit_estoc
|  |  +- triumph_weaponkit_fancymace
|  |  +- triumph_weaponkit_gdadao
|  |  +- triumph_weaponkit_greatval
|  |  +- triumph_weaponkit_hwi
|  |  +- triumph_weaponkit_ida
|  |  +- triumph_weaponkit_kaskara
|  |  +- triumph_weaponkit_krisdagger
|  |  +- triumph_weaponkit_ngombe
|  |  +- triumph_weaponkit_njoradagger
|  |  +- triumph_weaponkit_psy
|  |  +- triumph_weaponkit_rock
|  |  +- triumph_weaponkit_sabre
|  |  +- triumph_weaponkit_sengese
|  |  +- triumph_weaponkit_sword
|  |  +- triumph_weaponkit_tri
|  |  +- triumph_weaponkit_wide
|  |  +- triumph_weaponkit_wodao
|  |  +- triumph_zcross
|  |  +- trou
|  |  +- tunic
|  |  +- volfmantle
|  |  +- weatheredmask
|  |  +- wedding_band
|  |  +- wedding_band_ancient
|  |  +- wedding_band_bronze
|  |  +- wedding_band_gold
|  |  +- witchhat
|  |  |  `- old
|  |  +- wizhat
|  |  |  +- black
|  |  |  +- gen
|  |  |  +- green
|  |  |  +- red
|  |  |  `- yellow
|  |  +- woolencollar
|  |  +- wrappings
|  |  `- zcross_iron
|  +- loadout_menu
|  +- looping_sound
|  |  +- active_inside_ashstorm
|  |  +- active_outside_ashstorm
|  |  +- autosmither_work
|  |  +- blackmirror
|  |  +- blank
|  |  +- boatloop
|  |  +- boiling
|  |  +- boilloop
|  |  +- boneloop
|  |  +- clockloop
|  |  +- cog_loop
|  |  |  `- heavy
|  |  +- dmusloop
|  |  +- fireloop
|  |  +- flailswing
|  |  +- fliesloop
|  |  +- hail
|  |  +- indoor_hail
|  |  +- indoor_rain
|  |  +- instrument
|  |  +- invokeascendant
|  |  +- invokeevil
|  |  +- invokefire
|  |  +- invokegen
|  |  +- invokeholy
|  |  +- invokelightning
|  |  +- musloop
|  |  +- psydonmusicboxsound
|  |  +- rain
|  |  +- reverse_bear_trap
|  |  +- reverse_bear_trap_beep
|  |  +- snow
|  |  +- storm
|  |  +- streetlamp1
|  |  +- streetlamp2
|  |  +- streetlamp3
|  |  +- torchloop
|  |  +- waterwheel_loop
|  |  +- weak_inside_ashstorm
|  |  +- weak_outside_ashstorm
|  |  `- wind
|  +- magic_aspect
|  |  +- aegiscraft
|  |  +- artifice
|  |  +- augmentation
|  |  +- autowardry
|  |  +- battlewardry
|  |  +- cryomancy
|  |  +- displacement
|  |  +- exowardry
|  |  +- ferramancy
|  |  +- fulgurmancy
|  |  +- geomancy
|  |  +- hearthcraft
|  |  +- hex
|  |  +- illusion
|  |  +- kinesis
|  |  +- lesser_augmentation
|  |  +- lesser_kinesis
|  |  `- pyromancy
|  +- magic_item
|  |  +- greater
|  |  |  +- archery
|  |  |  +- frostveil
|  |  |  +- lifesteal
|  |  |  +- lightning
|  |  |  +- phoenixguard
|  |  |  +- returningweapon
|  |  |  +- void
|  |  |  `- woundclosing
|  |  +- mundane
|  |  |  +- holding
|  |  |  +- magnifiedlight
|  |  |  +- mining
|  |  |  +- nomagic
|  |  |  +- revealinglight
|  |  |  +- silver
|  |  |  +- woodcut
|  |  |  `- xylix
|  |  +- mythic
|  |  |  +- briarcurse
|  |  |  +- chaos_storm
|  |  |  +- freezing
|  |  |  +- infernalflame
|  |  |  `- rewind
|  |  `- superior
|  |     +- climbing
|  |     +- featherstep
|  |     +- fireresist
|  |     +- nightvision
|  |     +- smithing
|  |     +- thievery
|  |     `- unbreaking
|  +- map_adjustment
|  +- map_config
|  +- map_preloader
|  +- map_report
|  +- map_template
|  |  +- dungeon
|  |  |  +- entry
|  |  |  |  +- eastentrance
|  |  |  |  +- Northernentrance
|  |  |  |  `- tented
|  |  |  +- hallway
|  |  |  |  +- CaveTEast
|  |  |  |  +- CaveTWest
|  |  |  |  +- Crossjunction
|  |  |  |  +- Floortransition2
|  |  |  |  +- Hallwayeastwestplane
|  |  |  |  +- hallwesteastshort
|  |  |  |  +- HolyGrailHall
|  |  |  |  +- lampternhallway
|  |  |  |  +- longhall
|  |  |  |  +- LongHallStone
|  |  |  |  +- LongHallStone2
|  |  |  |  +- LongSliverStone
|  |  |  |  +- LongSliverStone2
|  |  |  |  +- LturnNorthEast
|  |  |  |  +- LturnSouthEast
|  |  |  |  +- LturnWestnorth
|  |  |  |  +- LturnWestSouth
|  |  |  |  +- Malphpiece2
|  |  |  |  +- Malphpiece3
|  |  |  |  +- Malphpiece5
|  |  |  |  +- Malphpiece9
|  |  |  |  +- MowPiece2
|  |  |  |  +- NormalHallway
|  |  |  |  +- North_Hallway
|  |  |  |  +- northminedhall
|  |  |  |  +- puzzle_dungeon_large
|  |  |  |  +- puzzle_dungeon_medium
|  |  |  |  +- puzzle_dungeon_small
|  |  |  |  +- right_left_floor_transition
|  |  |  |  +- SliceStone
|  |  |  |  +- SliceStone2
|  |  |  |  +- SmallCubeStone
|  |  |  |  +- SmallCubeStone2
|  |  |  |  +- smallhallns
|  |  |  |  +- SmallSliceStone
|  |  |  |  +- SmallSliceStone2
|  |  |  |  +- TinySliverStone
|  |  |  |  +- TinySliverStone2
|  |  |  |  +- TjunctionNorthSouthEast
|  |  |  |  +- TjunctionNorthWestEast
|  |  |  |  +- TjunctionWestNorthSouth
|  |  |  |  +- wild_dungeon_large
|  |  |  |  +- wild_dungeon_medium
|  |  |  |  `- wild_dungeon_small
|  |  |  +- rest
|  |  |  |  +- farm
|  |  |  |  +- largehallway
|  |  |  |  +- Malphpiece1
|  |  |  |  +- snackplatter
|  |  |  |  `- stingerpatch
|  |  |  `- room
|  |  |     +- acidfight
|  |  |     +- AcidMageTower
|  |  |     +- Allbutwesthall
|  |  |     +- Bathhouse_Dungeon
|  |  |     +- campnotherthing
|  |  |     +- cavecamp
|  |  |     +- DarkCorridors
|  |  |     +- drugden
|  |  |     +- dwelfhome
|  |  |     +- fightingpit
|  |  |     +- fightpit
|  |  |     +- ForgottenInn
|  |  |     +- goblincamp
|  |  |     +- GoblinInfestedJoint
|  |  |     +- Goonies
|  |  |     +- graveend
|  |  |     +- hctomb1
|  |  |     +- hctomb2
|  |  |     +- hctomb3
|  |  |     +- hctomb4
|  |  |     +- hctomb5
|  |  |     +- lava_large
|  |  |     +- lava_medium
|  |  |     +- lava_small
|  |  |     +- lavafort
|  |  |     +- magicanvil
|  |  |     +- Malphpiece4
|  |  |     +- queensretreat
|  |  |     +- rousecamp
|  |  |     +- sewer
|  |  |     +- sewers
|  |  |     +- skeletonroom
|  |  |     +- small_lab
|  |  |     +- SmallChurch
|  |  |     +- SmithRest
|  |  |     +- SteamCastle
|  |  |     +- TheatherOfSadism
|  |  |     +- Thelastbreath
|  |  |     `- TownRuins
|  |  +- ruin
|  |  `- unit_tests
|  +- mapGenerator
|  |  +- beach
|  |  +- bog
|  |  +- ca
|  |  |  `- maze
|  |  +- cave
|  |  |  +- lava
|  |  |  `- spider
|  |  +- decap
|  |  +- forest
|  |  +- massdelete
|  |  |  +- nomob
|  |  |  +- noturf
|  |  |  `- regen
|  |  +- mtn
|  |  +- repressurize
|  |  +- roguetownfield
|  |  `- underdark
|  +- mapGeneratorModule
|  |  +- beach
|  |  +- beachcoast
|  |  +- beachgrass
|  |  +- beachroad
|  |  +- beachsand
|  |  +- bog
|  |  +- boggrass
|  |  +- boggrassturf
|  |  +- bogroad
|  |  +- bogwater
|  |  +- border
|  |  +- bottomLayer
|  |  |  +- massdelete
|  |  |  |  +- leave_turfs
|  |  |  |  `- regeneration_delete
|  |  |  `- repressurize
|  |  +- cave
|  |  +- cavebeach
|  |  +- cavedirt
|  |  |  `- lava
|  |  +- cavespider
|  |  +- decapgrass
|  |  +- decaproad
|  |  +- decapsnow
|  |  +- denseLayer
|  |  +- forest
|  |  +- forestgrass
|  |  +- forestgrassturf
|  |  +- forestroad
|  |  +- mtn
|  |  +- roguetownfield
|  |  |  +- grass
|  |  |  `- road
|  |  +- roguetowngrass
|  |  +- splatterLayer
|  |  +- underdarkmud
|  |  `- underdarkstone
|  +- martial_art
|  +- migrant_assignment
|  +- migrant_pref
|  +- migrant_role
|  |  +- adventurer
|  |  +- assassin
|  |  +- bandit
|  |  +- dark_itinerant_knight
|  |  +- dark_itinerant_squire
|  |  +- fablefield
|  |  |  +- goliard
|  |  |  `- troubadour
|  |  +- gnoll
|  |  +- grenzel
|  |  |  +- bodyguard
|  |  |  +- envoy
|  |  |  `- priest
|  |  +- heartfelt
|  |  |  +- hand
|  |  |  +- knight
|  |  |  +- lord
|  |  |  `- retinue
|  |  +- kj_knight
|  |  +- kj_squire
|  |  +- lich
|  |  +- pilgrim
|  |  +- ranesheni
|  |  |  +- advisor
|  |  |  +- amirah
|  |  |  +- emir
|  |  |  `- janissary
|  |  +- runaway_prisoner
|  |  +- unbound_death_knight
|  |  +- unbound_spellblade
|  |  +- vampire
|  |  `- werewolf
|  +- migrant_wave
|  |  +- adventurer
|  |  +- adventurer_down_one
|  |  +- adventurer_down_three
|  |  +- adventurer_down_two
|  |  +- assassin
|  |  +- bandit
|  |  +- bandit_down_one
|  |  +- bandit_down_two
|  |  +- evil_knight
|  |  +- fablefield
|  |  +- fablefield_down_one
|  |  +- fablefield_down_two
|  |  +- gnolls
|  |  +- grenzel_envoy
|  |  +- grenzel_envoy_down_five
|  |  +- grenzel_envoy_down_four
|  |  +- grenzel_envoy_down_one
|  |  +- grenzel_envoy_down_three
|  |  +- grenzel_envoy_down_two
|  |  +- heartfelt
|  |  +- heartfelt_down_eight
|  |  +- heartfelt_down_five
|  |  +- heartfelt_down_four
|  |  +- heartfelt_down_nine
|  |  +- heartfelt_down_one
|  |  +- heartfelt_down_seven
|  |  +- heartfelt_down_six
|  |  +- heartfelt_down_ten
|  |  +- heartfelt_down_three
|  |  +- heartfelt_down_two
|  |  +- knightly_journey
|  |  +- knightly_journey_down_one
|  |  +- knightly_journey_down_two
|  |  +- lich
|  |  +- pilgrim
|  |  +- pilgrim_down_one
|  |  +- pilgrim_down_three
|  |  +- pilgrim_down_two
|  |  +- ranesheni_noble
|  |  +- ranesheni_noble_down_eight
|  |  +- ranesheni_noble_down_five
|  |  +- ranesheni_noble_down_four
|  |  +- ranesheni_noble_down_nine
|  |  +- ranesheni_noble_down_one
|  |  +- ranesheni_noble_down_seven
|  |  +- ranesheni_noble_down_six
|  |  +- ranesheni_noble_down_three
|  |  +- ranesheni_noble_down_two
|  |  +- runaway_prisoners
|  |  +- runaway_prisoners_down_one
|  |  +- runaway_prisoners_down_three
|  |  +- runaway_prisoners_down_two
|  |  +- unbound_death_knight
|  |  +- unbound_spellblade
|  |  +- vampire
|  |  `- werewolf
|  +- mind
|  +- mindlink
|  |  `- coven
|  +- mob_descriptor
|  |  +- age
|  |  +- body
|  |  |  +- athletic
|  |  |  +- average
|  |  |  +- bottomheavy
|  |  |  +- broadshoulder
|  |  |  +- bulky
|  |  |  +- burly
|  |  |  +- curvy
|  |  |  +- dainty
|  |  |  +- decrepit
|  |  |  +- gaunt
|  |  |  +- heavy
|  |  |  +- herculean
|  |  |  +- lanky
|  |  |  +- lean
|  |  |  +- lissome
|  |  |  +- muscular
|  |  |  +- pearshaped
|  |  |  +- petite
|  |  |  +- plump
|  |  |  +- pudgy
|  |  |  +- round
|  |  |  +- skeletal
|  |  |  +- slender
|  |  |  +- strongfat
|  |  |  +- thin
|  |  |  +- topheavy
|  |  |  +- twiggy
|  |  |  +- voluptuous
|  |  |  `- waspwaist
|  |  +- breasts
|  |  +- chitin
|  |  |  +- fine
|  |  |  +- hard
|  |  |  `- smooth
|  |  +- face
|  |  |  +- angular
|  |  |  +- broad
|  |  |  +- chiseled
|  |  |  +- chubby
|  |  |  +- delicate
|  |  |  +- disfigured
|  |  |  +- full
|  |  |  +- gaunt
|  |  |  +- mousy
|  |  |  +- rough
|  |  |  +- round
|  |  |  +- scarred
|  |  |  +- sharp
|  |  |  +- sleek
|  |  |  +- smooth
|  |  |  +- soft
|  |  |  +- tall
|  |  |  `- unremarkable
|  |  +- face_exp
|  |  |  +- affectionate
|  |  |  +- bitchy
|  |  |  +- bright
|  |  |  +- calm
|  |  |  +- cocky
|  |  |  +- cold
|  |  |  +- contemptous
|  |  |  +- coy
|  |  |  +- cutthroat
|  |  |  +- disinterested
|  |  |  +- fake
|  |  |  +- frustrated
|  |  |  +- genuine
|  |  |  +- haggard
|  |  |  +- humble
|  |  |  +- inquisitive
|  |  |  +- jaded
|  |  |  +- knowing
|  |  |  +- mocking
|  |  |  +- refined
|  |  |  +- salacious
|  |  |  +- smug
|  |  |  +- sour
|  |  |  +- spiteful
|  |  |  +- starry_eyed
|  |  |  +- stern
|  |  |  +- suave
|  |  |  +- suspicious
|  |  |  +- tender
|  |  |  `- warm
|  |  +- feathers
|  |  |  +- delicate
|  |  |  +- fine
|  |  |  +- frayed
|  |  |  +- soft
|  |  |  `- stiff
|  |  +- fur
|  |  |  +- bristly
|  |  |  +- coarse
|  |  |  +- dense
|  |  |  +- fluffy
|  |  |  +- lank
|  |  |  +- mangy
|  |  |  +- matted
|  |  |  +- plain
|  |  |  +- shaggy
|  |  |  +- short
|  |  |  +- silky
|  |  |  `- velvety
|  |  +- height
|  |  |  +- giant
|  |  |  +- middling
|  |  |  +- moderate
|  |  |  +- short
|  |  |  +- tall
|  |  |  +- tiny
|  |  |  `- towering
|  |  +- penis
|  |  +- prominent
|  |  |  +- adorable_presence
|  |  |  +- amphibian_features
|  |  |  +- aristocratic_haughtiness
|  |  |  +- avian_features
|  |  |  +- baggy_eye
|  |  |  +- bloodshot_eye
|  |  |  +- bovine_features
|  |  |  +- canine_features
|  |  |  +- cervine_features
|  |  |  +- chaste_mannerism
|  |  |  +- cleft_lip
|  |  |  +- clumsy
|  |  |  +- cold_gaze
|  |  |  +- crooked_nose
|  |  |  +- custom
|  |  |  |  +- one
|  |  |  |  `- two
|  |  |  +- deadfish_eye
|  |  |  +- dim_look
|  |  |  +- doting_presence
|  |  |  +- drooling
|  |  |  +- elaborate_tattoos
|  |  |  +- eloquent
|  |  |  +- enigmatic_tattoos
|  |  |  +- equine_features
|  |  |  +- extensive_scars
|  |  |  +- feline_features
|  |  |  +- ghastly_pale
|  |  |  +- ghoulish_appearance
|  |  |  +- haughty_atmosphere
|  |  |  +- hunched_over
|  |  |  +- hyaenidae_features
|  |  |  +- innocent_gaze
|  |  |  +- insectoid_features
|  |  |  +- intimidating_presence
|  |  |  +- lapine_features
|  |  |  +- lazy_eye
|  |  |  +- lizard_features
|  |  |  +- lordly_presence
|  |  |  +- marine_features
|  |  |  +- marsupial_features
|  |  |  +- mean_look
|  |  |  +- meek_presence
|  |  |  +- move_strange
|  |  |  +- none
|  |  |  +- physically_deformed
|  |  |  +- piercing_gaze
|  |  |  +- predatory_look
|  |  |  +- primate_features
|  |  |  +- prominent_bottom
|  |  |  +- prominent_chest
|  |  |  +- prominent_ears
|  |  |  +- prominent_jawline
|  |  |  +- prominent_potbelly
|  |  |  +- prominent_shoulders
|  |  |  +- prominent_thighs
|  |  |  +- promiscuous_mannerisms
|  |  |  +- ratty_hair
|  |  |  +- ritual_tattoos
|  |  |  +- rodent_features
|  |  |  +- slave_tattoos
|  |  |  +- thick_tail
|  |  |  +- tidy
|  |  |  +- tribal_tattoos
|  |  |  +- twitchy
|  |  |  +- unkempt
|  |  |  +- untrustworthy
|  |  |  +- vulpine_features
|  |  |  `- whimsy
|  |  +- scales
|  |  |  +- peeling
|  |  |  +- plain
|  |  |  +- plated
|  |  |  +- rough
|  |  |  `- smooth
|  |  +- skin
|  |  |  +- aged
|  |  |  +- ashen
|  |  |  +- diseased
|  |  |  +- dry
|  |  |  +- dusky
|  |  |  +- fine
|  |  |  +- hairy
|  |  |  +- irritated
|  |  |  +- normal
|  |  |  +- pockmarked
|  |  |  +- rugged
|  |  |  +- soft
|  |  |  +- sunkissed
|  |  |  `- wrinkled
|  |  +- stature
|  |  |  +- adventurer
|  |  |  +- archon
|  |  |  +- basterd
|  |  |  +- beguiler
|  |  |  +- blaggard
|  |  |  +- bookworm
|  |  |  +- brute
|  |  |  +- churl
|  |  |  +- creacher
|  |  |  +- creep
|  |  |  +- critter
|  |  |  +- cur
|  |  |  +- daredevil
|  |  |  +- degenerate
|  |  |  +- dignitary
|  |  |  +- dullard
|  |  |  +- fiend
|  |  |  +- fool
|  |  |  +- freek
|  |  |  +- gentleman
|  |  |  +- hag
|  |  |  +- hermit
|  |  |  +- highbrow
|  |  |  +- hustler
|  |  |  +- knave
|  |  |  +- lowlife
|  |  |  +- man
|  |  |  +- patriarch
|  |  |  +- plump
|  |  |  +- pupil
|  |  |  +- pushover
|  |  |  +- recluse
|  |  |  +- rogue
|  |  |  +- samaritan
|  |  |  +- savant
|  |  |  +- scholar
|  |  |  +- shitheel
|  |  |  +- slob
|  |  |  +- snob
|  |  |  +- socialite
|  |  |  +- soldier
|  |  |  +- stoic
|  |  |  +- stooge
|  |  |  +- thug
|  |  |  +- valiant
|  |  |  +- villain
|  |  |  +- vizier
|  |  |  +- wanderer
|  |  |  +- weerdoe
|  |  |  +- wench
|  |  |  +- wretch
|  |  |  `- zealot
|  |  +- testicles
|  |  +- trait
|  |  |  +- accursed
|  |  |  +- amber
|  |  |  +- aquatic
|  |  |  +- blessed
|  |  |  +- cadaverous
|  |  |  +- cerulean
|  |  |  +- clawed
|  |  |  +- crimson
|  |  |  +- dainty
|  |  |  +- disfigured
|  |  |  +- elven
|  |  |  +- emerald
|  |  |  +- fanged
|  |  |  +- feathered
|  |  |  +- feline
|  |  |  +- foreign
|  |  |  +- furred
|  |  |  +- giant
|  |  |  +- horned
|  |  |  +- lanky
|  |  |  +- limping
|  |  |  +- loutish
|  |  |  +- lupian
|  |  |  +- middling
|  |  |  +- moderate
|  |  |  +- mundane
|  |  |  +- rotten
|  |  |  +- rousley
|  |  |  +- scaly
|  |  |  +- short
|  |  |  +- snoutly
|  |  |  +- soggy
|  |  |  +- stout
|  |  |  +- tailed
|  |  |  +- tall
|  |  |  +- thin
|  |  |  +- tiny
|  |  |  +- towering
|  |  |  +- tusked
|  |  |  +- venardic
|  |  |  +- wide
|  |  |  `- zardish
|  |  +- vagina
|  |  `- voice
|  |     +- androgynous
|  |     +- booming
|  |     +- cheery
|  |     +- commanding
|  |     +- deep
|  |     +- dispassionate
|  |     +- doting
|  |     +- drawling
|  |     +- facetious
|  |     +- grave
|  |     +- gravelly
|  |     +- growly
|  |     +- honeyed
|  |     +- kind
|  |     +- lisping
|  |     +- melodic
|  |     +- monotone
|  |     +- nasal
|  |     +- ordinary
|  |     +- refined
|  |     +- shrill
|  |     +- sleepy
|  |     +- smoker
|  |     +- snide
|  |     +- soft
|  |     +- stilted
|  |     +- venomous
|  |     `- whiny
|  +- move_loop
|  |  +- has_target
|  |  |  +- dist_bound
|  |  |  |  +- move_away
|  |  |  |  `- move_to
|  |  |  +- force_move
|  |  |  +- move_towards
|  |  |  `- move_towards_budget
|  |  +- minecart
|  |  +- move
|  |  |  +- force
|  |  |  `- move_to
|  |  +- move_rand
|  |  `- move_to_rand
|  +- movement_detector
|  +- movement_packet
|  +- noticeboardpost
|  +- numbered_display
|  +- objective
|  |  +- aspirant
|  |  |  +- coup
|  |  |  |  +- one
|  |  |  |  +- three
|  |  |  |  `- two
|  |  |  `- loyal
|  |  |     `- one
|  |  +- assassinate
|  |  |  `- internal
|  |  +- bandit
|  |  +- brainwashing
|  |  +- build_zizo_shrine
|  |  +- capture
|  |  +- changeling_team_objective
|  |  +- consume_organs
|  |  +- contract
|  |  +- craft_shrine
|  |  +- create_abyssoids
|  |  +- custom
|  |  +- dark_itinerant
|  |  |  `- squire
|  |  +- debrain
|  |  +- delf
|  |  +- destroy
|  |  |  `- internal
|  |  +- dungeoneer
|  |  +- escape
|  |  |  +- escape_with_identity
|  |  |  `- prisoner
|  |  +- hoard_mammons
|  |  +- hug_beggar
|  |  +- improve_combat
|  |  +- improve_craft
|  |  +- listen_whispers
|  |  +- literacy
|  |  +- lux_extraction
|  |  +- maroon
|  |  +- marry
|  |  +- martyr
|  |  +- mock
|  |  |  +- monarch
|  |  |  `- noble
|  |  +- mutiny
|  |  +- nobility
|  |  +- prebel
|  |  +- proper_burial
|  |  +- protect
|  |  |  `- nonhuman
|  |  +- protect_object
|  |  +- punch_people
|  |  +- ravox_duel
|  |  +- release_fish
|  |  +- retainer
|  |  +- rotten_feast
|  |  +- snort_drugs
|  |  +- steal
|  |  +- steal_five_of_type
|  |  +- steal_items
|  |  +- survive
|  |  |  `- exist
|  |  +- tame_animal
|  |  +- taste_lux
|  |  +- torture
|  |  +- vampire
|  |  +- werewolf
|  |  `- wise_trees
|  +- objective_item
|  |  `- steal
|  |     `- rogue
|  |        +- crown
|  |        +- ledger
|  |        `- mkey
|  +- organ_dna
|  |  +- breasts
|  |  +- eyes
|  |  +- penis
|  |  +- testicles
|  |  `- vagina
|  +- outfit
|  |  +- job
|  |  |  `- roguetown
|  |  |     +- adventurer
|  |  |     |  +- cleric
|  |  |     |  +- crusader
|  |  |     |  +- spellblade
|  |  |     |  `- spellfist
|  |  |     +- bathworker
|  |  |     +- confessor
|  |  |     +- cook
|  |  |     |  `- basic
|  |  |     +- councillor
|  |  |     +- disciple
|  |  |     +- druid
|  |  |     +- gnoll_impure
|  |  |     +- greater_skeleton
|  |  |     |  +- lich
|  |  |     |  |  `- spellblade
|  |  |     |  `- necro
|  |  |     +- guildmaster
|  |  |     +- hag
|  |  |     +- hand
|  |  |     |  +- advisor
|  |  |     |  `- spymaster
|  |  |     +- inquisitor
|  |  |     +- knight
|  |  |     +- lady
|  |  |     +- lord
|  |  |     +- magician
|  |  |     +- manorguard
|  |  |     +- marshal
|  |  |     +- martyr
|  |  |     +- mercenary
|  |  |     |  +- atgervi
|  |  |     |  +- atgervishaman
|  |  |     |  +- blackoak_adept
|  |  |     |  +- desert_rider_almah
|  |  |     |  +- forlorn
|  |  |     |  +- gronn
|  |  |     |  +- gronnheavy
|  |  |     |  +- lirvanmerc
|  |  |     |  +- trollslayer
|  |  |     |  +- warscholar
|  |  |     |  +- warscholar_pontifex
|  |  |     |  `- warscholar_vizier
|  |  |     +- monk
|  |  |     +- physician
|  |  |     +- priest
|  |  |     +- psyaltrist
|  |  |     +- psydoniantemplar
|  |  |     +- seneschal
|  |  |     +- sergeant
|  |  |     +- sexton
|  |  |     |  `- gravetender
|  |  |     +- sojourner
|  |  |     +- squire
|  |  |     +- steward
|  |  |     +- suitor
|  |  |     +- tapster
|  |  |     +- templar
|  |  |     |  `- noc_spellblade
|  |  |     +- unbound_spellblade
|  |  |     +- vet
|  |  |     |  +- battlemaster
|  |  |     |  `- merc
|  |  |     +- veteran
|  |  |     +- wapprentice
|  |  |     |  `- spellblade
|  |  |     +- warden
|  |  |     +- watchman
|  |  |     `- wretch
|  |  |        +- ancient_spellblade
|  |  |        +- heretic
|  |  |        +- heretic_spellblade
|  |  |        +- heretic_spellfist
|  |  |        +- hereticspy
|  |  |        `- pariah
|  |  +- orcmarauder
|  |  +- orcravager
|  |  +- savageorc
|  |  +- savageorc2
|  |  +- treyliam
|  |  `- varedit
|  +- parsed_map
|  +- particle_weather
|  |  +- blood_rain_gentle
|  |  +- blood_rain_storm
|  |  +- fog
|  |  |  +- blood
|  |  |  +- darkness
|  |  |  +- necra
|  |  |  `- swamp
|  |  +- hail
|  |  +- leaves_gentle
|  |  +- leaves_storm
|  |  +- rain_gentle
|  |  +- rain_storm
|  |  +- sakura_gentle
|  |  +- sakura_storm
|  |  +- snow_gentle
|  |  `- snow_storm
|  +- PathNode
|  +- patron
|  |  +- divine
|  |  |  +- abyssor
|  |  |  +- astrata
|  |  |  +- dendor
|  |  |  +- eora
|  |  |  +- malum
|  |  |  +- necra
|  |  |  +- noc
|  |  |  +- pestra
|  |  |  +- ravox
|  |  |  +- undivided
|  |  |  `- xylix
|  |  +- godless
|  |  +- inhumen
|  |  |  +- baotha
|  |  |  +- graggar
|  |  |  +- matthios
|  |  |  `- zizo
|  |  +- mossmother
|  |  `- old_god
|  +- physiology
|  +- picture
|  +- plant_def
|  |  +- bush
|  |  |  +- berry
|  |  |  +- berry_poison
|  |  |  +- blackberry
|  |  |  +- eggplant
|  |  |  +- raspberry
|  |  |  +- strawberry
|  |  |  `- tomato
|  |  +- cabbage
|  |  +- carrot
|  |  +- coffee
|  |  +- fyritiusflower
|  |  +- garlick
|  |  +- manabloom
|  |  +- nut
|  |  +- oat
|  |  +- onion
|  |  +- pipeweed
|  |  +- poppy
|  |  +- potato
|  |  +- pumpkin
|  |  +- rice
|  |  +- sugarcane
|  |  +- sunflower
|  |  +- swampweed
|  |  +- tea
|  |  +- tree
|  |  |  +- apple
|  |  |  +- lemon
|  |  |  +- lime
|  |  |  +- pear
|  |  |  +- plum
|  |  |  `- tangerine
|  |  +- turnip
|  |  `- wheat
|  +- player_details
|  +- point
|  |  `- vector
|  |     `- processed
|  +- poll_option
|  +- poll_question
|  +- pollutant
|  |  +- food
|  |  |  +- apple_bread
|  |  |  +- apple_pie
|  |  |  +- baked_potato
|  |  |  +- berry_pie
|  |  |  +- biscuit
|  |  |  +- bookbread
|  |  |  +- bread
|  |  |  +- bun
|  |  |  +- cake
|  |  |  +- cheese_bun
|  |  |  +- cheese_cake
|  |  |  +- chocolate_bookbread
|  |  |  +- cooked_chicken
|  |  |  +- cooked_fish
|  |  |  +- cookies_caramel
|  |  |  +- cookies_chocolate
|  |  |  +- cookies_dragee
|  |  |  +- cookies_raisins
|  |  |  +- crab_pie
|  |  |  +- fish_pie
|  |  |  +- fried_bacon
|  |  |  +- fried_butter
|  |  |  +- fried_cabbage
|  |  |  +- fried_chicken
|  |  |  +- fried_crab
|  |  |  +- fried_crab_cake
|  |  |  +- fried_crow
|  |  |  +- fried_meat
|  |  |  +- fried_onion
|  |  |  +- fried_rat
|  |  |  +- fried_sausage
|  |  |  +- fried_shellfish
|  |  |  +- frosted_cake
|  |  |  +- fruity_bookbread
|  |  |  +- fruity_dottart
|  |  |  +- hardtack
|  |  |  +- honey_cake
|  |  |  +- meat_pie
|  |  |  +- muffin
|  |  |  +- pastry
|  |  |  +- pie_base
|  |  |  +- pot_pie
|  |  |  +- prezzel
|  |  |  +- pumpkin_pie
|  |  |  +- raisin_bread
|  |  |  +- roasted_seeds
|  |  |  +- toast
|  |  |  +- tomatoplate
|  |  |  +- tomatoplate_fish
|  |  |  +- tomatoplate_meat
|  |  |  +- tomatoplate_onion
|  |  |  +- tomatoplate_pear
|  |  |  +- tomatoplate_truffle
|  |  |  `- truffles
|  |  +- fragrance
|  |  |  +- cherry
|  |  |  +- cinnamon
|  |  |  +- frankincense
|  |  |  +- jasmine
|  |  |  +- lavender
|  |  |  +- mint
|  |  |  +- myrrh
|  |  |  +- pear
|  |  |  +- rose
|  |  |  +- sandalwood
|  |  |  +- strawberry
|  |  |  `- vanilla
|  |  +- metallic_scent
|  |  +- rot
|  |  `- smoke
|  +- pollution
|  +- position
|  +- preferences
|  +- progressbar
|  +- proximity_monitor
|  |  `- advanced
|  |     +- ai_aggro_tracking
|  |     +- ai_find_tracking
|  |     +- ai_target_tracking
|  |     +- debug
|  |     `- silence_field
|  +- qdel_item
|  +- quest
|  |  +- courier
|  |  +- kill
|  |  |  +- clearout
|  |  |  +- easy
|  |  |  +- outlaw
|  |  |  `- raid
|  |  `- retrieval
|  +- radial_menu
|  |  `- persistent
|  +- radio_frequency
|  +- reagent
|  |  +- acetaldehyde
|  |  +- acetone
|  |  +- acetone_oxide
|  |  +- allspice
|  |  +- aluminium
|  |  +- ammonia
|  |  +- ash
|  |  +- barbers_aid
|  |  +- berrypoison
|  |  +- blood
|  |  |  +- green
|  |  |  `- shitty
|  |  +- bloodacid
|  |  +- bluespace
|  |  +- bromine
|  |  +- buff
|  |  |  +- constitution
|  |  |  +- endurance
|  |  |  +- fortune
|  |  |  +- intelligence
|  |  |  +- perception
|  |  |  +- speed
|  |  |  +- strength
|  |  |  `- tri
|  |  +- carbon
|  |  +- carbondioxide
|  |  +- cellulose
|  |  +- charcoal
|  |  +- chlorine
|  |  +- colorful_reagent
|  |  |  `- powder
|  |  |     +- black
|  |  |     |  `- crayon
|  |  |     +- blue
|  |  |     |  `- crayon
|  |  |     +- green
|  |  |     |  `- crayon
|  |  |     +- invisible
|  |  |     +- orange
|  |  |     |  `- crayon
|  |  |     +- purple
|  |  |     |  `- crayon
|  |  |     +- red
|  |  |     |  `- crayon
|  |  |     +- white
|  |  |     |  `- crayon
|  |  |     `- yellow
|  |  |        `- crayon
|  |  +- concentrated_barbers_aid
|  |  +- consumable
|  |  |  +- Acoffee
|  |  |  +- acorn_powder
|  |  |  +- allspice
|  |  |  +- blackpepper
|  |  |  +- caffeine
|  |  |  |  +- coffee
|  |  |  |  +- coffee_spiced
|  |  |  |  +- tea
|  |  |  |  `- tea_spiced
|  |  |  +- chocolate
|  |  |  +- eggyolk
|  |  |  +- ethanol
|  |  |  |  +- ale
|  |  |  |  +- apfelweinheim
|  |  |  |  +- aqua_vitae
|  |  |  |  +- aurorian
|  |  |  |  +- avarmead
|  |  |  |  +- avarrice
|  |  |  |  +- baijiu
|  |  |  |  +- beer
|  |  |  |  +- blackberry
|  |  |  |  |  +- aged
|  |  |  |  |  `- delectable
|  |  |  |  +- blackgoat
|  |  |  |  +- brandy
|  |  |  |  |  +- pear
|  |  |  |  |  +- plum
|  |  |  |  |  +- strawberry
|  |  |  |  |  `- tangerine
|  |  |  |  +- butterhairs
|  |  |  |  +- cider
|  |  |  |  |  +- ambrosia
|  |  |  |  |  +- pear
|  |  |  |  |  `- strawberry
|  |  |  |  +- elfblue
|  |  |  |  +- elfred
|  |  |  |  +- fireleaf
|  |  |  |  +- gin
|  |  |  |  +- green
|  |  |  |  +- gronnmead
|  |  |  |  +- hagwoodbitter
|  |  |  |  +- huangjiu
|  |  |  |  +- jackberrywine
|  |  |  |  |  +- aged
|  |  |  |  |  `- delectable
|  |  |  |  +- jagdtrunk
|  |  |  |  +- kgunlager
|  |  |  |  +- kgunplum
|  |  |  |  +- kgunsake
|  |  |  |  +- kgunshochu
|  |  |  |  +- komuchisake
|  |  |  |  +- light
|  |  |  |  +- limoncello
|  |  |  |  +- luxwine
|  |  |  |  +- mead
|  |  |  |  |  `- spider
|  |  |  |  +- murkwine
|  |  |  |  +- nocshine
|  |  |  |  +- nred
|  |  |  |  +- onion
|  |  |  |  +- plum_wine
|  |  |  |  |  +- aged
|  |  |  |  |  `- delectable
|  |  |  |  +- raspberry
|  |  |  |  |  +- aged
|  |  |  |  |  `- delectable
|  |  |  |  +- redwine
|  |  |  |  +- ricespirit
|  |  |  |  +- ricewine
|  |  |  |  +- rtoper
|  |  |  |  +- rum
|  |  |  |  +- saigamilk
|  |  |  |  +- sazdistal
|  |  |  |  +- shejiu
|  |  |  |  +- sourwine
|  |  |  |  +- spicedwine
|  |  |  |  |  +- aged
|  |  |  |  |  `- delectable
|  |  |  |  +- spottedhen
|  |  |  |  +- stonebeards
|  |  |  |  +- tangerine
|  |  |  |  |  +- aged
|  |  |  |  |  `- delectable
|  |  |  |  +- voddena
|  |  |  |  +- whipwine
|  |  |  |  +- whitewine
|  |  |  |  +- wine
|  |  |  |  +- yaojiu
|  |  |  |  `- zagul
|  |  |  +- golden_calendula_tea
|  |  |  +- honey
|  |  |  +- milk
|  |  |  |  `- salted
|  |  |  +- nutriment
|  |  |  |  `- vitamin
|  |  |  +- oil
|  |  |  |  `- tallow
|  |  |  +- poppy_milk
|  |  |  +- pumpkinspice
|  |  |  +- sodiumchloride
|  |  |  +- soothing_valerian_tea
|  |  |  +- soup
|  |  |  |  +- apple
|  |  |  |  +- bone_broth
|  |  |  |  +- lemon
|  |  |  |  +- lime
|  |  |  |  +- pear
|  |  |  |  +- porridge
|  |  |  |  |  +- congee
|  |  |  |  |  +- frostedpudding
|  |  |  |  |  +- frycongee
|  |  |  |  |  +- fudgepudding
|  |  |  |  |  +- oatmeal
|  |  |  |  |  +- poisonfrostedpudding
|  |  |  |  |  +- pudding
|  |  |  |  |  +- thick
|  |  |  |  |  +- thickfrostedpudding
|  |  |  |  |  +- thickfudgepudding
|  |  |  |  |  +- thickpoisonfrostedpudding
|  |  |  |  |  `- thickpudding
|  |  |  |  +- purebutter
|  |  |  |  +- stew
|  |  |  |  |  +- aubergine_soup
|  |  |  |  |  +- bakedchicken
|  |  |  |  |  +- bakedthickchicken
|  |  |  |  |  +- berry
|  |  |  |  |  +- berry_poisoned
|  |  |  |  |  +- bisque
|  |  |  |  |  +- carrot_stew
|  |  |  |  |  +- cheese
|  |  |  |  |  +- cheeserice
|  |  |  |  |  +- chicken
|  |  |  |  |  +- cucumber_soup
|  |  |  |  |  +- egg
|  |  |  |  |  +- eggplant_soup
|  |  |  |  |  +- eggrice
|  |  |  |  |  +- evilfryfish
|  |  |  |  |  +- fish
|  |  |  |  |  +- frybisque
|  |  |  |  |  +- fryegg
|  |  |  |  |  +- fryfish
|  |  |  |  |  +- frymeat
|  |  |  |  |  +- frypork
|  |  |  |  |  +- fryrabbit
|  |  |  |  |  +- fryseafoodbroil
|  |  |  |  |  +- frysquash_soup
|  |  |  |  |  +- fryvolf
|  |  |  |  |  +- fryyucky
|  |  |  |  |  +- garlick_soup
|  |  |  |  |  +- hardtack
|  |  |  |  |  +- hardtacksalo
|  |  |  |  |  +- kingvolf
|  |  |  |  |  +- lavishaubergine_soup
|  |  |  |  |  +- lavishchicken
|  |  |  |  |  +- lavishfrybisque
|  |  |  |  |  +- lavishfryegg
|  |  |  |  |  +- lavishfryfish
|  |  |  |  |  +- lavishfrymeat
|  |  |  |  |  +- lavishfryrice
|  |  |  |  |  +- lavishfryseafoodbroil
|  |  |  |  |  +- meat
|  |  |  |  |  +- meatrice
|  |  |  |  |  +- nutty_stew
|  |  |  |  |  +- parmesan
|  |  |  |  |  +- pepperchicken
|  |  |  |  |  +- pepperfryfish
|  |  |  |  |  +- pepperfrymeat
|  |  |  |  |  +- plum_soup
|  |  |  |  |  +- pork
|  |  |  |  |  +- rabbit
|  |  |  |  |  +- saltmeat_stew
|  |  |  |  |  +- seafoodbroil
|  |  |  |  |  +- shrimprice
|  |  |  |  |  +- slop
|  |  |  |  |  +- squash_soup
|  |  |  |  |  +- survival_broth
|  |  |  |  |  +- thickcarrot_stew
|  |  |  |  |  +- thickcheese
|  |  |  |  |  +- thickchicken
|  |  |  |  |  +- thickcucumber_soup
|  |  |  |  |  +- thickfryegg
|  |  |  |  |  +- thickfrypork
|  |  |  |  |  +- thickhardtacksalo
|  |  |  |  |  +- thickparmesan
|  |  |  |  |  +- thickpork
|  |  |  |  |  +- thicksurvival_broth
|  |  |  |  |  +- tomato_soup
|  |  |  |  |  +- veggiefryfish
|  |  |  |  |  +- veggiefrymeat
|  |  |  |  |  +- veggiefryrabbit
|  |  |  |  |  +- veggiefryvolf
|  |  |  |  |  +- veggiethickchicken
|  |  |  |  |  +- viscera_broth
|  |  |  |  |  +- volf
|  |  |  |  |  `- yucky
|  |  |  |  +- tangerine_marmalade
|  |  |  |  `- veggie
|  |  |  |     +- cabbage
|  |  |  |     +- onion
|  |  |  |     +- potato
|  |  |  |     +- thickcabbage
|  |  |  |     +- thickfrycabbage
|  |  |  |     +- thickfryonion
|  |  |  |     +- thickfrypotato
|  |  |  |     +- thickonion
|  |  |  |     +- thickpotato
|  |  |  |     +- thickturnip
|  |  |  |     `- turnip
|  |  |  +- spiced_chocolate
|  |  |  `- sugar
|  |  |     `- molasses
|  |  +- copper
|  |  +- cryptobiolin
|  |  +- diethylamine
|  |  +- drug
|  |  |  +- abyss
|  |  |  +- apple
|  |  |  +- aranesp
|  |  |  +- blackberry
|  |  |  +- calendula
|  |  |  +- carrot
|  |  |  +- chocolate
|  |  |  +- crank
|  |  |  +- happiness
|  |  |  +- jacksberries
|  |  |  +- lime
|  |  |  +- mentha
|  |  |  +- methamphetamine
|  |  |  +- mushroomhallucinogen
|  |  |  +- nicotine
|  |  |  +- pumpup
|  |  |  +- salvia
|  |  |  +- space_drugs
|  |  |  +- strawberry
|  |  |  +- valeriana
|  |  |  `- ziggara
|  |  +- druqks
|  |  +- drying_agent
|  |  +- fermented_crab
|  |  +- fire_resist
|  |  +- floure
|  |  +- fluorine
|  |  +- fluorosurfactant
|  |  +- foaming_agent
|  |  +- frankenbrew
|  |  +- fuel
|  |  |  +- oil
|  |  |  `- unholywater
|  |  +- glitter
|  |  |  +- blue
|  |  |  +- pink
|  |  |  `- white
|  |  +- glycerol
|  |  +- gold
|  |  +- growthserum
|  |  +- hair_dye
|  |  +- hellwater
|  |  +- herozium
|  |  +- hydrogen
|  |  +- hydrogen_peroxide
|  |  +- impedrezene
|  |  +- infection
|  |  |  +- major
|  |  |  `- minor
|  |  +- iodine
|  |  +- iron
|  |  +- liquidgibs
|  |  +- lithium
|  |  +- lube
|  |  |  `- superlube
|  |  +- lye
|  |  +- medicine
|  |  |  +- antidote
|  |  |  +- healthpot
|  |  |  |  `- zarum
|  |  |  +- loversruin
|  |  |  +- manapot
|  |  |  +- omnizine
|  |  |  |  `- godblood
|  |  |  +- revival_fluid
|  |  |  +- salglu_solution
|  |  |  +- stampot
|  |  |  +- strong_antidote
|  |  |  +- stronghealth
|  |  |  +- strongmana
|  |  |  +- strongstam
|  |  |  `- vitae_essence
|  |  +- mercury
|  |  +- miasmagas
|  |  +- monkey_powder
|  |  +- moondust
|  |  +- moondust_purest
|  |  +- mulligan
|  |  +- mutationtoxin
|  |  +- nitrogen
|  |  +- nitrous_oxide
|  |  +- nitryl
|  |  +- organpoison
|  |  +- oxygen
|  |  +- ozium
|  |  +- pax
|  |  |  `- peaceborg
|  |  +- peaceborg
|  |  |  +- confuse
|  |  |  `- tire
|  |  +- pentaerythritol
|  |  +- phenol
|  |  +- phosphorus
|  |  +- plantnutriment
|  |  |  +- eznutriment
|  |  |  +- left4zednutriment
|  |  |  `- robustharvestnutriment
|  |  +- plastic_polymers
|  |  +- potassium
|  |  +- rogueacid
|  |  +- rotcure
|  |  +- royal_bee_jelly
|  |  +- saltpetre
|  |  +- sanctified_oil
|  |  +- serotrotium
|  |  +- silicon
|  |  +- silver
|  |  +- smart_foaming_agent
|  |  +- sodium
|  |  +- space_cleaner
|  |  |  +- ez_clean
|  |  |  `- sterilizine
|  |  +- spider_extract
|  |  +- spraytan
|  |  +- stable_plasma
|  |  +- stampoison
|  |  +- starsugar
|  |  +- stimulum
|  |  +- strongpoison
|  |  +- strongstampoison
|  |  +- sulfur
|  |  +- toxin
|  |  |  +- acid
|  |  |  |  +- fluacid
|  |  |  |  `- nitracid
|  |  |  +- amanitin
|  |  |  +- amatoxin
|  |  |  +- anacea
|  |  |  +- bad_food
|  |  |  +- bonehurtingjuice
|  |  |  +- bungotoxin
|  |  |  +- carpotoxin
|  |  |  +- chloralhydrate
|  |  |  +- coffeepowder
|  |  |  +- coniine
|  |  |  +- curare
|  |  |  +- cyanide
|  |  |  +- delayed
|  |  |  +- drow
|  |  |  +- fakebeer
|  |  |  +- fentanyl
|  |  |  +- formaldehyde
|  |  |  +- fyritiusnectar
|  |  |  +- ghoulpowder
|  |  |  +- heparin
|  |  |  +- histamine
|  |  |  +- initropidril
|  |  |  +- itching_powder
|  |  |  +- killersice
|  |  |  +- lexorin
|  |  |  +- lipolicide
|  |  |  +- mimesbane
|  |  |  +- mindbreaker
|  |  |  +- minttoxin
|  |  |  +- mutagen
|  |  |  +- mutetoxin
|  |  |  +- pancuronium
|  |  |  +- pestkiller
|  |  |  +- plantbgone
|  |  |  |  `- weedkiller
|  |  |  +- plasma
|  |  |  +- rotatium
|  |  |  +- slimejelly
|  |  |  +- sodium_thiopental
|  |  |  +- spewium
|  |  |  +- spidervenom_inert
|  |  |  +- spidervenom_paralytic
|  |  |  +- spore
|  |  |  +- spore_burning
|  |  |  +- sulfonal
|  |  |  +- teapowder
|  |  |  +- venom
|  |  |  `- zombiepowder
|  |  +- undeadash
|  |  +- uranium
|  |  |  `- radium
|  |  +- vampsolution
|  |  +- vitae
|  |  +- water
|  |  |  +- bathwater
|  |  |  +- blessed
|  |  |  +- cursed
|  |  |  +- gross
|  |  |  |  `- sewage
|  |  |  +- holywater
|  |  |  +- medicine
|  |  |  +- rosewater
|  |  |  +- rosewater_spiced
|  |  |  `- salty
|  |  `- yuck
|  +- reagents
|  +- recipe
|  +- recipe_wiki
|  +- rhythm_tracker
|  +- riddle
|  +- rmb_intent
|  |  +- aimed
|  |  +- feint
|  |  +- guard
|  |  +- riposte
|  |  +- special
|  |  +- strong
|  |  +- swift
|  |  `- weak
|  +- roguestock
|  |  +- bounty
|  |  |  `- treasure
|  |  +- import
|  |  |  +- alcoholset
|  |  |  +- blacksmith
|  |  |  +- bull
|  |  |  +- chicken
|  |  |  +- cow
|  |  |  +- crackers
|  |  |  +- craftsman
|  |  |  +- crossbow
|  |  |  +- farmequip
|  |  |  +- glasscrate
|  |  |  +- goat
|  |  |  +- goatmale
|  |  |  +- keyringsset
|  |  |  +- knight
|  |  |  +- manatarms
|  |  |  +- minecarttracks
|  |  |  +- planks
|  |  |  +- redpotion
|  |  |  +- rotationalnetwork
|  |  |  +- rotpotion
|  |  |  +- saigabuck
|  |  |  +- stoneblocks
|  |  |  +- tailor
|  |  |  +- warden
|  |  |  `- waterwheels
|  |  `- stockpile
|  |     +- apple
|  |     +- bass
|  |     +- blackberry
|  |     +- butter
|  |     +- cabbage
|  |     +- carp
|  |     +- carrot
|  |     +- cheese
|  |     +- cinnabar
|  |     +- clam
|  |     +- cloth
|  |     +- coal
|  |     +- cod
|  |     +- coffee
|  |     +- copper
|  |     +- crab
|  |     +- cucumber
|  |     +- cured
|  |     +- egg
|  |     +- eggplant
|  |     +- fat
|  |     +- fibers
|  |     +- fishfilet
|  |     +- fishmince
|  |     +- fur
|  |     +- garlick
|  |     +- glass
|  |     +- gold
|  |     +- grain
|  |     +- hide
|  |     +- iron
|  |     +- jacksberry
|  |     +- lemon
|  |     +- lime
|  |     +- lobster
|  |     +- meat
|  |     +- oat
|  |     +- onion
|  |     +- pear
|  |     +- plum
|  |     +- poppy
|  |     +- pork
|  |     +- potato
|  |     +- poultry
|  |     +- pumpkin
|  |     +- rabbit
|  |     +- raspberry
|  |     +- rice
|  |     +- rocknut
|  |     +- salmon
|  |     +- salt
|  |     +- shrimp
|  |     +- silk
|  |     +- silver
|  |     +- sole
|  |     +- stone
|  |     +- strawberry
|  |     +- sugar
|  |     +- tallow
|  |     +- tangerine
|  |     +- tea
|  |     +- tin
|  |     +- tomato
|  |     +- turnip
|  |     `- wood
|  +- rotation_network
|  +- round_event
|  |  +- animal_migration
|  |  |  +- hostile
|  |  |  `- passive
|  |  +- antagonist
|  |  |  `- solo
|  |  |     +- aspirants
|  |  |     +- bandits
|  |  |     +- dreamwalker
|  |  |     +- lich
|  |  |     +- rebel
|  |  |     +- vampire
|  |  |     +- vampires_and_werewolves
|  |  |     `- werewolf
|  |  +- collapsing_earth
|  |  +- deadite_migration
|  |  |  `- deadite
|  |  +- ghost_role
|  |  +- gobinvade
|  |  +- haunts
|  |  +- lightsout
|  |  +- migrant_wave
|  |  +- rogue
|  |  |  `- skeleton_siege
|  |  +- skellyinvade
|  |  +- skellysiege
|  |  `- worldsiege
|  +- round_event_control
|  |  +- abyssor_fish_release
|  |  +- abyssor_rage
|  |  +- antagonist
|  |  |  +- migrant_wave
|  |  |  |  +- assassins
|  |  |  |  +- banditsorgnolls
|  |  |  |  +- evil_knight
|  |  |  |  +- gnolls
|  |  |  |  +- lich
|  |  |  |  +- unbound_death_knight
|  |  |  |  +- unbound_spellblade
|  |  |  |  +- vampire
|  |  |  |  `- werewolf
|  |  |  `- solo
|  |  |     +- aspirants
|  |  |     +- assassins
|  |  |     +- bandits
|  |  |     +- dreamwalker
|  |  |     |  `- roundstart
|  |  |     +- lich
|  |  |     +- masquerade
|  |  |     +- rebel
|  |  |     +- vampires
|  |  |     +- vampires_and_werewolves
|  |  |     `- werewolf
|  |  +- astrata_grandeur
|  |  +- astrata_nobility
|  |  +- baotha_lux_tasting
|  |  +- baotha_revelry
|  |  +- baotha_snorting
|  |  +- collapsing_earth
|  |  +- create_abyssoids
|  |  +- crop_growth
|  |  +- dead_whispers
|  |  +- deadite_animal_migration
|  |  +- dendor_fertility
|  |  +- dendor_ire
|  |  +- dendor_taming
|  |  +- dendor_trees
|  |  +- dendor_vines_boon
|  |  +- dendor_vines_malus
|  |  +- eora_compassion
|  |  +- fishing_boon
|  |  +- fishing_malus
|  |  +- gobinvade
|  |  +- graggar_culling
|  |  +- graggar_organs
|  |  +- graggar_punch
|  |  +- haunts
|  |  +- herb_growth
|  |  +- herb_spread
|  |  +- herb_wither
|  |  +- hostile_animal_migration
|  |  +- lightsout
|  |  +- malum_craft_skills
|  |  +- malum_crafting
|  |  +- malum_diligence
|  |  +- matthios_fingers
|  |  +- matthios_hoard
|  |  +- matthios_theft
|  |  +- necra_burials
|  |  +- necra_requiem
|  |  +- noc_literacy
|  |  +- passive_animal_migration
|  |  +- pestra_lux
|  |  +- pestra_mercy
|  |  +- pestra_rotten_feast
|  |  +- price_fluctuation
|  |  +- ravox_combat
|  |  +- ravox_duel
|  |  +- ravox_resolve
|  |  +- retainer_recruitment
|  |  +- rogue
|  |  |  `- skeleton_siege
|  |  +- roundstart
|  |  +- schism_within_ten
|  |  +- skellyinvade
|  |  +- skellysiege
|  |  +- spacevine
|  |  +- town_fire
|  |  +- trade_request
|  |  +- vines
|  |  +- wild_crops
|  |  +- wizard
|  |  +- worldsiege
|  |  |  `- goblin
|  |  +- xylix_mocking
|  |  +- xylix_mocking_nobles
|  |  +- zizo_defilement
|  |  +- zizo_pet_cementery
|  |  +- zizo_shrines
|  |  `- zizo_torture
|  +- runeritual
|  |  +- binding
|  |  |  +- elemental_t1
|  |  |  +- elemental_t2
|  |  |  +- elemental_t3
|  |  |  +- elemental_t4
|  |  |  +- fae_t1
|  |  |  +- fae_t2
|  |  |  +- fae_t3
|  |  |  +- fae_t4
|  |  |  +- infernal_t1
|  |  |  +- infernal_t2
|  |  |  +- infernal_t3
|  |  |  +- infernal_t4
|  |  |  `- void_dragon
|  |  +- borrowed_madness
|  |  +- enchanting
|  |  |  +- archery
|  |  |  +- briars
|  |  |  +- chaosstorm
|  |  |  +- climbing
|  |  |  +- featherstep
|  |  |  +- fireresist
|  |  |  +- freeze
|  |  |  +- frostveil
|  |  |  +- infernalflame
|  |  |  +- lifesteal
|  |  |  +- lightning
|  |  |  +- magnifiedlight
|  |  |  +- mining
|  |  |  +- nightvision
|  |  |  +- returningweapon
|  |  |  +- revealinglight
|  |  |  +- rewind
|  |  |  +- smithing
|  |  |  +- storage
|  |  |  +- thievery
|  |  |  +- unbreaking
|  |  |  +- voidtouched
|  |  |  +- woodcut
|  |  |  `- xylix
|  |  +- joybringer
|  |  +- lesser_wolf
|  |  +- other
|  |  |  `- wall
|  |  |     +- t2
|  |  |     `- t3
|  |  +- ravox_vow
|  |  +- silver_blessing
|  |  +- spider_kinship
|  |  `- summoning
|  |     `- leyline_encounter
|  |        +- earthen_t1
|  |        +- earthen_t2
|  |        +- earthen_t3
|  |        +- earthen_t4
|  |        +- fae_t1
|  |        +- fae_t2
|  |        +- fae_t3
|  |        +- fae_t4
|  |        +- infernal_t1
|  |        +- infernal_t2
|  |        +- infernal_t3
|  |        +- infernal_t4
|  |        +- leyline_t2
|  |        +- void_dragon
|  |        `- void_t2
|  +- saymode
|  |  `- vocalcords
|  +- scheduled_event
|  +- schizohelp
|  +- SDQL2_query
|  +- SDQL_parser
|  +- sex_action
|  |  +- masturbate
|  |  |  +- anus
|  |  |  +- breasts
|  |  |  +- other
|  |  |  |  +- anus
|  |  |  |  +- clit
|  |  |  |  +- godjob
|  |  |  |  +- godjob_anal
|  |  |  |  +- godjob_vagina
|  |  |  |  +- magejob
|  |  |  |  +- magejob_anal
|  |  |  |  +- magejob_vagina
|  |  |  |  +- penis
|  |  |  |  +- tailjob
|  |  |  |  +- tailjob_anal
|  |  |  |  +- tailjob_oral
|  |  |  |  +- tailjob_vagina
|  |  |  |  `- vagina
|  |  |  +- penis
|  |  |  +- penis_over
|  |  |  +- vagina
|  |  |  `- vagina_finger
|  |  +- miscellaneous
|  |  |  +- facesitting
|  |  |  +- facesitting_anal
|  |  |  +- frotting
|  |  |  +- grind_body
|  |  |  +- rub_body
|  |  |  +- rub_ears
|  |  |  +- spanking
|  |  |  `- tonguebath
|  |  +- oral
|  |  |  +- armpit_nuzzle
|  |  |  +- blowjob
|  |  |  +- crotch_nuzzle
|  |  |  +- cunnilingus
|  |  |  +- foot_lick
|  |  |  +- kissing
|  |  |  +- lick_ears
|  |  |  +- rimming
|  |  |  +- suck_balls
|  |  |  `- suck_nipples
|  |  +- scissoring
|  |  +- sex
|  |  |  +- anal
|  |  |  |  `- double
|  |  |  +- boobjob
|  |  |  +- double_penetration
|  |  |  +- footjob
|  |  |  +- other
|  |  |  |  +- anal
|  |  |  |  +- boobjob
|  |  |  |  +- boobsmother
|  |  |  |  +- footjob
|  |  |  |  +- footsmother
|  |  |  |  +- thighjob
|  |  |  |  `- vagina
|  |  |  +- slit
|  |  |  |  `- double
|  |  |  +- thighjob
|  |  |  +- throat
|  |  |  |  `- double
|  |  |  `- vaginal
|  |  |     `- double
|  |  `- toy
|  |     +- anus
|  |     +- oral
|  |     +- other
|  |     |  +- anus
|  |     |  +- oral
|  |     |  `- vagina
|  |     `- vagina
|  +- sex_session
|  +- sex_session_lock
|  +- signal
|  +- skill
|  |  +- combat
|  |  |  +- axes
|  |  |  +- bows
|  |  |  +- crossbows
|  |  |  +- knives
|  |  |  +- maces
|  |  |  +- polearms
|  |  |  +- shields
|  |  |  +- slings
|  |  |  +- staves
|  |  |  +- swords
|  |  |  +- unarmed
|  |  |  +- whipsflails
|  |  |  `- wrestling
|  |  +- craft
|  |  |  +- alchemy
|  |  |  +- armorsmithing
|  |  |  +- blacksmithing
|  |  |  +- carpentry
|  |  |  +- ceramics
|  |  |  +- cooking
|  |  |  +- crafting
|  |  |  +- engineering
|  |  |  +- masonry
|  |  |  +- sewing
|  |  |  +- smelting
|  |  |  +- tanning
|  |  |  +- traps
|  |  |  `- weaponsmithing
|  |  +- labor
|  |  |  +- butchering
|  |  |  +- farming
|  |  |  +- fishing
|  |  |  +- lumberjacking
|  |  |  `- mining
|  |  +- magic
|  |  |  +- arcane
|  |  |  +- blood
|  |  |  +- druidic
|  |  |  `- holy
|  |  `- misc
|  |     +- athletics
|  |     +- climbing
|  |     +- lockpicking
|  |     +- medicine
|  |     +- music
|  |     +- reading
|  |     +- riding
|  |     +- sneaking
|  |     +- stealing
|  |     +- swimming
|  |     `- tracking
|  +- skill_holder
|  +- sleep_adv
|  +- song
|  |  `- handheld
|  +- songbook_ui
|  +- sortInstance
|  +- soullink
|  |  +- multisharer
|  |  `- shapeshift
|  +- sound_group
|  |  +- fire_loop
|  |  +- instruments
|  |  `- torches
|  +- space_level
|  +- space_transition_point
|  +- spatial_grid_cell
|  +- spawners_menu
|  +- special_intent
|  |  +- another_example_cast
|  |  +- axe_swing
|  |  +- coat_blade
|  |  +- dagger_dash
|  |  +- flail_sweep
|  |  +- greatsword_swing
|  |  +- ground_smash
|  |  +- ignite_dagger
|  |  +- limbguard
|  |  +- martyr_blazing_sweep
|  |  +- martyr_blazing_sweep_sword
|  |  +- martyr_blazing_trident
|  |  +- martyr_volcano_slam
|  |  +- permafrost
|  |  +- piercing_lunge
|  |  +- polearm_backstep
|  |  +- rectangle
|  |  |  `- example_rect
|  |  +- shin_swipe
|  |  +- side_sweep
|  |  +- upper_cut
|  |  `- whip_coil
|  +- special_trait
|  |  +- arsonist
|  |  +- atheism
|  |  +- atrophy
|  |  +- backproblems
|  |  +- bad_week
|  |  +- beautiful
|  |  +- bleublood
|  |  +- bookworm
|  |  +- bounty
|  |  +- civilizedbarbarian
|  |  +- corn_fed
|  |  +- cunning_linguist
|  |  +- curseofcain
|  |  +- deadened
|  |  +- duelist
|  |  +- eagle_eyed
|  |  +- gourmand
|  |  +- hussite
|  |  +- illicit_merchant
|  |  +- jesterphobia
|  |  +- languagesavant
|  |  +- latentmagic
|  |  +- lazy
|  |  +- lightstep
|  |  +- limpdick
|  |  +- lucky
|  |  +- maniac_awoken
|  |  +- mastercraftsmen
|  |  +- mule
|  |  +- my_precious
|  |  +- night_owl
|  |  +- nightvision
|  |  +- nimrod
|  |  +- nopouch
|  |  +- nothing
|  |  +- nude_sleeper
|  |  +- outlaw
|  |  +- pineapple
|  |  +- psydons_rider
|  |  +- punkprincess
|  |  +- richpouch
|  |  +- schizo_ambience
|  |  +- screenshake
|  |  +- spring_in_my_step
|  |  +- swift
|  |  +- thickskin
|  |  +- thief
|  |  +- tolerant
|  |  +- unlucky
|  |  +- value
|  |  +- vengantbum
|  |  `- wild_night
|  +- species
|  |  +- aasimar
|  |  +- akula
|  |  +- anthromorph
|  |  +- anthromorphsmall
|  |  +- construct
|  |  |  `- metal
|  |  +- demihuman
|  |  +- dendormole
|  |  +- dracon
|  |  +- dullahan
|  |  +- dwarf
|  |  |  +- gnome
|  |  |  `- mountain
|  |  +- elf
|  |  |  +- dark
|  |  |  |  `- raider
|  |  |  +- sun
|  |  |  `- wood
|  |  +- gnoll
|  |  +- goblin
|  |  |  +- cave
|  |  |  +- hell
|  |  |  +- moon
|  |  |  `- sea
|  |  +- goblinp
|  |  +- hag_true_form
|  |  +- halforc
|  |  +- human
|  |  |  +- halfelf
|  |  |  `- northern
|  |  +- kobold
|  |  +- lizardfolk
|  |  +- lupian
|  |  +- mirecrawler
|  |  +- moth
|  |  +- orc
|  |  +- shapebear
|  |  +- shapecabbit
|  |  +- shapecat
|  |  +- shapefox
|  |  +- shapesaiga
|  |  +- shapespider
|  |  +- shapewolf
|  |  +- tabaxi
|  |  +- tieberian
|  |  +- vulpkanin
|  |  `- werewolf
|  +- sprite_accessory
|  |  +- accessory
|  |  |  +- choker
|  |  |  +- chokere
|  |  |  +- earrings
|  |  |  |  +- em
|  |  |  |  `- sil
|  |  |  +- eyepierce
|  |  |  |  `- alt
|  |  |  +- harlequin
|  |  |  `- warpaint
|  |  +- antenna
|  |  |  `- moth
|  |  |     +- burnt_off
|  |  |     +- deathhead
|  |  |     +- firewatch
|  |  |     +- gothic
|  |  |     +- jungle
|  |  |     +- lovers
|  |  |     +- moonfly
|  |  |     +- mothra
|  |  |     +- oakworm
|  |  |     +- plain
|  |  |     +- poison
|  |  |     +- ragged
|  |  |     +- reddish
|  |  |     +- regal
|  |  |     +- royal
|  |  |     +- whitefly
|  |  |     `- witchwing
|  |  +- back_feature
|  |  +- brand
|  |  |  `- vampire_seal
|  |  +- breasts
|  |  |  +- pair
|  |  |  +- quad
|  |  |  `- sextuple
|  |  +- crests
|  |  |  +- bronzer
|  |  |  +- ironc
|  |  |  +- rubyb
|  |  |  `- steelt
|  |  +- ears
|  |  |  +- antenna_fuzzball1
|  |  |  +- antenna_fuzzball2
|  |  |  +- antenna_simple1
|  |  |  +- antenna_simple2
|  |  |  +- antenna_simple3
|  |  |  +- antenna_simple4
|  |  |  +- axolotl
|  |  |  +- bat
|  |  |  +- bear
|  |  |  +- big
|  |  |  |  +- acrador_long
|  |  |  |  +- acrador_short
|  |  |  |  +- rabbit_large
|  |  |  |  `- sandfox_large
|  |  |  +- bigwolf
|  |  |  +- bigwolf_inner
|  |  |  +- bunny
|  |  |  +- bunny_long
|  |  |  +- bunny_perky
|  |  |  +- cat
|  |  |  +- cat_big
|  |  |  +- cat_normal
|  |  |  +- cobrahood
|  |  |  +- cobrahoodears
|  |  |  +- cow
|  |  |  +- curled
|  |  |  +- deer
|  |  |  +- eevee
|  |  |  +- elephant
|  |  |  +- elf
|  |  |  +- elf_short
|  |  |  +- elfw
|  |  |  +- fennec
|  |  |  +- fish
|  |  |  +- fox
|  |  |  +- goblin
|  |  |  +- goblin_alt
|  |  |  +- goblin_small
|  |  |  +- halforc
|  |  |  +- husky
|  |  |  +- jellyfish
|  |  |  +- kangaroo
|  |  |  +- lab
|  |  |  +- lunasune
|  |  |  +- lynx
|  |  |  +- miqote
|  |  |  +- mouse
|  |  |  +- murid
|  |  |  +- nosferatu
|  |  |  +- otie
|  |  |  +- pede
|  |  |  +- perky
|  |  |  +- possum
|  |  |  +- rabbit
|  |  |  +- raccoon
|  |  |  +- sabresune
|  |  |  +- sergal
|  |  |  +- shark
|  |  |  +- skunk
|  |  |  +- squirrel
|  |  |  +- vulp
|  |  |  +- wolf
|  |  |  `- zorzor
|  |  +- eyes
|  |  |  +- humanoid
|  |  |  +- humanoid_cyber
|  |  |  +- humanoid_glow
|  |  |  `- moth
|  |  +- face_detail
|  |  |  +- brows
|  |  |  |  `- dark
|  |  |  +- burneye_l
|  |  |  +- burneye_r
|  |  |  +- burnface_l
|  |  |  +- burnface_r
|  |  |  +- deadeye_l
|  |  |  +- deadeye_r
|  |  |  +- mangled
|  |  |  +- scar
|  |  |  +- scarhead
|  |  |  +- scart
|  |  |  +- slashedeye_l
|  |  |  +- slashedeye_r
|  |  |  +- tattoo_eye_both
|  |  |  +- tattoo_eye_l
|  |  |  +- tattoo_eye_r
|  |  |  `- tattoo_lips
|  |  +- frills
|  |  |  +- aquatic
|  |  |  +- aquaticdualcolor
|  |  |  +- big
|  |  |  +- cobrahood
|  |  |  +- cobrahood_ears
|  |  |  +- divinity
|  |  |  +- earlike
|  |  |  +- earlike_angled
|  |  |  +- earlike_thick
|  |  |  +- horns
|  |  |  +- horns_double
|  |  |  +- short
|  |  |  +- shortdualcolor
|  |  |  +- simple
|  |  |  +- simpledualcolor
|  |  |  +- split
|  |  |  +- split_big
|  |  |  `- split_slim
|  |  +- hair
|  |  |  +- facial
|  |  |  |  +- abe
|  |  |  |  +- brokenman
|  |  |  |  +- burns
|  |  |  |  +- chaplin
|  |  |  |  +- chinlessbeard
|  |  |  |  +- chinstrap
|  |  |  |  +- croppedfullbeard
|  |  |  |  +- dwarf
|  |  |  |  +- elvis
|  |  |  |  +- fiveoclock
|  |  |  |  +- fiveoclockm
|  |  |  |  +- fiveoclockmoustache
|  |  |  |  +- fu
|  |  |  |  +- fullbeard
|  |  |  |  +- gt
|  |  |  |  +- hip
|  |  |  |  +- hogan
|  |  |  |  +- jensen
|  |  |  |  +- knightly
|  |  |  |  +- longbeard
|  |  |  |  +- manly
|  |  |  |  +- martialartist
|  |  |  |  +- moonshiner
|  |  |  |  +- moustache
|  |  |  |  +- mutton
|  |  |  |  +- muttonmus
|  |  |  |  +- neckbeard
|  |  |  |  +- pencilstache
|  |  |  |  +- pipe
|  |  |  |  +- selleck
|  |  |  |  +- sevenoclock
|  |  |  |  +- sevenoclockm
|  |  |  |  +- shaved
|  |  |  |  +- sideburn
|  |  |  |  +- smallstache
|  |  |  |  +- stubble
|  |  |  |  +- threeoclock
|  |  |  |  +- vandyke
|  |  |  |  +- viking
|  |  |  |  +- vlongbeard
|  |  |  |  +- volaju
|  |  |  |  +- vox
|  |  |  |  |  +- beard
|  |  |  |  |  +- colonel
|  |  |  |  |  +- fu
|  |  |  |  |  `- neck
|  |  |  |  +- walrus
|  |  |  |  `- watson
|  |  |  `- head
|  |  |     +- adventurer
|  |  |     +- afro
|  |  |     +- afro2
|  |  |     +- afro_large
|  |  |     +- alsoprotagonist
|  |  |     +- amazon
|  |  |     +- amazon_f
|  |  |     +- antenna
|  |  |     +- archivist
|  |  |     +- astolfo
|  |  |     +- badlycut
|  |  |     +- bald
|  |  |     +- baldfade
|  |  |     +- balding
|  |  |     +- barbarian_f
|  |  |     +- barmaid
|  |  |     +- baum
|  |  |     +- beartails_f
|  |  |     +- bedhead
|  |  |     +- bedhead2
|  |  |     +- bedhead3
|  |  |     +- bedheadlong
|  |  |     +- beehive
|  |  |     +- beehive2
|  |  |     +- berserker
|  |  |     +- bigpompadour
|  |  |     +- bishonen
|  |  |     +- bob
|  |  |     +- bob2
|  |  |     +- bob3
|  |  |     +- bob4
|  |  |     +- bob_f
|  |  |     +- bob_rt
|  |  |     +- bobcurl
|  |  |     +- boddicker
|  |  |     +- bog
|  |  |     +- boss
|  |  |     +- bowlcut
|  |  |     +- bowlcut2
|  |  |     +- braid
|  |  |     +- braided
|  |  |     +- braided_sidetail
|  |  |     +- braidtail
|  |  |     +- bubblebraids
|  |  |     +- bubblebraids_v2
|  |  |     +- bun
|  |  |     +- bun2
|  |  |     +- bun3
|  |  |     +- buns_f
|  |  |     +- bushy
|  |  |     +- bushy_alt
|  |  |     +- business
|  |  |     +- business2
|  |  |     +- business3
|  |  |     +- business4
|  |  |     +- buzz
|  |  |     +- casual
|  |  |     +- cavehead
|  |  |     +- chair_manbun
|  |  |     +- chair_ponytail6
|  |  |     +- cia
|  |  |     +- coffeehouse
|  |  |     +- combover
|  |  |     +- comet
|  |  |     +- conscript
|  |  |     +- cornrowbraid
|  |  |     +- cornrowbun
|  |  |     +- cornrowdualtail
|  |  |     +- cornrows1
|  |  |     +- cornrows2
|  |  |     +- cotton
|  |  |     +- cottonalt
|  |  |     +- countryponytail
|  |  |     +- countryponytailalt
|  |  |     +- courtier
|  |  |     +- crew
|  |  |     +- curls
|  |  |     +- curly_f
|  |  |     +- curtains
|  |  |     +- cut
|  |  |     +- damsel
|  |  |     +- dandpompadour
|  |  |     +- darkknight
|  |  |     +- dave
|  |  |     +- dawn
|  |  |     +- devillock
|  |  |     +- diagonalbangs
|  |  |     +- dome
|  |  |     +- doublebun
|  |  |     +- dreadlocks
|  |  |     +- dreadlocks_long
|  |  |     +- dreadlocksmessy
|  |  |     +- drillhair
|  |  |     +- drillhairextended
|  |  |     +- druid
|  |  |     +- emma
|  |  |     +- emo
|  |  |     +- emo2
|  |  |     +- emo_long
|  |  |     +- emofringe
|  |  |     +- emperor
|  |  |     +- empress
|  |  |     +- empress_f
|  |  |     +- fancy_elf
|  |  |     +- fancy_elf_f
|  |  |     +- father
|  |  |     +- fatherless
|  |  |     +- fatherless2
|  |  |     +- fatherless_elf_f
|  |  |     +- feather
|  |  |     +- female
|  |  |     +- flair
|  |  |     +- flattop
|  |  |     +- flattop_big
|  |  |     +- flow_hair
|  |  |     +- fluffball
|  |  |     +- fluffy
|  |  |     +- fluffylong
|  |  |     +- fluffyshort
|  |  |     +- foreigner
|  |  |     +- forelock
|  |  |     +- forester
|  |  |     +- forged
|  |  |     +- forsaken
|  |  |     +- fringetail
|  |  |     +- front_braid
|  |  |     +- gelled
|  |  |     +- gentle
|  |  |     +- ghast
|  |  |     +- glamourh
|  |  |     +- gloomy
|  |  |     +- gloomy_long
|  |  |     +- gloomy_medium
|  |  |     +- gloomy_short
|  |  |     +- gloomylong
|  |  |     +- gnomish_f
|  |  |     +- graceful
|  |  |     +- grenzelcut
|  |  |     +- gronnbraid
|  |  |     +- grumpy_f
|  |  |     +- hairfre
|  |  |     +- halfbang
|  |  |     +- halfbang2
|  |  |     +- halfshave_glamorous
|  |  |     +- halfshave_glamorous_alt
|  |  |     +- halfshave_long
|  |  |     +- halfshave_long_alt
|  |  |     +- halfshave_messy
|  |  |     +- halfshave_messy_alt
|  |  |     +- halfshave_messylong
|  |  |     +- halfshave_messylong_alt
|  |  |     +- halfshaved
|  |  |     +- hearth_f
|  |  |     +- hedgehog
|  |  |     +- heiress
|  |  |     +- heroic
|  |  |     +- highfade
|  |  |     +- highlander
|  |  |     +- highponytail
|  |  |     +- hime
|  |  |     +- himecut
|  |  |     +- himecut2
|  |  |     +- himeup
|  |  |     +- hitop
|  |  |     +- homely
|  |  |     +- homely_f
|  |  |     +- homewaifu
|  |  |     +- hprotagonist
|  |  |     +- hunter
|  |  |     +- hyenamane
|  |  |     +- inari
|  |  |     +- jade
|  |  |     +- jay
|  |  |     +- jensen
|  |  |     +- joestar
|  |  |     +- junia_tief_f
|  |  |     +- kagami
|  |  |     +- keanu
|  |  |     +- kepthair
|  |  |     +- kobeni_1
|  |  |     +- kobeni_2
|  |  |     +- kobeni_tail
|  |  |     +- kusanagi_alt
|  |  |     +- kusangi
|  |  |     +- lady_f
|  |  |     +- landlord
|  |  |     +- largebun
|  |  |     +- lion
|  |  |     +- long
|  |  |     +- long2
|  |  |     +- long3
|  |  |     +- long4
|  |  |     +- long_over_eye
|  |  |     +- long_over_eye_alt
|  |  |     +- longbangs
|  |  |     +- longemo
|  |  |     +- longer
|  |  |     +- longest
|  |  |     +- longest2
|  |  |     +- longestalt
|  |  |     +- longfringe
|  |  |     +- longponytail
|  |  |     +- longstraightponytail
|  |  |     +- longtails
|  |  |     +- loosebraid_f
|  |  |     +- lover_tief_m
|  |  |     +- lowbraid
|  |  |     +- lowbun
|  |  |     +- lowfade
|  |  |     +- maid_f
|  |  |     +- maiden_f
|  |  |     +- majestic
|  |  |     +- majestic_dwarf
|  |  |     +- majestic_elf
|  |  |     +- majestic_f
|  |  |     +- manbun
|  |  |     +- martial
|  |  |     +- martyr
|  |  |     +- mcsqueeb
|  |  |     +- medfade
|  |  |     +- mediumbraid
|  |  |     +- mediumessy
|  |  |     +- megaeyebrows
|  |  |     +- messy
|  |  |     +- messy_f
|  |  |     +- messy_rt
|  |  |     +- miner
|  |  |     +- modern
|  |  |     +- modern2
|  |  |     +- mohawk
|  |  |     +- monk
|  |  |     +- morning
|  |  |     +- mulder
|  |  |     +- mysterious_elf
|  |  |     +- mystery_f
|  |  |     +- neuter
|  |  |     +- newyou
|  |  |     +- nitori
|  |  |     +- nobility
|  |  |     +- noblesse_f
|  |  |     +- nofade
|  |  |     +- nomadic
|  |  |     +- not_floorlength_braid
|  |  |     +- novice
|  |  |     +- odango
|  |  |     +- ombre
|  |  |     +- oneshoulder
|  |  |     +- orc_f
|  |  |     +- over_eye
|  |  |     +- oxton
|  |  |     +- parted
|  |  |     +- partedside
|  |  |     +- performer_tief_f
|  |  |     +- pigtails
|  |  |     +- pigtails2
|  |  |     +- pigtails3
|  |  |     +- pirate
|  |  |     +- pixie
|  |  |     +- pixie_f
|  |  |     +- plain_f
|  |  |     +- playful
|  |  |     +- pompadour
|  |  |     +- ponytail1
|  |  |     +- ponytail2
|  |  |     +- ponytail3
|  |  |     +- ponytail4
|  |  |     +- ponytail5
|  |  |     +- ponytail6
|  |  |     +- ponytail7
|  |  |     +- ponytail8
|  |  |     +- ponytailwitcher
|  |  |     +- poofy
|  |  |     +- princely
|  |  |     +- protagonist
|  |  |     +- queenly_f
|  |  |     +- quiff
|  |  |     +- reversemohawk
|  |  |     +- rogue
|  |  |     +- romantic
|  |  |     +- ronin
|  |  |     +- rosa
|  |  |     +- rowbraid
|  |  |     +- rowbun
|  |  |     +- rowdualtail
|  |  |     +- rows1
|  |  |     +- rows2
|  |  |     +- royalcurls
|  |  |     +- runt
|  |  |     +- sabitsuki
|  |  |     +- sabitsuki_ponytail
|  |  |     +- samurai
|  |  |     +- scout
|  |  |     +- scribe
|  |  |     +- shaved
|  |  |     +- shavedmohawk
|  |  |     +- shavedpart
|  |  |     +- short
|  |  |     +- shortbangs
|  |  |     +- shortbraid
|  |  |     +- shorthair2
|  |  |     +- shorthair3
|  |  |     +- shorthair6
|  |  |     +- shorthair7
|  |  |     +- shorthaireighties
|  |  |     +- shorthaireighties_alt
|  |  |     +- shorthime
|  |  |     +- shortmessy
|  |  |     +- shoulderlength
|  |  |     +- shrine_f
|  |  |     +- sidecut
|  |  |     +- sidepartlongalt
|  |  |     +- sidetail
|  |  |     +- sidetail2
|  |  |     +- sidetail3
|  |  |     +- sidetail4
|  |  |     +- sideways_ponytail
|  |  |     +- singlebraid
|  |  |     +- skinhead
|  |  |     +- soilbride_f
|  |  |     +- son
|  |  |     +- son2
|  |  |     +- southern
|  |  |     +- spicy
|  |  |     +- spiky
|  |  |     +- spiky2
|  |  |     +- spiky3
|  |  |     +- spikyponytail
|  |  |     +- squire
|  |  |     +- squire_f
|  |  |     +- stacy
|  |  |     +- stacybun
|  |  |     +- stail
|  |  |     +- steppeman
|  |  |     +- straightlong
|  |  |     +- straightovereye
|  |  |     +- straightshort
|  |  |     +- straightside
|  |  |     +- suave
|  |  |     +- swain
|  |  |     +- swept
|  |  |     +- swept2
|  |  |     +- tails_f
|  |  |     +- thickcurly
|  |  |     +- thicklong
|  |  |     +- thicklong_alt
|  |  |     +- thickshort
|  |  |     +- thinning
|  |  |     +- thinningfront
|  |  |     +- thinningrear
|  |  |     +- tied
|  |  |     +- tied2
|  |  |     +- tied_f
|  |  |     +- tiedlong
|  |  |     +- tiedup_f
|  |  |     +- tightbun
|  |  |     +- topknot
|  |  |     +- tressshoulder
|  |  |     +- trimflat
|  |  |     +- trimmed
|  |  |     +- troubadour
|  |  |     +- tsidecut
|  |  |     +- twintail_floor
|  |  |     +- twintails
|  |  |     +- undercut
|  |  |     +- undercutleft
|  |  |     +- undercutright
|  |  |     +- unkept
|  |  |     +- unshavenmohawk
|  |  |     +- updo
|  |  |     +- updo_f
|  |  |     +- veryshortovereye
|  |  |     +- volaju
|  |  |     +- vox
|  |  |     |  +- afro
|  |  |     |  +- crestedquills
|  |  |     |  +- emperorquills
|  |  |     |  +- horns
|  |  |     |  +- keelquills
|  |  |     |  +- keetquills
|  |  |     |  +- kingly
|  |  |     |  +- mohawk
|  |  |     |  +- nights
|  |  |     |  +- razor
|  |  |     |  +- razorclipped
|  |  |     |  +- shortquills
|  |  |     |  +- tielquills
|  |  |     |  `- yasu
|  |  |     +- vulpkian
|  |  |     |  +- anita
|  |  |     |  +- jagged
|  |  |     |  +- kajam1
|  |  |     |  +- kajam2
|  |  |     |  +- keid
|  |  |     |  +- mizar
|  |  |     |  `- raine
|  |  |     +- warlady
|  |  |     +- warrior
|  |  |     +- waterfield
|  |  |     +- wavylong
|  |  |     +- wavyovereye
|  |  |     +- wildside
|  |  |     +- wisp
|  |  |     +- wisp_f
|  |  |     +- woodsman_elf
|  |  |     +- yakuza
|  |  |     +- ziegler
|  |  |     +- zoey
|  |  |     +- zone
|  |  |     `- zybantu
|  |  +- head_feature
|  |  |  +- ipc_screen
|  |  |  |  +- blank
|  |  |  |  +- blue
|  |  |  |  +- breakout
|  |  |  |  +- bsod
|  |  |  |  +- console
|  |  |  |  +- ecgwave
|  |  |  |  +- eight
|  |  |  |  +- eyes
|  |  |  |  +- goggles
|  |  |  |  +- golglider
|  |  |  |  +- green
|  |  |  |  +- heart
|  |  |  |  +- monoeye
|  |  |  |  +- nature
|  |  |  |  +- pink
|  |  |  |  +- purple
|  |  |  |  +- rainbow
|  |  |  |  +- red
|  |  |  |  +- redtext
|  |  |  |  +- rgb
|  |  |  |  +- scroll
|  |  |  |  +- shower
|  |  |  |  +- sinewave
|  |  |  |  +- squarewave
|  |  |  |  +- stars
|  |  |  |  +- sunburst
|  |  |  |  +- textdrop
|  |  |  |  `- yellow
|  |  |  +- skrell_hair
|  |  |  |  +- long
|  |  |  |  `- short
|  |  |  +- teshari_feathers
|  |  |  |  +- backstrafe
|  |  |  |  +- bushy
|  |  |  |  +- droopy
|  |  |  |  +- longway
|  |  |  |  +- mane
|  |  |  |  +- mohawk
|  |  |  |  +- mushroom
|  |  |  |  +- pointy
|  |  |  |  +- regular
|  |  |  |  +- spiky
|  |  |  |  +- thinmane
|  |  |  |  +- thinmohawk
|  |  |  |  +- tree
|  |  |  |  `- upright
|  |  |  `- xeno_head
|  |  |     +- hollywood
|  |  |     +- royal
|  |  |     +- standard
|  |  |     `- warrior
|  |  +- horns
|  |  |  +- angler
|  |  |  +- antlers
|  |  |  +- bigcurlyhorns
|  |  |  +- billberry
|  |  |  +- broken
|  |  |  +- brokenliftedhorns
|  |  |  +- bunhorns
|  |  |  +- curled
|  |  |  +- curledramhorns
|  |  |  +- curledramhornsalt
|  |  |  +- doublehorns
|  |  |  +- dragon
|  |  |  +- drake
|  |  |  +- drake_wide
|  |  |  +- faceguard
|  |  |  +- greathorns
|  |  |  +- guilmon
|  |  |  +- halforc
|  |  |  +- halo
|  |  |  +- knight
|  |  |  +- large
|  |  |  |  +- big_antlers
|  |  |  |  +- branching_antlers
|  |  |  |  +- dukely_antlers
|  |  |  |  +- highrise
|  |  |  |  +- large_antlers
|  |  |  |  +- pronghorn
|  |  |  |  +- regal_antlers
|  |  |  |  +- short_antlers
|  |  |  |  `- spire
|  |  |  +- lbroken
|  |  |  +- liftedhorns
|  |  |  +- longhorns
|  |  |  +- longtusk
|  |  |  +- marauder
|  |  |  +- oni
|  |  |  +- oni_large
|  |  |  +- outstretched
|  |  |  +- ram
|  |  |  +- ramalt
|  |  |  +- rbroken
|  |  |  +- sheephorns
|  |  |  +- short
|  |  |  +- sideswept
|  |  |  +- simple
|  |  |  +- smallantlers
|  |  |  +- smallramhorns
|  |  |  +- smallramhornsalt
|  |  |  +- smallramhornsthree
|  |  |  +- stabbers
|  |  |  +- tiefling
|  |  |  +- tieflingalt
|  |  |  +- uni
|  |  |  `- unihorn
|  |  +- legwear
|  |  |  `- stockings
|  |  |     +- fishnet
|  |  |     +- knee_high
|  |  |     +- knee_high_silk
|  |  |     +- silk
|  |  |     +- thigh_high
|  |  |     `- thigh_high_silk
|  |  +- neck_feature
|  |  |  +- mammal_fluff
|  |  |  |  +- fluff
|  |  |  |  +- fluff_dual
|  |  |  |  +- fluff_dual_front
|  |  |  |  +- fluff_front
|  |  |  |  +- insect_f
|  |  |  |  `- insect_m
|  |  |  `- moth_fluff
|  |  |     +- atlas
|  |  |     +- deathhead
|  |  |     +- firewatch
|  |  |     +- gothic
|  |  |     +- jungle
|  |  |     +- lovers
|  |  |     +- luna
|  |  |     +- monarch
|  |  |     +- moonfly
|  |  |     +- oakworm
|  |  |     +- plain
|  |  |     +- poison
|  |  |     +- punished
|  |  |     +- ragged
|  |  |     +- reddish
|  |  |     +- royal
|  |  |     +- snow
|  |  |     +- whitefly
|  |  |     `- witchwing
|  |  +- none
|  |  +- penis
|  |  |  +- barbknot
|  |  |  +- flared
|  |  |  +- hemi
|  |  |  +- hemiknot
|  |  |  +- human
|  |  |  +- knotted
|  |  |  +- knotted2
|  |  |  +- tapered
|  |  |  +- tapered_mammal
|  |  |  `- tentacle
|  |  +- piercing
|  |  |  +- beads
|  |  |  |  +- emerald
|  |  |  |  +- gold
|  |  |  |  `- silver
|  |  |  `- rings
|  |  |     +- emerald
|  |  |     +- gold
|  |  |     `- silver
|  |  +- snout
|  |  |  +- alienlizard
|  |  |  +- alienlizardteeth
|  |  |  +- bigbeak
|  |  |  +- bigbeakshort
|  |  |  +- bird
|  |  |  +- bovine
|  |  |  +- bug
|  |  |  +- bugna
|  |  |  +- cat
|  |  |  +- elephant
|  |  |  +- front
|  |  |  |  +- bigbeak
|  |  |  |  +- bird
|  |  |  |  +- bovine
|  |  |  |  +- bug
|  |  |  |  +- bugna
|  |  |  |  +- elephant
|  |  |  |  +- husky
|  |  |  |  +- lcanid
|  |  |  |  +- lcanidalt
|  |  |  |  +- lcanidstriped
|  |  |  |  +- lcanidstripedalt
|  |  |  |  +- otie
|  |  |  |  +- otiesmile
|  |  |  |  +- pede
|  |  |  |  +- redpanda
|  |  |  |  +- redpandaalt
|  |  |  |  +- rhino
|  |  |  |  +- rodent
|  |  |  |  +- round
|  |  |  |  +- roundlight
|  |  |  |  +- scanid
|  |  |  |  +- scanidalt
|  |  |  |  +- scanidalt2
|  |  |  |  +- scanidalt3
|  |  |  |  +- sergal
|  |  |  |  +- sharp
|  |  |  |  +- sharplight
|  |  |  |  +- skulldog
|  |  |  |  +- toucan
|  |  |  |  +- wolf
|  |  |  |  `- wolfalt
|  |  |  +- hanubus
|  |  |  +- hhorse
|  |  |  +- hjackal
|  |  |  +- hookbeak
|  |  |  +- hookbeakbig
|  |  |  +- hpanda
|  |  |  +- hspots
|  |  |  +- husky
|  |  |  +- hzebra
|  |  |  +- lcanid
|  |  |  +- lcanidalt
|  |  |  +- lcanidstriped
|  |  |  +- lcanidstripedalt
|  |  |  +- otie
|  |  |  +- otiesmile
|  |  |  +- pede
|  |  |  +- rat
|  |  |  +- redpanda
|  |  |  +- redpandaalt
|  |  |  +- rhino
|  |  |  +- rodent
|  |  |  +- round
|  |  |  +- rounddualcolor
|  |  |  +- roundlight
|  |  |  +- roundlightdualcolor
|  |  |  +- sbeak
|  |  |  +- scanid
|  |  |  +- scanidalt
|  |  |  +- scanidalt2
|  |  |  +- scanidalt3
|  |  |  +- sergal
|  |  |  +- shark
|  |  |  +- sharp
|  |  |  +- sharpdualcolor
|  |  |  +- sharplight
|  |  |  +- sharplightdualcolor
|  |  |  +- shortnosed
|  |  |  +- skulldog
|  |  |  +- slimbeak
|  |  |  +- slimbeakalt
|  |  |  +- slimbeakshort
|  |  |  +- stubby
|  |  |  +- stubbyalt
|  |  |  +- tajaran
|  |  |  +- toucan
|  |  |  +- vulp
|  |  |  +- wolf
|  |  |  `- wolfalt
|  |  +- soul
|  |  |  `- fire
|  |  +- tail
|  |  |  +- australian_shepherd
|  |  |  +- axolotl
|  |  |  +- batl
|  |  |  +- bats
|  |  |  +- bee
|  |  |  +- cat
|  |  |  +- catbig
|  |  |  +- corvid
|  |  |  +- cow
|  |  |  +- data_shark
|  |  |  +- deer
|  |  |  +- dullahan
|  |  |  |  `- heart
|  |  |  +- eevee
|  |  |  +- fennec
|  |  |  +- fish
|  |  |  +- forked_long
|  |  |  +- fox
|  |  |  +- fox2
|  |  |  +- guilmon
|  |  |  +- haven
|  |  |  +- hawk
|  |  |  +- horse
|  |  |  +- husky
|  |  |  +- insect
|  |  |  +- jackal
|  |  |  +- kangaroo
|  |  |  +- kitsune
|  |  |  +- lab
|  |  |  +- large_snake
|  |  |  +- large_snake_plain
|  |  |  +- leopard
|  |  |  +- lizard
|  |  |  |  +- dtiger
|  |  |  |  +- kobold
|  |  |  |  +- ltiger
|  |  |  |  +- smooth
|  |  |  |  `- spikes
|  |  |  +- lunasune
|  |  |  +- lynx
|  |  |  +- monkey
|  |  |  +- murid
|  |  |  +- orca
|  |  |  +- otie
|  |  |  +- owl
|  |  |  +- pede
|  |  |  +- rabbit
|  |  |  +- raccoon
|  |  |  +- raptor
|  |  |  +- rattlesnake
|  |  |  +- redpanda
|  |  |  +- sabresune
|  |  |  +- sergal
|  |  |  +- shark
|  |  |  +- sharknofin
|  |  |  +- shepherd
|  |  |  +- skunk
|  |  |  +- spade
|  |  |  +- squirrel
|  |  |  +- straighttail
|  |  |  +- stripe
|  |  |  +- swallow
|  |  |  +- tamamo_kitsune
|  |  |  +- tentacle
|  |  |  +- tiefling
|  |  |  |  `- heart
|  |  |  +- tiger
|  |  |  +- twocat
|  |  |  +- wolf
|  |  |  `- zorzor
|  |  +- tail_feature
|  |  |  +- large_snake
|  |  |  +- spines
|  |  |  |  +- aquatic
|  |  |  |  +- long
|  |  |  |  +- longmeme
|  |  |  |  +- short
|  |  |  |  `- shortmeme
|  |  |  `- vox_marking
|  |  |     +- bands
|  |  |     +- stripe
|  |  |     `- tip
|  |  +- testicles
|  |  |  `- pair
|  |  +- underwear
|  |  |  +- athletic_leotard
|  |  |  +- bikini
|  |  |  +- braies
|  |  |  +- briefs
|  |  |  |  `- eoran
|  |  |  +- leotard
|  |  |  `- panties
|  |  +- vagina
|  |  |  +- cloaca
|  |  |  +- furred
|  |  |  +- gaping
|  |  |  +- hairy
|  |  |  +- human
|  |  |  `- spade
|  |  `- wings
|  |     +- bat
|  |     +- bee
|  |     +- dragon
|  |     |  `- clipped
|  |     +- fairy
|  |     +- feathery
|  |     +- featheryv2
|  |     +- huge
|  |     |  +- angel
|  |     |  +- dragon
|  |     |  +- megamoth
|  |     |  +- mothra
|  |     |  +- robotic
|  |     |  `- skeleton
|  |     +- large
|  |     |  +- gargoyle
|  |     |  +- harpybat_alt
|  |     |  +- harpyfluff
|  |     |  +- harpyfolded
|  |     |  +- harpyowl
|  |     |  +- harpyswept
|  |     |  `- harpyswept_alt
|  |     +- moth
|  |     |  +- atlas
|  |     |  +- brown
|  |     |  +- deathhead
|  |     |  +- featherful
|  |     |  +- firewatch
|  |     |  +- gothic
|  |     |  +- jungle
|  |     |  +- lovers
|  |     |  +- luna
|  |     |  +- monarch
|  |     |  +- moonfly
|  |     |  +- oakworm
|  |     |  +- plain
|  |     |  +- plasmafire
|  |     |  +- poison
|  |     |  +- punished
|  |     |  +- ragged
|  |     |  +- reddish
|  |     |  +- rosy
|  |     |  +- royal
|  |     |  +- snow
|  |     |  +- whitefly
|  |     |  `- witchwing
|  |     `- wide
|  |        +- dragon_alt1
|  |        +- dragon_alt2
|  |        +- dragon_synth
|  |        +- harpywings
|  |        +- harpywings_top
|  |        +- harpywingsalt1
|  |        +- harpywingsalt1_top
|  |        +- harpywingsalt2
|  |        +- harpywingsalt2_top
|  |        +- low_wings
|  |        +- low_wings_top
|  |        +- robowing
|  |        +- spider
|  |        `- succubus
|  +- statpack
|  |  +- agile
|  |  |  +- deft
|  |  |  +- dextrous
|  |  |  +- hardy
|  |  |  +- swift
|  |  |  +- thug
|  |  |  +- tricky
|  |  |  `- wary
|  |  +- mental
|  |  |  +- adept
|  |  |  +- augury
|  |  |  +- aware
|  |  |  +- diligent
|  |  |  +- faithdriven
|  |  |  +- industrious
|  |  |  +- precise
|  |  |  +- scholarly
|  |  |  `- zealous
|  |  +- physical
|  |  |  +- enduring
|  |  |  +- muscular
|  |  |  +- struggler
|  |  |  +- tactician
|  |  |  +- taut
|  |  |  +- toil
|  |  |  `- trained
|  |  `- wildcard
|  |     +- austere
|  |     +- fated
|  |     +- frail
|  |     +- virtuous
|  |     `- wretched
|  +- status_effect
|  |  +- antimagic
|  |  +- awestruck
|  |  +- balance_immune
|  |  +- baotha_joyride
|  |  +- black_rot
|  |  +- black_rot_debility
|  |  +- blooddrunk
|  |  +- bog_communion
|  |  +- boon
|  |  +- bounty
|  |  +- buff
|  |  |  +- abyss
|  |  |  +- abyssal
|  |  |  +- acidsplash
|  |  |  +- adrenaline_rush
|  |  |  +- alch
|  |  |  |  +- constitutionpot
|  |  |  |  +- endurancepot
|  |  |  |  +- fire_resist
|  |  |  |  +- fortunepot
|  |  |  |  +- intelligencepot
|  |  |  |  +- perceptionpot
|  |  |  |  +- speedpot
|  |  |  |  +- strengthpot
|  |  |  |  `- tripot
|  |  |  +- anthraxbuff
|  |  |  +- arcyne_momentum
|  |  |  +- artificerint
|  |  |  +- artificerstr
|  |  |  +- ashen_aril
|  |  |  +- astrata_gaze
|  |  |  +- auspex
|  |  |  +- axedance
|  |  |  +- baothablessing
|  |  |  +- black_rot_carrier
|  |  |  +- blessed
|  |  |  +- bloodheal
|  |  |  +- bloodrage
|  |  |  +- call_to_arms
|  |  |  +- call_to_slaughter
|  |  |  +- campfire
|  |  |  +- campfire_stamina
|  |  |  +- celerity
|  |  |  +- censerbuff
|  |  |  +- champion
|  |  |  +- churnernegative
|  |  |  +- churnerprotection
|  |  |  +- clash
|  |  |  |  `- limbguard
|  |  |  +- cranking_soulchurner
|  |  |  +- crystalhide
|  |  |  +- dagger_boost
|  |  |  +- dagger_dash
|  |  |  +- darkvision
|  |  |  +- divine_rebirth_healing
|  |  |  +- dragonhide
|  |  |  |  `- fireresist
|  |  |  |     `- buff
|  |  |  +- drunk
|  |  |  +- druqks
|  |  |  +- empowered_strike
|  |  |  +- eora_grace
|  |  |  +- eoran_balm_effect
|  |  |  +- equalizebuff
|  |  |  +- familiar
|  |  |  |  +- burdened_coil
|  |  |  |  +- desert_bred_tenacity
|  |  |  |  +- lightstep
|  |  |  |  +- noticed_thought
|  |  |  |  +- quiet_resilience
|  |  |  |  +- settled_weight
|  |  |  |  +- silver_glance
|  |  |  |  +- soft_favor
|  |  |  |  +- starseam
|  |  |  |  +- steady_spark
|  |  |  |  +- subtle_slip
|  |  |  |  +- threaded_thoughts
|  |  |  |  `- worn_stone
|  |  |  +- featherfall
|  |  |  +- fermented_crab
|  |  |  +- flylordstriage
|  |  |  +- fog_grace
|  |  |  +- fog_ward
|  |  |  +- fog_ward_caster
|  |  |  +- fortify
|  |  |  +- fortitude
|  |  |  +- fotv
|  |  |  +- frost
|  |  |  +- frostbite
|  |  |  +- gate_phalanx
|  |  |  +- giants_strength
|  |  |  +- goodmassage
|  |  |  +- greatmassage
|  |  |  +- greatmealbuff
|  |  |  +- greatsnackbuff
|  |  |  +- griefflower
|  |  |  +- guardbuffone
|  |  |  +- guidance
|  |  |  +- guidinglight
|  |  |  |  `- undivided
|  |  |  +- hag_boon
|  |  |  |  +- creeping_moss
|  |  |  |  |  `- curse
|  |  |  |  +- natural_communion
|  |  |  |  `- storm_rebirth
|  |  |  +- haste
|  |  |  +- hawks_eyes
|  |  |  +- healing
|  |  |  |  +- crescendo_mending
|  |  |  |  +- eora
|  |  |  |  +- necras_vow
|  |  |  |  +- rejuvenationsong
|  |  |  |  |  `- full
|  |  |  |  +- rhythm_regen
|  |  |  |  +- saddleborn
|  |  |  |  `- spider_cocoon
|  |  |  +- hermes_trismegistus
|  |  |  +- herozium
|  |  |  +- infestation
|  |  |  +- innkeeperbuff
|  |  |  +- iron_skin
|  |  |  +- journey_end
|  |  |  +- journey_end_final
|  |  |  +- journey_ending
|  |  |  +- lesserwolf
|  |  |  +- lightningstruck
|  |  |  |  `- minor
|  |  |  +- lirvan_broken_scales
|  |  |  +- lirvan_tithe
|  |  |  +- massage
|  |  |  +- mealbuff
|  |  |  +- moondust
|  |  |  +- moondust_purest
|  |  |  +- moonlightdance
|  |  |  +- murkwine
|  |  |  +- necran_consecration
|  |  |  +- necran_mists
|  |  |  +- necras_vow
|  |  |  +- nocblessing
|  |  |  +- nocshine
|  |  |  +- oiled
|  |  |  +- order
|  |  |  |  +- heartfelt
|  |  |  |  |  +- bolster
|  |  |  |  |  +- charge
|  |  |  |  |  +- forheartfelt
|  |  |  |  |  `- retreat
|  |  |  |  +- hold
|  |  |  |  +- movemovemove
|  |  |  |  +- onfeet
|  |  |  |  `- takeaim
|  |  |  +- ozium
|  |  |  +- pacify
|  |  |  +- parry_buffer
|  |  |  +- peacecake
|  |  |  +- pestra_care
|  |  |  +- phalanx_ready
|  |  |  +- playing_dirge
|  |  |  |  +- discordant_dirge
|  |  |  |  +- enervating_elegy
|  |  |  |  `- rattling_requiem
|  |  |  +- playing_melody
|  |  |  |  +- accelakathist
|  |  |  |  +- fervor
|  |  |  |  +- furtive_fortissimo
|  |  |  |  +- intellectual_interval
|  |  |  |  +- recovery
|  |  |  |  +- rejuvenation
|  |  |  |  `- resolute_refrain
|  |  |  +- playing_music
|  |  |  +- psydonic_endurance
|  |  |  +- psyhealing
|  |  |  +- psyvived
|  |  |  +- quelling_soulchurner
|  |  |  +- rage
|  |  |  +- rage_stamina
|  |  |  +- ragebad
|  |  |  +- ravox_provocation
|  |  |  +- ravox_vow
|  |  |  +- recuperation
|  |  |  |  `- other
|  |  |  +- refocus
|  |  |  +- reversion
|  |  |  +- rockmuncher
|  |  |  +- seelie_drugs
|  |  |  +- sermon
|  |  |  +- snackbuff
|  |  |  +- song
|  |  |  |  +- accelakathist
|  |  |  |  |  `- full
|  |  |  |  +- fervor
|  |  |  |  |  `- full
|  |  |  |  +- furtive_fortissimo
|  |  |  |  +- intellectual_interval
|  |  |  |  |  `- full
|  |  |  |  +- recovery
|  |  |  |  |  `- full
|  |  |  |  `- resolute_refrain
|  |  |  |     `- full
|  |  |  +- spider_speak
|  |  |  +- stagehands_silence
|  |  |  +- starsugar
|  |  |  +- stoneskin
|  |  |  +- sweet
|  |  |  +- tempo_one
|  |  |  +- tempo_three
|  |  |  +- tempo_two
|  |  |  +- ten_united
|  |  |  +- transparent_eyeball
|  |  |  +- tuneup
|  |  |  +- twinned_gaze
|  |  |  +- twisted_sustenance
|  |  |  +- undermaidenbargain
|  |  |  +- undermaidenbargainheal
|  |  |  +- vampire_float
|  |  |  +- vendetta
|  |  |  +- vigorized
|  |  |  +- vitae
|  |  |  +- ward
|  |  |  +- wardenbuff
|  |  |  +- weed
|  |  |  +- windup
|  |  |  +- wise_moon
|  |  |  +- witherd
|  |  |  +- xylix_joy
|  |  |  +- zeybek_momentum
|  |  |  `- zizo_tithe
|  |  +- bugged
|  |  +- churned
|  |  +- compliance
|  |  +- crusher_damage
|  |  +- curse
|  |  |  +- hag_slumber
|  |  |  `- waterlogged
|  |  +- cyborg_power_regen
|  |  +- debuff
|  |  |  +- addiction
|  |  |  +- apostasy
|  |  |  +- arcanemark
|  |  |  +- axe_exhaustion
|  |  |  +- badmeal
|  |  |  +- badvision
|  |  |  +- baitcd
|  |  |  +- baited
|  |  |  +- baotha_addiction
|  |  |  +- baotha_withdrawal_stats
|  |  |  +- bleeding
|  |  |  +- bleedingworse
|  |  |  +- bleedingworst
|  |  |  +- blindness
|  |  |  +- blood_disgust
|  |  |  +- bloody_mess
|  |  |  +- breedable
|  |  |  +- burnedfood
|  |  |  +- call_to_arms
|  |  |  +- call_to_slaughter
|  |  |  +- chilled
|  |  |  +- clashcd
|  |  |  +- clickcd
|  |  |  +- climbing_lfwb
|  |  |  +- cold
|  |  |  |  `- greater
|  |  |  +- crit_resistance_cd
|  |  |  +- cursed
|  |  |  +- dazed
|  |  |  |  +- freisabre
|  |  |  |  +- longsword
|  |  |  |  +- longsword2h
|  |  |  |  +- shield
|  |  |  |  +- skullshatter
|  |  |  |  +- smite
|  |  |  |  +- stunner
|  |  |  |  `- swipe
|  |  |  +- deathdoorwilloss
|  |  |  +- debt_indicator
|  |  |  +- dendor_revival
|  |  |  +- devitalised
|  |  |  |  +- greater
|  |  |  |  `- lesser
|  |  |  +- diminish
|  |  |  +- disgracedguardsman
|  |  |  +- dreamfiend_curse
|  |  |  +- eoran_wilting
|  |  |  +- equalizedebuff
|  |  |  +- equalizedebuff_noble
|  |  |  +- excomm
|  |  |  +- exposed
|  |  |  +- feintcd
|  |  |  +- feinted
|  |  |  +- fog_chilled
|  |  |  +- frosted1
|  |  |  +- frosted2
|  |  |  +- frosted3
|  |  |  +- frosted4
|  |  |  +- gallowshumor
|  |  |  +- graggar_challenge
|  |  |  +- gravity_anchored
|  |  |  +- hag_bog_tether
|  |  |  |  `- wildshape
|  |  |  +- hag_curse
|  |  |  |  +- rotting_touch
|  |  |  |  `- storm_weakness
|  |  |  +- hereticsermon
|  |  |  +- hobbled
|  |  |  +- hungryt1
|  |  |  +- hungryt2
|  |  |  +- hungryt3
|  |  |  +- joybringer_druqks
|  |  |  +- leech_schizophrenia
|  |  |  +- liver_failure
|  |  |  +- lost_dungeoneer_hood
|  |  |  +- lost_naledi_mask
|  |  |  +- lost_shaman_hood
|  |  |  +- malum_revival
|  |  |  +- mesmerised
|  |  |  +- metabolic_acceleration
|  |  |  +- mishap_arcane_drunkenness
|  |  |  +- mishap_arcane_high
|  |  |  +- mishap_arcane_paralysis
|  |  |  +- mishap_blindness
|  |  |  +- mishap_confused
|  |  |  +- mishap_dimwitted
|  |  |  +- mishap_feeblemind
|  |  |  +- mishap_langloss
|  |  |  +- mishap_sleepy
|  |  |  +- mockery_stack
|  |  |  +- muscle_sore
|  |  |  +- necran_cross
|  |  |  |  `- strong
|  |  |  +- necrandeathdoorwilloss
|  |  |  +- netted
|  |  |  |  `- vile
|  |  |  +- no_coom_cheating
|  |  |  +- noc_revival
|  |  |  +- pestilent_plague
|  |  |  +- pomegranate_aura
|  |  |  +- pomegranate_beauty
|  |  |  +- postcooldown
|  |  |  +- random_revival
|  |  |  +- ravox_burden
|  |  |  +- ravox_revival
|  |  |  +- ravox_spirit_backlash
|  |  |  +- ravox_warrior_spirit
|  |  |  +- revived
|  |  |  +- riposted
|  |  |  +- ritesexpended
|  |  |  +- ritesexpended_heavy
|  |  |  +- ritualdefiled
|  |  |  +- rotfood
|  |  |  +- rotted
|  |  |  +- rotted_zombie
|  |  |  +- sensitive_nerves
|  |  |  +- sleepytime
|  |  |  +- song
|  |  |  |  +- discordant_dirge
|  |  |  |  |  `- full
|  |  |  |  +- enervating_elegy
|  |  |  |  |  `- full
|  |  |  |  `- rattling_requiem
|  |  |  |     `- full
|  |  |  +- specialcd
|  |  |  +- staggered
|  |  |  +- strikecd
|  |  |  +- submissive
|  |  |  +- thirstyt1
|  |  |  +- thirstyt2
|  |  |  +- thirstyt3
|  |  |  +- uncookedfood
|  |  |  +- vamp_dreams
|  |  |  +- vampbite
|  |  |  +- vulnerable
|  |  |  +- withered
|  |  |  +- yeetcd
|  |  |  `- zizo_drain
|  |  +- divine_exhaustion
|  |  +- divine_strike
|  |  +- dream_mark
|  |  +- dream_teleport
|  |  +- eora_blessing
|  |  +- eora_bond
|  |  +- eoranaura
|  |  +- exercised
|  |  +- fake_virus
|  |  +- fire_handler
|  |  |  +- fire_stacks
|  |  |  |  +- divine
|  |  |  |  `- sunder
|  |  |  |     `- blessed
|  |  |  `- wet_stacks
|  |  +- fleshmend
|  |  +- freon
|  |  |  +- freezing
|  |  |  `- watcher
|  |  +- go_away
|  |  +- gonbolaPacify
|  |  +- good_music
|  |  +- hag_root_tether
|  |  +- immolation
|  |  +- in_love
|  |  +- incapacitating
|  |  |  +- immobilized
|  |  |  +- knockdown
|  |  |  +- off_balanced
|  |  |  +- paralyzed
|  |  |  +- sleeping
|  |  |  +- stasis
|  |  |  +- stun
|  |  |  `- unconscious
|  |  +- joybringer
|  |  +- knot_fucked_stupid
|  |  +- knot_gaped
|  |  +- knot_tied
|  |  +- knotted
|  |  +- light_buff
|  |  |  `- moon
|  |  +- majesty_active
|  |  +- majesty_compulsion
|  |  +- mood
|  |  |  +- bad
|  |  |  +- good
|  |  |  +- vbad
|  |  |  `- vgood
|  |  +- neck_slice
|  |  +- orderbringer
|  |  +- pacify
|  |  +- pearlescent_aril
|  |  +- pomegranate_fatigue
|  |  +- recent_weapon
|  |  +- regen
|  |  |  `- soothing_bloom
|  |  +- regenerative_core
|  |  +- shadow_mend
|  |  +- sigil_mark
|  |  +- silenced
|  |  +- spasms
|  |  +- stacking
|  |  |  `- saw_bleed
|  |  +- strandling
|  |  +- swingdelay
|  |  |  +- disrupt
|  |  |  `- penalty
|  |  +- sword_spin
|  |  +- telescope_used
|  |  +- territorial_rage
|  |  +- thaumaturgy
|  |  +- throat_soothed
|  |  +- trance
|  |  +- ugotmail
|  |  +- vampire_spawn_protection
|  |  +- void_price
|  |  +- wheel
|  |  +- wish_granters_gift
|  |  +- woe
|  |  +- zombie_infection
|  |  `- zuranus
|  +- stew_recipe
|  |  +- allspice
|  |  +- apple
|  |  +- aubergine_soup
|  |  +- balefirestew
|  |  +- berry
|  |  +- berry_poisoned
|  |  +- bisque
|  |  +- bone
|  |  +- breadpudding
|  |  +- brothbrique
|  |  +- cabbage
|  |  +- carrot_stew
|  |  +- cheese
|  |  +- cheeserice
|  |  +- chicken
|  |  +- chocolate
|  |  +- chocolate_spiced
|  |  +- chocolatepudding
|  |  +- coffee
|  |  +- coffee_spiced
|  |  +- congee
|  |  +- cucumber_soup
|  |  +- egg
|  |  +- eggplant_soup
|  |  +- eggrice
|  |  +- evilfryfish
|  |  +- fish
|  |  +- frostedpudding
|  |  +- frybird
|  |  +- frybisque
|  |  +- frycongee
|  |  +- fryegg
|  |  +- fryfish
|  |  +- frymeat
|  |  +- frypork
|  |  +- fryrabbit
|  |  +- fryseafoodbroil
|  |  +- fryspider
|  |  +- frysquash_soup
|  |  +- fryvolf
|  |  +- garlick_soup
|  |  +- hardtackstew
|  |  +- kingvolf
|  |  +- lavishaubergine_soup
|  |  +- lavishfrybird
|  |  +- lavishfrybisque
|  |  +- lavishfryegg
|  |  +- lavishfryfish
|  |  +- lavishfryrice
|  |  +- lavishfryseafoodbroil
|  |  +- lemon
|  |  +- lime
|  |  +- meat
|  |  +- meatrice
|  |  +- nutty_stew
|  |  +- oatmeal
|  |  +- onion
|  |  +- parmesan
|  |  +- pear
|  |  +- pepperfrybird
|  |  +- pepperfryfish
|  |  +- pepperfrymeat
|  |  +- plum_soup
|  |  +- poppy_milk
|  |  +- pork
|  |  +- porridge
|  |  +- potato
|  |  +- purebutter
|  |  +- rabbit
|  |  +- roastcarrot_stew
|  |  +- rose_tea
|  |  +- rose_tea_spiced
|  |  +- saltmeat
|  |  +- seafoodbroil
|  |  +- shrimprice
|  |  +- slop
|  |  +- spider
|  |  +- squash_soup
|  |  +- tangerine_marmalade
|  |  +- tea
|  |  +- tea_spiced
|  |  +- thickbalefirestew
|  |  +- thickbreadpudding
|  |  +- thickbrothbrique
|  |  +- thickcabbage
|  |  +- thickcheese
|  |  +- thickchocolatepudding
|  |  +- thickcucumber_soup
|  |  +- thickfrostedpudding
|  |  +- thickfrybird
|  |  +- thickfrycabbage
|  |  +- thickfryegg
|  |  +- thickfryonion
|  |  +- thickfrypork
|  |  +- thickfrypotato
|  |  +- thickonion
|  |  +- thickparmesan
|  |  +- thickpork
|  |  +- thickporridge
|  |  +- thickpotato
|  |  +- thickturnip
|  |  +- tomato_soup
|  |  +- turnip
|  |  +- veggiefrybird
|  |  +- veggiefryfish
|  |  +- veggiefrymeat
|  |  +- veggiefryrabbit
|  |  +- veggiefryvolf
|  |  +- viscera
|  |  `- volf
|  +- storyteller
|  |  +- abyssor
|  |  +- astrata
|  |  +- baotha
|  |  +- dendor
|  |  +- eora
|  |  +- graggar
|  |  +- malum
|  |  +- matthios
|  |  +- necra
|  |  +- noc
|  |  +- pestra
|  |  +- psydon
|  |  +- ravox
|  |  +- xylix
|  |  `- zizo
|  +- stressevent
|  |  +- abyssor_rain
|  |  +- abyssor_storm
|  |  +- abysssmoke
|  |  +- apostasy
|  |  +- applesmoke
|  |  +- arcane_high
|  |  +- archivist_shushed
|  |  +- artistic_inspiration
|  |  +- artistic_inspiration_minor
|  |  +- astrata_grandeur
|  |  +- averse
|  |  +- bad_blood
|  |  +- badmeal
|  |  +- baotha_withdrawal_severe
|  |  +- bath
|  |  +- bathcleaned
|  |  +- bathwater
|  |  +- beautiful
|  |  +- blackberrysmoke
|  |  +- bleeding
|  |  +- blessed
|  |  +- blessed_weapon
|  |  +- blue_balls
|  |  +- bond_death
|  |  +- bond_ended
|  |  +- burntmeal
|  |  +- campfire
|  |  +- carrotsmoke
|  |  +- champion
|  |  +- chocolatesmoke
|  |  +- coldhead
|  |  +- confessed
|  |  +- confessedgood
|  |  +- creepy_squid
|  |  +- creepy_squid_happy
|  |  +- crisis_relief
|  |  +- crowd
|  |  +- cumgood
|  |  +- cumlove
|  |  +- cummax
|  |  +- cummid
|  |  +- cumok
|  |  +- cumpaingood
|  |  +- cumself
|  |  +- debt
|  |  +- dimwitted
|  |  +- dismembered
|  |  +- drankrat
|  |  +- dream_horror
|  |  +- drunk
|  |  +- drym
|  |  +- dungeoneerhoodlost
|  |  +- dwarfshaved
|  |  +- empathic_bond_formed
|  |  +- eoran_blessing
|  |  +- eoran_blessing_greater
|  |  +- excommunicated
|  |  +- favourite_drink
|  |  +- favourite_food
|  |  +- feebleminded
|  |  +- felldown
|  |  +- fermented_crab_bad
|  |  +- fermented_crab_good
|  |  +- freakout
|  |  +- fviewdismember
|  |  +- gallowshumor
|  |  +- goodmeal
|  |  +- goodsnack
|  |  +- graggar_culling_finished
|  |  +- graggar_culling_unfinished
|  |  +- graggarite_blood_rain
|  |  +- greatmeal
|  |  +- greatsnack
|  |  +- hand_fed_fruit
|  |  +- hated_drink
|  |  +- hated_food
|  |  +- headless
|  |  +- heretic_on_sermon
|  |  +- high
|  |  +- hithead
|  |  +- hungry
|  |  +- hunted
|  |  +- hydrated
|  |  +- jacksberriessmoke
|  |  +- jesterphobia
|  |  +- joke
|  |  +- keep_standard
|  |  +- keep_standard_lesser
|  |  +- kytherian_blessing
|  |  +- lasthigh
|  |  +- leprosy
|  |  +- limesmoke
|  |  +- lonely_max
|  |  +- lonely_one
|  |  +- lonely_three
|  |  +- lonely_two
|  |  +- lostchampion
|  |  +- lostward
|  |  +- majesty_compelled
|  |  +- maniac_woke_up
|  |  +- meditation
|  |  +- mehstew
|  |  +- menthasmoke
|  |  +- miasmagas
|  |  +- moondust
|  |  +- moondust_purest
|  |  +- music
|  |  |  +- five
|  |  |  +- four
|  |  |  +- six
|  |  |  +- three
|  |  |  `- two
|  |  +- naledimasklost
|  |  +- necrarevive
|  |  +- night_owl
|  |  +- noble_ate_without_table
|  |  +- noble_bad_manners
|  |  +- noble_bland_food
|  |  +- noble_bowed_to
|  |  +- noble_desperate
|  |  +- noble_impoverished_food
|  |  +- noble_lavish_food
|  |  +- nocrowd
|  |  +- nopeople
|  |  +- obsession_death
|  |  +- obsession_ended
|  |  +- obsession_panic
|  |  +- obsession_revival
|  |  +- obsession_target_healed
|  |  +- obsession_target_hurt
|  |  +- orb_madness
|  |  +- ozium
|  |  +- oziumoff
|  |  +- pacified
|  |  +- painmax
|  |  +- pallid_outdoors
|  |  +- parablood
|  |  +- paracrowd
|  |  +- parasol_rain
|  |  +- parasol_snow
|  |  +- parastr
|  |  +- paratalk
|  |  +- parched
|  |  +- peacecake
|  |  +- peckish
|  |  +- perfume
|  |  +- perseverance
|  |  +- prebel
|  |  +- precious_mob_died
|  |  +- profane
|  |  +- proximity_comfort
|  |  +- psycurse
|  |  +- psyprayer
|  |  +- public_thrill
|  |  +- puzzle_easy
|  |  +- puzzle_fail
|  |  +- puzzle_hard
|  |  +- puzzle_impossible
|  |  +- puzzle_medium
|  |  +- pweed
|  |  +- revenant_cross
|  |  +- rotfood
|  |  +- salviasmoke
|  |  +- saw_wonder
|  |  +- see_zuranus
|  |  |  +- graggarite
|  |  |  `- zizoite
|  |  +- seeblessed
|  |  +- separation_anxiety
|  |  +- sermon
|  |  +- sewertouched
|  |  +- shamanhoodlost
|  |  +- shitstew
|  |  +- sleepytime
|  |  +- something_stirs
|  |  |  `- telescope
|  |  +- soulchurner
|  |  +- soulchurnerhorror
|  |  +- soulchurnerpsydon
|  |  +- starsugar
|  |  +- starving
|  |  +- strawberrysmoke
|  |  +- stuffed
|  |  +- sweet
|  |  +- syoncalamity
|  |  +- terrible_dreams
|  |  +- test
|  |  +- testr
|  |  +- thefool
|  |  +- thirst
|  |  +- thrill
|  |  +- thrillsex
|  |  +- tortured
|  |  +- tragedy
|  |  +- triumph
|  |  +- uncanny
|  |  +- unseemly
|  |  +- valerianasmoke
|  |  +- vampiric_nostalgia
|  |  +- vampiric_reality
|  |  +- vblood
|  |  +- vice
|  |  +- viewdismember
|  |  +- viewgib
|  |  +- viewsinpunish
|  |  +- virginchurch
|  |  +- vomit
|  |  +- vomitedonother
|  |  +- vomitother
|  |  +- vomitself
|  |  +- ward
|  |  +- weed
|  |  +- wine_good
|  |  +- wine_great
|  |  +- wine_okay
|  |  +- xylix_star
|  |  |  `- xylixian
|  |  +- xylixian_fate
|  |  +- xylixian_pity
|  |  `- ziggarasmoke
|  +- supply_pack
|  |  `- rogue
|  |     +- adventure_supplies
|  |     |  +- bandages
|  |     |  +- bedroll
|  |     |  +- folding_alchcauldron
|  |     |  +- folding_alchstation
|  |     |  +- folding_table
|  |     |  +- ger
|  |     |  +- lamptern
|  |     |  +- mess_kit
|  |     |  +- needles
|  |     |  +- rationpaper
|  |     |  +- ropes
|  |     |  +- small_tent
|  |     |  +- waterskin
|  |     |  +- woodstaff
|  |     |  `- yurt
|  |     +- Alchemist
|  |     |  +- antidote
|  |     |  +- bedroll
|  |     |  +- blind_gas
|  |     |  +- botbomb
|  |     |  +- bronzeleftarm
|  |     |  +- bronzeleftleg
|  |     |  +- bronzerightarm
|  |     |  +- bronzerightleg
|  |     |  +- cheele
|  |     |  +- conpot
|  |     |  +- endpot
|  |     |  +- explosion
|  |     |  +- fire_gas
|  |     |  +- gambeson
|  |     |  +- gbottle
|  |     |  +- goldenapplecheap
|  |     |  +- gorget
|  |     |  +- healing_gas
|  |     |  +- heartblood
|  |     |  +- herozium
|  |     |  +- hgambeson
|  |     |  +- icoif
|  |     |  +- intpot
|  |     |  +- leather
|  |     |  |  +- flgloves
|  |     |  |  +- hbracers
|  |     |  |  +- hpants
|  |     |  |  +- Lbracers
|  |     |  |  +- lgloves
|  |     |  |  +- Lhelmet
|  |     |  |  `- pants
|  |     |  +- lucpot
|  |     |  +- mute_gas
|  |     |  +- perpot
|  |     |  +- poison
|  |     |  +- poison_gas
|  |     |  +- rapier
|  |     |  +- satchel_bomb
|  |     |  +- shortsword
|  |     |  +- spdpot
|  |     |  +- starsugar
|  |     |  +- strpot
|  |     |  +- surgery_bag
|  |     |  +- tntstick
|  |     |  +- trustworthyhat
|  |     |  `- trustworthyrobes
|  |     +- alcohol
|  |     |  +- apfelweinheim
|  |     |  +- avarmead
|  |     |  +- avarrice
|  |     |  +- baijiu
|  |     |  +- beer
|  |     |  +- blackgoat
|  |     |  +- butterhair
|  |     |  +- elfbeer
|  |     |  +- elfblue
|  |     |  +- elfcab
|  |     |  +- elfred
|  |     |  +- grenzelbeer
|  |     |  +- gronnmead
|  |     |  +- jagdtrunk
|  |     |  +- kgunlager
|  |     |  +- kgunplum
|  |     |  +- kgunsake
|  |     |  +- kgunshochu
|  |     |  +- nred
|  |     |  +- onin
|  |     |  +- rtoper
|  |     |  +- saigamilk
|  |     |  +- sazdistal
|  |     |  +- shejiu
|  |     |  +- stonebeard
|  |     |  +- voddena
|  |     |  +- winegrenzel
|  |     |  +- wineraneshen
|  |     |  +- winevalorred
|  |     |  +- winevalorwhite
|  |     |  +- yaojiu
|  |     |  +- zagul
|  |     |  `- zhonghuangjiu
|  |     +- apparel
|  |     |  +- backpack
|  |     |  +- belts
|  |     |  +- blackleatherbelt
|  |     |  +- cloaks
|  |     |  |  `- leather
|  |     |  +- crosses
|  |     |  |  +- divinepantheonabyssor
|  |     |  |  +- divinepantheonastrata
|  |     |  |  +- divinepantheondendor
|  |     |  |  +- divinepantheoneora
|  |     |  |  +- divinepantheonmalum
|  |     |  |  +- divinepantheonnecra
|  |     |  |  +- divinepantheonnoc
|  |     |  |  +- divinepantheonpestra
|  |     |  |  +- divinepantheonravox
|  |     |  |  +- divinepantheonten
|  |     |  |  +- psicross
|  |     |  |  +- silver
|  |     |  |  `- xylix
|  |     |  +- gwstrap
|  |     |  +- hair_dye
|  |     |  +- hoods
|  |     |  +- leatherbelt
|  |     |  +- merchant_pouch
|  |     |  +- plaquegold
|  |     |  +- plaquesilver
|  |     |  +- pouches
|  |     |  +- quiver
|  |     |  |  `- bolt
|  |     |  +- satchel
|  |     |  +- scabbard
|  |     |  +- sheath
|  |     |  +- shirts
|  |     |  |  `- tunic
|  |     |  +- shortsatchel
|  |     |  +- trousers
|  |     |  |  `- leather
|  |     |  `- trousrs
|  |     +- armor_exotic
|  |     |  +- gronn_pack_heavy
|  |     |  +- gronn_pack_light
|  |     |  +- gronn_pack_medium
|  |     |  +- legacycuirass_steel
|  |     |  +- legacyfluteplate_steel
|  |     |  +- legacyfullplate_steel
|  |     |  `- legacyhalfplate_steel
|  |     +- armor_iron
|  |     |  +- bevor_iron
|  |     |  +- boots_iron
|  |     |  +- bracers
|  |     |  +- breastplate_iron
|  |     |  +- brigandine_light
|  |     |  +- chaincoif_iron
|  |     |  +- chaingloves_iron
|  |     |  +- chainkilt
|  |     |  +- chainleg_iron
|  |     |  +- chainmail_iron
|  |     |  +- chausses_brigandine
|  |     |  +- chausses_plate
|  |     |  +- fullplate
|  |     |  +- gorget_iron
|  |     |  +- halfplate
|  |     |  +- hauberk_iron
|  |     |  +- horned
|  |     |  +- jackchains
|  |     |  +- kettle
|  |     |  +- knight
|  |     |  +- knightarmet
|  |     |  +- knightarmetgreatplume
|  |     |  +- mask_iron
|  |     |  +- mask_wildguard
|  |     |  +- plategloves_iron
|  |     |  +- rearbraces
|  |     |  +- sallet
|  |     |  +- skullcap_helmet
|  |     |  `- visored
|  |     +- armor_steel
|  |     |  +- bevor
|  |     |  +- boots_steel
|  |     |  +- bracers_plate
|  |     |  +- brigandine
|  |     |  +- chaincoif_full
|  |     |  +- chaincoif_steel
|  |     |  +- chaingloves_steel
|  |     |  +- chainkilt
|  |     |  +- chainleg_steel
|  |     |  +- chainmantle
|  |     |  +- chausses_brigandine
|  |     |  +- coatplates
|  |     |  +- cuirass_steel
|  |     |  +- elvenbarbute
|  |     |  +- elvenbarbutewinged
|  |     |  +- fluted_cuirass_steel
|  |     |  +- fullplate
|  |     |  +- fullplate_fluted
|  |     |  +- gorget_steel
|  |     |  +- halfplate
|  |     |  +- halfplate_fluted
|  |     |  +- haubergeon_steel
|  |     |  +- hauberk_steel
|  |     |  +- helmet_armet
|  |     |  +- helmet_barbute
|  |     |  +- helmet_barbute_great
|  |     |  +- helmet_barbute_visor
|  |     |  +- helmet_barred
|  |     |  +- helmet_bascinet
|  |     |  +- helmet_bucket
|  |     |  +- helmet_etruscan_bascinet
|  |     |  +- helmet_hounskull
|  |     |  +- helmet_kettle
|  |     |  +- helmet_knight
|  |     |  +- helmet_knight_armet
|  |     |  +- helmet_knight_armetgreatplume
|  |     |  +- helmet_nasal
|  |     |  +- helmet_pigface
|  |     |  +- helmet_sallet
|  |     |  +- helmet_sallet_visor
|  |     |  +- helmet_savoyard
|  |     |  +- helmet_sugarloaf
|  |     |  +- helmet_winged
|  |     |  +- kettle_slitted
|  |     |  +- mask_steel
|  |     |  +- plategloves
|  |     |  +- platelegs
|  |     |  +- rearbraces
|  |     |  +- scalemail
|  |     |  `- steel
|  |     |     `- belt
|  |     +- bandit
|  |     |  `- Mage
|  |     |     `- cinnabar
|  |     +- bath_clothes
|  |     |  +- anklets
|  |     |  +- athletic_leotard
|  |     |  +- bell_collar
|  |     |  +- belt
|  |     |  +- bikini
|  |     |  +- braies
|  |     |  +- briefs
|  |     |  +- collar
|  |     |  +- corset
|  |     |  +- fishnetstockings
|  |     |  +- kneestockings
|  |     |  +- leotard
|  |     |  +- loincloth
|  |     |  +- panties
|  |     |  +- silkbelt
|  |     |  +- silkbra
|  |     |  +- silkmask
|  |     |  +- silkstockings
|  |     |  +- silkydress
|  |     |  +- stockings_normal
|  |     |  `- thighstockings
|  |     +- bath_perfume
|  |     |  +- black_lipstik
|  |     |  +- cherry
|  |     |  +- cinnamon
|  |     |  +- frankincense
|  |     |  +- jade_lipstik
|  |     |  +- jasmine
|  |     |  +- lavender
|  |     |  +- mint
|  |     |  +- myrrh
|  |     |  +- pear
|  |     |  +- purple_lipstik
|  |     |  +- red_lipstik
|  |     |  +- rose
|  |     |  +- sandalwood
|  |     |  +- strawberry
|  |     |  `- vanilla
|  |     +- bath_rogue
|  |     |  +- chains
|  |     |  +- climbing_gear
|  |     |  +- eoran_candles
|  |     |  +- goldpin
|  |     |  +- grappler
|  |     |  +- net
|  |     |  +- piercings
|  |     |  +- quiver
|  |     |  +- silverpin
|  |     |  +- smokebomb
|  |     |  +- waterarrows
|  |     |  `- waterbolts
|  |     +- bath_smokes
|  |     |  +- asigs
|  |     |  +- bsigs
|  |     |  +- chsigs
|  |     |  +- csigs
|  |     |  +- jsigs
|  |     |  +- lsigs
|  |     |  +- masigs
|  |     |  +- msigs
|  |     |  +- sigar
|  |     |  +- sigs
|  |     |  +- ssigs
|  |     |  +- zigbox
|  |     |  +- zigbox_pipezig
|  |     |  +- zigbox_swampzig
|  |     |  `- zigdolier
|  |     +- blackmarket_arms
|  |     |  +- dagger
|  |     |  +- flail
|  |     |  +- heater
|  |     |  +- katar
|  |     |  +- mace
|  |     |  +- shortsword
|  |     |  +- spear
|  |     |  +- steelaxe
|  |     |  +- steelknuckle
|  |     |  +- sword
|  |     |  `- warhammer
|  |     +- blackmarket_diplomacy
|  |     |  +- arrows
|  |     |  +- bolts
|  |     |  +- bomb
|  |     |  +- bow
|  |     |  +- crossbow
|  |     |  +- goldpin
|  |     |  +- leathercollar
|  |     |  +- lockpick
|  |     |  +- lockpicks
|  |     |  +- quiver
|  |     |  +- recurve_bow
|  |     |  +- smokebomb
|  |     |  +- waterarrows
|  |     |  `- waterbolts
|  |     +- blackmarket_drugs
|  |     |  +- moondust
|  |     |  +- ozium
|  |     |  +- pipezig
|  |     |  +- soap
|  |     |  +- spice
|  |     |  `- swampzig
|  |     +- blackmarket_exotics
|  |     |  +- nomag
|  |     |  +- riddleofsteel
|  |     |  `- scrying
|  |     +- blackmarket_potions
|  |     |  +- antidote
|  |     |  +- healthpot
|  |     |  +- manapot
|  |     |  `- stamina
|  |     +- blackmarket_tools
|  |     |  +- backpack
|  |     |  +- bedroll
|  |     |  +- chain
|  |     |  +- grapplinghook
|  |     |  +- keyring
|  |     |  +- needle
|  |     |  +- pouches
|  |     |  +- prarml
|  |     |  +- prarmlbrz
|  |     |  +- prarmr
|  |     |  +- prarmrbrz
|  |     |  +- prlegl
|  |     |  +- prleglbrz
|  |     |  +- prlegr
|  |     |  +- prlegrbrz
|  |     |  +- satchel
|  |     |  +- waterskin
|  |     |  `- woodstaff
|  |     +- Brigand
|  |     |  +- axe
|  |     |  +- bascinet
|  |     |  +- Bevor
|  |     |  +- boots
|  |     |  +- bracers
|  |     |  +- brigandine
|  |     |  +- chaingauntlets
|  |     |  +- chainlegs
|  |     |  +- coif
|  |     |  +- coiffull
|  |     |  +- flail
|  |     |  +- flutedcuirass
|  |     |  +- Gaxe
|  |     |  +- gmace
|  |     |  +- gorget
|  |     |  +- grandmaul
|  |     |  +- Haubergeon
|  |     |  +- hauberk
|  |     |  +- hbascinet
|  |     |  +- heatshield
|  |     |  +- hgambeson
|  |     |  +- ironshield
|  |     |  +- Ironwarhammer
|  |     |  +- kiteshield
|  |     |  +- maul
|  |     |  +- pbascinet
|  |     |  +- scalemail
|  |     |  +- SDGaxe
|  |     |  +- SGaxe
|  |     |  +- sgorget
|  |     |  +- splintbracers
|  |     |  +- splintlegs
|  |     |  +- Staxe
|  |     |  +- steelcuirass
|  |     |  +- steelflail
|  |     |  +- steelmace
|  |     |  +- steelwarhammer
|  |     |  `- Tshield
|  |     +- drugs
|  |     |  +- fermented_crab
|  |     |  +- herozium
|  |     |  +- moondust
|  |     |  +- murkwine
|  |     |  +- nocshine
|  |     |  +- ozium
|  |     |  +- pdust
|  |     |  +- spice
|  |     |  +- starsugar
|  |     |  +- trippyzig
|  |     |  +- whipwine
|  |     |  +- zigbox
|  |     |  +- zigbox_pipezig
|  |     |  +- zigbox_swampzig
|  |     |  `- zigdolier
|  |     +- food
|  |     |  +- angler
|  |     |  +- butter
|  |     |  +- carp
|  |     |  +- chocolate
|  |     |  +- clownfish
|  |     |  +- coffee
|  |     |  +- eel
|  |     |  +- eggs
|  |     |  +- hardtack
|  |     |  +- honey
|  |     |  +- meat
|  |     |  +- pepper
|  |     |  +- raisinbreads
|  |     |  +- rosa
|  |     |  `- tea
|  |     +- gems
|  |     |  +- amber
|  |     |  +- amethyst
|  |     |  +- blortz
|  |     |  +- coral
|  |     |  +- diamond
|  |     |  +- gemerald
|  |     |  +- jade
|  |     |  +- onyxa
|  |     |  +- opal
|  |     |  +- riddleofsteel
|  |     |  +- rose
|  |     |  +- ruby
|  |     |  +- saffira
|  |     |  +- toper
|  |     |  `- turq
|  |     +- Iconoclast
|  |     |  +- armet
|  |     |  +- barhelmet
|  |     |  +- Bevor
|  |     |  +- boots
|  |     |  +- bracers
|  |     |  +- coif
|  |     |  +- coiffull
|  |     |  +- flail
|  |     |  +- Fullplate
|  |     |  +- gorget
|  |     |  +- halfplate
|  |     |  +- Haubergeon
|  |     |  +- hauberk
|  |     |  +- hgambeson
|  |     |  +- katar
|  |     |  +- kiteshield
|  |     |  +- knuckles
|  |     |  +- platechausses
|  |     |  +- plategaunt
|  |     |  +- punchdagger
|  |     |  +- sallet
|  |     |  +- savoyard
|  |     |  +- sgorget
|  |     |  +- steelflail
|  |     |  +- Tshield
|  |     |  `- visoredsallet
|  |     +- instruments
|  |     |  +- accord
|  |     |  +- drum
|  |     |  +- flute
|  |     |  +- guitar
|  |     |  +- harp
|  |     |  +- hurdygurdy
|  |     |  +- lute
|  |     |  +- mbox
|  |     |  +- psyalter
|  |     |  +- shamisen
|  |     |  +- viola
|  |     |  `- vocals
|  |     +- iron_weapons
|  |     |  +- axe
|  |     |  +- axewoodcutting
|  |     |  +- bardiche
|  |     |  +- broadswordiron
|  |     |  +- buckler
|  |     |  +- claymore
|  |     |  +- cudgel
|  |     |  +- dagger
|  |     |  +- flail
|  |     |  +- flailalt
|  |     |  +- goedendag
|  |     |  +- greataxe
|  |     |  +- greatflail
|  |     |  +- greatsword
|  |     |  +- hammer
|  |     |  +- hatchet
|  |     |  +- heavydagger
|  |     |  +- lucerne
|  |     |  +- mace
|  |     |  +- messer
|  |     |  +- shield
|  |     |  +- shortsword
|  |     |  +- spear
|  |     |  +- sword
|  |     |  +- tower
|  |     |  +- towershield
|  |     |  `- whip
|  |     +- Knave
|  |     |  +- brigandine
|  |     |  +- climbing_gear
|  |     |  +- coif
|  |     |  +- coifheavy
|  |     |  +- crossbow
|  |     |  +- dagger
|  |     |  +- daggerss
|  |     |  +- elfdagger
|  |     |  +- gambeson
|  |     |  +- grappler
|  |     |  +- hgambeson
|  |     |  +- leather
|  |     |  |  +- flgloves
|  |     |  |  +- hbracers
|  |     |  |  +- heavy
|  |     |  |  +- hlgloves
|  |     |  |  +- hlhelmet
|  |     |  |  +- hpants
|  |     |  |  +- khelmet
|  |     |  |  +- Lbracers
|  |     |  |  +- lgloves
|  |     |  |  +- lhelmet
|  |     |  |  `- pants
|  |     |  +- lockpicks
|  |     |  +- longbow
|  |     |  +- Mancatcher
|  |     |  +- Navaja
|  |     |  +- parrydag
|  |     |  +- quiver
|  |     |  +- quivers
|  |     |  |  +- arrows
|  |     |  |  |  +- poison
|  |     |  |  |  `- steel
|  |     |  |  `- bolts
|  |     |  |     +- light
|  |     |  |     `- pyro
|  |     |  +- recurvebow
|  |     |  +- runicflask
|  |     |  +- slurbow
|  |     |  +- splintbracers
|  |     |  +- splintlegs
|  |     |  `- steeltossblades
|  |     +- Knight
|  |     |  +- armet
|  |     |  +- Bevor
|  |     |  +- BFlamberge
|  |     |  +- bracers
|  |     |  +- coif
|  |     |  +- coiffull
|  |     |  +- ebeak
|  |     |  +- estoc
|  |     |  +- flutedFullplate
|  |     |  +- froggy
|  |     |  +- Fullplate
|  |     |  +- gmace
|  |     |  +- gorget
|  |     |  +- greatsword
|  |     |  +- halfplate
|  |     |  +- Haubergeon
|  |     |  +- hauberk
|  |     |  +- hgambeson
|  |     |  +- kiteshield
|  |     |  +- knighthelm
|  |     |  +- knighthelmold
|  |     |  +- lsword
|  |     |  +- mblacksteelfullplate
|  |     |  +- mblkplateboots
|  |     |  +- mblkplatechausses
|  |     |  +- mblkplategaunt
|  |     |  +- mblkstelarmet
|  |     |  +- plateboots
|  |     |  +- platechausses
|  |     |  +- plategaunt
|  |     |  +- saiga
|  |     |  +- sbelt
|  |     |  +- SFlamberge
|  |     |  +- SGaxeknight
|  |     |  `- sgorget
|  |     +- light_armor
|  |     |  +- arming_jacket
|  |     |  +- gambeson
|  |     |  +- grenzel_hat
|  |     |  +- heavy_leather_armor
|  |     |  +- heavy_leather_coat
|  |     |  +- heavy_leather_gloves
|  |     |  +- heavy_leather_jacket
|  |     |  +- heavy_leather_pants
|  |     |  +- heavy_padded_coif
|  |     |  +- hide_armor
|  |     |  +- leather_bracers
|  |     |  +- leather_gorget
|  |     |  +- lightgambeson
|  |     |  +- padded_gambeson
|  |     |  +- paddedcoif
|  |     |  +- sewingkit
|  |     |  +- spellsigner_robes
|  |     |  +- spellsinger_hat
|  |     |  +- studded_leather_armor
|  |     |  `- studded_leather_cuirass
|  |     +- livestock
|  |     |  +- cat
|  |     |  +- chicken
|  |     |  +- cow
|  |     |  +- goat
|  |     |  +- hog
|  |     |  +- hog_rider
|  |     |  +- pig
|  |     |  +- queen_bee
|  |     |  +- saiga
|  |     |  `- swine
|  |     +- luxury
|  |     |  +- canvas
|  |     |  +- circlet
|  |     |  +- easel
|  |     |  +- fancyteaset
|  |     |  +- fineparasol
|  |     |  +- goldring
|  |     |  +- listenst
|  |     |  +- manaflower
|  |     |  +- merctoken
|  |     |  +- moondust
|  |     |  +- nomag
|  |     |  +- ozium
|  |     |  +- paintbrush
|  |     |  +- paintpalette
|  |     |  +- parasol
|  |     |  +- polishing_kit
|  |     |  +- scrying
|  |     |  +- signet
|  |     |  +- silverastcross
|  |     |  +- silverdagger
|  |     |  +- silvernecracross
|  |     |  +- silvernoccross
|  |     |  +- silverpsicross
|  |     |  +- silvertencross
|  |     |  +- spice
|  |     |  `- talkstone
|  |     +- Mage
|  |     |  +- book
|  |     |  +- coolhat
|  |     |  +- coolrobes
|  |     |  +- gambeson
|  |     |  +- gorget
|  |     |  +- grand_implement
|  |     |  +- greater_implement
|  |     |  +- hgambeson
|  |     |  +- icoif
|  |     |  +- leather
|  |     |  |  +- hbracers
|  |     |  |  +- hpants
|  |     |  |  +- Lbracers
|  |     |  |  +- lgloves
|  |     |  |  +- Lhelmet
|  |     |  |  +- pants
|  |     |  |  +- qstaff
|  |     |  |  +- sqstaff
|  |     |  |  `- woodenstaff
|  |     |  +- lesser_implement
|  |     |  +- nomag
|  |     |  +- ring_swiftness
|  |     |  +- ring_vitality
|  |     |  +- ring_wisdom
|  |     |  +- scryorb
|  |     |  +- sdagger
|  |     |  +- serfstone
|  |     |  +- talkstone
|  |     |  `- witchhat
|  |     +- merc_weapons
|  |     |  +- beardedaxe
|  |     |  +- erapier
|  |     |  +- etruscanlongsword
|  |     |  +- glaive
|  |     |  +- grenzelstaff
|  |     |  +- handclaw_iron
|  |     |  +- handclaw_steel
|  |     |  +- katana
|  |     |  +- kazengunhookblade
|  |     |  +- kazengunkodachi
|  |     |  +- kazengunscabbard
|  |     |  +- kazenguntanto
|  |     |  +- nagaika
|  |     |  +- naginata
|  |     |  +- naledistaff
|  |     |  +- navaja
|  |     |  +- pulaxe
|  |     |  +- saildagger
|  |     |  `- shamshir
|  |     +- potions
|  |     |  +- antidote
|  |     |  +- bottlebombs
|  |     |  +- conpot
|  |     |  +- endpot
|  |     |  +- healthpot
|  |     |  +- intpot
|  |     |  +- lucpot
|  |     |  +- manapot
|  |     |  +- perpot
|  |     |  +- rotcure
|  |     |  +- runicflask
|  |     |  +- spdpot
|  |     |  +- stamina
|  |     |  `- strpot
|  |     +- ranged_weapons
|  |     |  +- crossbow
|  |     |  |  `- slurbow
|  |     |  +- hurlbat
|  |     |  +- javeliniron
|  |     |  +- javelinsteel
|  |     |  +- longbow
|  |     |  +- net
|  |     |  +- quiver
|  |     |  +- quivers
|  |     |  |  +- arrows
|  |     |  |  +- barrows
|  |     |  |  +- bolts
|  |     |  |  +- lightbolts
|  |     |  |  +- poisonarrows
|  |     |  |  `- pyrobolts
|  |     |  +- recurvebow
|  |     |  +- slingandpouch
|  |     |  +- slingiron
|  |     |  +- tossbladeiron
|  |     |  `- tossbladesteel
|  |     +- rawmats
|  |     |  +- ash
|  |     |  +- cloth
|  |     |  +- coal
|  |     |  +- copper
|  |     |  +- iron
|  |     |  +- lumber
|  |     |  +- silver
|  |     |  +- stones
|  |     |  `- tin
|  |     +- seeds
|  |     |  +- apple
|  |     |  +- berries
|  |     |  +- berry
|  |     |  +- cabbage
|  |     |  +- coffee
|  |     |  +- fruits
|  |     |  +- onion
|  |     |  +- poppy
|  |     |  +- potato
|  |     |  +- rocknut
|  |     |  +- spelt
|  |     |  +- sugarcane
|  |     |  +- swampweed
|  |     |  +- tea
|  |     |  `- weed
|  |     +- Sellsword
|  |     |  +- Bevor
|  |     |  +- bolts
|  |     |  +- boots
|  |     |  +- bracers
|  |     |  +- buckler
|  |     |  +- chaingauntlets
|  |     |  +- chainlegs
|  |     |  +- coif
|  |     |  +- coiffull
|  |     |  +- crossbow
|  |     |  +- ebeak
|  |     |  +- Etruscancrate
|  |     |  +- Forlorncrate
|  |     |  +- Grenzelcrate
|  |     |  +- halberd
|  |     |  +- hauberk
|  |     |  +- heatshield
|  |     |  +- hgambeson
|  |     |  +- lance
|  |     |  +- Longswordcrate
|  |     |  +- lsword
|  |     |  +- Otavancrate
|  |     |  +- partizan
|  |     |  +- sallet
|  |     |  +- sgorget
|  |     |  +- shortsword
|  |     |  +- steelcuirass
|  |     |  +- steelmask
|  |     |  +- SZweihandersword
|  |     |  `- visoredsallet
|  |     +- steel_weapons
|  |     |  +- aplongsword
|  |     |  +- battleaxe
|  |     |  +- billhook
|  |     |  +- boarspear
|  |     |  +- broadsword
|  |     |  +- chefcleaver
|  |     |  +- chefknife
|  |     |  +- cutlass
|  |     |  +- dagger
|  |     |  +- eaglebeak
|  |     |  +- estoc
|  |     |  +- falchion
|  |     |  +- falx
|  |     |  +- fishingspear
|  |     |  +- flail
|  |     |  +- grandmace
|  |     |  +- greataxe
|  |     |  +- greataxedoublehead
|  |     |  +- greataxeknight
|  |     |  +- greatsword
|  |     |  +- halberd
|  |     |  +- katar
|  |     |  +- kriegmesser
|  |     |  +- lance
|  |     |  +- longsword
|  |     |  +- mace
|  |     |  +- messer
|  |     |  +- messeralt
|  |     |  +- partizan
|  |     |  +- rapier
|  |     |  +- rhomphaia
|  |     |  +- rondeldagger
|  |     |  +- sabre
|  |     |  +- sflangedmace
|  |     |  +- shortsword
|  |     |  +- steelknuckle
|  |     |  +- sword
|  |     |  `- warhammer
|  |     +- Things
|  |     |  +- backpack
|  |     |  +- bandages
|  |     |  +- belt
|  |     |  +- chain
|  |     |  +- clotchkit
|  |     |  +- cloth
|  |     |  +- coppiette
|  |     |  +- Dragonscale
|  |     |  +- goldenapple
|  |     |  +- gwstrap
|  |     |  +- hardtack
|  |     |  +- healthpot
|  |     |  +- healthpotstrong
|  |     |  +- hknife
|  |     |  +- Lamp
|  |     |  +- manapot
|  |     |  +- manapotstrong
|  |     |  +- metalkit
|  |     |  +- moondust
|  |     |  +- needle
|  |     |  +- ozium
|  |     |  +- rubyband
|  |     |  +- satchel
|  |     |  +- scabbard_knife
|  |     |  +- scabbard_sword
|  |     |  +- smokebomb
|  |     |  +- spice
|  |     |  +- stampot
|  |     |  +- stampotstrong
|  |     |  +- swampweed
|  |     |  +- twstrap
|  |     |  +- Waterskin
|  |     |  `- westleach
|  |     +- tools
|  |     |  +- alch_bottle
|  |     |  +- alch_bottles
|  |     |  +- bait
|  |     |  +- bottl
|  |     |  +- bottle_kit
|  |     |  +- chains
|  |     |  +- chisel
|  |     |  +- flint
|  |     |  +- fryingpan
|  |     |  +- hammer
|  |     |  +- handsaw
|  |     |  +- headhook
|  |     |  +- herbsoap
|  |     |  +- hoe
|  |     |  +- huntingknife
|  |     |  +- ironpick
|  |     |  +- keyrings
|  |     |  +- lockpicks
|  |     |  +- metalkit
|  |     |  +- paper
|  |     |  +- pfork
|  |     |  +- pipes
|  |     |  +- plough
|  |     |  +- prarml
|  |     |  +- prarmr
|  |     |  +- prlegl
|  |     |  +- prlegr
|  |     |  +- sacks
|  |     |  +- scissors
|  |     |  +- scomst
|  |     |  +- scythe
|  |     |  +- serfst
|  |     |  +- shopkeyy
|  |     |  +- shovel
|  |     |  +- sickle
|  |     |  +- soapps
|  |     |  +- spade
|  |     |  +- surgeonsbag
|  |     |  +- thresher
|  |     |  `- tongs
|  |     `- wardrobe
|  |        +- belt
|  |        |  +- battleskirt
|  |        |  `- battleskirt_faulds
|  |        +- caparison
|  |        |  +- caparison
|  |        |  +- caparison_astrata
|  |        |  +- caparison_eora
|  |        |  +- caparison_fogbeast
|  |        |  `- caparison_psy
|  |        +- cloaks
|  |        |  +- bandolier
|  |        |  +- bcloaks
|  |        |  +- blackshroud
|  |        |  +- blacktabard
|  |        |  +- direbear
|  |        |  +- direbear_light
|  |        |  +- fitted_cloak
|  |        |  +- furcloak
|  |        |  +- gcloaks
|  |        |  +- halfcloak
|  |        |  +- jupon
|  |        |  +- jupon_short
|  |        |  +- poncho
|  |        |  +- rcloaks
|  |        |  +- ridercloak
|  |        |  +- scarletshroud
|  |        |  +- scarlettabard
|  |        |  +- surcoat
|  |        |  +- tabard
|  |        |  `- thief_cloak
|  |        +- collar
|  |        |  +- bell_collar
|  |        |  +- collar
|  |        |  +- cursed_collar
|  |        |  `- forlorn_collar
|  |        +- gloves
|  |        |  +- clothwrap
|  |        |  +- fgloves
|  |        |  +- handwraps
|  |        |  `- leather
|  |        +- hat
|  |        |  +- bardhat
|  |        |  +- chaperon
|  |        |  +- deserthood
|  |        |  +- duelist_hat
|  |        |  +- fancyhat
|  |        |  +- folded_hat
|  |        |  +- furhat
|  |        |  +- headband
|  |        |  +- heavyhood
|  |        |  +- hijab
|  |        |  +- hood
|  |        |  +- keffiyeh
|  |        |  +- nightmanhat
|  |        |  +- nunveil
|  |        |  +- nurseveil
|  |        |  +- papakha
|  |        |  +- physicianhat
|  |        |  +- smokingcap
|  |        |  `- witchhat
|  |        +- masks
|  |        |  +- goldmask
|  |        |  +- goldspecs
|  |        |  +- halfmask
|  |        |  +- ragmask
|  |        |  `- specs
|  |        +- packages
|  |        |  +- jester_pack
|  |        |  +- maid_pack
|  |        |  `- maid_pack_supreme
|  |        +- pants
|  |        |  +- desertskirt
|  |        |  +- formal
|  |        |  +- leather_pants
|  |        |  +- leather_shorts
|  |        |  +- sailor_pants
|  |        |  +- skirt
|  |        |  `- tights
|  |        +- shirt
|  |        |  +- blackforeignshirt
|  |        |  +- desertbra
|  |        |  +- lowcut
|  |        |  +- shirt
|  |        |  +- striped_shirt
|  |        |  +- tunic
|  |        |  +- undervestements
|  |        |  `- whiteforeignshirt
|  |        +- shoes
|  |        |  +- clothanklets
|  |        |  +- darkboots
|  |        |  +- furanklets
|  |        |  +- leather
|  |        |  +- noble
|  |        |  +- ridingboots
|  |        |  +- sandals
|  |        |  `- shalal
|  |        `- suits
|  |           +- anklets
|  |           +- bardress
|  |           +- blackdress
|  |           +- bluedress
|  |           +- fallgown
|  |           +- formal
|  |           +- gown
|  |           +- magerobes
|  |           +- maid_pack_shitty
|  |           +- nunhabit
|  |           +- silkbelt
|  |           +- silkbra
|  |           +- silkmask
|  |           +- stockings_black
|  |           +- stockings_black_fishnet
|  |           +- stockings_black_silk
|  |           +- stockings_blue
|  |           +- stockings_blue_fishnet
|  |           +- stockings_blue_silk
|  |           +- stockings_knee_white
|  |           +- stockings_purple
|  |           +- stockings_purple_fishnet
|  |           +- stockings_purple_silk
|  |           +- stockings_red
|  |           +- stockings_red_fishnet
|  |           +- stockings_red_silk
|  |           +- stockings_thigh_white
|  |           +- stockings_white
|  |           +- stockings_white_fishnet
|  |           +- stockings_white_silk
|  |           +- strapless_dress_black
|  |           +- strapless_dress_blue
|  |           +- strapless_dress_purple
|  |           +- strapless_dress_red
|  |           +- summergown
|  |           +- whiterobes
|  |           `- wintergown
|  +- surgery
|  |  +- advanced
|  |  +- amputation
|  |  +- augmentation
|  |  +- bloodletting
|  |  +- cure_black_rot
|  |  +- cure_rot
|  |  +- embedded_removal
|  |  +- extract_lux
|  |  +- fix_bone
|  |  +- healing
|  |  +- organ_manipulation
|  |  |  `- soft
|  |  +- plastic_surgery
|  |  +- prosthetic_removal
|  |  +- prosthetic_replacement
|  |  +- relocate_bone
|  |  +- rogue_revival
|  |  `- rogue_revival_with_a_big_fat_tick
|  +- surgery_step
|  |  +- add_prosthetic
|  |  +- add_taur
|  |  +- amputate
|  |  +- bloodlet
|  |  +- burn_rot
|  |  +- cauterize
|  |  +- clamp
|  |  +- cutvein
|  |  +- drill
|  |  +- extract_black_rose_residue
|  |  +- extract_lux
|  |  +- heal
|  |  |  +- brute
|  |  |  |  +- basic
|  |  |  |  `- upgraded
|  |  |  |     `- femto
|  |  |  +- burn
|  |  |  |  +- basic
|  |  |  |  `- upgraded
|  |  |  |     `- femto
|  |  |  `- combo
|  |  |     `- upgraded
|  |  |        `- femto
|  |  +- incise
|  |  +- infuse_lux
|  |  +- infuse_tick
|  |  +- make_organs
|  |  +- manipulate_organs
|  |  +- mouth_to_mouth
|  |  +- relocate_bone
|  |  +- remove_external_organs
|  |  +- remove_object
|  |  +- remove_prosthetic
|  |  +- replace_limb
|  |  +- reshape_face
|  |  +- retract
|  |  +- saw
|  |  `- set_bone
|  +- targetting_datum
|  |  `- basic
|  |     +- allow_items
|  |     +- ignore_faction
|  |     `- not_friends
|  |        +- allow_items
|  |        `- attack_closed_turfs
|  +- team
|  |  +- custom
|  |  +- nation
|  |  `- prebels
|  +- tennite_schism
|  +- tgs_api
|  |  +- latest
|  |  +- v3210
|  |  +- v4
|  |  `- v5
|  +- tgs_chat_channel
|  +- tgs_chat_command
|  |  +- adminwho
|  |  +- ahelp
|  |  +- endnotify
|  |  +- irccheck
|  |  +- ircstatus
|  |  +- namecheck
|  |  +- notify
|  |  +- reload_admins
|  |  +- sdql
|  |  +- verify
|  |  +- whitelist_add
|  |  `- whitelist_remove
|  +- tgs_chat_embed
|  |  +- field
|  |  +- footer
|  |  +- media
|  |  +- provider
|  |  |  `- author
|  |  `- structure
|  +- tgs_chat_user
|  +- tgs_event_handler
|  +- tgs_message_content
|  +- tgs_revision_information
|  |  `- test_merge
|  +- tgs_version
|  +- tgui
|  +- tgui_alert
|  |  `- async
|  +- tgui_checkbox_input
|  +- tgui_color_picker
|  +- tgui_input_number
|  +- tgui_input_text
|  +- tgui_list_input
|  +- tgui_panel
|  +- tgui_say
|  +- tgui_window
|  +- theme_picker
|  +- threat_region
|  +- threat_region_display
|  +- thrownthing
|  +- time_of_day
|  |  +- dawn
|  |  +- daytime
|  |  +- dusk
|  |  +- midnight
|  |  +- sunrise
|  |  `- sunset
|  +- timedevent
|  +- trade_request
|  +- triumph_buy
|  |  +- female_power
|  |  +- grenzelhoft_maximum
|  |  +- pick_any_class
|  |  `- wipe_triumphs
|  +- triumph_buy_menu
|  +- turf_reservation
|  |  `- transit
|  +- ui_state
|  |  +- admin_state
|  |  `- not_incapacitated_state
|  |     `- standing
|  +- unit_test
|  |  +- find_reference_sanity
|  |  +- focus_only
|  |  +- reagent_id_typos
|  |  `- reagent_recipe_collisions
|  +- universal_icon
|  +- usurpation_rite
|  |  +- golden_accord
|  |  +- lunar_ascension
|  |  +- martial_supercession
|  |  +- popular_acclaim
|  |  +- progressive_dominion
|  |  +- psydonian_tribunal
|  |  +- sacred_supercession
|  |  `- solar_succession
|  +- vampire_project
|  |  +- armor_crafting
|  |  +- power_growth
|  |  +- power_growth_2
|  |  +- power_growth_3
|  |  +- power_growth_4
|  |  +- servant
|  |  |  +- servant_t1
|  |  |  +- servant_t2
|  |  |  `- servant_t3
|  |  `- sunsteal
|  +- verbs
|  |  `- menu
|  |     `- Settings
|  |        `- Ghost
|  |           `- chatterbox
|  |              `- Events
|  +- vine_controller
|  +- vine_mutation
|  |  +- aggressive_spread
|  |  +- earthy
|  |  +- explosive
|  |  +- fire_proof
|  |  +- healing
|  |  +- light
|  |  +- thorns
|  |  +- toxicity
|  |  +- transparency
|  |  +- vine_eating
|  |  `- woodening
|  +- virtue
|  |  +- combat
|  |  |  +- bowman
|  |  |  +- combat_aware
|  |  |  +- combat_virtue
|  |  |  +- crossbowman
|  |  |  +- devotee
|  |  |  |  `- astratan_affinity
|  |  |  +- dualwielder
|  |  |  +- guarded
|  |  |  +- magical_potential
|  |  |  +- pallid
|  |  |  +- rotcured
|  |  |  `- sharp
|  |  +- heretic
|  |  |  `- zchurch_keyholder
|  |  +- items
|  |  |  `- arsonist
|  |  +- movement
|  |  |  `- acrobatic
|  |  +- none
|  |  +- origin
|  |  |  +- avar
|  |  |  +- azuria
|  |  |  +- etrusca
|  |  |  +- grenzelhoft
|  |  |  +- gronn
|  |  |  +- hammerhold
|  |  |  +- kazengun
|  |  |  +- lingyue
|  |  |  +- lirvas
|  |  |  +- naledi
|  |  |  +- otava
|  |  |  +- racial
|  |  |  |  `- underdark
|  |  |  +- raneshen
|  |  |  `- unknown
|  |  +- size
|  |  |  `- giant
|  |  +- thief
|  |  |  `- drug_runner
|  |  `- utility
|  |     +- apprentice
|  |     +- bronzelimbs
|  |     +- deadened
|  |     +- failed_squire
|  |     +- feral_appetite
|  |     +- feytouched
|  |     +- granary
|  |     +- hollow
|  |     +- homesteader
|  |     +- intellectual
|  |     +- keenears
|  |     +- mountable
|  |     +- noble
|  |     +- notable
|  |     +- performer
|  |     +- prowler
|  |     +- riding
|  |     +- skilled
|  |     +- tracker
|  |     +- ugly
|  |     `- woodwalker
|  +- voicepack
|  |  +- female
|  |  |  +- dainty
|  |  |  +- haughty
|  |  |  `- warrior
|  |  `- male
|  |     +- foppish
|  |     +- knight
|  |     +- stern
|  |     `- warrior
|  +- weakref
|  +- weather
|  |  +- floor_is_lava
|  |  `- rain
|  +- withdraw_tab
|  +- world_faction
|  +- world_topic
|  |  +- adminmsg
|  |  +- adminwho
|  |  +- ahelp_relay
|  |  +- namecheck
|  |  +- news_report
|  |  +- ping
|  |  +- playing
|  |  +- pr_announce
|  |  +- server_hop
|  |  `- status
|  +- world_trait
|  |  +- abyssor_rage
|  |  +- baotha_revelry
|  |  +- dendor_drought
|  |  +- dendor_fertility
|  |  +- fertility
|  |  +- fishing_decrease
|  |  +- fishing_increase
|  |  +- goblin_siege
|  |  +- malum_diligence
|  |  +- matthios_fingers
|  |  +- necra_requiem
|  |  +- noc_wisdom
|  |  +- pestra_mercy
|  |  +- rousman_siege
|  |  +- skeleton_siege
|  |  +- zizo_defilement
|  |  `- zizo_pet_cementery
|  `- wound
|     +- artery
|     |  +- chest
|     |  +- neck
|     |  `- reattachment
|     +- bite
|     |  +- large
|     |  `- small
|     +- bruise
|     |  +- large
|     |  +- small
|     |  `- woundheal
|     +- cbt
|     |  `- permanent
|     +- dislocation
|     |  `- neck
|     +- dismemberment
|     |  +- head
|     |  +- l_arm
|     |  +- l_leg
|     |  +- r_arm
|     |  +- r_leg
|     |  `- taur
|     +- dynamic
|     |  +- bite
|     |  +- bruise
|     |  +- gouge
|     |  +- lashing
|     |  +- puncture
|     |  +- punish
|     |  `- slash
|     +- facial
|     |  +- disfigurement
|     |  |  `- nose
|     |  +- ears
|     |  +- eyes
|     |  |  +- left
|     |  |  |  `- permanent
|     |  |  `- right
|     |  |     `- permanent
|     |  `- tongue
|     +- fracture
|     |  +- chest
|     |  +- groin
|     |  +- head
|     |  |  +- brain
|     |  |  |  `- shatter
|     |  |  +- ears
|     |  |  +- eyes
|     |  |  +- nose
|     |  |  `- shatter
|     |  +- mouth
|     |  +- neck
|     |  |  `- shatter
|     |  `- no_bleed
|     +- grievous
|     |  +- pre_decapitation_blunt
|     |  `- pre_decapitation_sharp
|     +- lashing
|     |  +- large
|     |  `- small
|     +- nocburn
|     +- puncture
|     |  +- drilling
|     |  +- large
|     |  `- small
|     +- scarring
|     +- slash
|     |  +- disembowel
|     |  +- incision
|     |  +- large
|     |  +- small
|     |  `- vein
|     `- sunder
|        +- chest
|        `- head
+- mob
|  +- camera
|  +- dead
|  |  +- new_player
|  |  `- observer
|  |     +- admin
|  |     +- rogue
|  |     |  +- arcaneeye
|  |     |  `- nodraw
|  |     `- screye
|  |        `- blackmirror
|  +- dview
|  +- living
|  |  +- brain
|  |  +- carbon
|  |  |  +- human
|  |  |  |  +- dummy
|  |  |  |  `- species
|  |  |  |     +- aasimar
|  |  |  |     +- akula
|  |  |  |     +- anthromorph
|  |  |  |     +- anthromorphsmall
|  |  |  |     +- construct
|  |  |  |     |  `- metal
|  |  |  |     |     `- zizoconstruct
|  |  |  |     |        `- ambush
|  |  |  |     +- demihuman
|  |  |  |     +- dracon
|  |  |  |     +- dullahan
|  |  |  |     +- dwarf
|  |  |  |     |  +- gnome
|  |  |  |     |  `- mountain
|  |  |  |     +- dwarfskeleton
|  |  |  |     |  `- ambush
|  |  |  |     |     `- knight
|  |  |  |     |        `- summoned
|  |  |  |     +- elf
|  |  |  |     |  +- dark
|  |  |  |     |  |  `- drowraider
|  |  |  |     |  |     +- ambush
|  |  |  |     |  |     +- disarmed_test
|  |  |  |     |  |     +- spear_test
|  |  |  |     |  |     +- sword_test
|  |  |  |     |  |     `- whip_test
|  |  |  |     |  +- sun
|  |  |  |     |  `- wood
|  |  |  |     +- gnoll
|  |  |  |     |  +- female
|  |  |  |     |  `- male
|  |  |  |     +- goblin
|  |  |  |     |  +- cave
|  |  |  |     |  +- hell
|  |  |  |     |  +- moon
|  |  |  |     |  +- npc
|  |  |  |     |  |  +- ambush
|  |  |  |     |  |  |  +- cave
|  |  |  |     |  |  |  +- hell
|  |  |  |     |  |  |  +- moon
|  |  |  |     |  |  |  `- sea
|  |  |  |     |  |  +- archer
|  |  |  |     |  |  +- cave
|  |  |  |     |  |  +- hell
|  |  |  |     |  |  +- large
|  |  |  |     |  |  +- moon
|  |  |  |     |  |  +- sea
|  |  |  |     |  |  `- slinger
|  |  |  |     |  `- sea
|  |  |  |     +- goblinp
|  |  |  |     +- halforc
|  |  |  |     +- human
|  |  |  |     |  +- halfelf
|  |  |  |     |  `- northern
|  |  |  |     |     +- bog_deserters
|  |  |  |     |     |  +- ambush
|  |  |  |     |     |  `- better_gear
|  |  |  |     |     |     `- ambush
|  |  |  |     |     +- border_reiver
|  |  |  |     |     |  +- highgear
|  |  |  |     |     |  |  `- ambush
|  |  |  |     |     |  +- lowgear
|  |  |  |     |     |  |  `- ambush
|  |  |  |     |     |  `- midgear
|  |  |  |     |     |     `- ambush
|  |  |  |     |     +- bum
|  |  |  |     |     |  `- ambush
|  |  |  |     |     +- deranged_knight
|  |  |  |     |     |  +- graggar
|  |  |  |     |     |  +- hedgeknight
|  |  |  |     |     |  +- matthios
|  |  |  |     |     |  `- zizo
|  |  |  |     |     +- heretical_fiend_no_gear
|  |  |  |     |     |  `- zizo_cultist
|  |  |  |     |     |     `- ambush
|  |  |  |     |     +- highwayman
|  |  |  |     |     |  +- ambush
|  |  |  |     |     |  `- dk_goon
|  |  |  |     |     +- mad_touched_treasure_hunter
|  |  |  |     |     |  `- ambush
|  |  |  |     |     +- militia
|  |  |  |     |     |  +- ambush
|  |  |  |     |     |  +- deserter
|  |  |  |     |     |  `- guard
|  |  |  |     |     +- outlaw_duelist
|  |  |  |     |     +- outlaw_ranger
|  |  |  |     |     +- outlaw_tank
|  |  |  |     |     +- searaider
|  |  |  |     |     |  `- ambush
|  |  |  |     |     `- thief
|  |  |  |     +- kobold
|  |  |  |     +- lizardfolk
|  |  |  |     |  `- psy_vault_guard
|  |  |  |     |     `- ambush
|  |  |  |     +- lupian
|  |  |  |     +- moth
|  |  |  |     +- npc
|  |  |  |     |  +- arcyne_invoker
|  |  |  |     |  `- deadite
|  |  |  |     +- orc
|  |  |  |     |  `- npc
|  |  |  |     |     +- archer
|  |  |  |     |     +- berserker
|  |  |  |     |     +- footsoldier
|  |  |  |     |     +- marauder
|  |  |  |     |     `- warlord
|  |  |  |     +- skeleton
|  |  |  |     |  +- no_equipment
|  |  |  |     |  `- npc
|  |  |  |     |     +- ambush
|  |  |  |     |     +- archer
|  |  |  |     |     +- bogguard
|  |  |  |     |     |  `- master
|  |  |  |     |     +- dungeon
|  |  |  |     |     |  `- lich
|  |  |  |     |     +- easy
|  |  |  |     |     +- hard
|  |  |  |     |     |  `- noequip
|  |  |  |     |     +- medium
|  |  |  |     |     |  `- noequip
|  |  |  |     |     +- mediumspread
|  |  |  |     |     |  `- lich
|  |  |  |     |     +- no_equipment
|  |  |  |     |     +- pirate
|  |  |  |     |     +- special
|  |  |  |     |     |  +- disgraced_noble
|  |  |  |     |     |  `- vile_doctor
|  |  |  |     |     `- supereasy
|  |  |  |     +- tabaxi
|  |  |  |     +- tieberian
|  |  |  |     +- vulpkanin
|  |  |  |     +- werewolf
|  |  |  |     |  +- female
|  |  |  |     |  `- male
|  |  |  |     `- wildshape
|  |  |  |        +- bear
|  |  |  |        +- cabbit
|  |  |  |        +- cat
|  |  |  |        +- dendormole
|  |  |  |        +- fox
|  |  |  |        +- hag
|  |  |  |        +- mirecrawler
|  |  |  |        +- saiga
|  |  |  |        +- spider
|  |  |  |        `- volf
|  |  |  +- monkey
|  |  |  |  +- angry
|  |  |  |  `- punpun
|  |  |  `- spirit
|  |  +- simple_animal
|  |  |  +- butterfly
|  |  |  +- chick
|  |  |  +- chicken
|  |  |  +- cockroach
|  |  |  +- cow
|  |  |  +- flesh_decoy
|  |  |  +- grenchensnacker
|  |  |  +- hostile
|  |  |  |  +- boss
|  |  |  |  |  +- baroness
|  |  |  |  |  +- fishboss
|  |  |  |  |  `- lich
|  |  |  |  +- lizard
|  |  |  |  |  `- space
|  |  |  |  +- retaliate
|  |  |  |  |  +- bat
|  |  |  |  |  |  `- crow
|  |  |  |  |  +- frog
|  |  |  |  |  +- gaseousform
|  |  |  |  |  +- ghost
|  |  |  |  |  +- goat
|  |  |  |  |  +- goose
|  |  |  |  |  |  `- vomit
|  |  |  |  |  +- poison
|  |  |  |  |  |  `- snake
|  |  |  |  |  +- rogue
|  |  |  |  |  |  +- bigrat
|  |  |  |  |  |  |  `- gethsmane
|  |  |  |  |  |  +- bull
|  |  |  |  |  |  +- cat
|  |  |  |  |  |  +- chicken
|  |  |  |  |  |  +- cow
|  |  |  |  |  |  |  +- bullet
|  |  |  |  |  |  |  `- cowlet
|  |  |  |  |  |  +- direbear
|  |  |  |  |  |  +- dragon
|  |  |  |  |  |  |  `- broodmother
|  |  |  |  |  |  +- drider
|  |  |  |  |  |  |  `- tame
|  |  |  |  |  |  +- elemental
|  |  |  |  |  |  |  +- behemoth
|  |  |  |  |  |  |  +- colossus
|  |  |  |  |  |  |  +- crawler
|  |  |  |  |  |  |  `- warden
|  |  |  |  |  |  +- fae
|  |  |  |  |  |  |  +- dryad
|  |  |  |  |  |  |  +- glimmerwing
|  |  |  |  |  |  |  +- sprite
|  |  |  |  |  |  |  `- sylph
|  |  |  |  |  |  +- fogbeast
|  |  |  |  |  |  |  +- kid
|  |  |  |  |  |  |  |  `- male
|  |  |  |  |  |  |  +- male
|  |  |  |  |  |  |  |  `- tame
|  |  |  |  |  |  |  `- tame
|  |  |  |  |  |  +- fox
|  |  |  |  |  |  |  +- guildpet
|  |  |  |  |  |  |  `- witch_shifted
|  |  |  |  |  |  +- goat
|  |  |  |  |  |  |  +- goatlet
|  |  |  |  |  |  |  +- goatletboy
|  |  |  |  |  |  |  `- tame
|  |  |  |  |  |  +- goatmale
|  |  |  |  |  |  |  `- tame
|  |  |  |  |  |  +- hag_shapeshift
|  |  |  |  |  |  +- headless
|  |  |  |  |  |  +- infernal
|  |  |  |  |  |  |  +- fiend
|  |  |  |  |  |  |  +- hellhound
|  |  |  |  |  |  |  +- imp
|  |  |  |  |  |  |  `- watcher
|  |  |  |  |  |  +- lamia
|  |  |  |  |  |  +- leylinelycan
|  |  |  |  |  |  +- mimic
|  |  |  |  |  |  |  `- gold
|  |  |  |  |  |  +- minotaur
|  |  |  |  |  |  |  +- axe
|  |  |  |  |  |  |  |  +- female
|  |  |  |  |  |  |  |  `- wounded
|  |  |  |  |  |  |  +- female
|  |  |  |  |  |  |  +- original
|  |  |  |  |  |  |  `- wounded
|  |  |  |  |  |  |     `- chained
|  |  |  |  |  |  +- mirespider
|  |  |  |  |  |  |  `- angry
|  |  |  |  |  |  +- mole
|  |  |  |  |  |  +- mossback
|  |  |  |  |  |  +- mudcrab
|  |  |  |  |  |  |  `- cabbit
|  |  |  |  |  |  |     `- witch_shifted
|  |  |  |  |  |  +- orc
|  |  |  |  |  |  |  +- event
|  |  |  |  |  |  |  +- orc2
|  |  |  |  |  |  |  |  `- event
|  |  |  |  |  |  |  +- orc_marauder
|  |  |  |  |  |  |  |  +- event
|  |  |  |  |  |  |  |  +- ravager
|  |  |  |  |  |  |  |  |  `- event
|  |  |  |  |  |  |  |  `- spear
|  |  |  |  |  |  |  |     `- event
|  |  |  |  |  |  |  +- ranged
|  |  |  |  |  |  |  |  `- event
|  |  |  |  |  |  |  +- spear
|  |  |  |  |  |  |  |  `- event
|  |  |  |  |  |  |  `- spear2
|  |  |  |  |  |  |     `- event
|  |  |  |  |  |  +- primordial
|  |  |  |  |  |  |  +- air
|  |  |  |  |  |  |  +- fire
|  |  |  |  |  |  |  `- water
|  |  |  |  |  |  +- revenant
|  |  |  |  |  |  |  +- dragon
|  |  |  |  |  |  |  +- mirespider
|  |  |  |  |  |  |  +- mirespider_lurker
|  |  |  |  |  |  |  +- weak
|  |  |  |  |  |  |  `- wolf
|  |  |  |  |  |  +- saiga
|  |  |  |  |  |  |  +- saigaboy
|  |  |  |  |  |  |  +- saigabuck
|  |  |  |  |  |  |  |  `- tame
|  |  |  |  |  |  |  +- saigakid
|  |  |  |  |  |  |  +- tame
|  |  |  |  |  |  |  `- undead
|  |  |  |  |  |  +- spider
|  |  |  |  |  |  |  `- mutated
|  |  |  |  |  |  +- swine
|  |  |  |  |  |  |  +- hog
|  |  |  |  |  |  |  |  +- piglet
|  |  |  |  |  |  |  |  `- tame
|  |  |  |  |  |  |  `- piglet
|  |  |  |  |  |  +- troll
|  |  |  |  |  |  |  +- axe
|  |  |  |  |  |  |  +- bog
|  |  |  |  |  |  |  `- cave
|  |  |  |  |  |  +- trufflepig
|  |  |  |  |  |  +- voiddragon
|  |  |  |  |  |  +- voidstoneobelisk
|  |  |  |  |  |  +- werewolf_npc
|  |  |  |  |  |  |  `- f
|  |  |  |  |  |  +- wolf
|  |  |  |  |  |  |  +- badger
|  |  |  |  |  |  |  +- bobcat
|  |  |  |  |  |  |  +- raccoon
|  |  |  |  |  |  |  `- witch_shifted
|  |  |  |  |  |  `- wolf_undead
|  |  |  |  |  `- smallrat
|  |  |  |  |     `- witch_shifted
|  |  |  |  `- rogue
|  |  |  |     +- border_reiver_crossbow
|  |  |  |     +- border_reiver_lance_rider
|  |  |  |     |  `- sabre
|  |  |  |     +- deepone
|  |  |  |     |  +- arm
|  |  |  |     |  |  `- boss
|  |  |  |     |  +- boss
|  |  |  |     |  +- spit
|  |  |  |     |  |  `- boss
|  |  |  |     |  `- wiz
|  |  |  |     |     `- boss
|  |  |  |     +- dragger
|  |  |  |     +- dreamfiend
|  |  |  |     |  +- ancient
|  |  |  |     |  |  `- unbound
|  |  |  |     |  +- major
|  |  |  |     |  |  `- unbound
|  |  |  |     |  `- unbound
|  |  |  |     +- haunt
|  |  |  |     |  `- omen
|  |  |  |     +- mirespider_lurker
|  |  |  |     |  +- angry
|  |  |  |     |  `- mushroom
|  |  |  |     +- mirespider_paralytic
|  |  |  |     |  `- angry
|  |  |  |     +- skeleton
|  |  |  |     |  +- axe
|  |  |  |     |  |  `- event
|  |  |  |     |  +- bow
|  |  |  |     |  |  `- event
|  |  |  |     |  +- guard
|  |  |  |     |  |  `- event
|  |  |  |     |  +- ravox_ghost
|  |  |  |     |  |  +- axe
|  |  |  |     |  |  +- spear
|  |  |  |     |  |  `- sword
|  |  |  |     |  `- spear
|  |  |  |     |     `- event
|  |  |  |     +- spirit_vengeance
|  |  |  |     +- xylixdouble
|  |  |  |     `- zardman_jailer_mage
|  |  |  +- mouse
|  |  |  |  +- brown
|  |  |  |  |  `- Tom
|  |  |  |  +- gray
|  |  |  |  `- white
|  |  |  `- pet
|  |  |     +- cat
|  |  |     |  +- kitten
|  |  |     |  +- original
|  |  |     |  +- Proc
|  |  |     |  +- rogue
|  |  |     |  |  +- black
|  |  |     |  |  |  +- academy
|  |  |     |  |  |  `- witch_shifted
|  |  |     |  |  `- inn
|  |  |     |  +- Runtime
|  |  |     |  `- witch_shifted
|  |  |     +- dog
|  |  |     |  +- corgi
|  |  |     |  |  +- exoticcorgi
|  |  |     |  |  +- Ian
|  |  |     |  |  +- Lisa
|  |  |     |  |  +- narsie
|  |  |     |  |  `- puppy
|  |  |     |  |     `- void
|  |  |     |  `- pug
|  |  |     +- familiar
|  |  |     |  +- ashcoiler
|  |  |     |  +- bat
|  |  |     |  +- cat_black
|  |  |     |  +- cat_pink
|  |  |     |  +- chicken_black
|  |  |     |  +- chicken_brown
|  |  |     |  +- chicken_grey
|  |  |     |  +- chicken_white
|  |  |     |  +- crow
|  |  |     |  +- emberdrake
|  |  |     |  +- frog_green
|  |  |     |  +- frog_purple
|  |  |     |  +- glimmer_hare
|  |  |     |  +- gravemoss_serpent
|  |  |     |  +- hollow_antlerling
|  |  |     |  +- mechanical
|  |  |     |  |  +- brass_thrum
|  |  |     |  |  `- gemspire_beetle
|  |  |     |  +- mist_lynx
|  |  |     |  +- mouse_brown
|  |  |     |  +- mouse_grey
|  |  |     |  +- mouse_white
|  |  |     |  +- mudcrab
|  |  |     |  +- parrot
|  |  |     |  +- pondstone_toad
|  |  |     |  +- rat
|  |  |     |  +- ripplefox
|  |  |     |  +- rune_rat
|  |  |     |  +- snake
|  |  |     |  +- starfield_crow
|  |  |     |  +- thornback_turtle
|  |  |     |  +- vaporroot_wisp
|  |  |     |  `- whisper_stoat
|  |  |     `- fox
|  |  |        `- Renault
|  |  `- split_personality
|  |     `- traitor
|  `- oranges_ear
+- obj
|  +- effect
|  |  +- abstract
|  |  |  +- eye_lighting
|  |  |  +- marker
|  |  |  |  `- at
|  |  |  +- mirage_holder
|  |  |  +- particle_holder
|  |  |  |  `- cached
|  |  |  +- pollution
|  |  |  `- sync_holder
|  |  |     `- veil
|  |  +- acid
|  |  +- after_image
|  |  +- baseturf_helper
|  |  |  +- lava
|  |  |  `- lava_land
|  |  |     `- surface
|  |  +- beam
|  |  +- bee_swarm
|  |  +- bees
|  |  |  `- wild
|  |  +- blade_dance_zone
|  |  +- blessing
|  |  +- buildmode_line
|  |  +- bump_teleporter
|  |  +- countdown
|  |  |  `- hourglass
|  |  +- debugging
|  |  |  +- mapfix_marker
|  |  |  `- marker
|  |  +- decal
|  |  |  +- carpet
|  |  |  |  +- kover_black
|  |  |  |  +- kover_darkred
|  |  |  |  +- kover_purple
|  |  |  |  `- square
|  |  |  |     `- black
|  |  |  +- chempuff
|  |  |  +- cleanable
|  |  |  |  +- black_rot_vomit
|  |  |  |  +- blood
|  |  |  |  |  +- drip
|  |  |  |  |  +- footprints
|  |  |  |  |  |  `- mud
|  |  |  |  |  +- gibs
|  |  |  |  |  |  +- body
|  |  |  |  |  |  +- core
|  |  |  |  |  |  +- down
|  |  |  |  |  |  +- limb
|  |  |  |  |  |  +- old
|  |  |  |  |  |  +- torso
|  |  |  |  |  |  `- up
|  |  |  |  |  +- old
|  |  |  |  |  +- puddle
|  |  |  |  |  +- splatter
|  |  |  |  |  |  `- walls
|  |  |  |  |  +- tracks
|  |  |  |  |  `- xtracks
|  |  |  |  +- chem_pile
|  |  |  |  +- confetti
|  |  |  |  +- coom
|  |  |  |  +- crayon
|  |  |  |  +- debris
|  |  |  |  |  +- glassy
|  |  |  |  |  +- stony
|  |  |  |  |  `- woody
|  |  |  |  +- dirt
|  |  |  |  |  +- cobweb
|  |  |  |  |  |  `- cobweb2
|  |  |  |  |  `- dust
|  |  |  |  +- discharge
|  |  |  |  +- dreamfiend_ichor
|  |  |  |  |  +- huge
|  |  |  |  |  `- large
|  |  |  |  +- food
|  |  |  |  |  +- egg_smudge
|  |  |  |  |  +- flour
|  |  |  |  |  +- mess
|  |  |  |  |  +- pie_smudge
|  |  |  |  |  +- plant_smudge
|  |  |  |  |  +- salt
|  |  |  |  |  `- tomato_smudge
|  |  |  |  +- glitter
|  |  |  |  |  +- blue
|  |  |  |  |  +- pink
|  |  |  |  |  `- white
|  |  |  |  +- greenglow
|  |  |  |  +- heart_blood
|  |  |  |  |  `- small
|  |  |  |  +- heart_shards
|  |  |  |  +- insect
|  |  |  |  +- insectguts
|  |  |  |  +- molten_object
|  |  |  |  |  `- large
|  |  |  |  +- plasma
|  |  |  |  +- robot_debris
|  |  |  |  |  `- old
|  |  |  |  +- roguerune
|  |  |  |  |  +- arcyne
|  |  |  |  |  |  +- binding
|  |  |  |  |  |  |  `- greater
|  |  |  |  |  |  +- enchantment
|  |  |  |  |  |  |  `- greater
|  |  |  |  |  |  +- summoning
|  |  |  |  |  |  |  +- adv
|  |  |  |  |  |  |  +- max
|  |  |  |  |  |  |  `- mid
|  |  |  |  |  |  +- teleport
|  |  |  |  |  |  +- wall
|  |  |  |  |  |  `- wallgreater
|  |  |  |  |  +- blood
|  |  |  |  |  +- divine
|  |  |  |  |  +- druid
|  |  |  |  |  `- god
|  |  |  |  |     +- baotha
|  |  |  |  |     +- dendor
|  |  |  |  |     +- psydon
|  |  |  |  |     `- ravox
|  |  |  |  +- shreds
|  |  |  |  +- sigil
|  |  |  |  |  +- E
|  |  |  |  |  +- N
|  |  |  |  |  +- NE
|  |  |  |  |  +- NW
|  |  |  |  |  +- S
|  |  |  |  |  +- SE
|  |  |  |  |  +- SW
|  |  |  |  |  `- W
|  |  |  |  +- trail_holder
|  |  |  |  +- vomit
|  |  |  |  |  `- old
|  |  |  |  `- xenoblood
|  |  |  |     +- xgibs
|  |  |  |     |  +- body
|  |  |  |     |  +- core
|  |  |  |     |  +- down
|  |  |  |     |  +- larva
|  |  |  |     |  |  `- body
|  |  |  |     |  +- limb
|  |  |  |     |  +- torso
|  |  |  |     |  `- up
|  |  |  |     `- xsplatter
|  |  |  +- cobble
|  |  |  |  `- mossy
|  |  |  +- cobbleedge
|  |  |  +- edge
|  |  |  +- edge_corner
|  |  |  +- herringbone
|  |  |  +- marker_export
|  |  |  +- mossy
|  |  |  +- remains
|  |  |  |  +- badger
|  |  |  |  +- bear
|  |  |  |  +- bigrat
|  |  |  |  +- bobcat
|  |  |  |  +- cabbit
|  |  |  |  +- cow
|  |  |  |  +- crow
|  |  |  |  +- fogbeast
|  |  |  |  +- fox
|  |  |  |  +- human
|  |  |  |  +- mole
|  |  |  |  +- pig
|  |  |  |  +- plasma
|  |  |  |  +- raccoon
|  |  |  |  +- saiga
|  |  |  |  +- troll
|  |  |  |  +- wolf
|  |  |  |  `- xeno
|  |  |  |     `- larva
|  |  |  +- shadow_floor
|  |  |  |  `- corner
|  |  |  `- wood
|  |  |     +- herringbone
|  |  |     `- herringbone2
|  |  +- DPfall
|  |  +- DPtarget
|  |  +- dream_horror
|  |  +- dummy
|  |  |  +- lighting_obj
|  |  |  |  `- moblight
|  |  |  |     `- fire
|  |  |  +- parlor_trick
|  |  |  `- phased_mob
|  |  |     +- slaughter
|  |  |     `- spell_jaunt
|  |  +- dungeon_directional_helper
|  |  |  +- east
|  |  |  |  `- top
|  |  |  +- north
|  |  |  |  `- top
|  |  |  +- south
|  |  |  |  `- top
|  |  |  `- west
|  |  |     `- top
|  |  +- ebeam
|  |  +- explosion
|  |  +- falling_sakura
|  |  +- fog_parter
|  |  +- forcefield
|  |  |  +- cult
|  |  |  +- mime
|  |  |  |  `- advanced
|  |  |  `- wizard
|  |  +- frozen_mist
|  |  +- fullbright
|  |  +- fun_balloon
|  |  |  +- scatter
|  |  |  `- sentience
|  |  +- gate_phalanx_spear
|  |  +- gibspawner
|  |  |  +- generic
|  |  |  |  `- animal
|  |  |  `- human
|  |  |     `- bodypartless
|  |  +- gravity_anchor_zone
|  |  +- hag_teleport_marker
|  |  +- hallucination
|  |  |  +- danger
|  |  |  |  +- anomaly
|  |  |  |  +- chasm
|  |  |  |  `- lava
|  |  |  `- simple
|  |  |     +- bluespace_stream
|  |  |     `- securitron
|  |  +- hotspot
|  |  |  `- vampiric
|  |  +- iron_tempest
|  |  +- landmark
|  |  |  +- awaystart
|  |  |  +- blobstart
|  |  |  +- carpspawn
|  |  |  +- chest_or_mimic
|  |  |  |  +- gold
|  |  |  |  +- locked_or_trapped
|  |  |  |  `- loot_chest
|  |  |  |     `- locked
|  |  |  +- chimeric_calyx_spawner
|  |  |  |  +- fifteen
|  |  |  |  `- thirty
|  |  |  +- deaths_door
|  |  |  |  +- entry
|  |  |  |  |  +- bl
|  |  |  |  |  +- br
|  |  |  |  |  +- tl
|  |  |  |  |  `- tr
|  |  |  |  `- exit
|  |  |  +- ert_spawn
|  |  |  +- event_spawn
|  |  |  +- events
|  |  |  |  +- animal_migration_point
|  |  |  |  +- deadite_animal_migration_point
|  |  |  |  +- haunts
|  |  |  |  `- testportal
|  |  |  +- hellexit
|  |  |  +- hellspawn
|  |  |  +- holding_facility
|  |  |  +- latejoin
|  |  |  +- lift_id
|  |  |  +- map_load_mark
|  |  |  +- mapGenerator
|  |  |  |  `- rogue
|  |  |  |     +- beach
|  |  |  |     +- bog
|  |  |  |     +- cave
|  |  |  |     |  +- lava
|  |  |  |     |  `- spider
|  |  |  |     +- decap
|  |  |  |     +- forest
|  |  |  |     +- mountain
|  |  |  |     +- roguetownfield
|  |  |  |     `- underdark
|  |  |  +- observer_start
|  |  |  +- prisonwarp
|  |  |  +- quest_spawner
|  |  |  |  +- easy
|  |  |  |  +- hard
|  |  |  |  `- medium
|  |  |  +- ruin
|  |  |  +- secequipment
|  |  |  +- start
|  |  |  |  +- absolver
|  |  |  |  +- adventurer
|  |  |  |  +- adventurerlate
|  |  |  |  +- apothecary
|  |  |  |  +- archivist
|  |  |  |  +- bandit
|  |  |  |  +- bathmaster
|  |  |  |  +- bathworker
|  |  |  |  +- bishop
|  |  |  |  +- cleric
|  |  |  |  +- clerk
|  |  |  |  +- cook
|  |  |  |  +- councillor
|  |  |  |  +- courtagent
|  |  |  |  +- crier
|  |  |  |  +- delf
|  |  |  |  +- druid
|  |  |  |  +- farmer
|  |  |  |  +- fisher
|  |  |  |  +- gnoll
|  |  |  |  +- gnolllate
|  |  |  |  +- gravedigger
|  |  |  |  +- guardsman
|  |  |  |  +- guildmaster
|  |  |  |  +- guildsman
|  |  |  |  +- hag
|  |  |  |  +- haglate
|  |  |  |  +- hand
|  |  |  |  +- hostage
|  |  |  |  +- innkeep
|  |  |  |  +- innkeeper
|  |  |  |  +- innkeeperer
|  |  |  |  +- inquisitor
|  |  |  |  +- jester
|  |  |  |  +- keeper
|  |  |  |  +- knight
|  |  |  |  +- lady
|  |  |  |  +- lord
|  |  |  |  +- lunatic
|  |  |  |  +- magician
|  |  |  |  +- marshal
|  |  |  |  +- martyr
|  |  |  |  +- mercenary
|  |  |  |  +- mercenarylate
|  |  |  |  +- merchant
|  |  |  |  +- monk
|  |  |  |  +- new_player
|  |  |  |  +- nukeop
|  |  |  |  +- nukeop_leader
|  |  |  |  +- orthodoxist
|  |  |  |  +- physician
|  |  |  |  +- prince
|  |  |  |  +- prisonerr
|  |  |  |  +- seneschal
|  |  |  |  +- sergeant
|  |  |  |  +- servant
|  |  |  |  +- sexton
|  |  |  |  +- shophand
|  |  |  |  +- sieges
|  |  |  |  +- squire
|  |  |  |  +- steward
|  |  |  |  +- suitor
|  |  |  |  +- tailor
|  |  |  |  +- tapster
|  |  |  |  +- templar
|  |  |  |  +- trader
|  |  |  |  +- vagabond
|  |  |  |  +- vagrant
|  |  |  |  +- vampireknight
|  |  |  |  +- vampirelord
|  |  |  |  +- vampirespawn
|  |  |  |  +- veteran
|  |  |  |  +- villager
|  |  |  |  +- wapprentice
|  |  |  |  +- warden
|  |  |  |  +- wizard
|  |  |  |  +- wretch
|  |  |  |  `- wretchlate
|  |  |  +- thunderdome
|  |  |  |  +- admin
|  |  |  |  +- observe
|  |  |  |  +- one
|  |  |  |  `- two
|  |  |  +- tram
|  |  |  |  `- queued_path
|  |  |  |     +- cargo_exit
|  |  |  |     +- cargo_map_enter
|  |  |  |     +- cargo_map_exit
|  |  |  |     +- cargo_pre_enter
|  |  |  |     +- cargo_stop
|  |  |  |     +- cargo_storage_point
|  |  |  |     +- debug_1
|  |  |  |     `- debug_2
|  |  |  +- travel_spawn_point
|  |  |  +- travel_tile_location
|  |  |  +- treyliam
|  |  |  +- underworld
|  |  |  +- underworldcoin
|  |  |  +- underworldsafe
|  |  |  +- underworldstrands
|  |  |  +- unit_test_bottom_left
|  |  |  +- unit_test_top_right
|  |  |  +- vteleport
|  |  |  +- vteleportdestination
|  |  |  +- vteleportsenddest
|  |  |  `- vteleportsending
|  |  +- lily_petal
|  |  |  +- three
|  |  |  `- two
|  |  +- list_container
|  |  |  `- mobl
|  |  +- mapping_helpers
|  |  |  +- access
|  |  |  |  `- locker
|  |  |  +- component_injector
|  |  |  +- dead_body_placer
|  |  |  +- floor_clothing_equipper
|  |  |  +- no_lava
|  |  |  +- outfit_handler
|  |  |  `- secret_door_creator
|  |  +- melee_swing
|  |  +- mine
|  |  |  +- explosive
|  |  |  +- gas
|  |  |  |  +- n2o
|  |  |  |  `- plasma
|  |  |  +- kickmine
|  |  |  +- pickup
|  |  |  |  +- healing
|  |  |  |  `- speed
|  |  |  +- sound
|  |  |  |  `- bwoink
|  |  |  `- stun
|  |  +- mob_spawn
|  |  |  `- human
|  |  |     +- corpse
|  |  |     |  +- damaged
|  |  |     |  `- delayed
|  |  |     `- orc
|  |  |        `- corpse
|  |  |           +- orcmarauder
|  |  |           +- orcravager
|  |  |           +- savageorc
|  |  |           `- savageorc2
|  |  +- obeliskbeam
|  |  +- oneway
|  |  |  +- baroness
|  |  |  +- lich
|  |  |  +- psy_bog
|  |  |  `- psy_bog_two
|  |  +- overlay
|  |  |  +- beam
|  |  |  +- coconut
|  |  |  +- light_visible
|  |  |  +- palmtree_l
|  |  |  +- palmtree_r
|  |  |  +- sparkles
|  |  |  +- thermite
|  |  |  +- typing_indicator
|  |  |  +- vis
|  |  |  +- water
|  |  |  |  +- area_cover
|  |  |  |  `- top
|  |  |  `- zone_sel
|  |  +- overlayTest
|  |  +- particle_effect
|  |  |  +- expl_particles
|  |  |  +- foam
|  |  |  |  +- long_life
|  |  |  |  `- metal
|  |  |  |     +- iron
|  |  |  |     +- resin
|  |  |  |     `- smart
|  |  |  +- ion_trails
|  |  |  |  `- flight
|  |  |  +- smoke
|  |  |  |  +- bad
|  |  |  |  +- blind_gas
|  |  |  |  +- chem
|  |  |  |  +- fast
|  |  |  |  +- fire_gas
|  |  |  |  +- healing_gas
|  |  |  |  +- mute_gas
|  |  |  |  +- poison_gas
|  |  |  |  +- sleeping
|  |  |  |  `- transparent
|  |  |  +- sparks
|  |  |  |  +- electricity
|  |  |  |  `- quantum
|  |  |  +- steam
|  |  |  `- water
|  |  +- portal
|  |  |  +- anom
|  |  |  `- permanent
|  |  |     `- one_way
|  |  |        +- destroy
|  |  |        `- keep
|  |  +- proc_holder
|  |  |  `- spell
|  |  |     +- aimed
|  |  |     |  `- fireball
|  |  |     +- aoe_turf
|  |  |     |  +- conjure
|  |  |     |  |  +- mime_chair
|  |  |     |  |  +- mime_wall
|  |  |     |  |  +- presents
|  |  |     |  |  `- the_traps
|  |  |     |  `- knock
|  |  |     +- bloodcrawl
|  |  |     +- invoked
|  |  |     |  +- abduct
|  |  |     |  +- abscond
|  |  |     |  +- abyssal_infusion
|  |  |     |  +- abyssal_strength
|  |  |     |  +- abyssheal
|  |  |     |  +- abyssor_bends
|  |  |     |  +- abyssor_undertow
|  |  |     |  +- appraise
|  |  |     |  |  `- secular
|  |  |     |  +- aquatic_compulsion
|  |  |     |  +- astrataspark
|  |  |     |  +- attach_bodypart
|  |  |     |  +- avert
|  |  |     |  +- baothablessings
|  |  |     |  +- baothavice
|  |  |     |  +- barter
|  |  |     |  +- bless_cross
|  |  |     |  +- bless_food
|  |  |     |  +- blindness
|  |  |     |  +- blood_heal
|  |  |     |  +- bonechill
|  |  |     |  +- bonemend
|  |  |     |  +- bud
|  |  |     |  +- call_dreamfiend
|  |  |     |  +- call_mossback
|  |  |     |  +- chain_lightning_breath
|  |  |     |  +- challenge
|  |  |     |  +- chokeslam
|  |  |     |  +- conjure_primordial
|  |  |     |  +- convert_heretic
|  |  |     |  +- convert_heretic_priest
|  |  |     |  +- convert_psydon
|  |  |     |  +- craftercovenant
|  |  |     |  +- create_shrooms
|  |  |     |  +- cure_rot
|  |  |     |  |  `- priest
|  |  |     |  +- deaths_door
|  |  |     |  +- diagnose
|  |  |     |  |  `- secular
|  |  |     |  +- digclay
|  |  |     |  +- diminish
|  |  |     |  +- divine_rebirth
|  |  |     |  +- dragon_lightning
|  |  |     |  +- dragon_swoop
|  |  |     |  +- dream_bind
|  |  |     |  +- dream_trance
|  |  |     |  +- dropkick
|  |  |     |  +- ele_quake
|  |  |     |  +- engineeranalyze
|  |  |     |  +- engineertuneup
|  |  |     |  +- engineerwindup
|  |  |     |  +- eora_blessing
|  |  |     |  +- eoracurse
|  |  |     |  +- extract_heart
|  |  |     |  +- eyebite
|  |  |     |  +- fiend_meteor
|  |  |     |  +- fire_obelisk_beam
|  |  |     |  +- fittedclothing
|  |  |     |  +- fog_ward
|  |  |     |  +- frostbite
|  |  |     |  +- gallowshumor
|  |  |     |  +- gnoll_sniff
|  |  |     |  +- grant_boon
|  |  |     |  +- gravemark
|  |  |     |  |  `- no_sprite
|  |  |     |  +- griefflower
|  |  |     |  +- hammerfall
|  |  |     |  +- headbutt
|  |  |     |  +- heal
|  |  |     |  |  +- astrata
|  |  |     |  |  `- undivided
|  |  |     |  +- heartweave
|  |  |     |  +- heatmetal
|  |  |     |  +- huntersyell
|  |  |     |  +- ignition
|  |  |     |  |  `- undivided
|  |  |     |  +- immolation
|  |  |     |  +- infestation
|  |  |     |  +- invisibility
|  |  |     |  |  +- gnoll
|  |  |     |  |  `- miracle
|  |  |     |  +- jaunt
|  |  |     |  +- joyride
|  |  |     |  +- knock
|  |  |     |  +- lasthigh
|  |  |     |  +- learn
|  |  |     |  +- lesser_heal
|  |  |     |  +- mark_target
|  |  |     |  +- massage
|  |  |     |  +- mastersillusion
|  |  |     |  +- matthios_churn
|  |  |     |  +- matthios_equalize
|  |  |     |  +- matthios_firebreath
|  |  |     |  +- matthios_transact
|  |  |     |  +- mimicry
|  |  |     |  +- mindlink
|  |  |     |  |  `- hag
|  |  |     |  +- mineroresight
|  |  |     |  +- minion_order
|  |  |     |  |  +- lich
|  |  |     |  |  `- primordial
|  |  |     |  +- moondream
|  |  |     |  +- necra_vow
|  |  |     |  +- necras_sight
|  |  |     |  +- noc_sight
|  |  |     |  +- old_blindness
|  |  |     |  +- order
|  |  |     |  |  +- heartfelt
|  |  |     |  |  |  +- bolster
|  |  |     |  |  |  +- charge
|  |  |     |  |  |  +- forheartfelt
|  |  |     |  |  |  `- retreat
|  |  |     |  |  +- hold
|  |  |     |  |  +- movemovemove
|  |  |     |  |  +- onfeet
|  |  |     |  |  `- takeaim
|  |  |     |  +- painkiller
|  |  |     |  +- perseverance
|  |  |     |  +- persistence
|  |  |     |  +- pestilent_blade
|  |  |     |  +- pestra_heal
|  |  |     |  +- pestra_leech
|  |  |     |  +- pomegranate
|  |  |     |  +- primordialmark
|  |  |     |  +- projectile
|  |  |     |  |  +- acidsplash
|  |  |     |  |  |  `- quietus
|  |  |     |  |  +- airblade
|  |  |     |  |  +- arcynestrike
|  |  |     |  |  +- baali_fireball
|  |  |     |  |  +- bloodsteal
|  |  |     |  |  +- blowingdust
|  |  |     |  |  +- divineblast
|  |  |     |  |  +- graggar_blood_net
|  |  |     |  |  +- profane
|  |  |     |  |  |  `- miracle
|  |  |     |  |  +- sacred_flame
|  |  |     |  |  +- sickness
|  |  |     |  |  `- unholyblast
|  |  |     |  +- psydonabsolve
|  |  |     |  +- psydonendure
|  |  |     |  +- psydonlux_tamper
|  |  |     |  +- pyroclastic_puff
|  |  |     |  +- raise_spirits_vengeance
|  |  |     |  +- raise_undead
|  |  |     |  +- raise_undead_formation
|  |  |     |  |  +- miracle
|  |  |     |  |  `- necromancer
|  |  |     |  +- raise_undead_guard
|  |  |     |  |  `- miracle
|  |  |     |  +- raise_warrior_spirits
|  |  |     |  +- recuperation
|  |  |     |  +- refocusstudies
|  |  |     |  +- remotebomb
|  |  |     |  +- repulse
|  |  |     |  +- restoration
|  |  |     |  +- resurrect
|  |  |     |  |  +- abyssor
|  |  |     |  |  +- baotha
|  |  |     |  |  +- dendor
|  |  |     |  |  +- eora
|  |  |     |  |  +- graggar
|  |  |     |  |  +- hag
|  |  |     |  |  +- malum
|  |  |     |  |  +- matthios
|  |  |     |  |  +- noc
|  |  |     |  |  +- pestra
|  |  |     |  |  +- ravox
|  |  |     |  |  +- undivided
|  |  |     |  |  +- xylix
|  |  |     |  |  `- zizo
|  |  |     |  +- revel_in_slaughter
|  |  |     |  +- revive
|  |  |     |  +- rituos
|  |  |     |  |  `- miracle
|  |  |     |  +- root_affinity
|  |  |     |  +- saxtonhale
|  |  |     |  +- shepherd
|  |  |     |  +- silence
|  |  |     |  |  +- archivist_silence
|  |  |     |  |  +- graggar
|  |  |     |  |  `- miracle
|  |  |     |  +- slumber_exile
|  |  |     |  +- spiderspeak
|  |  |     |  +- spiritual_siphon
|  |  |     |  +- stunner
|  |  |     |  +- summon_dreamfiend_curse
|  |  |     |  +- summon_marked
|  |  |     |  +- summon_rift
|  |  |     |  +- sundering_lightning
|  |  |     |  +- sunstrike
|  |  |     |  +- takeapprentice
|  |  |     |  +- tame_undead
|  |  |     |  |  `- miracle
|  |  |     |  +- teach
|  |  |     |  +- thunderstrike
|  |  |     |  +- tipscales
|  |  |     |  +- track_mark
|  |  |     |  +- transform_tree
|  |  |     |  +- transmutation_rite
|  |  |     |  +- tug_of_war
|  |  |     |  +- twist_food
|  |  |     |  +- vampire_float
|  |  |     |  +- veilbound_shift
|  |  |     |  +- vendetta
|  |  |     |  +- ventriloquism
|  |  |     |  +- vigorousexchange
|  |  |     |  +- vizier_restoration
|  |  |     |  +- wound_closure
|  |  |     |  `- wound_heal
|  |  |     +- self
|  |  |     |  +- abyssor_wind
|  |  |     |  +- astrata_fireresist
|  |  |     |  +- astrata_gaze
|  |  |     |  +- astrata_sword
|  |  |     |  +- axedance
|  |  |     |  +- balance_immune
|  |  |     |  +- basic_heal
|  |  |     |  +- bearclaws
|  |  |     |  +- bless_drink
|  |  |     |  +- blindnessorsilence
|  |  |     |  +- boulder_scrounge
|  |  |     |  +- cabbitclaws
|  |  |     |  +- call_infernals
|  |  |     |  +- call_to_arms
|  |  |     |  +- catclaws
|  |  |     |  +- check_boot
|  |  |     |  +- choose_riding_virtue_mount
|  |  |     |  +- choose_schism_side
|  |  |     |  +- claws
|  |  |     |  |  `- gnoll
|  |  |     |  +- colossus_stomp
|  |  |     |  +- convertrole
|  |  |     |  |  +- agent
|  |  |     |  |  +- bog
|  |  |     |  |  +- brother
|  |  |     |  |  +- brotherhood
|  |  |     |  |  +- guard
|  |  |     |  |  +- heartfelt
|  |  |     |  |  +- monk
|  |  |     |  |  +- retainer
|  |  |     |  |  +- servant
|  |  |     |  |  +- templar
|  |  |     |  |  `- zizosquire
|  |  |     |  +- create_abyssoid
|  |  |     |  +- create_vines
|  |  |     |  +- createhoney
|  |  |     |  +- divine_strike
|  |  |     |  |  `- undivided
|  |  |     |  +- dragon_slam
|  |  |     |  +- foxclaws
|  |  |     |  +- graggar_bloodrage
|  |  |     |  +- graggar_call_to_slaughter
|  |  |     |  +- graggar_chainbreak
|  |  |     |  +- grant_nobility
|  |  |     |  +- grant_title
|  |  |     |  +- hagclaws
|  |  |     |  +- heir_spell_bundle
|  |  |     |  +- howl
|  |  |     |  |  +- call_of_the_moon
|  |  |     |  |  `- gnoll
|  |  |     |  +- inscription_cache
|  |  |     |  +- insufflation
|  |  |     |  +- lich_announce
|  |  |     |  +- lirvan_tithe
|  |  |     |  +- locate_dead
|  |  |     |  +- lurking_step
|  |  |     |  +- matthios_muffle
|  |  |     |  +- moleclaw
|  |  |     |  +- moon_light
|  |  |     |  +- noc_spell_bundle
|  |  |     |  +- phantasm_fade
|  |  |     |  +- phantom_flicker
|  |  |     |  +- provocation
|  |  |     |  +- psydonpersist
|  |  |     |  +- psydonprayer
|  |  |     |  +- psydonrespite
|  |  |     |  +- rage
|  |  |     |  +- ragebad
|  |  |     |  +- rebelconvert
|  |  |     |  +- recall_cache
|  |  |     |  +- repair
|  |  |     |  +- saddleborn
|  |  |     |  |  +- sendaway
|  |  |     |  |  `- whistle
|  |  |     |  +- saigahoofs
|  |  |     |  +- scent_of_the_grave
|  |  |     |  +- smolder_shroud
|  |  |     |  +- soothing_bloom
|  |  |     |  +- spiderfangs
|  |  |     |  |  `- mire
|  |  |     |  +- starseers_cry
|  |  |     |  +- stillness_of_stone
|  |  |     |  +- suicidebomb
|  |  |     |  |  `- lesser
|  |  |     |  +- summon_obelisks
|  |  |     |  +- telljoke
|  |  |     |  +- telltragedy
|  |  |     |  +- ten_united
|  |  |     |  +- twinned_gaze
|  |  |     |  +- undivided_miracle_bundle
|  |  |     |  +- verdant_sprout
|  |  |     |  +- verdant_veil
|  |  |     |  +- weaveweb
|  |  |     |  +- wildshape
|  |  |     |  |  `- hag_true_form
|  |  |     |  +- wise_moon
|  |  |     |  +- wolfclaws
|  |  |     |  +- xylixslip
|  |  |     |  +- zeybek_momentum
|  |  |     |  |  +- almah
|  |  |     |  |  +- janissary
|  |  |     |  |  `- zeybek
|  |  |     |  `- zizo_snuff
|  |  |     `- targeted
|  |  |        +- abrogation
|  |  |        +- area_teleport
|  |  |        +- beasttame
|  |  |        +- blesscrop
|  |  |        +- churn
|  |  |        +- conjure_glowshroom
|  |  |        +- conjure_item
|  |  |        +- conjure_vines
|  |  |        +- emplosion
|  |  |        +- ethereal_jaunt
|  |  |        +- forcewall
|  |  |        |  `- mime
|  |  |        +- inflict_handler
|  |  |        +- mime
|  |  |        |  `- speak
|  |  |        +- personality_commune
|  |  |        +- projectile
|  |  |        |  `- dumbfire
|  |  |        +- ravox_challenge
|  |  |        +- shapeshift
|  |  |        |  +- cabbit
|  |  |        |  +- dendormole
|  |  |        |  +- gaseousform
|  |  |        |  +- mireboi
|  |  |        |  +- rat
|  |  |        |  +- vampire
|  |  |        |  |  `- bat
|  |  |        |  `- witch
|  |  |        |     +- bat
|  |  |        |     +- cabbit
|  |  |        |     +- cat
|  |  |        |     |  `- black
|  |  |        |     +- crow
|  |  |        |     +- lesser_vernard
|  |  |        |     +- lesser_wolf
|  |  |        |     `- rous
|  |  |        +- soulspeak
|  |  |        +- spiderconjur
|  |  |        +- summonitem
|  |  |        +- summonweapon
|  |  |        +- tesla
|  |  |        +- touch
|  |  |        |  +- loversruin
|  |  |        |  +- orison
|  |  |        |  +- parlor_trick
|  |  |        |  `- summonrogueweapon
|  |  |        |     +- astratagrasp
|  |  |        |     +- nocgrasp
|  |  |        |     `- ravoxgrasp
|  |  |        +- transfix_neu
|  |  |        +- trigger
|  |  |        +- turf_teleport
|  |  |        |  `- blink
|  |  |        `- woundlick
|  |  +- projectile
|  |  |  +- impact
|  |  |  |  +- disabler
|  |  |  |  +- heavy_laser
|  |  |  |  +- laser
|  |  |  |  |  `- blue
|  |  |  |  +- plasma_cutter
|  |  |  |  +- pointline
|  |  |  |  +- pulse
|  |  |  |  +- stun
|  |  |  |  +- wormhole
|  |  |  |  `- xray
|  |  |  +- muzzle
|  |  |  |  +- disabler
|  |  |  |  +- heavy_laser
|  |  |  |  +- laser
|  |  |  |  |  `- blue
|  |  |  |  +- plasma_cutter
|  |  |  |  +- pointline
|  |  |  |  +- pulse
|  |  |  |  +- stun
|  |  |  |  +- wormhole
|  |  |  |  `- xray
|  |  |  `- tracer
|  |  |     +- blood
|  |  |     +- bloodsteal
|  |  |     +- disabler
|  |  |     +- heavy_laser
|  |  |     +- laser
|  |  |     |  `- blue
|  |  |     +- plasma_cutter
|  |  |     +- pointline
|  |  |     +- pulse
|  |  |     +- solar_beam
|  |  |     +- stun
|  |  |     +- tracer
|  |  |     |  +- aiming
|  |  |     |  `- beam_rifle
|  |  |     +- wormhole
|  |  |     `- xray
|  |  +- projectile_lighting
|  |  +- quest_spawn
|  |  +- reversion_marker
|  |  +- solid_invisible_barrier
|  |  +- sound_emitter
|  |  +- spawner
|  |  |  +- lootdrop
|  |  |  |  +- ancient_equipment_spawner
|  |  |  |  +- armored_boots_spawner
|  |  |  |  +- armored_gloves_spawner
|  |  |  |  +- armored_wrists_spawner
|  |  |  |  +- blacksteel_equipment_spawner
|  |  |  |  +- cheap_candle_spawner
|  |  |  |  +- cheap_clutter_spawner
|  |  |  |  +- cheap_jewelry_spawner
|  |  |  |  +- cheap_tableware_spawner
|  |  |  |  +- decrepit_equipment_spawner
|  |  |  |  +- elven_equipment_spawner
|  |  |  |  +- general_loot_hi
|  |  |  |  |  `- x3
|  |  |  |  +- general_loot_low
|  |  |  |  |  `- x3
|  |  |  |  +- general_loot_mid
|  |  |  |  |  `- x3
|  |  |  |  +- hag
|  |  |  |  |  +- enchanted_moss
|  |  |  |  |  +- mothers_cache
|  |  |  |  |  +- raw_botanicals
|  |  |  |  |  `- wyrd_artifacts
|  |  |  |  +- heavy_armor_spawner
|  |  |  |  +- helmet_spawner
|  |  |  |  +- horny_armor_spawner
|  |  |  |  +- iron_copper_weapon_spawner
|  |  |  |  +- light_armor_spawner
|  |  |  |  +- medium_armor_spawner
|  |  |  |  +- peasant_weapon_spawner
|  |  |  |  +- potion_ingredient
|  |  |  |  |  `- herb
|  |  |  |  +- potion_poisons
|  |  |  |  +- potion_stats
|  |  |  |  +- potion_vitals
|  |  |  |  +- roguetown
|  |  |  |  |  +- abyssor
|  |  |  |  |  +- dungeon
|  |  |  |  |  |  +- armor
|  |  |  |  |  |  +- clothing
|  |  |  |  |  |  +- food
|  |  |  |  |  |  +- materials
|  |  |  |  |  |  +- medical
|  |  |  |  |  |  +- misc
|  |  |  |  |  |  +- money
|  |  |  |  |  |  +- spells
|  |  |  |  |  |  +- tools
|  |  |  |  |  |  `- weapons
|  |  |  |  |  `- sewers
|  |  |  |  +- silver_weapon_spawner
|  |  |  |  +- steel_weapon_spawner
|  |  |  |  +- valuable_candle_spawner
|  |  |  |  +- valuable_clutter_spawner
|  |  |  |  +- valuable_jewelry_spawner
|  |  |  |  `- valuable_tableware_spawner
|  |  |  +- roguemap
|  |  |  |  +- beartrap
|  |  |  |  +- hauntpile
|  |  |  |  +- pit
|  |  |  |  +- shroud
|  |  |  |  +- stump
|  |  |  |  +- tree
|  |  |  |  +- treeorbush
|  |  |  |  `- treeorstump
|  |  |  +- structure
|  |  |  `- trap
|  |  +- spell_rune
|  |  +- spell_rune_under
|  |  +- spresent
|  |  +- statclick
|  |  |  +- ahelp
|  |  |  +- debug
|  |  |  +- SDQL2_VV_all
|  |  |  `- ticket_list
|  |  +- step_trigger
|  |  |  +- message
|  |  |  +- sound_effect
|  |  |  +- stopper
|  |  |  +- teleport_fancy
|  |  |  +- teleporter
|  |  |  |  `- random
|  |  |  `- thrower
|  |  +- supplypod_selector
|  |  +- temp_visual
|  |  |  +- acidsplash
|  |  |  +- air_strike_telegraph
|  |  |  +- arcyne_strike_fx
|  |  |  +- armor_chunk
|  |  |  +- armor_glint
|  |  |  +- baroness_dying
|  |  |  +- barter_fx
|  |  |  +- bedrockore
|  |  |  +- blade_burst
|  |  |  +- blade_cut
|  |  |  +- blade_stab
|  |  |  +- blade_storm_telegraph
|  |  |  +- bleed
|  |  |  |  `- explode
|  |  |  +- blink
|  |  |  |  `- shadowstep
|  |  |  +- blob
|  |  |  +- bluespace_fissure
|  |  |  +- borgflash
|  |  |  +- bsa_splash
|  |  |  +- cataclysm_boulder
|  |  |  +- censer_dust
|  |  |  +- cleaning_pulse
|  |  |  +- cult
|  |  |  |  +- turf
|  |  |  |  |  `- floor
|  |  |  |  +- blood
|  |  |  |  |  `- out
|  |  |  |  +- door
|  |  |  |  |  `- unruned
|  |  |  |  +- portal
|  |  |  |  +- rune_spawn
|  |  |  |  |  +- rune1
|  |  |  |  |  |  +- center
|  |  |  |  |  |  `- inner
|  |  |  |  |  +- rune2
|  |  |  |  |  |  +- center
|  |  |  |  |  |  `- inner
|  |  |  |  |  +- rune3
|  |  |  |  |  |  +- center
|  |  |  |  |  |  `- inner
|  |  |  |  |  +- rune4
|  |  |  |  |  |  +- center
|  |  |  |  |  |  `- inner
|  |  |  |  |  +- rune5
|  |  |  |  |  |  +- center
|  |  |  |  |  |  `- inner
|  |  |  |  |  +- rune6
|  |  |  |  |  |  +- center
|  |  |  |  |  |  `- inner
|  |  |  |  |  `- rune7
|  |  |  |  |     +- center
|  |  |  |  |     `- inner
|  |  |  |  +- sac
|  |  |  |  `- sparks
|  |  |  +- curse
|  |  |  +- decoy
|  |  |  |  `- fading
|  |  |  |     +- fivesecond
|  |  |  |     +- halfsecond
|  |  |  |     `- threesecond
|  |  |  +- desynchronizer
|  |  |  +- diminish
|  |  |  +- dir_setting
|  |  |  |  +- attack_effect
|  |  |  |  +- bloodsplatter
|  |  |  |  |  `- xenosplatter
|  |  |  |  +- cleave_visual
|  |  |  |  +- cult
|  |  |  |  |  `- phase
|  |  |  |  |     `- out
|  |  |  |  +- curse
|  |  |  |  |  +- blob
|  |  |  |  |  +- grasp_portal
|  |  |  |  |  |  `- fading
|  |  |  |  |  `- hand
|  |  |  |  +- firing_effect
|  |  |  |  |  +- energy
|  |  |  |  |  `- magic
|  |  |  |  +- ninja
|  |  |  |  |  +- cloak
|  |  |  |  |  +- phase
|  |  |  |  |  |  `- out
|  |  |  |  |  `- shadow
|  |  |  |  +- speedbike_trail
|  |  |  |  +- tailsweep
|  |  |  |  `- wraith
|  |  |  |     `- out
|  |  |  +- dragon_flight
|  |  |  |  `- end
|  |  |  +- dragon_swoop
|  |  |  +- drakewall
|  |  |  +- dust_animation
|  |  |  +- dust_animation_filter
|  |  |  +- emp
|  |  |  |  `- pulse
|  |  |  +- ensnare
|  |  |  |  `- long
|  |  |  +- explosion
|  |  |  +- falling_boulder
|  |  |  +- fire
|  |  |  |  `- shortduration
|  |  |  +- fireball
|  |  |  +- firebreath_actual
|  |  |  +- firewave
|  |  |  |  +- spark
|  |  |  |  +- sun_mark
|  |  |  |  |  `- pre_sunstrike
|  |  |  |  +- sunbeam
|  |  |  |  `- sunstrike
|  |  |  |     `- primary
|  |  |  +- flies
|  |  |  +- frozen_mist_tile
|  |  |  +- gate_phalanx_thrust
|  |  |  +- gemqualityore
|  |  |  +- gib_animation
|  |  |  |  `- animal
|  |  |  +- grasp_telegraph
|  |  |  |  `- long
|  |  |  +- gravity
|  |  |  +- gravity_anchor_ground
|  |  |  +- gravity_trap
|  |  |  +- gravpush
|  |  |  +- guardian
|  |  |  |  `- phase
|  |  |  |     `- out
|  |  |  +- gust
|  |  |  +- heal
|  |  |  +- heal_blood
|  |  |  +- heal_rogue
|  |  |  |  +- bubble
|  |  |  |  +- campfire
|  |  |  |  `- hag
|  |  |  +- heart
|  |  |  |  `- sex_effects
|  |  |  |     `- red_heart
|  |  |  +- highqualityore
|  |  |  +- impact_effect
|  |  |  |  +- blue_laser
|  |  |  |  +- green_laser
|  |  |  |  +- ion
|  |  |  |  +- purple_laser
|  |  |  |  +- red_laser
|  |  |  |  |  `- wall
|  |  |  |  `- shrink
|  |  |  +- kinetic_blast
|  |  |  +- lava_warning
|  |  |  +- lavastaff
|  |  |  +- lich_dying
|  |  |  +- lightning
|  |  |  +- lirvan_sunset_dragon
|  |  |  +- love_heart
|  |  |  |  `- invisible
|  |  |  +- lycan
|  |  |  +- marker
|  |  |  +- medqualityore
|  |  |  +- monkeyify
|  |  |  |  `- humanify
|  |  |  +- moon
|  |  |  +- mummy_animation
|  |  |  +- music_rogue
|  |  |  +- necra_consecrate
|  |  |  +- offered_item_effect
|  |  |  +- particle_up
|  |  |  +- paw_swipe
|  |  |  +- point
|  |  |  |  `- still
|  |  |  +- psyheal_rogue
|  |  |  +- revenant
|  |  |  |  `- cracks
|  |  |  +- small_smoke
|  |  |  |  `- halfsecond
|  |  |  +- snap_freeze
|  |  |  +- song_telltale
|  |  |  |  +- buff
|  |  |  |  `- debuff
|  |  |  +- songs
|  |  |  |  +- inspiration_bardsongt1
|  |  |  |  +- inspiration_bardsongt2
|  |  |  |  +- inspiration_bardsongt3
|  |  |  |  +- inspiration_dirget1
|  |  |  |  +- inspiration_dirget2
|  |  |  |  +- inspiration_dirget3
|  |  |  |  +- inspiration_melodyt1
|  |  |  |  +- inspiration_melodyt2
|  |  |  |  `- inspiration_melodyt3
|  |  |  +- soundping
|  |  |  +- special_intent
|  |  |  +- spell_impact
|  |  |  +- spinning_dagger
|  |  |  +- spore
|  |  |  +- stomp
|  |  |  +- stone_throw
|  |  |  +- stress_event
|  |  |  |  `- invisible
|  |  |  +- surrender
|  |  |  +- swingdelay
|  |  |  +- target
|  |  |  +- targetlightning
|  |  |  +- telekinesis
|  |  |  +- thunderstrike_actual
|  |  |  +- trap
|  |  |  |  +- emergence
|  |  |  |  +- ferramancy
|  |  |  |  +- firebreath
|  |  |  |  +- hex
|  |  |  |  +- kinesis
|  |  |  |  +- meteor
|  |  |  |  `- thunderstrike
|  |  |  |     +- layer_one
|  |  |  |     `- layer_two
|  |  |  +- trap_wall
|  |  |  |  +- battle_ward
|  |  |  |  +- earth
|  |  |  |  `- fire
|  |  |  +- trapice
|  |  |  +- truffle_overlay
|  |  |  +- vamp_summon
|  |  |  |  `- end
|  |  |  +- vamp_teleport
|  |  |  +- warp_cube
|  |  |  +- wave_up
|  |  |  +- wither_ground
|  |  |  `- wizard
|  |  |     `- out
|  |  +- track
|  |  |  +- structure
|  |  |  `- thievescant
|  |  +- tracker
|  |  |  +- drain
|  |  |  `- soul
|  |  +- turf_decal
|  |  |  +- arrows
|  |  |  |  +- red
|  |  |  |  `- white
|  |  |  +- bot
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  +- bot_red
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  +- bot_white
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  +- box
|  |  |  |  +- corners
|  |  |  |  +- red
|  |  |  |  |  `- corners
|  |  |  |  `- white
|  |  |  |     `- corners
|  |  |  +- caution
|  |  |  |  +- red
|  |  |  |  +- stand_clear
|  |  |  |  |  +- red
|  |  |  |  |  `- white
|  |  |  |  `- white
|  |  |  +- delivery
|  |  |  |  +- red
|  |  |  |  `- white
|  |  |  +- loading_area
|  |  |  |  +- red
|  |  |  |  `- white
|  |  |  +- magedecal
|  |  |  +- plaque
|  |  |  +- raven
|  |  |  |  +- eight
|  |  |  |  +- five
|  |  |  |  +- four
|  |  |  |  +- nine
|  |  |  |  +- one
|  |  |  |  +- seven
|  |  |  |  +- six
|  |  |  |  +- three
|  |  |  |  `- two
|  |  |  +- raven_ship_sign
|  |  |  +- sand
|  |  |  |  `- plating
|  |  |  +- stripes
|  |  |  |  +- asteroid
|  |  |  |  |  +- box
|  |  |  |  |  +- corner
|  |  |  |  |  +- end
|  |  |  |  |  +- full
|  |  |  |  |  `- line
|  |  |  |  +- box
|  |  |  |  +- corner
|  |  |  |  +- end
|  |  |  |  +- full
|  |  |  |  +- line
|  |  |  |  +- red
|  |  |  |  |  +- box
|  |  |  |  |  +- corner
|  |  |  |  |  +- end
|  |  |  |  |  +- full
|  |  |  |  |  `- line
|  |  |  |  `- white
|  |  |  |     +- box
|  |  |  |     +- corner
|  |  |  |     +- end
|  |  |  |     +- full
|  |  |  |     `- line
|  |  |  +- tile
|  |  |  |  +- bar
|  |  |  |  +- blue
|  |  |  |  +- brown
|  |  |  |  +- green
|  |  |  |  +- neutral
|  |  |  |  +- purple
|  |  |  |  +- red
|  |  |  |  `- yellow
|  |  |  +- trimline
|  |  |  |  +- blue
|  |  |  |  |  +- corner
|  |  |  |  |  +- end
|  |  |  |  |  +- filled
|  |  |  |  |  |  +- corner
|  |  |  |  |  |  +- end
|  |  |  |  |  |  `- line
|  |  |  |  |  `- line
|  |  |  |  +- brown
|  |  |  |  |  +- corner
|  |  |  |  |  +- end
|  |  |  |  |  +- filled
|  |  |  |  |  |  +- corner
|  |  |  |  |  |  +- end
|  |  |  |  |  |  `- line
|  |  |  |  |  `- line
|  |  |  |  +- green
|  |  |  |  |  +- corner
|  |  |  |  |  +- end
|  |  |  |  |  +- filled
|  |  |  |  |  |  +- corner
|  |  |  |  |  |  +- end
|  |  |  |  |  |  `- line
|  |  |  |  |  `- line
|  |  |  |  +- neutral
|  |  |  |  |  +- corner
|  |  |  |  |  +- end
|  |  |  |  |  +- filled
|  |  |  |  |  |  +- corner
|  |  |  |  |  |  +- end
|  |  |  |  |  |  `- line
|  |  |  |  |  `- line
|  |  |  |  +- purple
|  |  |  |  |  +- corner
|  |  |  |  |  +- end
|  |  |  |  |  +- filled
|  |  |  |  |  |  +- corner
|  |  |  |  |  |  +- end
|  |  |  |  |  |  `- line
|  |  |  |  |  `- line
|  |  |  |  +- red
|  |  |  |  |  +- corner
|  |  |  |  |  +- end
|  |  |  |  |  +- filled
|  |  |  |  |  |  +- corner
|  |  |  |  |  |  +- end
|  |  |  |  |  |  `- line
|  |  |  |  |  `- line
|  |  |  |  +- white
|  |  |  |  |  +- corner
|  |  |  |  |  +- end
|  |  |  |  |  +- filled
|  |  |  |  |  |  +- corner
|  |  |  |  |  |  +- end
|  |  |  |  |  |  `- line
|  |  |  |  |  `- line
|  |  |  |  `- yellow
|  |  |  |     +- corner
|  |  |  |     +- end
|  |  |  |     +- filled
|  |  |  |     |  +- corner
|  |  |  |     |  +- end
|  |  |  |     |  `- line
|  |  |  |     `- line
|  |  |  `- weather
|  |  |     +- dirt
|  |  |     +- sand
|  |  |     |  `- light
|  |  |     `- snow
|  |  |        `- corner
|  |  +- visuals
|  |  |  `- black_ice
|  |  +- waterfall
|  |  |  `- acid
|  |  +- whirlpool
|  |  +- wisp
|  |  |  `- prestidigitation
|  |  `- wither_zone
|  +- emitters
|  |  `- weather
|  |     `- rain
|  +- fae_trickery_trap
|  |  +- disorient
|  |  `- drop
|  +- gblock
|  +- item
|  |  +- abyssal_marker
|  |  |  +- tidal
|  |  |  `- volatile
|  |  +- alch
|  |  |  +- airdust
|  |  |  +- artemisia
|  |  |  +- atropa
|  |  |  +- benedictus
|  |  |  +- berrypowder
|  |  |  +- bone
|  |  |  +- bonemeal
|  |  |  +- calendula
|  |  |  +- coaldust
|  |  |  +- earthdust
|  |  |  +- euphrasia
|  |  |  +- feaudust
|  |  |  +- firedust
|  |  |  +- golddust
|  |  |  +- hag_moss
|  |  |  |  +- enchanted
|  |  |  |  |  +- caring
|  |  |  |  |  +- corrosive
|  |  |  |  |  +- crawling
|  |  |  |  |  +- creeping
|  |  |  |  |  +- deathless
|  |  |  |  |  +- dreamy
|  |  |  |  |  +- drowned
|  |  |  |  |  +- gilded
|  |  |  |  |  +- random
|  |  |  |  |  |  +- high
|  |  |  |  |  |  +- low
|  |  |  |  |  |  `- mid
|  |  |  |  |  +- rooted
|  |  |  |  |  +- rotting
|  |  |  |  |  `- soaked
|  |  |  |  +- envy
|  |  |  |  +- fury
|  |  |  |  +- grief
|  |  |  |  +- lullaby
|  |  |  |  +- mercy
|  |  |  |  +- pride
|  |  |  |  `- sorrow
|  |  |  +- horn
|  |  |  +- hypericum
|  |  |  +- infernaldust
|  |  |  +- irondust
|  |  |  +- magicdust
|  |  |  +- manabloompowder
|  |  |  +- matricaria
|  |  |  +- mentha
|  |  |  +- mineraldust
|  |  |  +- ozium
|  |  |  +- paris
|  |  |  +- puresalt
|  |  |  +- rosa
|  |  |  +- runedust
|  |  |  +- salvia
|  |  |  +- seeddust
|  |  |  +- silverdust
|  |  |  +- sinew
|  |  |  +- solardust
|  |  |  +- swampdust
|  |  |  +- symphitum
|  |  |  +- taraxacum
|  |  |  +- tobaccodust
|  |  |  +- transisdust
|  |  |  +- urtica
|  |  |  +- valeriana
|  |  |  +- viscera
|  |  |  `- waterdust
|  |  +- ammo_box
|  |  |  `- magazine
|  |  |     `- internal
|  |  |        `- shot
|  |  |           +- bow
|  |  |           +- heavy_xbow
|  |  |           +- sling
|  |  |           +- slurbow
|  |  |           `- xbow
|  |  +- ammo_casing
|  |  |  +- caseless
|  |  |  |  `- rogue
|  |  |  |     +- arrow
|  |  |  |     |  +- blunt
|  |  |  |     |  +- bronze
|  |  |  |     |  +- elemental
|  |  |  |     |  |  +- fire
|  |  |  |     |  |  +- frost
|  |  |  |     |  |  +- kinetic
|  |  |  |     |  |  +- splinter
|  |  |  |     |  |  `- thunder
|  |  |  |     |  +- iron
|  |  |  |     |  |  `- aalloy
|  |  |  |     |  +- poison
|  |  |  |     |  +- silver
|  |  |  |     |  +- steel
|  |  |  |     |  |  `- paalloy
|  |  |  |     |  +- stone
|  |  |  |     |  |  `- poison
|  |  |  |     |  `- water
|  |  |  |     +- bolt
|  |  |  |     |  +- aalloy
|  |  |  |     |  +- blunt
|  |  |  |     |  +- bronze
|  |  |  |     |  +- holy
|  |  |  |     |  +- light
|  |  |  |     |  +- paalloy
|  |  |  |     |  +- poison
|  |  |  |     |  +- pyro
|  |  |  |     |  +- silver
|  |  |  |     |  `- water
|  |  |  |     +- bullet
|  |  |  |     +- heavy_bolt
|  |  |  |     |  +- aalloy
|  |  |  |     |  +- blunt
|  |  |  |     |  +- bronze
|  |  |  |     |  +- paalloy
|  |  |  |     |  `- silver
|  |  |  |     +- javelin
|  |  |  |     |  +- aalloy
|  |  |  |     |  +- bronze
|  |  |  |     |  +- silver
|  |  |  |     |  `- steel
|  |  |  |     |     `- paalloy
|  |  |  |     `- sling_bullet
|  |  |  |        +- aalloy
|  |  |  |        +- bronze
|  |  |  |        +- fire_pot
|  |  |  |        +- heavy_sling_bullet
|  |  |  |        +- iron
|  |  |  |        +- paalloy
|  |  |  |        +- scattershot
|  |  |  |        `- stone
|  |  |  `- spent
|  |  +- antag_spawner
|  |  +- armor_brush
|  |  +- armorkit_empty
|  |  +- ash
|  |  |  `- snappop_phoenix
|  |  +- bait
|  |  |  +- bloody
|  |  |  +- leech
|  |  |  +- spider
|  |  |  `- sweet
|  |  +- banhammer
|  |  +- bedroll
|  |  +- bedsheet
|  |  |  +- random
|  |  |  `- rogue
|  |  |     +- cloth
|  |  |     +- double_pelt
|  |  |     +- fabric
|  |  |     +- fabric_double
|  |  |     +- pelt
|  |  |     `- wool
|  |  +- bee_smoker
|  |  +- bee_treatment
|  |  |  +- antiviral
|  |  |  +- insecticide
|  |  |  `- miticide
|  |  +- black_rose
|  |  +- bloodcrawl
|  |  +- blueprint
|  |  |  `- mace_mushroom
|  |  +- bodybag
|  |  +- bodypart
|  |  |  +- chest
|  |  |  |  +- devil
|  |  |  |  +- goblin
|  |  |  |  +- monkey
|  |  |  |  `- spirit
|  |  |  +- head
|  |  |  |  +- devil
|  |  |  |  +- monkey
|  |  |  |  `- spirit
|  |  |  +- l_arm
|  |  |  |  +- devil
|  |  |  |  +- goblin
|  |  |  |  +- monkey
|  |  |  |  +- prosthetic
|  |  |  |  |  +- bronzeleft
|  |  |  |  |  +- gold
|  |  |  |  |  +- iron
|  |  |  |  |  +- steel
|  |  |  |  |  `- woodleft
|  |  |  |  `- spirit
|  |  |  +- l_leg
|  |  |  |  +- devil
|  |  |  |  +- digitigrade
|  |  |  |  +- goblin
|  |  |  |  +- monkey
|  |  |  |  +- prosthetic
|  |  |  |  |  +- bronzeleft
|  |  |  |  |  +- gold
|  |  |  |  |  +- iron
|  |  |  |  |  `- steel
|  |  |  |  `- spirit
|  |  |  +- r_arm
|  |  |  |  +- devil
|  |  |  |  +- goblin
|  |  |  |  +- monkey
|  |  |  |  +- prosthetic
|  |  |  |  |  +- bronzeright
|  |  |  |  |  +- gold
|  |  |  |  |  +- iron
|  |  |  |  |  +- steel
|  |  |  |  |  `- woodright
|  |  |  |  `- spirit
|  |  |  +- r_leg
|  |  |  |  +- devil
|  |  |  |  +- digitigrade
|  |  |  |  +- goblin
|  |  |  |  +- monkey
|  |  |  |  +- prosthetic
|  |  |  |  |  +- bronzeright
|  |  |  |  |  +- gold
|  |  |  |  |  +- iron
|  |  |  |  |  `- steel
|  |  |  |  `- spirit
|  |  |  `- taur
|  |  |     +- goat
|  |  |     +- horse
|  |  |     +- lamia
|  |  |     `- spider
|  |  +- bomb
|  |  |  +- smoke
|  |  |  `- tripbomb
|  |  +- bone
|  |  |  `- splinter
|  |  +- book
|  |  |  +- arcyne_compendium
|  |  |  +- granter
|  |  |  |  +- action
|  |  |  |  +- arcane_aspect
|  |  |  |  |  +- major
|  |  |  |  |  +- mastery
|  |  |  |  |  +- minor
|  |  |  |  |  `- utility
|  |  |  |  +- crafting_recipe
|  |  |  |  |  `- tailor
|  |  |  |  |     +- eastern
|  |  |  |  |     `- western
|  |  |  |  `- spell
|  |  |  |     +- bonechill
|  |  |  |     +- mimery_blockade
|  |  |  |     `- random
|  |  |  +- manual
|  |  |  |  `- random
|  |  |  +- mimery
|  |  |  +- random
|  |  |  |  `- triple
|  |  |  +- rogue
|  |  |  |  +- abyssor
|  |  |  |  +- arcyne
|  |  |  |  +- beardling
|  |  |  |  +- bibble
|  |  |  |  |  `- psy
|  |  |  |  +- blackmountain
|  |  |  |  +- bookofpriests
|  |  |  |  +- cardgame
|  |  |  |  +- cooking
|  |  |  |  +- festus
|  |  |  |  +- fishing
|  |  |  |  +- knowledge1
|  |  |  |  +- law
|  |  |  |  +- loadoutbook
|  |  |  |  +- naledi1
|  |  |  |  +- naledi2
|  |  |  |  +- naledi3
|  |  |  |  +- naledi4
|  |  |  |  +- necra
|  |  |  |  +- nitebeast
|  |  |  |  +- noc
|  |  |  |  +- playerbook
|  |  |  |  +- robber
|  |  |  |  +- secret
|  |  |  |  |  +- dragon_stanza
|  |  |  |  |  +- ledger
|  |  |  |  |  +- thefireisgone
|  |  |  |  |  `- xylix
|  |  |  |  +- sword
|  |  |  |  +- tales1
|  |  |  |  +- tales3
|  |  |  |  `- yeoldecookingmanual
|  |  |  `- spellbook
|  |  +- book_crafting_kit
|  |  +- bottle_kit
|  |  +- bountytrap
|  |  +- bouquet
|  |  |  +- calendula
|  |  |  +- matricaria
|  |  |  +- rosa
|  |  |  `- salvia
|  |  +- broom
|  |  +- burial_shroud
|  |  +- candle
|  |  |  +- candlestick
|  |  |  |  +- gold
|  |  |  |  |  +- lit
|  |  |  |  |  `- single
|  |  |  |  |     `- lit
|  |  |  |  `- silver
|  |  |  |     +- lit
|  |  |  |     `- single
|  |  |  |        `- lit
|  |  |  +- eora
|  |  |  |  `- lit
|  |  |  +- gold
|  |  |  |  `- lit
|  |  |  +- infinite
|  |  |  +- lit
|  |  |  +- silver
|  |  |  |  `- lit
|  |  |  +- skull
|  |  |  |  `- lit
|  |  |  `- yellow
|  |  |     `- lit
|  |  +- canvas
|  |  +- caparison
|  |  |  +- astrata
|  |  |  +- azure
|  |  |  +- drd
|  |  |  +- eora
|  |  |  +- fogbeast
|  |  |  +- heartfelt
|  |  |  +- psy
|  |  |  `- ryan
|  |  +- carpet
|  |  |  +- exotic
|  |  |  `- standard
|  |  +- cart_upgrade
|  |  |  +- level_1
|  |  |  `- level_2
|  |  +- carvedgem
|  |  |  +- amber
|  |  |  |  +- beaver
|  |  |  |  +- bust
|  |  |  |  +- cameo
|  |  |  |  +- comb
|  |  |  |  +- duck
|  |  |  |  +- fancyvase
|  |  |  |  +- figurine
|  |  |  |  +- fish
|  |  |  |  +- obelisk
|  |  |  |  +- statue
|  |  |  |  +- sun
|  |  |  |  +- tablet
|  |  |  |  +- urn
|  |  |  |  `- vase
|  |  |  +- coral
|  |  |  |  +- bust
|  |  |  |  +- cameo
|  |  |  |  +- comb
|  |  |  |  +- duck
|  |  |  |  +- fancyvase
|  |  |  |  +- figurine
|  |  |  |  +- fish
|  |  |  |  +- jaw
|  |  |  |  +- obelisk
|  |  |  |  +- shark
|  |  |  |  +- statue
|  |  |  |  +- tablet
|  |  |  |  +- urn
|  |  |  |  `- vase
|  |  |  +- jade
|  |  |  |  +- bust
|  |  |  |  +- cameo
|  |  |  |  +- comb
|  |  |  |  +- duck
|  |  |  |  +- fancyvase
|  |  |  |  +- figurine
|  |  |  |  +- fish
|  |  |  |  +- obelisk
|  |  |  |  +- statue
|  |  |  |  +- tablet
|  |  |  |  +- urn
|  |  |  |  +- vase
|  |  |  |  `- wyrm
|  |  |  +- onyxa
|  |  |  |  +- bust
|  |  |  |  +- cameo
|  |  |  |  +- comb
|  |  |  |  +- duck
|  |  |  |  +- fancyvase
|  |  |  |  +- figurine
|  |  |  |  +- fish
|  |  |  |  +- obelisk
|  |  |  |  +- snake
|  |  |  |  +- spider
|  |  |  |  +- statue
|  |  |  |  +- tablet
|  |  |  |  +- urn
|  |  |  |  `- vase
|  |  |  +- opal
|  |  |  |  +- bust
|  |  |  |  +- cameo
|  |  |  |  +- comb
|  |  |  |  +- crab
|  |  |  |  +- duck
|  |  |  |  +- fancyvase
|  |  |  |  +- figurine
|  |  |  |  +- fish
|  |  |  |  +- obelisk
|  |  |  |  +- statue
|  |  |  |  +- tablet
|  |  |  |  +- urn
|  |  |  |  `- vase
|  |  |  +- rose
|  |  |  |  +- bust
|  |  |  |  +- cameo
|  |  |  |  +- carp
|  |  |  |  +- comb
|  |  |  |  +- duck
|  |  |  |  +- fancyvase
|  |  |  |  +- figurine
|  |  |  |  +- fish
|  |  |  |  +- flower
|  |  |  |  +- obelisk
|  |  |  |  +- rawrose
|  |  |  |  +- statue
|  |  |  |  +- tablet
|  |  |  |  +- urn
|  |  |  |  `- vase
|  |  |  +- shell
|  |  |  |  +- bust
|  |  |  |  +- cameo
|  |  |  |  +- comb
|  |  |  |  +- duck
|  |  |  |  +- fancyvase
|  |  |  |  +- figurine
|  |  |  |  +- fish
|  |  |  |  +- obelisk
|  |  |  |  +- openoyster
|  |  |  |  +- rawshell
|  |  |  |  +- statue
|  |  |  |  +- tablet
|  |  |  |  +- turtle
|  |  |  |  +- urn
|  |  |  |  `- vase
|  |  |  `- turq
|  |  |     +- bust
|  |  |     +- cameo
|  |  |     +- comb
|  |  |     +- duck
|  |  |     +- fancyvase
|  |  |     +- figurine
|  |  |     +- fish
|  |  |     +- ka
|  |  |     +- obelisk
|  |  |     +- scarab
|  |  |     +- statue
|  |  |     +- tablet
|  |  |     +- urn
|  |  |     `- vase
|  |  +- chair
|  |  |  +- greyscale
|  |  |  +- rogue
|  |  |  |  +- crafted
|  |  |  |  `- fancy
|  |  |  |     `- crafted
|  |  |  +- stool
|  |  |  |  `- bar
|  |  |  |     `- rogue
|  |  |  |        `- crafted
|  |  |  `- wood
|  |  |     `- wings
|  |  +- chalk
|  |  +- cigbutt
|  |  |  +- cigarbutt
|  |  |  `- roach
|  |  +- clothing
|  |  |  +- accessory
|  |  |  |  `- medal
|  |  |  |     `- gold
|  |  |  |        `- ordom
|  |  |  +- barding
|  |  |  |  +- chain
|  |  |  |  `- fogbeast
|  |  |  |     `- chain
|  |  |  +- climbing_gear
|  |  |  +- cloak
|  |  |  |  +- absolutionistrobe
|  |  |  |  +- apron
|  |  |  |  |  +- blacksmith
|  |  |  |  |  +- brown
|  |  |  |  |  +- cook
|  |  |  |  |  `- waist
|  |  |  |  |     +- bar
|  |  |  |  |     +- brown
|  |  |  |  |     +- fancymaid
|  |  |  |  |     `- maid
|  |  |  |  +- bandolier
|  |  |  |  +- banneret
|  |  |  |  +- battlenun
|  |  |  |  +- black_cloak
|  |  |  |  +- cape
|  |  |  |  |  +- archivist
|  |  |  |  |  +- blkknight
|  |  |  |  |  +- crusader
|  |  |  |  |  +- fur
|  |  |  |  |  +- guard
|  |  |  |  |  +- hood
|  |  |  |  |  +- inquisitor
|  |  |  |  |  +- knight
|  |  |  |  |  +- puritan
|  |  |  |  |  +- purple
|  |  |  |  |  +- red
|  |  |  |  |  `- rogue
|  |  |  |  +- chasuble
|  |  |  |  +- cotehardie
|  |  |  |  |  `- mageblue
|  |  |  |  +- darkcloak
|  |  |  |  |  +- bear
|  |  |  |  |  |  `- light
|  |  |  |  |  `- minotaur
|  |  |  |  |     `- red
|  |  |  |  +- eastcloak1
|  |  |  |  +- eastcloak2
|  |  |  |  +- forrestercloak
|  |  |  |  |  +- autumn
|  |  |  |  |  `- snow
|  |  |  |  +- graggar
|  |  |  |  +- half
|  |  |  |  |  +- brown
|  |  |  |  |  +- lich
|  |  |  |  |  +- orange
|  |  |  |  |  +- red
|  |  |  |  |  +- rider
|  |  |  |  |  |  `- red
|  |  |  |  |  +- shadowcloak
|  |  |  |  |  `- vet
|  |  |  |  +- heartfelt
|  |  |  |  +- hierophant
|  |  |  |  +- holysee
|  |  |  |  +- kazengun
|  |  |  |  +- lordcloak
|  |  |  |  |  `- ladycloak
|  |  |  |  +- martyr
|  |  |  |  +- matron
|  |  |  |  +- ordinatorcape
|  |  |  |  |  `- lirvas
|  |  |  |  +- poncho
|  |  |  |  |  +- dittocloak
|  |  |  |  |  +- fancycoat
|  |  |  |  |  `- mageblue
|  |  |  |  +- psyaltrist
|  |  |  |  +- raincloak
|  |  |  |  |  +- blue
|  |  |  |  |  +- brown
|  |  |  |  |  +- feather_cloak
|  |  |  |  |  +- furcloak
|  |  |  |  |  |  +- black
|  |  |  |  |  |  +- brown
|  |  |  |  |  |  +- crafted
|  |  |  |  |  |  +- darkgreen
|  |  |  |  |  |  `- woad
|  |  |  |  |  +- green
|  |  |  |  |  +- mageblue
|  |  |  |  |  +- mortus
|  |  |  |  |  +- purple
|  |  |  |  |  `- red
|  |  |  |  +- scaledcloak
|  |  |  |  +- stole
|  |  |  |  |  +- purple
|  |  |  |  |  `- red
|  |  |  |  +- tabard
|  |  |  |  |  +- abyssorite
|  |  |  |  |  +- black
|  |  |  |  |  +- blkknight
|  |  |  |  |  +- crusader
|  |  |  |  |  |  +- abyssor
|  |  |  |  |  |  +- astrata
|  |  |  |  |  |  +- dendor
|  |  |  |  |  |  +- eora
|  |  |  |  |  |  +- malum
|  |  |  |  |  |  +- necra
|  |  |  |  |  |  +- noc
|  |  |  |  |  |  +- pestra
|  |  |  |  |  |  +- psydon
|  |  |  |  |  |  +- ravox
|  |  |  |  |  |  `- tief
|  |  |  |  |  +- devotee
|  |  |  |  |  |  +- abyssor
|  |  |  |  |  |  +- astrata
|  |  |  |  |  |  +- dendor
|  |  |  |  |  |  +- eora
|  |  |  |  |  |  +- malum
|  |  |  |  |  |  +- necra
|  |  |  |  |  |  +- noc
|  |  |  |  |  |  +- pestra
|  |  |  |  |  |  +- psydon
|  |  |  |  |  |  +- ravox
|  |  |  |  |  |  `- xylix
|  |  |  |  |  +- knight
|  |  |  |  |  +- lich
|  |  |  |  |  +- psydontabard
|  |  |  |  |  |  `- alt
|  |  |  |  |  +- retinue
|  |  |  |  |  |  `- banneret
|  |  |  |  |  +- sleevedtabard
|  |  |  |  |  `- stabard
|  |  |  |  |     +- black
|  |  |  |  |     +- bog
|  |  |  |  |     +- crusader
|  |  |  |  |     |  +- astrata
|  |  |  |  |     |  +- bsteel
|  |  |  |  |     |  +- heavy
|  |  |  |  |     |  +- legacy
|  |  |  |  |     |  +- t
|  |  |  |  |     |  |  +- astrata
|  |  |  |  |     |  |  +- legacy
|  |  |  |  |     |  |  `- undivided
|  |  |  |  |     |  `- undivided
|  |  |  |  |     +- dungeon
|  |  |  |  |     +- grenzelhoft
|  |  |  |  |     +- grenzelmage
|  |  |  |  |     +- guard
|  |  |  |  |     +- guardhood
|  |  |  |  |     |  +- elder
|  |  |  |  |     |  `- lich
|  |  |  |  |     +- mercenary
|  |  |  |  |     `- surcoat
|  |  |  |  |        +- bailiff
|  |  |  |  |        +- councillor
|  |  |  |  |        +- guard
|  |  |  |  |        +- lich
|  |  |  |  |        `- short
|  |  |  |  +- templar
|  |  |  |  |  +- astratan
|  |  |  |  |  +- eoran
|  |  |  |  |  +- malumite
|  |  |  |  |  +- necran
|  |  |  |  |  +- pestran
|  |  |  |  |  +- ravox
|  |  |  |  |  +- undivided
|  |  |  |  |  +- undivided_alt
|  |  |  |  |  `- xylixian
|  |  |  |  |     `- faux
|  |  |  |  +- thief_cloak
|  |  |  |  |  +- mageblue
|  |  |  |  |  `- yoruku
|  |  |  |  +- tribal
|  |  |  |  +- undivided
|  |  |  |  +- volfmantle
|  |  |  |  +- wardencloak
|  |  |  |  `- wickercloak
|  |  |  +- glasses
|  |  |  |  `- blindfold
|  |  |  |     `- white
|  |  |  +- gloves
|  |  |  |  `- roguetown
|  |  |  |     +- angle
|  |  |  |     |  +- atgervi
|  |  |  |     |  +- grenzelgloves
|  |  |  |     |  |  +- blacksmith
|  |  |  |     |  |  `- freifechter
|  |  |  |     |  +- gronn
|  |  |  |     |  `- gronnfur
|  |  |  |     +- bandages
|  |  |  |     |  +- pontifex
|  |  |  |     |  +- pugilist
|  |  |  |     |  `- weighted
|  |  |  |     +- chain
|  |  |  |     |  +- aalloy
|  |  |  |     |  +- black
|  |  |  |     |  +- blk
|  |  |  |     |  +- contraption
|  |  |  |     |  |  `- voltic
|  |  |  |     |  +- gronn
|  |  |  |     |  +- iron
|  |  |  |     |  +- paalloy
|  |  |  |     |  +- psydon
|  |  |  |     |  `- vampire
|  |  |  |     +- courtphysician
|  |  |  |     |  `- female
|  |  |  |     +- eastgloves1
|  |  |  |     +- eastgloves2
|  |  |  |     +- elven_gloves
|  |  |  |     |  `- autumn
|  |  |  |     +- fingerless
|  |  |  |     |  `- shadowgloves
|  |  |  |     |     `- elflock
|  |  |  |     +- fingerless_leather
|  |  |  |     +- knuckles
|  |  |  |     |  +- ancient
|  |  |  |     |  +- bronze
|  |  |  |     |  |  `- zizoconstruct
|  |  |  |     |  +- decrepit
|  |  |  |     |  +- eora
|  |  |  |     |  `- psydon
|  |  |  |     |     `- old
|  |  |  |     +- leather
|  |  |  |     |  `- black
|  |  |  |     +- nomagic
|  |  |  |     +- otavan
|  |  |  |     |  +- inqgloves
|  |  |  |     |  `- psygloves
|  |  |  |     `- plate
|  |  |  |        +- aalloy
|  |  |  |        +- atgervi
|  |  |  |        +- blacksteel
|  |  |  |        |  `- modern
|  |  |  |        +- blkknight
|  |  |  |        |  `- death
|  |  |  |        +- dreamwalker
|  |  |  |        +- dwarven
|  |  |  |        +- graggar
|  |  |  |        +- holysee
|  |  |  |        |  `- ritual
|  |  |  |        +- iron
|  |  |  |        |  `- gronn
|  |  |  |        +- kote
|  |  |  |        +- matthios
|  |  |  |        +- paalloy
|  |  |  |        +- shadowgauntlets
|  |  |  |        `- zizo
|  |  |  +- head
|  |  |  |  +- hooded
|  |  |  |  |  `- rainhood
|  |  |  |  |     +- feather_hood
|  |  |  |  |     `- furhood
|  |  |  |  +- inqarticles
|  |  |  |  |  `- blackbag
|  |  |  |  +- mob_holder
|  |  |  |  +- peaceflower
|  |  |  |  `- roguetown
|  |  |  |     +- antlerhood
|  |  |  |     +- archercap
|  |  |  |     +- armingcap
|  |  |  |     |  `- padded
|  |  |  |     +- articap
|  |  |  |     +- bardhat
|  |  |  |     +- beekeeper
|  |  |  |     +- briarthorns
|  |  |  |     +- brimmed
|  |  |  |     +- bucklehat
|  |  |  |     +- cap
|  |  |  |     |  `- dwarf
|  |  |  |     +- chaperon
|  |  |  |     |  +- councillor
|  |  |  |     |  +- greyscale
|  |  |  |     |  |  +- elder
|  |  |  |     |  |  `- shepherd
|  |  |  |     |  `- noble
|  |  |  |     |     +- bailiff
|  |  |  |     |     +- evil
|  |  |  |     |     +- guildmaster
|  |  |  |     |     `- hand
|  |  |  |     +- chef
|  |  |  |     +- circlet
|  |  |  |     |  +- carvedgem
|  |  |  |     |  |  +- amber
|  |  |  |     |  |  +- coral
|  |  |  |     |  |  +- jade
|  |  |  |     |  |  +- onyxa
|  |  |  |     |  |  +- opal
|  |  |  |     |  |  +- rose
|  |  |  |     |  |  +- shell
|  |  |  |     |  |  `- turq
|  |  |  |     |  +- saffiratiara
|  |  |  |     |  `- triumph
|  |  |  |     +- cookhat
|  |  |  |     +- courtphysician
|  |  |  |     |  `- female
|  |  |  |     +- crown
|  |  |  |     |  +- fakecrown
|  |  |  |     |  +- serpcrown
|  |  |  |     |  +- sparrowcrown
|  |  |  |     |  `- surplus
|  |  |  |     +- cyberdeck
|  |  |  |     +- dendormask
|  |  |  |     +- deserthood
|  |  |  |     +- duelhat
|  |  |  |     |  `- pretzel
|  |  |  |     +- eoramask
|  |  |  |     +- explorerhat
|  |  |  |     +- fancyhat
|  |  |  |     +- fedora
|  |  |  |     +- fisherhat
|  |  |  |     +- flathat
|  |  |  |     +- grenzelhofthat
|  |  |  |     |  `- triumph
|  |  |  |     +- hatblu
|  |  |  |     +- hatfur
|  |  |  |     +- headband
|  |  |  |     |  +- bloodied
|  |  |  |     |  +- monk
|  |  |  |     |  |  `- barbarian
|  |  |  |     |  +- naledi
|  |  |  |     |  `- red
|  |  |  |     +- headdress
|  |  |  |     |  `- alt
|  |  |  |     +- helmet
|  |  |  |     |  +- bandana
|  |  |  |     |  +- bascinet
|  |  |  |     |  |  +- antler
|  |  |  |     |  |  +- atgervi
|  |  |  |     |  |  |  `- gronn
|  |  |  |     |  |  |     `- ownel
|  |  |  |     |  |  +- dreamwalker
|  |  |  |     |  |  +- etruscan
|  |  |  |     |  |  |  +- black
|  |  |  |     |  |  |  `- grenzelhoft
|  |  |  |     |  |  |     `- triumph
|  |  |  |     |  |  `- pigface
|  |  |  |     |  |     +- black
|  |  |  |     |  |     `- hounskull
|  |  |  |     |  |        +- black
|  |  |  |     |  |        `- dakken
|  |  |  |     |  +- blacksteel
|  |  |  |     |  |  +- modern
|  |  |  |     |  |  |  `- grenzelhoft
|  |  |  |     |  |  |     `- triumph
|  |  |  |     |  |  `- psythorns
|  |  |  |     |  +- bronze
|  |  |  |     |  +- bronzegladiator
|  |  |  |     |  +- coppercap
|  |  |  |     |  +- elvenbarbute
|  |  |  |     |  |  +- blackoak
|  |  |  |     |  |  `- winged
|  |  |  |     |  |     `- blackoak
|  |  |  |     |  +- goblin
|  |  |  |     |  +- heavy
|  |  |  |     |  |  +- aalloy
|  |  |  |     |  |  +- absolver
|  |  |  |     |  |  |  `- unblessed
|  |  |  |     |  |  +- abyssorgreathelm
|  |  |  |     |  |  +- astratahelm
|  |  |  |     |  |  +- astratan
|  |  |  |     |  |  +- banneret
|  |  |  |     |  |  +- barbute
|  |  |  |     |  |  |  +- great
|  |  |  |     |  |  |  `- visor
|  |  |  |     |  |  |     `- dakken
|  |  |  |     |  |  +- beakhelm
|  |  |  |     |  |  +- bronze
|  |  |  |     |  |  +- bucket
|  |  |  |     |  |  |  +- black
|  |  |  |     |  |  |  +- crusader
|  |  |  |     |  |  |  |  +- blacksteel
|  |  |  |     |  |  |  |  `- gold
|  |  |  |     |  |  |  |     `- cleric
|  |  |  |     |  |  |  +- gold
|  |  |  |     |  |  |  |  `- cleric
|  |  |  |     |  |  |  +- gronn
|  |  |  |     |  |  |  `- iron
|  |  |  |     |  |  +- crusader
|  |  |  |     |  |  |  `- t
|  |  |  |     |  |  +- dendorhelm
|  |  |  |     |  |  +- dwarven
|  |  |  |     |  |  |  `- smith
|  |  |  |     |  |  +- elven_helm
|  |  |  |     |  |  |  +- autumn
|  |  |  |     |  |  |  |  `- light
|  |  |  |     |  |  |  `- light
|  |  |  |     |  |  +- eoran
|  |  |  |     |  |  +- frogmouth
|  |  |  |     |  |  |  `- greatplume
|  |  |  |     |  |  +- graggar
|  |  |  |     |  |  +- guard
|  |  |  |     |  |  |  +- aalloy
|  |  |  |     |  |  |  +- black
|  |  |  |     |  |  |  +- bogman
|  |  |  |     |  |  |  `- paalloy
|  |  |  |     |  |  +- holysee
|  |  |  |     |  |  |  `- alt
|  |  |  |     |  |  +- kabuto
|  |  |  |     |  |  +- knight
|  |  |  |     |  |  |  +- aalloy
|  |  |  |     |  |  |  +- armet
|  |  |  |     |  |  |  |  +- black
|  |  |  |     |  |  |  |  +- dakken
|  |  |  |     |  |  |  |  +- dasfox
|  |  |  |     |  |  |  |  `- eiren_helmet
|  |  |  |     |  |  |  +- black
|  |  |  |     |  |  |  +- fluted
|  |  |  |     |  |  |  +- gilded
|  |  |  |     |  |  |  +- gold
|  |  |  |     |  |  |  |  `- king
|  |  |  |     |  |  |  +- greatplume
|  |  |  |     |  |  |  |  `- fluted
|  |  |  |     |  |  |  +- iron
|  |  |  |     |  |  |  |  `- greatplume
|  |  |  |     |  |  |  +- old
|  |  |  |     |  |  |  |  `- iron
|  |  |  |     |  |  |  +- paalloy
|  |  |  |     |  |  |  `- skettle
|  |  |  |     |  |  |     `- black
|  |  |  |     |  |  +- malum
|  |  |  |     |  |  +- matthios
|  |  |  |     |  |  +- necrahelm
|  |  |  |     |  |  +- necran
|  |  |  |     |  |  +- nochelm
|  |  |  |     |  |  +- ordinatorhelm
|  |  |  |     |  |  |  `- plume
|  |  |  |     |  |  +- paalloy
|  |  |  |     |  |  +- pestran
|  |  |  |     |  |  |  `- keeper
|  |  |  |     |  |  +- psybucket
|  |  |  |     |  |  +- psydonbarbute
|  |  |  |     |  |  +- psydonhelm
|  |  |  |     |  |  |  `- ryan
|  |  |  |     |  |  +- psysallet
|  |  |  |     |  |  +- ravoxhelm
|  |  |  |     |  |  +- sheriff
|  |  |  |     |  |  |  +- black
|  |  |  |     |  |  |  `- gold
|  |  |  |     |  |  |     `- king
|  |  |  |     |  |  +- undivided
|  |  |  |     |  |  +- undivided_ritual
|  |  |  |     |  |  +- vampire
|  |  |  |     |  |  +- volfplate
|  |  |  |     |  |  |  +- berserker
|  |  |  |     |  |  |  `- puritan
|  |  |  |     |  |  +- xylixhelm
|  |  |  |     |  |  `- zizo
|  |  |  |     |  |     +- frogge
|  |  |  |     |  |     `- volfhelm
|  |  |  |     |  +- horned
|  |  |  |     |  +- kettle
|  |  |  |     |  |  +- aalloy
|  |  |  |     |  |  +- iron
|  |  |  |     |  |  +- jingasa
|  |  |  |     |  |  +- minershelm
|  |  |  |     |  |  +- paalloy
|  |  |  |     |  |  `- wide
|  |  |  |     |  +- leather
|  |  |  |     |  |  +- advanced
|  |  |  |     |  |  +- chapeau
|  |  |  |     |  |  +- goblin
|  |  |  |     |  |  +- saiga
|  |  |  |     |  |  |  `- atgervi
|  |  |  |     |  |  +- shaman_hood
|  |  |  |     |  |  `- volfhelm
|  |  |  |     |  +- otavan
|  |  |  |     |  +- sallet
|  |  |  |     |  |  +- beastskull
|  |  |  |     |  |  +- eoran
|  |  |  |     |  |  +- grenzelhoft
|  |  |  |     |  |  |  `- triumph
|  |  |  |     |  |  +- iron
|  |  |  |     |  |  +- raneshen
|  |  |  |     |  |  +- shishak
|  |  |  |     |  |  +- visored
|  |  |  |     |  |  |  +- black
|  |  |  |     |  |  |  +- gilded
|  |  |  |     |  |  |  `- iron
|  |  |  |     |  |  `- warden
|  |  |  |     |  |     +- bear
|  |  |  |     |  |     +- goat
|  |  |  |     |  |     +- rat
|  |  |  |     |  |     `- wolf
|  |  |  |     |  +- skullcap
|  |  |  |     |  +- tricorn
|  |  |  |     |  |  +- lucky
|  |  |  |     |  |  `- skull
|  |  |  |     |  `- winged
|  |  |  |     +- hennin
|  |  |  |     +- inqhat
|  |  |  |     |  `- gravehat
|  |  |  |     +- jester
|  |  |  |     +- knitcap
|  |  |  |     +- maidband
|  |  |  |     +- maidhead
|  |  |  |     +- menacing
|  |  |  |     |  +- bandit
|  |  |  |     |  +- executioner
|  |  |  |     |  `- mad_touched_treasure_hunter
|  |  |  |     +- mentorhat
|  |  |  |     |  +- koruu
|  |  |  |     |  `- walkthewaste
|  |  |  |     +- necrahood
|  |  |  |     +- necramask
|  |  |  |     +- necromhood
|  |  |  |     +- nightman
|  |  |  |     +- nun
|  |  |  |     +- nyle
|  |  |  |     |  `- consortcrown
|  |  |  |     +- papakha
|  |  |  |     |  `- crafted
|  |  |  |     +- physician
|  |  |  |     +- priesthat
|  |  |  |     +- priestmask
|  |  |  |     +- puritan
|  |  |  |     |  `- armored
|  |  |  |     +- reqhat
|  |  |  |     +- roguehood
|  |  |  |     |  +- abyssor
|  |  |  |     |  +- astrata
|  |  |  |     |  |  `- stonekeep
|  |  |  |     |  +- black
|  |  |  |     |  +- darkgreen
|  |  |  |     |  +- eorahood
|  |  |  |     |  +- feld
|  |  |  |     |  +- hierophant
|  |  |  |     |  +- mageblue
|  |  |  |     |  +- nochood
|  |  |  |     |  +- phys
|  |  |  |     |  +- pontifex
|  |  |  |     |  +- psydon
|  |  |  |     |  |  `- confessor
|  |  |  |     |  +- ravox
|  |  |  |     |  +- ravoxgorget
|  |  |  |     |  +- red
|  |  |  |     |  +- shalal
|  |  |  |     |  |  +- black
|  |  |  |     |  |  +- heavyhood
|  |  |  |     |  |  +- hijab
|  |  |  |     |  |  |  +- black
|  |  |  |     |  |  |  +- gallant
|  |  |  |     |  |  |  +- raneshen
|  |  |  |     |  |  |  `- yoruku
|  |  |  |     |  |  `- purple
|  |  |  |     |  +- shroudblack
|  |  |  |     |  +- shroudscarlet
|  |  |  |     |  +- shroudwhite
|  |  |  |     |  |  `- evil_ah_ah
|  |  |  |     |  +- studded
|  |  |  |     |  |  `- retinue
|  |  |  |     |  +- undivided
|  |  |  |     |  +- unholy
|  |  |  |     |  |  +- enchanted
|  |  |  |     |  |  `- lich
|  |  |  |     |  `- warden
|  |  |  |     |     +- antler
|  |  |  |     |     `- munitioneer
|  |  |  |     +- shawl
|  |  |  |     +- smokingcap
|  |  |  |     +- spellcasterhat
|  |  |  |     +- strawhat
|  |  |  |     +- vampire
|  |  |  |     +- veiled
|  |  |  |     |  `- loudmouth
|  |  |  |     +- witchhat
|  |  |  |     |  `- old
|  |  |  |     `- wizhat
|  |  |  |        +- black
|  |  |  |        +- gen
|  |  |  |        |  `- wise
|  |  |  |        +- green
|  |  |  |        +- red
|  |  |  |        `- yellow
|  |  |  +- mask
|  |  |  |  +- bandana
|  |  |  |  |  `- black
|  |  |  |  +- cigarette
|  |  |  |  |  +- cigar
|  |  |  |  |  |  +- cohiba
|  |  |  |  |  |  `- havana
|  |  |  |  |  +- pipe
|  |  |  |  |  |  +- cobpipe
|  |  |  |  |  |  +- crafted
|  |  |  |  |  |  `- westman
|  |  |  |  |  `- rollie
|  |  |  |  |     +- abyss
|  |  |  |  |     |  `- crafted
|  |  |  |  |     +- apple
|  |  |  |  |     |  `- crafted
|  |  |  |  |     +- blackberry
|  |  |  |  |     |  `- crafted
|  |  |  |  |     +- calendula
|  |  |  |  |     +- cannabis
|  |  |  |  |     |  `- cheroot
|  |  |  |  |     +- carrot
|  |  |  |  |     |  `- crafted
|  |  |  |  |     +- chocolate
|  |  |  |  |     |  `- crafted
|  |  |  |  |     +- jacksberries
|  |  |  |  |     |  `- crafted
|  |  |  |  |     +- jacksberriespoison
|  |  |  |  |     |  `- crafted
|  |  |  |  |     +- lime
|  |  |  |  |     |  `- crafted
|  |  |  |  |     +- mentha
|  |  |  |  |     |  `- crafted
|  |  |  |  |     +- menthaapple
|  |  |  |  |     |  `- crafted
|  |  |  |  |     +- mindbreaker
|  |  |  |  |     +- nicotine
|  |  |  |  |     |  `- cheroot
|  |  |  |  |     +- salvia
|  |  |  |  |     |  `- crafted
|  |  |  |  |     +- salviavaleriana
|  |  |  |  |     |  `- crafted
|  |  |  |  |     +- strawberry
|  |  |  |  |     |  `- crafted
|  |  |  |  |     +- trippy
|  |  |  |  |     `- ziggara
|  |  |  |  |        `- crafted
|  |  |  |  +- muzzle
|  |  |  |  +- pig
|  |  |  |  |  `- cursed
|  |  |  |  +- rat
|  |  |  |  |  +- bat
|  |  |  |  |  +- bear
|  |  |  |  |  +- bee
|  |  |  |  |  +- fox
|  |  |  |  |  +- jackal
|  |  |  |  |  +- raven
|  |  |  |  |  `- tribal
|  |  |  |  `- rogue
|  |  |  |     +- blindfold
|  |  |  |     |  `- fake
|  |  |  |     +- courtphysician
|  |  |  |     |  `- brassbeak
|  |  |  |     +- duelmask
|  |  |  |     +- eyepatch
|  |  |  |     |  `- left
|  |  |  |     +- facemask
|  |  |  |     |  +- aalloy
|  |  |  |     |  +- bronze
|  |  |  |     |  |  +- anthro
|  |  |  |     |  |  `- classic
|  |  |  |     |  |     `- anthro
|  |  |  |     |  +- carved
|  |  |  |     |  |  +- ambermask
|  |  |  |     |  |  +- coralmask
|  |  |  |     |  |  +- jademask
|  |  |  |     |  |  +- onyxamask
|  |  |  |     |  |  +- opalmask
|  |  |  |     |  |  +- rosemask
|  |  |  |     |  |  +- shellmask
|  |  |  |     |  |  `- turqmask
|  |  |  |     |  +- copper
|  |  |  |     |  +- goldmask
|  |  |  |     |  |  `- triumph
|  |  |  |     |  +- goldmaskc
|  |  |  |     |  |  `- triumph
|  |  |  |     |  +- psydonmask
|  |  |  |     |  +- shadowfacemask
|  |  |  |     |  +- steel
|  |  |  |     |  |  +- confessor
|  |  |  |     |  |  |  `- lensed
|  |  |  |     |  |  +- kazengun
|  |  |  |     |  |  |  `- full
|  |  |  |     |  |  +- paalloy
|  |  |  |     |  |  |  `- mad_touched
|  |  |  |     |  |  `- steppesman
|  |  |  |     |  |     `- anthro
|  |  |  |     |  +- yoruku_kitsune
|  |  |  |     |  `- yoruku_oni
|  |  |  |     +- goblin_mask
|  |  |  |     +- iamcrystalclear
|  |  |  |     +- lordmask
|  |  |  |     |  +- l
|  |  |  |     |  +- naledi
|  |  |  |     |  |  `- sojourner
|  |  |  |     |  +- tarnished
|  |  |  |     |  `- triumph
|  |  |  |     +- physician
|  |  |  |     +- ragmask
|  |  |  |     |  +- black
|  |  |  |     |  `- red
|  |  |  |     +- sack
|  |  |  |     |  `- psy
|  |  |  |     +- shepherd
|  |  |  |     |  `- shadowmask
|  |  |  |     |     `- delf
|  |  |  |     +- silkmask
|  |  |  |     +- skullmask
|  |  |  |     +- spectacles
|  |  |  |     |  +- golden
|  |  |  |     |  `- inq
|  |  |  |     |     `- spawnpair
|  |  |  |     +- wildguard
|  |  |  |     `- xylixmask
|  |  |  |        `- weathered
|  |  |  +- neck
|  |  |  |  +- cloak
|  |  |  |  |  +- cap
|  |  |  |  |  +- ce
|  |  |  |  |  +- cmo
|  |  |  |  |  +- hop
|  |  |  |  |  +- hos
|  |  |  |  |  +- qm
|  |  |  |  |  `- rd
|  |  |  |  +- neckerchief
|  |  |  |  +- necklace
|  |  |  |  |  `- dope
|  |  |  |  +- petcollar
|  |  |  |  +- portalamulet
|  |  |  |  +- roguetown
|  |  |  |  |  +- bevor
|  |  |  |  |  |  +- bronze
|  |  |  |  |  |  +- iron
|  |  |  |  |  |  `- zizo
|  |  |  |  |  +- blkknight
|  |  |  |  |  +- carved
|  |  |  |  |  |  +- amberamulet
|  |  |  |  |  |  +- coralamulet
|  |  |  |  |  |  +- jadeamulet
|  |  |  |  |  |  +- onyxaamulet
|  |  |  |  |  |  +- opalamulet
|  |  |  |  |  |  +- roseamulet
|  |  |  |  |  |  +- shellamulet
|  |  |  |  |  |  `- turqamulet
|  |  |  |  |  +- chaincoif
|  |  |  |  |  |  +- black
|  |  |  |  |  |  +- chainmantle
|  |  |  |  |  |  |  `- matthios
|  |  |  |  |  |  +- full
|  |  |  |  |  |  |  `- black
|  |  |  |  |  |  +- iron
|  |  |  |  |  |  |  `- aalloy
|  |  |  |  |  |  `- paalloy
|  |  |  |  |  +- coif
|  |  |  |  |  |  +- heavypadding
|  |  |  |  |  |  `- padded
|  |  |  |  |  +- collar
|  |  |  |  |  |  +- bell_collar
|  |  |  |  |  |  +- feldcollar
|  |  |  |  |  |  +- forlorn
|  |  |  |  |  |  +- leather
|  |  |  |  |  |  |  `- nomagic
|  |  |  |  |  |  +- prisoner
|  |  |  |  |  |  +- surgcollar
|  |  |  |  |  |  `- woolen
|  |  |  |  |  +- fencerguard
|  |  |  |  |  |  +- generic
|  |  |  |  |  |  `- inq
|  |  |  |  |  +- gorget
|  |  |  |  |  |  +- aalloy
|  |  |  |  |  |  +- bronze
|  |  |  |  |  |  +- copper
|  |  |  |  |  |  +- cursed_collar
|  |  |  |  |  |  +- forlorncollar
|  |  |  |  |  |  +- gold
|  |  |  |  |  |  |  `- king
|  |  |  |  |  |  +- paalloy
|  |  |  |  |  |  |  `- vampire
|  |  |  |  |  |  `- steel
|  |  |  |  |  |     +- gold
|  |  |  |  |  |     +- graggar
|  |  |  |  |  |     `- kazengun
|  |  |  |  |  +- horus
|  |  |  |  |  +- leather
|  |  |  |  |  +- luckcharm
|  |  |  |  |  |  `- mercmedal
|  |  |  |  |  |     +- anthrax
|  |  |  |  |  |     +- atgervi
|  |  |  |  |  |     +- blackoak
|  |  |  |  |  |     +- condottiero
|  |  |  |  |  |     +- desertrider
|  |  |  |  |  |     +- forlorn
|  |  |  |  |  |     +- freifechter
|  |  |  |  |  |     +- grenzelhoft
|  |  |  |  |  |     +- grudgebearer
|  |  |  |  |  |     +- kazengun
|  |  |  |  |  |     +- routier
|  |  |  |  |  |     +- steppesman
|  |  |  |  |  |     +- underdweller
|  |  |  |  |  |     +- vaquero
|  |  |  |  |  |     `- warscholar
|  |  |  |  |  +- ornateamulet
|  |  |  |  |  |  `- noble
|  |  |  |  |  |     `- triumph
|  |  |  |  |  +- psicross
|  |  |  |  |  |  +- aalloy
|  |  |  |  |  |  +- abyssor
|  |  |  |  |  |  |  `- gronn
|  |  |  |  |  |  +- astrata
|  |  |  |  |  |  |  +- bronze
|  |  |  |  |  |  |  +- dasfox
|  |  |  |  |  |  |  `- g
|  |  |  |  |  |  |     `- triumph
|  |  |  |  |  |  +- bpearl
|  |  |  |  |  |  +- bronze
|  |  |  |  |  |  +- dendor
|  |  |  |  |  |  |  `- gronn
|  |  |  |  |  |  +- eora
|  |  |  |  |  |  +- g
|  |  |  |  |  |  |  `- triumph
|  |  |  |  |  |  +- hag
|  |  |  |  |  |  +- inhumen
|  |  |  |  |  |  |  +- aalloy
|  |  |  |  |  |  |  +- baotha
|  |  |  |  |  |  |  +- baothagronn
|  |  |  |  |  |  |  +- bronze
|  |  |  |  |  |  |  +- g
|  |  |  |  |  |  |  |  `- triumph
|  |  |  |  |  |  |  +- graggar
|  |  |  |  |  |  |  |  +- bronze
|  |  |  |  |  |  |  |  `- gronn
|  |  |  |  |  |  |  +- gronn
|  |  |  |  |  |  |  |  `- special
|  |  |  |  |  |  |  +- iron
|  |  |  |  |  |  |  +- matthios
|  |  |  |  |  |  |  |  `- gronn
|  |  |  |  |  |  |  `- paalloy
|  |  |  |  |  |  +- malum
|  |  |  |  |  |  |  +- bronze
|  |  |  |  |  |  |  `- secret
|  |  |  |  |  |  +- naledi
|  |  |  |  |  |  +- necra
|  |  |  |  |  |  +- noc
|  |  |  |  |  |  |  +- aalloy
|  |  |  |  |  |  |  +- bronze
|  |  |  |  |  |  |  `- paalloy
|  |  |  |  |  |  +- paalloy
|  |  |  |  |  |  +- pearl
|  |  |  |  |  |  +- pestra
|  |  |  |  |  |  +- ravox
|  |  |  |  |  |  |  `- bronze
|  |  |  |  |  |  +- reform
|  |  |  |  |  |  +- shell
|  |  |  |  |  |  |  `- bracelet
|  |  |  |  |  |  +- silver
|  |  |  |  |  |  |  +- astrata
|  |  |  |  |  |  |  +- necra
|  |  |  |  |  |  |  +- noc
|  |  |  |  |  |  |  `- undivided
|  |  |  |  |  |  +- undivided
|  |  |  |  |  |  +- weeping
|  |  |  |  |  |  +- wood
|  |  |  |  |  |  `- xylix
|  |  |  |  |  +- shalal
|  |  |  |  |  +- skullamulet
|  |  |  |  |  |  `- gemerald
|  |  |  |  |  `- talkstone
|  |  |  |  +- scarf
|  |  |  |  |  +- black
|  |  |  |  |  +- christmas
|  |  |  |  |  +- cyan
|  |  |  |  |  +- darkblue
|  |  |  |  |  +- green
|  |  |  |  |  +- orange
|  |  |  |  |  +- pink
|  |  |  |  |  +- purple
|  |  |  |  |  +- red
|  |  |  |  |  +- yellow
|  |  |  |  |  `- zebra
|  |  |  |  +- stethoscope
|  |  |  |  +- stripedbluescarf
|  |  |  |  +- stripedgreenscarf
|  |  |  |  +- stripedredscarf
|  |  |  |  `- tie
|  |  |  |     +- black
|  |  |  |     +- blue
|  |  |  |     +- detective
|  |  |  |     +- horrible
|  |  |  |     `- red
|  |  |  +- ring
|  |  |  |  +- aalloy
|  |  |  |  +- active
|  |  |  |  |  +- nomag
|  |  |  |  |  `- shimmeringlens
|  |  |  |  +- amber
|  |  |  |  +- band
|  |  |  |  |  +- aalloy
|  |  |  |  |  +- bronze
|  |  |  |  |  +- gold
|  |  |  |  |  `- paalloy
|  |  |  |  +- blacksteel
|  |  |  |  +- bronze
|  |  |  |  +- coral
|  |  |  |  +- diamond
|  |  |  |  |  `- triumph
|  |  |  |  +- diamondbs
|  |  |  |  +- diamonds
|  |  |  |  +- dragon_ring
|  |  |  |  +- duelist
|  |  |  |  +- emerald
|  |  |  |  +- emeraldbs
|  |  |  |  +- emeralds
|  |  |  |  +- gold
|  |  |  |  |  `- triumph
|  |  |  |  +- griefflower
|  |  |  |  +- jade
|  |  |  |  +- onyxa
|  |  |  |  +- opal
|  |  |  |  +- quartz
|  |  |  |  +- quartzbs
|  |  |  |  +- quartzs
|  |  |  |  +- rose
|  |  |  |  +- ruby
|  |  |  |  +- rubybs
|  |  |  |  +- rubys
|  |  |  |  +- sapphire
|  |  |  |  +- sapphirebs
|  |  |  |  +- sapphires
|  |  |  |  +- shell
|  |  |  |  +- signet
|  |  |  |  |  +- alt
|  |  |  |  |  +- silver
|  |  |  |  |  `- triumph
|  |  |  |  +- silver
|  |  |  |  |  `- cleric
|  |  |  |  +- statamythortz
|  |  |  |  +- statdorpel
|  |  |  |  +- statgemerald
|  |  |  |  +- statonyx
|  |  |  |  +- statrontz
|  |  |  |  +- topaz
|  |  |  |  +- topazbs
|  |  |  |  +- topazs
|  |  |  |  `- turq
|  |  |  +- shoes
|  |  |  |  +- courtphysician
|  |  |  |  |  `- female
|  |  |  |  `- roguetown
|  |  |  |     +- anklets
|  |  |  |     +- armor
|  |  |  |     |  `- rumaclan
|  |  |  |     |     `- shitty
|  |  |  |     +- boots
|  |  |  |     |  +- aalloy
|  |  |  |     |  +- armor
|  |  |  |     |  |  +- blacksteel
|  |  |  |     |  |  |  `- modern
|  |  |  |     |  |  +- blk
|  |  |  |     |  |  +- blkknight
|  |  |  |     |  |  |  `- death
|  |  |  |     |  |  +- bronze
|  |  |  |     |  |  +- dreamwalker
|  |  |  |     |  |  +- dwarven
|  |  |  |     |  |  +- gold
|  |  |  |     |  |  |  `- king
|  |  |  |     |  |  +- graggar
|  |  |  |     |  |  +- holysee
|  |  |  |     |  |  |  `- ritual
|  |  |  |     |  |  +- iron
|  |  |  |     |  |  |  `- gronn
|  |  |  |     |  |  +- matthios
|  |  |  |     |  |  +- vampire
|  |  |  |     |  |  `- zizo
|  |  |  |     |  +- clothlinedanklets
|  |  |  |     |  +- elven_boots
|  |  |  |     |  |  `- autumn
|  |  |  |     |  +- furlinedanklets
|  |  |  |     |  +- furlinedboots
|  |  |  |     |  +- leather
|  |  |  |     |  |  +- atgervi
|  |  |  |     |  |  `- reinforced
|  |  |  |     |  |     +- kazengun
|  |  |  |     |  |     `- short
|  |  |  |     |  +- muffle_matthios
|  |  |  |     |  +- nobleboot
|  |  |  |     |  |  `- steppesman
|  |  |  |     |  +- otavan
|  |  |  |     |  |  `- inqboots
|  |  |  |     |  +- paalloy
|  |  |  |     |  `- psydonboots
|  |  |  |     +- gladiator
|  |  |  |     +- grenzelhoft
|  |  |  |     |  `- freifechter
|  |  |  |     +- horseshoes
|  |  |  |     |  +- gold
|  |  |  |     |  +- silver
|  |  |  |     |  `- steel
|  |  |  |     +- jester
|  |  |  |     +- ridingboots
|  |  |  |     +- sandals
|  |  |  |     |  +- aalloy
|  |  |  |     |  `- paalloy
|  |  |  |     +- shalal
|  |  |  |     +- shortboots
|  |  |  |     `- simpleshoes
|  |  |  |        +- buckle
|  |  |  |        +- lord
|  |  |  |        `- white
|  |  |  +- suit
|  |  |  |  `- roguetown
|  |  |  |     +- armor
|  |  |  |     |  +- armordress
|  |  |  |     |  |  +- alt
|  |  |  |     |  |  `- winterdress
|  |  |  |     |  |     `- monarch
|  |  |  |     |  +- basiceast
|  |  |  |     |  |  +- crafteast
|  |  |  |     |  |  `- mentorsuit
|  |  |  |     |  +- brigandine
|  |  |  |     |  |  +- banneret
|  |  |  |     |  |  +- gronn
|  |  |  |     |  |  +- haraate
|  |  |  |     |  |  +- heavy
|  |  |  |     |  |  `- light
|  |  |  |     |  +- chainmail
|  |  |  |     |  |  +- aalloy
|  |  |  |     |  |  +- bikini
|  |  |  |     |  |  +- hauberk
|  |  |  |     |  |  |  +- aalloy
|  |  |  |     |  |  |  |  `- heavy
|  |  |  |     |  |  |  +- atgervi
|  |  |  |     |  |  |  +- black
|  |  |  |     |  |  |  +- graggar
|  |  |  |     |  |  |  +- heavy
|  |  |  |     |  |  |  +- iron
|  |  |  |     |  |  |  |  `- heavy
|  |  |  |     |  |  |  |     `- zycuirass
|  |  |  |     |  |  |  +- matthios
|  |  |  |     |  |  |  +- ornate
|  |  |  |     |  |  |  +- paalloy
|  |  |  |     |  |  |  |  +- heavy
|  |  |  |     |  |  |  |  `- vampire
|  |  |  |     |  |  |  `- zizo
|  |  |  |     |  |  +- iron
|  |  |  |     |  |  |  `- vampire
|  |  |  |     |  |  +- light
|  |  |  |     |  |  |  `- fencer
|  |  |  |     |  |  `- paalloy
|  |  |  |     |  +- corset
|  |  |  |     |  +- gambeson
|  |  |  |     |  |  +- dark
|  |  |  |     |  |  +- heavy
|  |  |  |     |  |  |  +- black
|  |  |  |     |  |  |  +- chargah
|  |  |  |     |  |  |  +- grenzelhoft
|  |  |  |     |  |  |  +- hand
|  |  |  |     |  |  |  |  +- advisor
|  |  |  |     |  |  |  |  `- spymaster
|  |  |  |     |  |  |  +- hierophant
|  |  |  |     |  |  |  |  `- civilian
|  |  |  |     |  |  |  +- inq
|  |  |  |     |  |  |  +- otavan
|  |  |  |     |  |  |  |  `- inq
|  |  |  |     |  |  |  +- pontifex
|  |  |  |     |  |  |  +- raneshen
|  |  |  |     |  |  |  +- shadowrobe
|  |  |  |     |  |  |  `- strudels
|  |  |  |     |  |  +- light
|  |  |  |     |  |  +- lord
|  |  |  |     |  |  |  `- heavy
|  |  |  |     |  |  |     `- silkjacket
|  |  |  |     |  |  `- shadowrobe
|  |  |  |     |  +- heartfelt
|  |  |  |     |  |  `- hand
|  |  |  |     |  +- leather
|  |  |  |     |  |  +- bikini
|  |  |  |     |  |  +- cuirass
|  |  |  |     |  |  +- goblin
|  |  |  |     |  |  +- heavy
|  |  |  |     |  |  |  +- atgervi
|  |  |  |     |  |  |  +- coat
|  |  |  |     |  |  |  |  +- confessor
|  |  |  |     |  |  |  |  +- gravecoat
|  |  |  |     |  |  |  |  +- raneshen
|  |  |  |     |  |  |  |  +- steppe
|  |  |  |     |  |  |  |  `- trophyfur
|  |  |  |     |  |  |  +- freifechter
|  |  |  |     |  |  |  +- gronn
|  |  |  |     |  |  |  +- jacket
|  |  |  |     |  |  |  |  +- black
|  |  |  |     |  |  |  |  `- courtphysician
|  |  |  |     |  |  |  |     `- female
|  |  |  |     |  |  |  +- shadowvest
|  |  |  |     |  |  |  |  `- drowraider
|  |  |  |     |  |  |  +- shepherd
|  |  |  |     |  |  |  `- tailcoat
|  |  |  |     |  |  +- hide
|  |  |  |     |  |  |  +- bikini
|  |  |  |     |  |  |  `- goblin
|  |  |  |     |  |  +- jacket
|  |  |  |     |  |  |  `- artijacket
|  |  |  |     |  |  +- studded
|  |  |  |     |  |  |  +- bikini
|  |  |  |     |  |  |  +- cuirbouilli
|  |  |  |     |  |  |  +- psyaltrist
|  |  |  |     |  |  |  `- warden
|  |  |  |     |  |  |     `- upgraded
|  |  |  |     |  |  `- vest
|  |  |  |     |  |     +- black
|  |  |  |     |  |     +- hand
|  |  |  |     |  |     +- sailor
|  |  |  |     |  |     |  `- nightman
|  |  |  |     |  |     +- white
|  |  |  |     |  |     `- winterjacket
|  |  |  |     |  +- longcoat
|  |  |  |     |  |  +- brown
|  |  |  |     |  |  `- eiren
|  |  |  |     |  +- manual
|  |  |  |     |  |  +- pushups
|  |  |  |     |  |  |  `- leather
|  |  |  |     |  |  |     `- good
|  |  |  |     |  |  `- sewable
|  |  |  |     |  |     `- confessor
|  |  |  |     |  +- plate
|  |  |  |     |  |  +- aalloy
|  |  |  |     |  |  +- bikini
|  |  |  |     |  |  +- blacksteel
|  |  |  |     |  |  |  `- modern
|  |  |  |     |  |  +- blk
|  |  |  |     |  |  +- blkknight
|  |  |  |     |  |  |  `- death
|  |  |  |     |  |  +- bronze
|  |  |  |     |  |  |  `- light
|  |  |  |     |  |  +- cuirass
|  |  |  |     |  |  |  +- aalloy
|  |  |  |     |  |  |  +- blacksteel
|  |  |  |     |  |  |  +- copper
|  |  |  |     |  |  |  +- fencer
|  |  |  |     |  |  |  |  +- elven
|  |  |  |     |  |  |  |  `- psydon
|  |  |  |     |  |  |  +- fluted
|  |  |  |     |  |  |  |  +- dasfox
|  |  |  |     |  |  |  |  +- gold
|  |  |  |     |  |  |  |  |  +- heroic
|  |  |  |     |  |  |  |  |  `- king
|  |  |  |     |  |  |  |  `- ornate
|  |  |  |     |  |  |  +- iron
|  |  |  |     |  |  |  |  `- goblin
|  |  |  |     |  |  |  +- legacy
|  |  |  |     |  |  |  `- paalloy
|  |  |  |     |  |  +- elven_plate
|  |  |  |     |  |  |  `- autumn
|  |  |  |     |  |  |     `- light
|  |  |  |     |  |  +- fluted
|  |  |  |     |  |  |  +- graggar
|  |  |  |     |  |  |  +- ornate
|  |  |  |     |  |  |  `- shadowplate
|  |  |  |     |  |  +- full
|  |  |  |     |  |  |  +- bikini
|  |  |  |     |  |  |  +- blacksteel
|  |  |  |     |  |  |  |  `- modern
|  |  |  |     |  |  |  +- bronze
|  |  |  |     |  |  |  |  `- alt
|  |  |  |     |  |  |  +- dreamwalker
|  |  |  |     |  |  |  +- dwarven
|  |  |  |     |  |  |  |  `- smith
|  |  |  |     |  |  |  +- fluted
|  |  |  |     |  |  |  |  +- legacy
|  |  |  |     |  |  |  |  `- ornate
|  |  |  |     |  |  |  |     `- ordinator
|  |  |  |     |  |  |  +- holysee
|  |  |  |     |  |  |  |  `- ritual
|  |  |  |     |  |  |  +- iron
|  |  |  |     |  |  |  +- legacy
|  |  |  |     |  |  |  +- matthios
|  |  |  |     |  |  |  +- samsibsa
|  |  |  |     |  |  |  `- zizo
|  |  |  |     |  |  +- iron
|  |  |  |     |  |  |  `- gronn
|  |  |  |     |  |  +- legacy
|  |  |  |     |  |  +- otavan
|  |  |  |     |  |  +- paalloy
|  |  |  |     |  |  |  `- artificer
|  |  |  |     |  |  +- scale
|  |  |  |     |  |  |  +- inqcoat
|  |  |  |     |  |  |  |  `- armored
|  |  |  |     |  |  |  +- marshal
|  |  |  |     |  |  |  `- steppe
|  |  |  |     |  |  +- silver
|  |  |  |     |  |  `- vampire
|  |  |  |     |  +- regenerating
|  |  |  |     |  |  +- skin
|  |  |  |     |  |  |  +- arcyne_ward
|  |  |  |     |  |  |  |  +- bestowed
|  |  |  |     |  |  |  |  +- crystalhide
|  |  |  |     |  |  |  |  `- dragonhide
|  |  |  |     |  |  |  +- disciple
|  |  |  |     |  |  |  |  +- bailiff
|  |  |  |     |  |  |  |  +- barbarian
|  |  |  |     |  |  |  |  +- berserker
|  |  |  |     |  |  |  |  +- gladiator
|  |  |  |     |  |  |  |  `- lirvas
|  |  |  |     |  |  |  +- easttats
|  |  |  |     |  |  |  +- gnoll_armor
|  |  |  |     |  |  |  |  +- impure
|  |  |  |     |  |  |  |  +- knight
|  |  |  |     |  |  |  |  +- shaman
|  |  |  |     |  |  |  |  `- templar
|  |  |  |     |  |  |  +- iconoclast
|  |  |  |     |  |  |  `- werewolf_skin
|  |  |  |     |  |  `- slayer
|  |  |  |     |  +- silkcoat
|  |  |  |     |  +- skin_armor
|  |  |  |     |  |  +- bear_skin
|  |  |  |     |  |  +- cabbit_skin
|  |  |  |     |  |  +- cat_skin
|  |  |  |     |  |  +- fox_skin
|  |  |  |     |  |  +- hag_skin
|  |  |  |     |  |  +- moss_skin
|  |  |  |     |  |  +- saiga_skin
|  |  |  |     |  |  +- spider_chitin
|  |  |  |     |  |  +- spider_skin
|  |  |  |     |  |  +- wolf_skin
|  |  |  |     |  |  `- zizoconstructarmor
|  |  |  |     |  +- vestments_padded
|  |  |  |     |  `- workervest
|  |  |  |     `- shirt
|  |  |  |        +- apothshirt
|  |  |  |        +- courtphysician
|  |  |  |        |  `- female
|  |  |  |        +- desertbra
|  |  |  |        +- dress
|  |  |  |        |  +- captainrobe
|  |  |  |        |  +- emerald
|  |  |  |        |  +- funkydress
|  |  |  |        |  +- gen
|  |  |  |        |  |  +- black
|  |  |  |        |  |  +- blue
|  |  |  |        |  |  +- purple
|  |  |  |        |  |  +- sexy
|  |  |  |        |  |  `- strapless
|  |  |  |        |  |     +- alt
|  |  |  |        |  |     +- black
|  |  |  |        |  |     +- blue
|  |  |  |        |  |     +- purple
|  |  |  |        |  |     `- red
|  |  |  |        |  +- gown
|  |  |  |        |  |  +- fallgown
|  |  |  |        |  |  +- summergown
|  |  |  |        |  |  `- wintergown
|  |  |  |        |  +- maid
|  |  |  |        |  +- maidfancy
|  |  |  |        |  +- maidservant
|  |  |  |        |  +- royal
|  |  |  |        |  |  +- hand_f
|  |  |  |        |  |  +- hand_m
|  |  |  |        |  |  +- prince
|  |  |  |        |  |  `- princess
|  |  |  |        |  +- silkdress
|  |  |  |        |  |  +- black
|  |  |  |        |  |  +- green
|  |  |  |        |  |  +- loudmouth
|  |  |  |        |  |  +- princess
|  |  |  |        |  |  +- steward
|  |  |  |        |  |  `- weddingdress
|  |  |  |        |  +- silkydress
|  |  |  |        |  `- slit
|  |  |  |        +- explorer
|  |  |  |        +- fancyjacket
|  |  |  |        +- formal
|  |  |  |        +- freifechter
|  |  |  |        |  `- shepherd
|  |  |  |        +- jester
|  |  |  |        +- maesune
|  |  |  |        +- rags
|  |  |  |        +- robe
|  |  |  |        |  +- abyssor
|  |  |  |        |  +- archivist
|  |  |  |        |  +- astrata
|  |  |  |        |  +- bared
|  |  |  |        |  +- black
|  |  |  |        |  +- courtmage
|  |  |  |        |  +- dendor
|  |  |  |        |  +- eora
|  |  |  |        |  |  `- alt
|  |  |  |        |  +- feld
|  |  |  |        |  +- hag
|  |  |  |        |  +- hierophant
|  |  |  |        |  +- mageblue
|  |  |  |        |  +- magegreen
|  |  |  |        |  +- mageorange
|  |  |  |        |  +- magered
|  |  |  |        |  +- mageyellow
|  |  |  |        |  +- merchant
|  |  |  |        |  +- monk
|  |  |  |        |  |  `- holy
|  |  |  |        |  +- necra
|  |  |  |        |  +- necromancer
|  |  |  |        |  +- noc
|  |  |  |        |  +- nun
|  |  |  |        |  +- phys
|  |  |  |        |  +- physician
|  |  |  |        |  +- pointfex
|  |  |  |        |  +- priest
|  |  |  |        |  +- ravox
|  |  |  |        |  +- sofiavest
|  |  |  |        |  +- spellcasterrobe
|  |  |  |        |  +- tabardblack
|  |  |  |        |  +- tabardscarlet
|  |  |  |        |  +- tabardwhite
|  |  |  |        |  |  `- evil_ah_ah
|  |  |  |        |  +- undivided
|  |  |  |        |  +- unholy
|  |  |  |        |  |  +- enchanted
|  |  |  |        |  |  `- lich
|  |  |  |        |  +- white
|  |  |  |        |  `- wizard
|  |  |  |        +- shadowshirt
|  |  |  |        |  `- elflock
|  |  |  |        |     `- drowraider
|  |  |  |        +- shortshirt
|  |  |  |        |  +- bog
|  |  |  |        |  `- merc
|  |  |  |        +- silkbra
|  |  |  |        +- tribalrag
|  |  |  |        |  `- gladiator
|  |  |  |        +- tunic
|  |  |  |        |  +- black
|  |  |  |        |  +- blue
|  |  |  |        |  +- green
|  |  |  |        |  +- noblecoat
|  |  |  |        |  +- purple
|  |  |  |        |  +- red
|  |  |  |        |  +- silktunic
|  |  |  |        |  +- ucolored
|  |  |  |        |  `- white
|  |  |  |        +- undershirt
|  |  |  |        |  +- artificer
|  |  |  |        |  +- black
|  |  |  |        |  +- brown
|  |  |  |        |  +- eastshirt1
|  |  |  |        |  +- eastshirt2
|  |  |  |        |  +- formal
|  |  |  |        |  +- green
|  |  |  |        |  +- guard
|  |  |  |        |  +- guardsecond
|  |  |  |        |  +- lord
|  |  |  |        |  +- lowcut
|  |  |  |        |  +- priest
|  |  |  |        |  +- puritan
|  |  |  |        |  +- purple
|  |  |  |        |  +- red
|  |  |  |        |  +- sailor
|  |  |  |        |  |  `- red
|  |  |  |        |  +- scarlet
|  |  |  |        |  +- vagrant
|  |  |  |        |  |  `- l
|  |  |  |        |  `- webs
|  |  |  |        `- vampire
|  |  |  +- under
|  |  |  |  +- rank
|  |  |  |  `- roguetown
|  |  |  |     +- brayette
|  |  |  |     +- brigandinelegs
|  |  |  |     +- chainlegs
|  |  |  |     |  +- banneret
|  |  |  |     |  +- black
|  |  |  |     |  +- blk
|  |  |  |     |  +- gronn
|  |  |  |     |  +- iron
|  |  |  |     |  |  `- kilt
|  |  |  |     |  +- kilt
|  |  |  |     |  |  +- aalloy
|  |  |  |     |  |  +- gold
|  |  |  |     |  |  `- paalloy
|  |  |  |     |  `- skirt
|  |  |  |     +- heavy_leather_pants
|  |  |  |     |  +- bronzeskirt
|  |  |  |     |  +- eastpants1
|  |  |  |     |  +- eastpants2
|  |  |  |     |  +- grenzelpants
|  |  |  |     |  +- kazengun
|  |  |  |     |  |  `- black
|  |  |  |     |  +- otavan
|  |  |  |     |  |  +- generic
|  |  |  |     |  |  `- shepherd
|  |  |  |     |  +- shadowpants
|  |  |  |     |  |  `- drowraider
|  |  |  |     |  `- shorts
|  |  |  |     +- loincloth
|  |  |  |     |  +- brown
|  |  |  |     |  +- deprived
|  |  |  |     |  `- pink
|  |  |  |     +- platelegs
|  |  |  |     |  +- aalloy
|  |  |  |     |  +- blacksteel
|  |  |  |     |  |  `- modern
|  |  |  |     |  +- blkknight
|  |  |  |     |  |  `- death
|  |  |  |     |  +- dreamwalker
|  |  |  |     |  +- graggar
|  |  |  |     |  +- holysee
|  |  |  |     |  |  `- ritual
|  |  |  |     |  +- iron
|  |  |  |     |  |  `- gronn
|  |  |  |     |  +- matthios
|  |  |  |     |  +- paalloy
|  |  |  |     |  +- skirt
|  |  |  |     |  +- vampire
|  |  |  |     |  `- zizo
|  |  |  |     +- skirt
|  |  |  |     |  +- black
|  |  |  |     |  +- blue
|  |  |  |     |  +- brown
|  |  |  |     |  +- courtphysician
|  |  |  |     |  +- desert
|  |  |  |     |  +- green
|  |  |  |     |  +- random
|  |  |  |     |  `- red
|  |  |  |     +- splintlegs
|  |  |  |     +- tights
|  |  |  |     |  +- black
|  |  |  |     |  +- explorerpants
|  |  |  |     |  +- formal
|  |  |  |     |  +- formalfancy
|  |  |  |     |  +- green
|  |  |  |     |  +- jester
|  |  |  |     |  +- lord
|  |  |  |     |  +- puritan
|  |  |  |     |  +- purple
|  |  |  |     |  +- red
|  |  |  |     |  +- sailor
|  |  |  |     |  +- shorts
|  |  |  |     |  `- vagrant
|  |  |  |     |     `- l
|  |  |  |     +- trou
|  |  |  |     |  +- apothecary
|  |  |  |     |  +- artipants
|  |  |  |     |  +- beltpants
|  |  |  |     |  +- leather
|  |  |  |     |  |  +- atgervi
|  |  |  |     |  |  +- courtphysician
|  |  |  |     |  |  +- eastern
|  |  |  |     |  |  +- gronn
|  |  |  |     |  |  +- mourning
|  |  |  |     |  |  `- pontifex
|  |  |  |     |  |     `- raneshen
|  |  |  |     |  +- leathertights
|  |  |  |     |  `- shadowpants
|  |  |  |     `- webs
|  |  |  +- wall_grab
|  |  |  `- wrists
|  |  |     `- roguetown
|  |  |        +- allwrappings
|  |  |        |  `- scarlet
|  |  |        +- bracers
|  |  |        |  +- aalloy
|  |  |        |  +- black
|  |  |        |  +- brigandine
|  |  |        |  |  `- black
|  |  |        |  +- bronze
|  |  |        |  +- cloth
|  |  |        |  |  +- gladiator
|  |  |        |  |  +- monk
|  |  |        |  |  `- naledi
|  |  |        |  +- copper
|  |  |        |  +- gold
|  |  |        |  |  `- king
|  |  |        |  +- graggar
|  |  |        |  +- hand
|  |  |        |  +- iron
|  |  |        |  +- jackchain
|  |  |        |  +- leather
|  |  |        |  |  `- heavy
|  |  |        |  +- lirvas
|  |  |        |  +- matthios
|  |  |        |  +- paalloy
|  |  |        |  |  `- vampire
|  |  |        |  +- psythorns
|  |  |        |  +- splint
|  |  |        |  `- zizo
|  |  |        +- gem
|  |  |        |  +- amberbracelet
|  |  |        |  +- coralbracelet
|  |  |        |  +- jadebracelet
|  |  |        |  +- onyxabracelet
|  |  |        |  +- opalbracelet
|  |  |        |  +- rosebracelet
|  |  |        |  +- shellbracelet
|  |  |        |  `- turqbracelet
|  |  |        +- nocwrappings
|  |  |        +- royalsleeves
|  |  |        `- wrappings
|  |  +- codespeak_manual
|  |  |  `- unlimited
|  |  +- compost
|  |  +- construction
|  |  |  +- bundle
|  |  |  |  `- nail
|  |  |  +- nail
|  |  |  `- repairkit
|  |  |     `- structure
|  |  +- contraption
|  |  |  +- bronzeprosthetic
|  |  |  +- folding_table_stored
|  |  |  +- goldprosthetic
|  |  |  +- ironprosthetic
|  |  |  +- linker
|  |  |  |  `- master
|  |  |  +- lock_imprinter
|  |  |  +- pick
|  |  |  |  `- drill
|  |  |  +- shears
|  |  |  +- steelprosthetic
|  |  |  `- wood_metalizer
|  |  +- cooking
|  |  |  +- pan
|  |  |  |  +- aalloy
|  |  |  |  `- bronze
|  |  |  +- platter
|  |  |  |  +- aalloy
|  |  |  |  +- bronze
|  |  |  |  +- carved
|  |  |  |  |  +- amber
|  |  |  |  |  +- coral
|  |  |  |  |  +- jade
|  |  |  |  |  +- onyxa
|  |  |  |  |  +- opal
|  |  |  |  |  +- rose
|  |  |  |  |  +- shell
|  |  |  |  |  `- turq
|  |  |  |  +- copper
|  |  |  |  +- gold
|  |  |  |  +- pewter
|  |  |  |  `- silver
|  |  |  `- skewer
|  |  +- coveter
|  |  +- cross_construction_kit
|  |  +- customblank
|  |  +- customlock
|  |  |  `- finished
|  |  +- debug
|  |  |  `- human_spawner
|  |  +- detective_scanner
|  |  +- dice
|  |  |  +- d00
|  |  |  +- d1
|  |  |  +- d10
|  |  |  +- d100
|  |  |  +- d12
|  |  |  +- d2
|  |  |  +- d20
|  |  |  +- d4
|  |  |  +- d6
|  |  |  |  +- ebony
|  |  |  |  `- space
|  |  |  +- d8
|  |  |  +- eightbd20
|  |  |  +- fourdd6
|  |  |  `- fudge
|  |  +- dildo
|  |  |  +- gold
|  |  |  +- iron
|  |  |  +- silver
|  |  |  +- steel
|  |  |  `- wood
|  |  +- dmusicbox
|  |  +- dye_brush
|  |  +- enchantingkit
|  |  |  +- aisuwand
|  |  |  +- bat
|  |  |  +- bigfoot
|  |  |  +- bigfoot_axe
|  |  |  +- dakken_alloybsword
|  |  |  +- dakken_zizhelm
|  |  |  +- dasfox_cuirass
|  |  |  +- dasfox_helm
|  |  |  +- dasfox_lance
|  |  |  +- drd_lsword
|  |  |  +- eiren_helmet
|  |  |  +- eirensabre2
|  |  |  +- koruu_glaive
|  |  |  +- lmwevil_brassbeak
|  |  |  +- plexiant
|  |  |  +- rebel
|  |  |  +- ryan_psyhelm
|  |  |  +- ryebread
|  |  |  +- sci_flame
|  |  |  +- sci_sand
|  |  |  +- shudderfly_dagger
|  |  |  +- srusu
|  |  |  +- stinketh_pike
|  |  |  +- stinketh_shashka
|  |  |  +- strudel1
|  |  |  +- strudel2
|  |  |  +- strudel3
|  |  |  +- strudel4
|  |  |  +- triumph_armorkit
|  |  |  +- triumph_armorkit_drow
|  |  |  +- triumph_weaponkit_axe
|  |  |  +- triumph_weaponkit_axedouble
|  |  |  +- triumph_weaponkit_estoc
|  |  |  +- triumph_weaponkit_fancymace
|  |  |  +- triumph_weaponkit_kris
|  |  |  +- triumph_weaponkit_njora
|  |  |  +- triumph_weaponkit_psy
|  |  |  +- triumph_weaponkit_sabre
|  |  |  +- triumph_weaponkit_tri
|  |  |  +- triumph_weaponkit_whip
|  |  |  +- triumph_weaponkit_wide
|  |  |  +- weapon
|  |  |  |  +- aeternum
|  |  |  |  +- drd_shield
|  |  |  |  +- eiren
|  |  |  |  +- eiren_m
|  |  |  |  +- eirensabre
|  |  |  |  +- eirensword
|  |  |  |  +- inverserun
|  |  |  |  +- koruu_kukri
|  |  |  |  |  `- warden
|  |  |  |  +- maesune_sabre
|  |  |  |  +- maesune_shield
|  |  |  |  +- noire_flsword
|  |  |  |  +- regnum
|  |  |  |  +- triumph_weaponkit_ada
|  |  |  |  +- triumph_weaponkit_dadao
|  |  |  |  +- triumph_weaponkit_gdadao
|  |  |  |  +- triumph_weaponkit_greatval
|  |  |  |  +- triumph_weaponkit_hwi
|  |  |  |  +- triumph_weaponkit_ida
|  |  |  |  +- triumph_weaponkit_kaskara
|  |  |  |  +- triumph_weaponkit_ngombe
|  |  |  |  +- triumph_weaponkit_rock
|  |  |  |  +- triumph_weaponkit_sengese
|  |  |  |  +- triumph_weaponkit_sword
|  |  |  |  +- triumph_weaponkit_wodao
|  |  |  |  `- waff
|  |  |  +- zoe
|  |  |  +- zoe_shovel
|  |  |  +- zydrasgreataxe
|  |  |  `- zydrashauberk
|  |  +- enchantmentscroll
|  |  |  +- archery
|  |  |  +- briars
|  |  |  +- chaos_storm
|  |  |  +- climbing
|  |  |  +- featherstep
|  |  |  +- fireresist
|  |  |  +- freeze
|  |  |  +- frostveil
|  |  |  +- holding
|  |  |  +- infernalflame
|  |  |  +- lifesteal
|  |  |  +- lightning
|  |  |  +- magnifiedlight
|  |  |  +- mining
|  |  |  +- nightvision
|  |  |  +- phoenixguard
|  |  |  +- returningweapon
|  |  |  +- revealinglight
|  |  |  +- rewind
|  |  |  +- smithing
|  |  |  +- thievery
|  |  |  +- unbreaking
|  |  |  +- voidtouched
|  |  |  +- woodcut
|  |  |  +- woundclosing
|  |  |  `- xylix
|  |  +- etherealballdeployer
|  |  +- fertilizer
|  |  +- fishingcage
|  |  +- fishingrod
|  |  |  +- aalloy
|  |  |  +- bronze
|  |  |  `- crafted
|  |  +- flashlight
|  |  |  +- flare
|  |  |  |  +- light
|  |  |  |  `- torch
|  |  |  |     +- lantern
|  |  |  |     |  +- bronze
|  |  |  |     |  +- bronzelamptern
|  |  |  |     |  |  `- malums_lamptern
|  |  |  |     |  +- copper
|  |  |  |     |  +- psycenser
|  |  |  |     |  +- pumpkin
|  |  |  |     |  |  +- frown
|  |  |  |     |  |  +- grin
|  |  |  |     |  |  +- psy
|  |  |  |     |  |  +- surprise
|  |  |  |     |  |  +- ten
|  |  |  |     |  |  +- woozy
|  |  |  |     |  |  `- zizo
|  |  |  |     |  `- voidlamptern
|  |  |  |     `- metal
|  |  |  `- lantern
|  |  |     `- shrunken
|  |  +- flesh_decoy
|  |  +- flesh_node
|  |  +- flint
|  |  +- flowercrown
|  |  |  +- briar
|  |  |  +- calendula
|  |  |  +- manabloom
|  |  |  +- matricaria
|  |  |  +- rosa
|  |  |  `- salvia
|  |  +- folding_alchcauldron_stored
|  |  +- folding_alchstation_stored
|  |  +- folding_table_stored
|  |  +- fruit_of_eora
|  |  +- gavelblock
|  |  +- gavelhammer
|  |  +- gem_device
|  |  |  `- goldface
|  |  +- glow_petal
|  |  +- grabbing
|  |  |  `- bite
|  |  +- grapplinghook
|  |  +- grown
|  |  |  `- log
|  |  |     `- tree
|  |  |        +- bowpartial
|  |  |        |  +- longbow
|  |  |        |  `- recurve
|  |  |        +- small
|  |  |        +- stake
|  |  |        `- stick
|  |  +- gun
|  |  |  `- ballistic
|  |  |     `- revolver
|  |  |        +- grenadelauncher
|  |  |        |  +- bow
|  |  |        |  |  +- classic
|  |  |        |  |  +- longbow
|  |  |        |  |  |  `- warden
|  |  |        |  |  +- recurve
|  |  |        |  |  |  +- autumn
|  |  |        |  |  |  +- blackoak
|  |  |        |  |  |  +- steppesman
|  |  |        |  |  |  `- warden
|  |  |        |  |  `- short
|  |  |        |  +- crossbow
|  |  |        |  |  +- aalloy
|  |  |        |  |  +- heavy
|  |  |        |  |  |  `- paalloy
|  |  |        |  |  `- slurbow
|  |  |        |  `- sling
|  |  |        `- last_resort
|  |  +- hag_blessing_item
|  |  +- hag_catalyst
|  |  |  +- synth_base
|  |  |  |  `- gilded
|  |  |  `- varnish_base
|  |  +- hag_test_item
|  |  +- hair_dye_cream
|  |  +- handheld_bell
|  |  +- handmirror
|  |  +- heart_blood_canister
|  |  |  `- filled
|  |  +- heart_blood_vial
|  |  |  `- filled
|  |  +- heart_canister
|  |  +- herbseed
|  |  |  +- artemisia
|  |  |  +- atropa
|  |  |  +- benedictus
|  |  |  +- calendula
|  |  |  +- euphrasia
|  |  |  +- hypericum
|  |  |  +- manabloom
|  |  |  +- matricaria
|  |  |  +- mentha
|  |  |  +- paris
|  |  |  +- rosa
|  |  |  +- salvia
|  |  |  +- symphitum
|  |  |  +- taraxacum
|  |  |  +- urtica
|  |  |  `- valeriana
|  |  +- hookah_mouthpiece
|  |  +- hot_potato
|  |  |  +- harmless
|  |  |  |  `- toy
|  |  |  `- syndicate
|  |  +- hourglass
|  |  |  +- admin
|  |  |  `- temporal
|  |  +- impact_grenade
|  |  |  +- explosion
|  |  |  `- smoke
|  |  |     +- blind_gas
|  |  |     +- fire_gas
|  |  |     +- healing_gas
|  |  |     +- mute_gas
|  |  |     `- poison_gas
|  |  +- ingot
|  |  |  +- aalloy
|  |  |  +- aaslag
|  |  |  +- blacksteel
|  |  |  +- bronze
|  |  |  +- component
|  |  |  |  +- berserkswordblade
|  |  |  |  +- berserkswordgrip
|  |  |  |  +- glutcrystal
|  |  |  |  `- heapofrawiron
|  |  |  +- copper
|  |  |  +- draconic
|  |  |  +- drow
|  |  |  +- gold
|  |  |  +- iron
|  |  |  +- ketryl
|  |  |  +- lithmyc
|  |  |  +- purifiedaalloy
|  |  |  +- silver
|  |  |  +- silverblessed
|  |  |  |  `- bullion
|  |  |  +- steel
|  |  |  +- sylveric
|  |  |  +- tin
|  |  |  `- weeping
|  |  +- inhand_tester
|  |  |  `- big
|  |  +- inqarticles
|  |  |  +- bmirror
|  |  |  +- garrote
|  |  |  +- indexer
|  |  |  +- spyglass
|  |  |  `- tallowpot
|  |  +- jingle_bells
|  |  +- key
|  |  |  +- displaycase
|  |  |  +- janitor
|  |  |  `- security
|  |  +- kitchen
|  |  |  +- fork
|  |  |  |  +- aalloy
|  |  |  |  +- bronze
|  |  |  |  +- carved
|  |  |  |  |  +- amber
|  |  |  |  |  +- coral
|  |  |  |  |  +- jade
|  |  |  |  |  +- onyxa
|  |  |  |  |  +- opal
|  |  |  |  |  +- rose
|  |  |  |  |  +- shell
|  |  |  |  |  `- turq
|  |  |  |  +- gold
|  |  |  |  +- iron
|  |  |  |  +- silver
|  |  |  |  `- tin
|  |  |  +- rollingpin
|  |  |  `- spoon
|  |  |     +- aalloy
|  |  |     +- bronze
|  |  |     +- carved
|  |  |     |  +- amber
|  |  |     |  +- coral
|  |  |     |  +- jade
|  |  |     |  +- onyxa
|  |  |     |  +- opal
|  |  |     |  +- rose
|  |  |     |  +- shell
|  |  |     |  `- turq
|  |  |     +- gold
|  |  |     +- iron
|  |  |     +- plastic
|  |  |     +- silver
|  |  |     `- tin
|  |  +- lantern
|  |  |  `- fog_repelling
|  |  |     `- empty
|  |  +- leechtick
|  |  +- leechtick_bloated
|  |  +- legwears
|  |  |  +- black
|  |  |  +- blue
|  |  |  +- fishnet
|  |  |  |  +- black
|  |  |  |  +- blue
|  |  |  |  +- purple
|  |  |  |  +- red
|  |  |  |  `- white
|  |  |  +- knee_high
|  |  |  |  `- white
|  |  |  +- knee_high_silk
|  |  |  |  `- white
|  |  |  +- purple
|  |  |  +- red
|  |  |  +- silk
|  |  |  |  +- black
|  |  |  |  +- blue
|  |  |  |  +- purple
|  |  |  |  +- red
|  |  |  |  `- white
|  |  |  +- thigh_high
|  |  |  |  `- white
|  |  |  +- thigh_high_silk
|  |  |  |  `- white
|  |  |  `- white
|  |  +- lighter
|  |  |  `- greyscale
|  |  +- lipstick
|  |  |  +- black
|  |  |  +- jade
|  |  |  `- purple
|  |  +- listeningdevice
|  |  +- listenstone
|  |  +- lockpick
|  |  |  `- goldpin
|  |  |     `- silver
|  |  +- lockpickring
|  |  |  +- mundane
|  |  |  `- one
|  |  +- magic
|  |  |  +- artifact
|  |  |  +- elemental
|  |  |  |  +- fragment
|  |  |  |  +- mote
|  |  |  |  +- relic
|  |  |  |  `- shard
|  |  |  +- fae
|  |  |  |  +- fairydust
|  |  |  |  +- heartwoodcore
|  |  |  |  +- iridescentscale
|  |  |  |  `- sylvanessence
|  |  |  +- infernal
|  |  |  |  +- ash
|  |  |  |  +- core
|  |  |  |  +- fang
|  |  |  |  `- flame
|  |  |  +- leyline
|  |  |  +- manacrystal
|  |  |  +- melded
|  |  |  |  +- t1
|  |  |  |  +- t2
|  |  |  |  +- t3
|  |  |  |  +- t4
|  |  |  |  `- t5
|  |  |  +- obsidian
|  |  |  `- voidstone
|  |  +- magnifying_glass
|  |  +- maneaterseed
|  |  +- manuscript
|  |  +- match
|  |  |  `- firebrand
|  |  +- mattcoin
|  |  +- melee
|  |  |  +- new_touch_attack
|  |  |  |  +- prestidigitation
|  |  |  |  `- rune_ward
|  |  |  +- touch_attack
|  |  |  |  +- lesserknock
|  |  |  |  +- loversruin
|  |  |  |  +- orison
|  |  |  |  +- parlor_trick
|  |  |  |  +- quietus
|  |  |  |  `- rogueweapon
|  |  |  |     +- astratagrasp
|  |  |  |     +- bladeofpsydon
|  |  |  |     +- nocgrasp
|  |  |  |     `- ravoxgrasp
|  |  |  `- transforming
|  |  +- merctoken
|  |  +- millstone
|  |  +- mimictrinket
|  |  +- mini_flagpole
|  |  |  +- apothecary
|  |  |  +- artificer
|  |  |  +- bathhouse
|  |  |  +- blacksmith
|  |  |  +- church
|  |  |  +- duke
|  |  |  +- fisher
|  |  |  +- freeform2
|  |  |  +- innkeeper
|  |  |  +- merchant
|  |  |  +- steward
|  |  |  +- tailor
|  |  |  `- university
|  |  +- mobilestove
|  |  +- multitool
|  |  |  `- field_debug
|  |  +- mundane
|  |  |  `- puzzlebox
|  |  |     +- easy
|  |  |     +- impossible
|  |  |     `- medium
|  |  +- natural
|  |  |  +- bone
|  |  |  +- bowstring
|  |  |  +- brick
|  |  |  +- bundle
|  |  |  |  +- bone
|  |  |  |  |  `- full
|  |  |  |  +- brick
|  |  |  |  +- cloth
|  |  |  |  |  `- bandage
|  |  |  |  |     `- full
|  |  |  |  +- curred_hide
|  |  |  |  +- fibers
|  |  |  |  |  `- full
|  |  |  |  +- glass
|  |  |  |  +- plank
|  |  |  |  +- silk
|  |  |  |  +- stick
|  |  |  |  |  `- full
|  |  |  |  +- stoneblock
|  |  |  |  `- worms
|  |  |  +- chaff
|  |  |  |  +- oat
|  |  |  |  +- rice
|  |  |  |  `- wheat
|  |  |  +- clay
|  |  |  |  +- claybottle
|  |  |  |  +- claybottleclassic
|  |  |  |  +- claybrick
|  |  |  |  +- claycup
|  |  |  |  +- claycupclassic
|  |  |  |  +- clayfancyvase
|  |  |  |  +- clayfancyvaseclassic
|  |  |  |  +- claystatue
|  |  |  |  +- clayvase
|  |  |  |  +- clayvaseclassic
|  |  |  |  +- glassbatch
|  |  |  |  +- rawteacup
|  |  |  |  `- rawteapot
|  |  |  +- cloth
|  |  |  |  `- bandage
|  |  |  +- cured
|  |  |  |  `- essence
|  |  |  +- dirtclod
|  |  |  |  `- snow
|  |  |  +- feather
|  |  |  |  `- infernal
|  |  |  +- fibers
|  |  |  +- fur
|  |  |  |  +- bobcat
|  |  |  |  +- direbear
|  |  |  |  +- fox
|  |  |  |  +- goat
|  |  |  |  +- mole
|  |  |  |  +- rabbit
|  |  |  |  +- raccoon
|  |  |  |  +- rat
|  |  |  |  `- wolf
|  |  |  +- glass
|  |  |  +- glass_shard
|  |  |  +- head
|  |  |  |  +- direbear
|  |  |  |  +- dragon
|  |  |  |  |  `- broodmother
|  |  |  |  +- fox
|  |  |  |  +- goat
|  |  |  |  +- honeyspider
|  |  |  |  +- minotaur
|  |  |  |  +- mirelurker
|  |  |  |  +- mirespider
|  |  |  |  +- mirespider_paralytic
|  |  |  |  +- mole
|  |  |  |  +- rous
|  |  |  |  +- saiga
|  |  |  |  +- troll
|  |  |  |  |  +- axe
|  |  |  |  |  `- cave
|  |  |  |  `- volf
|  |  |  +- hide
|  |  |  |  `- cured
|  |  |  +- poo
|  |  |  |  +- cow
|  |  |  |  `- horse
|  |  |  +- rabbitsfoot
|  |  |  +- rock
|  |  |  |  +- cinnabar
|  |  |  |  +- coal
|  |  |  |  +- copper
|  |  |  |  +- dungeon
|  |  |  |  +- elementalmote
|  |  |  |  +- gem
|  |  |  |  +- gold
|  |  |  |  +- iron
|  |  |  |  +- random_ore
|  |  |  |  +- salt
|  |  |  |  +- silver
|  |  |  |  `- tin
|  |  |  +- saddle
|  |  |  +- shellplant
|  |  |  |  `- pumpkin
|  |  |  +- silk
|  |  |  +- stone
|  |  |  |  `- sending
|  |  |  +- stoneblock
|  |  |  +- thorn
|  |  |  +- whetstone
|  |  |  +- wood
|  |  |  |  `- plank
|  |  |  `- worms
|  |  |     +- grubs
|  |  |     `- leech
|  |  |        +- abyssoid
|  |  |        `- cheele
|  |  +- necro_relics
|  |  |  `- necro_crystal
|  |  +- needle
|  |  |  +- aalloy
|  |  |  +- bronze
|  |  |  +- pestra
|  |  |  `- thorn
|  |  |     `- cleric
|  |  +- net
|  |  +- organ
|  |  |  +- adamantine_resonator
|  |  |  +- antennas
|  |  |  |  +- ipc
|  |  |  |  +- moth
|  |  |  |  `- synth
|  |  |  +- appendix
|  |  |  +- back_feature
|  |  |  +- brain
|  |  |  |  +- alien
|  |  |  |  +- construct
|  |  |  |  `- dullahan
|  |  |  +- breasts
|  |  |  +- dullahan_vision
|  |  |  +- ears
|  |  |  |  +- akula
|  |  |  |  +- anthro
|  |  |  |  +- bronze
|  |  |  |  +- cat
|  |  |  |  +- cybernetic
|  |  |  |  |  `- upgraded
|  |  |  |  +- elf
|  |  |  |  +- elfw
|  |  |  |  +- goblin
|  |  |  |  +- halforc
|  |  |  |  +- invincible
|  |  |  |  +- lupian
|  |  |  |  +- penguin
|  |  |  |  +- psy_vault_guard
|  |  |  |  +- tajaran
|  |  |  |  +- tiefling
|  |  |  |  `- vulpkanin
|  |  |  +- eyes
|  |  |  |  +- construct
|  |  |  |  +- elf
|  |  |  |  +- goblin
|  |  |  |  +- halfelf
|  |  |  |  +- moth
|  |  |  |  +- night_vision
|  |  |  |  |  +- alien
|  |  |  |  |  +- argonian
|  |  |  |  |  +- mushroom
|  |  |  |  |  +- nightmare
|  |  |  |  |  +- werewolf
|  |  |  |  |  +- wild_goblin
|  |  |  |  |  `- zombie
|  |  |  |  +- robotic
|  |  |  |  |  +- flashlight
|  |  |  |  |  +- glow
|  |  |  |  |  +- shield
|  |  |  |  |  +- thermals
|  |  |  |  |  `- xray
|  |  |  |  `- snail
|  |  |  +- frills
|  |  |  |  `- lizard
|  |  |  +- head_feature
|  |  |  |  +- skrell_hair
|  |  |  |  `- xeno_head
|  |  |  +- heart
|  |  |  |  +- construct
|  |  |  |  `- cursed
|  |  |  +- horns
|  |  |  |  +- halforc
|  |  |  |  `- humanoid
|  |  |  +- liver
|  |  |  |  +- alien
|  |  |  |  +- construct
|  |  |  |  +- cybernetic
|  |  |  |  |  `- upgraded
|  |  |  |  +- fly
|  |  |  |  `- plasmaman
|  |  |  +- lungs
|  |  |  |  +- construct
|  |  |  |  +- plasmaman
|  |  |  |  `- slime
|  |  |  +- neck_feature
|  |  |  |  +- anthro_fluff
|  |  |  |  `- moth_fluff
|  |  |  +- penis
|  |  |  |  +- barbed
|  |  |  |  +- barbed_knotted
|  |  |  |  +- equine
|  |  |  |  +- knotted
|  |  |  |  |  `- big
|  |  |  |  +- tapered
|  |  |  |  +- tapered_double
|  |  |  |  +- tapered_double_knotted
|  |  |  |  +- tapered_mammal
|  |  |  |  `- tentacle
|  |  |  +- snout
|  |  |  |  +- akula
|  |  |  |  +- anthro
|  |  |  |  +- beak
|  |  |  |  +- cat
|  |  |  |  +- lizard
|  |  |  |  |  `- psy_vault_guard
|  |  |  |  +- lupian
|  |  |  |  +- synth
|  |  |  |  +- tajaran
|  |  |  |  +- vox
|  |  |  |  `- vulpkanin
|  |  |  +- soul
|  |  |  |  `- fire
|  |  |  +- stomach
|  |  |  |  +- construct
|  |  |  |  +- ethereal
|  |  |  |  +- fly
|  |  |  |  `- plasmaman
|  |  |  +- tail
|  |  |  |  +- akula
|  |  |  |  +- anthro
|  |  |  |  +- avali
|  |  |  |  +- cat
|  |  |  |  +- dullahan
|  |  |  |  +- kobold
|  |  |  |  +- lizard
|  |  |  |  |  `- fake
|  |  |  |  +- lupian
|  |  |  |  +- monkey
|  |  |  |  +- synth
|  |  |  |  +- tajaran
|  |  |  |  +- tiefling
|  |  |  |  +- vox
|  |  |  |  +- vulpkanin
|  |  |  |  `- xeno
|  |  |  +- tail_feature
|  |  |  |  +- lizard_spines
|  |  |  |  `- vox_marking
|  |  |  +- taur_body
|  |  |  |  +- humanoid
|  |  |  |  `- synth
|  |  |  +- testicles
|  |  |  |  `- internal
|  |  |  +- tongue
|  |  |  |  +- abductor
|  |  |  |  +- alien
|  |  |  |  +- bone
|  |  |  |  |  `- plasmaman
|  |  |  |  +- construct
|  |  |  |  +- fly
|  |  |  |  +- lizard
|  |  |  |  +- moth
|  |  |  |  +- robot
|  |  |  |  +- snail
|  |  |  |  +- wild_tongue
|  |  |  |  `- zombie
|  |  |  +- vagina
|  |  |  +- vocal_cords
|  |  |  |  +- adamantine
|  |  |  |  `- colossus
|  |  |  `- wings
|  |  |     +- anthro
|  |  |     +- dracon
|  |  |     +- flight
|  |  |     |  +- angel
|  |  |     |  +- dragon
|  |  |     |  +- megamoth
|  |  |     |  `- night_kin
|  |  |     `- moth
|  |  +- oystershell
|  |  +- paint_brush
|  |  +- paint_palette
|  |  |  `- filled
|  |  +- paper
|  |  |  +- bsmith
|  |  |  +- carbon
|  |  |  +- construction
|  |  |  +- contract
|  |  |  |  `- employment
|  |  |  +- crumpled
|  |  |  |  +- bloody
|  |  |  |  `- muddy
|  |  |  +- fluff
|  |  |  |  +- jobs
|  |  |  |  |  +- jobs
|  |  |  |  |  +- medical
|  |  |  |  |  |  `- hippocratic
|  |  |  |  |  +- mining
|  |  |  |  |  |  `- smelter_notice
|  |  |  |  |  +- security
|  |  |  |  |  |  +- beepsky_mom
|  |  |  |  |  |  `- court_judgement
|  |  |  |  |  `- toxins
|  |  |  |  |     `- chemical_info
|  |  |  |  +- shuttles
|  |  |  |  |  `- daniel
|  |  |  |  +- sop
|  |  |  |  `- stations
|  |  |  |     +- centcom
|  |  |  |     |  +- broken_evac
|  |  |  |     |  +- bulletin
|  |  |  |     |  `- disk_memo
|  |  |  |     `- lavaland
|  |  |  |        `- orm_notice
|  |  |  +- guides
|  |  |  |  `- jobs
|  |  |  |     +- hydroponics
|  |  |  |     `- security
|  |  |  |        +- courtroom
|  |  |  |        +- labor_camp
|  |  |  |        `- range
|  |  |  +- inqslip
|  |  |  |  +- accusation
|  |  |  |  +- arrival
|  |  |  |  |  +- abso
|  |  |  |  |  +- inq
|  |  |  |  |  `- ortho
|  |  |  |  `- confession
|  |  |  +- inquisition_poultice_info
|  |  |  `- scroll
|  |  |     +- bounty
|  |  |     +- cargo
|  |  |     +- grudge
|  |  |     +- quest
|  |  |     +- sell_price_changes
|  |  |     `- trade_requests
|  |  +- parcel
|  |  +- pearl
|  |  |  `- blue
|  |  +- penis_fake
|  |  +- perfume
|  |  |  +- cherry
|  |  |  +- cinnamon
|  |  |  +- frankincense
|  |  |  +- jasmine
|  |  |  +- lavender
|  |  |  +- mint
|  |  |  +- myrrh
|  |  |  +- pear
|  |  |  +- rose
|  |  |  +- sandalwood
|  |  |  +- strawberry
|  |  |  `- vanilla
|  |  +- pestle
|  |  +- phylactery
|  |  +- piercings
|  |  |  +- beads
|  |  |  |  +- emerald
|  |  |  |  +- gold
|  |  |  |  `- silver
|  |  |  `- rings
|  |  |     +- emerald
|  |  |     +- gold
|  |  |     `- silver
|  |  +- polishing_cream
|  |  +- psydonmusicbox
|  |  +- pumpkinshell
|  |  +- queen_bee
|  |  +- quicksilver
|  |  |  `- luxinfused
|  |  +- quiver
|  |  |  +- bolt
|  |  |  |  +- heavy
|  |  |  |  +- light
|  |  |  |  `- standard
|  |  |  +- javelin
|  |  |  `- sling
|  |  +- ration
|  |  +- razor
|  |  +- reagent_containers
|  |  |  +- dropper
|  |  |  +- eoran_seed
|  |  |  +- food
|  |  |  |  `- snacks
|  |  |  |     +- allspice
|  |  |  |     +- badrecipe
|  |  |  |     +- balefire
|  |  |  |     |  `- slice
|  |  |  |     +- butter
|  |  |  |     +- butterslice
|  |  |  |     +- canned
|  |  |  |     +- caramel
|  |  |  |     +- chocolate
|  |  |  |     |  `- slice
|  |  |  |     +- clothing
|  |  |  |     +- crow
|  |  |  |     |  `- dead
|  |  |  |     +- deadmouse
|  |  |  |     +- dragee
|  |  |  |     +- egg
|  |  |  |     +- eoran_aril
|  |  |  |     |  +- ashen
|  |  |  |     |  +- auric
|  |  |  |     |  +- cerulean
|  |  |  |     |  +- crimson
|  |  |  |     |  +- fractal
|  |  |  |     |  +- ochre
|  |  |  |     |  +- opalescent
|  |  |  |     |  +- pearlescent
|  |  |  |     |  `- roseate
|  |  |  |     +- fat
|  |  |  |     |  `- salo
|  |  |  |     |     `- slice
|  |  |  |     +- fish
|  |  |  |     |  +- angler
|  |  |  |     |  +- bass
|  |  |  |     |  +- beaksnapper
|  |  |  |     |  +- black_bass
|  |  |  |     |  +- carp
|  |  |  |     |  +- clam
|  |  |  |     |  +- clownfish
|  |  |  |     |  +- cod
|  |  |  |     |  +- crab
|  |  |  |     |  +- creepy_eel
|  |  |  |     |  +- creepy_shark
|  |  |  |     |  +- creepy_squid
|  |  |  |     |  +- dead
|  |  |  |     |  +- eel
|  |  |  |     |  +- flounder
|  |  |  |     |  +- lobster
|  |  |  |     |  +- mackerel
|  |  |  |     |  +- mudskipper
|  |  |  |     |  +- oyster
|  |  |  |     |  +- plaice
|  |  |  |     |  +- salmon
|  |  |  |     |  |  `- black_headed
|  |  |  |     |  +- shrimp
|  |  |  |     |  +- sole
|  |  |  |     |  +- sturgeon
|  |  |  |     |  +- sunny
|  |  |  |     |  +- swamp_mother
|  |  |  |     |  +- swamp_shrimp
|  |  |  |     |  `- zizo_abberation
|  |  |  |     +- grown
|  |  |  |     |  +- apple
|  |  |  |     |  |  `- gold
|  |  |  |     |  +- berries
|  |  |  |     |  |  `- rogue
|  |  |  |     |  |     `- poison
|  |  |  |     |  +- cabbage
|  |  |  |     |  |  `- rogue
|  |  |  |     |  +- carrot
|  |  |  |     |  +- coffee
|  |  |  |     |  +- coffeebeans
|  |  |  |     |  +- coffeebeans_spiced
|  |  |  |     |  +- coffeebeansroasted
|  |  |  |     |  +- cucumber
|  |  |  |     |  +- eggplant
|  |  |  |     |  +- fruit
|  |  |  |     |  |  +- blackberry
|  |  |  |     |  |  |  `- skysugarbase
|  |  |  |     |  |  +- blackberry_sugared
|  |  |  |     |  |  +- lemon
|  |  |  |     |  |  +- lime
|  |  |  |     |  |  +- pear
|  |  |  |     |  |  +- plum
|  |  |  |     |  |  +- raspberry
|  |  |  |     |  |  +- strawberry
|  |  |  |     |  |  +- tangerine
|  |  |  |     |  |  +- tangerine_sugared
|  |  |  |     |  |  +- tomato
|  |  |  |     |  |  `- tomato_sliced
|  |  |  |     |  +- garlick
|  |  |  |     |  |  `- rogue
|  |  |  |     |  +- manabloom
|  |  |  |     |  +- nut
|  |  |  |     |  +- nut_sugared
|  |  |  |     |  +- oat
|  |  |  |     |  +- onion
|  |  |  |     |  |  `- rogue
|  |  |  |     |  +- pepperseed
|  |  |  |     |  +- potato
|  |  |  |     |  |  `- rogue
|  |  |  |     |  +- rice
|  |  |  |     |  +- rogue
|  |  |  |     |  |  +- chocolate_spiced
|  |  |  |     |  |  +- fyritius
|  |  |  |     |  |  |  `- bloodied
|  |  |  |     |  |  +- pipeweed
|  |  |  |     |  |  +- pipeweeddry
|  |  |  |     |  |  +- poppy
|  |  |  |     |  |  +- rosa_petals
|  |  |  |     |  |  +- rosa_petals_dried
|  |  |  |     |  |  +- rosa_petals_spiced
|  |  |  |     |  |  +- swampweed
|  |  |  |     |  |  +- swampweeddry
|  |  |  |     |  |  +- tealeaves_dry
|  |  |  |     |  |  +- tealeaves_ground
|  |  |  |     |  |  `- tealeaves_spiced
|  |  |  |     |  +- skysugarslab
|  |  |  |     |  +- sugarcane
|  |  |  |     |  +- sugarshape
|  |  |  |     |  |  +- amark
|  |  |  |     |  |  +- arch
|  |  |  |     |  |  +- archway
|  |  |  |     |  |  +- castle
|  |  |  |     |  |  +- dmark
|  |  |  |     |  |  +- flag
|  |  |  |     |  |  +- hmark
|  |  |  |     |  |  +- house
|  |  |  |     |  |  +- pmark
|  |  |  |     |  |  +- smark
|  |  |  |     |  |  +- statuek
|  |  |  |     |  |  +- statuel
|  |  |  |     |  |  +- statuer
|  |  |  |     |  |  +- statuey
|  |  |  |     |  |  +- tower
|  |  |  |     |  |  +- towers
|  |  |  |     |  |  +- tree
|  |  |  |     |  |  `- zmark
|  |  |  |     |  +- sunflower
|  |  |  |     |  +- tea
|  |  |  |     |  +- vegetable
|  |  |  |     |  |  `- turnip
|  |  |  |     |  `- wheat
|  |  |  |     +- jamtallow
|  |  |  |     +- jamtallowslice
|  |  |  |     +- marmalade
|  |  |  |     +- marmaladeslice
|  |  |  |     +- organ
|  |  |  |     |  `- heart
|  |  |  |     +- pepper
|  |  |  |     +- pumpkinspice
|  |  |  |     +- roastseeds
|  |  |  |     |  +- pumpkin
|  |  |  |     |  `- sunflower
|  |  |  |     +- rogue
|  |  |  |     |  +- abread_half
|  |  |  |     |  +- abreaduncooked
|  |  |  |     |  +- alecod
|  |  |  |     |  +- applebread
|  |  |  |     |  +- applebreadslice
|  |  |  |     |  +- applecake
|  |  |  |     |  +- applecakeslice
|  |  |  |     |  +- applenutcake
|  |  |  |     |  +- applenutcakeslice
|  |  |  |     |  +- berrycake
|  |  |  |     |  |  `- poison
|  |  |  |     |  +- berrycakeslice
|  |  |  |     |  |  `- poison
|  |  |  |     |  +- berrysalmon
|  |  |  |     |  +- biscuit
|  |  |  |     |  +- blackberrybookbread
|  |  |  |     |  +- blackberrybookbread_slice
|  |  |  |     |  +- blackberrybread_uncooked
|  |  |  |     |  +- blackberrycake
|  |  |  |     |  +- blackberrycakeslice
|  |  |  |     |  +- bookbread
|  |  |  |     |  +- bookbread_slice
|  |  |  |     |  +- bookbread_slice_jamtallowed
|  |  |  |     |  +- bookbread_slice_marmaladed
|  |  |  |     |  +- bread
|  |  |  |     |  +- breadslice
|  |  |  |     |  |  `- toast
|  |  |  |     |  |     +- buttered
|  |  |  |     |  |     +- jamtallowed_slice
|  |  |  |     |  |     `- marmaladed_slice
|  |  |  |     |  +- bun
|  |  |  |     |  +- bun_grenz
|  |  |  |     |  +- bun_jamtallow
|  |  |  |     |  +- bun_marmalade
|  |  |  |     |  +- bun_raston
|  |  |  |     |  +- butterdough
|  |  |  |     |  +- butterdoughslice
|  |  |  |     |  +- buttersole
|  |  |  |     |  +- cake
|  |  |  |     |  +- cake_base
|  |  |  |     |  +- cakeslice
|  |  |  |     |  +- carrotcake
|  |  |  |     |  +- carrotcakeslice
|  |  |  |     |  +- carrotsteak
|  |  |  |     |  +- ccake
|  |  |  |     |  +- ccakeslice
|  |  |  |     |  +- ccakeuncooked
|  |  |  |     |  +- cheddar
|  |  |  |     |  |  `- aged
|  |  |  |     |  +- cheddarslice
|  |  |  |     |  |  `- aged
|  |  |  |     |  +- cheddarwedge
|  |  |  |     |  |  `- aged
|  |  |  |     |  +- cheese
|  |  |  |     |  +- cheesebun
|  |  |  |     |  +- chocolatebiscuit
|  |  |  |     |  +- chocolatebookbread
|  |  |  |     |  +- chocolatebookbread_slice
|  |  |  |     |  +- chocolatebread_uncooked
|  |  |  |     |  +- cookie
|  |  |  |     |  +- cookie_unused
|  |  |  |     |  +- cookiec
|  |  |  |     |  +- cookied
|  |  |  |     |  +- cookier
|  |  |  |     |  +- cookieslice
|  |  |  |     |  +- cookieslicec
|  |  |  |     |  +- cookiesliced
|  |  |  |     |  +- cookieslicer
|  |  |  |     |  +- crabcake
|  |  |  |     |  +- crackerscooked
|  |  |  |     |  +- crossbun
|  |  |  |     |  +- crossbun_jamtallowed
|  |  |  |     |  +- crossbun_marmaladed
|  |  |  |     |  +- dendorsalmon
|  |  |  |     |  +- dot_tart
|  |  |  |     |  |  +- apple
|  |  |  |     |  |  +- blackberry
|  |  |  |     |  |  +- goldapple
|  |  |  |     |  |  +- pear
|  |  |  |     |  |  +- plum
|  |  |  |     |  |  +- raspberry
|  |  |  |     |  |  +- strawberry
|  |  |  |     |  |  `- tangerine
|  |  |  |     |  +- dough
|  |  |  |     |  +- dough_base
|  |  |  |     |  +- doughslice
|  |  |  |     |  +- eggplantcarved
|  |  |  |     |  +- eggplantmeat
|  |  |  |     |  +- eggplantstuffedraw
|  |  |  |     |  +- fishtomatoplate
|  |  |  |     |  +- fishtomatoplate_slice
|  |  |  |     |  +- flatdough
|  |  |  |     |  +- foodbase
|  |  |  |     |  |  +- biscuit_raw
|  |  |  |     |  |  +- cheesebun_raw
|  |  |  |     |  |  +- cheesewheel
|  |  |  |     |  |  +- chickentender
|  |  |  |     |  |  +- chocolatebiscuit_raw
|  |  |  |     |  |  +- cookie_raw
|  |  |  |     |  |  +- cookiec_raw
|  |  |  |     |  |  +- cookied_raw
|  |  |  |     |  |  +- cookier_raw
|  |  |  |     |  |  +- crabcakeraw
|  |  |  |     |  |  +- crossbun_raw
|  |  |  |     |  |  +- halfcookie_raw
|  |  |  |     |  |  +- halfcookiec_raw
|  |  |  |     |  |  +- halfcookied_raw
|  |  |  |     |  |  +- halfcookier_raw
|  |  |  |     |  |  +- handpieraw
|  |  |  |     |  |  |  +- apple
|  |  |  |     |  |  |  +- berry
|  |  |  |     |  |  |  +- cabbage
|  |  |  |     |  |  |  +- crab
|  |  |  |     |  |  |  +- fish
|  |  |  |     |  |  |  +- meat
|  |  |  |     |  |  |  +- mushroom
|  |  |  |     |  |  |  +- poison
|  |  |  |     |  |  |  `- potato
|  |  |  |     |  |  +- hardtack_raw
|  |  |  |     |  |  +- nitzel
|  |  |  |     |  |  +- piebottom
|  |  |  |     |  |  +- plumbiscuit_raw
|  |  |  |     |  |  +- prezzel_raw
|  |  |  |     |  |  +- psycrossbun_raw
|  |  |  |     |  |  +- pumpkinball_raw
|  |  |  |     |  |  +- pumpkinloaf_raw
|  |  |  |     |  |  +- schnitzel
|  |  |  |     |  |  +- squires_delight
|  |  |  |     |  |  +- tangerinebiscuit_raw
|  |  |  |     |  |  +- tartdough_apple
|  |  |  |     |  |  +- tartdough_blackberry
|  |  |  |     |  |  +- tartdough_goldapple
|  |  |  |     |  |  +- tartdough_pear
|  |  |  |     |  |  +- tartdough_plum
|  |  |  |     |  |  +- tartdough_raspberry
|  |  |  |     |  |  +- tartdough_strawberry
|  |  |  |     |  |  +- tartdough_tangerine
|  |  |  |     |  |  +- tomatoplate_raw
|  |  |  |     |  |  +- tomatoplate_raw_cheese
|  |  |  |     |  |  +- tomatoplate_raw_fish
|  |  |  |     |  |  +- tomatoplate_raw_onion
|  |  |  |     |  |  +- tomatoplate_raw_pear
|  |  |  |     |  |  +- tomatoplate_raw_poisontruffles
|  |  |  |     |  |  +- tomatoplate_raw_sausage
|  |  |  |     |  |  +- tomatoplate_raw_truffles
|  |  |  |     |  |  `- wienernitzel
|  |  |  |     |  +- friedcrow
|  |  |  |     |  +- friedegg
|  |  |  |     |  |  +- bacon
|  |  |  |     |  |  +- fried
|  |  |  |     |  |  +- hammerhold
|  |  |  |     |  |  +- sausage
|  |  |  |     |  |  +- sausagebacon
|  |  |  |     |  |  +- tiberian
|  |  |  |     |  |  `- two
|  |  |  |     |  +- friedrat
|  |  |  |     |  +- frostedcake
|  |  |  |     |  +- frostedcakeslice
|  |  |  |     |  +- frostedcakeuncooked
|  |  |  |     |  +- frosting
|  |  |  |     |  +- fruit
|  |  |  |     |  |  +- apple_sliced
|  |  |  |     |  |  |  `- gold
|  |  |  |     |  |  `- pumpkin_sliced
|  |  |  |     |  +- frybirdbucket
|  |  |  |     |  +- frybirdtato
|  |  |  |     |  +- frybread
|  |  |  |     |  +- fryfish
|  |  |  |     |  |  +- angler
|  |  |  |     |  |  +- bass
|  |  |  |     |  |  +- beaksnapper
|  |  |  |     |  |  +- black_bass
|  |  |  |     |  |  +- carp
|  |  |  |     |  |  +- clam
|  |  |  |     |  |  +- clownfish
|  |  |  |     |  |  +- cod
|  |  |  |     |  |  +- crab
|  |  |  |     |  |  +- eel
|  |  |  |     |  |  +- flounder
|  |  |  |     |  |  +- lobster
|  |  |  |     |  |  |  `- meal
|  |  |  |     |  |  +- mackerel
|  |  |  |     |  |  +- mudskipper
|  |  |  |     |  |  +- plaice
|  |  |  |     |  |  +- salmon
|  |  |  |     |  |  |  `- black_headed
|  |  |  |     |  |  +- shrimp
|  |  |  |     |  |  +- sole
|  |  |  |     |  |  +- sturgeon
|  |  |  |     |  |  +- sunny
|  |  |  |     |  |  +- swamp_mother
|  |  |  |     |  |  +- swamp_shrimp
|  |  |  |     |  |  `- zizo_abberation
|  |  |  |     |  +- garlickbass
|  |  |  |     |  +- handpie
|  |  |  |     |  |  +- apple
|  |  |  |     |  |  +- berry
|  |  |  |     |  |  +- cabbage
|  |  |  |     |  |  +- crab
|  |  |  |     |  |  +- fish
|  |  |  |     |  |  +- meat
|  |  |  |     |  |  +- mushroom
|  |  |  |     |  |  +- poison
|  |  |  |     |  |  `- potato
|  |  |  |     |  +- hcake
|  |  |  |     |  +- hcakeslice
|  |  |  |     |  +- hcakeuncooked
|  |  |  |     |  +- honey
|  |  |  |     |  |  +- ambrosia
|  |  |  |     |  |  +- healing
|  |  |  |     |  |  +- luminescent
|  |  |  |     |  |  +- spider
|  |  |  |     |  |  +- toxic
|  |  |  |     |  |  `- wild
|  |  |  |     |  +- jackberrybookbread
|  |  |  |     |  +- jackberrybookbread_slice
|  |  |  |     |  +- jackberrybread_uncooked
|  |  |  |     |  +- jelliedeel
|  |  |  |     |  +- lemonbookbread
|  |  |  |     |  +- lemonbookbread_slice
|  |  |  |     |  +- lemonbread_uncooked
|  |  |  |     |  +- lemoncake
|  |  |  |     |  +- lemoncakeslice
|  |  |  |     |  +- lemoncoppiette
|  |  |  |     |  +- limecake
|  |  |  |     |  +- limecakeslice
|  |  |  |     |  +- manacake
|  |  |  |     |  +- manacakeslice
|  |  |  |     |  +- meat
|  |  |  |     |  |  +- bacon
|  |  |  |     |  |  |  `- fried
|  |  |  |     |  |  +- brothbrique
|  |  |  |     |  |  |  `- slice
|  |  |  |     |  |  +- chickentender
|  |  |  |     |  |  +- coppiette
|  |  |  |     |  |  +- crab
|  |  |  |     |  |  |  `- fried
|  |  |  |     |  |  +- driedfishfilet
|  |  |  |     |  |  +- fatty
|  |  |  |     |  |  |  `- roast
|  |  |  |     |  |  +- fish
|  |  |  |     |  |  |  `- fried
|  |  |  |     |  |  +- ham
|  |  |  |     |  |  |  +- sliced
|  |  |  |     |  |  |  `- steamed
|  |  |  |     |  |  +- mince
|  |  |  |     |  |  |  +- beef
|  |  |  |     |  |  |  +- fish
|  |  |  |     |  |  |  +- poultry
|  |  |  |     |  |  |  `- rabbit
|  |  |  |     |  |  +- nitzel
|  |  |  |     |  |  |  +- schnitzel
|  |  |  |     |  |  |  `- wiener
|  |  |  |     |  |  +- poultry
|  |  |  |     |  |  |  +- baked
|  |  |  |     |  |  |  |  +- butter
|  |  |  |     |  |  |  |  +- doublestacked
|  |  |  |     |  |  |  |  `- spiced
|  |  |  |     |  |  |  |     `- ducal
|  |  |  |     |  |  |  `- cutlet
|  |  |  |     |  |  |     `- fried
|  |  |  |     |  |  +- rabbit
|  |  |  |     |  |  |  `- fried
|  |  |  |     |  |  |     `- garlick
|  |  |  |     |  |  |        `- cucumber
|  |  |  |     |  |  +- salami
|  |  |  |     |  |  |  `- slice
|  |  |  |     |  |  +- sausage
|  |  |  |     |  |  |  `- cooked
|  |  |  |     |  |  +- shellfish
|  |  |  |     |  |  |  `- fried
|  |  |  |     |  |  +- spider
|  |  |  |     |  |  |  `- fried
|  |  |  |     |  |  `- steak
|  |  |  |     |  |     +- fried
|  |  |  |     |  |     +- gnoll
|  |  |  |     |  |     |  `- seared
|  |  |  |     |  |     +- vilespawn
|  |  |  |     |  |     |  `- admin
|  |  |  |     |  |     `- wolf
|  |  |  |     |  |        `- fried
|  |  |  |     |  |           `- garlick
|  |  |  |     |  |              `- cucumber
|  |  |  |     |  +- meat_rotten
|  |  |  |     |  +- meattomatoplate
|  |  |  |     |  +- meattomatoplate_slice
|  |  |  |     |  +- menthacake
|  |  |  |     |  +- menthacakeslice
|  |  |  |     |  +- milkclam
|  |  |  |     |  +- muffin
|  |  |  |     |  |  +- cheese
|  |  |  |     |  |  |  `- baked
|  |  |  |     |  |  `- honey
|  |  |  |     |  |     `- baked
|  |  |  |     |  +- muffindough
|  |  |  |     |  +- onionplaice
|  |  |  |     |  +- onionsteak
|  |  |  |     |  +- oniontomatoplate
|  |  |  |     |  +- oniontomatoplate_slice
|  |  |  |     |  +- pastry
|  |  |  |     |  +- peacecake
|  |  |  |     |  +- peacecakeslice
|  |  |  |     |  +- pearbookbread
|  |  |  |     |  +- pearbookbread_slice
|  |  |  |     |  +- pearbread_uncooked
|  |  |  |     |  +- peartomatoplate
|  |  |  |     |  +- peartomatoplate_slice
|  |  |  |     |  +- pepperfish
|  |  |  |     |  +- pepperlobsta
|  |  |  |     |  +- peppersteak
|  |  |  |     |  |  `- ducal
|  |  |  |     |  +- pie
|  |  |  |     |  |  `- cooked
|  |  |  |     |  |     +- apple
|  |  |  |     |  |     +- berry
|  |  |  |     |  |     +- crab
|  |  |  |     |  |     +- meat
|  |  |  |     |  |     |  +- fish
|  |  |  |     |  |     |  `- meat
|  |  |  |     |  |     +- poison
|  |  |  |     |  |     +- pot
|  |  |  |     |  |     `- pumpkin
|  |  |  |     |  +- piedough
|  |  |  |     |  +- pieslice
|  |  |  |     |  |  `- pumpkin
|  |  |  |     |  +- plumbiscuit
|  |  |  |     |  +- plumbookbread
|  |  |  |     |  +- plumbookbread_slice
|  |  |  |     |  +- plumbread_uncooked
|  |  |  |     |  +- poisonberrybookbread
|  |  |  |     |  +- poisonberrybookbread_slice
|  |  |  |     |  +- poisonberrybread_uncooked
|  |  |  |     |  +- poisontruffletomatoplate
|  |  |  |     |  +- poisontruffletomatoplate_slice
|  |  |  |     |  +- preserved
|  |  |  |     |  |  +- cabbage_fried
|  |  |  |     |  |  +- carrot_baked
|  |  |  |     |  |  +- eggplantstuffed
|  |  |  |     |  |  +- eggplantstuffedcheese
|  |  |  |     |  |  +- onion_fried
|  |  |  |     |  |  +- potato_baked
|  |  |  |     |  |  +- potato_fried
|  |  |  |     |  |  +- pumpkin_mashed
|  |  |  |     |  |  `- rice_cooked
|  |  |  |     |  +- prezzel
|  |  |  |     |  +- psycrossbun
|  |  |  |     |  +- psycrossbun_jamtallowed
|  |  |  |     |  +- psycrossbun_marmaladed
|  |  |  |     |  +- pumpkinball
|  |  |  |     |  +- pumpkinloaf
|  |  |  |     |  +- pumpkinloafslice
|  |  |  |     |  +- raisinbread
|  |  |  |     |  +- raisinbreadslice
|  |  |  |     |  +- raisins
|  |  |  |     |  |  +- blackberry
|  |  |  |     |  |  +- lemon
|  |  |  |     |  |  +- lime
|  |  |  |     |  |  +- pear
|  |  |  |     |  |  +- plum
|  |  |  |     |  |  +- raspberry
|  |  |  |     |  |  +- strawberry
|  |  |  |     |  |  +- sweetglass
|  |  |  |     |  |  |  +- blackberry
|  |  |  |     |  |  |  +- lemon
|  |  |  |     |  |  |  +- lime
|  |  |  |     |  |  |  +- pear
|  |  |  |     |  |  |  +- plum
|  |  |  |     |  |  |  +- raspberry
|  |  |  |     |  |  |  +- strawberry
|  |  |  |     |  |  |  `- tangerine
|  |  |  |     |  |  `- tangerine
|  |  |  |     |  +- raspberrybookbread
|  |  |  |     |  +- raspberrybookbread_slice
|  |  |  |     |  +- raspberrybread_uncooked
|  |  |  |     |  +- raspberrycake
|  |  |  |     |  +- raspberrycakeslice
|  |  |  |     |  +- rbread_half
|  |  |  |     |  +- rbreaduncooked
|  |  |  |     |  +- ricebeef
|  |  |  |     |  +- ricebeefcar
|  |  |  |     |  +- ricebird
|  |  |  |     |  +- ricebirdcar
|  |  |  |     |  +- ricecheese
|  |  |  |     |  +- riceegg
|  |  |  |     |  +- riceeggcheese
|  |  |  |     |  +- ricepork
|  |  |  |     |  +- riceporkcuc
|  |  |  |     |  +- riceshrimp
|  |  |  |     |  +- riceshrimpcar
|  |  |  |     |  +- ricewet
|  |  |  |     |  +- rocknutcake
|  |  |  |     |  +- rocknutcakeslice
|  |  |  |     |  +- sandwich
|  |  |  |     |  |  +- bacon
|  |  |  |     |  |  +- cheese
|  |  |  |     |  |  +- egg
|  |  |  |     |  |  +- ham
|  |  |  |     |  |  +- salami
|  |  |  |     |  |  +- salo
|  |  |  |     |  |  `- tartar
|  |  |  |     |  +- steakcarrotonion
|  |  |  |     |  +- strawberrycake
|  |  |  |     |  +- strawberrycakeslice
|  |  |  |     |  +- strudel
|  |  |  |     |  |  `- sugar
|  |  |  |     |  +- strudeldough
|  |  |  |     |  +- strudelslice
|  |  |  |     |  |  `- sugar
|  |  |  |     |  +- stuffedegg
|  |  |  |     |  |  `- cooked
|  |  |  |     |  +- tangerinebiscuit
|  |  |  |     |  +- tangerinebookbread
|  |  |  |     |  +- tangerinebookbread_slice
|  |  |  |     |  +- tangerinebread_uncooked
|  |  |  |     |  +- tangerinecake
|  |  |  |     |  +- tangerinecakeslice
|  |  |  |     |  +- tartar
|  |  |  |     |  +- tartdough
|  |  |  |     |  +- toastcrumbs
|  |  |  |     |  +- tomatoplate
|  |  |  |     |  +- tomatoplate_slice
|  |  |  |     |  +- toxicshrooms
|  |  |  |     |  |  `- cooked
|  |  |  |     |  +- trailmix
|  |  |  |     |  +- truffles
|  |  |  |     |  |  `- cooked
|  |  |  |     |  +- truffletomatoplate
|  |  |  |     |  +- truffletomatoplate_slice
|  |  |  |     |  +- veg
|  |  |  |     |  |  +- cabbage_sliced
|  |  |  |     |  |  +- cucumber_sliced
|  |  |  |     |  |  +- garlick_clove
|  |  |  |     |  |  +- onion_sliced
|  |  |  |     |  |  `- potato_sliced
|  |  |  |     |  +- wienercabbage
|  |  |  |     |  +- wieneronions
|  |  |  |     |  +- wienerpotato
|  |  |  |     |  `- wienerpotatonions
|  |  |  |     +- smallrat
|  |  |  |     |  `- dead
|  |  |  |     +- squiresdelight
|  |  |  |     +- store
|  |  |  |     +- sugar
|  |  |  |     +- sugarstatue
|  |  |  |     |  +- amark
|  |  |  |     |  +- arch
|  |  |  |     |  +- archway
|  |  |  |     |  +- castle
|  |  |  |     |  +- dmark
|  |  |  |     |  +- flag
|  |  |  |     |  +- hmark
|  |  |  |     |  +- house
|  |  |  |     |  +- pmark
|  |  |  |     |  +- smark
|  |  |  |     |  +- statuek
|  |  |  |     |  +- statuel
|  |  |  |     |  +- statuer
|  |  |  |     |  +- statuey
|  |  |  |     |  +- tower
|  |  |  |     |  +- towers
|  |  |  |     |  +- tree
|  |  |  |     |  `- zmark
|  |  |  |     +- tallow
|  |  |  |     |  `- red
|  |  |  |     +- veg
|  |  |  |     |  `- turnip_sliced
|  |  |  |     `- xenoburger
|  |  |  +- glass
|  |  |  |  +- bottle
|  |  |  |  |  +- alchemical
|  |  |  |  |  |  +- blessedwater
|  |  |  |  |  |  +- conpot
|  |  |  |  |  |  +- endpot
|  |  |  |  |  |  +- fermented_crab
|  |  |  |  |  |  +- healthpot
|  |  |  |  |  |  +- healthpotnew
|  |  |  |  |  |  +- intpot
|  |  |  |  |  |  +- lucpot
|  |  |  |  |  |  +- manapot
|  |  |  |  |  |  +- perpot
|  |  |  |  |  |  +- rogue
|  |  |  |  |  |  |  `- rotcure
|  |  |  |  |  |  +- spdpot
|  |  |  |  |  |  +- spidervenom_paralytic
|  |  |  |  |  |  +- strongmanapot
|  |  |  |  |  |  +- strpot
|  |  |  |  |  |  `- tripot
|  |  |  |  |  +- brewing_bottle
|  |  |  |  |  +- claybottle
|  |  |  |  |  |  +- beer
|  |  |  |  |  |  +- gronnmead
|  |  |  |  |  |  +- nred
|  |  |  |  |  |  +- water
|  |  |  |  |  |  +- whitewine
|  |  |  |  |  |  `- wine
|  |  |  |  |  +- claybottleclassic
|  |  |  |  |  +- clayfancyvase
|  |  |  |  |  +- clayfancyvaseclassic
|  |  |  |  |  +- clayvase
|  |  |  |  |  +- clayvaseclassic
|  |  |  |  |  +- frankenbrew
|  |  |  |  |  |  `- third
|  |  |  |  |  +- mercury
|  |  |  |  |  +- revival
|  |  |  |  |  +- rogue
|  |  |  |  |  |  +- antidote
|  |  |  |  |  |  +- beer
|  |  |  |  |  |  |  +- apfelweinheim
|  |  |  |  |  |  |  +- aurorian
|  |  |  |  |  |  |  +- avarmead
|  |  |  |  |  |  |  +- avarrice
|  |  |  |  |  |  |  +- baijiu
|  |  |  |  |  |  |  +- blackgoat
|  |  |  |  |  |  |  +- butterhairs
|  |  |  |  |  |  |  +- fireleaf
|  |  |  |  |  |  |  +- gronnmead
|  |  |  |  |  |  |  +- hagwoodbitter
|  |  |  |  |  |  |  +- huangjiu
|  |  |  |  |  |  |  +- jagdtrunk
|  |  |  |  |  |  |  +- kgunlager
|  |  |  |  |  |  |  +- kgunplum
|  |  |  |  |  |  |  +- kgunsake
|  |  |  |  |  |  |  +- kgunshochu
|  |  |  |  |  |  |  +- komuchisake
|  |  |  |  |  |  |  +- murkwine
|  |  |  |  |  |  |  +- nocshine
|  |  |  |  |  |  |  +- nred
|  |  |  |  |  |  |  +- ratkept
|  |  |  |  |  |  |  +- rtoper
|  |  |  |  |  |  |  +- saigamilk
|  |  |  |  |  |  |  +- sazdistal
|  |  |  |  |  |  |  +- shejiu
|  |  |  |  |  |  |  +- stonebeardreserve
|  |  |  |  |  |  |  +- voddena
|  |  |  |  |  |  |  +- whipwine
|  |  |  |  |  |  |  +- yaojiu
|  |  |  |  |  |  |  `- zagul
|  |  |  |  |  |  +- berrypoison
|  |  |  |  |  |  +- elfblue
|  |  |  |  |  |  +- elfred
|  |  |  |  |  |  +- healthpot
|  |  |  |  |  |  |  `- zarum
|  |  |  |  |  |  +- healthpotnew
|  |  |  |  |  |  +- manapot
|  |  |  |  |  |  +- poison
|  |  |  |  |  |  +- redwine
|  |  |  |  |  |  +- spicedwine
|  |  |  |  |  |  +- spicedwineaged
|  |  |  |  |  |  +- spicedwinedelectable
|  |  |  |  |  |  +- stampoison
|  |  |  |  |  |  +- stampot
|  |  |  |  |  |  +- strong_antidote
|  |  |  |  |  |  +- strongmanapot
|  |  |  |  |  |  +- strongpoison
|  |  |  |  |  |  +- strongstampoison
|  |  |  |  |  |  +- strongstampot
|  |  |  |  |  |  +- triumphbeer
|  |  |  |  |  |  +- water
|  |  |  |  |  |  +- whitewine
|  |  |  |  |  |  `- wine
|  |  |  |  |  |     `- sourwine
|  |  |  |  |  +- sanctified_oil
|  |  |  |  |  `- waterskin
|  |  |  |  |     +- milk
|  |  |  |  |     `- purifier
|  |  |  |  +- bowl
|  |  |  |  |  +- aalloy
|  |  |  |  |  +- bronze
|  |  |  |  |  +- carved
|  |  |  |  |  |  +- amber
|  |  |  |  |  |  +- coral
|  |  |  |  |  |  +- jade
|  |  |  |  |  |  +- onyxa
|  |  |  |  |  |  +- opal
|  |  |  |  |  |  +- rose
|  |  |  |  |  |  +- shell
|  |  |  |  |  |  `- turq
|  |  |  |  |  +- gold
|  |  |  |  |  +- iron
|  |  |  |  |  `- silver
|  |  |  |  +- bucket
|  |  |  |  |  `- pot
|  |  |  |  |     +- aalloy
|  |  |  |  |     +- bronze
|  |  |  |  |     +- carved
|  |  |  |  |     |  +- teapotamber
|  |  |  |  |     |  +- teapotcoral
|  |  |  |  |     |  +- teapotjade
|  |  |  |  |     |  +- teapotonyxa
|  |  |  |  |     |  +- teapotopal
|  |  |  |  |     |  +- teapotrose
|  |  |  |  |     |  +- teapotshell
|  |  |  |  |     |  `- teapotturq
|  |  |  |  |     +- copper
|  |  |  |  |     +- kettle
|  |  |  |  |     |  `- tankard
|  |  |  |  |     |     +- blacksteel
|  |  |  |  |     |     `- silver
|  |  |  |  |     +- stone
|  |  |  |  |     `- teapot
|  |  |  |  |        `- fancy
|  |  |  |  +- cup
|  |  |  |  |  +- aalloygob
|  |  |  |  |  +- aalloymug
|  |  |  |  |  +- bronzegob
|  |  |  |  |  +- bronzemug
|  |  |  |  |  +- carved
|  |  |  |  |  |  +- amber
|  |  |  |  |  |  +- amberfancy
|  |  |  |  |  |  +- coral
|  |  |  |  |  |  +- coralfancy
|  |  |  |  |  |  +- jade
|  |  |  |  |  |  +- jadefancy
|  |  |  |  |  |  +- onyxa
|  |  |  |  |  |  +- onyxafancy
|  |  |  |  |  |  +- opal
|  |  |  |  |  |  +- opalfancy
|  |  |  |  |  |  +- rose
|  |  |  |  |  |  +- rosefancy
|  |  |  |  |  |  +- shell
|  |  |  |  |  |  +- shellfancy
|  |  |  |  |  |  +- turq
|  |  |  |  |  |  `- turqfancy
|  |  |  |  |  +- ceramic
|  |  |  |  |  |  `- fancy
|  |  |  |  |  +- claycup
|  |  |  |  |  +- claycupclassic
|  |  |  |  |  +- golden
|  |  |  |  |  |  +- poison
|  |  |  |  |  |  `- small
|  |  |  |  |  +- silver
|  |  |  |  |  |  +- pewter
|  |  |  |  |  |  `- small
|  |  |  |  |  +- skull
|  |  |  |  |  +- steel
|  |  |  |  |  `- wooden
|  |  |  |  |     `- crafted
|  |  |  |  +- mortar
|  |  |  |  `- rag
|  |  |  +- lux
|  |  |  |  `- eoran_aril
|  |  |  +- lux_impure
|  |  |  +- lux_moss
|  |  |  +- peppermill
|  |  |  +- pill
|  |  |  |  +- aranesp
|  |  |  |  +- cyanide
|  |  |  |  +- floorpill
|  |  |  |  +- happiness
|  |  |  |  +- happy
|  |  |  |  +- iron
|  |  |  |  +- lsd
|  |  |  |  +- patch
|  |  |  |  `- tox
|  |  |  +- powder
|  |  |  |  +- coarse_salt
|  |  |  |  +- flour
|  |  |  |  +- herozium
|  |  |  |  +- mineral
|  |  |  |  +- moondust
|  |  |  |  +- moondust_purest
|  |  |  |  +- ozium
|  |  |  |  +- rocknut
|  |  |  |  +- salt
|  |  |  |  +- spice
|  |  |  |  `- starsugar
|  |  |  |     `- skysugar
|  |  |  `- spidervenom_inert
|  |  +- recipe_book
|  |  |  +- alchemy
|  |  |  +- blacksmithing
|  |  |  +- builder
|  |  |  +- ceramics
|  |  |  +- cooking
|  |  |  +- engineering
|  |  |  +- hag_grimoire
|  |  |  |  `- moss_recipes
|  |  |  +- leatherworking
|  |  |  +- magic
|  |  |  +- miracle_compendium
|  |  |  +- sewing
|  |  |  +- spell_list
|  |  |  `- survival
|  |  +- repair_kit
|  |  |  +- bad
|  |  |  `- metal
|  |  |     `- bad
|  |  +- restraints
|  |  |  `- legcuffs
|  |  |     `- beartrap
|  |  |        +- armed
|  |  |        |  `- camouflage
|  |  |        `- crafted
|  |  +- reverse_bear_trap
|  |  +- riddleofsteel
|  |  +- riding_offhand
|  |  +- ritechalk
|  |  +- rogue
|  |  |  +- instrument
|  |  |  |  +- accord
|  |  |  |  +- drum
|  |  |  |  +- flute
|  |  |  |  +- guitar
|  |  |  |  +- harp
|  |  |  |  |  `- handcarved
|  |  |  |  +- hurdygurdy
|  |  |  |  +- lute
|  |  |  |  +- psyaltery
|  |  |  |  +- shamisen
|  |  |  |  +- viola
|  |  |  |  `- vocals
|  |  |  `- painting
|  |  |     +- queen
|  |  |     +- seraphina
|  |  |     `- skullzhg
|  |  +- roguebin
|  |  |  `- trash
|  |  +- roguecoin
|  |  |  +- aalloy
|  |  |  +- copper
|  |  |  +- gold
|  |  |  +- inqcoin
|  |  |  `- silver
|  |  +- roguegear
|  |  +- roguegem
|  |  |  +- amber
|  |  |  +- amethyst
|  |  |  |  `- naledi
|  |  |  +- blood_diamond
|  |  |  +- blue
|  |  |  +- coral
|  |  |  +- diamond
|  |  |  +- green
|  |  |  +- jade
|  |  |  +- onyxa
|  |  |  +- opal
|  |  |  +- oyster
|  |  |  +- random
|  |  |  +- random_gemcraft
|  |  |  +- ruby
|  |  |  +- turq
|  |  |  +- violet
|  |  |  `- yellow
|  |  +- roguekey
|  |  |  +- apartments
|  |  |  |  +- stable1
|  |  |  |  +- stable2
|  |  |  |  +- stablemaster
|  |  |  |  +- stablemaster_1
|  |  |  |  +- stablemaster_2
|  |  |  |  +- stablemaster_3
|  |  |  |  +- stablemaster_4
|  |  |  |  +- stablemaster_5
|  |  |  |  +- stall1
|  |  |  |  +- stall2
|  |  |  |  +- stall3
|  |  |  |  `- stall4
|  |  |  +- apothecary
|  |  |  +- archive
|  |  |  +- armory
|  |  |  +- bandit
|  |  |  +- bath
|  |  |  +- bathmaster
|  |  |  +- bathworker
|  |  |  +- church
|  |  |  |  +- roomi
|  |  |  |  +- roomii
|  |  |  |  +- roomiii
|  |  |  |  +- roomiv
|  |  |  |  +- roomix
|  |  |  |  +- roomv
|  |  |  |  +- roomvi
|  |  |  |  +- roomvii
|  |  |  |  +- roomviii
|  |  |  |  +- roomx
|  |  |  |  +- roomxi
|  |  |  |  +- roomxii
|  |  |  |  +- roomxiii
|  |  |  |  `- roomxiv
|  |  |  +- crafterguild
|  |  |  +- craftermaster
|  |  |  +- crier
|  |  |  +- custom
|  |  |  +- dungeon
|  |  |  +- fancyroomi
|  |  |  +- fancyroomii
|  |  |  +- fancyroomiii
|  |  |  +- fancyroomiv
|  |  |  +- fancyroomv
|  |  |  +- farm
|  |  |  +- garrison
|  |  |  +- graveyard
|  |  |  +- hag
|  |  |  +- hand
|  |  |  +- heir
|  |  |  |  +- one
|  |  |  |  `- two
|  |  |  +- inhumen
|  |  |  |  +- four
|  |  |  |  +- one
|  |  |  |  +- three
|  |  |  |  `- two
|  |  |  +- inquisitionmanor
|  |  |  +- inquisitor
|  |  |  +- keeper
|  |  |  +- keeper_inner
|  |  |  +- knight
|  |  |  +- lord
|  |  |  +- mage
|  |  |  |  +- baroness
|  |  |  |  `- lich
|  |  |  +- manor
|  |  |  |  +- councillor
|  |  |  |  |  +- three
|  |  |  |  |  `- two
|  |  |  |  +- guest
|  |  |  |  |  +- four
|  |  |  |  |  +- three
|  |  |  |  |  `- two
|  |  |  |  +- knight
|  |  |  |  |  +- four
|  |  |  |  |  +- three
|  |  |  |  |  `- two
|  |  |  |  +- servant
|  |  |  |  |  +- five
|  |  |  |  |  +- four
|  |  |  |  |  +- six
|  |  |  |  |  +- three
|  |  |  |  |  `- two
|  |  |  |  `- squire
|  |  |  |     +- four
|  |  |  |     +- three
|  |  |  |     `- two
|  |  |  +- marshal
|  |  |  +- mercenary
|  |  |  |  `- bedrooms
|  |  |  |     +- ii
|  |  |  |     +- iii
|  |  |  |     +- iv
|  |  |  |     +- v
|  |  |  |     +- vi
|  |  |  |     +- vii
|  |  |  |     `- viii
|  |  |  +- merchant
|  |  |  +- physician
|  |  |  +- porta
|  |  |  +- priest
|  |  |  +- psy_bog
|  |  |  |  +- exit
|  |  |  |  `- two
|  |  |  +- psydonkey
|  |  |  +- roomhunt
|  |  |  +- roomi
|  |  |  +- roomii
|  |  |  +- roomiii
|  |  |  +- roomiv
|  |  |  +- roomv
|  |  |  +- roomvi
|  |  |  +- royal
|  |  |  +- sergeant
|  |  |  +- shop
|  |  |  +- skeleton
|  |  |  +- steward
|  |  |  +- tailor
|  |  |  +- tavern
|  |  |  +- tavernkeep
|  |  |  +- townie
|  |  |  +- townie_smith_extras
|  |  |  +- university
|  |  |  +- university_secure
|  |  |  +- vampire
|  |  |  |  +- guest
|  |  |  |  `- maid
|  |  |  +- vault
|  |  |  +- veteran
|  |  |  +- walls
|  |  |  +- warden
|  |  |  `- zurch_bedroom
|  |  |     +- admin
|  |  |     +- eight
|  |  |     +- eleven
|  |  |     +- five
|  |  |     +- four
|  |  |     +- nine
|  |  |     +- seven
|  |  |     +- six
|  |  |     +- ten
|  |  |     +- three
|  |  |     +- twelve
|  |  |     `- two
|  |  +- roguemachine
|  |  |  +- mastermail
|  |  |  `- navigator
|  |  |     `- smuggler
|  |  +- rogueore
|  |  |  +- cinnabar
|  |  |  +- coal
|  |  |  |  `- charcoal
|  |  |  +- copper
|  |  |  +- gold
|  |  |  +- iron
|  |  |  +- lithmyc
|  |  |  +- silver
|  |  |  `- tin
|  |  +- roguestatue
|  |  |  +- aalloy
|  |  |  +- blacksteel
|  |  |  +- bronze
|  |  |  +- clay
|  |  |  +- glass
|  |  |  +- gold
|  |  |  |  `- loot
|  |  |  +- iron
|  |  |  +- silver
|  |  |  `- steel
|  |  +- rogueweapon
|  |  |  +- bear_claw
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  +- blowrod
|  |  |  +- cabbit_claw
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  +- cat_claw
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  +- chisel
|  |  |  |  +- assembly
|  |  |  |  |  +- hammer
|  |  |  |  |  |  `- bronze
|  |  |  |  |  +- hammerblacksteel
|  |  |  |  |  |  `- bronze
|  |  |  |  |  +- hammerbronze
|  |  |  |  |  |  `- bronze
|  |  |  |  |  +- hammerclaw
|  |  |  |  |  |  `- bronze
|  |  |  |  |  +- mallet
|  |  |  |  |  |  `- bronze
|  |  |  |  |  +- stone
|  |  |  |  |  |  `- bronze
|  |  |  |  |  `- stoneblock
|  |  |  |  |     `- bronze
|  |  |  |  `- bronze
|  |  |  +- drd
|  |  |  |  `- shield
|  |  |  +- eaglebeak
|  |  |  |  `- lucerne
|  |  |  +- eirenxiv
|  |  |  |  +- eiren_m
|  |  |  |  `- eirensword
|  |  |  +- estoc
|  |  |  |  +- triumph
|  |  |  |  `- worttrager
|  |  |  +- example
|  |  |  |  +- ada
|  |  |  |  +- aeternum
|  |  |  |  +- dadao
|  |  |  |  +- eiren_greatsword
|  |  |  |  +- eiren_sabre
|  |  |  |  +- eiren_sabre_alt
|  |  |  |  +- gdadao
|  |  |  |  +- hwi
|  |  |  |  +- ida
|  |  |  |  +- inverserun_greatsword
|  |  |  |  +- kaskara
|  |  |  |  +- ngombe
|  |  |  |  +- regnum
|  |  |  |  +- sengese
|  |  |  |  +- stinketh_sabre
|  |  |  |  +- valorian_broadsword
|  |  |  |  +- valorian_greatsword
|  |  |  |  +- valorian_sword
|  |  |  |  +- waffai_greatsword
|  |  |  |  `- wodao
|  |  |  +- fishspear
|  |  |  |  `- depthseek
|  |  |  +- flail
|  |  |  |  +- aflail
|  |  |  |  +- alt
|  |  |  |  +- bronze
|  |  |  |  +- militia
|  |  |  |  +- peasantwarflail
|  |  |  |  |  +- iron
|  |  |  |  |  `- matthios
|  |  |  |  `- sflail
|  |  |  |     +- necraflail
|  |  |  |     +- paflail
|  |  |  |     +- psyflail
|  |  |  |     |  `- relic
|  |  |  |     `- silver
|  |  |  +- fox_claw
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  +- gangrel
|  |  |  +- greataxe
|  |  |  |  +- bronze
|  |  |  |  +- dreamscape
|  |  |  |  |  `- active
|  |  |  |  +- militia
|  |  |  |  |  `- silver
|  |  |  |  +- psy
|  |  |  |  +- silver
|  |  |  |  +- steel
|  |  |  |  |  +- doublehead
|  |  |  |  |  |  +- graggar
|  |  |  |  |  |  +- martyr
|  |  |  |  |  |  `- minotaur
|  |  |  |  |  +- gilded
|  |  |  |  |  +- hag
|  |  |  |  |  `- knight
|  |  |  |  `- zygreataxe
|  |  |  +- greatsword
|  |  |  |  +- aalloy
|  |  |  |  +- bsword
|  |  |  |  |  +- dreamscape
|  |  |  |  |  |  `- active
|  |  |  |  |  `- psy
|  |  |  |  |     +- relic
|  |  |  |  |     `- unforgotten
|  |  |  |  +- elfgsword
|  |  |  |  +- elvish
|  |  |  |  +- grenz
|  |  |  |  |  `- flamberge
|  |  |  |  |     +- aalloy
|  |  |  |  |     +- blacksteel
|  |  |  |  |     +- malum
|  |  |  |  |     +- paalloy
|  |  |  |  |     `- ravox
|  |  |  |  +- iron
|  |  |  |  +- paalloy
|  |  |  |  +- psygsword
|  |  |  |  |  `- relic
|  |  |  |  +- silver
|  |  |  |  `- zwei
|  |  |  +- hag_claw
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  +- halberd
|  |  |  |  +- bardiche
|  |  |  |  |  +- aalloy
|  |  |  |  |  +- elvish
|  |  |  |  |  |  `- autumn
|  |  |  |  |  +- paalloy
|  |  |  |  |  `- scythe
|  |  |  |  +- bone
|  |  |  |  +- glaive
|  |  |  |  |  +- dreamscape
|  |  |  |  |  |  `- active
|  |  |  |  |  +- elvish
|  |  |  |  |  +- knightcaptain
|  |  |  |  |  `- koruu
|  |  |  |  +- hag
|  |  |  |  +- pestran
|  |  |  |  `- psyhalberd
|  |  |  |     `- relic
|  |  |  +- hammer
|  |  |  |  +- aalloy
|  |  |  |  +- blacksteel
|  |  |  |  +- bronze
|  |  |  |  +- copper
|  |  |  |  +- iron
|  |  |  |  +- steel
|  |  |  |  +- stone
|  |  |  |  `- wood
|  |  |  +- handclaw
|  |  |  |  +- gronn
|  |  |  |  |  `- silver
|  |  |  |  `- steel
|  |  |  +- handsaw
|  |  |  |  `- bronze
|  |  |  +- hoe
|  |  |  |  +- aalloy
|  |  |  |  +- bronze
|  |  |  |  +- copper
|  |  |  |  `- stone
|  |  |  +- huntingknife
|  |  |  |  +- bronze
|  |  |  |  +- chefknife
|  |  |  |  |  `- cleaver
|  |  |  |  +- cleaver
|  |  |  |  +- combat
|  |  |  |  |  +- bronze
|  |  |  |  |  +- fencerguy
|  |  |  |  |  +- iron
|  |  |  |  |  |  `- kris
|  |  |  |  |  +- kris
|  |  |  |  |  +- messser
|  |  |  |  |  `- njora
|  |  |  |  +- copper
|  |  |  |  +- idagger
|  |  |  |  |  +- adagger
|  |  |  |  |  +- dtace
|  |  |  |  |  +- elvish
|  |  |  |  |  |  `- autumn
|  |  |  |  |  +- kris
|  |  |  |  |  +- navaja
|  |  |  |  |  |  `- freifechter
|  |  |  |  |  +- njora
|  |  |  |  |  +- silver
|  |  |  |  |  |  +- arcyne
|  |  |  |  |  |  +- elvish
|  |  |  |  |  |  |  +- drow
|  |  |  |  |  |  |  `- poopknife
|  |  |  |  |  |  +- psydagger
|  |  |  |  |  |  `- stake
|  |  |  |  |  |     `- psy
|  |  |  |  |  +- stake
|  |  |  |  |  +- steel
|  |  |  |  |  |  +- bone
|  |  |  |  |  |  +- corroded
|  |  |  |  |  |  |  `- dirk
|  |  |  |  |  |  +- decorated
|  |  |  |  |  |  +- fire
|  |  |  |  |  |  +- holysee
|  |  |  |  |  |  +- kazengun
|  |  |  |  |  |  +- kris
|  |  |  |  |  |  +- njora
|  |  |  |  |  |  +- padagger
|  |  |  |  |  |  +- parrying
|  |  |  |  |  |  |  +- hand
|  |  |  |  |  |  |  `- vaquero
|  |  |  |  |  |  +- pestrasickle
|  |  |  |  |  |  |  `- keeper
|  |  |  |  |  |  +- profane
|  |  |  |  |  |  +- rondel
|  |  |  |  |  |  +- shudderfly
|  |  |  |  |  |  +- special
|  |  |  |  |  |  `- trainer
|  |  |  |  |  +- virtue
|  |  |  |  |  `- warden_machete
|  |  |  |  +- njora
|  |  |  |  +- scissors
|  |  |  |  |  `- steel
|  |  |  |  +- stoneknife
|  |  |  |  |  +- kukri
|  |  |  |  |  `- opalknife
|  |  |  |  +- throwingknife
|  |  |  |  |  +- aalloy
|  |  |  |  |  +- kazengun
|  |  |  |  |  +- psydon
|  |  |  |  |  +- silver
|  |  |  |  |  +- steel
|  |  |  |  |  |  `- palloy
|  |  |  |  |  `- triumph
|  |  |  |  `- wood
|  |  |  +- katar
|  |  |  |  +- abyssor
|  |  |  |  +- bronze
|  |  |  |  |  `- gladiator
|  |  |  |  +- psydon
|  |  |  |  +- punchdagger
|  |  |  |  |  `- frei
|  |  |  |  `- silver
|  |  |  +- koruu
|  |  |  |  `- kukri
|  |  |  |     `- warden
|  |  |  +- lordscepter
|  |  |  +- mace
|  |  |  |  +- alloy
|  |  |  |  +- bronze
|  |  |  |  +- church
|  |  |  |  +- cudgel
|  |  |  |  |  +- copper
|  |  |  |  |  +- flanged
|  |  |  |  |  |  `- silver
|  |  |  |  |  +- justice
|  |  |  |  |  +- psy
|  |  |  |  |  |  `- old
|  |  |  |  |  +- psyclassic
|  |  |  |  |  |  `- old
|  |  |  |  |  `- shellrungu
|  |  |  |  +- goden
|  |  |  |  |  +- aalloy
|  |  |  |  |  +- deepduke
|  |  |  |  |  +- kanabo
|  |  |  |  |  +- martyr
|  |  |  |  |  +- psymace
|  |  |  |  |  `- steel
|  |  |  |  |     +- paalloy
|  |  |  |  |     `- ravox
|  |  |  |  +- gold
|  |  |  |  +- maul
|  |  |  |  |  +- grand
|  |  |  |  |  |  `- malum
|  |  |  |  |  +- spiked
|  |  |  |  |  `- steel
|  |  |  |  +- mushroom
|  |  |  |  +- oar
|  |  |  |  +- parasol
|  |  |  |  |  `- noble
|  |  |  |  +- rungu
|  |  |  |  +- spiked
|  |  |  |  +- steel
|  |  |  |  |  +- morningstar
|  |  |  |  |  +- palloy
|  |  |  |  |  +- rungu
|  |  |  |  |  `- silver
|  |  |  |  |     +- decorated
|  |  |  |  |     `- rungu
|  |  |  |  +- stunmace
|  |  |  |  +- warhammer
|  |  |  |  |  +- alloy
|  |  |  |  |  +- bronze
|  |  |  |  |  |  `- decorated
|  |  |  |  |  +- shishpar
|  |  |  |  |  `- steel
|  |  |  |  |     +- paalloy
|  |  |  |  |     +- shishpar
|  |  |  |  |     `- silver
|  |  |  |  +- woodclub
|  |  |  |  |  +- crafted
|  |  |  |  |  `- deprived
|  |  |  |  `- wsword
|  |  |  +- maesune
|  |  |  |  +- sabre
|  |  |  |  `- shield
|  |  |  +- magicbrick
|  |  |  +- mole_claw
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  +- nerocavalier
|  |  |  |  `- flsword
|  |  |  +- pick
|  |  |  |  +- aalloy
|  |  |  |  +- blacksteel
|  |  |  |  +- bronze
|  |  |  |  +- copper
|  |  |  |  +- militia
|  |  |  |  |  `- steel
|  |  |  |  +- paalloy
|  |  |  |  +- steel
|  |  |  |  `- stone
|  |  |  +- pitchfork
|  |  |  |  +- aalloy
|  |  |  |  +- bronze
|  |  |  |  `- copper
|  |  |  +- saiga_hoof
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  +- scabbard
|  |  |  |  +- gwstrap
|  |  |  |  +- sheath
|  |  |  |  |  +- courtphysician
|  |  |  |  |  |  `- hand
|  |  |  |  |  +- kazengun
|  |  |  |  |  +- noble
|  |  |  |  |  +- royal
|  |  |  |  |  `- strap
|  |  |  |  `- sword
|  |  |  |     +- kazengun
|  |  |  |     |  +- gold
|  |  |  |     |  +- kodachi
|  |  |  |     |  +- noparry
|  |  |  |     |  `- steel
|  |  |  |     +- noble
|  |  |  |     +- royal
|  |  |  |     `- strap
|  |  |  +- scythe
|  |  |  +- shield
|  |  |  |  +- arcyne_aegis
|  |  |  |  +- atgervi
|  |  |  |  +- bronze
|  |  |  |  |  `- great
|  |  |  |  +- buckler
|  |  |  |  |  +- banneret
|  |  |  |  |  `- palloy
|  |  |  |  +- heater
|  |  |  |  |  `- crafted
|  |  |  |  +- iron
|  |  |  |  |  +- bone
|  |  |  |  |  `- steppesman
|  |  |  |  +- steam
|  |  |  |  +- tower
|  |  |  |  |  +- holysee
|  |  |  |  |  +- metal
|  |  |  |  |  |  +- alloy
|  |  |  |  |  |  +- gold
|  |  |  |  |  |  +- palloy
|  |  |  |  |  |  `- psy
|  |  |  |  |  +- raneshen
|  |  |  |  |  `- spidershield
|  |  |  |  `- wood
|  |  |  |     `- deprived
|  |  |  +- shovel
|  |  |  |  +- aalloy
|  |  |  |  +- bronze
|  |  |  |  +- silver
|  |  |  |  +- small
|  |  |  |  |  `- crafted
|  |  |  |  `- zoe_silence
|  |  |  +- sickle
|  |  |  |  +- aalloy
|  |  |  |  +- bronze
|  |  |  |  `- copper
|  |  |  +- spear
|  |  |  |  +- aalloy
|  |  |  |  +- assegai
|  |  |  |  |  `- iron
|  |  |  |  +- billhook
|  |  |  |  +- boar
|  |  |  |  |  `- frei
|  |  |  |  |     `- pike
|  |  |  |  |        +- reformist
|  |  |  |  |        `- stinketh
|  |  |  |  +- bonespear
|  |  |  |  +- bronze
|  |  |  |  |  +- strapless
|  |  |  |  |  `- winged
|  |  |  |  |     `- strapless
|  |  |  |  +- dreamscape_trident
|  |  |  |  |  `- active
|  |  |  |  +- holysee
|  |  |  |  +- improvisedbillhook
|  |  |  |  +- keep_standard
|  |  |  |  +- lance
|  |  |  |  |  `- dasfox
|  |  |  |  +- militia
|  |  |  |  +- naginata
|  |  |  |  |  `- koruu
|  |  |  |  +- paalloy
|  |  |  |  +- partizan
|  |  |  |  |  `- martyr
|  |  |  |  +- psyspear
|  |  |  |  |  `- old
|  |  |  |  +- short
|  |  |  |  +- silver
|  |  |  |  +- spellblade
|  |  |  |  +- stone
|  |  |  |  |  `- copper
|  |  |  |  +- trainer
|  |  |  |  `- trident
|  |  |  +- spider_fang
|  |  |  |  +- left
|  |  |  |  +- mire
|  |  |  |  |  +- left
|  |  |  |  |  `- right
|  |  |  |  `- right
|  |  |  +- stoneaxe
|  |  |  |  +- battle
|  |  |  |  |  +- abyssoraxe
|  |  |  |  |  +- ice
|  |  |  |  |  +- psyaxe
|  |  |  |  |  |  `- triumph
|  |  |  |  |  +- slayer
|  |  |  |  |  +- steppesman
|  |  |  |  |  |  `- chupa
|  |  |  |  |  `- triumph
|  |  |  |  +- boneaxe
|  |  |  |  +- handaxe
|  |  |  |  |  +- copper
|  |  |  |  |  `- triumph
|  |  |  |  +- hurlbat
|  |  |  |  +- oath
|  |  |  |  `- woodcut
|  |  |  |     +- aaxe
|  |  |  |     +- bronze
|  |  |  |     |  `- triumph
|  |  |  |     +- bronzebattleaxe
|  |  |  |     +- pick
|  |  |  |     +- silver
|  |  |  |     |  `- triumph
|  |  |  |     +- steel
|  |  |  |     |  +- atgervi
|  |  |  |     |  +- decorated
|  |  |  |     |  +- paaxe
|  |  |  |     |  +- slayer
|  |  |  |     |  +- triumph
|  |  |  |     |  `- woodcutter
|  |  |  |     +- triumph
|  |  |  |     +- triumphalt
|  |  |  |     +- troll
|  |  |  |     +- wardenpick
|  |  |  |     `- woodcutter
|  |  |  +- surgery
|  |  |  |  +- bonesetter
|  |  |  |  +- cautery
|  |  |  |  +- hammer
|  |  |  |  +- hemostat
|  |  |  |  |  +- first
|  |  |  |  |  +- improv
|  |  |  |  |  +- second
|  |  |  |  |  `- third
|  |  |  |  +- retractor
|  |  |  |  |  `- improv
|  |  |  |  +- saw
|  |  |  |  |  `- improv
|  |  |  |  `- scalpel
|  |  |  +- sword
|  |  |  |  +- astrata_sword
|  |  |  |  +- blacksteel
|  |  |  |  |  `- decorated
|  |  |  |  +- broken
|  |  |  |  +- bronze
|  |  |  |  +- cutlass
|  |  |  |  +- dakken_sword
|  |  |  |  +- decorated
|  |  |  |  +- falchion
|  |  |  |  |  `- militia
|  |  |  |  |     `- bronze
|  |  |  |  +- falx
|  |  |  |  |  `- stalker
|  |  |  |  +- gold
|  |  |  |  +- iron
|  |  |  |  +- long
|  |  |  |  |  +- ap
|  |  |  |  |  |  `- triumph
|  |  |  |  |  +- broadsword
|  |  |  |  |  |  +- bronze
|  |  |  |  |  |  `- steel
|  |  |  |  |  +- church
|  |  |  |  |  +- crusader
|  |  |  |  |  +- dakken_longsword
|  |  |  |  |  +- death
|  |  |  |  |  +- dec
|  |  |  |  |  +- drd
|  |  |  |  |  +- elvish
|  |  |  |  |  |  `- autumn
|  |  |  |  |  +- etruscan
|  |  |  |  |  |  `- freifechter
|  |  |  |  |  +- exe
|  |  |  |  |  |  +- astrata
|  |  |  |  |  |  +- berserk
|  |  |  |  |  |  |  +- dragonslayer
|  |  |  |  |  |  |  `- gnoll
|  |  |  |  |  |  +- cloth
|  |  |  |  |  |  +- rockhill
|  |  |  |  |  |  `- silver
|  |  |  |  |  +- fencerguy
|  |  |  |  |  +- greatkhopesh
|  |  |  |  |  +- hag
|  |  |  |  |  +- hand
|  |  |  |  |  +- heirloom
|  |  |  |  |  +- holysee
|  |  |  |  |  +- judgement
|  |  |  |  |  |  +- ascendant
|  |  |  |  |  |  `- vlord
|  |  |  |  |  +- kriegmesser
|  |  |  |  |  |  +- noc
|  |  |  |  |  |  +- pestran
|  |  |  |  |  |  +- psy
|  |  |  |  |  |  +- sabreguard
|  |  |  |  |  |  +- silver
|  |  |  |  |  |  `- ssangsudo
|  |  |  |  |  +- marlin
|  |  |  |  |  +- martyr
|  |  |  |  |  +- oathkeeper
|  |  |  |  |  +- oldpsysword
|  |  |  |  |  |  `- psycrucifix
|  |  |  |  |  +- psysword
|  |  |  |  |  |  `- psycrucifix
|  |  |  |  |  +- rhomphaia
|  |  |  |  |  |  `- copper
|  |  |  |  |  +- shotel
|  |  |  |  |  |  `- iron
|  |  |  |  |  +- silver
|  |  |  |  |  +- training
|  |  |  |  |  +- triumph
|  |  |  |  |  |  +- psycrucifix
|  |  |  |  |  |  +- rockhill
|  |  |  |  |  |  +- sabreguard
|  |  |  |  |  |  `- wideguard
|  |  |  |  |  +- undivided
|  |  |  |  |  `- zizo
|  |  |  |  +- rapier
|  |  |  |  |  +- aliseo
|  |  |  |  |  +- courtphysician
|  |  |  |  |  +- dec
|  |  |  |  |  +- eora
|  |  |  |  |  +- hand
|  |  |  |  |  +- lord
|  |  |  |  |  +- psy
|  |  |  |  |  |  `- relic
|  |  |  |  |  +- silver
|  |  |  |  |  +- vaquero
|  |  |  |  |  `- wideguard
|  |  |  |  +- saber
|  |  |  |  |  `- iron
|  |  |  |  +- sabre
|  |  |  |  |  +- alloy
|  |  |  |  |  +- bane
|  |  |  |  |  +- banneret
|  |  |  |  |  +- bronzekhopesh
|  |  |  |  |  +- dec
|  |  |  |  |  +- elf
|  |  |  |  |  +- freifechter
|  |  |  |  |  +- hook
|  |  |  |  |  +- mulyeog
|  |  |  |  |  |  +- rumacaptain
|  |  |  |  |  |  `- rumahench
|  |  |  |  |  +- nockhopesh
|  |  |  |  |  +- palloy
|  |  |  |  |  +- shamshir
|  |  |  |  |  |  +- dono_scidragon_flame
|  |  |  |  |  |  `- dono_scidragon_sand
|  |  |  |  |  +- stalker
|  |  |  |  |  `- steppesman
|  |  |  |  +- short
|  |  |  |  |  +- ashort
|  |  |  |  |  +- broken
|  |  |  |  |  +- elvish
|  |  |  |  |  +- falchion
|  |  |  |  |  +- gladius
|  |  |  |  |  |  +- agladius
|  |  |  |  |  |  +- decorated
|  |  |  |  |  |  `- pagladius
|  |  |  |  |  +- gronn
|  |  |  |  |  +- iron
|  |  |  |  |  |  `- chipped
|  |  |  |  |  +- kazengun
|  |  |  |  |  +- messer
|  |  |  |  |  |  +- alt
|  |  |  |  |  |  +- bronze
|  |  |  |  |  |  +- copper
|  |  |  |  |  |  +- duelist
|  |  |  |  |  |  `- iron
|  |  |  |  |  |     `- virtue
|  |  |  |  |  +- pashortsword
|  |  |  |  |  +- psy
|  |  |  |  |  `- silver
|  |  |  |  +- silver
|  |  |  |  |  `- decorated
|  |  |  |  `- stone
|  |  |  +- thresher
|  |  |  |  +- aalloy
|  |  |  |  `- bronze
|  |  |  +- tongs
|  |  |  |  +- aalloy
|  |  |  |  +- blacksteel
|  |  |  |  +- bronze
|  |  |  |  `- stone
|  |  |  +- wand
|  |  |  |  +- aisu
|  |  |  |  +- grand
|  |  |  |  `- greater
|  |  |  +- werewolf_claw
|  |  |  |  +- gnoll
|  |  |  |  |  +- left
|  |  |  |  |  `- right
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  +- whip
|  |  |  |  +- antique
|  |  |  |  |  `- psywhip
|  |  |  |  +- bronze
|  |  |  |  |  `- triumph
|  |  |  |  +- nagaika
|  |  |  |  +- psywhip_lesser
|  |  |  |  +- silver
|  |  |  |  |  `- triumph
|  |  |  |  +- spiderwhip
|  |  |  |  +- triumph
|  |  |  |  `- xylix
|  |  |  +- wolf_claw
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  `- woodstaff
|  |  |     +- aries
|  |  |     +- implement
|  |  |     |  +- grand
|  |  |     |  |  +- blacksteel
|  |  |     |  |  +- magos
|  |  |     |  |  `- naledi
|  |  |     |  `- greater
|  |  |     |     `- blacksteel
|  |  |     +- militia
|  |  |     +- polearm
|  |  |     +- quarterstaff
|  |  |     |  +- gold
|  |  |     |  +- iron
|  |  |     |  +- psy
|  |  |     |  +- silver
|  |  |     |  `- steel
|  |  |     `- wise
|  |  +- rope
|  |  |  +- chain
|  |  |  |  `- bindingshackles
|  |  |  |     +- t2
|  |  |  |     +- t3
|  |  |  |     +- t4
|  |  |  |     `- t5
|  |  |  `- inqarticles
|  |  |     `- inquirycord
|  |  +- rotation_contraption
|  |  |  +- cog
|  |  |  +- debug_source
|  |  |  +- horizontal
|  |  |  +- large_cog
|  |  |  +- minecart_rail
|  |  |  |  `- railbreak
|  |  |  +- roller
|  |  |  +- shaft
|  |  |  +- vertical
|  |  |  `- waterwheel
|  |  +- rune
|  |  |  `- spell
|  |  |     +- air_rune
|  |  |     +- blank_rune
|  |  |     +- earth_rune
|  |  |     +- fire_rune
|  |  |     `- water_rune
|  |  +- runicflask
|  |  |  `- charged
|  |  +- satchel_bomb
|  |  |  `- mega
|  |  +- scomstone
|  |  |  +- bad
|  |  |  |  `- garrison
|  |  |  `- garrison
|  |  |     `- hand
|  |  +- scrap
|  |  +- scrying
|  |  +- seeds
|  |  |  +- apple
|  |  |  +- berryrogue
|  |  |  |  `- poison
|  |  |  +- blackberry
|  |  |  +- cabbage
|  |  |  +- carrot
|  |  |  +- coffee
|  |  |  +- eggplant
|  |  |  +- fyritius
|  |  |  +- garlick
|  |  |  +- lemon
|  |  |  +- lime
|  |  |  +- nut
|  |  |  +- onion
|  |  |  +- pear
|  |  |  +- pipeweed
|  |  |  +- plum
|  |  |  +- poppy
|  |  |  +- potato
|  |  |  +- pumpkin
|  |  |  +- raspberry
|  |  |  +- rice
|  |  |  +- strawberry
|  |  |  +- sugarcane
|  |  |  +- sunflower
|  |  |  +- swampweed
|  |  |  +- tangerine
|  |  |  +- tea
|  |  |  +- tomato
|  |  |  +- turnip
|  |  |  `- wheat
|  |  |     `- oat
|  |  +- shaft
|  |  |  +- metal
|  |  |  +- reinforced
|  |  |  `- wood
|  |  +- sharpener
|  |  |  `- super
|  |  +- showpiece_dummy
|  |  +- signal_horn
|  |  +- skillbook
|  |  |  `- unfinished
|  |  +- skull
|  |  +- smallDelivery
|  |  +- smokeshell
|  |  +- soap
|  |  |  `- bath
|  |  +- soulthread
|  |  |  `- deathsdoor
|  |  +- speakerinq
|  |  +- spellbook_unfinished
|  |  |  `- pre_arcyne
|  |  +- staff
|  |  |  `- stick
|  |  +- storage
|  |  |  +- backpack
|  |  |  |  `- rogue
|  |  |  |     +- artibackpack
|  |  |  |     +- backpack
|  |  |  |     |  `- bagpack
|  |  |  |     `- satchel
|  |  |  |        +- beltpack
|  |  |  |        +- black
|  |  |  |        +- cloth
|  |  |  |        +- heartfelt
|  |  |  |        +- otavan
|  |  |  |        `- short
|  |  |  +- bag
|  |  |  |  `- tray
|  |  |  |     `- psy
|  |  |  +- belt
|  |  |  |  `- rogue
|  |  |  |     +- leather
|  |  |  |     |  +- battleskirt
|  |  |  |     |  |  +- barbarian
|  |  |  |     |  |  +- black
|  |  |  |     |  |  +- breechcloth
|  |  |  |     |  |  |  +- blackbelt
|  |  |  |     |  |  |  `- red
|  |  |  |     |  |  +- faulds
|  |  |  |     |  |  |  `- red
|  |  |  |     |  |  `- red
|  |  |  |     |  +- black
|  |  |  |     |  +- cloth
|  |  |  |     |  |  +- bandit
|  |  |  |     |  |  `- lady
|  |  |  |     |  +- cloth_belt
|  |  |  |     |  +- double
|  |  |  |     |  +- knifebelt
|  |  |  |     |  |  `- black
|  |  |  |     |  +- plaquegold
|  |  |  |     |  |  `- steward
|  |  |  |     |  +- plaquesilver
|  |  |  |     |  +- rope
|  |  |  |     |  |  `- dark
|  |  |  |     |  +- sash
|  |  |  |     |  |  `- maid
|  |  |  |     |  +- shalal
|  |  |  |     |  |  `- purple
|  |  |  |     |  +- silkbelt
|  |  |  |     |  +- slayer
|  |  |  |     |  +- steel
|  |  |  |     |  |  `- tasset
|  |  |  |     |  +- suspenders
|  |  |  |     |  `- zig_bandolier
|  |  |  |     +- pouch
|  |  |  |     |  +- alchemy
|  |  |  |     |  +- cloth
|  |  |  |     |  +- coins
|  |  |  |     |  |  +- aalloy
|  |  |  |     |  |  `- poor
|  |  |  |     |  +- healing
|  |  |  |     |  +- medicine
|  |  |  |     |  +- merchant
|  |  |  |     |  +- tailorscrap
|  |  |  |     |  +- triumphlunch
|  |  |  |     |  `- zigarrete
|  |  |  |     `- surgery_bag
|  |  |  |        +- empty
|  |  |  |        `- full
|  |  |  |           `- physician
|  |  |  +- book
|  |  |  +- fancy
|  |  |  |  +- candle_box
|  |  |  |  +- cigarettes
|  |  |  |  |  `- zig
|  |  |  |  |     `- empty
|  |  |  |  `- egg_box
|  |  |  +- gadget
|  |  |  |  `- messkit
|  |  |  +- hip
|  |  |  |  +- headhook
|  |  |  |  |  `- bronze
|  |  |  |  `- orestore
|  |  |  |     `- bronze
|  |  |  +- keyring
|  |  |  |  +- acolyte
|  |  |  |  +- apothecary
|  |  |  |  +- apprentice
|  |  |  |  +- archivist
|  |  |  |  +- bathmaster
|  |  |  |  +- church
|  |  |  |  +- guildmaster
|  |  |  |  +- heir
|  |  |  |  +- innfancyi
|  |  |  |  +- innfancyii
|  |  |  |  +- innfancyiii
|  |  |  |  +- innfancyiv
|  |  |  |  +- innfancyv
|  |  |  |  +- innhunt
|  |  |  |  +- innkeep
|  |  |  |  +- innkeep_rooms
|  |  |  |  +- inquisitor
|  |  |  |  +- jester
|  |  |  |  +- keeper
|  |  |  |  +- knight
|  |  |  |  +- lady
|  |  |  |  +- lord
|  |  |  |  +- magician
|  |  |  |  +- manatarms
|  |  |  |  +- manor
|  |  |  |  |  `- guest
|  |  |  |  |     +- four
|  |  |  |  |     +- one
|  |  |  |  |     +- three
|  |  |  |  |     `- two
|  |  |  |  +- marshal
|  |  |  |  +- merchant
|  |  |  |  +- physician
|  |  |  |  +- seneschal
|  |  |  |  +- sergeant
|  |  |  |  +- soilson
|  |  |  |  +- squire
|  |  |  |  +- steward
|  |  |  |  +- tailor
|  |  |  |  +- vampire
|  |  |  |  `- warden
|  |  |  +- magebag
|  |  |  |  +- associate
|  |  |  |  `- starter
|  |  |  +- meatbag
|  |  |  +- pill_bottle
|  |  |  |  `- dice
|  |  |  |     +- farkle
|  |  |  |     `- hazard
|  |  |  `- roguebag
|  |  |     +- ash
|  |  |     +- crafted
|  |  |     +- farmer_berries
|  |  |     +- farmer_fruits
|  |  |     +- farmer_rocknut
|  |  |     +- farmer_smokes
|  |  |     +- food
|  |  |     `- leechbait
|  |  +- tablecloth
|  |  |  `- silk
|  |  +- target
|  |  |  +- alien
|  |  |  |  `- anchored
|  |  |  +- clown
|  |  |  `- syndicate
|  |  +- taster
|  |  +- teleportation_scroll
|  |  |  `- apprentice
|  |  +- tent_kit
|  |  |  +- ger
|  |  |  `- yurt
|  |  +- thetoll
|  |  +- throwing_star
|  |  |  `- ninja
|  |  +- tk_grab
|  |  +- tntstick
|  |  +- toy
|  |  |  +- cards
|  |  |  |  +- cardhand
|  |  |  |  +- deck
|  |  |  |  |  +- syndicate
|  |  |  |  |  `- tarot
|  |  |  |  `- singlecard
|  |  |  `- snappop
|  |  |     `- phoenix
|  |  +- trash
|  |  |  +- applecore
|  |  |  +- candle
|  |  |  +- gapplecore
|  |  |  +- pistachios
|  |  |  `- plate
|  |  +- tripwire
|  |  +- twohanded
|  |  |  `- required
|  |  |     `- kirbyplants
|  |  |        +- dead
|  |  |        +- photosynthetic
|  |  |        `- random
|  |  +- twstrap
|  |  |  `- bombstrap
|  |  +- udder
|  |  +- underworld
|  |  |  `- coin
|  |  |     `- notracking
|  |  `- undies
|  |     +- athletic_leotard
|  |     +- bikini
|  |     +- braies
|  |     +- briefs_eoran
|  |     +- leotard
|  |     `- panties
|  +- machinery
|  |  +- anvil
|  |  |  +- bronze
|  |  |  `- crafted
|  |  +- artificer_table
|  |  +- gear_painter
|  |  +- light
|  |  |  +- broken
|  |  |  +- built
|  |  |  +- floor
|  |  |  +- oldlight
|  |  |  +- rogue
|  |  |  |  +- campfire
|  |  |  |  |  +- create_campfire
|  |  |  |  |  +- densefire
|  |  |  |  |  +- fireplace
|  |  |  |  |  +- longlived
|  |  |  |  |  `- pyre
|  |  |  |  +- candle
|  |  |  |  |  +- blue
|  |  |  |  |  |  +- l
|  |  |  |  |  |  `- r
|  |  |  |  |  +- floorcandle
|  |  |  |  |  |  +- alt
|  |  |  |  |  |  |  `- pink
|  |  |  |  |  |  `- pink
|  |  |  |  |  +- l
|  |  |  |  |  +- off
|  |  |  |  |  |  +- l
|  |  |  |  |  |  `- r
|  |  |  |  |  +- r
|  |  |  |  |  `- weak
|  |  |  |  |     +- l
|  |  |  |  |     `- r
|  |  |  |  +- cauldron
|  |  |  |  |  `- folding
|  |  |  |  +- chand
|  |  |  |  +- firebowl
|  |  |  |  |  +- church
|  |  |  |  |  |  `- off
|  |  |  |  |  +- off
|  |  |  |  |  +- standing
|  |  |  |  |  |  `- blue
|  |  |  |  |  `- stump
|  |  |  |  +- forge
|  |  |  |  |  `- arcane
|  |  |  |  +- hearth
|  |  |  |  |  +- conjured
|  |  |  |  |  `- mobilestove
|  |  |  |  +- lanternpost
|  |  |  |  +- oven
|  |  |  |  |  +- center
|  |  |  |  |  +- conjured
|  |  |  |  |  +- east
|  |  |  |  |  +- north
|  |  |  |  |  +- south
|  |  |  |  |  `- west
|  |  |  |  +- smelter
|  |  |  |  |  +- bronze
|  |  |  |  |  +- great
|  |  |  |  |  `- hiron
|  |  |  |  `- torchholder
|  |  |  |     +- c
|  |  |  |     +- hotspring
|  |  |  |     |  `- standing
|  |  |  |     +- l
|  |  |  |     `- r
|  |  |  +- roguestreet
|  |  |  |  `- midlamp
|  |  |  `- small
|  |  |     +- broken
|  |  |     `- built
|  |  +- loom
|  |  +- tanningrack
|  |  `- tram_controls
|  +- merge_conflict_marker
|  +- particle_emitter
|  |  `- smoke
|  +- projectile
|  |  +- bullet
|  |  |  +- arrow
|  |  |  |  +- elemental
|  |  |  |  |  +- fire
|  |  |  |  |  +- frost
|  |  |  |  |  +- kinetic
|  |  |  |  |  +- splinter
|  |  |  |  |  `- thunder
|  |  |  |  `- water
|  |  |  +- bolt
|  |  |  |  +- pyro
|  |  |  |  `- water
|  |  |  +- reusable
|  |  |  |  +- arrow
|  |  |  |  |  +- ancient
|  |  |  |  |  +- blunt
|  |  |  |  |  +- bronze
|  |  |  |  |  +- iron
|  |  |  |  |  |  `- aalloy
|  |  |  |  |  +- orc
|  |  |  |  |  +- poison
|  |  |  |  |  |  `- stone
|  |  |  |  |  +- silver
|  |  |  |  |  +- steel
|  |  |  |  |  |  `- paalloy
|  |  |  |  |  `- stone
|  |  |  |  |     `- wall_projectile
|  |  |  |  +- bolt
|  |  |  |  |  +- aalloy
|  |  |  |  |  +- blunt
|  |  |  |  |  +- bronze
|  |  |  |  |  +- holy
|  |  |  |  |  +- light
|  |  |  |  |  +- paalloy
|  |  |  |  |  `- silver
|  |  |  |  +- bullet
|  |  |  |  +- deepone
|  |  |  |  +- heavy_bolt
|  |  |  |  |  +- aalloy
|  |  |  |  |  +- blunt
|  |  |  |  |  +- bronze
|  |  |  |  |  +- paalloy
|  |  |  |  |  `- silver
|  |  |  |  `- sling_bullet
|  |  |  |     +- aalloy
|  |  |  |     +- bronze
|  |  |  |     +- heavy_sling_bullet
|  |  |  |     +- iron
|  |  |  |     +- paalloy
|  |  |  |     `- stone
|  |  |  +- sling_bullet
|  |  |  |  +- fire_pot
|  |  |  |  `- scattershot
|  |  |  +- spider
|  |  |  `- spider_shroom
|  |  +- discharge
|  |  +- earthenchunk
|  |  +- energy
|  |  |  +- airblade
|  |  |  |  +- blunt
|  |  |  |  `- stab
|  |  |  +- arcynestrike
|  |  |  |  +- blunt
|  |  |  |  `- stab
|  |  |  +- azurean_pilum
|  |  |  |  +- arc
|  |  |  |  `- empowered
|  |  |  |     `- arc
|  |  |  +- divineblast
|  |  |  |  `- arc
|  |  |  +- rogue3
|  |  |  +- stygian
|  |  |  |  `- arc
|  |  |  `- unholyblast
|  |  |     `- arc
|  |  `- magic
|  |     +- acidsplash
|  |     |  +- quietus
|  |     |  `- wall_projectile
|  |     +- antimagic
|  |     +- aoe
|  |     |  +- dragon_breath
|  |     |  `- fireball
|  |     |     +- infernal
|  |     |     `- rogue
|  |     |        +- arc
|  |     |        +- artillery
|  |     |        |  `- arc
|  |     |        `- great
|  |     |           +- arc
|  |     |           `- lich
|  |     +- arc_bolt
|  |     |  `- arc
|  |     +- arcane_barrage
|  |     +- arcyne_lance
|  |     |  `- arc
|  |     +- baroness
|  |     |  `- lightning
|  |     +- blade_storm
|  |     +- bloodlightning
|  |     +- bloodsteal
|  |     +- blowingdust
|  |     |  +- moondust
|  |     |  +- spice
|  |     |  `- starsugar
|  |     +- boulder
|  |     |  `- arc
|  |     +- bounty
|  |     +- death
|  |     +- fetch
|  |     +- firebolt
|  |     +- flying
|  |     +- frostbolt
|  |     |  +- arc
|  |     |  +- Baroness
|  |     |  +- greater
|  |     |  `- wall_projectile
|  |     +- gravel_blast
|  |     |  `- arc
|  |     +- greater_arcyne_bolt
|  |     |  `- arc
|  |     +- ice_burst
|  |     |  `- arc
|  |     +- iron_tempest_seed
|  |     +- lesser_fetch
|  |     +- lesser_repel
|  |     +- lich
|  |     |  `- lightning
|  |     +- lightning
|  |     +- locker
|  |     +- mockery_note
|  |     +- necropotence
|  |     +- profane
|  |     |  `- major
|  |     +- repel
|  |     +- resurrection
|  |     +- sacred_flame
|  |     +- safety
|  |     +- sapping
|  |     +- sawblade
|  |     +- sickness
|  |     |  `- lich
|  |     +- soulshot
|  |     +- spell
|  |     +- spellblade
|  |     +- spitfire
|  |     |  `- arc
|  |     +- teleport
|  |     +- unholy_grasp
|  |     `- zardman_jailer_mage
|  |        `- lightning
|  +- random
|  |  +- loot
|  |  |  `- spider_cave
|  |  `- spider
|  +- shapeshift_holder
|  +- structure
|  |  +- active_abyssor_rune
|  |  |  +- greater
|  |  |  `- tidal
|  |  +- apiary
|  |  |  `- starter
|  |  +- arcyne_wall
|  |  |  +- caster
|  |  |  `- greater
|  |  |     `- caster
|  |  +- arrow_ward
|  |  +- ascendant_altar
|  |  +- autosmither
|  |  +- barricade
|  |  |  +- crude
|  |  |  |  `- snow
|  |  |  `- rogue
|  |  |     `- crude
|  |  +- bars
|  |  |  +- cemetery
|  |  |  +- chainlink
|  |  |  +- grille
|  |  |  +- passage
|  |  |  |  +- shutter
|  |  |  |  |  `- open
|  |  |  |  `- steel
|  |  |  +- pipe
|  |  |  |  `- left
|  |  |  +- shop
|  |  |  |  `- bronze
|  |  |  +- steel
|  |  |  `- tough
|  |  +- bearpelt
|  |  +- bed
|  |  |  `- rogue
|  |  |     +- bedroll
|  |  |     +- conjured
|  |  |     +- inn
|  |  |     |  +- double
|  |  |     |  +- hay
|  |  |     |  +- pileofshit
|  |  |     |  +- wool
|  |  |     |  `- wooldouble
|  |  |     `- shit
|  |  +- beehive
|  |  |  `- wild
|  |  +- bell_barrier
|  |  +- boatbell
|  |  +- bobcatpelt
|  |  +- bonepile
|  |  +- bookcase
|  |  |  +- random
|  |  |  |  +- adult
|  |  |  |  +- archive
|  |  |  |  +- fiction
|  |  |  |  +- nonfiction
|  |  |  |  +- reference
|  |  |  |  `- religion
|  |  |  `- random_recipes
|  |  +- broadcast_horn
|  |  |  +- loudmouth
|  |  |  |  `- guest
|  |  |  `- paid
|  |  +- chair
|  |  |  +- arrestchair
|  |  |  +- bench
|  |  |  |  +- church
|  |  |  |  |  +- mid
|  |  |  |  |  +- r
|  |  |  |  |  `- smallbench
|  |  |  |  +- couch
|  |  |  |  |  `- r
|  |  |  |  +- coucha
|  |  |  |  |  `- r
|  |  |  |  +- couchablack
|  |  |  |  |  `- r
|  |  |  |  +- couchamagenta
|  |  |  |  |  `- r
|  |  |  |  `- ultimacouch
|  |  |  |     `- r
|  |  |  +- comfy
|  |  |  |  +- beige
|  |  |  |  +- black
|  |  |  |  +- brown
|  |  |  |  +- lime
|  |  |  |  +- shuttle
|  |  |  |  `- teal
|  |  |  +- frankenstein
|  |  |  |  `- zizo
|  |  |  +- freedomchair
|  |  |  |  `- crafted
|  |  |  +- greyscale
|  |  |  +- hotspring_bench
|  |  |  |  +- corner
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  +- mime
|  |  |  +- office
|  |  |  |  `- light
|  |  |  +- stool
|  |  |  |  +- bar
|  |  |  |  `- rogue
|  |  |  `- wood
|  |  |     +- rogue
|  |  |     |  +- chair3
|  |  |     |  +- chair4
|  |  |     |  +- chair5
|  |  |     |  +- fancy
|  |  |     |  `- throne
|  |  |     `- wings
|  |  +- closet
|  |  |  +- body_bag
|  |  |  +- burial_shroud
|  |  |  +- crate
|  |  |  |  +- chest
|  |  |  |  |  +- autosmither
|  |  |  |  |  +- coffinlootbox
|  |  |  |  |  +- coffinlootbox_high
|  |  |  |  |  +- coffinlootbox_middle
|  |  |  |  |  +- crafted
|  |  |  |  |  +- crate
|  |  |  |  |  +- gold
|  |  |  |  |  +- inqarmory
|  |  |  |  |  +- inqcrate
|  |  |  |  |  +- inqreliquary
|  |  |  |  |  +- loot_chest
|  |  |  |  |  |  `- locked
|  |  |  |  |  |     `- indestructible
|  |  |  |  |  +- merchant
|  |  |  |  |  +- neu
|  |  |  |  |  +- neu_fancy
|  |  |  |  |  +- neu_iron
|  |  |  |  |  +- old_crate
|  |  |  |  |  |  +- apoth_initial_pot
|  |  |  |  |  |  `- apothseed
|  |  |  |  |  +- steward
|  |  |  |  |  +- trapped
|  |  |  |  |  |  `- locked
|  |  |  |  |  `- wicker
|  |  |  |  |     `- bait
|  |  |  |  +- coffin
|  |  |  |  |  +- keylock
|  |  |  |  |  |  `- psydung
|  |  |  |  |  +- royal
|  |  |  |  |  |  `- keylock
|  |  |  |  |  |     `- psydon
|  |  |  |  |  `- vampire
|  |  |  |  +- drawer
|  |  |  |  |  +- inn
|  |  |  |  |  `- random
|  |  |  |  +- miningcar
|  |  |  |  `- roguecloset
|  |  |  |     +- crafted
|  |  |  |     +- dark
|  |  |  |     +- inn
|  |  |  |     |  +- chest
|  |  |  |     |  `- south
|  |  |  |     `- lord
|  |  |  |        `- duke_preset
|  |  |  +- decay
|  |  |  +- dirthole
|  |  |  |  +- closed
|  |  |  |  |  `- loot
|  |  |  |  `- grave
|  |  |  `- supplypod
|  |  |     +- bluespacepod
|  |  |     +- centcompod
|  |  |     `- extractionpod
|  |  +- composter
|  |  |  +- full
|  |  |  `- halffull
|  |  +- crabnest
|  |  +- crystal_spire
|  |  |  +- greater
|  |  |  `- tidal
|  |  +- curtain
|  |  |  +- black
|  |  |  +- blue
|  |  |  +- bounty
|  |  |  +- brown
|  |  |  +- green
|  |  |  +- magenta
|  |  |  +- purple
|  |  |  `- red
|  |  +- deaths_door_portal
|  |  +- deaths_door_shrine
|  |  +- debug_rotation_source
|  |  +- displaycase
|  |  |  `- trophy
|  |  +- dungeon_entry
|  |  |  +- center
|  |  |  `- hamlet
|  |  +- dungeon_exit
|  |  +- dungeontool
|  |  |  +- mover
|  |  |  +- trigger
|  |  |  `- triggered
|  |  |     +- barracksalert
|  |  |     +- invisibleshutterclosed
|  |  |     `- thiefdaddmobs
|  |  +- earthen_pillar
|  |  +- earthen_wall
|  |  +- easel
|  |  +- englauncher
|  |  +- eoran_pomegranate_tree
|  |  +- etherealball
|  |  +- far_travel
|  |  +- feedinghole
|  |  +- fence
|  |  |  +- corner
|  |  |  +- cut
|  |  |  |  +- large
|  |  |  |  `- medium
|  |  |  +- door
|  |  |  |  `- opened
|  |  |  +- end
|  |  |  `- post
|  |  +- fermentation_keg
|  |  |  +- avarrice
|  |  |  +- beer
|  |  |  +- blackgoat
|  |  |  +- coffee
|  |  |  +- crafted
|  |  |  +- distiller
|  |  |  +- gronmead
|  |  |  +- hagwoodbitter
|  |  |  +- jagt
|  |  |  +- kgsunsake
|  |  |  +- onion
|  |  |  +- random
|  |  |  |  `- water
|  |  |  +- redwine
|  |  |  +- rose_tea
|  |  |  +- saigamilk
|  |  |  +- sourwine
|  |  |  +- spicedwine
|  |  |  +- spicedwineaged
|  |  |  +- spicedwinedelectable
|  |  |  +- tea
|  |  |  +- water
|  |  |  +- whitewine
|  |  |  +- zagul
|  |  |  `- zarum
|  |  +- fireaxecabinet
|  |  |  +- south
|  |  |  `- unforgotten
|  |  |     `- south
|  |  +- flagpole
|  |  +- floordoor
|  |  |  +- gatehatch
|  |  |  |  +- inner
|  |  |  |  `- outer
|  |  |  `- open
|  |  +- flora
|  |  |  +- ausbushes
|  |  |  |  +- brflowers
|  |  |  |  +- fernybush
|  |  |  |  +- fullgrass
|  |  |  |  +- genericbush
|  |  |  |  +- grassybush
|  |  |  |  +- lavendergrass
|  |  |  |  +- leafybush
|  |  |  |  +- palebush
|  |  |  |  +- pointybush
|  |  |  |  +- ppflowers
|  |  |  |  +- reedbush
|  |  |  |  +- sparsegrass
|  |  |  |  +- stalkybush
|  |  |  |  +- sunnybush
|  |  |  |  `- ywflowers
|  |  |  +- bush
|  |  |  +- grass
|  |  |  |  +- both
|  |  |  |  +- brown
|  |  |  |  +- green
|  |  |  |  +- jungle
|  |  |  |  |  `- b
|  |  |  |  `- tangler
|  |  |  |     `- real
|  |  |  +- hotspring_rocks
|  |  |  |  +- grassy
|  |  |  |  `- small
|  |  |  |     +- five
|  |  |  |     +- four
|  |  |  |     +- three
|  |  |  |     `- two
|  |  |  +- junglebush
|  |  |  |  +- b
|  |  |  |  +- c
|  |  |  |  `- large
|  |  |  +- mushroomcluster
|  |  |  |  `- cute
|  |  |  +- newbranch
|  |  |  |  +- connector
|  |  |  |  `- leafless
|  |  |  +- newleaf
|  |  |  |  `- corner
|  |  |  +- newtree
|  |  |  +- rock
|  |  |  |  +- jungle
|  |  |  |  `- pile
|  |  |  |     `- largejungle
|  |  |  +- rogueflora
|  |  |  |  +- marigold
|  |  |  |  +- nettles
|  |  |  |  +- poppy
|  |  |  |  +- thistle
|  |  |  |  `- wormwood
|  |  |  +- roguegrass
|  |  |  |  +- bush
|  |  |  |  |  +- wall
|  |  |  |  |  |  `- tall
|  |  |  |  |  `- westleach
|  |  |  |  +- herb
|  |  |  |  |  +- artemisia
|  |  |  |  |  +- atropa
|  |  |  |  |  +- benedictus
|  |  |  |  |  +- calendula
|  |  |  |  |  +- euphrasia
|  |  |  |  |  +- hypericum
|  |  |  |  |  +- manabloom
|  |  |  |  |  +- matricaria
|  |  |  |  |  +- mentha
|  |  |  |  |  +- paris
|  |  |  |  |  +- random
|  |  |  |  |  +- rosa
|  |  |  |  |  +- salvia
|  |  |  |  |  +- symphitum
|  |  |  |  |  +- taraxacum
|  |  |  |  |  +- urtica
|  |  |  |  |  `- valeriana
|  |  |  |  +- maneater
|  |  |  |  |  `- real
|  |  |  |  |     `- juvenile
|  |  |  |  +- pumpkin
|  |  |  |  +- pyroclasticflowers
|  |  |  |  +- swampweed
|  |  |  |  +- thorn_bush
|  |  |  |  `- water
|  |  |  |     `- reeds
|  |  |  +- rogueshroom
|  |  |  |  `- happy
|  |  |  |     +- angel
|  |  |  |     +- fat
|  |  |  |     +- metal
|  |  |  |     +- random
|  |  |  |     `- white
|  |  |  +- roguetree
|  |  |  |  +- burnt
|  |  |  |  +- evil
|  |  |  |  +- pine
|  |  |  |  |  `- dead
|  |  |  |  +- stump
|  |  |  |  |  +- burnt
|  |  |  |  |  +- log
|  |  |  |  |  `- pine
|  |  |  |  +- underworld
|  |  |  |  `- wise
|  |  |  +- sakura
|  |  |  +- shroomstump
|  |  |  +- stump
|  |  |  +- tinymushrooms
|  |  |  |  `- cute
|  |  |  `- tree
|  |  |     +- dead
|  |  |     +- evil
|  |  |     +- jungle
|  |  |     |  `- small
|  |  |     `- palm
|  |  +- fluff
|  |  |  +- alch
|  |  |  |  `- folding
|  |  |  +- arc
|  |  |  +- beach_umbrella
|  |  |  |  +- cap
|  |  |  |  +- engine
|  |  |  |  +- science
|  |  |  |  +- security
|  |  |  |  `- syndi
|  |  |  +- big_chain
|  |  |  +- buysign
|  |  |  +- canopy
|  |  |  |  +- booth
|  |  |  |  |  +- booth02
|  |  |  |  |  +- booth_green
|  |  |  |  |  `- booth_green02
|  |  |  |  `- green
|  |  |  +- ceramicswheel
|  |  |  +- clock
|  |  |  +- clockwork
|  |  |  |  +- alloy_shards
|  |  |  |  |  +- large
|  |  |  |  |  +- medium
|  |  |  |  |  +- medium_gearbit
|  |  |  |  |  `- small
|  |  |  |  +- blind_eye
|  |  |  |  +- clockgolem_remains
|  |  |  |  `- fallen_armor
|  |  |  +- clodpile
|  |  |  +- customsign
|  |  |  +- divine
|  |  |  |  +- conduit
|  |  |  |  +- convertaltar
|  |  |  |  +- defensepylon
|  |  |  |  +- nexus
|  |  |  |  +- powerpylon
|  |  |  |  `- shrine
|  |  |  +- drake_statue
|  |  |  |  `- falling
|  |  |  +- grindwheel
|  |  |  +- headstake
|  |  |  +- helljailer
|  |  |  +- littlebanners
|  |  |  |  +- bluered
|  |  |  |  +- bluewhite
|  |  |  |  +- greenblue
|  |  |  |  +- greenred
|  |  |  |  `- greenwhite
|  |  |  +- nest
|  |  |  +- paper
|  |  |  |  +- corner
|  |  |  |  `- stack
|  |  |  +- pillow
|  |  |  |  +- black
|  |  |  |  +- blue
|  |  |  |  +- brown
|  |  |  |  +- green
|  |  |  |  +- magenta
|  |  |  |  +- purple
|  |  |  |  `- red
|  |  |  +- psycross
|  |  |  |  +- baotha
|  |  |  |  |  `- decorated
|  |  |  |  +- copper
|  |  |  |  +- crafted
|  |  |  |  +- fog
|  |  |  |  +- graggar
|  |  |  |  |  `- decorated
|  |  |  |  +- matthios
|  |  |  |  |  `- decorated
|  |  |  |  +- necra
|  |  |  |  |  +- cloth
|  |  |  |  |  `- consecrated
|  |  |  |  +- psycrucifix
|  |  |  |  |  +- silver
|  |  |  |  |  `- stone
|  |  |  |  `- zizocross
|  |  |  |     +- golden
|  |  |  |     `- stone
|  |  |  +- psyexit
|  |  |  +- railing
|  |  |  |  +- border
|  |  |  |  |  +- east
|  |  |  |  |  +- north
|  |  |  |  |  `- west
|  |  |  |  +- corner
|  |  |  |  |  +- north_east
|  |  |  |  |  +- south_east
|  |  |  |  |  `- south_west
|  |  |  |  +- fence
|  |  |  |  +- stonehedge
|  |  |  |  `- wood
|  |  |  |     +- east
|  |  |  |     +- north
|  |  |  |     `- west
|  |  |  +- ravox
|  |  |  |  +- challenged
|  |  |  |  `- challenger
|  |  |  +- sellsign
|  |  |  +- signage
|  |  |  +- statue
|  |  |  |  +- aasimar
|  |  |  |  +- abyssor
|  |  |  |  |  `- dolomite
|  |  |  |  +- astrata
|  |  |  |  |  `- gold
|  |  |  |  +- evil
|  |  |  |  +- femalestatue
|  |  |  |  |  `- zizo
|  |  |  |  +- femalestatue1
|  |  |  |  +- femalestatue2
|  |  |  |  +- gargoyle
|  |  |  |  |  +- candles
|  |  |  |  |  `- moss
|  |  |  |  |     `- candles
|  |  |  |  +- knight
|  |  |  |  |  +- interior
|  |  |  |  |  |  `- r
|  |  |  |  |  |     `- bronze
|  |  |  |  |  `- r
|  |  |  |  +- knightalt
|  |  |  |  |  `- r
|  |  |  |  +- myth
|  |  |  |  +- pillar
|  |  |  |  +- psy
|  |  |  |  +- psybloody
|  |  |  |  +- scare
|  |  |  |  +- small
|  |  |  |  +- spider
|  |  |  |  `- tdummy
|  |  |  +- testportal
|  |  |  +- traveltile
|  |  |  |  +- bandit
|  |  |  |  +- bathhouse_passage
|  |  |  |  |  `- cave
|  |  |  |  +- drow
|  |  |  |  +- dungeon
|  |  |  |  +- eventarea
|  |  |  |  |  `- multiz
|  |  |  |  +- vampire
|  |  |  |  `- wretch
|  |  |  +- wallclock
|  |  |  |  +- l
|  |  |  |  +- r
|  |  |  |  `- vampire
|  |  |  |     +- l
|  |  |  |     `- r
|  |  |  `- walldeco
|  |  |     +- alarm
|  |  |     +- artificerflag
|  |  |     +- barbersign
|  |  |     +- barbersignreverse
|  |  |     +- bath
|  |  |     |  +- five
|  |  |     |  +- four
|  |  |     |  +- gents
|  |  |     |  +- ladies
|  |  |     |  +- seven
|  |  |     |  +- six
|  |  |     |  +- three
|  |  |     |  +- two
|  |  |     |  `- wallrope
|  |  |     +- bigpainting
|  |  |     |  `- lake
|  |  |     +- bsmith
|  |  |     +- chains
|  |  |     +- church
|  |  |     |  `- line
|  |  |     +- customflag
|  |  |     +- flower
|  |  |     +- goblet
|  |  |     +- innsign
|  |  |     +- mageguild
|  |  |     +- mageguild2
|  |  |     +- maidendrape
|  |  |     +- maidensigil
|  |  |     |  `- r
|  |  |     +- med
|  |  |     +- med2
|  |  |     +- med3
|  |  |     +- med4
|  |  |     +- med5
|  |  |     +- med6
|  |  |     +- mona
|  |  |     +- moon
|  |  |     +- painting
|  |  |     |  +- queen
|  |  |     |  +- seraphina
|  |  |     |  `- skull
|  |  |     +- psybanner
|  |  |     |  `- red
|  |  |     +- rpainting
|  |  |     |  +- crown
|  |  |     |  `- forest
|  |  |     +- serpflag
|  |  |     +- sign
|  |  |     |  +- merchantsign
|  |  |     |  |  `- left
|  |  |     |  +- saiga
|  |  |     |  |  `- left
|  |  |     |  `- trophy
|  |  |     +- sparrowflag
|  |  |     +- steward
|  |  |     +- stone
|  |  |     |  +- bronze
|  |  |     |  +- stone2
|  |  |     |  +- stone3
|  |  |     |  +- stone4
|  |  |     |  +- stone5
|  |  |     |  `- stone6
|  |  |     +- vinez
|  |  |     |  +- blue
|  |  |     |  +- l
|  |  |     |  +- offset
|  |  |     |  +- r
|  |  |     |  `- red
|  |  |     +- wallshield
|  |  |     +- wantedposter
|  |  |     |  +- l
|  |  |     |  `- r
|  |  |     `- xavo
|  |  +- foamedmetal
|  |  |  `- iron
|  |  +- forcefield_weak
|  |  |  `- shelter_wall
|  |  +- foxpelt
|  |  +- gate
|  |  |  +- bars
|  |  |  |  `- preopen
|  |  |  +- preopen
|  |  |  `- psy_vault
|  |  +- gearbox
|  |  +- giantfur
|  |  |  `- small
|  |  +- globe
|  |  +- glowshroom
|  |  |  `- dendorite
|  |  +- gob_portal
|  |  +- gravemarker
|  |  +- guillotine
|  |  +- handcart
|  |  +- healingfountain
|  |  +- hotspring
|  |  |  `- border
|  |  |     +- eight
|  |  |     +- eleven
|  |  |     +- five
|  |  |     +- four
|  |  |     +- fourteen
|  |  |     +- nine
|  |  |     +- seven
|  |  |     +- six
|  |  |     +- ten
|  |  |     +- thirteen
|  |  |     +- three
|  |  |     +- twelve
|  |  |     `- two
|  |  +- ichor_stone
|  |  +- industrial_lift
|  |  |  +- debug
|  |  |  +- public
|  |  |  `- tram
|  |  +- infernalengine
|  |  +- kitchenspike
|  |  +- kitchenspike_frame
|  |  +- kybraxor
|  |  |  `- psy
|  |  +- ladder
|  |  |  +- earth
|  |  |  `- unbreakable
|  |  +- lever
|  |  |  +- hidden
|  |  |  `- wall
|  |  +- leyline
|  |  |  +- normal
|  |  |  |  +- coast
|  |  |  |  +- decap
|  |  |  |  `- grove
|  |  |  +- powerful
|  |  |  `- tamed
|  |  +- leyline_anchor_tether
|  |  +- life_candle
|  |  +- loot
|  |  |  `- pile
|  |  +- manaflower
|  |  +- mannequin
|  |  |  `- male
|  |  |     +- decorative
|  |  |     |  +- training_dummy_style
|  |  |     |  `- woman
|  |  |     `- female
|  |  +- meathook
|  |  +- minecart_rail
|  |  |  `- railbreak
|  |  +- mineral_door
|  |  |  +- bars
|  |  |  +- barsold
|  |  |  +- secret
|  |  |  +- swing_door
|  |  |  `- wood
|  |  |     +- bath
|  |  |     |  +- bathmaid
|  |  |     |  `- courtesan
|  |  |     +- blue
|  |  |     +- deadbolt
|  |  |     |  +- arcyne
|  |  |     |  |  `- caster
|  |  |     |  `- shutter
|  |  |     +- donjon
|  |  |     |  +- highsecurity
|  |  |     |  `- stone
|  |  |     |     +- broken
|  |  |     |     `- highsecurity
|  |  |     +- fancywood
|  |  |     +- red
|  |  |     +- towner
|  |  |     |  +- blacksmith
|  |  |     |  +- cheesemaker
|  |  |     |  +- fisher
|  |  |     |  +- generic
|  |  |     |  |  `- two_keys
|  |  |     |  +- hunter
|  |  |     |  +- miner
|  |  |     |  +- seamstress
|  |  |     |  +- witch
|  |  |     |  `- woodworker
|  |  |     +- violet
|  |  |     `- window
|  |  +- mirror
|  |  |  +- fancy
|  |  |  `- magic
|  |  +- noose
|  |  |  `- gallows
|  |  +- piano
|  |  |  `- unanchored
|  |  +- pillory
|  |  |  +- crafted
|  |  |  +- double
|  |  |  +- reinforced
|  |  |  `- town
|  |  +- plasticflaps
|  |  |  `- opaque
|  |  +- plough
|  |  +- portal
|  |  +- portal_jaunt
|  |  +- pressure_plate
|  |  +- primal_rift
|  |  +- rack
|  |  |  `- rogue
|  |  |     `- shelf
|  |  |        +- big
|  |  |        +- biggest
|  |  |        `- notdense
|  |  +- reliquarybox
|  |  +- ritualcircle
|  |  |  +- abyssor
|  |  |  +- abyssor_alt
|  |  |  +- abyssor_alt_inactive
|  |  |  +- astrata
|  |  |  +- eora
|  |  |  +- graggar
|  |  |  +- malum
|  |  |  +- matthios
|  |  |  +- necra
|  |  |  +- noc
|  |  |  +- pestra
|  |  |  +- undivided
|  |  |  +- xylix
|  |  |  `- zizo
|  |  +- rogue
|  |  |  `- trophy
|  |  |     `- deer
|  |  +- roguemachine
|  |  |  +- atm
|  |  |  +- balloon_pad
|  |  |  +- bathvend
|  |  |  +- bounty
|  |  |  +- camera
|  |  |  |  +- left
|  |  |  |  `- right
|  |  |  +- chimeric_calyx
|  |  |  +- chimeric_heart_beast
|  |  |  +- chimeric_slab
|  |  |  +- contractledger
|  |  |  +- crier
|  |  |  +- drugmachine
|  |  |  +- goldface
|  |  |  |  +- copperface
|  |  |  |  `- public
|  |  |  |     +- apothecary
|  |  |  |     +- smith
|  |  |  |     +- tailor
|  |  |  |     `- wretch_cat
|  |  |  +- hag_cauldron
|  |  |  +- hag_heart
|  |  |  +- hag_ward
|  |  |  +- headeater
|  |  |  +- hoardbarrier
|  |  |  +- Hoardmaster
|  |  |  +- lottery_roguetown
|  |  |  +- mail
|  |  |  |  +- l
|  |  |  |  +- paired_hermes
|  |  |  |  |  +- bathhouse
|  |  |  |  |  `- cove
|  |  |  |  `- r
|  |  |  +- mazeroot
|  |  |  +- money
|  |  |  |  +- l
|  |  |  |  +- r
|  |  |  |  `- twins
|  |  |  +- mossmother
|  |  |  |  `- travel
|  |  |  +- musicbox
|  |  |  |  `- tavern
|  |  |  +- noticeboard
|  |  |  +- potionseller
|  |  |  |  +- crafted
|  |  |  |  `- university
|  |  |  +- scomm
|  |  |  |  +- l
|  |  |  |  +- r
|  |  |  |  `- receive_only
|  |  |  |     +- l
|  |  |  |     `- r
|  |  |  +- steward
|  |  |  +- stockpile
|  |  |  +- talkstatue
|  |  |  |  +- church
|  |  |  |  `- mercenary
|  |  |  +- titan
|  |  |  +- vaultbank
|  |  |  +- vendor
|  |  |  |  +- bathhouse
|  |  |  |  +- centcom
|  |  |  |  +- church_bedroomset_one
|  |  |  |  +- church_bedroomset_two
|  |  |  |  +- inn
|  |  |  |  +- keep_councillors
|  |  |  |  +- keep_guests
|  |  |  |  +- keep_knights
|  |  |  |  +- keep_princes
|  |  |  |  +- keep_servant
|  |  |  |  +- keep_squire
|  |  |  |  +- merchant
|  |  |  |  `- stablemaster
|  |  |  `- withdraw
|  |  +- roguerock
|  |  +- roguetent
|  |  +- roguethrone
|  |  +- roguewindow
|  |  |  +- harem1
|  |  |  +- harem2
|  |  |  +- harem3
|  |  |  +- openclose
|  |  |  |  `- reinforced
|  |  |  |     `- brick
|  |  |  `- stained
|  |  |     +- silver
|  |  |     +- yellow
|  |  |     `- zizo
|  |  +- roller
|  |  +- rope_ladder
|  |  +- rotation_piece
|  |  |  `- cog
|  |  |     `- large
|  |  +- rune_ward
|  |  |  +- alarm
|  |  |  +- chill
|  |  |  +- damage
|  |  |  +- fire
|  |  |  `- stun
|  |  +- sacrificealtar
|  |  +- sawblade_trap
|  |  +- shisha
|  |  |  `- hookah
|  |  +- soil
|  |  |  `- debug_soil
|  |  +- spawner
|  |  +- spider
|  |  |  +- cocoon
|  |  |  `- stickyweb
|  |  |     +- mirespider
|  |  |     `- solo
|  |  +- spike_pit
|  |  +- spirit_board
|  |  +- stairs
|  |  |  +- fancy
|  |  |  |  +- c
|  |  |  |  +- l
|  |  |  |  `- r
|  |  |  `- stone
|  |  +- standingbell
|  |  +- stationary_bell
|  |  +- statue
|  |  +- stone_rack
|  |  +- stone_tile
|  |  |  +- block
|  |  |  |  +- burnt
|  |  |  |  `- cracked
|  |  |  +- burnt
|  |  |  +- center
|  |  |  |  +- burnt
|  |  |  |  `- cracked
|  |  |  +- cracked
|  |  |  +- slab
|  |  |  |  +- burnt
|  |  |  |  `- cracked
|  |  |  +- surrounding
|  |  |  |  +- burnt
|  |  |  |  `- cracked
|  |  |  `- surrounding_tile
|  |  |     +- burnt
|  |  |     `- cracked
|  |  +- table
|  |  |  +- church
|  |  |  |  +- alt
|  |  |  |  +- end
|  |  |  |  |  `- alt
|  |  |  |  |     `- north
|  |  |  |  `- m
|  |  |  |     `- alt
|  |  |  +- cooling
|  |  |  +- fine
|  |  |  +- finer
|  |  |  +- finestone
|  |  |  +- optable
|  |  |  +- vtable
|  |  |  |  `- v2
|  |  |  `- wood
|  |  |     +- fancy
|  |  |     |  +- black
|  |  |     |  +- blue
|  |  |     |  +- cyan
|  |  |     |  +- green
|  |  |     |  +- orange
|  |  |     |  +- purple
|  |  |     |  +- red
|  |  |     |  +- royalblack
|  |  |     |  `- royalblue
|  |  |     +- folding
|  |  |     +- large_table
|  |  |     |  +- middle
|  |  |     |  +- middle_east
|  |  |     |  +- middle_west
|  |  |     |  +- north
|  |  |     |  +- north_east
|  |  |     |  +- north_west
|  |  |     |  +- south_east
|  |  |     |  `- south_west
|  |  |     +- long_table
|  |  |     |  +- east
|  |  |     |  +- mid
|  |  |     |  |  `- alt
|  |  |     |  +- north_east
|  |  |     |  `- right
|  |  |     +- map
|  |  |     |  +- five
|  |  |     |  +- four
|  |  |     |  +- six
|  |  |     |  +- three
|  |  |     |  `- two
|  |  |     `- poor
|  |  |        +- alt
|  |  |        `- alt_alt
|  |  +- target_stake
|  |  +- telescope
|  |  +- tent_component
|  |  +- tent_wall
|  |  +- thronething
|  |  +- toilet
|  |  +- trap
|  |  |  +- bogtrap
|  |  |  |  +- bomb
|  |  |  |  +- freeze
|  |  |  |  +- kneestingers
|  |  |  |  `- poison
|  |  |  +- bomb
|  |  |  +- chill
|  |  |  +- curse
|  |  |  |  `- hidden
|  |  |  +- damage
|  |  |  +- fire
|  |  |  +- flame
|  |  |  +- rock_fall
|  |  |  +- saw_blades
|  |  |  +- shock
|  |  |  +- stun
|  |  |  |  `- hunter
|  |  |  +- wall_projectile
|  |  |  |  +- acidsplash
|  |  |  |  `- frostbolt
|  |  |  +- ward
|  |  |  `- water
|  |  +- underworld
|  |  |  +- barrier
|  |  |  +- carriage
|  |  |  +- carriage_normal
|  |  |  `- carriageman
|  |  +- vampire
|  |  |  +- bloodpool
|  |  |  +- portal
|  |  |  |  `- sending
|  |  |  +- portalmaker
|  |  |  `- scryingorb
|  |  +- vampthrone
|  |  +- vertical_gearbox
|  |  +- vine
|  |  |  `- dendor
|  |  +- voidstoneobelisk
|  |  +- wallladder
|  |  +- waterwheel
|  |  +- waywardspirit
|  |  +- well
|  |  |  +- fountain
|  |  |  |  `- mana
|  |  |  `- poisoned
|  |  +- wild_plant
|  |  |  `- nospread
|  |  |     +- manabloom
|  |  |     `- poppy
|  |  +- winch
|  |  `- wonder
|  `- vehicle
|     `- ridden
|        `- dinghy
`- turf
   +- baseturf_bottom
   +- baseturf_skipover
   |  `- shuttle
   +- closed
   |  +- basic
   |  +- dungeon_void
   |  +- indestructible
   |  |  +- abductor
   |  |  +- baseturfs_ded
   |  |  +- necropolis
   |  |  +- oldshuttle
   |  |  |  `- corner
   |  |  +- opshuttle
   |  |  +- paper
   |  |  +- riveted
   |  |  |  `- boss
   |  |  |     `- see_through
   |  |  +- rock
   |  |  |  `- snow
   |  |  |     `- ice
   |  |  +- sandstone
   |  |  `- splashscreen
   |  +- mineral
   |  |  +- random
   |  |  |  `- rogue
   |  |  |     +- high
   |  |  |     `- med
   |  |  `- rogue
   |  |     +- bedrock
   |  |     +- cinnabar
   |  |     +- coal
   |  |     +- copper
   |  |     +- elementalmote
   |  |     +- gem
   |  |     +- gold
   |  |     +- iron
   |  |     +- salt
   |  |     +- silver
   |  |     `- tin
   |  +- transparent
   |  `- wall
   |     +- mineral
   |     |  `- rogue
   |     |     +- brick
   |     |     |  `- window
   |     |     +- craftstone
   |     |     +- decostone
   |     |     |  +- cand
   |     |     |  +- center
   |     |     |  +- end
   |     |     |  |  +- east
   |     |     |  |  +- north
   |     |     |  |  `- west
   |     |     |  +- fluffstone
   |     |     |  +- long
   |     |     |  |  `- east_west
   |     |     |  `- mossy
   |     |     |     +- blue
   |     |     |     |  +- cand
   |     |     |     |  +- end
   |     |     |     |  `- long
   |     |     |     +- cand
   |     |     |     +- end
   |     |     |     +- long
   |     |     |     `- red
   |     |     |        +- cand
   |     |     |        +- end
   |     |     |        `- long
   |     |     +- decowood
   |     |     |  `- vert
   |     |     +- pipe
   |     |     |  +- corners
   |     |     |  |  +- eight
   |     |     |  |  +- four
   |     |     |  |  `- one
   |     |     |  +- joint
   |     |     |  |  +- eight
   |     |     |  |  +- four
   |     |     |  |  `- one
   |     |     |  `- line
   |     |     |     `- four
   |     |     +- roofwall
   |     |     |  +- center
   |     |     |  +- innercorner
   |     |     |  |  +- dir1
   |     |     |  |  +- dir4
   |     |     |  |  `- dir8
   |     |     |  +- middle
   |     |     |  |  +- dir1
   |     |     |  |  +- dir4
   |     |     |  |  `- dir8
   |     |     |  `- outercorner
   |     |     |     +- dir1
   |     |     |     +- dir4
   |     |     |     `- dir8
   |     |     +- stone
   |     |     |  +- blue_moss
   |     |     |  +- moss
   |     |     |  |  `- unbreakable
   |     |     |  +- red_moss
   |     |     |  +- unbreakable
   |     |     |  `- window
   |     |     |     +- blue_moss
   |     |     |     +- moss
   |     |     |     |  `- unbreakable
   |     |     |     `- unbreakable
   |     |     +- stonebrick
   |     |     +- tent
   |     |     +- wood
   |     |     |  `- window
   |     |     `- wooddark
   |     |        +- end
   |     |        |  +- east
   |     |        |  +- north
   |     |        |  `- west
   |     |        +- horizontal
   |     |        +- slitted
   |     |        +- vertical
   |     |        `- window
   |     +- shroud
   |     |  `- hag
   |     `- smooth
   +- open
   |  +- floor
   |  |  +- carpet
   |  |  |  +- inn
   |  |  |  +- purple
   |  |  |  +- red
   |  |  |  +- royalblack
   |  |  |  `- stellar
   |  |  `- rogue
   |  |     +- AzureSand
   |  |     +- blocks
   |  |     |  +- bluestone
   |  |     |  +- flipped
   |  |     |  +- green
   |  |     |  +- newstone
   |  |     |  |  `- alt
   |  |     |  +- paving
   |  |     |  |  `- vert
   |  |     |  +- platform
   |  |     |  `- stonered
   |  |     |     `- tiny
   |  |     +- carpet
   |  |     |  `- lord
   |  |     |     +- center
   |  |     |     |  `- no_teleport
   |  |     |     +- left
   |  |     |     `- right
   |  |     +- church
   |  |     +- churchbrick
   |  |     +- churchmarble
   |  |     +- churchrough
   |  |     +- cobble
   |  |     |  `- mossy
   |  |     +- cobblerock
   |  |     +- concrete
   |  |     |  `- bronze
   |  |     +- crawl_space
   |  |     +- dark_ice
   |  |     |  `- regular
   |  |     +- dirt
   |  |     |  +- ambush
   |  |     |  `- road
   |  |     +- grass
   |  |     +- grasscold
   |  |     +- grassred
   |  |     +- grassyel
   |  |     +- greenstone
   |  |     |  +- glyph1
   |  |     |  +- glyph2
   |  |     |  +- glyph3
   |  |     |  +- glyph4
   |  |     |  +- glyph5
   |  |     |  +- glyph6
   |  |     |  `- runed
   |  |     +- hay
   |  |     +- herringbone
   |  |     +- hexstone
   |  |     +- metal
   |  |     |  `- barograte
   |  |     |     `- open
   |  |     +- naturalstone
   |  |     +- rooftop
   |  |     |  +- east
   |  |     |  +- green
   |  |     |  |  +- corner1
   |  |     |  |  |  +- direight
   |  |     |  |  |  +- dirfive
   |  |     |  |  |  +- dirfour
   |  |     |  |  |  +- dirnine
   |  |     |  |  |  +- dirone
   |  |     |  |  |  +- dirsix
   |  |     |  |  |  `- dirten
   |  |     |  |  +- east
   |  |     |  |  +- north
   |  |     |  |  `- west
   |  |     |  +- north
   |  |     |  `- west
   |  |     +- ruinedwood
   |  |     |  +- chevron
   |  |     |  +- herringbone
   |  |     |  +- herringbone_clear
   |  |     |  +- platform
   |  |     |  +- spiral
   |  |     |  `- turned
   |  |     +- sand
   |  |     +- shroud
   |  |     |  `- hag
   |  |     +- snow
   |  |     +- snowpatchy
   |  |     +- snowrough
   |  |     +- tile
   |  |     |  +- bath
   |  |     |  +- bfloorz
   |  |     |  +- brick
   |  |     |  +- brownbrick
   |  |     |  +- checker
   |  |     |  +- checkeralt
   |  |     |  +- harem
   |  |     |  +- harem1
   |  |     |  +- harem2
   |  |     |  +- masonic
   |  |     |  |  +- inverted
   |  |     |  |  +- single
   |  |     |  |  `- spiral
   |  |     |  `- tilerg
   |  |     +- twig
   |  |     |  `- platform
   |  |     +- underworld
   |  |     |  +- road
   |  |     |  `- space
   |  |     |     +- quiet
   |  |     |     `- sparkle_quiet
   |  |     +- volcanic
   |  |     +- wood
   |  |     |  +- herringbone
   |  |     |  `- nosmooth
   |  |     `- woodturned
   |  |        `- nosmooth
   |  +- lava
   |  |  +- acid
   |  |  +- nosmooth
   |  |  `- smooth
   |  |     +- airless
   |  |     `- lava_land_surface
   |  +- transparent
   |  |  `- openspace
   |  |     `- airless
   |  `- water
   |     +- bath
   |     |  `- pool
   |     |     `- mid
   |     +- bloody
   |     +- cleanshallow
   |     +- ocean
   |     |  `- deep
   |     +- pond
   |     +- river
   |     |  `- flow
   |     |     +- east
   |     |     +- north
   |     |     `- west
   |     +- sewer
   |     +- swamp
   |     |  `- deep
   |     `- transparent
   |        +- inner
   |        |  +- ocean
   |        |  +- pond
   |        |  `- swamp
   |        +- river
   |        |  +- inner
   |        |  |  +- east
   |        |  |  +- north
   |        |  |  +- south
   |        |  |  `- west
   |        |  `- surface
   |        |     +- east
   |        |     +- north
   |        |     +- south
   |        |     `- west
   |        `- surface
   |           +- ocean
   |           +- pond
   |           `- swamp
   `- template_noop
```
