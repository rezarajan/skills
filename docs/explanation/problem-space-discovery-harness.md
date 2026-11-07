# The problem-space-discovery harness

`problem-space-discovery` is built as a harness, not a free-form conversation. It
has a defined state (the problem model), defined rules (the control loop and its
checks) and a defined output (the Blueprint or the handoff). It enters, runs,
hands off and exits, and never operates outside those rules.

It helps to read it as a feedback control system:

| Control element | In the harness |
| --------------- | -------------- |
| Setpoint | The definition of done in `SKILL.md` |
| Plant (the state being controlled) | The problem model, `problem-model.yaml` |
| Sensor | `scripts/check_model.py` and the challenge checks |
| Error signal | Test-first and test-next assumptions, unmet definition-of-done criteria, unresolved contradictions |
| Controller | Move selection, ranked by Assumptions Mapping category |
| Actuator | The move: ask, research, apply a framework, challenge, synthesise |
| Supervisor | The state machine in `meta.status`: `intake`, `loop`, `synthesis`, `handoff`, `closed` |

The inner loop runs once per turn. Each move changes the model, the sensor
reads the model back, and the next turn's assessment works on what changed.
That feedback is why the skill keeps an explicit model rather than relying on
prose. The supervisor decides which part of the harness a turn enters. It also
provides the two ways out: the normal path through synthesis and handoff, and
the opt-out, which can be taken from any state.

## Control flow

```mermaid
%%{init: {"flowchart": {"curve": "step", "nodeSpacing": 40, "rankSpacing": 40}}}%%
flowchart TB
    TURN(["User turn"]) --> OPT{"Explicit<br/>opt-out?"}
    OPT -- "no: resume at<br/>meta.status" --> I1
    OPT -- "yes" --> O1

    subgraph INTAKE["intake"]
        direction TB
        I1["Intake question<br/>solution-in-disguise check"] --> I2["Propose depth mode"]
        I2 --> I3["Classify domain (Cynefin)"]
    end

    subgraph LOOP["loop: one pass per turn"]
        direction TB
        A["Assess model<br/>against definition of done"] --> E{"Error left?"}
        E -- "yes" --> P["Pick move by<br/>Assumptions Mapping category"]
        P --> X["Execute move<br/>ask · research · framework · challenge"]
        X --> U["Update model"]
        U --> S["Sensor<br/>check_model.py · challenge checks"]
        S --> R["Report briefly<br/>end of turn"]
        U -. "writes" .-> MODEL[("problem-model.yaml")]
        MODEL -. "next turn reads" .-> A
    end

    subgraph SYNTH["synthesis"]
        direction TB
        Y1["Challenge checks<br/>alternative framing"] --> Y2["Render Blueprint<br/>collapse rule applied"]
    end

    subgraph HAND["handoff"]
        H1["Fill handoff.template.md<br/>from model"]
    end

    subgraph OPTOUT["opt-out, from any state"]
        direction TB
        O1["Quick brief<br/>assumptions · alternative framing"] --> O2["Handoff artifact"]
        O2 --> O3["State boundary once"]
    end

    I3 -- "domain classified,<br/>depth agreed" --> A
    E -- "no: done,<br/>or user asks" --> Y1
    Y2 -- "user ready<br/>for solutions" --> H1
    H1 -- "artifact delivered" --> CLOSED
    O3 --> CLOSED

    CLOSED(["closed"]) --> RE{"Asked to<br/>reopen?"}
    RE -- "no" --> NONE["Answer outside discovery<br/>no intake, no frameworks"]
    RE -- "yes: status = loop,<br/>reload model" --> LOOP

    classDef state fill:#eef2ff,stroke:#4f46e5,color:#1e1b4b
    classDef store fill:#ecfdf5,stroke:#059669,color:#064e3b
    classDef stop fill:#fef2f2,stroke:#dc2626,color:#7f1d1d
    class INTAKE,LOOP,SYNTH,HAND state
    class MODEL store
    class CLOSED,OPTOUT stop
```

## Why the exits matter

A discovery skill without a clean exit tends to keep doing discovery: when the
user opts out, it soft-refuses, and when the user asks a solution question after
the handoff, it starts intake again. The `closed` state fixes both. Once the
handoff is delivered, the harness gives up control until the user asks to
reopen it, and reopening resumes the loop on the saved model instead of
starting over.

## Why one prioritisation method

The controller ranks moves by a single rule, Assumptions Mapping with a fixed
importance test, so two runs on the same model choose the same next move. A
judgment-based ranking makes the loop's behaviour depend on phrasing rather
than on the model. The principle behind the rule is the value of information:
research is worth doing only if its result could change the definition.
