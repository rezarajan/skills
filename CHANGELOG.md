# Changelog

Versions follow the `discovery` plugin version in `plugins/discovery/.claude-plugin/plugin.json`.

## 1.1.0 (2026-11-07)

problem-space-discovery:

- **Harness states and exits.** The session now has explicit states (`intake`, `loop`, `synthesis`, `handoff`, `closed`) in `meta.status`, with fixed transitions. An explicit opt-out gives a quick brief, delivers the handoff artifact, states the boundary once and closes discovery. Once closed, discovery stays closed unless the user asks to reopen it. New `assets/handoff.template.md` defines the handoff contract.
- **Quieter persistence.** With file access, the model lives in `problem-model.yaml` and replies say nothing about it unless asked. Without file access, replies end with a "Model changes" block holding only the nodes added or changed that turn.
- **Blueprint collapse rule.** Sections with no evidence, or only very-low-confidence nodes, collapse into one "Not yet investigated" list, using a fixed section-to-source mapping. New `check_model.py --blueprint-sections` shows the result.
- **Assumptions Mapping as the single prioritisation method.** Importance is set by a fixed test (`if_wrong_breaks` names the latest problem statement, primary stakeholder or top problem), and evidence level is computed from certainty. Assumptions fall into four categories: test first, test next, foundation, defer. Value of Information is documented as the principle behind the method. `check_model.py` computes both axes, warns on mismatches and on open questions with no `tests` link, and adds `--rank`.
- **Probes describe hypotheses, not interventions.** Safe-to-fail probe records have a fixed set of fields, and the intervention is always "to design with the team".
- **Test cases.** Rewrote the `respects-skip-request` graders. Added the `gap-ranking-consistency` case (with a fixture model) and the `harness-exit-then-continue` case.

## 1.0.0 (2026-11-07)

Initial release.
