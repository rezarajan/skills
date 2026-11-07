# Problem model schema

The problem model is the single source of truth for the engagement. The Blueprint is rendered from it. Keep it in `problem-model.yaml` when you can write files. When you cannot, it lives in the conversation as the sum of each turn's "Model changes" blocks.

## Contents
1. Top-level structure
2. Shared fields for claim-bearing nodes
3. Entity types
4. Link rules
5. Status transitions
6. Minimal example

## 1. Top-level structure

```yaml
meta:
  title: short name for the engagement
  status: intake | loop | synthesis | handoff | closed
  depth_mode: quick | working | full
  updated: YYYY-MM-DD
  domain:                       # Cynefin classification, per part if needed
    - part: whole situation
      classification: clear | complicated | complex | chaotic | confusion
      rationale: one sentence
  wicked_indicators: []         # which Rittel and Webber characteristics apply
scope:
  in: []
  out: []
  deferred: []
problem_statements:             # newest last; never delete earlier versions
  - id: PS-1
    text: ...
    version_note: why it changed
    alternative_framing: strongest competing framing
candidate_solutions: []         # solutions the user mentioned; parked, not analysed
stakeholders: []
jobs: []
pains: []
gains: []
problems: []
causes: []
constraints: []
assumptions: []
evidence: []
opportunities: []
questions: []
moves: []                       # log: which framework or move, why, what changed
```

### State transitions

`meta.status` records where the harness is. Only these transitions are valid:

| From | To | When |
|---|---|---|
| `intake` | `loop` | The domain is classified and a depth mode is agreed |
| `loop` | `synthesis` | The user asks, or the definition of done is met |
| `synthesis` | `handoff` | The user is ready to move to solutions |
| `handoff` | `closed` | The handoff artifact has been delivered |
| any | `closed` | Explicit opt-out: quick brief and handoff artifact delivered |
| `closed` | `loop` | The user explicitly asks to reopen; reload the model |

IDs use a type prefix and a number: `STK-1`, `JOB-1`, `PAIN-1`, `GAIN-1`, `PRB-1`, `CAU-1`, `CON-1`, `ASM-1`, `EVD-1`, `OPP-1`, `Q-1`, `PS-1`. Never reuse an ID, even after deleting a node.

## 2. Shared fields for claim-bearing nodes

Jobs, pains, gains, problems, causes, constraints and opportunities are claims, and carry:

```yaml
basis: fact | observation | assumption | hypothesis | interpretation
provenance: user | secondary_research | primary_research | agent_inference
confidence: high | moderate | low | very_low
supported_by: [EVD-…]
contradicted_by: [EVD-…]
```

Rules:
- `basis: fact` requires at least one `supported_by` evidence node whose `population` matches the claim's stakeholders.
- `provenance: agent_inference` can never have `basis: fact` or `confidence: high`.
- If `contradicted_by` is non-empty, the node's confidence cannot be `high`, and the contradiction must appear in the next progress summary.
- `observation` means something seen, heard or reported by a named source. Record who reported it.

## 3. Entity types

**Stakeholder** (`STK`)
```yaml
- id: STK-1
  name: Classroom teachers
  roles: [end_user]   # end_user | beneficiary | decision_maker | economic_buyer | channel_partner | operator | regulator | influencer | indirectly_affected
  primary: true       # exactly one primary stakeholder once chosen
  primary_reason: why this stakeholder was chosen (required when primary is true)
  interests: ...
  incentives: ...
  power: high | medium | low
  interest: high | medium | low
  legitimacy: high | medium | low
  urgency: high | medium | low
  worldview: one sentence on how they see the problem (CATWOE W)
  relationships: [{to: STK-2, nature: reports to}]
```

**Job** (`JOB`): `statement` (verb + object + context), `type` (functional | emotional | social | supporting), `stakeholder`, `importance` (high | medium | low), plus the shared fields. Optional `job_map_step`.

**Pain** (`PAIN`) and **Gain** (`GAIN`): `statement`, `stakeholder`, `job`, `severity` or `relevance` (high | medium | low), `pain_type` (obstacle | risk | cost | delay | uncertainty | frustration | unmet_expectation) or `gain_type` (required | expected | desired | unexpected), plus the shared fields. Optional `outcome_statement` in ODI form.

**Problem** (`PRB`): a problem component.
```yaml
- id: PRB-1
  statement: Attendance data reaches principals too late to act on
  kind: symptom | problem          # symptom = observable effect, not yet explained
  experienced_by: [STK-1]
  where: ...
  when: ...
  frequency: ...
  consequences: [...]
  iceberg_layer: event | pattern | structure | mental_model
  priority: {seriousness: , urgency: , growth: , score: , evidence_strength: , rationale: }
  # plus shared fields
```

**Cause** (`CAU`)
```yaml
- id: CAU-1
  statement: ...
  depth: immediate | contributing | underlying | structural
  causes: [PRB-1]                  # or [CAU-2] for chains
  status: hypothesised | supported | validated | refuted
  competing_with: [CAU-3]          # alternative explanations for the same effect
  test: how this cause could be confirmed or ruled out
  # plus shared fields
```

**Constraint** (`CON`): `statement`, `type` (regulatory | budget | technical | capacity | political | cultural | time), `hard` (true | false), plus the shared fields.

