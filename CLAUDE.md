# CLAUDE.md — ai-skills

## What this repo is

A **Claude Code plugin** (not an SS13 fork, and not a codebase that compiles). It ships a skill
ecosystem for SS13 / BYOND work. Everything here is Markdown skill specs, JSON manifests, a couple
of Python/shell helpers and documentation — there is no build and no test suite.

The repo is simultaneously a **marketplace** (root `.claude-plugin/marketplace.json`, name
`ss13-ai-skills`) and the host of exactly one **plugin** (`plugins/ss13-byond/`, name `ss13-byond`).
Users subscribe with:

```
claude plugin marketplace add PatapoIIIa/ai-skills
claude plugin install ss13-byond@ss13-ai-skills
```

## Module map

- `.claude-plugin/marketplace.json` — marketplace entry. `metadata.pluginRoot` is `./plugins`.
- `plugins/ss13-byond/.claude-plugin/plugin.json` — the plugin manifest.
- `plugins/ss13-byond/skills/*/SKILL.md` — five skills, each with its own `references/`
  (progressive disclosure), and some with `scripts/`, `assets/`, `evals/`, `agents/`.
  Skills are namespaced at runtime as `ss13-byond:<name>`.
- `ai_navigation_*/` — semantic bases for specific forks. **Data, not skills, and deliberately
  outside the plugin** so subscribers never receive fork-specific state. Do not move them in.
- `docs/` — bilingual user guides and benchmark tables. `README.md` — the public face.
- `scripts/validate_ecosystem.py` — repo-maintenance only, deliberately **outside** `plugins/` so
  subscribers never receive it. Checks the invariants below mechanically.
- `scripts/check_versions.py` + `scripts/version_watch.yaml` + `scripts/version_baseline.json` —
  the upstream version watch. Reads pins over HTTPS from the canonical repos, never from clones.
- `scripts/verify_claims.py` + `plugins/*/skills/*/claims.yaml` — the claim-drift workflow. The
  YAML ships with each skill (path-free, so a subscriber can run it too); the runner is
  maintenance-only. See *Claim drift* below.
- `scripts/render_version_table.py` — regenerates the README block between
  `<!-- versions:start -->` / `<!-- versions:end -->`. The workflow runs it and commits
  the result, so the public table never has to be updated by hand.
- `.github/workflows/skill-truth.yml` — weekly CI. Runs the two network-only checkers,
  refreshes the README table, and backs the badge at the top of the README.
- `scripts/hooks/post-commit` — opt-in git hook that runs the drift check on a throttle.
- `scripts/run_evals.py` — executes the eval sets that ship with each skill. Two modes:
  `routing` (default, cheap) asks which skills the model would load and checks that against
  each eval's `expect_skills`/`forbid_skills`; `full` runs the prompt and saves the transcript.
  `--dry-run` validates the eval files and prints the plan without a single model call, which is
  what CI and a nested shell can do. **The negative half is the point**: `forbid_skills` is what
  catches over-triggering, since a router that loads everything passes any purely positive check.
  Needs an authenticated `claude` CLI; an agent-run shell usually has none and it says so rather
  than pretending.
- `AGENTS.md` — the same brief as this file, shortened, for non-Claude agents that read that
  convention. `CONTRIBUTING.md` — the evidence rules a change is judged on. `CHANGELOG.md` —
  dated (not numbered, since there is no version) record of what changed for subscribers.

The five skills and the one contract that binds them: `byond-codemaster-controller` routes;
`byond-ss13-coding`, `ss13-tgui` and `tgstation-modular-content` implement on separate axes;
`ss13-tgs-deploy` is an operations skill that works alone. See the controller's dispatch gates.

## Entry points & lifecycle

Claude Code auto-discovers `skills/` by directory — there is no registration file. A skill is live
the moment its folder exists and the plugin is reloaded. To activate changes in a session:
**`/reload-plugins`** (no restart). To test without installing:
`claude --plugin-dir ./plugins/ss13-byond`.

A skill spec is YAML frontmatter (`name`, `description`) plus a Markdown body. The `description` is
what triggers model invocation, so it carries the trigger vocabulary — including Russian terms,
because the user works in both languages.

## Adding or removing a skill is a 6-touch change

Miss one and the ecosystem contradicts itself. In order:

