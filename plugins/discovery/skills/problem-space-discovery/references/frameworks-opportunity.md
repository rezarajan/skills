# Opportunity identification, appraisal and prioritisation

An opportunity is an unmet need, pain or desire worth addressing, stated without a solution. Not every pain is an opportunity, and an opportunity is not a validated business case.

## Contents
1. Opportunity Solution Tree (opportunity layer)
2. ODI opportunity scoring
3. Seriousness, urgency and growth
4. Weighted problem scoring
5. Pareto analysis
6. Impact versus effort: why to avoid it here
7. Desirability, feasibility, viability as a lens on opportunities
8. Appraisal lenses checklist

---

## 1. Opportunity Solution Tree (opportunity layer)

- **Answers**: Which needs could move the desired outcome, and how do they relate?
- **Fits**: Once there is a clear desired outcome and evidence of needs.
- **Writes**: `opportunities` with `serves_outcome` and `parent`.
- **Source**: Teresa Torres, Continuous Discovery Habits (2021).

The full tree has four levels: desired outcome, opportunities, solutions, assumption tests. This skill builds the top two and stops.

Rules:
- One desired outcome at the top, ideally measurable and within the team's influence.
- Opportunities are customer needs, pains or desires, discovered through research, never features.
- Opportunities nest: a broad opportunity breaks into smaller, more specific ones. Prefer to work on a specific child opportunity rather than a vague parent.
- Compare and contrast sibling opportunities rather than asking "should we do this one, yes or no?"
- Every opportunity links to its evidence. An opportunity with no evidence is an assumption.

---

## 2. ODI opportunity scoring

- **Answers**: Quantitatively, which desired outcomes are most underserved?
- **Fits**: Only when there is survey data on importance and satisfaction for well-formed outcome statements, from a sample of the relevant population.
- **Source**: Ulwick, "Turn Customer Input into Innovation" (HBR, 2002); What Customers Want (2005).

Formula:

    Opportunity = Importance + max(Importance − Satisfaction, 0)

Importance and satisfaction are typically the share of respondents rating an outcome in the top two boxes of a five-point scale, expressed on a 0–10 scale. The formula weights importance twice as heavily as satisfaction, and does not let over-satisfaction reduce the score below importance. Commonly cited interpretation: scores above 10 indicate underserved outcomes, above 15 extremely underserved. Low-importance, high-satisfaction outcomes suggest over-service.

Without survey data, do not compute scores. You may rank outcomes qualitatively and label the ranking a hypothesis, or design the survey (see research-protocol.md).

---

## 3. Seriousness, urgency and growth (Kepner-Tregoe)

- **Answers**: Relative priority across problems, with little data.
- **Fits**: Early triage, any domain.
- **Method**: Rate each problem relative to the others (high, medium, low) on seriousness (current impact), urgency (time before it becomes harder or impossible to address) and growth (will it get worse if left alone). Record the evidence behind each rating. Anything low on all three can be set aside for now.

---

## 4. Weighted problem scoring

- **Answers**: A transparent ranking across several criteria.
- **Fits**: When the user needs a defensible portfolio.

Default criteria (adjust with the user, and state the weights):
- Severity of impact
- Frequency of occurrence
- Number of people affected, and who (dependent stakeholders count)
- Urgency
- Strategic importance to the user's mandate
- Interconnectedness: how many other problems it drives
- Potential for meaningful improvement

Score **evidence strength** separately and display it next to the importance score. Never multiply it into a single number: a high score built on no evidence should look different from a high score built on direct evidence. Show results as a table with both columns, and call out the "high importance, weak evidence" problems as research priorities.

---

## 5. Pareto analysis

- **Fits**: Only when frequency or impact counts exist for categories of problem.
- **Method**: Sort categories by count or impact; plot cumulative share. Identify the "vital few" that account for most of the effect. Do not assume an 80/20 split; report whatever the data shows.

---

## 6. Impact versus effort: why to avoid it here

Effort belongs to solutions. At the problem stage it smuggles solution assumptions into prioritisation and biases towards easy fixes. The skill's boundary says not to confuse ease of solving with importance. If the user wants a second axis, use **investigability** (how cheaply the uncertainty about this problem can be reduced) instead, and label it as such.

---

## 7. Desirability, feasibility, viability as a lens on opportunities

- **Source**: IDEO's design thinking lens; used by Strategyzer and in Bland and Osterwalder's Testing Business Ideas, which adds adaptability.
- **Use here**: For each opportunity, record what evidence exists that the need is real and important (desirability), and which known constraints bound any response (feasibility, viability, adaptability). Do not assess a specific solution's feasibility. The output is a set of assumptions to map (frameworks-evidence.md), not a go/no-go decision.

---

## 8. Appraisal lenses checklist

For each candidate opportunity, record:
- Importance of the underlying need, and to whom.
- Frequency and severity of the pain.
- Number and type of people affected.
- Existing alternatives and workarounds, and how well they serve the need. Elaborate workarounds are strong evidence of a real need.
- Willingness and ability to change (Forces of Progress).
- Strategic relevance to the user's mandate.
- Evidence strength.
- Where it would act in the system (leverage point level).
- What would have to be true for it to be worth pursuing (feeds Assumptions Mapping).
