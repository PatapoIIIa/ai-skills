# Runtime Flow

Generated for Azure-Peak. Use this file when the question is about order of execution, ownership, or lifecycle rather than just file location.

## Canonical Flows

### 1. World Bootstrap and Scheduler Startup

- Typical chain: `/world` -> `Master` -> subsystem subtype discovery -> `PreInit/Initialize` -> runlevel-driven `fire()`.
- Runtime owners: `Master` and the target `SS*`.
- Open first: `code/world.dm`, `code/controllers/master.dm`, `code/controllers/subsystem.dm`.
- Use when: startup, init order, tick budgeting, scheduler, or ownership questions.

### 1a. Atom Initialization Lifecycle

- Typical chain: `SSatoms.Initialize()` -> iterates map atoms -> calls `atom.Initialize(mapload)` -> atoms returning `INITIALIZE_HINT_LATELOAD` go into `late_loaders` -> `LateInitialize()` runs after map atom initialization.
- Runtime owner: `SSatoms`.
- Open first: `code/controllers/subsystem/atoms.dm`.
- Key facts: `INITIALIZE_HINT_NORMAL` means no `LateInitialize`; subclasses needing late map objects must explicitly return `INITIALIZE_HINT_LATELOAD` if their parent does not.

### 2. Round Flow to Antagonist Assignment

- Typical chain: ticker/storyteller state -> `round_event_control` selection -> `round_event` setup -> `add_antag_datum(...)` -> antagonist `on_gain()`.
- Runtime owners: `SSticker`, `SSgamemode`, `SSevents`.
- Open first: `code/controllers/subsystem/ticker.dm`, `code/controllers/subsystem/storyteller.dm`, `code/controllers/subsystem/events.dm`, `code/modules/events/**`, `code/modules/antagonists/**`.

### 3. Role / Job / Migrant Spawn

- Typical chain: round or join flow -> job/migrant role resolution -> loadout/spawn setup -> mob enters map -> later class/antag overlays.
- Runtime owners: `SSjob`, `SSmigrants`, `SSrole_class_handler`.
- Open first: `code/controllers/subsystem/job.dm`, `code/controllers/subsystem/migrants.dm`, `code/modules/jobs/**`, `code/datums/migrants/**`.

### 4. Action or Spell to Status Effect

- Typical chain: user input/action button -> `/datum/action` or spell proc -> validation/cost/cooldown -> `apply_status_effect(...)` or direct mob/item change.
- Runtime owners: direct action/spell/status datums, `SSskills`, sometimes `SSmood`.
- Open first: `code/modules/spells/**`, `code/datums/actions/**`, `code/datums/status_effects/**`.

### 5. Signal and Component Reaction Path

- Typical chain: source proc -> `SEND_SIGNAL(...)` -> component/element handler -> state mutation/status/follow-up proc.
- Runtime owner: `SSdcs` plus the owning feature path.
- Open first: `code/datums/components/**`, `code/datums/elements/**`, `code/__DEFINES/dcs/**`, `code/__DEFINES/components.dm`.

### 6. Movement and Pull/Buckle/Throw

- Typical chain: `/client/Move` -> `/atom/movable/Move` -> `Moved/Cross/Crossed/Bump` -> optional pull/buckle/throw side path.
- Runtime owners: `SSmovement`, `SSmove_manager`, `SSthrowing`, `SSdcs`.
- Open first: `ai_navigation/movement_signal_map.md`, `code/modules/mob/mob_movement.dm`, `code/game/atoms_movable.dm`, `code/game/objects/buckling.dm`, `code/controllers/subsystem/movement/**`.
- Pulling uses direct procs.

### 7. AI Tick to Mob Action

- Typical chain: controller process -> behavior selection/execution -> movement/path update -> mob action/attack/use.
- Runtime owners: `SSai_controllers`, `SSai_behaviors`, `SSai_movement`.
- Open first: `code/controllers/subsystem/ai_controller.dm`, `code/controllers/subsystem/processing/ai_behaviours.dm`, `code/controllers/subsystem/processing/ai_movement.dm`, `code/datums/ai/**`.

### 8. Mapping and World Generation

- Typical chain: map bootstrap/generation pass -> template placement or mapgen -> landmarks/spawners become available -> jobs/events/mobs use those locations.
- Runtime owners: `SSmapping`, `SSminor_mapping`, `SSdungeon_generator`, `SSmapgen`, `SSpathfinder`.
- Open first: `code/controllers/subsystem/mapping.dm`, `_maps/**`, `code/modules/mapping/**`, `code/modules/procedural_mapping/**`, `code/controllers/subsystem/processing/mapgen.dm`.

### 9. Questing and Contracts

- Typical chain: contract ledger interaction -> quest datum selection -> scroll/object/component creation -> objective signal/proc updates -> ledger turn-in.
- Runtime owners: `SSdcs`, `SSroguemachine`, player/ledger flow.
- Open first: `code/modules/roguetown/roguemachine/questing/contract_ledger.dm`, `code/modules/roguetown/roguemachine/questing/types/**`, `code/modules/roguetown/roguemachine/questing/items/**`, `code/modules/roguetown/roguemachine/questing/questing_components.dm`, `code/__DEFINES/questing.dm`.

### 10. UI Request to Gameplay State

- Typical chain: UI interaction -> DM-side UI/TGUI datum -> underlying gameplay datum/mob/proc -> optional status/component update.
- Runtime owners: `SStgui`, `SSchat`, `SSstatpanel`.
- Open first: `code/modules/tgui/**`, `code/modules/tgui_input/**`, `code/modules/tgui_panel/**`, `interface/**`, `tgui/packages/**`.

## Escalation Rules

- If you know the keyword but not the flow, start with `ai_navigation/entrypoints.md`.
- If you know the flow but not the owner, use `ai_navigation/subsystem_map.md`.
- If you know the systems involved but not how they connect, use `ai_navigation/system_dependencies.md`.
- If the issue is still local after identifying the flow, go back to source files instead of opening more maps.
