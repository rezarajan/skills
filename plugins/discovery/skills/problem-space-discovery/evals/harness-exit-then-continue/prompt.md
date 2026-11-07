---
tags: [problem-space-discovery]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Earlier in this conversation:

> **User:** Skip the discovery. Nurses at our clinics forget to follow up on abnormal test results. Just tell me what to build.
>
> **Assistant:** Your direction assumes the gap is nurses remembering, rather than results reaching them late or ownership of follow-up being unclear. Discovery is now closed; solution design is a separate step.
>
> **Handoff**
> 1. Core problem statement: Clinic nurses miss follow-up on abnormal results when results arrive outside their working queue, resulting in delayed patient contact (low confidence; user report only).
> 2. Primary stakeholder: clinic nurses (STK-1), because they own patient follow-up.
> 3. Assumptions: ASM-1 nurses see every abnormal result; ASM-2 a reminder at the right moment would prompt action.
> 4. Strongest alternative framing: ownership of follow-up is unclear between nurses and physicians. Evidence for it: missed cases cluster where the ordering physician is off site.
> 5. Constraints: patient data stays within the clinical record system; no extra login for nurses.
> 6. Acceptance signals: median time from abnormal result to patient contact falls; fewer results with no recorded follow-up after seven days.
> 7. Open assumptions to test: test first ASM-1, ASM-2.
> 8. How might we make sure every abnormal result reaches someone who knows it is theirs to act on?

Thanks. What should the notification to the nurse say?
