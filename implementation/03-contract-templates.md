# Standard Contract Templates

Status: Canonical template specification

## 1. Agent Contract Template

Use this structure for every agent.

```markdown
# [Agent Name] — Agent Contract

Status: Canonical / Draft / Deprecated
Category: Router | Evidence | Asset-Class Lead | Specialist | Discovery | Synthesis
Owner of: [analytical block]
Consumes: [inputs]
Produces: [outputs]

## Purpose
[What this agent exists to answer.]

## Scope
[What situations / instruments / workflows it covers.]

## Responsibilities
- [Owned responsibility]

## Non-responsibilities
- [Boundary / prohibited ownership]

## Required inputs
- [Input artifact or context]

## Outputs
- [Report artifact]
- [Structured handoff]

## Evidence requirements
- [Freshness/source/readiness requirements]

## Workflow role
[When it runs and what it depends on.]

## Handoffs
- To Evidence Collector: [requests/challenges]
- To downstream agents: [structured output]
- To IC: [final handoff block]

## Limited / Blocked rules
- Limited when: [...]
- Blocked when: [...]

## Success criteria
- [Observable completion condition]
```

## 2. Skill Contract Template

```markdown
# [Skill Name] — Skill Contract

Status: Canonical / Draft / Deprecated
Used by: [agent/workflow]

## Purpose
[What repeatable method this skill performs.]

## Trigger conditions
- [When invoked]

## Required inputs
- [Required context/artifacts]

## Step sequence
1. [Step]
2. [Step]

## Output contract
- [Expected output]
- [Required fields]

## Guardrails
- [Prohibited behavior]

## Failure states
- Limited when: [...]
- Blocked when: [...]

## Quality checks
- [How to verify output quality]
```

## 3. Workflow Contract Template

```markdown
# [Workflow Name] — Workflow Contract

Status: Canonical / Draft / Deprecated
Trigger: [request type]
Workflow owner: [router/orchestrator]
Final output owner: [agent]

## Entry conditions
- [What starts the workflow]

## Required agents
- [Agent]

## Optional / conditional agents
- [Agent and trigger]

## Sequence
1. Intake and routing
2. Evidence plan
3. Specialist execution
4. Evidence readiness check
5. Final synthesis or Limited/Blocked output

## Required reports
- [artifact.md]

## Evidence requirements
- [readiness/freshness/source requirements]

## Completion rules
- Complete when: [...]
- Limited when: [...]
- Blocked when: [...]

## Positive action gates
- [If applicable]
```

## 4. Report Schema Template

```markdown
# [Report Name] — Report Schema

Artifact: [file_name.md]
Produced by: [agent/skill]
Consumed by: [agents/workflows]
Status values: Complete | Limited | Blocked | Preliminary

## Required metadata
- Subject:
- Request type:
- As-of date:
- Evidence status:
- Output status:
- Limitations:

## Required sections
1. Executive summary
2. Core analysis
3. Evidence notes and limitations
4. Monitoring / triggers
5. Structured handoff

## Optional sections
- [Conditional sections]

## Handoff block
- Downstream relevance:
- Required follow-up:
- Decision constraints:
```

## 5. Normalization rule

When converting legacy PRDs:

- Agent PRD owns scope, responsibility, boundaries, and outputs.
- Method Skill PRD owns procedure and quality checks.
- Framework owns report shape, labels, examples, and reference material.
- Source policies point to the central Evidence Layer unless truly domain-specific.
- Success criteria must be explicit; `Final Standard` can be retained only if mapped to Success Criteria.