1. `plugins/ss13-byond/skills/<name>/SKILL.md` — the spec itself.
2. **Controller Gate 1** — a new node *in front of the default node* (the last one in Gate 1), with
   its domain guard, renumbering what follows. This is the only place routing may be defined, and
   the only place that may refer to a node by number — everywhere else names nodes by role, so
   adding a skill cannot leave a stale "see node 5" behind.
3. Controller's *Architecture skills this controller binds* table — invariants + which base files
   to bind (or an explicit "none", as `ss13-tgs-deploy` has).
4. Controller frontmatter `description` — it lists the skills by name.
5. `README.md` — the *Что внутри* table **and** the mermaid dependency tree.
6. `docs/skills-guide.ru.md` **and** `docs/skills-guide.en.md` — both, always paired.

Then run all three, in this order:

```
python scripts/validate_ecosystem.py
claude plugin validate ./plugins/ss13-byond
claude plugin validate .
```

**`validate_ecosystem.py` enforces touches 2–6 mechanically** — plus link integrity, orphaned
reference/asset/script files, description length against the 1024 limit, EN+RU eval balance, the
skill-count claims in both guides, that every skill Gate 1 dispatches to actually exists, that no
file outside the gate list refers to a node by number, machine paths, CRLF and empty directories.
It exists because the 6-touch rule was aspirational until it wasn't: `ss13-tgs-deploy` shipped with
touch #6 skipped (both guides still said "four skills") and nothing caught it for six weeks. It
exits non-zero on errors, so it can gate a commit. Warnings are advisory — a description at 960
chars still loads, but it has no room left for a new trigger word.

Touch #1 is the only one the script cannot check: it has no opinion about whether the SKILL.md body
is any good.

## Version watch — the pins the skills quote

The skills quote versions: *"verified present in tgui-core 5.6.0"*, *"built rust-g 6.1.0"*,
*"needed BYOND 516.1661"*. `scripts/check_versions.py` reads a short list of files straight from
the canonical upstreams over HTTPS and diffs the pins against a committed baseline.

```
python scripts/check_versions.py            # what moved
python scripts/check_versions.py --update   # accept current as the new baseline
```

- `scripts/version_watch.yaml` — which repos, which files, which keys, and which skill claim each
  key backs. Six upstreams: `tgstation/tgstation`, `Bubberstation/Bubberstation`,
  `cmss13-devs/cmss13`, `Monkestation/Vanderlin`, `Rotwood-Vale/Ratwood-2.0`,
  `Azure-Peak/Azure-Peak`; files `dependencies.sh` and `tgui/packages/tgui/package.json`.
- `scripts/version_baseline.json` — machine-written, **committed on purpose**: `git log -p` on it
  is the record of when each project moved a pin.

Outcomes are `MOVED`, `NEW`, `GONE` (tgstation deleted `NODE_VERSION_LTS`, so keys really do
vanish) and `SAME`. When a moved key backs a claim, the report names the claim that now needs
re-reading — and stays quiet when the new value is still inside the claim's `verified_at` set.

**Read upstream, never a local clone. This is the whole point of the file.** Measured 2026-09-01,
the `tgstation` working tree on this machine was **1039 commits behind its own `origin/master`**
and still reported `BYOND_MINOR=1659` when upstream said `1685`. A watch that reads clones reports
how stale your clones are.

**And read the upstream the claim is actually about.** Checking `ss13-tgs-deploy`'s recorded
`RUST_G_VERSION=6.1.0` against a locally available *downstream* Vanderlin fork reported drift
(3.9.0) and looked like the skill had rotted. It had not: `Monkestation/Vanderlin` still pins
6.1.0 and BYOND 516.1661 on master, exactly what the skill records. The fork simply lags. That is
what `scope_repo` in `claim_links` exists for.

*Transport note:* Python's TLS trust store rejects the certificate chain on this machine
(`Basic Constraints of CA cert not marked critical`), so the script falls back to `curl`, which
verifies against a different store. Verification is never disabled; if both refuse, the run reports
the failure. `--offline-ok` makes an unreachable network a non-finding rather than an error.

### The README table is generated, the baseline is not

`render_version_table.py` rewrites the README block on every CI run and commits it, so the public
"skill's version vs reality" table is always live. It deliberately **never writes
`version_baseline.json`**: the baseline is a human acknowledgement that an affected claim has been
re-read, and auto-accepting it in CI would silently swallow the alert `check_versions.py` exists to
raise. The table describes reality, the baseline records what has been accepted, and they are
allowed to disagree — that disagreement is the finding.

Consequences worth knowing:

