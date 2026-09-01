#!/usr/bin/env python3
"""Validate this repository's own invariants.

The 6-touch rule in CLAUDE.md says adding or removing a skill has to land in six
places, and that missing one makes the ecosystem contradict itself. That rule was
aspirational until this script existed: `ss13-tgs-deploy` shipped with touch #6
(both language guides) skipped, and nothing caught it.

This checks the invariants that can be checked mechanically. It does not judge
content -- it judges whether the parts of the repo still agree with each other.

Usage:
    python scripts/validate_ecosystem.py [--repo-root PATH] [-v]

Exit codes: 0 = clean or warnings only, 1 = at least one error.
"""

import argparse
import io
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML is required: pip install pyyaml\n")
    raise SystemExit(2)


# The controller routes; it does not route to itself. Checks that ask "is this
# skill reachable from the dispatch gates" skip it by name.
CONTROLLER = "byond-codemaster-controller"

NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "одного": 1, "двух": 2, "трёх": 3, "трех": 3,
    "четырёх": 4, "четырех": 4, "пяти": 5,
    "шести": 6, "семи": 7, "восьми": 8,
}

# A URL is not a machine path. Strip URLs before scanning, otherwise "https://",
# "byond://" and even a docker bind like "tgs/config:/config_data" trip the
# drive-letter pattern. The lookbehind is what excludes "config:/" -- a real
# drive letter is never preceded by another word character.
URL_RE = re.compile(r"\b[a-z][a-z0-9+.-]*://\S+", re.I)
MACHINE_PATH_RE = re.compile(r"(?<!\w)[A-Za-z]:[\\/]|/home/[a-z]|/Users/")  # allow-machine-path
MD_LINK_RE = re.compile(r"\]\(([^)]+)\)")

DESC_HARD_LIMIT = 1024
DESC_WARN_AT = 950


class Report(object):
    def __init__(self, verbose=False):
        self.errors = []
        self.warnings = []
        self.passes = 0
        self.verbose = verbose

    def error(self, check, detail):
        self.errors.append((check, detail))

    def warn(self, check, detail):
        self.warnings.append((check, detail))

    def ok(self, check, detail=""):
        self.passes += 1
        if self.verbose:
            print("  ok    %s %s" % (check, detail))

    def summary(self):
        print("")
        for check, detail in self.errors:
            print("ERROR  [%s] %s" % (check, detail))
        for check, detail in self.warnings:
            print("WARN   [%s] %s" % (check, detail))
        print("")
        print("%d checks passed, %d warnings, %d errors"
              % (self.passes, len(self.warnings), len(self.errors)))
        return 1 if self.errors else 0


def read(path):
    with io.open(path, encoding="utf-8") as fh:
        return fh.read()


def rel(path, root):
    """Repo-relative path with forward slashes, so reports read the same on every OS."""
    return os.path.relpath(path, root).replace("\\", "/")


def frontmatter(text, path):
    """Return the parsed YAML frontmatter, or None if it is malformed."""
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None


def discover_skills(root):
    """Every skills/<name>/SKILL.md under plugins/, keyed by directory name."""
    skills = {}
    plugins_dir = os.path.join(root, "plugins")
    if not os.path.isdir(plugins_dir):
        return skills
    for plugin in sorted(os.listdir(plugins_dir)):
        skills_dir = os.path.join(plugins_dir, plugin, "skills")
        if not os.path.isdir(skills_dir):
            continue
        for name in sorted(os.listdir(skills_dir)):
            skill_md = os.path.join(skills_dir, name, "SKILL.md")
            if os.path.isfile(skill_md):
                skills[name] = os.path.join(skills_dir, name)
    return skills


def check_frontmatter(root, skills, rep):
    for name, path in sorted(skills.items()):
        skill_md = os.path.join(path, "SKILL.md")
        data = frontmatter(read(skill_md), skill_md)
        if data is None:
            rep.error("frontmatter", "%s: SKILL.md has no parseable YAML frontmatter" % name)
            continue
        if data.get("name") != name:
            rep.error("frontmatter",
                      "%s: frontmatter name is %r but the directory is %r"
                      % (name, data.get("name"), name))
        else:
            rep.ok("frontmatter", "%s name matches directory" % name)

        desc = data.get("description") or ""
        if not desc:
            rep.error("frontmatter", "%s: empty description -- the model cannot trigger it" % name)
        elif len(desc) > DESC_HARD_LIMIT:
            rep.error("description-length",
                      "%s: %d chars exceeds the %d limit"
                      % (name, len(desc), DESC_HARD_LIMIT))
        elif len(desc) > DESC_WARN_AT:
            rep.warn("description-length",
                     "%s: %d chars, only %d of headroom left before the %d limit"
                     % (name, len(desc), DESC_HARD_LIMIT - len(desc), DESC_HARD_LIMIT))
        else:
            rep.ok("description-length", "%s %d chars" % (name, len(desc)))

        extra = set(data.keys()) - set(["name", "description"])
        if extra:
            rep.warn("frontmatter",
                     "%s: unexpected frontmatter keys %s -- the CLI validator is stricter "
                     "than the docs and has rejected extra keys before"
                     % (name, sorted(extra)))


