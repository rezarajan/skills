#!/usr/bin/env python3
"""Check a problem model for integrity, evidence rules and definition-of-done coverage.

Usage:
    python scripts/check_model.py problem-model.yaml   (or .json)
    python scripts/check_model.py --rank problem-model.yaml
    python scripts/check_model.py --blueprint-sections problem-model.yaml

--rank prints the assumptions in their Assumptions Mapping categories, by ID within each.
--blueprint-sections prints whether each Blueprint section renders or collapses.

Exit code 0 when there are no errors (warnings allowed), 1 when there are errors,
2 when the file cannot be read. Requires PyYAML for .yaml files; .json needs nothing.
"""

import argparse
import json
import re
import sys
from pathlib import Path

COLLECTIONS = [
    "problem_statements", "stakeholders", "jobs", "pains", "gains", "problems",
    "causes", "constraints", "assumptions", "evidence", "opportunities", "questions",
]
CLAIM_COLLECTIONS = ["jobs", "pains", "gains", "problems", "causes", "constraints", "opportunities"]
REF_FIELDS = [
    "supported_by", "contradicted_by", "experienced_by", "causes", "competing_with",
    "derived_from", "stakeholders", "related", "blocks", "parent", "stakeholder", "job",
    "if_wrong_breaks", "tests",
]
STATUSES = ["intake", "loop", "synthesis", "handoff", "closed"]
CERTAINTY_RANK = {"very_low": 0, "low": 1, "moderate": 2, "high": 3}
CATEGORIES = ["test first", "test next", "foundation", "defer"]
SECTIONS = [  # (number, title, source); source is a collection list, None (never collapse) or a rule name
    (1, "Executive summary", None),
    (2, "Initial challenge and context", ["problem_statements"]),
    (3, "Problem scope and boundaries", ["scope"]),
    (4, "Environmental and contextual analysis", ["constraints"]),
    (5, "Stakeholder ecosystem map", ["stakeholders"]),
    (6, "Customer and user profiles", ["jobs", "pains", "gains"]),
    (7, "Jobs, pains and gains", ["jobs", "pains", "gains"]),
    (8, "Journey and experience analysis", "journey"),
    (9, "Problem decomposition map", ["problems"]),
    (10, "Symptoms and root cause analysis", ["causes"]),
    (11, "Systems map and interdependencies", "systems"),
    (12, "Unmet needs and opportunity landscape", ["opportunities"]),
    (13, "Evidence map", ["evidence"]),
    (14, "Assumption and hypothesis register", ["assumptions"]),
    (15, "Knowledge gaps and research requirements", None),
    (16, "Prioritised problem portfolio", "portfolio"),
    (17, "Core problem statement", ["problem_statements"]),
    (18, "Supporting problem statements", ["problem_statements"]),
    (19, "Problem definition and rationale", ["problem_statements"]),
    (20, "Recommended next steps", None),
]


def load(path):
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    try:
        import yaml
    except ImportError:
        sys.exit("PyYAML is not installed. Install it, or save the model as JSON.")
    return yaml.safe_load(text) or {}


