---
name: "byond-codemaster-controller"
description: "Master controller for the SS13/BYOND skill ecosystem — the skill-over-skills that decides when and which skill to invoke (byond-ss13-coding, ss13-tgui, tgstation-modular-content, ss13-tgs-deploy, and future ones), defines their interaction contract, and owns per-repository semantic bases (ai_navigation folders): discovery, bootstrap from zero, binding briefs, integrity control. Use at the start of ANY non-trivial task in an SS13/BYOND fork; whenever it is unclear which skill applies or two skills could both apply; and whenever the user mentions семантика/семантический анализ репозитория, семантическая база, ai_navigation, собрать/обновить/проверить базу, navigation layer, восстановить инфраструктуру, новая кодовая база, skill ecosystem, or a navigation doc contradicts the code. Works from zero: no pre-existing bases or registry required."
---

# BYOND Codemaster Controller

The skill-over-skills for SS13/BYOND work: it routes every task to the right architecture skill(s), arbitrates when their domains overlap, and owns the lifecycle of semantic bases. It assumes **nothing** about the machine: no pre-existing bases, no fixed folder layout, no absolute paths. Given only the installed skills and a codebase — even one never seen before — it builds its own working infrastructure.

## The three layers

| # | Layer | Role | How to locate |
|---|---|---|---|
| 1 | **Controller** (this skill) | Skill dispatch + interaction contract + base lifecycle (discover, create, bind, verify, refresh, retire) | installed skill |
| 2 | **Architecture skills** | The deepest, fork-invariant design patterns and anti-patterns | installed skills, referenced **by name**: `byond-ss13-coding`, `ss13-tgui`, `tgstation-modular-content` |
| 3 | **Semantic bases** | Factual current state of one fork (`ai_navigation/` folders); regenerable data, never authoritative over code | discovered on disk (Discovery protocol below) — never hardcoded |

Outside this stack sits one **operations** skill, `ss13-tgs-deploy` (TGS/Docker/hosting/asset delivery). It is dispatched by Gate 1's first node and then works alone: it answers questions about the *host a build runs on*, not about the code, so it binds to no semantic base and never composes with the architecture skills. Keep it out of the layer model rather than bending the model to fit it.

Truth hierarchy: **repo code > semantic base (fork facts) > architecture skill (fork-specific claims)** — but an architecture skill always wins on framework invariants and anti-patterns, and `byond-ss13-coding` is the reference on engine semantics (tier-1 facts). A base recommending an anti-pattern is a broken base — fix it.

If a referenced skill is not installed, degrade gracefully: state which skill is missing, continue from the layers that are present, and do not guess its content from memory.

Semantic bases are **cattle, not pets**: every base file has a spec and a generation method (`references/file-specs.md`), so any base can be rebuilt from its codebase alone. This skill carries **no machine state**: which repos exist and where their bases live is data, discovered on disk or read from the workspace registry.

## Skill dispatch — two independent gates, composed

Don't scan a table of prose conditions looking for the "best fit" — that's how a task ends up over-triggering two overlapping rows at once. Walk two small gates instead; each node is one crisp, checkable question, evaluated in order, first match wins. The final skill set is whatever Gate 1 returns, optionally prefixed by Gate 2.

**Gate 1 — which skill(s) implement the work?**

1. Is the work about **running a server rather than changing its code** — TGS/tgstation-server, DreamDaemon, Docker, hosting, deploying/migrating/rebuilding an instance, asset-CDN or nginx delivery, `librust_g.so`/build-toolchain failures? → `ss13-tgs-deploy` alone. **STOP** (ops axis: no Gate 2, no semantic base — bases describe code, not hosts).
   *Boundary:* the symptom must live on the host. A slow or crashing **game** is not this node — a server that lags because a proc is expensive is the default node's work, and only becomes this node's when the evidence points at the host (RAM, disk, the container, the toolchain, asset delivery). "The server is broken" is not a routing signal; what is broken is.
2. Is the ask purely "where should this go" / mergeability, with no code to write yet? → `tgstation-modular-content` alone. **STOP** (skip Gate 2 — already resolved).
3. Is this a semantic-base task (create/discover/verify/refresh `ai_navigation/`), or "which skill(s) apply to my task"? → this skill handles it directly, via the Discovery protocol below. **STOP** (skip Gate 2).
4. Does the task touch `tgui/` files, `ui_interact`/`tgui_interact`/`ui_data`/`ui_act`, `ByondUi`, or a blank/white-window symptom, with **no** DM-side systems work (subsystems, components, signals, lifecycle) in the same change? → `ss13-tgui` alone implements. → go to Gate 2.
5. Does the task touch **both** `tgui/` work and DM-side systems work in the same change? → `byond-ss13-coding` implements the DM side up to the `ui_data`/`ui_act` boundary; `ss13-tgui` implements everything inside `tgui/`. → go to Gate 2.
6. Default — everything else (DM coding, review, performance, debugging, porting between forks): `byond-ss13-coding` implements alone. → go to Gate 2.

