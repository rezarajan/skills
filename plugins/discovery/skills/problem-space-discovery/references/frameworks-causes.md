# Problem decomposition and causal analysis

These tools assume cause and effect can be traced, which holds in Cynefin's clear and complicated domains. In complex domains, use them only on sub-parts that are complicated, and use the systems file for the rest.

Separate, for every problem component: symptoms, immediate causes, contributing factors, underlying causes and structural causes. Record each cause with `status` and at least one competing explanation where one plausibly exists.

## Contents
1. Kepner-Tregoe Problem Analysis (IS / IS NOT)
2. Problem tree
3. Fishbone (Ishikawa)
4. Five Whys, constrained
5. Fault tree
6. Current Reality Tree (Theory of Constraints)
7. Cause-testing checklist

---

## 1. Kepner-Tregoe Problem Analysis (IS / IS NOT)

- **Answers**: Why does this deviation occur here and not there, now and not before?
- **Fits**: A specific deviation from expected performance, with unknown cause, in a complicated domain. Strongest of these tools when the problem is selective (affects some units, places or times but not others).
- **Inputs**: A deviation statement ("what is wrong with what"); data about where it does and does not occur.
- **Writes**: `causes` with `test`; `questions` for missing IS NOT data.
- **Source**: Kepner and Tregoe, The New Rational Manager. Recommended in the German automotive industry's 8D problem-solving handbook (VDA).

Specification table:

| Dimension | IS | IS NOT (closest comparable) | Distinction | Changes |
|---|---|---|---|---|
| What object, what deviation | | | | |
| Where (geographically, on the object) | | | | |
| When (first seen, pattern, in lifecycle) | | | | |
| Extent (how many, how much, trend) | | | | |

Steps:
1. Fill IS and IS NOT for each dimension. The IS NOT must be the closest case that could have the problem but does not; it is not just the opposite of IS.
2. For each pair, ask what is distinctive about the IS compared with the IS NOT.
3. For each distinction, ask what changed in, on, around or about it, and when.
4. Generate possible causes from distinctions and changes, and from expertise.
5. Test each cause: does it explain both the IS and the IS NOT? Note the assumptions needed to make it fit.
6. The most probable cause explains the full pattern with the fewest and most reasonable assumptions.
7. Confirm it with a check in the real world before marking it `validated`.

**Misuse**: Thin IS NOT data. Without it, causes cannot be tested. If IS NOT data is missing, that becomes the next research question.

---

## 2. Problem tree

- **Answers**: How do the causes and consequences of a focal problem relate?
- **Fits**: Complicated problems, development and public-sector planning, workshops with stakeholders.
- **Writes**: `problems` (focal and effects), `causes` with `depth`.
- **Source**: Widely used in development planning and the Logical Framework Approach; described in ODI's (Overseas Development Institute) planning toolkit.

Steps:
1. Agree the focal problem (the trunk).
2. Identify direct causes below it, and their causes below them (roots).
3. Identify consequences above it, and their consequences (branches).
4. Where two causes are independent, place them at the same level.
5. Ask: does this represent reality? Are economic, political and socio-cultural dimensions included? Which causes are getting better, worse or staying the same?

Wording rule: do not phrase a problem as the absence of a solution ("no dashboard", "lack of training"). State the actual negative condition ("principals learn about absence patterns weeks after they start").

The objectives tree that usually follows (rewording problems as goals) is solution planning; do not produce it in this skill unless asked, and then label it as a handoff artifact.

Consider running separate trees with different stakeholder groups; their trees often differ in revealing ways.

---

## 3. Fishbone (Ishikawa)

- **Answers**: Which categories of cause have we not considered?
- **Fits**: Breadth before depth, in complicated domains. Card (2017) recommends it over Five Whys for exactly this reason.
- **Writes**: candidate `causes` with `status: hypothesised`.
- **Source**: Kaoru Ishikawa.

Choose categories that fit the domain:
- Manufacturing (6M): Methods, Machines, Materials, Measurement, Manpower (people), Mother Nature (environment).
- Services and public sector: People, Process, Policy, Place and environment, Technology, Information and measurement, Incentives.
- Data and software systems: Sources, Pipelines, Schemas and contracts, Infrastructure, Configuration, People and process, Monitoring.

Every candidate cause starts as a hypothesis. The fishbone generates candidates; it does not establish causes.

---

## 4. Five Whys, constrained

- **Answers**: How deep does one causal branch go?
- **Fits**: Depth probing on a single, already-evidenced branch in a complicated domain.
- **Source**: Toyota Production System (Taiichi Ohno). Critique: Card, "The problem with '5 whys'" (BMJ Quality and Safety, 2017).

Card's critique, which this skill accepts: Five Whys oversimplifies; it pushes towards a single causal chain when problems are usually multi-causal; its depth of five is arbitrary; and different investigators reach different "root causes" from the same facts.

Constraints when you use it:
- Use it after a fishbone or problem tree, on one branch, not as the whole analysis.
- At each level, ask whether there is more than one answer. If so, branch.
- Attach evidence to each link. A link with no evidence stays a hypothesis.
- Stop when evidence runs out, or when the next "why" leaves the stakeholders' sphere of influence. Do not stop at five for its own sake.
- If the chain ends at "people made a mistake", ask what made the mistake likely. Blame is rarely a root cause.

Never present the output as "the root cause" of a multi-causal problem.

---

## 5. Fault tree

- **Answers**: Which combinations of lower-level failures produce a top-level failure?
- **Fits**: Technical or safety-critical systems where failures combine logically.
- **Method**: Start from the undesired top event. Decompose with AND gates (all inputs needed) and OR gates (any input suffices). Mark basic events with any known frequency data. Minimal cut sets show the smallest combinations that cause the top event.

---

## 6. Current Reality Tree (Theory of Constraints)

- **Answers**: Which few core problems produce most of the observed undesirable effects?
- **Fits**: Organisational systems with many visible symptoms.
- **Source**: Eliyahu Goldratt's Thinking Processes.
- **Method**: List the undesirable effects (UDEs) people observe. Connect them with "if… then…" sufficiency logic, adding the conditions needed for each link to hold. Trace downwards until several UDEs converge on a small number of core problems. Test each link by asking whether the cause is sufficient on its own, or needs another condition.

---

## 7. Cause-testing checklist

Before raising any cause above `hypothesised`:
- Does it explain all of the observations, including where the problem does not occur?
- Is there a competing explanation? Record it in `competing_with`.
- Is the link correlation or causation? What would we expect to see if the cause were removed?
- Does the timing fit (cause before effect)?
- Is the evidence about this population and setting?
- What test would rule it out, and has it been run?
