#!/usr/bin/env python3
"""Read-only scanner for common SS13 TGUI review smells.

This is not a linter. It prints suspicious locations so Codex can inspect them
with the appropriate reference playbook.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


DEFAULT_EXTENSIONS = {
    ".dm",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".scss",
    ".css",
}


@dataclass(frozen=True)
class Rule:
    code: str
    severity: str
    pattern: re.Pattern[str]
    hint: str


RULES = [
    Rule(
        "base64-payload",
        "warn",
        re.compile(r"\bicon2base64\s*\(|data:image/|base64", re.IGNORECASE),
        "Generated/base64 image payload. Good for rare dynamic snapshots; for repeated catalogs, check ui_assets()/spritesheets.",
    ),
    Rule(
        "static-data-refresh",
        "info",
        re.compile(r"\bui_static_data\b|\bupdate_static_data(?:_for_all_viewers)?\b"),
        "Static data path. Verify this payload is stable and full refreshes are intentional.",
    ),
    Rule(
        "manual-ui-update",
        "warn",
        re.compile(r"\bsend_update\s*\(|var/datum/tgui/(?!ui\b)\w+|open_uis"),
        "Manual UI refs/open_uis/send_update. Prefer SStgui.update_uis(src) and standard try_update_ui lifecycle.",
    ),
    Rule(
        "try-update-ui-control-flow",
        "warn",
        re.compile(r"if\s*\(\s*SStgui\.try_update_ui\s*\("),
        "try_update_ui used as an open-UI lookup/control-flow guard. In normal code, assign once in ui_interact.",
    ),
    Rule(
        "autoupdate-off",
        "warn",
        re.compile(r"\bset_autoupdate\s*\(\s*FALSE\s*\)"),
        "Autoupdate disabled. Verify every external mutation pushes SStgui.update_uis(src).",
    ),
    Rule(
        "cache",
        "info",
        re.compile(r"GLOBAL_LIST_EMPTY\([^)]*cache|GLOBAL_VAR_INIT\([^)]*cache|/var/list/[^\\n]*cache|cache_key", re.IGNORECASE),
        "Custom cache. Verify measured need and meaningful content/state key.",
    ),
    Rule(
        "temporary-logger",
        "warn",
        re.compile(r"WRITE_LOG|world\.timeofday|pref_log|debug_log|render_count|thumbnail_renders", re.IGNORECASE),
        "Instrumentation/timing/logger. Remove after measurement unless this is permanent observability.",
    ),
    Rule(
        "heavy-preview",
        "warn",
        re.compile(r"getFlatIcon|render_preview|apply_prefs_to|generate_or_wait_for_human_dummy|\bicon\s*\(", re.IGNORECASE),
        "Potential heavy BYOND render/icon work. Keep off hot paths or make async/signature-cached.",
    ),
    Rule(
        "client-param",
        "info",
        re.compile(r"params\[|href_list\[|(?<![A-Za-z0-9_])act\s*\("),
        "Client-supplied action data. Verify type/range/membership validation before mutation.",
    ),
    Rule(
        "deprecated-local-state",
        "info",
        re.compile(r"\buseLocalState\b"),
        "useLocalState is deprecated in modern TGUI v5. Prefer React state unless this fork still needs the old hook.",
    ),
    Rule(
        "box-as",
        "warn",
        re.compile(r"<Box[^>]*\bas=[\"'](button|section|header|strong|h[1-6]|label)[\"']", re.IGNORECASE),
        "Suspicious Box-as native tag replacement. Check native semantics/ref/attributes.",
    ),
    Rule(
        "raw-button",
        "info",
        re.compile(r"<button\b|<section\b|<h[1-6]\b"),
        "Raw HTML. Ensure it is intentional, or use local TGUI components where they carry behavior.",
    ),
]


def iter_files(paths: list[Path], extensions: set[str]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file():
            if path.suffix.lower() in extensions:
                files.append(path)
            continue
        for child in path.rglob("*"):
            if child.is_file() and child.suffix.lower() in extensions:
                files.append(child)
    return sorted(set(files))


def scan_file(path: Path, max_matches_per_rule: int) -> list[tuple[Rule, int, str]]:
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []

    hits: list[tuple[Rule, int, str]] = []
    counts: dict[str, int] = {}
    for lineno, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith(("//", "/*", "*")):
            continue
        for rule in RULES:
            if counts.get(rule.code, 0) >= max_matches_per_rule:
                continue
            if rule.pattern.search(line):
                counts[rule.code] = counts.get(rule.code, 0) + 1
                hits.append((rule, lineno, stripped))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories to scan")
    parser.add_argument(
        "--extensions",
        default=",".join(sorted(DEFAULT_EXTENSIONS)),
        help="Comma-separated file extensions to scan",
    )
    parser.add_argument("--max-matches-per-rule", type=int, default=8)
    args = parser.parse_args()

    extensions = {
        ext if ext.startswith(".") else f".{ext}"
        for ext in (part.strip().lower() for part in args.extensions.split(","))
        if ext
    }

    files = iter_files(args.paths, extensions)
    total_hits = 0
    for path in files:
        hits = scan_file(path, args.max_matches_per_rule)
        if not hits:
            continue
        print(f"\n{path}")
        for rule, lineno, text in hits:
            total_hits += 1
            print(f"  {lineno}: [{rule.severity}] {rule.code}: {text}")
            print(f"      {rule.hint}")

    print(f"\nScanned {len(files)} files, found {total_hits} suspicious locations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