**Gate 2 — does placement need a mergeability decision?** (only asked if Gate 1 didn't already STOP)

7. Two conditions, both required:
   **(a) Does the fork track upstream?** Lead with the `modular_*`/`master_files` directory convention — that is the reliable detector. A semantic base or a root `AGENTS.md` may also say so, but a root `AGENTS.md` was present in only 1 of 5 checkouts measured 2026-09-01, so **its absence is not evidence either way**.
   **(b) Does this change need a genuinely new placement** — a new file, interface or override — rather than an edit to something already sitting in its correct modular home?
   Both yes → prepend `tgstation-modular-content`: it decides placement and file layout **first**; whatever Gate 1 selected implements the content inside that placement.
   Otherwise → Gate 1's answer stands unchanged.

**This section is the single source of truth for routing.** The architecture skills each declare only their own boundary and defer here; if one of them appears to restate this table, that copy is drift — fix it there, not by forking the logic.

**If the guards still disagree after both gates** — a real clash means one skill was stretched outside its own guard; re-check the guards rather than picking by feel. **If the task exposes knowledge neither skill has** — route the fact to the right layer: invariant everywhere → the architecture skill (enrichment intake); true only in this fork → the semantic base (§Feedback loop in `references/binding.md`).

New architecture skills join Gate 1 as a new node in front of its **default node** — the last one, which catches everything else — stating the new node's domain guard and where it sits relative to the existing ones. Renumber the nodes below it in the same edit. **Refer to a node by its role ("the default node", "the ops node"), never by its number, anywhere outside this section**: numbers shift every time a skill is added, and a stale "see node 5" elsewhere in the ecosystem is drift that nothing will catch.

## Discovery protocol (run this first, every time)

Given the repo (or directory) the task points at:

1. **In-repo base:** does `<repo>/ai_navigation/` exist with an `AGENTS.md` or `router.md` inside? → that is the repo's base. **Check with a direct filesystem probe (`ls`/`dir`), not a search tool:** in-repo bases and fork overlays are often gitignored, and gitignore-respecting glob/grep tooling silently reports them absent (verified failure mode, 2026-07-16). Primary convention *by design*: a base lives inside its repo, because base docs self-reference as `ai_navigation/...`. **But measured across a real workspace (2026-09-01) only 2 of 5 SS13 checkouts actually shipped one**, so in practice step 1 usually misses and steps 2-3 carry the protocol. Keep the ordering — an in-repo hit is authoritative when it happens — but do not treat a miss as informative, and never conclude “no base exists” from step 1 alone.
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

Referenced by name; interaction order is the Skill dispatch gates above. If one is not installed, say so and continue without it. The base-file lists below are **candidates, not a mandatory load-out**: when the base has a `router.md`, follow its task-conditional dispatch ("pick one helper") and open further candidates only when a concrete need fires — a 2026-07-16 dry run confirmed router-first loading is strictly cheaper with no loss.

| Skill | Invariants for | Bind with these base files |
|---|---|---|
| `byond-ss13-coding` | DM semantics, SS13 architecture (MC/subsystems, components, signals, lifecycle/qdel), performance, review | `coding_standards.md`, `subsystem_map.md`, `signal_map.md`, `core_procs.md`, `engine_limits.md` |
| `ss13-tgui` | TGUI lifecycle, components, ByondUi bridge, runtime triage | `tgui_guide.md`, `signal_map.md`, `coding_standards.md` |
| `tgstation-modular-content` | Modular overlay patterns, upstream mergeability | `modular_guide.md`, `architecture.md`, `content_patterns.md` |
| `ss13-tgs-deploy` | TGS/Docker deployment, hosting, asset delivery | **none** — ops skill, binds to no base (see §The three layers) |

## Decision flow

| Situation | Do |
|---|---|
| Coding task, discovery found a base | Bind: base `router.md` → one helper; pick the architecture skill(s) per the dispatch gates; produce a binding brief per `references/binding.md` |
| Coding task, no base | Do the task from source (still applying the dispatch gates); offer to bootstrap afterwards |
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