def as_list(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def id_key(nid):
    m = re.match(r"^(.*?)(\d+)$", str(nid))
    return (m.group(1), int(m.group(2))) if m else (str(nid), 0)


def moves_mention(model, words):
    return any(any(w in str(m.get("move", "")).lower() for w in words)
               for m in as_list(model.get("moves")) if isinstance(m, dict))


def anchors(model):
    """IDs whose breakage makes an assumption high importance."""
    out = set()
    statements = [s for s in as_list(model.get("problem_statements")) if isinstance(s, dict)]
    if statements and statements[-1].get("id"):
        out.add(str(statements[-1]["id"]))
    for s in as_list(model.get("stakeholders")):
        if isinstance(s, dict) and s.get("primary") and s.get("id"):
            out.add(str(s["id"]))
    scored = []
    for p in as_list(model.get("problems")):
        if isinstance(p, dict) and isinstance(p.get("priority"), dict):
            try:
                scored.append((float(p["priority"].get("score")), str(p.get("id"))))
            except (TypeError, ValueError):
                pass
    if scored:
        top = max(s for s, _ in scored)
        out.update(pid for s, pid in scored if s == top)
    return out


def assess_assumption(node, evidence, anchor_ids):
    """Return (computed importance, computed evidence level, category)."""
    breaks = {str(b) for b in as_list(node.get("if_wrong_breaks"))}
    importance = "high" if breaks & anchor_ids else "low"
    certs = [CERTAINTY_RANK.get(evidence.get(str(s), {}).get("certainty"), 0)
             for s in as_list(node.get("supported_by")) if str(s) in evidence]
    level = "none" if not certs else ("strong" if max(certs) >= 2 else "some")
    if importance == "low":
        category = "defer"
    else:
        category = {"none": "test first", "some": "test next", "strong": "foundation"}[level]
    return importance, level, category


def section_states(model):
    causes = [c for c in as_list(model.get("causes")) if isinstance(c, dict)]
    cause_ids = {str(c.get("id")) for c in causes}
    chained = any(str(r) in cause_ids for c in causes for r in as_list(c.get("causes")))

    def has_content(coll):
        if coll == "scope":
            scope = model.get("scope") or {}
            return isinstance(scope, dict) and any(as_list(v) for v in scope.values())
        return bool(as_list(model.get(coll)))

    def all_very_low(nodes):
        nodes = [n for n in nodes if isinstance(n, dict)]
        return bool(nodes) and all(n.get("confidence") == "very_low" for n in nodes)

    states = []
    for num, title, source in SECTIONS:
        if source is None:
            render = True
        elif source == "journey":
            render = moves_mention(model, ("journey", "service"))
        elif source == "systems":
            render = chained or moves_mention(model, ("system", "loop"))
        elif source == "portfolio":
            nodes = [p for p in as_list(model.get("problems")) if isinstance(p, dict) and p.get("priority")]
            render = bool(nodes) and not all_very_low(nodes)
        else:
            nodes = [n for c in source if c != "scope" for n in as_list(model.get(c))]
            render = any(has_content(c) for c in source) and not all_very_low(nodes)
        states.append((num, title, "render" if render else "collapse"))
    return states


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("model")
    parser.add_argument("--rank", action="store_true",
                        help="print assumptions by Assumptions Mapping category")
    parser.add_argument("--blueprint-sections", action="store_true",
                        help="print render or collapse for each Blueprint section")
    args = parser.parse_args()
    path = Path(args.model)
    try:
        model = load(path)
    except Exception as exc:  # noqa: BLE001 - report any parse failure plainly
        print(f"Cannot read {path}: {exc}")
        return 2

    errors, warnings = [], []
    nodes = {}  # id -> (collection, node)

    for coll in COLLECTIONS:
        for node in as_list(model.get(coll)):
            if not isinstance(node, dict) or "id" not in node:
                errors.append(f"{coll}: entry without an id: {node!r}")
                continue
            nid = str(node["id"])
            if nid in nodes:
                errors.append(f"Duplicate id {nid}")
            nodes[nid] = (coll, node)

    # Reference integrity, and who references whom
    referenced = set()
    for nid, (coll, node) in nodes.items():
        for field in REF_FIELDS:
            for ref in as_list(node.get(field)):
                ref = str(ref)
                if ref and ref not in nodes:
                    errors.append(f"{nid}.{field} points to missing id {ref}")
                referenced.add(ref)
        for rel in as_list(node.get("relationships")):
            if isinstance(rel, dict) and rel.get("to"):
                if str(rel["to"]) not in nodes:
                    errors.append(f"{nid}.relationships points to missing id {rel['to']}")
                referenced.add(str(rel["to"]))
    for move in as_list(model.get("moves")):
        if isinstance(move, dict):
            referenced.update(str(r) for r in as_list(move.get("changed")))

    evidence = {nid: n for nid, (c, n) in nodes.items() if c == "evidence"}

    # Claim rules
    for coll in CLAIM_COLLECTIONS:
        for node in as_list(model.get(coll)):
            if not isinstance(node, dict):
                continue
            nid = node.get("id", "?")
            basis, prov, conf = node.get("basis"), node.get("provenance"), node.get("confidence")
            supports = [str(s) for s in as_list(node.get("supported_by"))]
            if basis == "fact" and not supports:
                errors.append(f"{nid} is marked fact but has no supported_by evidence")
            if basis == "fact" and supports and all(
                evidence.get(s, {}).get("kind") == "anecdotal" for s in supports
            ):
                warnings.append(f"{nid} is marked fact on anecdotal evidence only")
            if prov == "agent_inference" and (basis == "fact" or conf == "high"):
                errors.append(f"{nid} is agent inference but marked fact or high confidence")
            if as_list(node.get("contradicted_by")) and conf == "high":
                errors.append(f"{nid} has contradicting evidence but high confidence")
            if conf is None and coll != "problems":
                warnings.append(f"{nid} has no confidence level")

    # Type-specific link rules
    for node in as_list(model.get("problems")):
        if isinstance(node, dict) and not as_list(node.get("experienced_by")):
            errors.append(f"{node.get('id')} has no experienced_by stakeholder")
    for node in as_list(model.get("causes")):
        if not isinstance(node, dict):
            continue
        if not as_list(node.get("causes")):
            errors.append(f"{node.get('id')} does not link to the problem or cause it explains")
        if node.get("status") == "validated" and not any(
            evidence.get(str(s), {}).get("kind") == "direct" for s in as_list(node.get("supported_by"))
        ):
            warnings.append(f"{node.get('id')} is validated without direct evidence")
        if not node.get("test") and node.get("status") in (None, "hypothesised"):
            warnings.append(f"{node.get('id')} is hypothesised with no test recorded")
    for node in as_list(model.get("opportunities")):
        if isinstance(node, dict) and not as_list(node.get("derived_from")):
            errors.append(f"{node.get('id')} does not derive from any job, pain, gain or problem")
    anchor_ids = anchors(model)
    assessed = {}  # id -> (importance, evidence_level, category)
    for node in as_list(model.get("assumptions")):
        if not isinstance(node, dict):
            continue
        nid = node.get("id")
        if "if_wrong_breaks" not in node:
            warnings.append(f"{nid} has no if_wrong_breaks; importance computed as low")
        importance, level, category = assess_assumption(node, evidence, anchor_ids)
        assessed[str(nid)] = (importance, level, category)
        if node.get("importance") is not None and node["importance"] != importance:
            warnings.append(f"{nid} states importance {node['importance']}, computed {importance}")
        if node.get("importance") is not None and not node.get("importance_rationale"):
            warnings.append(f"{nid} states importance with no importance_rationale")
        if node.get("evidence_level") is not None and node["evidence_level"] != level:
            warnings.append(f"{nid} states evidence_level {node['evidence_level']}, computed {level}")
        if category in ("test first", "test next") and not node.get("test"):
            errors.append(f"{nid} is {category} with no test")
    for node in as_list(model.get("questions")):
        if not isinstance(node, dict) or node.get("status", "open") != "open":
            continue
        tests = [str(t) for t in as_list(node.get("tests"))]
        if not tests:
            warnings.append(f"{node.get('id')} is open but tests no assumption")
        for ref in tests:
            if ref in nodes and nodes[ref][0] != "assumptions":
                errors.append(f"{node.get('id')}.tests points to {ref}, which is not an assumption")

    status = (model.get("meta") or {}).get("status")
    if status is None:
        warnings.append("meta.status is missing")
    elif status not in STATUSES:
        errors.append(f"meta.status '{status}' is not one of {', '.join(STATUSES)}")

    primaries = [s for s in as_list(model.get("stakeholders")) if isinstance(s, dict) and s.get("primary")]
    if len(primaries) > 1:
        errors.append("More than one primary stakeholder: " + ", ".join(str(s.get("id")) for s in primaries))
    for s in primaries:
        if not s.get("primary_reason"):
            warnings.append(f"{s.get('id')} is primary but has no primary_reason")

    # Orphans
    for nid, (coll, node) in nodes.items():
        if coll in ("problem_statements", "stakeholders", "questions"):
            continue
        links_out = any(as_list(node.get(f)) for f in REF_FIELDS)
        if nid not in referenced and not links_out:
            warnings.append(f"{nid} ({coll}) is not linked to anything")

    # Definition of done
    meta, scope = model.get("meta") or {}, model.get("scope") or {}
    primary = primaries[0].get("id") if primaries else None

    def for_primary(coll):
        return [n for n in as_list(model.get(coll)) if isinstance(n, dict)
                and (primary in as_list(n.get("stakeholder")) or primary in as_list(n.get("stakeholders")))]

    causes = [c for c in as_list(model.get("causes")) if isinstance(c, dict)]
    problems = [p for p in as_list(model.get("problems")) if isinstance(p, dict)]
    assumptions = [a for a in as_list(model.get("assumptions")) if isinstance(a, dict)]
    statements = [s for s in as_list(model.get("problem_statements")) if isinstance(s, dict)]
    questions = [q for q in as_list(model.get("questions")) if isinstance(q, dict)]
    domains = [d.get("classification") for d in as_list(meta.get("domain")) if isinstance(d, dict)]
    cause_ids = {str(c.get("id")) for c in causes}
    chained = any(str(r) in cause_ids for c in causes for r in as_list(c.get("causes")))
    systems_move = any("system" in str(m.get("move", "")).lower() or "loop" in str(m.get("move", "")).lower()
                       for m in as_list(model.get("moves")) if isinstance(m, dict))
    only_ordered = bool(domains) and all(d in ("clear", "complicated") for d in domains)

    dod = [
        ("Domain classified; scope has in and out",
         bool(domains) and bool(as_list(scope.get("in"))) and bool(as_list(scope.get("out")))),
        ("One primary stakeholder chosen, with a reason",
         len(primaries) == 1 and bool(primaries[0].get("primary_reason"))),
        ("Jobs, pains and gains exist for the primary stakeholder",
         bool(primary) and all(for_primary(c) for c in ("jobs", "pains", "gains"))),
        ("Symptoms separated from causes; every cause has a status",
         any(p.get("kind") == "symptom" for p in problems) and bool(causes)
         and all(c.get("status") for c in causes)),
        ("Interdependencies mapped (or problem is ordered and small)",
         chained or systems_move or (only_ordered and len(problems) <= 2)),
        ("Riskiest assumptions listed, each with a test",
         bool(assumptions) and all(a.get("test") for a in assumptions
                                   if assessed.get(str(a.get("id")), ("low",))[0] == "high"
                                   and assessed[str(a.get("id"))][2] != "foundation")),
        ("Problems prioritised, evidence strength scored separately",
         bool(problems) and all(isinstance(p.get("priority"), dict)
                                and p["priority"].get("evidence_strength") for p in problems)),
        ("Core problem statement with an alternative framing",
         bool(statements) and bool(statements[-1].get("alternative_framing"))),
        ("Next research steps specified",
         any(q.get("status", "open") == "open" and q.get("resolution") for q in questions)),
    ]

    if args.rank:
        print("ASSUMPTIONS MAPPING")
        for cat in CATEGORIES:
            ids = sorted((i for i, a in assessed.items() if a[2] == cat), key=id_key)
            print(f"  {cat}: {', '.join(ids) if ids else '(none)'}")
            for i in ids:
                node = nodes[i][1]
                breaks = ", ".join(str(b) for b in as_list(node.get("if_wrong_breaks"))) or "nothing named"
                print(f"    {i}  breaks: {breaks}; evidence: {assessed[i][1]}")
        return 1 if errors else 0
    if args.blueprint_sections:
        print("BLUEPRINT SECTIONS")
        for num, title, state in section_states(model):
            print(f"  {num:>2}  {title:<42} {state}")
        return 1 if errors else 0

    print(f"Model: {path}")
    print(f"Nodes: {len(nodes)}  Errors: {len(errors)}  Warnings: {len(warnings)}\n")
    if errors:
        print("ERRORS")
        for e in errors:
            print(f"  - {e}")
        print()
    if warnings:
        print("WARNINGS")
        for w in warnings:
            print(f"  - {w}")
        print()
    print("DEFINITION OF DONE")
    for label, ok in dod:
        print(f"  [{'x' if ok else ' '}] {label}")
    done = sum(ok for _, ok in dod)
    print(f"\n{done}/{len(dod)} criteria met." + ("" if done == len(dod) else " Provisional definition only."))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
