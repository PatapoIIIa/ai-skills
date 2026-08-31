# Binding — applying architecture knowledge to repository semantics

Binding answers one question: **"We know how this is supposed to work (architecture skill) — how does that apply to what actually exists in this fork (semantic base)?"**

An architecture skill without a base produces code that does not compile here (wrong proc names, wrong import paths, wrong include order). A base without an architecture skill produces code that compiles but repeats known anti-patterns (hand-rolled caches, act polling, non-modular edits). The binding brief forces both to be consulted before code is written.

## Binding algorithm

1. **Classify the task domain.** General DM/SS13 coding → `byond-ss13-coding` (the default). TGUI/web UI → `ss13-tgui`. Fork content that must stay mergeable → `tgstation-modular-content`. Several can apply — their interaction order is the Skill dispatch gates in this skill's SKILL.md. If no architecture skill covers the domain, work from the base alone; do not stretch a skill past its activation guard.
2. **Resolve repo → base** via the Discovery protocol in `SKILL.md` (in-repo `ai_navigation/` → workspace registry → sibling glob). No base → work from source, offer bootstrap afterwards.
3. **Pull invariants** from the architecture skill: contracts that hold everywhere (e.g. "`ui_act` returning truthy already triggers `SStgui.update_uis`", "modular code never edits upstream files in place"). These you will not re-derive or violate.
4. **Pull local facts** from the base: entry proc names, import paths, overlay directory, include order, which signals/subsystems exist, local policies (e.g. Azure's TGUI localization pipeline is a base-level requirement no cross-fork skill knows).
5. **Write the binding brief** (below), with verification greps for every local fact you rely on — bases drift, and a brief built on a stale fact is worse than none.
6. **Verify, then code.** Run the greps. Mismatch → code wins; note the drift; flush it to the registry backlog at task end (`integrity.md` §Post-task feedback).

## Fact classes — what must be verified, and how hard

**Load-bearing facts** become literal text in code or decide where files go: proc names, import paths, file names and extensions, route registration, include/overlay locations, signal names. A stale load-bearing fact produces code that does not compile or does not merge.

The structural defense: **the base routes; a neighbor supplies the literal text.** Never type an identifier from a base doc into code. Use the base to find one real neighboring implementation in THIS repo (an interface, a module, a component), and copy the import path / proc name / registration pattern from that file. Under this rule even a badly drifted base cannot inject a stale identifier — at worst it routes you to the neighbor more slowly. (Real case: a base's guide showed `from '../components'` while the repo had migrated to `'tgui-core/components'`; every actual neighbor already had the correct import.)

**Advisory facts** — policies, recipes, impact maps, risk tiers. Verify opportunistically; a stale one wastes attention but cannot break a build. Trust them unless the base is already marked drifted.

## Gaps — when the skills and the base are all silent

Some questions fall between architecture skills (too fork-specific for them) and the base (never written down). Do not fill the hole from memory of other forks. Derive from precedent:

1. Rephrase the question as a countable repo query ("do any `.tsx` live under the overlay dir?" → find/count them).
2. Run it. The majority pattern IS the local convention; record the derived fact in the brief with its evidence and command.
3. No precedent at all (first-of-its-kind in this fork)? Compare against the upstream lineage (a read-only upstream checkout, if the workspace rules list one) and mark the fact as *derived, not local* — lower confidence, say so.
4. Feed the derived fact into the base after the task — the next agent should not re-derive it.

## Binding brief format

A checklist, not documentation:

```text
Task: <one line>
Repo: <path>  Base: <base dir>  Skills: <architecture skills engaged>
Invariants (skill): <2-6 bullets that constrain the design>
Local facts (base): <2-8 bullets: names, paths, wiring, policies — each with source file>
Verify first: <rg/Test-Path commands for facts that could have drifted>
Conflicts/gaps: <where layers disagreed and which layer won>
```

Example — "add a TGUI settings panel to a Vanderlin-family fork":

```text
Task: new TGUI settings panel for X
Repo: <workspace>/SomeVanderlinFork  Base: <repo>/ai_navigation  Skills: byond-ss13-coding, ss13-tgui, tgstation-modular-content
Invariants: entry via SStgui.try_update_ui; no stored datum/tgui refs; autoupdate off +
  push at change sites; ui_act params are hostile; new files live in the overlay layer.
Local facts: entry proc is ui_interact (tgui_guide.md); component import path per
  tgui_guide.md; DM files under the overlay dir (modular_guide.md); route registration per
  local routes table (tgui_guide.md).
Verify first: rg "ui_interact" <one neighboring interface>; ls tgui/packages/tgui/interfaces
Conflicts/gaps: tgui_guide.md names index.ts — repo has index.tsx (code wins; base flagged)
```

## Conflict resolution

| Disagreement | Winner | Then |
|---|---|---|
| Base vs code | Code | Fix the base, re-sync (see `integrity.md`) |
| Architecture skill vs code | Code | Fork divergence, not a broken invariant — record the variant in the skill (enrichment) |
| Skill vs base, about a **fork-local fact** (name, path, what exists) | Base | Skills generalize; bases enumerate. Still grep |
| Skill vs base, about a **framework invariant / anti-pattern** | Skill | A base recommending an anti-pattern (act polling, stored UI refs) is wrong — fix the base |
| Two bases claim one repo | Registry | Fix the registry; one repo, one base |

## Feedback loop (enrichment)

Binding is where knowledge gaps surface. Route each discovered fact to the layer matching its generality:

- **True everywhere** (a fork variant of a proc name, a routing mechanism variant, a transferable debugging lesson) → the architecture skill, via its enrichment intake (dev advice → PR archaeology → skill).
- **True in this fork** (a recurring local recipe, a local policy) → the semantic base.
- **True for one subsystem** (impact map, development protocol) → that subsystem's deep map.

Misfiled knowledge is the main way both layers rot: fork facts in a skill silently break other forks; invariants copy-pasted into bases go stale the moment the skill improves.
