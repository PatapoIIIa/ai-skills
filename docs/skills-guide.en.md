# SS13/BYOND AI Skill Set — Guide

This is the human-readable description of the five skills in this repository. A skill is a package of instructions that an AI agent (Claude and compatible) loads when it picks up a matching task. The skills carry no machine-specific state: install them anywhere and work with any SS13 fork.

## What's in the set

| Skill | In one phrase |
|---|---|
| **byond-codemaster-controller** | The dispatcher: decides which skill to invoke and manages per-repo "semantic bases" |
| **byond-ss13-coding** | Universal Dream Maker coding: language, SS13 architecture, performance, review |
| **ss13-tgui** | Everything TGUI and browser UI: React frontend, DM backend, blank-window triage |
| **tgstation-modular-content** | How to add fork content that survives upstream syncs |
| **ss13-tgs-deploy** | Standing up and running the server itself: TGS, Docker, builds, asset delivery |

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

## ss13-tgs-deploy — server deployment

The set's only operations skill: it is about the machine a build runs on, not the code inside it. Standing tgstation-server up in Docker from zero, creating the instance, EventScripts, the glibc trap in prebuilt `librust_g.so`, building tgui through Bun, serving assets from nginx with mandatory CORS, and — a topic of its own — which directories survive a deploy and which are silently recreated.

It sits apart from the other four: it binds to no semantic base (bases describe code, not hosts) and does not combine with the architecture skills. It has two edges: a DM compile error surfaced by a deploy goes to `byond-ss13-coding`, and an interface that renders wrong while assets are demonstrably being served goes to `ss13-tgui`.

Worth calling out separately: all of its commands run against a live host (`/etc/fstab`, swap, packages, nginx), so the skill is required to **propose them rather than run them** on its own initiative.

Example requests:

- EN: "Stand our SS13 fork up on a fresh Ubuntu box with TGS in Docker — walk me through it from zero."
- RU: «Подними наш форк SS13 на чистой Ubuntu через TGS в Docker — проведи с нуля».
- EN: "tgui windows are blank on the new server and nginx is logging a flood of 404s on `/`."
- RU: «На новом сервере tgui-окна пустые, а nginx сыплет 404 на `/`».

## How they work together

1. The controller looks at the task and assigns roles (the dispatch gates in its SKILL.md).
2. For combined tasks the order is fixed: **placement beats implementation** (modular-content decides file structure; coding/tgui decide contents), and **the DM side is separated from the frontend** (byond-ss13-coding owns everything up to the `ui_data`/`ui_act` boundary; ss13-tgui owns the rest).
3. Truth hierarchy: live repo code > semantic base (fork facts) > skill (general patterns). On engine semantics, byond-ss13-coding has the final word.
4. The operations axis stands apart: when the task is about the host rather than the code, the controller hands it to `ss13-tgs-deploy` whole and stops there — no semantic base, no composition with the architecture skills.

## Installation

The recommended route is the plugin subscription — install once, updates arrive on their own.

```bash
claude plugin marketplace add PatapoIIIa/ai-skills
```

```bash
claude plugin install ss13-byond@ss13-ai-skills
```

Install the whole set rather than picking skills apart: the controller routes to the others by name and degrades if they are missing. The manifest deliberately omits `version`, so you track the default branch's latest commit; for updates, see the "Обновление / Updating" section in [README.md](../README.md).

**When `/plugin` is unavailable.** In some environments — the desktop app and other non-terminal surfaces — the slash command answers `/plugin isn't available in this environment`. The `claude plugin ...` commands above still work; they just need a real shell. If you have no terminal at hand, anything that can run shell commands will do — for example the [Desktop Commander](https://github.com/wonderwhy-er/DesktopCommanderMCP) MCP server: ask your assistant to run the same commands through it. Verify with `claude plugin list`, where the Version field for `ss13-byond@ss13-ai-skills` is a git SHA.

For agents without plugin support, take the individual skill folder from `plugins/ss13-byond/skills/` and add it to your agent's skill storage by hand.

Either way there are no paths to configure: the agent discovers repository and semantic-base locations itself via the discovery protocol.

## Honesty

The skills explicitly forbid the agent from claiming code "compiled" or "was tested" unless the corresponding commands actually ran. Instead, the agent must list which checks (compile, DreamChecker, CI) you can run yourself.
