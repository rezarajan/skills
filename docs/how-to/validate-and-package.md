# Validate and package

Requires Python 3 and PyYAML (`pip install pyyaml`).

## Validate

```
python3 tools/skills.py validate     # spec and manifest checks
claude plugin validate .             # Claude Code's own marketplace check
```

CI runs `tools/skills.py validate` on every push and pull request.

## Package for claude.ai

```
python3 tools/skills.py package
```

This validates first, then writes `dist/<skill>.skill` for each skill: a zip of
the skill folder without `evals/`.
