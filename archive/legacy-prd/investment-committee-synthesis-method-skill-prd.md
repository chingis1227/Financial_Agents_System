# Investment Committee Synthesis Method Skill PRD

## Purpose

This skill defines how the Investment Committee Agent synthesizes evidence, specialist reports, valuation, risk, and context into a final investment committee memo.

The skill is not a research skill. It is a synthesis, judgment, and memo-writing method.

Its purpose is to help the IC Agent produce a final memo that is:

- evidence-backed;
- decision-oriented;
- professionally written;
- readable in one sitting;
- clear about action, reasoning, assumptions, risks, and monitoring;
- strict about uncertainty and missing data.

## Core Question

```text
How should the IC Agent transform the evidence pack and specialist reports into a coherent final investment judgment?
```

## Skill Owner

Primary owner:

```text
Investment Committee Agent
```

This skill may be used only when the IC Agent is producing or preparing a final IC memo.

## Required Inputs

The skill requires a structured IC synthesis request.

```yaml
ic_synthesis_request:
  request_id:
  user_question:
  asset_or_theme:
  asset_class:
  memo_profile:
  target_depth:
  intended_use:
  portfolio_context_available:
  required_reports:
  optional_reports:
  missing_reports:
  evidence_pack_path:
  specialist_report_paths:
  known_limitations:
  requested_output_path:
```

For a Company / Asset-first Standard IC Memo, the expected inputs are:

- intake context;
- evidence pack;
- lead asset analysis;
- valuation / expectations analysis;
- risk / red team review;
- relevant context modules where material.

## Method Overview

The synthesis method has ten steps.

```text
1. Readiness check
2. Memo profile selection
3. Evidence and freshness check
4. Specialist input extraction
5. Materiality filtering
6. Tension and contradiction synthesis
7. Decision formation
8. Memo drafting
9. Verification and anti-hallucination check
10. Structured output metadata and follow-up requests
```

## Step 1 — Readiness Check

Before drafting, the IC Agent must verify whether the required inputs exist and are usable.

The agent should check:

- Is there an evidence pack?
- Is there a lead asset analysis?
- Is there valuation / expectations analysis?
- Is there risk / red team review?
- Are relevant context modules present where material?
- Are any required files missing?
- Are any inputs stale, contradictory, or unsupported?
- Is the workflow scope clear?

If critical inputs are missing, the agent should not improvise.

It should return:

```text
No Decision — More Work Required
```

with required follow-up steps.

## Step 2 — Memo Profile Selection

The skill supports adaptive memo profiles.

Currently fully defined:

```text
Company / Asset-first Standard IC Memo
```

Supported non-equity / non-company profiles use the relevant upstream specialist framework rather than forcing an equity-style memo:

- sector / industry memo;
- theme memo;
- ETF memo;
- commodity memo;
- crypto memo;
- fixed income memo.

The IC Agent should not force an equity-style memo onto non-equity assets. If a profile needs asset-specific sections that are not covered by available specialist reports, the output should be Limited and should state the missing inputs directly.

## Step 3 — Evidence and Freshness Check

The agent must check evidence quality before synthesis.

It should identify:

- strongest evidence areas;
- weak or missing evidence areas;
- stale data;
- proxy data;
- unverified claims;
- source hierarchy issues;
- valuation as-of date;
- market data as-of date;
- catalyst/news freshness;
- risk event freshness.

Market-sensitive conclusions must include relevant dates where material.

Example:

```text
Market Data As Of: 25 June 2026
```

If stale data affects the decision, the memo should be Limited or Blocked.

## Step 4 — Specialist Input Extraction

The agent should extract the decision-relevant contribution from each specialist report.

It should not summarize every detail.

For each available specialist input, identify:

```text
1. Key finding
2. Evidence strength
3. Investment implication
4. Material risks or caveats
5. Confidence / limitation notes
6. Follow-up needs, if any
```

The IC Agent should translate specialist inputs into investment language.

Bad:

```text
The Risk Agent concluded regulatory risk is high.
```

Better:

```text
Regulatory exposure is a material risk because it could reduce growth visibility and cap valuation upside unless the issue is resolved.
```

## Step 5 — Materiality Filtering

The agent must apply a materiality filter.

Include only information that affects:

- thesis;
- valuation;
- risk/reward;
- timing;
- portfolio role;
- decision confidence;
- monitoring.