def check_six_touch(root, skills, rep):
    """Touches 2-6 of the rule in CLAUDE.md, for every non-controller skill."""
    controller_md = os.path.join(skills[CONTROLLER], "SKILL.md") if CONTROLLER in skills else None
    if controller_md is None:
        rep.error("six-touch", "controller skill %s not found; routing cannot be checked" % CONTROLLER)
        return

    controller_text = read(controller_md)
    controller_fm = frontmatter(controller_text, controller_md) or {}
    controller_desc = controller_fm.get("description", "")

    gate_section = section(controller_text, "## Skill dispatch", "## Discovery protocol")
    bind_section = section(controller_text, "## Architecture skills this controller binds",
                           "## Decision flow")

    readme = read(os.path.join(root, "README.md"))
    readme_mermaid = "\n".join(re.findall(r"```mermaid(.*?)```", readme, re.S))

    guides = {}
    for lang in ("ru", "en"):
        p = os.path.join(root, "docs", "skills-guide.%s.md" % lang)
        if os.path.isfile(p):
            guides[lang] = read(p)
        else:
            rep.error("six-touch", "missing docs/skills-guide.%s.md" % lang)

    for name in sorted(skills):
        if name != CONTROLLER:
            probe(rep, "touch2-gate", name, gate_section,
                  "not routed from the controller's Gate 1 -- it can never be dispatched")
            probe(rep, "touch3-binding", name, bind_section,
                  "missing from the controller's binding table (state its base files, or an explicit none)")
            probe(rep, "touch4-controller-desc", name, controller_desc,
                  "not named in the controller's frontmatter description")

        probe(rep, "touch5-readme-table", name, readme,
              "missing from README.md")
        probe(rep, "touch5-readme-mermaid", name, readme_mermaid,
              "missing from the README dependency tree")
        for lang, text in sorted(guides.items()):
            probe(rep, "touch6-guide-%s" % lang, name, text,
                  "missing from docs/skills-guide.%s.md -- this is the touch that got skipped before" % lang)


def probe(rep, check, name, haystack, complaint):
    if name in (haystack or ""):
        rep.ok(check, name)
    else:
        rep.error(check, "%s: %s" % (name, complaint))


def section(text, start_marker, end_marker):
    """Slice between two headings; empty string if either marker is absent."""
    try:
        start = text.index(start_marker)
    except ValueError:
        return ""
    try:
        end = text.index(end_marker, start)
    except ValueError:
        end = len(text)
    return text[start:end]


def check_node_references(root, skills, rep):
    """Gate node numbers shift whenever a skill is added.

    The controller's dispatch section is the only place allowed to number its
    nodes; everywhere else names them by role ("the default node"). A stale
    "see node 5" in another file is drift that nothing else catches. Quoted
    spans are exempt, so the rule may quote the very example it forbids.
    """
    quoted = re.compile(r'"[^"]*"')
    numbered = re.compile(r"\bnode \d", re.I)
    controller_md = os.path.join(skills[CONTROLLER], "SKILL.md") if CONTROLLER in skills else None

    targets = [os.path.join(root, "CLAUDE.md"), os.path.join(root, "README.md")]
    for name, path in sorted(skills.items()):
        for dirpath, _dirnames, filenames in os.walk(path):
            targets.extend(os.path.join(dirpath, f) for f in filenames
                           if f.endswith((".md", ".json", ".yaml")))
    for scan_root in (os.path.join(root, "docs"),):
        if os.path.isdir(scan_root):
            for dirpath, _dirnames, filenames in os.walk(scan_root):
                targets.extend(os.path.join(dirpath, f) for f in filenames if f.endswith(".md"))

    hits = 0
    for target in targets:
        if not os.path.isfile(target):
            continue
        is_gate_section = (controller_md and os.path.samefile(target, controller_md))
        for line_no, line in enumerate(read(target).splitlines(), 1):
            if numbered.search(quoted.sub("", line)):
                hits += 1
                where = "the controller's own dispatch section" if is_gate_section else "another file"
                rep.error("node-reference",
                          "%s:%d numbers a dispatch node in %s -- name it by role instead: %s"
                          % (rel(target, root), line_no, where, line.strip()[:80]))
    if not hits:
        rep.ok("node-reference", "no numeric gate-node references outside the gate list")


