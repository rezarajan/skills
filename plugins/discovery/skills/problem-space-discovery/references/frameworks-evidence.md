# Evidence, assumptions and validation

## Contents
1. Evidence types
2. Say versus do
3. Certainty grading (adapted from GRADE)
4. Assumptions Mapping
5. Hypothesis format
6. Test Card and Learning Card
7. The Evidence and Assumption Register

---

## 1. Evidence types

| Kind | Meaning | Examples |
|---|---|---|
| Direct | Observed behaviour, measured outcomes or primary research about this population | System logs, attendance records, observed workflow, interviews with the affected group |
| Indirect | Credible secondary research or stakeholder reports, about a similar population or reported second-hand | Published studies, government statistics for a wider region, a manager describing staff experience |
| Anecdotal | Individual experiences or unverified accounts | One complaint, a story told in a meeting |
| None | An assumption with no support yet | "Teachers would use this if it existed" |

A claim's confidence follows its best evidence, adjusted by certainty grading below.

---

## 2. Say versus do

From Testing Business Ideas (Bland and Osterwalder, 2019) and the wider customer development tradition: what people say (opinions, predictions, stated preferences, survey intentions) is weaker evidence than what people do (behaviour, workarounds, time or money spent, commitments made). Tag every evidence node with `say_or_do`.

Particularly weak: compliments, hypothetical answers ("I would use…"), and generalisations ("I always…"). Rob Fitzpatrick's The Mom Test calls these compliments and fluff.

---

## 3. Certainty grading (adapted from GRADE)

GRADE (Grading of Recommendations, Assessment, Development and Evaluation) rates certainty of evidence as high, moderate, low or very low, and downgrades for specific concerns. This skill adapts the idea for non-clinical evidence. It is a reasoning aid, not a formal GRADE assessment.

Starting point by source type:
- Measured behavioural or operational data about the population, or systematic observation: start **high**.
- Structured primary research (interviews, surveys) with the population: start **moderate**.
- Secondary research about a similar population, or reports from someone outside the affected group: start **moderate** if rigorous, **low** otherwise.
- Anecdote or agent inference: **very low**.

Downgrade one level for each serious concern:
- **Risk of bias**: who produced it, and do they have an interest in the conclusion? Was the sample self-selected?
- **Indirectness**: different population, setting, time or question from the one in the model. The most common problem with secondary research.
- **Inconsistency**: sources disagree without explanation.
- **Imprecision**: small samples, vague measures, wide ranges.
- **Selection or publication bias**: only successes reported, or only the loudest voices heard.
- **Staleness**: conditions have changed since collection.

Upgrade one level only for a large, consistent effect seen across independent sources.

---

## 4. Assumptions Mapping

- **Answers**: Which beliefs, if wrong, would most damage the problem definition or an opportunity, and have the least evidence?
- **Source**: David J. Bland; Bland and Osterwalder, Testing Business Ideas (2019).
- **Writes**: `assumptions` with `category`, `if_wrong_breaks`, `importance`, `importance_rationale`, `supported_by`, `evidence_level`, `test`.

This is the single method for prioritising research and knowledge gaps. Do not add other scoring.

Steps:
1. Make assumptions explicit. Bland's categories are desirability, feasibility and viability, plus adaptability. In problem discovery also include causal assumptions (A causes B) and contextual assumptions (the situation is as described).
2. **Importance axis, by a fixed test.** Record in `if_wrong_breaks` the IDs the assumption holds up. Importance is `high` if and only if that list names the latest problem statement, the primary stakeholder or the highest-priority problem; otherwise it is `low`. Write one sentence in `importance_rationale` saying why the assumption breaks what it names.
3. **Evidence axis, computed.** `none` if nothing supports it; `some` if the best supporting evidence has certainty `low` or `very_low`; `strong` if the best has certainty `moderate` or `high`.
4. Place each assumption in one category:

| Category | Importance | Evidence | Action |
|---|---|---|---|
| 1. Test first | high | none | Research now |
| 2. Test next | high | some | Research after test first |
| 3. Foundation, do not research | high | strong | Build on it; recheck only if contradicted |
| 4. Defer, do not research | low | any | Leave until importance changes |

5. Within a category, order by ID. There is no tie-break scoring.
6. For each test first and test next assumption, write a test (section 6) or a research question that `tests` it.

**Why this works.** The principle behind the method is the value of information: information is worth gathering only if it could change a decision (Howard, "Information Value Theory", IEEE Transactions on Systems Science and Cybernetics, 1966). An assumption that breaks nothing important cannot change the definition, and one already well evidenced is unlikely to. The quantitative form, the expected value of perfect information (EVPI), is used to prioritise research in health technology assessment for NICE, but it needs a probabilistic decision model that discovery rarely has. Use the principle here, not the calculation.

Testing assumptions that are unimportant, however weakly evidenced, is activity rather than progress.

---

## 5. Hypothesis format

    We believe that [stakeholder] experiences [problem] when [context],
    because [cause].
    We will know this is true when we observe [specific, observable signal].

A hypothesis must be falsifiable: write down what result would show it is wrong.

---

## 6. Test Card and Learning Card (Strategyzer)

Test Card, written before research or an experiment:
- **We believe that** [hypothesis]
- **To verify that, we will** [the cheapest research or experiment that could test it]
- **And measure** [metric or observation]
- **We are right if** [success criterion, set in advance]

Also note how critical the assumption is, the test's cost, and how reliable its data will be.

Learning Card, written after:
- **We believed that** [hypothesis]
- **We observed** [what happened, with data]
- **From that we learned** [insight]
- **Therefore, we will** [next action: persevere, revise the definition, or drop the line of inquiry]

Update the model from the Learning Card: change statuses, add evidence nodes, and record the move.

---

## 7. The Evidence and Assumption Register

Rendered in the Blueprint as one table per significant problem component:

| Claim | Basis | Evidence (IDs) | Kind | Say/Do | Certainty | Competing explanations | Assumptions | Open questions | Research needed |
|---|---|---|---|---|---|---|---|---|---|

Order rows by importance, then by weakest evidence first.
