# Repository layout

```
.claude-plugin/marketplace.json     catalogue of plugins (Claude Code)
plugins/<plugin>/                   one plugin per domain, grouping related skills
  .claude-plugin/plugin.json        plugin name, version, description
  skills/<skill-name>/              one folder per skill
    SKILL.md                        required: frontmatter + instructions (< 500 lines)
    references/                     docs loaded on demand, one level deep
    assets/                         templates and static files
    scripts/                        executable helpers
    evals/                          test cases (excluded from packages)
tools/skills.py                     validate and package
.github/workflows/validate.yml      runs validation on every push and pull request
docs/                               repository documentation (Diátaxis)
CHANGELOG.md                        release notes, one entry per plugin version
dist/                               build output from `tools/skills.py package` (ignored)
```
