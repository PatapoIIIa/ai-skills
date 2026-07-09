---
name: "semantic-controller"
description: "Discovers, creates, and maintains per-repository semantic bases (ai_navigation folders) for SS13/BYOND codebases, and binds architecture-knowledge skills (ss13-tgui, tgstation-modular-content) to a base for concrete tasks. Use whenever the user mentions семантическая база, семантика репозитория, ai_navigation, собрать/обновить/проверить базу, navigation layer, a new repo that needs mapping; before any non-trivial coding task in an SS13/BYOND fork (to route through the repo's base and produce a binding brief); and whenever a navigation doc contradicts the code. Works from zero: no pre-existing bases or registry required."
---

# Semantic Controller

Semantic bases are **cattle, not pets**: every file in a base has a spec and a generation method (`references/file-specs.md`), so any base can be rebuilt from its codebase alone. This skill owns that lifecycle — discover, create, bind, verify, refresh, retire. It carries **no machine state**: which repos exist and where their bases live is data, discovered on disk or read from the workspace registry.

## Discovery protocol (run this first, every time)

Given the repo (or directory) the task points at:

1. **In-repo base:** does `<repo>/ai_navigation/` exist with an `AGENTS.md` or `router.md` inside? → that is the repo's base. Primary convention: a base lives inside its repo, because base docs self-reference as `ai_navigation/...`.
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

Referenced by name; interaction order between them is defined in `run-skill-generator`. If one is not installed, say so and continue without it.

| Skill | Invariants for | Bind with these base files |
|---|---|---|
| `ss13-tgui` | TGUI lifecycle, components, ByondUi bridge, runtime triage | `tgui_guide.md`, `signal_map.md`, `coding_standards.md` |
| `tgstation-modular-content` | Modular overlay patterns, upstream mergeability | `modular_guide.md`, `architecture.md`, `content_patterns.md` |

## Decision flow

| Situation | Do |
|---|---|
| Coding task, discovery found a base | Bind: base `router.md` → one helper; if an architecture skill covers the domain, produce a binding brief per `references/binding.md` |
| Coding task, no base | Do the task from source; offer to bootstrap afterwards |
| New codebase should get a base | `references/bootstrap.md` (assessment → staged build), with `references/file-specs.md` as the per-file DNA |
| Base is stale / suspect / just refreshed | `references/integrity.md`: run `scripts/validate_semantic_base.py`, refresh by drift tier, re-stamp, update registry |
| Base contradicts code | Code wins. Navigation Miss Protocol: a missing/thin base entry never proves absence — grep the source, use what you find, then fix the base entry |
| Base recommends what an architecture skill calls an anti-pattern | The skill wins; fix the base (`references/binding.md` §Conflicts) |
| Fork fact surfaces that an architecture skill lacks | Propose enrichment to that skill; fork-local facts stay in the base (`references/binding.md` §Feedback loop) |
| Repo family is unknown or not BYOND/SS13 at all | Run the Stage 0 assessment (`references/bootstrap.md`) to see which layers even have equivalents; architecture skills stay out of domains the repo lacks; the reasoning model (routing → ownership → contracts) still applies |
| Question falls between the skills and the base (nobody wrote it down) | Derive from repo precedent, not from memory of other forks (`references/binding.md` §Gaps) |

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
