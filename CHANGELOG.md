# Changelog

There are no version numbers here, on purpose. The plugin manifest omits
`version`, so the git SHA *is* the version and subscribers track the default
branch's latest commit (see `CLAUDE.md` → Conventions). Entries are therefore
dated, and describe what changed **for someone using the skills** — not what
each commit touched. Most commits in this repo are automatic working-tree
sweeps named `Update`; reading them is not a substitute for this file.

To pull any of this:

```bash
claude plugin marketplace update ss13-ai-skills
claude plugin update ss13-byond@ss13-ai-skills
```

Both commands are required — the first refreshes the catalogue, the second
installs. Nothing arrives without them.

---

## 2026-09-01

**`byond-ss13-coding` — engine facts corrected after an external review.** An
experienced SS13 engineer raised ten objections; seven held after checking
against the official DM Reference, a live tgstation checkout and the engine
developer's own statements. Now fixed in the skill:

- `static` and `global` are one modifier with a single storage slot, so a
  static **cannot** be overridden per subtype — which constrains the shared
  scratch-list pattern the performance reference recommends.
- `sleep` stops the whole caller chain; `spawn` defers only the indented block
  and the current proc keeps running. The contrast is now stated explicitly.
- `world.cpu` and `map_cpu` are **running averages**, not per-tick readings, and
  `tick_usage` under 100 can still be overtime. Don't quote them about one tick.
- Blur pass count scales with radius rather than being a flat two; the dominant
  cost is added render contexts, not shader maths.
- `/mutable_appearance` promoted from a footnote to the intended mechanism for
  avoiding temporary-appearance churn.
- `do_after` documented as a **blocking** `while` + `stoplag()` loop that already
  re-checks user/target state — relax it via `timed_action_flags`, don't
  re-implement those checks.
- On tg, `SSspatial_grid` beats re-scanning with `view()` — but only for the
  three categories it indexes (hearers, client mobs, atmos machines).

Three objections did **not** hold and the skill was deliberately left unchanged:
"use lazylists always" (tg's own docs scope them to hot types with
rarely-used lists), "qdel calls `del` anyway" (only on the hard-delete path),
and "the view maximum is bigger than 70×70" (the Reference says ~5000 tiles;
the real nuance, now recorded, is that the limit is an *area*).

**`ss13-tgui` — React guidance scoped to tgui's render model.** New section
covering four rules that are correctness rather than micro-optimisation
(no components inside components; derive during render instead of mirroring
backend data through `useEffect`; lazy `useState` initialisers; functional
`setState`), with an explicit instruction to discard waterfall/bundle/server
advice from general React sources — measured against a live fork, none of it
has any referent in tgui.

**Semantic bases marked stale.** Every `ai_navigation_*` base now carries a
dated STALE banner. They remain routing aids; do not quote identifiers from
them without grepping the code. (Bases are not shipped to subscribers.)

**Tooling.** `scripts/run_evals.py` added — the 54 evals across five skills had
never been executed. `verify_claims.py` now accepts a list of project files.
`byond-codemaster-controller` gained a `claims.yaml`, the last skill without one.
Root `AGENTS.md` added for non-Claude agents working on the repo.

## 2026-08-31

**The repo became a Claude Code plugin and marketplace.** Install is now
`claude plugin marketplace add PatapoIIIa/ai-skills` then
`claude plugin install ss13-byond@ss13-ai-skills`. Skills moved to
`plugins/ss13-byond/skills/` (with `git mv`, so history survives) and are
namespaced `ss13-byond:<name>` at runtime.

**Routing consolidated.** The controller's flat dispatch table became two
sequential gates; `ss13-tgs-deploy` — previously invisible to routing — became
Gate 1's first node as an operations axis that works alone. Each architecture
skill now declares only its own boundary, and the duplicated interaction matrix
and truth hierarchy were deleted from the skills that restated them.

**Repo hygiene**, borrowed from the `wow-addon` plugin after evaluating it: a
maintainer brief (`CLAUDE.md`), a `.gitattributes` LF policy (81 tracked files
carried CRLF, and the shipped deploy `.sh` files run on Linux), and the missing
`LICENSE` (MIT was declared in the manifest but no licence text shipped).

## 2026-07-18

**`ss13-tgui` validated against live tgstation.** Three defects fixed: a false
causal claim about why upstream avoids the `getFlatIcon` canvas bug, the
`parent: config.window` rule (legacy in-tree only — modern tgui-core parents
itself), and a stale `map_popups.dm` path. The `getFlatIcon` bug itself was
confirmed verbatim in master and, later, in a Vanderlin-family fork.

## 2026-07-20

`ss13-tgs-deploy` added — TGS/Docker deployment, written from a real
deployment rather than from documentation.

## 2026-07-15 — first public version

Four skills: the controller plus `byond-ss13-coding`, `ss13-tgui` and
`tgstation-modular-content`.

---

*Entries before 2026-08-31 are reconstructed from the repository history and
working notes; they record the changes that mattered, not every edit.*
