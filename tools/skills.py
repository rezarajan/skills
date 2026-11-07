#!/usr/bin/env python3
"""Validate and package every skill in this repo.

    python3 tools/skills.py validate     # check spec rules and manifests
    python3 tools/skills.py package      # validate, then write dist/<skill>.skill

A .skill file is a zip of the skill folder (evals/ excluded) for upload to claude.ai.
Requires PyYAML.
"""
import json, re, sys, zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ALLOWED = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SKIP_DIRS = {"__pycache__", "node_modules"}


def skills():
    return sorted(p.parent for p in ROOT.glob("plugins/*/skills/*/SKILL.md"))


def check_skill(d, errs):
    text = (d / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return errs.append(f"{d.name}: missing YAML frontmatter")
    fm = yaml.safe_load(m.group(1)) or {}
    if extra := set(fm) - ALLOWED:
        errs.append(f"{d.name}: unexpected frontmatter keys {sorted(extra)}")
    name, desc = str(fm.get("name", "")), str(fm.get("description", "")).strip()
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        errs.append(f"{d.name}: invalid name '{name}'")
    if name != d.name:
        errs.append(f"{d.name}: name '{name}' must match folder name")
    if not desc or len(desc) > 1024 or "<" in desc or ">" in desc:
        errs.append(f"{d.name}: description empty, over 1024 chars, or contains angle brackets")
    if isinstance(fm.get("metadata"), dict) and any(not isinstance(v, str) for v in fm["metadata"].values()):
        errs.append(f"{d.name}: metadata values must be strings (quote versions)")
    if (n := text.count("\n")) > 500:
        errs.append(f"{d.name}: SKILL.md is {n} lines; keep it under 500")
    for ref in re.findall(r"`((?:references|scripts|assets)/[^`\s]+)`", text):
        if not (d / ref).exists():
            errs.append(f"{d.name}: SKILL.md mentions missing file {ref}")
    nested = [p for p in d.rglob("SKILL.md") if p != d / "SKILL.md" and "evals" not in p.parts]
    if nested:
        errs.append(f"{d.name}: nested SKILL.md files {nested}")


def check_manifests(errs):
    mp = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    for key in ("name", "owner", "plugins"):
        if key not in mp:
            errs.append(f"marketplace.json: missing '{key}'")
    listed = set()
    for entry in mp.get("plugins", []):
        src = ROOT / entry.get("source", "")
        listed.add(src.resolve())
        pj = src / ".claude-plugin/plugin.json"
        if ".." in entry.get("source", "") or not pj.exists():
            errs.append(f"marketplace entry '{entry.get('name')}': bad source or missing plugin.json")
            continue
        meta = json.loads(pj.read_text())
        if meta.get("name") != entry.get("name"):
            errs.append(f"plugin '{entry.get('name')}': name differs from plugin.json ('{meta.get('name')}')")
        if not meta.get("version"):
            errs.append(f"plugin '{entry.get('name')}': plugin.json has no version")
    for pdir in (ROOT / "plugins").iterdir():
        if pdir.is_dir() and pdir.resolve() not in listed:
            errs.append(f"plugins/{pdir.name} is not listed in marketplace.json")


def validate():
    errs = []
    found = skills()
    for d in found:
        check_skill(d, errs)
    check_manifests(errs)
    for e in errs:
        print(f"ERROR  {e}")
    print(f"{len(found)} skill(s) checked, {len(errs)} error(s).")
    return not errs


def package():
    if not validate():
        return False
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    for d in skills():
        out = dist / f"{d.name}.skill"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(d.rglob("*")):
                rel = f.relative_to(d)
                if f.is_file() and not (SKIP_DIRS & set(rel.parts)) and rel.parts[0] != "evals" \
                        and f.suffix != ".pyc" and f.name != ".DS_Store":
                    z.write(f, Path(d.name) / rel)
        print(f"Packaged {out.relative_to(ROOT)}")
    return True


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    ok = {"validate": validate, "package": package}.get(cmd, lambda: print(__doc__))()
    sys.exit(0 if ok else 1)
