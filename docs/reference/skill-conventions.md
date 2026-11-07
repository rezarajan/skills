# Skill conventions

`tools/skills.py validate` enforces the rules marked *(checked)*.

## Naming

- Skill folder name equals `name` in `SKILL.md`: lowercase letters, digits, and
  single hyphens, at most 64 characters. *(checked)*
- A plugin's entry name in `marketplace.json` equals `name` in that plugin's
  `plugin.json`. *(checked)*
- Every directory under `plugins/` is listed in `marketplace.json`. *(checked)*

## SKILL.md frontmatter

- `name` and `description` are required. *(checked)*
- `description` is at most 1024 characters and contains no angle brackets.
  *(checked)* It is the trigger: say what the skill does and when to use it, in
  the words a user would actually type.
- Allowed optional keys: `license`, `compatibility`, `metadata`,
  `allowed-tools`. *(checked)*
- Put author and version under `metadata`, quoted as strings. *(checked)*

## Body

- `SKILL.md` stays under 500 lines. *(checked)* Move detail into `references/`
  and say in `SKILL.md` when to read each file.
- Every `references/`, `scripts/`, or `assets/` path mentioned in backticks in
  `SKILL.md` exists. *(checked)*
- No nested `SKILL.md` files outside `evals/`. *(checked)*
- Reference files are linked from `SKILL.md` only, never from each other.
- Add a contents list to any reference file over about 100 lines.

## Versioning

- Every published change bumps `version` in `plugin.json`. Claude Code uses it
  to detect updates. *(presence checked)*
- Mirror the version in each changed skill's `metadata.version`.
- Record each version in `CHANGELOG.md` at the repo root.

## Evals

Each skill has `evals/<case-name>/` folders in the `claude plugin eval` format:

| File | Contents |
| ---- | -------- |
| `prompt.md` | The user prompt for the case |
| `case.yaml` | `schema_version`, `name`, `expected_outcome` |
| `graders/NN-*.md` | One grading criterion per file |
