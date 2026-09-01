# Source Index

Where this skill's fork claims come from and which of them have been re-checked against a live checkout. This skill's content is *conventions*, not engine semantics — and a convention is exactly the kind of claim that rots quietly, because a fork can rename its modular root or change its include mechanism without anything failing loudly.

The rule this file enforces: **a named folder, tag, or file path in this skill is a landmark to grep for, never a landmark to assume.** Where a claim could not be re-verified, it says so rather than reading as fact.

## Grades

| Tag | Meaning |
|---|---|
| `[verified YYYY-MM-DD]` | Grepped against a live checkout on that date; the command and the result are recorded below |
| `[observed]` | Read off a real checkout when the skill was authored, but not present in any checkout available for re-verification |
| `[reasoned]` | A design judgement built on verified facts — argued, not measured |

## Verification pass — 2026-09-01

Static, read-only greps against local checkouts. Six repositories were reachable; the ones that carry a modular convention are named by repository and project file, per this repo's identification rule.

### Bubberstation (`tgstation.dme`) — every claim confirmed

| Claim | Result |
|---|---|
| Modular roots `modular_skyrat/` and `modular_zubbers/` | `[verified 2026-09-01]` both present |
| `master_files/` mirrors the upstream path | `[verified 2026-09-01]` present at `modular_zubbers/master_files/`, containing `code/`, `icons/`, `skyrat/` |
| Self-contained modules in `modules/<feature>/` | `[verified 2026-09-01]` present, e.g. `ammo_workbench/`, `jobs/`, `plexagon_navsec/` |
| The fork's own handbook is `modular_zubbers/readme.md` | `[verified 2026-09-01]` present |
| Includes go between `// BEGIN_INCLUDE` / `// END_INCLUDE` in `tgstation.dme` | `[verified 2026-09-01]` both markers present |
| Late-loading defines folder `code/__DEFINES/~~bubber_defines/` | `[verified 2026-09-01]` present, `~~` prefix intact |
| Automapper config at `_maps/.../automapper/automapper_config.toml` | `[verified 2026-09-01]` present at `_maps/bubber/automapper/automapper_config.toml` |
| tgui fork-file marker `// THIS IS A BUBBER UI FILE` | `[verified 2026-09-01]` present in multiple `interfaces/` files |
| `BUBBER EDIT` / `SKYRAT EDIT` upstream-edit tag grammar | `[verified 2026-09-01]` 1351 `BUBBER EDIT` and 1845 `SKYRAT EDIT` occurrences under `code/`; a third form, `ZUBBER EDIT`, appears exactly once and is **not** an established tag — do not copy it |

Bubberstation is the focus fork and it holds up completely. Nothing on this page's Bubberstation guidance needs qualification.

### cmss13-MARINES (`colonialmarines.dme`) — confirmed as the counter-example

| Claim | Result |
|---|---|
| No modular root; edits `code/` directly | `[verified 2026-09-01]` no `modular_*` and no `master_files/` exist |
| Ships `code/__pragmas.dm` as a lint safety net | `[verified 2026-09-01]` present |

### Vanderlin and Roguetown lineages — the aggregator could not be re-verified

This is the finding that changed the skill.

`modular_abel/` and its `_module.dm` aggregator are described in `fork-comparison.md` in enough concrete detail (`erp/`, `dun_world/`, `races/`, `force_load.dm`, `config/map.json`, a disposable `vanderlin.modular_abel.dme`) that they were plainly read off a real tree — they are `[observed]`, not invented. But **no checkout available on 2026-09-01 contains them**, so the pattern could not be re-confirmed, and the forks that *are* available contradict the impression that it is the family norm:

| Repository | Project file | Modular roots found | Include mechanism |
|---|---|---|---|
| Rivermist-Hollow-Vanderlin | `vanderlin.dme` | `modular_alizeria/`, `modular_ratwood/`, `modular_rmh/` | flat per-file `#include` list |
| Twilight-Axis | `roguetown.dme` | `modular/`, `modular_deserttown/`, `modular_twilight_axis/` | flat per-file `#include` list |
| Ratwood-2.0 | `roguetown.dme` | ten roots, including `modular_azurepeak/`, `modular_causticcove/`, `modular_ochrevalley/`, `modular_twilight_axis/` | flat per-file `#include` list |
| Lands-of-Alizeria | `roguetown.dme` | six roots | flat per-file `#include` list |

`_module.dm` exists in **none** of the four. A downstream fork of an aggregator codebase does not inherit the aggregator.

Consequences already applied to the skill: step 4 of the workflow now says to grep the `.dme` rather than assume a mechanism, and `fork-comparison.md` carries a rarity warning under its include-style recommendation. The aggregator's *design* argument (one stable `.dme` line versus thousands of churned ones) is untouched — that remains `[reasoned]` and sound; only the claim about how commonly you will meet it was overstated.

### The active-root heuristic — verified, and sharpened

The workflow told you to check "`git log -1 -- <dir>` and recent commit counts". Measured on Twilight-Axis, 2026-09-01:

| Root | Commits touching it | Last commit |
|---|---|---|
| `modular_twilight_axis/` | 3305 | 2026-08-23 |
| `modular/` | 743 | 2026-08-22 |
| `modular_deserttown/` | 2 | 2026-08-22 |

**Commit count separates the live root from the fossils by a factor of 4.5; the last-commit dates all fall inside a single day and separate nothing.** Half of the original advice was actively misleading, so step 1 now leads with the count and ships the one-line ranking command. Ratwood-2.0's ten roots make the same point at greater scale: on a fork that old, "which folder is current" is not answerable by looking.

## What is still unverified

- **Everything about upstream Vanderlin** — `modular_abel/`, the theme-based override layout, `upstream_fixes.dm`, the `force_load.dm` readme habit, the temp-DME build, the map-import pipeline. All `[observed]`, none re-checkable here. Treat them as one fork's documented practice, not as a family norm.
- **The compile-verification note** at the top of `fork-comparison.md` (same-type var add, subtype, `. = ..()` wrap, single-file define, DM 516, 0 errors) was not re-run in this pass. It remains as recorded.
- **`extension-recipes.md`** was not audited recipe-by-recipe; its per-content-type steps rest on the same Bubberstation layout verified above, but the individual recipes have no independent verification.
- **Nothing here is checked against upstream tgstation itself.** This skill is about downstream forks; where a claim concerns engine or DM semantics rather than fork convention, `byond-ss13-coding` is the authority.

## Re-running this pass

Every check above is a one-liner against a checkout. Identify repositories by name and project file, never by a path on someone's disk:

```bash
ls -d modular_* master_files 2>/dev/null                  # roots
for d in modular*/; do echo "$(git rev-list --count HEAD -- "$d") $d"; done | sort -rn
grep -c "BEGIN_INCLUDE\|END_INCLUDE" <project>.dme        # include mechanism
find . -maxdepth 3 -name "_module.dm"                     # aggregator?
ls -d code/__DEFINES/~~*                                  # late-loading defines
find _maps -name "automapper_config.toml"                 # modular maps
grep -rho "[A-Z]* EDIT" code | sort | uniq -c | sort -rn  # the real tag grammar
```

When a claim is re-confirmed, add the date beside the existing one rather than replacing it — a convention that held on two dates is worth more than one that was silently rewritten.
