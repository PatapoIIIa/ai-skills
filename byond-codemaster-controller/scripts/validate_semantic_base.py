#!/usr/bin/env python3
"""Validate a semantic base (ai_navigation_* directory) against its repository.

Checks that path-like references inside the base's Markdown files resolve:
  - internal refs (ai_navigation/xxx.md, or bare xxx.md present in the base) -> base dir
  - repo refs (code/**, modular*/**, tgui/**, *.dme, ...) -> one of the --repo roots

Usage:
  python validate_semantic_base.py <base-dir> --repo <repo-root> [--repo <root2>] [--strict]

Exit code 0 = clean, 1 = missing references found.
"""
import argparse
import re
import sys
from pathlib import Path

BACKTICK = re.compile(r"`([^`\n]+)`")
LINE_SUFFIX = re.compile(r":[0-9][0-9,:-]*$")
KNOWN_EXT = (".dm", ".dme", ".md", ".tsx", ".ts", ".scss", ".dmi", ".json", ".py", ".yml", ".yaml", ".toml")
SKIP_CHARS = set("<>$(){}|\"' ")
# DM language tokens that masquerade as paths: /datum/foo type paths, var/name, proc refs
DM_ROOTS = {"var", "proc", "list", "datum", "obj", "mob", "turf", "area", "atom",
            "client", "world", "image", "icon", "sound", "matrix", "regex", "savefile"}


def candidate_paths(md_text):
    for token in BACKTICK.findall(md_text):
        token = token.strip().rstrip(".,;")
        if not token or any(c in SKIP_CHARS for c in token):
            continue
        if token.startswith(("http", "rg ", "#", "-", "/", "./", "../")) or "..." in token:
            continue  # leading "/" = BYOND type path, not a file path
        if any(seg.isupper() for seg in token.split("/")):
            continue  # RUNLEVEL_LOBBY/SETUP/... style define alternatives
        if token.count("/") == 1 and not token.endswith("/") and "." not in token.split("/")[1]:
            continue  # word alternatives like `pixel_x/y`, `jobs/migrants`
        token = LINE_SUFFIX.sub("", token)
        has_sep = "/" in token or "\\" in token
        if not has_sep and not token.lower().endswith(KNOWN_EXT):
            continue
        if re.fullmatch(r"\.\w+", token):
            continue  # bare extension like `.md`
        if not re.fullmatch(r"[\w.\\/*?-]+", token):
            continue
        token = token.replace("\\", "/")
        if token.split("/")[0] in DM_ROOTS:
            continue
        yield token


def strip_glob(token):
    """Return the concrete prefix of a glob token ('code/modules/**' -> 'code/modules')."""
    if any(c in token for c in "*?"):
        parts = []
        for part in token.split("/"):
            if any(c in part for c in "*?"):
                break
            parts.append(part)
        return "/".join(parts)
    return token


def resolves(token, base_dir, repos):
    concrete = strip_glob(token).strip("/")
    if not concrete:
        return True  # pure glob like '**' — nothing checkable
    rel = concrete
    if rel.startswith("ai_navigation/"):
        rel_in_base = rel[len("ai_navigation/"):]
        return (base_dir / rel_in_base).exists()
    # bare .md files usually refer to siblings inside the base
    if "/" not in rel and rel.endswith(".md"):
        return (base_dir / rel).exists()
    if (base_dir / rel).exists():
        return True
    for repo in repos:
        if (repo / rel).exists():
            return True
    # bare filename (e.g. roguetown.dme): only check repo roots, else unresolvable
    if "/" not in rel:
        return None
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("base_dir", type=Path)
    ap.add_argument("--repo", action="append", type=Path, default=[], help="repository root(s) this base describes")
    ap.add_argument("--strict", action="store_true", help="also report unresolvable bare filenames")
    args = ap.parse_args()

    base_dir = args.base_dir.resolve()
    repos = [r.resolve() for r in args.repo]
    if not base_dir.is_dir():
        sys.exit(f"not a directory: {base_dir}")

    missing, unresolved, checked = [], [], 0
    for md in sorted(base_dir.rglob("*.md")):
        seen = set()
        for token in candidate_paths(md.read_text(encoding="utf-8", errors="replace")):
            if token in seen:
                continue
            seen.add(token)
            checked += 1
            ok = resolves(token, base_dir, repos)
            if ok is False:
                missing.append((md.name, token))
            elif ok is None:
                unresolved.append((md.name, token))

    print(f"base: {base_dir.name}  repos: {[r.name for r in repos] or 'none'}  refs checked: {checked}")
    for name, token in missing:
        print(f"  MISSING   {name}: {token}")
    if args.strict:
        for name, token in unresolved:
            print(f"  unresolved {name}: {token}")
    print(f"missing: {len(missing)}  unresolved bare names: {len(unresolved)}")
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