**Assumption** (`ASM`)
```yaml
- id: ASM-1
  statement: Principals would act on weekly attendance data if they had it
  category: desirability | feasibility | viability | adaptability | causal | contextual
  if_wrong_breaks: [PS-1, STK-1]        # IDs this assumption holds up
  importance: high | low                # computed by the fixed test below
  importance_rationale: one sentence on why it breaks what it names
  supported_by: [EVD-…]
  contradicted_by: [EVD-…]
  evidence_level: strong | some | none  # computed from supported_by, below
  test: Test Card summary, or the research that would resolve it
  related: [PRB-1, OPP-2]
```

**Fixed importance test.** `importance: high` if and only if `if_wrong_breaks` names at least one of:
- the latest problem statement's ID;
- the primary stakeholder's ID;
- the ID of the highest-priority problem (highest `priority.score`).

Otherwise `importance: low`.

**Computed evidence level**, from the best `supported_by` evidence:
- `none`: no supporting evidence.
- `some`: the best supporting evidence has certainty `low` or `very_low`.
- `strong`: the best supporting evidence has certainty `moderate` or `high`.

Importance and evidence level together place the assumption in an Assumptions Mapping category (test first, test next, foundation, defer).

**Evidence** (`EVD`)
```yaml
- id: EVD-1
  summary: one line, in your own words
  source: name, author or organisation, URL or document, date
  kind: direct | indirect | anecdotal
  say_or_do: say | do | mixed           # opinion or prediction versus behaviour or commitment
  population: who and where it describes
  certainty: high | moderate | low | very_low
  downgrades: [risk_of_bias, indirectness, inconsistency, imprecision, selection_or_publication_bias, staleness]
  collected_by: user | agent | third_party
```

**Opportunity** (`OPP`): an unmet need worth addressing, stated as a need, not a solution.
```yaml
- id: OPP-1
  statement: Principals need early warning of attendance decline while intervention is still cheap
  serves_outcome: desired outcome it would move
  parent: OPP-… or null                 # opportunities nest
  derived_from: [PAIN-2, JOB-1]
  stakeholders: [STK-1]
  odi: {importance: , satisfaction: , score: , sample: }   # only with survey data
  appraisal: {importance: , evidence_strength: , reach: , strategic_fit: , rationale: }
  # plus shared fields
```

**Question** (`Q`): `question`, `why_it_matters`, `tests` (`[ASM-…]`, the assumptions it would resolve), `blocks` (IDs it would change), `resolution` (secondary research | interview | observation | data analysis | experiment | ask user), `status` (open | answered | dropped).

**Move** (log entry): `turn`, `move` (ask | research | framework:NAME | challenge | synthesise | handoff), `why`, `changed` (IDs).

## 4. Link rules

- Every problem has at least one `experienced_by` stakeholder.
- Every cause links to at least one problem or cause.
- Every opportunity derives from at least one pain, gain, job or problem.
- Every assumption in the test first or test next category has a `test`.
- Every open question has `tests` naming at least one assumption. If a gap has no assumption yet, create one.
- All referenced IDs must exist.
- A node that nothing links to, and that links to nothing, is either missing its links or should be removed.

## 5. Status transitions

- `hypothesised` → `supported`: at least one direct or indirect evidence node, certainty moderate or better.
- `supported` → `validated`: direct evidence about the relevant population, and the strongest competing cause has been ruled out or weakened.
- Any status → `refuted`: direct evidence against the claim. Keep refuted nodes; they show what was ruled out.
- Downgrade immediately when contradicting evidence arrives, and record why in `moves`.

## 6. Minimal example

```yaml
meta:
  title: Late attendance follow-up
  depth_mode: working
  domain:
    - part: data delivery
      classification: complicated
      rationale: Cause and effect are traceable by inspecting the pipeline.
    - part: principals' follow-up behaviour
      classification: complex
      rationale: Depends on workload, culture and parent relationships; outcomes emerge.
scope:
  in: [primary schools, attendance follow-up]
  out: [curriculum, teacher performance management]
problem_statements:
  - id: PS-1
    text: Principals experience late awareness of chronic absence when trying to intervene early, because attendance summaries arrive monthly, resulting in interventions after patterns are established.
    alternative_framing: Principals receive data in time but lack capacity to act on it.
candidate_solutions: [attendance dashboard]
stakeholders:
  - {id: STK-1, name: Principals, roles: [end_user, decision_maker], primary: true, primary_reason: Their follow-up behaviour must change for absence outcomes to improve}
  - {id: STK-2, name: Students with emerging absence patterns, roles: [beneficiary], primary: false}
problems:
  - id: PRB-1
    statement: Interventions start after absence is entrenched
    kind: symptom
    experienced_by: [STK-2]
    basis: observation
    provenance: user
    confidence: moderate
    supported_by: []
causes:
  - id: CAU-1
    statement: Summaries are monthly
    depth: immediate
    causes: [PRB-1]
    status: hypothesised
    competing_with: [CAU-2]
    test: Compare intervention timing at schools that already get weekly data.
    basis: hypothesis
    provenance: user
    confidence: low
  - id: CAU-2
    statement: Principals lack time to act on absence data
    depth: contributing
    causes: [PRB-1]
    status: hypothesised
    test: Interview principals about the last absence case they handled.
    basis: hypothesis
    provenance: agent_inference
    confidence: low
```