Do not include details simply because they exist in a specialist report.

The IC memo is not a compressed version of all specialist reports. It is a decision document.

## Step 6 — Tension and Contradiction Synthesis

The IC Agent must identify and resolve key analytical tensions.

Common tensions:

- business quality vs valuation;
- long-term thesis vs near-term setup;
- positive catalysts vs thesis-breaker risks;
- supportive macro vs crowded positioning;
- attractive valuation vs weak asset quality;
- strong theme vs poor investment vehicle;
- consensus optimism vs actual evidence.

The agent should explain:

- what the tension is;
- why it matters;
- which side carries more weight;
- how it affects the action;
- what evidence would change the conclusion.

If the final decision differs from the general tone of specialist reports, the IC Agent must explain why.

## Step 7 — Decision Formation

The agent should form the final decision using this hierarchy:

```text
1. Evidence sufficiency
2. Thesis-breaker / permanent impairment risk
3. Valuation / expectations
4. Business / asset quality
5. Catalysts / timing / positioning
6. Light portfolio role
7. Monitoring clarity
```

This is not a scoring formula. It is a professional judgment sequence.

The IC Agent should answer:

- Is a responsible decision possible?
- Is the asset attractive?
- Is the price / expectation setup attractive?
- What can break the thesis?
- Is now a good time to act?
- What should a new investor do?
- What should an existing holder do?
- What would change the view?

## Positive Action Gate

The agent must not issue positive action unless valuation and risk review are available and sufficient.

Positive actions include:

- Initiate Position;
- Add to Existing Position;
- Build Gradually.

If valuation or risk is missing, positive action is prohibited.

## Action Language

The memo should use natural action labels.

For a new position:

- Initiate Position;
- Build Gradually;
- Do Not Initiate Yet;
- Avoid;
- No Decision — More Work Required.

For existing holders:

- Add to Existing Position;
- Maintain / Hold;
- Reduce Exposure;
- Exit Position;
- No Decision — More Work Required.

The memo should avoid awkward internal labels such as:

```text
New Money Action
```

Use:

```text
For a New Position
For Existing Holders
```

## Decision Confidence Method

Decision Confidence must always include explanation.

Preferred format:

```text
Decision Confidence: High / Moderate / Low / Insufficient Basis
Why: ...
What would raise confidence: ...
What would lower confidence: ...
```

Decision Confidence reflects:

- evidence quality;
- valuation support;
- risk/reward asymmetry;
- thesis durability;
- missing data;
- contradiction severity;
- monitoring clarity.

It is not a probability forecast.

## Step 8 — Memo Drafting

The default Standard Company / Asset-first IC Memo structure is:

```text
## Final Investment Memo

1. Investment View
2. Action Box
3. Why This Action, Not the Alternatives
4. What Matters Most
5. Investment Scorecard
6. Situation Overview
7. The Core Debate
8. Core Thesis
9. Key Assumptions
10. Integrated Evidence Synthesis
11. What Is Priced In
12. Where the Market May Be Wrong
13. Bull / Base / Bear Cases
14. Risks and Thesis Breakers
15. Catalysts and Monitoring Plan
16. Next Steps
17. Evidence & Data Quality Appendix
```

The memo should be structured, but not robotic.

It must read like a professional investment memo, not a system log.

## Writing Standard

The IC memo should:

- explain the picture clearly;
- use natural investment language;
- avoid generic AI phrasing;
- avoid agent-by-agent narration;
- avoid empty labels;
- explain practical meaning;
- preserve uncertainty;
- remain concise but substantive.

The reader should finish the memo with a clear understanding of:

- what matters;
- what is priced in;
- what can go right;
- what can go wrong;
- why the action follows;
- what to monitor next.

## Action Box Method

The Action Box should include:

```text
For a New Position:
For Existing Holders:
Practical Meaning:
Primary Reason:
Decision Confidence:
Time Horizon:
Portfolio Role:
Reassessment Trigger:
Evidence Caveat: [only if material]
```

Complete memos do not need to say “Complete” in the Action Box.

Limited memos should include a natural Evidence Caveat only when material.

Blocked memos must begin clearly with:

```text
No Decision — More Work Required
```

## Investment Scorecard Method

The scorecard should be qualitative, not numeric by default.

