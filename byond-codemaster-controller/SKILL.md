---
name: "byond-codemaster-controller"
description: "Master controller for the SS13/BYOND skill ecosystem — the skill-over-skills that decides when and which skill to invoke (byond-ss13-coding, ss13-tgui, tgstation-modular-content, and future ones), defines their interaction contract, and owns per-repository semantic bases (ai_navigation folders): discovery, bootstrap from zero, binding briefs, integrity control. Use at the start of ANY non-trivial task in an SS13/BYOND fork; whenever it is unclear which skill applies or two skills could both apply; and whenever the user mentions семантика/семантический анализ репозитория, семантическая база, ai_navigation, собрать/обновить/проверить базу, navigation layer, восстановить инфраструктуру, новая кодовая база, skill ecosystem, or a navigation doc contradicts the code. Works from zero: no pre-existing bases or registry required."
---

# BYOND Codemaster Controller

The skill-over-skills for SS13/BYOND work: it routes every task to the right architecture skill(s), arbitrates when their domains overlap, and owns the lifecycle of semantic bases. It assumes **nothing** about the machine: no pre-existing bases, no fixed folder layout, no absolute paths. Given only the installed skills and a codebase — even one never seen before — it builds its own working infrastructure.

## The three layers

| # | Layer | Role | How to locate |
|---|---|---|---|
| 1 | **Controller** (this skill) | Skill dispatch + interaction contract + base lifecycle (discover, create, bind, verify, refresh, retire) | installed skill |
| 2 | **Architecture skills** | The deepest, fork-invariant design patterns and anti-patterns | installed skills, referenced **by name**: `byond-ss13-coding`, `ss13-tgui`, `tgstation-modular-content` |
| 3 | **Semantic bases** | Factual current state of one fork (`ai_navigation/` folders); regenerable data, never authoritative over code | discovered on disk (Discovery protocol below) — never hardcoded |

Truth hierarchy: **repo code > semantic base (fork facts) > architecture skill (fork-specific claims)** — but an architecture skill always wins on framework invariants and anti-patterns, and `byond-ss13-coding` is the reference on engine semantics (tier-1 facts). A base recommending an anti-pattern is a broken base — fix it.

If a referenced skill is not installed, degrade gracefully: state which skill is missing, continue from the layers that are present, and do not guess its content from memory.

Semantic bases are **cattle, not pets**: every base file has a spec and a generation method (`references/file-specs.md`), so any base can be rebuilt from its codebase alone. This skill carries **no machine state**: which repos exist and where their bases live is data, discovered on disk or read from the workspace registry.

## Skill dispatch — when and which skill to invoke

Each architecture skill has an activation guard — respect it; do not stretch a skill past its domain.

| Situation | Contract |
|---|---|
| General DM/SS13 coding: writing or reviewing DM code, systems (subsystems, components, signals, traits, timers), lifecycle/qdel bugs, runtimes, performance, porting between forks | `byond-ss13-coding` — the default architecture skill when no narrower guard matches |
| Task is pure UI/webview (tgui files, ui_* procs, ByondUi, blank windows) | `ss13-tgui` alone |
| Task is fork content that must survive upstream sync | `tgstation-modular-content` alone |
| Modular tgui interface (both apply) | `tgstation-modular-content` decides **placement and file layout** (overlay dir, include wiring, edit markers); `ss13-tgui` decides **implementation** (lifecycle, data flow, components). Placement constraints outrank implementation convenience — a correct UI in the wrong layer is a merge conflict later |
| DM implementation on a tracking fork (`byond-ss13-coding` + `tgstation-modular-content`) | modular-content decides **placement**, byond-ss13-coding decides **DM implementation** (same axis split as with tgui) |
| DM feature with a tgui surface (`byond-ss13-coding` + `ss13-tgui`) | byond-ss13-coding owns the DM side up to the data/action boundary (`ui_data` payload shape, `ui_act` security); ss13-tgui owns everything inside `tgui/` |
| Skills appear to disagree | They own different axes (mergeability vs framework correctness vs engine semantics); a real clash means one is applied outside its guard — re-check the guards |
| Task reveals knowledge neither skill has | Route the fact to the right layer: invariant everywhere → the architecture skill (enrichment intake); true only in this fork → the semantic base (§Feedback loop in `references/binding.md`) |

