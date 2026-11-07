# Research protocol

## Contents
1. Choosing what to research
2. Secondary research procedure
3. Source preference and grading
4. Recording research in the model
5. Primary research: choosing a method
6. Interview design (Mom Test and switch interview)
7. Surveys for outcome scoring
8. Safe-to-fail probes for complex domains
9. Templates: research plan and interview guide

---

## 1. Choosing what to research

Research is chosen by Assumptions Mapping category, and by nothing else:

1. **Test first** (high importance, no evidence): research these now.
2. **Test next** (high importance, some evidence): research these once test first is exhausted.
3. **Foundation** (high importance, strong evidence): do not research.
4. **Defer** (low importance, any evidence): do not research.

Within a category, take assumptions in ID order. Every research question `tests` at least one assumption. When a gap has no assumption behind it (a cause with competing explanations, a claim about dependent stakeholders that came only from powerful ones, missing IS NOT data), first write the assumption it rests on, then place it.

State the question before searching. Research without a question tends to collect material that confirms the framing you started with.

---

## 2. Secondary research procedure

When search tools are available:
1. Write the specific question, and the population and setting it concerns.
2. Search for evidence for and against. Deliberately search for disconfirming evidence and for alternative explanations.
3. Prefer primary and official sources (statistics agencies, regulators, peer-reviewed research, organisations' own reports) over aggregators and commentary.
4. Check each source's population, setting, date and method against the claim.
5. Record each useful finding as an evidence node, summarised in your own words.
6. Report findings separately from what the user told you, with citations.

Useful source types by question:
- Scale and trends: national statistics, official administrative data, regulators.
- Causes and mechanisms: peer-reviewed research, systematic reviews, evaluations of past programmes.
- Practice and context: government and agency reports, sector bodies, case studies (treat as indirect, often biased towards success).
- Market context: company filings, industry bodies, credible market research (check who paid for it).

Without search tools, say so, mark the claim as needing secondary research, and suggest where to look.

Never imply that secondary research proves what a specific group experiences. It can make a claim plausible; only primary evidence about the group establishes it.

---

## 3. Source preference and grading

Grade each source with the certainty approach in frameworks-evidence.md. For secondary sources, check in particular:
- **Authority and interest**: who produced it, who funded it, and what they gain from the conclusion.
- **Method**: is it measured, surveyed, modelled or opinion? What was the sample?
- **Indirectness**: same population, setting and time as the claim?
- **Recency**: does it pre-date a relevant change?
- **Corroboration**: do independent sources agree?

---

## 4. Recording research in the model

For each finding, create an `EVD` node (summary, source, kind, say_or_do, population, certainty, downgrades), then link it with `supported_by` or `contradicted_by` on the claims it bears on, adjust their confidence, and log the move. If the finding raises a new question, add a `Q` node.

---

## 5. Primary research: choosing a method

The agent designs primary research; the user or their team runs it. Pick the cheapest method that could change the decision.

| Need | Method | Notes |
|---|---|---|
| What actually happens, at scale | Analysis of existing operational data | Often the cheapest direct evidence, and it is already collected. Ask what logs, records or systems exist before proposing anything new. |
| How people actually do the job | Contextual observation (watching the work where it happens) | Strongest for workarounds and for gaps between stated and actual process. |
| Why people act as they do; the history of a decision | Interviews about specific past episodes | Use the rules in section 6. |
| Behaviour over time | Diary studies | For intermittent problems. |
| How widespread and important needs are | Surveys | Only after interviews have produced well-formed outcome statements. |
| Shared understanding across groups | Facilitated workshops (problem trees, journey mapping) | Run separately with different stakeholder groups, then compare. |
| Whether a cause or dynamic is real in a complex domain | Safe-to-fail probes | See section 8. |

Note ethical and access constraints: research with minors, patients or vulnerable groups usually needs approvals and safeguarding. Raise this, and do not design around it.

---

## 6. Interview design

**The Mom Test** (Rob Fitzpatrick, 2013). Three rules:
1. Talk about their life, not your idea.
2. Ask about specifics in the past, not generics or opinions about the future.
3. Talk less and listen more.

Bad data to deflect or anchor: compliments, fluff (generic claims, future-tense promises, hypotheticals) and ideas (feature requests). When someone says "I usually…" or "I would…", ask about the last time it happened.

**Switch interview** (Moesta and Spiek), for adoption or behaviour-change problems: reconstruct the timeline of a real past change, from first thought, through passive and active looking, to deciding, and to the first use. Probe for the four forces at each stage: push, pull, anxiety and habit.

Good questions:
- "Tell me about the last time [the job] happened. Walk me through it."
- "What did you do next? Who else was involved?"
- "What have you tried to make this easier? What happened?"
- "What does this cost you, in time, money or anything else?"
- "Who else should I talk to about this?"

Avoid: "Would you use…?", "Do you think it's a good idea…?", "How much would you pay for…?", and any question that describes a solution.

---

## 7. Surveys for outcome scoring

Use only after interviews have produced outcome statements in ODI form (frameworks-needs.md). For each outcome, ask importance and current satisfaction on matching five-point scales. Sample the relevant population, record how respondents were reached, and segment by stakeholder type. Compute opportunity scores as in frameworks-opportunity.md.

---

## 8. Safe-to-fail probes for complex domains

In Cynefin's complex domain, analysis cannot settle which causes matter. Design several small, cheap, reversible probes in parallel, each testing a different hypothesis about the system. A probe is described by the hypothesis it tests, never by what is done. Each probe record has exactly these fields:

```yaml
- hypothesis: ASM-3            # an ASM or CAU ID
  amplify_if: signal that would amplify it
  dampen_if: signal that would dampen it
  stop_when: stop condition
  observer: who checks, and how often
  intervention: to design with the team
```

The probe never names a specific intervention. Choosing what to try is design work for the user's team. Probes produce evidence about the problem; present them as research, not as solutions.

---

## 9. Templates

**Research plan** (one row per question; test first before test next, then by ASM-ID):

| Q-ID | ASM-ID | Category | Question | Why it matters (IDs it would change) | Method | Who with | Effort | What result would change our mind |
|---|---|---|---|---|---|---|---|---|

**Interview guide**:
1. Purpose (internal, not read out): the Q-IDs and assumptions this guide tests.
2. Warm-up: their role and responsibilities, in their own words.
3. The last specific episode of the job: walk-through, others involved, tools used, what went wrong.
4. Workarounds and their cost.
5. Previous attempts to fix it, and why they stopped.
6. Forces (if relevant): what pushed them to look for change, what held them back.
7. Close: "What should I have asked?" and "Who else should I talk to?"
