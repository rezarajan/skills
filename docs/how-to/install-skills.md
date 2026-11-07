# Install skills

## Claude Code

From a local clone:

```
claude plugin marketplace add .
claude plugin install <plugin>@skills
```

For example, `claude plugin install discovery@skills`.

## claude.ai

1. Build the packages:

   ```
   pip install pyyaml
   python3 tools/skills.py package
   ```

2. Upload `dist/<skill>.skill` as a skill in claude.ai.
