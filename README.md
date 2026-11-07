# skills

A monorepo of agentic skills. Every skill follows the open
[Agent Skills specification](https://agentskills.io), so it works in Claude Code,
claude.ai, and other compatible agents. The repo is also a Claude Code plugin
marketplace named `skills`.

## Skills

| Plugin | Skill | What it does |
| ------ | ----- | ------------ |
| discovery | [problem-space-discovery](plugins/discovery/skills/problem-space-discovery/SKILL.md) | Investigates and defines problems and opportunities before solution design, producing an evidence-graded Problem Space Blueprint |

## Quick start

```
claude plugin marketplace add .
claude plugin install discovery@skills
```

For claude.ai, see [Install skills](docs/how-to/install-skills.md).

## Documentation

Docs live in [`docs/`](docs/README.md) and follow [Diátaxis](https://diataxis.fr/).

- How-to: [Install skills](docs/how-to/install-skills.md),
  [Add a skill](docs/how-to/add-a-skill.md),
  [Validate and package](docs/how-to/validate-and-package.md)
- Reference: [Repository layout](docs/reference/repo-layout.md),
  [Skill conventions](docs/reference/skill-conventions.md)
- Explanation: [The problem-space-discovery harness](docs/explanation/problem-space-discovery-harness.md)
