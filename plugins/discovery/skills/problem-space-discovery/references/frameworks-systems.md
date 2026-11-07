# Systems thinking frameworks

Use these when the problem persists despite fixes, when stakeholders' actions interact, or when the domain is complex. Their output is a map of what keeps the problem in place, not a root cause.

## Contents
1. Iceberg model
2. Causal loop diagrams
3. System archetypes
4. Leverage points
5. Theory of Constraints: the bottleneck lens
6. Questions to ask of any system map

---

## 1. Iceberg model

- **Answers**: What lies beneath the visible events?
- **Fits**: Recurring problems; framing conversations with stakeholders.
- **Writes**: `iceberg_layer` on problems and causes.

| Layer | Question | Example |
|---|---|---|
| Events | What just happened? | A student was flagged for chronic absence in May. |
| Patterns | What has been happening over time? | Flags cluster in the final term, every year. |
| Structures | What produces the pattern? Rules, incentives, flows, physical layout. | Data is summarised monthly; follow-up responsibility is undefined. |
| Mental models | What beliefs keep the structure in place? | "Absence is a family matter, not the school's." |

Fixes at the event level rarely last. Note which layer each proposed cause sits at.

---

## 2. Causal loop diagrams

- **Answers**: Which feedback loops sustain or amplify the problem?
- **Fits**: Complex domains; problems that grow, oscillate or resist fixes.
- **Writes**: `causes` linked in cycles; `moves` log with the loops described.

Notation:
- Variables are nouns that can increase or decrease ("workload", "trust in data"), not events.
- A link marked **+** (or **s**, same) means the variables move in the same direction; **−** (or **o**, opposite) means opposite directions.
- A loop is **reinforcing (R)** if it has an even number of − links; **balancing (B)** if odd.
- Mark **delays** on links where effects take time; delays explain overshoot and why fixes look like they failed.

In text environments, describe each loop as a sentence chain ("More workload → less follow-up → more entrenched absence → more workload: R1") and offer a diagram if the environment supports one.

---

## 3. System archetypes

- **Answers**: Does this situation match a known recurring structure, and what does that structure usually require?
- **Source**: Senge, The Fifth Discipline (1990), with Kemeny, Goodman and Kiefer; system dynamics tradition from Forrester and Meadows.

| Archetype | Signature | Diagnostic question |
|---|---|---|
| Fixes that fail | A quick fix relieves the symptom, then a delayed side effect makes it worse | Did the problem return, worse, after a fix? |
| Shifting the burden | A symptomatic fix is used instead of a fundamental one, and capacity for the fundamental fix erodes | Are we relying on a workaround that makes the real fix harder? |
| Limits to growth (limits to success) | Growth stalls as it meets a constraint | Did something work well, then plateau? What is it hitting? |
| Eroding goals (drifting goals) | Standards are lowered to close the gap with performance | Have targets quietly been lowered? |
| Escalation | Two parties each respond to the other's actions with more of the same | Is each side reacting to the other? |
| Success to the successful | Resources flow to whoever succeeded first, starving others | Do early winners keep getting more? |
| Tragedy of the commons | Individually rational use depletes a shared resource | Is a shared resource being drawn down by everyone? |
| Growth and underinvestment | Capacity investment lags demand, performance drops, investment is withheld | Is under-capacity being used to justify further under-investment? |

A match is a hypothesis. Confirm it by checking whether the loops and delays it implies are present in the evidence.

---

## 4. Leverage points

- **Answers**: Where in the system would change matter most?
- **Fits**: After the system is mapped; for appraising opportunities, not for choosing solutions.
- **Source**: Donella Meadows, "Leverage Points: Places to Intervene in a System" (1999). Listed from least to most effective:

12. Constants, parameters, numbers (subsidies, taxes, standards)
11. Sizes of buffers and other stabilising stocks
10. Structure of material stocks and flows
9. Lengths of delays, relative to the rate of system change
8. Strength of negative (balancing) feedback loops
7. Gain around positive (reinforcing) feedback loops
6. Structure of information flows (who has access to what)
5. Rules of the system (incentives, punishments, constraints)
4. Power to add, change, evolve or self-organise system structure
3. Goals of the system
2. Mindset or paradigm from which the system arises
1. Power to transcend paradigms

Meadows' warning: most attention goes to parameters, which have the least leverage. In discovery, use the list to label where each opportunity would act, and to notice when every opportunity on the table is a parameter change. Information flows (6) are a frequent, under-recognised cause of failure in data and reporting problems.

---

## 5. Theory of Constraints: the bottleneck lens

- **Answers**: Is one constraint limiting the whole system's throughput?
- **Fits**: Flow problems: delays, backlogs, capacity.
- **Source**: Goldratt, The Goal (1984). Five focusing steps: identify the constraint, exploit it, subordinate everything else to it, elevate it, repeat.
- **Use in discovery**: identify the constraint and gather evidence that it is the constraint (queues form before it; capacity elsewhere sits idle). The later steps are solution work.

---

## 6. Questions to ask of any system map

- What behaviours reinforce the current situation, and who benefits from it?
- Does solving one part create a problem elsewhere?
- Do stakeholders experience competing outcomes from the same structure?
- Where are the delays, and do they explain why past fixes seemed to fail?
- Which information is missing, late or held by the wrong people?
- What structural condition, rule or goal keeps the problem in place?
