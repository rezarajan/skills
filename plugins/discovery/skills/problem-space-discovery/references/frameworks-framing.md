# Framing frameworks

Use these at intake and whenever the nature of the problem is in doubt. Each card lists: the question it answers, where it fits, required inputs, what it writes to the model, common misuse, and the source.

## Contents
1. Cynefin
2. Wicked-problem check
3. Kepner-Tregoe Situation Appraisal
4. 5W1H
5. Problem statement forms
6. Where this skill sits in the Double Diamond

---

## 1. Cynefin

- **Answers**: What kind of situation is this, and therefore which kind of analysis is valid?
- **Fits**: Always, at intake. Re-check when evidence surprises you.
- **Inputs**: The user's description; any history of attempted fixes.
- **Writes**: `meta.domain` (per part), and it constrains which frameworks you may apply.
- **Source**: Snowden, Kurtz and Snowden (2003, IBM Systems Journal); Snowden and Boone, "A Leader's Framework for Decision Making" (HBR, 2007). Domain names changed over time: known/knowable became simple/complicated, then obvious, now clear.

| Domain | Cause and effect | Decision pattern | What it means for discovery |
|---|---|---|---|
| Clear | Obvious to anyone | Sense, categorise, respond | Light discovery. Confirm the category, apply known practice. Watch for complacency. |
| Complicated | Discoverable through analysis or expertise | Sense, analyse, respond | Causal tools are valid: KT, problem trees, fishbone, fault trees. Bring in experts. |
| Complex | Visible only in hindsight; emergent | Probe, sense, respond | Hold several hypotheses at once. Map the system. Recommend small safe-to-fail probes rather than more analysis. Never claim a single root cause. |
| Chaotic | No stable relationship | Act, sense, respond | Stabilise first. Discovery is premature; help scope what to stabilise, then reclassify. |
| Confusion (centre) | Unclear which domain applies | Break apart | Split the situation into parts and classify each. |

Diagnostic questions:
- Has this exact problem been solved before, here or elsewhere, with a known fix? (clear)
- Could a competent expert trace the cause given time and data? (complicated)
- Do people's responses to interventions change the problem? Have reasonable fixes produced surprising effects? (complex)
- Is harm happening right now with no time to analyse? (chaotic)

**Misuse**: Classifying the whole situation once and forgetting it. Different parts often sit in different domains (a data pipeline fault is complicated; how people respond to the data is complex). Treating "complex" as "difficult". The dividing line is whether cause and effect can be known in advance.

---

## 2. Wicked-problem check

- **Answers**: Is the problem definition itself contested and entangled with solutions?
- **Fits**: Social, policy and multi-stakeholder organisational problems.
- **Source**: Rittel and Webber, "Dilemmas in a General Theory of Planning" (Policy Sciences, 1973), which lists ten characteristics.

Indicators to check (record matches in `meta.wicked_indicators`):
- No definitive formulation: how you frame the problem already implies a solution.
- No stopping rule: there is no point at which it is clearly solved.
- Solutions are better or worse, not right or wrong.
- Every attempted solution has consequences that cannot be undone.
- Each instance is essentially unique.
- It can be seen as a symptom of another problem.
- Stakeholders hold sharply different worldviews about what the problem is.

Implications when several apply: treat it as complex in Cynefin terms; expect the problem statement to keep evolving; run CATWOE per worldview (frameworks-stakeholders.md); make the scope and the chosen framing explicit, and say whose framing it is.

---

## 3. Kepner-Tregoe Situation Appraisal

- **Answers**: The user brought a tangle. Which concerns are separate, which come first, and what kind of analysis does each need?
- **Fits**: Any domain, especially at intake when several issues arrive as one.
- **Inputs**: A list of concerns, however messy.
- **Writes**: Separate `problems`, each with `priority` filled; `questions` for missing facts.
- **Source**: Kepner and Tregoe, The New Rational Manager. KT's four processes are Situation Appraisal, Problem Analysis, Decision Analysis and Potential Problem Analysis.

Steps:
1. **List** threats, opportunities and concerns without discussing them yet.
2. **Separate and clarify**: split compound concerns into specific, actionable parts. Ask "what exactly do we mean by…", "what evidence do we have…", "what different deviations or decisions are inside this?"
3. **Set priority** relative to each other on three dimensions:
   - Seriousness: current impact on people, safety, cost, service, reputation.
   - Urgency: when does it need to be resolved before it becomes harder or impossible?
   - Growth: if left alone, will it get worse, and how fast?
4. **Determine the analysis needed**: a deviation with unknown cause → Problem Analysis (frameworks-causes.md); a choice → out of scope here, note it; a future risk → record as a constraint or assumption.

**Misuse**: Scoring priorities without evidence. Record the evidence behind each rating.

---

## 4. 5W1H

- **Answers**: What do we actually know about the situation?
- **Fits**: Vague or early-stage challenges.
- **Writes**: Scope, stakeholders, problem `where`/`when`/`frequency`, open questions.

Ask only the questions whose answers are missing and would change the framing:
- **What** is happening? What is the observable evidence?
- **Who** experiences it, causes it, notices it, decides about it?
- **Where** does it occur, and where does it not?
- **When** did it start, how often does it happen, and is it changing?
- **Why** does it matter, and to whom? What triggered this investigation now?
- **How** is it currently handled? What has already been tried, and what happened?

Asking "where does it not occur?" early pays off: it sets up IS / IS NOT analysis later.

---

## 5. Problem statement forms

Choose the form that fits the domain. Record each version in `problem_statements` with a version note.

- **Default (from this skill)**: "[Stakeholder] experiences [problem] when trying to [job or outcome], because of [evidence-supported contributing factors], resulting in [observable consequences]."
- **Deviation statement (KT)**, for complicated problems: "What is wrong with what?" — an object and its deviation from expected performance, such as "Nightly enrolment loads for 3 of 40 schools are incomplete since March."
- **Point of view (design thinking)**: "[User] needs [need] because [insight]." Use when the insight is evidenced, not assumed.
- **Outcome framing**: the measurable outcome that should move, in ODI form (see frameworks-needs.md).

Quality checks for any statement:
- It names a stakeholder, not "users" or "the organisation".
- It contains no solution. "Lack of a dashboard" is a solution in disguise; ask what the dashboard would change.
- It is not phrased as the absence of something unless that absence is itself the harm.
- Every "because" clause points to a cause in the model, with its confidence visible.
- It is narrow enough that a team could tell whether it improved.

---

## 6. Where this skill sits in the Double Diamond

The UK Design Council's Double Diamond (2004/2005; expanded into the Framework for Innovation in 2019) has four phases: Discover, Define, Develop, Deliver. The first diamond is the problem space; the second is the solution space. This skill covers the first diamond: diverge in Discover (widen context, stakeholders, needs, causes) and converge in Define (prioritise, state, bound). The 2019 framework's principles of putting people first, communicating visually and inclusively, collaborating and co-creating, and iterating continuously apply throughout.

Use this framing when the user asks where they are in the process, or wants to jump to Develop before Define has converged.
