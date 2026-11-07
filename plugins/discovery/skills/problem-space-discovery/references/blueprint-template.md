# Problem Space Blueprint template

Render the Blueprint from the problem model. Never add content that is not in the model. Sections with nothing to show collapse, by the rule below; a section that renders but skipped a framework says "Not applied, because [reason]".

For every section that has content: state the findings, the frameworks applied, the supporting evidence (IDs or citations), the assumptions, the outstanding questions, and the implications. Use tables and diagrams where they make relationships clearer than prose.

## Which sections, by depth mode

| # | Section | Quick brief | Working | Full |
|---|---|---|---|---|
| 1 | Executive summary | ✓ (3–5 sentences) | ✓ | ✓ |
| 2 | Initial challenge and context | ✓ (short) | ✓ | ✓ |
| 3 | Problem scope and boundaries | ✓ | ✓ | ✓ |
| 4 | Environmental and contextual analysis | | if relevant | ✓ |
| 5 | Stakeholder ecosystem map | primary stakeholder only | ✓ | ✓ |
| 6 | Customer and user profiles | | ✓ | ✓ |
| 7 | Jobs, pains and gains | top 3 of each | ✓ | ✓ |
| 8 | Journey and experience analysis | | if relevant | if relevant |
| 9 | Problem decomposition map | | ✓ | ✓ |
| 10 | Symptoms and root cause analysis | causes as hypotheses | ✓ | ✓ |
| 11 | Systems map and interdependencies | | if complex | ✓ |
| 12 | Unmet needs and opportunity landscape | | ✓ | ✓ |
| 13 | Evidence map | | ✓ | ✓ |
| 14 | Assumption and hypothesis register | riskiest 3 | ✓ | ✓ |
| 15 | Knowledge gaps and research requirements | ✓ | ✓ | ✓ |
| 16 | Prioritised problem portfolio | | ✓ | ✓ |
| 17 | Core problem statement | ✓ (provisional) | ✓ | ✓ |
| 18 | Supporting problem statements | | ✓ | ✓ |
| 19 | Problem definition and rationale, with alternative framing | ✓ | ✓ | ✓ |
| 20 | Recommended next steps | ✓ | ✓ | ✓ |

## Collapse rule

A section collapses if every collection it draws on is empty, or if all its nodes have `confidence: very_low`. Sections marked "never collapse" always render. Depth mode decides which sections are candidates; this rule decides which of those render.

| Section | Draws on |
|---|---|
| 1 Executive summary, 15 Knowledge gaps, 20 Next steps | never collapse |
| 2 Initial challenge, 17–19 Problem statements and definition | `problem_statements` |
| 3 Scope | `scope` |
| 4 Environment | `constraints` |
| 5 Stakeholders | `stakeholders` |
| 6 Profiles, 7 Jobs, pains and gains | `jobs`, `pains`, `gains` |
| 8 Journey | render only if `moves` records a journey or service-blueprint framework; otherwise collapse |
| 9 Decomposition | `problems` |
| 10 Symptoms and causes | `causes` |
| 11 Systems map | render only if any cause links to another cause, or `moves` records a systems framework; otherwise collapse |
| 12 Opportunities | `opportunities` |
| 13 Evidence map | `evidence` |
| 14 Assumption register | `assumptions` |
| 16 Portfolio | `problems` that have `priority` |

Collapsed sections become one list, **Not yet investigated**, placed after section 19 and before section 20. Each item names the section and the assumptions (by ID) whose testing would populate it. Order the list by the Assumptions Mapping category of those assumptions (test first, test next, foundation, defer), then by ID.

## Section guidance

1. **Executive summary**: the core problem statement, who it affects, the most important causes with their confidence, the top opportunities, the biggest uncertainty, and the next step.
2. **Initial challenge and context**: how the challenge was first described, what triggered it, and how the framing changed during discovery (from `problem_statements` history).
3. **Scope and boundaries**: in, out, deferred, with reasons. Candidate solutions mentioned by the user, listed as parked.
4. **Environment**: only forces with a stated link to the problem.
5. **Stakeholder ecosystem**: roles table; power-interest or salience view; dependent stakeholders flagged; the primary stakeholder and why.
6. **Profiles**: one per key segment.
7. **Jobs, pains, gains**: ranked, with confidence and evidence.
8. **Journey**: current state only.
9. **Decomposition**: problem components and how they relate.
10. **Symptoms and causes**: table of symptom → immediate → contributing → underlying → structural, each with status and competing explanations.
11. **Systems map**: loops, delays, archetypes matched, leverage levels.
12. **Opportunities**: opportunity tree (outcome and opportunity layers), with appraisal lenses.
13. **Evidence map**: claims against evidence, kind, say/do, certainty.
14. **Assumption register**: grouped by Assumptions Mapping category (test first, test next, foundation, defer), by ID within each; for each assumption, what it breaks if wrong, its evidence level, and the test for each test first and test next assumption.
15. **Knowledge gaps**: the research plan table from research-protocol.md, in the same category order.
16. **Portfolio**: priority table with importance and evidence strength in separate columns; criteria and weights stated.
17. **Core problem statement**: the current version.
18. **Supporting statements**: one per major sub-problem.
19. **Definition and rationale**: why this framing; the strongest alternative framing and what would favour it; confidence summary (established, probable, unknown).
20. **Next steps**: research to run, in priority order; decisions the user needs to make; whether the definition is ready for handoff to solution work, and if not, what remains.

## Formatting

- Write in plain, precise prose. Avoid unexplained framework jargon in the summary; the user may share it with people who do not know the frameworks.
- Show confidence inline, for example "(moderate; EVD-3, EVD-7)".
- If the environment supports documents or files, offer the Blueprint as a document. Otherwise render it in the reply.
