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
2. **Controller Gate 1** — a new numbered node *in front of the default* (currently node 5), with
   its domain guard. This is the only place routing may be defined.
3. Controller's *Architecture skills this controller binds* table — invariants + which base files
   to bind (or an explicit "none", as `ss13-tgs-deploy` has).
4. Controller frontmatter `description` — it lists the skills by name.
5. `README.md` — the *Что внутри* table **and** the mermaid dependency tree.
6. `docs/skills-guide.ru.md` **and** `docs/skills-guide.en.md` — both, always paired.

Then run `claude plugin validate ./plugins/ss13-byond` and `claude plugin validate .`.

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

- `ai_navigation_tg_banda/` is an empty, git-untracked leftover directory.
- Benchmarks in `docs/benchmarks.*.md` are single-run measurements; their limitations section says
  so, and that honesty is load-bearing — don't quote the numbers without it.
