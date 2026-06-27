# Evidence Request Protocol

## 1. Purpose

This protocol defines how downstream agents request additional evidence, challenge readiness, and register specialist-discovered evidence.

It prevents uncontrolled research, hidden sources, silent override of evidence limitations, and decision-relevant conclusions based on unregistered evidence.

## 2. Structured Evidence Request

Specialist agents should request additional evidence using this template:

```text
Requesting Agent:
Target Claim / Question:
Why It Matters:
Required Evidence:
Preferred Source Type:
Materiality:
Priority:
Current Limitation:
Decision Impact:
Required for Complete Report:
Deadline / Freshness Need:
```

Allowed materiality:

```text
Critical
Material
Contextual
Optional
Not Material
```

Allowed priority:

```text
High
Medium
Low
Deferred
```

Requests should be specific. Vague requests such as “find more on margins” or “check risks” should be rejected or returned for clarification.

## 3. Evidence Request Response

Evidence Collector response:

```text
Request Status:
Evidence Found:
Evidence Not Found:
Sources Checked:
Source Quality:
Freshness:
Claim Support Status:
Effect on Analytical Evidence:
Effect on Decision Evidence:
Remaining Limitation:
Recommended Next Step:
```

Allowed request statuses:

```text
Completed
Partially Completed
Unable to Complete
Blocked by Access
Not Material
Deferred
```

## 4. Evidence Addition Notice

Used when a specialist discovers material evidence.

Template:

```text
Discovering Agent:
Source:
Evidence Type:
Claim Supported:
Why Material:
Source Date:
Accessed Date:
Proposed Source Tier:
Freshness:
Limitation:
Decision Impact:
Registration Required Before IC:
```

Material specialist-discovered evidence may be used provisionally for analysis, but material claims, valuation inputs, risk conclusions, or IC decision logic may rely on it only after the evidence is registered, tiered, timestamped, and classified in the evidence pack.

## 5. Readiness Challenge Protocol

Specialists may challenge Evidence Collector readiness, but they may not silently override it.

Template:

```text
Original Evidence Status:
Challenging Agent:
Reason for Challenge:
Claim / Evidence Area Affected:
Additional Domain Rationale:
New Evidence Included:
Proposed Revised Status:
Decision Impact:
Evidence Collector Response:
Final Recorded Status:
```

If unresolved, the evidence status should be marked contested and passed downstream.

Contested evidence should not support strong final decision logic without caveat.

## 6. Pre-IC Evidence Lock Request

Before Investment Committee synthesis, the orchestrator or IC workflow should request an evidence lock.

Request template:

```text
Workflow:
Target:
Evidence Pack:
Specialist Reports Completed:
Known Evidence Additions:
Known Refresh Triggers:
Requested IC Output Type:
```

Evidence Collector response:

```text
Evidence Lock Status:
Decision Evidence Status:
Allowed IC Output Status:
Refresh Required:
Open Gaps:
Open Contradictions:
Positive Action Constraints:
Lock Timestamp:
```

Allowed evidence lock statuses:

```text
Locked
Locked with Caveats
Refresh Required
Blocked
```

## 7. Prohibited Request Patterns

Specialists should not make vague requests such as:

```text
Find more on margins.
Check risks.
Look up latest news.
Get better valuation data.
```

They must specify the claim, source need, materiality, freshness need, and decision impact.

## 8. Practical Examples

### Valuation Request

```text
Requesting Agent: Valuation & Expectations Agent
Target Claim / Question: Are consensus revenue estimates current enough to test market-implied expectations?
Why It Matters: Positive IC action requires valuation evidence that reflects current expectations.
Required Evidence: Latest consensus revenue / EPS estimates and estimate revision trend.
Preferred Source Type: Recognized market data provider or reputable consensus source.
Materiality: Critical
Priority: High
Current Limitation: Current evidence pack has market price but no verified estimates.
Decision Impact: IC memo should remain Limited without this evidence.
Required for Complete Report: Yes
Freshness Need: Latest available as of analysis date.
```

### Risk Request

```text
Requesting Agent: Risk / Red Team Agent
Target Claim / Question: Is customer concentration thesis-critical and sufficiently disclosed?
Why It Matters: Concentrated demand could materially affect revenue durability and downside risk.
Required Evidence: Direct customer concentration disclosure, segment disclosure, or bounded proxy evidence.
Preferred Source Type: Company filing, earnings call transcript, or official customer disclosure.
Materiality: Material
Priority: Medium
Current Limitation: Evidence pack has segment data but no direct customer concentration disclosure.
Decision Impact: Risk review may proceed as Limited; IC should not treat demand durability as fully verified.
Required for Complete Report: No, unless concentration is central to the thesis.
Freshness Need: Latest annual or quarterly disclosure.
```