Example:

```text
Business Quality: Strong
Valuation / Expectations: Demanding
Risk Profile: Manageable but asymmetric
Macro Backdrop: Mixed
Catalysts: Moderate
Market Positioning: Probable crowded long; not a standalone action signal
Overall Risk/Reward: Attractive business, imperfect entry.
```

No default 8/10 or numeric scoring.

## Scenario Method

Bull / Base / Bear cases are required for Standard IC Memo.

Each scenario should explain:

- what must be true;
- key drivers;
- valuation / expectation implication;
- risk implication;
- what would make the scenario more likely.

No scenario probabilities by default unless supported by:

- explicit model;
- user request;
- robust evidence.

## Risk Method

The Risks and Thesis Breakers section should include 3–5 major risks.

For each:

```text
Risk:
Why it matters:
Thesis breaker condition:
```

Do not create a long risk laundry list.

Distinguish between:

- normal risk;
- material risk;
- thesis breaker;
- permanent impairment risk.

## Monitoring Method

The Catalysts and Monitoring Plan should include:

```text
Near-term catalysts:
Confirmation signals:
Warning signals:
Invalidation triggers:
```

The plan should answer:

```text
What should be watched after this memo?
```

## Appendix Method

The Evidence & Data Quality Appendix should include:

- materials reviewed;
- evidence quality by area;
- missing / stale / proxy data;
- key limitations;
- source freshness notes;
- follow-up requests.

It should not:

- become a full bibliography;
- duplicate all specialist reports;
- hide material caveats that belong in the main memo;
- introduce new unsupported analysis.

## Step 9 — Verification and Anti-Hallucination Check

Before finalizing, the IC Agent must run a silent pre-final check.

The check should verify:

- no unsupported material factual claims;
- no invented numbers, dates, events, or sources;
- no new research inserted without permission;
- facts and interpretations are separated;
- weak evidence was not strengthened;
- source freshness was respected;
- valuation conclusions have as-of dates where relevant;
- missing data is disclosed;
- Decision Confidence reflects evidence quality;
- no exact position sizing appears;
- no internal agent references appear in the main memo;
- no overconfident language appears.

This check is silent and should not be displayed as a checklist in the final memo.

## Step 10 — Structured Output Metadata

The skill should produce structured output metadata for workflow handoff.

Example:

```yaml
ic_output_metadata:
  memo_status:
  action_internal_category:
  for_a_new_position:
  for_existing_holders:
  decision_confidence:
  primary_reason:
  key_assumptions:
  key_risks:
  reassessment_trigger:
  required_follow_ups:
  evidence_quality:
  output_path:
```

This metadata may later become a separate file, but initially it can be a structured handoff.

## Follow-Up Requests

If the memo is Limited or Blocked, include structured follow-up requests.

Example:

```yaml
follow_up_request:
  to:
  reason:
  needed:
  priority:
  required_for:
```

The request should be specific enough for the next agent to act.

Bad:

```text
Need more data.
```

Better:

```text
Need refreshed valuation inputs, including current market price, consensus revenue / EPS estimates, peer multiples, historical multiple range, and reverse-implied growth sensitivity.
```

## Prohibited Behaviors

The skill prohibits:

- direct-call final opinions without required inputs;
- new research by default;
- exact position sizing;
- robotic agent-by-agent summaries;
- unsupported facts;
- overconfident claims;
- hiding material caveats in appendix only;
- turning weak evidence into strong claims;
- generic action labels without practical meaning;
- final action without Decision Confidence explanation.

## Output Status Handling

### Complete

Use when required inputs are sufficient.

Do not over-emphasize “Complete” in the main memo.

### Limited

Use when a conclusion is possible but evidence limitations matter.

Include natural Evidence Caveat when material.

### Blocked

Use when responsible investment judgment is impossible.

Must include:

- practical meaning;
- why blocked;
- missing evidence;
- required follow-up steps.

## Language

The skill produces Markdown deliverables in English by default.

Chat discussion with the user may be in Russian.

## Relationship to Global Standards

This skill must follow:

- global investment analytical writing style;
- human-readable investment report standard;
- reader layer / verification layer model;
- material claim support rule;
- Decision Confidence standard;
- Action Label Practical Meaning standard;
- source quality and anti-hallucination standard;
- no exact position sizing rule.
