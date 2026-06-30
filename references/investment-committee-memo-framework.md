# Investment Committee Memo Framework

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: Investment Committee  
Contributors: Evidence Collector; asset-class agents; specialist agents  
Used by: Investment Committee; investment-committee-synthesis skill  
Primary reference for: IC memo wording examples and decision-support presentation references  
Supporting reference for: report-writing examples only; canonical report schemas govern final outputs  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: Medium  
Last reviewed: 2026-06-28  
Review trigger: Review when IC report schemas, Action Box rules, or decision-label rules change.  
Owner review needed: No  
Split/index status: Indexed in implementation/reference-library-index.md  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->


## Purpose

This framework defines the default structure and section-level requirements for the final Investment Committee memo.

Primary artifact:

```text
final_investment_memo.md
```

The framework is designed for the Standard Company / Asset-first IC Memo.

It should be adapted later for sector, theme, ETF, commodity, crypto, and fixed income memo profiles.

## Core Standard

The final memo should be a professional investment committee memo, not an agent log.

It should help the reader understand:

- what the asset is;
- why it matters now;
- what the core investment debate is;
- what the thesis depends on;
- what is priced in;
- what could go right;
- what could go wrong;
- what action is appropriate;
- what would change the view.

The memo should be concise enough to read in one sitting, but substantive enough to immerse the reader in the investment case.

Default target:

```text
1,500–3,000 words
5–10 minute read
```

## Default Section Order

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

The section order is the default. The agent may lightly adapt it when the request type requires it, but should preserve the decision-first logic.

## 1. Investment View

### Purpose

Give the reader the main investment view immediately.

### Should Answer

- What is the final view?
- Is the asset attractive, unattractive, or conditionally attractive?
- What is the main trade-off?
- What matters most for the decision?

### Style

Use 1–3 strong paragraphs.

Avoid:

- generic summary;
- agent-by-agent recap;
- unsupported certainty;
- overly short “buy/sell” statement.

### Example Style

```text
The asset remains fundamentally attractive, but the current setup is not compelling enough for a new position. Business quality and long-term demand remain strong, yet valuation already reflects a demanding growth scenario. The decision therefore depends less on whether the company is high quality and more on whether future results can exceed what the market already expects.
```

## 2. Action Box

### Purpose

Translate the memo into a practical decision.

### Required Fields

```text
For a New Position:
For Existing Holders:
Practical Meaning:
Primary Reason:
Decision Confidence:
Time Horizon:
Portfolio Role:
Reassessment Trigger:
Evidence Caveat: [only when material]
Market Data As Of: [when valuation / price-sensitive]
```

### Field Guidance

#### For a New Position

Use natural labels:

- Initiate Position;
- Build Gradually;
- Do Not Initiate Yet;
- Avoid;
- No Decision — More Work Required.

#### For Existing Holders

Use natural labels:

- Add to Existing Position;
- Maintain / Hold;
- Reduce Exposure;
- Exit Position;
- No Decision — More Work Required.

#### Practical Meaning

Must explain what the action means in plain language.

Bad:

```text
Action: Do Not Initiate Yet.
```

Better:

```text
Practical Meaning: Do not open a new position at the current setup. Keep the asset under review and reassess if valuation improves or evidence strengthens that the market is underestimating durable growth.
```

#### Decision Confidence

Must include the level and why.

```text
Decision Confidence: Moderate — the business evidence is strong, but valuation and incomplete positioning data limit confidence in the timing.
```

#### Portfolio Role

Keep light and qualitative.

Allowed:

- core candidate;
- satellite growth exposure;
- tactical exposure;
- hedge;
- diversifier;
- watchlist candidate;
- avoid-for-portfolio / not suitable for stated portfolio role;
- no clear portfolio role.

No exact sizing.

#### Evidence Caveat

Use only when material.

Example:

```text
Evidence Caveat: The conclusion is usable, but timing confidence is lower because market positioning data is incomplete.
```

## 3. Why This Action, Not the Alternatives

### Purpose

Explain why the selected action is better than more bullish or more bearish alternatives.

### Should Answer

- Why this action?
- Why not initiate / add more aggressively?
- Why not avoid / reduce?
- What would change the view?

### Example Structure

```text
The asset is not an outright Avoid because the business quality and long-term demand picture remain attractive. It is not an Initiate Position because valuation already embeds strong execution assumptions and leaves limited room for disappointment. The appropriate action is therefore Do Not Initiate Yet for a new position, while existing holders can Maintain / Hold if the thesis remains intact.
```

## 4. What Matters Most

### Purpose

Identify the 2–4 factors that truly drive the decision.

### Format

Short numbered list.

### Example

```text
1. Whether demand remains durable beyond the current cycle.
2. Whether margins normalize modestly or structurally compress.
3. Whether valuation already captures most of the upside.
4. Whether near-term catalysts can improve the risk/reward.
```

## 5. Investment Scorecard

### Purpose

Give a quick qualitative map of the investment picture.

