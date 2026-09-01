#!/usr/bin/env bash
# Fingerprint an unknown SS13/BYOND checkout in one pass.
#
# Workflow step 2 ("identify the codebase family") is mechanical, deterministic,
# and runs before every other step -- so it is the one place in this skill that
# earns an exact command rather than prose. Getting it wrong misroutes
# everything downstream: you apply tg idioms to a fork that never adopted them,
# or look for `PROC_REF` in a pre-515 codebase.
#
# Read-only. Prints the seven checks from references/repository-profiles.md
# (Fingerprinting an unknown codebase) and nothing else.
#
# Usage:  bash fingerprint.sh [path-to-checkout]     (defaults to .)

set -u
R="${1:-.}"

if [ ! -d "$R" ]; then
  echo "not a directory: $R" >&2
  exit 1
fi

dme=$(ls "$R"/*.dme 2>/dev/null | head -1)
if [ -z "$dme" ]; then
  echo "no .dme at $R -- not a BYOND project root?" >&2
  exit 1
fi

# 1. project file + include style
echo "project file : $(basename "$dme")"
echo "includes     : $(grep -c '^#include' "$dme" 2>/dev/null) lines in the .dme"

# 2. local instructions -- these outrank the skill, so they are listed first
found=""
for f in AGENTS.md CLAUDE.md CONTRIBUTING.md .github/guides SpacemanDMM.toml ai_navigation; do
  [ -e "$R/$f" ] && found="$found $f"
done
echo "local rules  :${found:- none found}"

# 3. modular roots. Note the .dme uses backslashes on Windows-authored repos,
#    so the include grep must accept either separator or it silently reports 0.
roots=$(ls -d "$R"/modular*/ "$R"/master_files/ 2>/dev/null | sed 's|.*/\([^/]*\)/$|\1|')
if [ -n "$roots" ]; then
  echo "modular roots:"
  for n in $roots; do
    inc=$(grep -ciE "^#include \"$n[\\/]" "$dme" 2>/dev/null)
    dmf=$(find "$R/$n" -name '*.dm' 2>/dev/null | wc -l)
    printf '  %-28s %5s .dm files  %5s includes\n' "$n" "$dmf" "$inc"
  done
  echo "  (an include is load-bearing; a file on disk can be dead -- rank by includes"
  echo "   when commit history is too short to rank by commits)"
else
  echo "modular roots: none -- treat as a hard fork, not an upstream-tracking one"
fi

# 4. toolkit depth: is the tg toolkit living idiom or an imported skeleton?
for sym in 'RegisterSignal(' 'AddComponent(' 'addtimer('; do
  printf 'uses %-18s %s files\n' "${sym%(}" \
    "$(grep -rl "$sym" --include='*.dm' "$R" 2>/dev/null | wc -l)"
done

# 5. era markers
spt=$(grep -rl 'seconds_per_tick' --include='*.dm' "$R" 2>/dev/null | wc -l)
dtm=$(grep -rl 'delta_time'       --include='*.dm' "$R" 2>/dev/null | wc -l)
pr=$(grep -rl 'PROC_REF('         --include='*.dm' "$R" 2>/dev/null | wc -l)
echo "era          : seconds_per_tick=$spt  delta_time=$dtm  PROC_REF=$pr"
echo "               (spt-dominant = current tg; dt-dominant = ~2020-23 snapshot;"
echo "                PROC_REF absent = pre-515, use .proc/name)"

# 6. UI stack
ui=$(grep -rl 'ui_interact('   --include='*.dm' "$R" 2>/dev/null | wc -l)
tg=$(grep -rl 'tgui_interact(' --include='*.dm' "$R" 2>/dev/null | wc -l)
echo "ui stack     : ui_interact=$ui  tgui_interact=$tg  tgui/=$([ -d "$R/tgui" ] && echo yes || echo no)  nano/=$([ -d "$R/nano" ] && echo yes || echo no)"
echo "               (the larger of the two entry procs is this fork's name for it)"

# 7. lint infra -- defines what "passes checks" means locally
ci=$(ls "$R"/.github/workflows/*.y*ml 2>/dev/null | wc -l)
echo "lint/CI      : SpacemanDMM.toml=$([ -f "$R/SpacemanDMM.toml" ] && echo yes || echo no)  workflows=$ci"