- A red badge after an upstream version bump is **correct**, not a malfunction. Clear it by
  re-reading the affected claim and then running `check_versions.py --update`.
- The workflow needs `contents: write` for that one commit. Nothing else in it writes.
- No trigger loop: the push filter covers `scripts/**` and `claims.yaml` but not `README.md`, and
  a `GITHUB_TOKEN` push does not start a workflow anyway.
- `actions/checkout` leaves a detached HEAD on push and schedule events, so the commit step pushes
  to `HEAD:${{ github.ref_name }}` explicitly.

## Claim drift — the skills assert facts that expire

`validate_ecosystem.py` checks that the repo agrees with *itself*. `verify_claims.py` checks that
the skills still agree with **the repositories on this machine**: that `modular_zubbers/` is still
where Bubberstation puts modular content, that `BUBBER EDIT` is still the tag, that a cited
`code/...` path still resolves. Nothing fails loudly when a fork renames a folder — the skill just
starts handing out stale facts with full confidence.

**Division of labour with the version watch above: pins are watched upstream, layout is checked
locally.** No `claims.yaml` carries a version check any more — those moved to `version_watch.yaml`
after local clones produced four false drift reports.

That split is measured, not assumed. Every clone in this workspace points at a **personal fork**
rather than the canonical repo (`PatapoIIIa/tgstation`, not `tgstation/tgstation`) and several are
months stale, so it was a fair question whether layout claims survive it. They do: **21 of 21 paths
checked against the canonical upstreams on 2026-09-01 agreed with clones up to 1039 commits
behind**, because folder conventions move on a scale of years while version pins move weekly. The
local run now prints each checkout's origin, HEAD date and behind-count, so nobody has to take that
on trust.

To take clones out of the loop entirely:

```
python scripts/verify_claims.py --source upstream
```

This reads the canonical repositories through the GitHub trees API — one request each, no clone
touched. It answers `paths_exist` and `paths_absent` only; `grep` needs file contents and
`commit_rank` needs history, so both report SKIP with that reason rather than guessing. Targets
carry `upstream: owner/repo` and `branch:` for this. A claim that is inherently about downstream
state carries `scope: local` and is skipped upstream, because pointing it at the canonical repo
would answer a different question convincingly — `aggregator-not-inherited-downstream` is the case
that forced the flag.

**Set `branch:` from the repository's real default.** Three of the six watched repos default to
`main`; all three also still have a `master` carrying identical pins today, which is precisely the
trap — a stale mirror branch returns plausible, frozen data instead of an error.

Each skill's claims live in `<skill>/claims.yaml`, next to the prose ledger in
`references/source-index.md` that they mechanise. **Repositories are identified by project file and
content markers, never by a path** — the runner supplies paths by scanning a workspace at runtime,
so the YAML stays shippable and machine-independent.

```
python scripts/verify_claims.py                    # scan the parent directory
python scripts/verify_claims.py --workspace PATH   # scan somewhere else
python scripts/verify_claims.py --skill ss13-tgui  # one skill
```

Three outcomes, and the middle one is the point:

| | Meaning | What to do |
|---|---|---|
| `OK` | reality still matches | nothing |
| `DRIFT` | reality moved; the claim is not wrong, it is **unverified again** | re-read the claim against the new version, then update `last_verified` |
| `BROKEN` | reality contradicts the claim; the skill now says something false | fix the skill |

**DRIFT is not a defect in the fork** and is the normal steady state — forks bump `tgui-core`
constantly. It is a queue of evidence that has expired.

Check types: `paths_exist`, `paths_absent` (both glob), `grep` (with `min_count`), `pin` (reads
`dependencies.sh`-style `export NAME=value` or `package.json` deps, compares against
`verified_at`), and `commit_rank`. Scope a hard claim to upstream via `name_hint` rather than
letting an old fork's lag register as the convention changing; use `missing_key: skip` where a fork
that never adopted something is out of scope rather than a counter-example.

**Scheduling — weekly or every 10 commits, whichever comes first.** The triggers are OR'd:

```
python scripts/verify_claims.py --every-commits 10 --max-age-days 7
```

State lives in `.git/skill-drift/` (machine-local, never committed). `scripts/hooks/post-commit`
wires this up; install it deliberately, it is not automatic:

```
cp scripts/hooks/post-commit .git/hooks/post-commit && chmod +x .git/hooks/post-commit
```