Rows compose: a task hitting three axes at once (e.g. a modular DM mechanic with a tgui surface) applies each relevant pairwise row simultaneously — placement decisions outrank DM implementation, which owns everything up to the `ui_data`/`ui_act` boundary, past which UI implementation rules. No special 3-way contract is needed.

New architecture skills join this table with: name, domain guard, and interaction rules against the existing ones.

## Discovery protocol (run this first, every time)

Given the repo (or directory) the task points at:

1. **In-repo base:** does `<repo>/ai_navigation/` exist with an `AGENTS.md` or `router.md` inside? → that is the repo's base. **Check with a direct filesystem probe (`ls`/`dir`), not a search tool:** in-repo bases and fork overlays are often gitignored, and gitignore-respecting glob/grep tooling silently reports them absent (verified failure mode, 2026-07-16). Primary convention: a base lives inside its repo, because base docs self-reference as `ai_navigation/...`.
2. **Workspace registry:** search upward from the repo (and the working directory) for `ai_navigation_registry.md`. If found, resolve the repo through its table — it may map the repo to a base stored elsewhere (legacy/standalone layouts).
3. **Sibling bases:** if still nothing, glob for `ai_navigation*` directories next to the repo and in the parent workspace; match by the repo facts stated in each base's `AGENTS.md`/`SKILL.md` (project file name, overlay dir) — never by folder name alone.
4. **Nothing found:** the repo has no base. Proceed from source; offer to bootstrap (`references/bootstrap.md`). Never block the user's task on base creation.

Then, before trusting whatever was found:

5. **Identity check (always, even for an in-repo base):** the base must describe THIS repo — its stated project file and overlay dir must actually exist here. Forks get cloned together with their parent's `ai_navigation/`, so an in-repo base can be foreign. Identity mismatch → treat as foreign: its *reasoning structure* may still help, its *facts* do not transfer; say so and offer a refresh/bootstrap.
6. **Freshness spot-check (cheap, calibrates trust):** grep 2-3 load-bearing facts from the base against the code (entry proc name in one neighboring interface, one component import in a real frontend file, the overlay include in the project file). All hold → trust normally. Any miss → mark the base **drifted** for this session: use it for routing, never for literal identifiers (see `references/binding.md` §Fact classes), and log the miss to the registry backlog.

### Workspace registry (local data file, owned by the machine — not part of this skill)

`ai_navigation_registry.md` lives at the workspace root (the directory holding the repos). Created/updated by this skill on first bootstrap or on request. Format:

```markdown
# AI Navigation Registry
Workspace: <root path>   Updated: YYYY-MM-DD

| Base (path) | Repositories (paths) | Project file | Overlay layer | Deployed at | Notes |
|---|---|---|---|---|---|

## Workspace rules
- <machine-specific rules: read-only upstream checkouts, sync conventions, known gaps>

## Known drift / parity backlog
- <base>: <finding> (found YYYY-MM-DD)
```

One repo — one base. Registry rows use paths *relative to the workspace root* where possible. Everything machine-specific (existing repos, drift findings, local rules like "upstream checkout is read-only") belongs here or in the bases — never in skill files.

## Architecture skills this controller binds

Referenced by name; interaction order is the Skill dispatch table above. If one is not installed, say so and continue without it. The base-file lists below are **candidates, not a mandatory load-out**: when the base has a `router.md`, follow its task-conditional dispatch ("pick one helper") and open further candidates only when a concrete need fires — a 2026-07-16 dry run confirmed router-first loading is strictly cheaper with no loss.

