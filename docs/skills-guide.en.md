# SS13/BYOND AI Skill Set — Guide

This is the human-readable description of the four skills in this repository. A skill is a package of instructions that an AI agent (Claude and compatible) loads when it picks up a matching task. The skills carry no machine-specific state: install them anywhere and work with any SS13 fork.

## What's in the set

| Skill | In one phrase |
|---|---|
| **byond-codemaster-controller** | The dispatcher: decides which skill to invoke and manages per-repo "semantic bases" |
| **byond-ss13-coding** | Universal Dream Maker coding: language, SS13 architecture, performance, review |
| **ss13-tgui** | Everything TGUI and browser UI: React frontend, DM backend, blank-window triage |
| **tgstation-modular-content** | How to add fork content that survives upstream syncs |

The economy principle: the agent loads only the skill (and only those of its reference files) that the current task needs. Nothing "just in case".

## byond-codemaster-controller — the dispatcher

The "skill over skills". Every non-trivial task starts here: it classifies the work (pure DM? UI? modular content? a combination?) and engages the right skills in the right order. Its second domain is semantic bases (`ai_navigation/` folders): per-repository reference layers it can discover, freshness-check, and bootstrap from zero for an unfamiliar codebase.

Example requests it responds to:

- EN: "Set up a navigation base for this new fork and tell me which skills apply to my task."
- RU: «Собери семантическую базу для нового форка и скажи, какие скиллы нужны под мою задачу».

## byond-ss13-coding — universal DM/SS13 coding

The main workhorse. It knows Dream Maker language and BYOND engine semantics (verified against the official reference), SS13 architecture (Master Controller, subsystems, components, signals, object lifecycle and qdel), performance rules (tick budget, allocations, appearances), and a code-review procedure with a checklist. It separates "engine truth" from "project convention": it will not force tgstation style onto a fork with a different architecture.

Example requests:

- EN: "Add a component that regenerates the wearer every 5 seconds and clean it up properly on deletion."
- RU: «Добавь компонент, который регенерирует носителя каждые 5 секунд, и корректно очисти его при удалении».
- EN: "Review this DM patch for hard-delete risks."
- RU: «Проверь этот DM-патч на риски hard delete».

## ss13-tgui — interfaces

The specialist skill for everything TGUI: window lifecycle, `ui_data`/`ui_act`, React components and styling, the BYOND-browser bridge, asset delivery, and triage of blank/white windows across platforms. The coding skill hands off here as soon as a task crosses the "DM data → interface" boundary.

Example requests:

- EN: "My tgui window opens blank on Windows 7 clients — help me triage it."
- RU: «TGUI-окно открывается белым у клиентов на Windows 7 — помоги разобраться».

## tgstation-modular-content — modular content

The skill about *where changes go* on a fork that regularly pulls upstream: modular folders, overlays, edit tags, aggregator includes. Its goal is to keep your features from turning into merge conflicts on every rebase. It pairs with the coding skill: this one decides "where", that one decides "how".

Example requests:

- EN: "Add a new job item on our fork without touching upstream files."
- RU: «Добавь новый предмет профессии на нашем форке, не трогая upstream-файлы».

## How they work together

1. The controller looks at the task and assigns roles (the dispatch gates in its SKILL.md).
2. For combined tasks the order is fixed: **placement beats implementation** (modular-content decides file structure; coding/tgui decide contents), and **the DM side is separated from the frontend** (byond-ss13-coding owns everything up to the `ui_data`/`ui_act` boundary; ss13-tgui owns the rest).
3. Truth hierarchy: live repo code > semantic base (fork facts) > skill (general patterns). On engine semantics, byond-ss13-coding has the final word.

## Installation

1. Take a skill folder (or the packaged `.skill` — it is a plain zip) and add it to your agent's skill storage (in the Claude app: Skills panel → Add).
2. Skills are self-contained: no paths to configure. The agent discovers repository and base locations itself via the discovery protocol.

## Honesty

The skills explicitly forbid the agent from claiming code "compiled" or "was tested" unless the corresponding commands actually ran. Instead, the agent must list which checks (compile, DreamChecker, CI) you can run yourself.