### Rules

- Qualitative only by default.
- No numeric 8/10 scoring unless a separate framework explicitly requires it.
- Do not let the scorecard replace narrative reasoning.

### Default Company / Asset Scorecard

```text
Business Quality:
Competitive Position:
Financial Trajectory:
Valuation / Expectations:
Risk Profile:
Macro Backdrop:
Catalysts:
Market Positioning:
Overall Risk/Reward:
```

### Example

```text
Business Quality: Strong
Competitive Position: Durable but under pressure from customer concentration and competition
Financial Trajectory: Strong, but expectations are high
Valuation / Expectations: Demanding
Risk Profile: Manageable but asymmetric
Macro Backdrop: Mixed
Catalysts: Moderate
Market Positioning: Possible / probable crowding; not a standalone action signal
Overall Risk/Reward: Attractive business, imperfect entry
```

## 6. Situation Overview

### Purpose

Help the reader enter the topic quickly.

### Should Include

- what the asset / company is;
- why it matters;
- why the question is relevant now;
- the current market context;
- the main investor debate.

### Length

Usually 1–3 paragraphs.

### Avoid

- Wikipedia-style company description;
- irrelevant history;
- generic business summary.

## 7. The Core Debate

### Purpose

Explain the real investment argument.

### Should Include

- bullish case;
- bearish case;
- what the market appears to be debating;
- what the final decision depends on.

### Example

```text
The bullish case is that the company remains a scarce supplier to a durable structural growth market and can sustain earnings power longer than consensus expects. The bearish case is not that the company is weak, but that the current price already discounts years of strong execution while competitive, margin, and demand-cycle risks leave limited room for disappointment.
```

## 8. Core Thesis

### Purpose

State the central investment thesis clearly.

### Should Include

- 3–5 thesis pillars;
- the economic logic of the idea;
- what must happen for the thesis to work;
- whether the thesis is long-term, tactical, cyclical, defensive, or event-driven.

### Example Structure

```text
The thesis rests on three pillars:
1. [Pillar]
2. [Pillar]
3. [Pillar]
```

## 9. Key Assumptions

### Purpose

Make the decision logic honest by showing what must be true.

### Should Include

- demand assumption;
- margin / profitability assumption;
- valuation / expectations assumption;
- risk assumption;
- macro / catalyst assumption where material.

### Example

```text
The decision depends on three assumptions:
1. Demand remains durable enough to support earnings above current expectations.
2. Margins normalize only modestly rather than structurally compressing.
3. The current valuation can still be supported by upward revisions or a better entry point.
```

## 10. Integrated Evidence Synthesis

### Purpose

Synthesize specialist findings naturally.

This section should not be agent-by-agent.

### Possible Subsections

Use only relevant subsections.

```text
Business Quality and Competitive Position
Financial Trajectory
Valuation and Expectations
Macro Sensitivity
Market Positioning
News and Catalysts
Risk Profile
Portfolio Role
```

### Rules

- Integrate evidence into a coherent investment narrative.
- Preserve nuance and uncertainty.
- Do not repeat every detail from specialist reports.
- Do not hide material caveats.
- Use source context minimally in the main memo.

### Bad Style

```text
The Equity Agent said the business is good. The Valuation Agent said valuation is expensive. The Risk Agent found three risks.
```

### Better Style

```text
Business quality is the strongest part of the case, but valuation is the main constraint. The company appears well positioned competitively, yet the current price already assumes durable execution and limits the margin of safety.
```

## 11. What Is Priced In

### Purpose

Explain what expectations the current price appears to reflect.

### Should Include

- valuation context;
- market expectations;
- implied growth or profitability assumptions;
- whether expectations are demanding or conservative;
- what scenario is needed for upside.

### Rules

- Required when valuation / expectations are relevant.
- Must use valuation work; do not invent implied expectations.
- Include as-of date where relevant.

### Example

```text
The current valuation appears to assume continued strong growth, resilient margins, and limited execution slippage. The asset does not require perfection, but it does require continued evidence that earnings power can exceed already elevated expectations.
```

## 12. Where the Market May Be Wrong

### Purpose

Identify possible sources of mispricing or misunderstanding.

### Should Be Two-Sided

Include where relevant:

- bullish market error;
- bearish market error;
- which error matters more for the action.

### Edge Handling

If there is a clear edge, explain where it comes from.

If there is no clear edge, say so directly.

Example:

```text
The memo does not identify a clear informational or analytical edge. The company may still be high quality, but the case for a new position depends more on future execution than on an obvious current mispricing.
```

## 13. Bull / Base / Bear Cases

### Purpose

Frame the decision under different plausible outcomes.

### Rules

- Required for Standard IC Memo.
- No probabilities by default.
- Use probabilities only if supported by explicit model, user request, or strong evidence.
- Keep scenarios decision-relevant.

### Scenario Template