def check_gate_targets(root, skills, rep):
    """Every skill the gates dispatch to must actually exist as a directory."""
    if CONTROLLER not in skills:
        return
    text = read(os.path.join(skills[CONTROLLER], "SKILL.md"))
    gates = section(text, "**Gate 1 —", "**This section is the single source of truth")
    if not gates:
        rep.error("gate-targets", "could not locate the Gate 1 dispatch list in the controller")
        return
    for referenced in sorted(set(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", gates))):
        if referenced.startswith(("ss13-", "byond-", "tgstation-")) and referenced not in skills:
            rep.error("gate-targets",
                      "Gate 1 dispatches to %r, which is not an installed skill" % referenced)
    rep.ok("gate-targets", "every skill named in Gate 1 exists")


def check_skill_count_claims(root, skills, rep):
    """Prose like "the five skills" / "пяти скиллов" has to match reality."""
    expected = len(skills)
    patterns = [
        ("en", os.path.join(root, "docs", "skills-guide.en.md"),
         re.compile(r"the ([a-z]+) skills", re.I)),
        ("ru", os.path.join(root, "docs", "skills-guide.ru.md"),
         re.compile(r"описание ([а-яё]+) скиллов", re.I)),
    ]
    for lang, path, pattern in patterns:
        if not os.path.isfile(path):
            continue
        text = read(path)
        found = False
        for word in pattern.findall(text):
            value = NUMBER_WORDS.get(word.lower())
            if value is None:
                continue
            found = True
            if value != expected:
                rep.error("skill-count",
                          "docs/skills-guide.%s.md claims %r (%d) skills but %d exist"
                          % (lang, word, value, expected))
            else:
                rep.ok("skill-count", "%s guide agrees on %d" % (lang, expected))
        if not found:
            rep.warn("skill-count",
                     "docs/skills-guide.%s.md states no skill count -- cannot verify it against %d"
                     % (lang, expected))


def check_links(root, skills, rep):
    for name, path in sorted(skills.items()):
        for dirpath, _dirnames, filenames in os.walk(path):
            for filename in filenames:
                if not filename.endswith(".md"):
                    continue
                full = os.path.join(dirpath, filename)
                for target in MD_LINK_RE.findall(read(full)):
                    if target.startswith(("http://", "https://", "#", "mailto:")):
                        continue
                    bare = target.split("#", 1)[0]
                    if not bare:
                        continue
                    if not os.path.exists(os.path.join(dirpath, bare)):
                        rep.error("links", "%s -> %s does not resolve"
                                  % (rel(full, root), target))


def check_orphans(root, skills, rep):
    """A reference/asset/script nobody points at will never be opened."""
    for name, path in sorted(skills.items()):
        skill_text = read(os.path.join(path, "SKILL.md"))
        for sub in ("references", "assets", "scripts"):
            subdir = os.path.join(path, sub)
            if not os.path.isdir(subdir):
                continue
            for filename in sorted(os.listdir(subdir)):
                if filename.startswith("."):
                    continue
                if filename not in skill_text:
                    rep.error("orphan",
                              "%s/%s/%s is never mentioned by its SKILL.md -- unreachable"
                              % (name, sub, filename))


def check_tooling_symmetry(root, skills, rep):
    for name, path in sorted(skills.items()):
        agents = os.path.join(path, "agents", "openai.yaml")
        if os.path.isfile(agents):
            rep.ok("tooling", "%s has agents/openai.yaml" % name)
        else:
            rep.warn("tooling", "%s has no agents/openai.yaml while its siblings do" % name)

        evals = os.path.join(path, "evals", "evals.json")
        if not os.path.isfile(evals):
            rep.warn("tooling", "%s has no evals/evals.json while its siblings do" % name)
            continue
        try:
            data = json.loads(read(evals))
        except ValueError as exc:
            rep.error("evals", "%s: evals.json is not valid JSON (%s)" % (name, exc))
            continue

        if data.get("skill_name") != name:
            rep.error("evals", "%s: evals.json skill_name is %r"
                      % (name, data.get("skill_name")))
        entries = data.get("evals") or []
        if not entries:
            rep.error("evals", "%s: evals.json has no eval entries" % name)
            continue
        langs = {}
        for entry in entries:
            langs[entry.get("lang")] = langs.get(entry.get("lang"), 0) + 1
        if langs.get("ru", 0) != langs.get("en", 0):
            rep.error("evals",
                      "%s: %d ru vs %d en prompts -- example prompts ship in EN+RU pairs"
                      % (name, langs.get("ru", 0), langs.get("en", 0)))
        else:
            rep.ok("evals", "%s %d balanced pairs" % (name, langs.get("en", 0)))


KNOWN_CHECK_TYPES = ("paths_exist", "paths_absent", "grep", "pin", "commit_rank")


def check_claims_files(root, skills, rep):
    """A malformed claims.yaml does not fail loudly -- it silently stops checking.

    A claim naming a target that does not exist reports SKIP ("no checkout for
    target"), which is indistinguishable from "you don't have that repo cloned".
    That is the exact silent no-op the drift workflow exists to prevent, so it is
    caught here instead.
    """
    for name, path in sorted(skills.items()):
        claims_path = os.path.join(path, "claims.yaml")
        if not os.path.isfile(claims_path):
            continue
        try:
            doc = yaml.safe_load(read(claims_path)) or {}
        except yaml.YAMLError as exc:
            rep.error("claims", "%s: claims.yaml does not parse (%s)" % (name, exc))
            continue

        if doc.get("skill") != name:
            rep.error("claims", "%s: claims.yaml declares skill %r" % (name, doc.get("skill")))

        targets = doc.get("targets") or {}
        if not targets:
            rep.error("claims", "%s: claims.yaml defines no targets" % name)

        seen = set()
        claims = doc.get("claims") or []
        if not claims:
            rep.error("claims", "%s: claims.yaml defines no claims" % name)
        for claim in claims:
            cid = claim.get("id")
            if not cid:
                rep.error("claims", "%s: a claim has no id" % name)
                continue
            if cid in seen:
                rep.error("claims", "%s: duplicate claim id %r" % (name, cid))
            seen.add(cid)

            if claim.get("target") not in targets:
                rep.error("claims",
                          "%s/%s: target %r is not defined -- the claim would silently never run"
                          % (name, cid, claim.get("target")))
            if not claim.get("says"):
                rep.error("claims", "%s/%s: no 'says' text, so a report cannot explain itself"
                          % (name, cid))
            spec = claim.get("check") or {}
            if spec.get("type") not in KNOWN_CHECK_TYPES:
                rep.error("claims", "%s/%s: unknown check type %r"
                          % (name, cid, spec.get("type")))
        rep.ok("claims", "%s %d claims over %d targets" % (name, len(claims), len(targets)))


def check_hygiene(root, rep):
    """No machine paths, no CRLF, no empty directories in what ships."""
    # scripts/ is in scope for CRLF above all: scripts/hooks/* are shell scripts
    # without a .sh extension, and a CRLF shebang makes them fail silently.
    scan_roots = [os.path.join(root, "plugins"),
                  os.path.join(root, "docs"),
                  os.path.join(root, "scripts")]
    for scan_root in scan_roots:
        if not os.path.isdir(scan_root):
            continue
        for dirpath, dirnames, filenames in os.walk(scan_root):
            dirnames[:] = [d for d in dirnames
                           if d not in (".git", "__pycache__", "node_modules")]
            if not dirnames and not filenames:
                rep.warn("empty-dir", "%s is empty -- git will not track it"
                         % rel(dirpath, root))
            for filename in filenames:
                full = os.path.join(dirpath, filename)
                relpath = rel(full, root)
                with io.open(full, "rb") as fh:
                    raw = fh.read()
                if b"\r\n" in raw:
                    rep.error("crlf", "%s contains CRLF; .gitattributes pins this tree to LF" % relpath)
                try:
                    text = raw.decode("utf-8")
                except UnicodeDecodeError:
                    continue
                for line_no, line in enumerate(text.splitlines(), 1):
                    # A line may opt out -- the checker's own pattern definition
                    # necessarily contains what the checker looks for.
                    if "allow-machine-path" in line:
                        continue
                    if MACHINE_PATH_RE.search(URL_RE.sub("", line)):
                        rep.error("machine-path",
                                  "%s:%d looks like a machine-specific path: %s"
                                  % (relpath, line_no, line.strip()[:90]))


def main():
    # This repo is bilingual and the report quotes file content; a Windows
    # console's default codepage turns em dashes and Cyrillic into noise.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo-root", default=None,
                        help="repository root (default: the parent of this script's directory)")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="print every passing check, not just the failures")
    args = parser.parse_args()

    root = args.repo_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rep = Report(verbose=args.verbose)

    skills = discover_skills(root)
    if not skills:
        sys.stderr.write("No skills found under %s/plugins/*/skills/\n" % root)
        return 2
    print("Validating %d skills in %s" % (len(skills), root))
    print("  " + ", ".join(sorted(skills)))

    check_frontmatter(root, skills, rep)
    check_six_touch(root, skills, rep)
    check_gate_targets(root, skills, rep)
    check_node_references(root, skills, rep)
    check_skill_count_claims(root, skills, rep)
    check_links(root, skills, rep)
    check_orphans(root, skills, rep)
    check_tooling_symmetry(root, skills, rep)
    check_claims_files(root, skills, rep)
    check_hygiene(root, rep)

    return rep.summary()


if __name__ == "__main__":
    raise SystemExit(main())