The hook backgrounds the run and `post-commit` cannot fail a commit, so committing never waits.
A full scan across ten checkouts is ~1.6 s: `grep` checks stop as soon as `min_count` is cleared,
which is what keeps it hook-sized (it was 14 s before that).

For a weekly run without a hook, schedule the same command with `--max-age-days 7`; it no-ops when
called too soon, so over-scheduling is harmless.

**When a check is wrong, fix the check.** The first run produced four `BROKEN`s that were all
instrument error — `ByondUi` lives in `node_modules/tgui-core` (no fork vendors it in-tree) and
CEV-Eris predates the Bun build. Narrow the target or scope the claim; do not record an
instrument defect as a skill defect.

## Conventions & footguns

- **`version` is deliberately absent from `plugin.json`.** That makes the git SHA the version, so
  subscribers track the default branch's latest commit with no manual bumps. `claude plugin
  validate` emits a warning about it — **the warning is intentional; do not "fix" it by pinning a
  version.** Pinning would silently freeze every existing subscriber.
- **The local `claude plugin validate` is stricter than the published docs.** It rejected
  `displayName` in `plugin.json` and `$schema` + top-level `description` in `marketplace.json`
  (marketplace description belongs at `metadata.description`). Trust the CLI over the docs, and
  re-run it after every manifest edit.
- **Routing lives in exactly one place.** The controller's dispatch gates are the single source of
  truth; each other skill declares only its own boundary. If a skill appears to restate the
  interaction matrix, that copy is drift — delete it there rather than forking the logic. The same
  applies to the truth hierarchy, which exists once, in the controller.
- **No machine-specific paths and no usernames anywhere tracked in this repo** — skills *and*
  semantic bases alike, since the whole repo is public. Identify a repository by name and project
  file (`Twilight-Axis`, `roguetown.dme`), never by where it sits on someone's disk. Before
  finishing, grep the tree for `C:\`, `C:/`, `/home/`, `/Users/`.
- **Never write a third party's handle or nickname into any file here.** Sources are tagged by
  *role* — `[DM Ref]`, `[tg]`, `[dev]`, `[community]`, `[heuristic]`, `[measure]` — never by
  identity. This applies to skills, docs and commit messages.
- **Example prompts come in EN + RU pairs.** Eval sets, docs and skill examples all follow this;
  a single-language example is an incomplete one.
- **Engine claims are verified, not recalled.** A tier-1 BYOND fact needs the official DM Reference
  (local `help/ref/info.html`, or the mirror at `ref.dm-lang.org`); a claim about tg conventions
  needs a grep against a live tgstation checkout. Record what was checked in the skill's
  `source-index.md` / `source-corpus.md`, and mark anything unverified as such rather than
  promoting it to fact.
- **Honest reporting is a hard rule inside the skills, and it binds work on the skills too.** Never
  state that something compiled, ran, or passed unless the command executed and its output was
  seen. "Validated the manifest" and "loaded the plugin in a session" are different claims.
- **Line endings are pinned LF** by the root `.gitattributes`. The shipped
  `ss13-tgs-deploy/assets/*.sh` run on a Linux host, where a CRLF after the shebang makes the
  kernel look for an interpreter named `bash\r`.

## Known state

- **Every `ai_navigation_*` base is stale (audited 2026-09-01) and none should be trusted for literal
  identifiers.** They are routing aids: follow one to the right area of the code, then read the code.
  Each base's `AGENTS.md` and `router.md` now carries a dated STALE banner with its own numbers.
  Measured: `ai_navigation_twilight` — 0 broken path refs, generated 2026-07-09, entry-proc claim
  re-verified, the healthiest; `ai_navigation_tg_banda_kaga` — 11 broken refs and **no generation
  stamp at all**; `ai_navigation_vanders_river` — 24 broken refs, stamps up to ~6 months old, the
  worst. Regenerate rather than patch: the controller can rebuild any base from `file-specs.md`.
  Two lessons from the audit worth keeping: drift can *resolve itself* (this base warns
  `SSmove_manager` may be absent from Vanderlin; it now exists), and `validate_semantic_base.py`
  reports skill-relative pointers such as `references/performance.md` as MISSING — those are
  **false positives** (the base names the owning skill in the same sentence), so filter them out
  before counting: 15 raw findings in that base were 11 real.
- `ai_navigation_tg_banda/` is an empty, git-untracked leftover directory.
- Benchmarks in `docs/benchmarks.*.md` are single-run measurements; their limitations section says
  so, and that honesty is load-bearing — don't quote the numbers without it.