```text
Bull Case
What must be true:
Key drivers:
Investment implication:
What would make this more likely:

Base Case
What must be true:
Key drivers:
Investment implication:
What would make this more likely:

Bear Case
What must be true:
Key drivers:
Investment implication:
What would make this more likely:
```

## 14. Risks and Thesis Breakers

### Purpose

Identify what can go wrong and what would actually break the thesis.

### Rules

- Focus on 3–5 major risks.
- No laundry list.
- Separate risk from thesis breaker.
- Preserve severity and uncertainty.

### Risk Card Template

```text
Risk:
Why it matters:
Thesis breaker condition:
```

### Example

```text
Risk: Margin durability risk.
Why it matters: The valuation depends on sustained profitability, so structural margin pressure would reduce earnings power and multiple support.
Thesis breaker condition: The thesis weakens materially if margin compression proves structural rather than temporary.
```

## 15. Catalysts and Monitoring Plan

### Purpose

Translate the memo into an ongoing monitoring plan.

### Required Blocks

```text
Near-term catalysts:
Confirmation signals:
Warning signals:
Invalidation triggers:
```

### Guidance

#### Near-Term Catalysts

Events that could change market perception or evidence quality.

Examples:

- earnings;
- guidance;
- product launch;
- regulatory decision;
- macro data;
- investor day;
- M&A event.

#### Confirmation Signals

What supports the thesis.

#### Warning Signals

What weakens the thesis.

#### Invalidation Triggers

What breaks the thesis.

## 16. Next Steps

### Purpose

Explain what to do after reading the memo.

### Should Be Short

Examples:

```text
1. Do not initiate at the current setup; keep the asset under review.
2. Reassess after the next earnings report and updated guidance.
3. Refresh valuation and positioning data before upgrading the action.
```

For Blocked memos, Next Steps should list required workflow steps.

## 17. Evidence & Data Quality Appendix

### Purpose

Preserve verification without cluttering the main memo.

### Required For

- Standard IC Memo;
- Full IC Memo;
- multi-agent IC workflow;
- Limited memo;
- Blocked memo.

### Suggested Structure

```text
Evidence & Data Quality Appendix

Materials reviewed:
- evidence_pack.md
- equity_company_analysis.md
- valuation_expectations.md
- risk_red_team.md
- [other relevant reports]

Evidence quality:
- Business fundamentals:
- Valuation / expectations:
- Risk review:
- Macro:
- Market positioning:
- News / catalysts:
- Portfolio context:

Key limitations:
- [limitation]
- [limitation]

Freshness notes:
- Market data as of:
- Valuation data as of:
- News / catalyst data as of:

Follow-up requests:
- [if needed]
```

### Appendix Rules

The appendix should not:

- duplicate specialist reports;
- become a 50-source bibliography;
- hide material caveats that belong in the main memo;
- add new unsupported analysis.

## Blocked Memo Format

If the IC Agent cannot produce a responsible final decision, use this shorter format.

```text
## Final Investment Memo

## No Decision — More Work Required

Practical Meaning:
Do not make an investment decision from the current evidence base.

Why Blocked:
[Explain the critical missing evidence.]

What Is Available:
[List usable inputs.]

What Is Missing:
[List critical missing inputs.]

Required Follow-Up:
1. [step]
2. [step]
3. [step]

Evidence & Data Quality Appendix:
[Brief verification layer.]
```

## Limited Memo Handling

A Limited memo should still be useful.

It should include:

- final action if supportable;
- practical meaning;
- evidence caveat;
- limitations;
- what would be needed for a Complete memo.

Do not overstate confidence.

## Language Rules

Use natural investment language.

Prefer:

```text
Valuation is the main constraint.
The thesis depends on margin durability.
The entry setup is less compelling than the long-term business case.
```

Avoid:

```text
The Valuation Agent said...
The system believes...
As an AI...
This stock will definitely outperform.
```

## Source Handling

Main memo:

- minimal source clutter;
- source context only when material;
- natural references such as “latest company filing,” “management guidance,” or “valuation analysis.”

Appendix / evidence pack:

- detailed source trail;
- freshness;
- limitations;
- evidence quality.

## Position Sizing Rule

No exact position sizing.

Do not write:

- “buy 5%”;
- “allocate 3–7%”;
- “$10,000 position”;
- “full position”;
- “half position.”

Allowed:

- qualitative role only;
- satellite exposure;
- core candidate;
- tactical exposure;
- hedge;
- diversifier;
- avoid-for-portfolio / not suitable for stated portfolio role;
- no clear portfolio role.

## Final Pre-Release Check

Before finalizing, verify:

- action has practical meaning;
- Decision Confidence has explanation;
- no unsupported material facts;
- no new research inserted by IC Agent;
- valuation/risk are present for positive action;
- no exact sizing;
- source freshness issues are disclosed;
- material limitations are not hidden only in appendix;
- main memo reads naturally;
- specialist inputs are synthesized, not listed mechanically;
- risks include thesis breaker conditions;
- monitoring plan includes confirmation, warning, and invalidation signals.