| Skill | Invariants for | Bind with these base files |
|---|---|---|
| `byond-ss13-coding` | DM semantics, SS13 architecture (MC/subsystems, components, signals, lifecycle/qdel), performance, review | `coding_standards.md`, `subsystem_map.md`, `signal_map.md`, `core_procs.md`, `engine_limits.md` |
| `ss13-tgui` | TGUI lifecycle, components, ByondUi bridge, runtime triage | `tgui_guide.md`, `signal_map.md`, `coding_standards.md` |
| `tgstation-modular-content` | Modular overlay patterns, upstream mergeability | `modular_guide.md`, `architecture.md`, `content_patterns.md` |

## Decision flow

| Situation | Do |
|---|---|
| Coding task, discovery found a base | Bind: base `router.md` → one helper; pick the architecture skill(s) per the dispatch table; produce a binding brief per `references/binding.md` |
| Coding task, no base | Do the task from source (still applying the dispatch table); offer to bootstrap afterwards |
| New codebase should get a base | `references/bootstrap.md` (assessment → staged build), with `references/file-specs.md` as the per-file DNA |
| Base is stale / suspect / just refreshed | `references/integrity.md`: run `scripts/validate_semantic_base.py`, refresh by drift tier, re-stamp, update registry |
| Base contradicts code | Code wins. Navigation Miss Protocol: a missing/thin base entry never proves absence — grep the source, use what you find, then fix the base entry |
| Base recommends what an architecture skill calls an anti-pattern | The skill wins; fix the base (`references/binding.md` §Conflicts) |
| Fork fact surfaces that an architecture skill lacks | Propose enrichment to that skill; fork-local facts stay in the base (`references/binding.md` §Feedback loop) |
| Repo family is unknown or not BYOND/SS13 at all | Run the Stage 0 assessment (`references/bootstrap.md`) to see which layers even have equivalents; architecture skills stay out of domains the repo lacks; the reasoning model (routing → ownership → contracts) still applies |
| Question falls between the skills and the base (nobody wrote it down) | Derive from repo precedent, not from memory of other forks (`references/binding.md` §Gaps) |

## Cold start (fresh machine, zero infrastructure)

1. Install this skill plus the architecture skills.
2. Point a session at any SS13/BYOND repo and start a task — no other setup.
3. Discovery finds a base if the repo ships one (`<repo>/ai_navigation/`); otherwise work proceeds from source, with an offer to bootstrap a base from the file specs.
4. The first bootstrap also creates the workspace registry (a local **data** file owned by the user's machine, not by any skill) — from then on, multi-repo dispatch is data-driven.

Keep that property when editing this skill: machine state (which repos exist, where bases live, what drifted) belongs in the workspace registry and the bases themselves — **never** in skill files. Never write an absolute path into a skill.

## Hard rules

- A base is a routing aid, never a source of truth. Verify against code before concluding or editing.
- Every generated inventory (signal counts, type counts, subsystem index) carries its generation date and the command that produced it — refreshes regenerate, never hand-edit.
- Preferred layout: single copy at `<repo>/ai_navigation/`. If the workspace keeps a master copy elsewhere (registry says so), every edit lands in the master first, then re-deploys; `diff -rq` between copies must be empty.
- Respect workspace rules from the registry (e.g. read-only upstream checkouts) before touching anything.
- Do not create helper files for systems the repo does not have; do not duplicate architecture-skill content into a base — link the skill by name instead.

## References

- `references/bootstrap.md` — build a base from zero on any codebase: assessment, staged build order, deployment, registration. Read when creating or migrating a base.
- `references/file-specs.md` — the DNA: per-file spec (purpose, required sections, generated vs authored, drift tier) for every base file. Read during bootstrap and when auditing base parity.
- `references/binding.md` — binding brief format, conflict resolution matrix, enrichment feedback loop. Read for any task combining an architecture skill with a base.
- `references/integrity.md` — validation, drift tiers, refresh procedure, sync/registry maintenance, parity audit. Read for maintenance.
- `scripts/validate_semantic_base.py` — checks that path references inside a base resolve in the base and the repo. Run after every refresh and bootstrap.
