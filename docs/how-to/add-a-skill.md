# Add a skill

1. If the skill belongs to a new plugin, create
   `plugins/<plugin>/.claude-plugin/plugin.json` with `name`, `version`, and
   `description`. Then add a matching entry to `.claude-plugin/marketplace.json`.
2. Create `plugins/<plugin>/skills/<skill-name>/SKILL.md` with `name` and
   `description` frontmatter. See [Skill conventions](../reference/skill-conventions.md).
3. Add `references/`, `assets/`, `scripts/`, and `evals/` as needed.
4. Bump `version` in `plugin.json` and mirror it in the skill's
   `metadata.version`.
5. Add a row to the skills table in the root `README.md`.
6. [Validate](validate-and-package.md), then commit.
