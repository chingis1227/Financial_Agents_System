# Equity Deep Dive Workflow

## 1. Purpose

This document defines the full investment-oriented workflow for analyzing a single public equity.

It is separate from the Equity Agent.

```text
Equity Agent = company-quality analysis.
Equity Deep Dive Workflow = full investment-oriented process from evidence collection to final investment memo.
```

The workflow answers:

```text
Is this a good business, is the current price attractive, is now a good time to enter, what can break the thesis, and what is the final investment conclusion?
```

## 2. Scope

The workflow covers single-company public equity deep dives.

In scope:

- public listed equities;
- global companies;
- US-first source depth;
- ADRs when underlying issuer data is available;
- standard investment-oriented analysis.

Out of scope for this workflow:

- private companies;
- startups;
- VC-style analysis;
- multi-company comparison workflow;
- portfolio construction;
- position sizing;
- technical trading systems.

Company comparison workflows are outside this workflow's current scope and require a separate workflow if needed.

## 3. Default Mode

The workflow has one default mode:

```text
Standard Investment-Oriented Equity Deep Dive
```

There are no quick / standard / deep variants in the target design.

The workflow should apply Pareto discipline: deep on the variables that matter, concise on secondary issues.

## 4. Core Decision Framework

The workflow is organized around five questions.

### 4.1 Is this a good business?

Primary owners:

- Equity Agent;
- Financial Statement Analysis Skill;
- Sector & Industry Analysis Agent.

Required outputs:

- `equity_company_analysis.md`
- `financial_statement_analysis.md`
- `sector_context.md`

### 4.2 Is the current price attractive?

Primary owner:

- Valuation & Expectations Agent.

Required output:

- `valuation_expectations.md`

### 4.3 Is now a good time to enter?

Primary owners:

- Market Positioning Agent;
- News & Catalysts Agent;
- Macro Agent.

Required outputs:

- `market_positioning.md`
- `news_catalysts.md`
- `macro_sensitivity.md`

### 4.4 What can break the thesis?

Primary owner:

- Risk / Red Team Agent.

Required output:

- `risk_red_team.md`

### 4.5 What is the final decision?

Primary owner:

- Investment Committee Agent.

Required output:

- `final_investment_memo.md`

## 5. Required Reports

A complete workflow should produce:

```text
evidence_pack.md
financial_statement_analysis.md
sector_context.md
equity_company_analysis.md
valuation_expectations.md
market_positioning.md
news_catalysts.md
macro_sensitivity.md
risk_red_team.md
final_investment_memo.md
```

## 6. Output Folder Structure

Recommended folder structure:

```text
equity_deep_dive_[ticker]/
  evidence_pack.md
  financial_statement_analysis.md
  sector_context.md
  equity_company_analysis.md
  valuation_expectations.md
  market_positioning.md
  news_catalysts.md
  macro_sensitivity.md
  risk_red_team.md
  final_investment_memo.md
```

For non-US tickers, the folder name should use a clear ticker or company identifier.

## 7. Workflow Sequence

The workflow is partially parallel, not strictly linear.

### Step 0 — Intake and Routing

The workflow starts only after the request has been classified by:

```text
master-intake-router-prd.md
asset-intake-router-prd.md
```

For generic public-equity requests such as:

```text
Analyze Nvidia.
```

the Asset Intake Router should treat the request as a full asset-first equity workflow unless the user explicitly scopes it to a narrower task such as valuation, risk, market reaction, or financial statement analysis.

The router should ask up to three relevant context questions when useful, but it should not block the workflow with a full questionnaire if the route is already clear.

Expected intake artifact:

```text
intake.md
```

or an equivalent structured intake block containing the original request, selected route, asset, user intent, horizon if known, current exposure if known, thesis / concern if known, missing context, freshness requirement, and planned modules.

### Step 1 — Evidence Collection

The Evidence Collector Agent creates:

```text
evidence_pack.md
```

The evidence pack should follow `evidence-pack-framework.md` and function as a claim-support evidence artifact, not a source dump.

For a complete equity deep dive, the evidence pack should include:

- instrument identity and user intake context;
- primary company filings and investor materials;
- latest results and earnings materials;
- financial and segment evidence;
- current market data with as-of date;
- relevant sector / industry evidence;
- material recent news check;
- valuation-relevant inputs where available;
- risk-relevant evidence gaps;
- missing, stale, proxied, contradictory, or inaccessible data;
- downstream readiness matrix for Equity, Valuation, Risk, Market Positioning, News / Catalysts, Macro, and Investment Committee.

The Evidence Collector should distinguish Analytical Evidence Sufficiency from Decision Evidence Sufficiency. Specialist work may proceed when analytical evidence is sufficient, but a complete final IC decision requires decision-grade evidence and a pre-IC evidence lock.

### Step 2 — Parallel Specialist Work

After the base evidence pack is available, the following can run in parallel:

```text
Financial Statement Analysis
Sector & Industry Analysis
News & Catalysts
Market Positioning
Macro Sensitivity
```

News & Catalysts should use the dedicated package:

```text
news-catalysts-agent-prd.md
news-catalysts-method-skill-prd.md
news-catalysts-framework.md
```

It should produce a memo-first `news_catalysts.md` with recent events, active carryover events, upcoming catalyst map, negative news check, source / date confidence, event-risk flags, and structured handoffs. The output status should be Complete, Limited, Blocked, or Preliminary Catalyst Scan depending on scope and source quality.

Macro Sensitivity should use the dedicated Macro package:

```text
macro-agent-prd.md
macro-analysis-method-skill-prd.md
macro-sensitivity-framework.md
macro-regime-framework.md
macro-indicator-cadence-source-registry.md
macro-block-playbooks.md
macro-g3-fx-regional-policy-overlay.md
macro-expectations-surprise-framework.md
```

It should produce `macro_sensitivity.md`, not a full macro essay. In an equity deep dive, Macro Agent should identify only material macro drivers for the company or thesis, such as real yields, Fed path, growth cycle, consumer income, credit spreads, liquidity, USD / FX translation, commodity inputs, or G3 regional policy exposure where relevant.

Fresh market data are mandatory when the macro conclusion depends on current rates, FX, DXY, oil, gold, credit spreads, volatility, or market-implied policy expectations. Slow official releases may be carried forward only with timestamps. If material macro data are stale or missing, Macro Sensitivity should be Limited or Blocked for the affected conclusion rather than filled with generic commentary.

Expected outputs:

```text
financial_statement_analysis.md
sector_context.md
news_catalysts.md
market_positioning.md
macro_sensitivity.md
```

### Step 3 — Equity Company Analysis

The Equity Agent writes:

```text
equity_company_analysis.md
```

Direct inputs:

```text
evidence_pack.md
financial_statement_analysis.md
sector_context.md
material news/catalyst notes, if available
```

The Equity Agent owns the company-quality answer, not the final investment decision.

### Step 4 — Valuation & Expectations

The Valuation & Expectations Agent writes:

```text
valuation_expectations.md
```

This report should address:

```text
What is already priced in, and are those expectations reasonable?
```

It should use an expectations-adjusted value doctrine and follow the dedicated Valuation & Expectations package:

```text
valuation-expectations-agent-prd.md
valuation-expectations-method-skill-prd.md
valuation-expectations-framework.md
```

The report should include:

- current valuation snapshot;
- absolute and quality-adjusted valuation;
- primary valuation method and supporting methods;
- sector-specific metric selection;
- market-implied expectations;
- scenario-implied valuation ranges, not a single-point target price;
- return bridge;
- margin of safety as an Investment Committee input;
- valuation asymmetry;
- valuation risk flags;
- misleading metric flags;
- value trap, quality trap, and growth trap diagnostics;
- monitoring signals tied to implied expectations;
- structured handoff to Risk / Red Team and Investment Committee.

The report must classify its status as:

```text
Complete Valuation
Limited Valuation
Blocked Valuation
```

The Valuation & Expectations Agent should use financial analysis, market data, consensus expectations as a benchmark, management guidance, estimate revisions, historical valuation, peer valuation with comparability scoring, and reverse-expectations logic where available.

The agent must follow source hierarchy, timestamp discipline, and anti-hallucination rules. Unsupported valuation numbers must not be invented.

### Step 5 — Risk / Red Team

The Risk / Red Team Agent should run after Equity Company Analysis and Valuation & Expectations are available.

Reason:

```text
Risk / Red Team should challenge the specific investment thesis and embedded expectations, not produce a generic risk list.
```

Expected output:

```text
risk_red_team.md
```

The report should follow the dedicated Risk / Red Team package:

```text
risk-red-team-agent-prd.md
risk-red-team-method-skill-prd.md
risk-red-team-framework.md
```

The report should include:

- short Risk Executive Summary;
- core thesis under attack;
- critical assumptions map;
- 3-7 material failure paths, with top-3 depth;
- explicit transmission mechanism and valuation link for major failure paths;
- bear case challenge / valuation downside integrity check;
- accounting / governance red flag gate;
- balance sheet / liquidity fragility gate;
- market expectations / positioning gate;
- risk watchlist for potentially material but immature risks;
- thesis-relevant tail risks;
- excluded / deprioritized risk rationale;
- priority challenge requests;
- structured handoff to Investment Committee.

The report must classify its status as:

```text
Complete Risk Review
Limited Risk Review
Blocked Risk Review
Preliminary Risk Scan
```

If valuation is not ready, Risk / Red Team may begin a preliminary business-risk scan, but it cannot produce a Complete Risk Review because it cannot assess priced-in expectations or bear-case severity.

The agent must not issue buy/sell/hold recommendations, target prices, position sizing, or hidden investment actions. It may issue a risk challenge verdict and analytical challenge requests.

### Step 6 — Investment Committee Synthesis

The Investment Committee Agent writes:

```text
final_investment_memo.md
```

It uses:

```text
investment-committee-agent-prd.md
investment-committee-synthesis-method-skill-prd.md
investment-committee-memo-framework.md
```

The Investment Committee Agent is downstream-only. It should run after the required evidence and specialist reports are available and after the Evidence Collector has completed a pre-IC evidence lock / freshness check.

For a Complete equity final memo, required inputs normally include:

- intake context;
- `evidence_pack.md`;
- `equity_company_analysis.md`;
- `valuation_expectations.md`;
- `risk_red_team.md`;
- relevant context reports where material, such as macro, news / catalysts, market positioning, sector context, and portfolio fit.

Positive actions such as Initiate Position, Add to Existing Position, or Build Gradually require sufficient valuation / expectations work, Risk / Red Team review, and decision evidence sufficiency confirmed by the Evidence Collector.

The final memo should synthesize all specialist work into a natural professional investment memo. It should not mention internal agents by name in the main conclusion and should not become an agent-by-agent recap.

The default Standard IC Memo includes:

- Investment View;
- Action Box;
- Why This Action, Not the Alternatives;
- What Matters Most;
- Investment Scorecard;
- Situation Overview;
- The Core Debate;
- Core Thesis;
- Key Assumptions;
- Integrated Evidence Synthesis;
- What Is Priced In;
- Where the Market May Be Wrong;
- Bull / Base / Bear Cases;
- Risks and Thesis Breakers;
- Catalysts and Monitoring Plan;
- Next Steps;
- Evidence & Data Quality Appendix.

The Action Box should use natural labels such as:

```text
For a New Position: Do Not Initiate Yet
For Existing Holders: Maintain / Hold
```

Every action must include practical meaning, Decision Confidence with explanation, time horizon, light qualitative portfolio role, and reassessment trigger.

The final memo must not include exact position sizing.

If required inputs are missing, the Investment Committee Agent should produce a Blocked or Limited memo with structured follow-up requests rather than improvising a final opinion.
## 8. Completion Rules

### 8.1 Mandatory Decision Gates

A complete final investment memo cannot be produced without these mandatory decision-gate reports:

```text
valuation_expectations.md
risk_red_team.md
```

Without either of these, the Investment Committee Agent must not issue a positive action. The final memo must be marked:

```text
Status: incomplete / blocked for final decision
```

A preliminary synthesis may be produced, but not a complete final investment decision.

Before IC synthesis, the Evidence Collector should perform a pre-IC evidence lock. If the lock status is `Refresh Required` or `Blocked`, the IC Agent must not produce a Complete Final Memo. If IC readiness is Limited, the IC Agent may produce only a Limited Final Memo unless the limitation is resolved or is clearly not decision-critical.

### 8.2 Context Limitations

The following reports are required for the full investment-oriented workflow but are not always mandatory decision gates for a business-plus-valuation conclusion:

```text
market_positioning.md
news_catalysts.md
macro_sensitivity.md
```

If any are missing, the final memo must clearly state:

```text
Limited timing / market context.
```

Market Positioning becomes a conditional decision-relevant gate when expectations, crowding, positioning, event reaction, or narrative saturation are material to the investment case. Examples include “is this priced in?”, “is this crowded?”, post-earnings reaction analysis, high-multiple narrative stocks, short-squeeze risk, crowded themes, or timing-sensitive entry questions.

In those cases, missing or blocked `market_positioning.md` may require a Limited Final Memo or block the specific conclusion that depends on positioning evidence. Missing optional positioning channels should not block the whole workflow unless they are material to the conclusion being made.

News & Catalysts becomes a conditional decision-relevant gate when recent events, upcoming catalysts, event risk, catalyst failure, or freshness materially affect the investment case. Examples include earnings or guidance windows, regulatory decisions, M&A, litigation, major product or customer events, management changes, index / capital-markets events, and material peer read-throughs.

In those cases, missing, stale, or blocked `news_catalysts.md` may require a Limited Final Memo or block a positive IC action until the material news / catalyst freshness issue is resolved. A bounded negative-news check is sufficient only when its source window, source types, and limitations are clearly stated.

## 9. Ownership Map

| Question | Primary Owner | Output |
|---|---|---|
| What do we know and what is missing? | Evidence Collector Agent | `evidence_pack.md`, readiness matrix, pre-IC evidence lock |
| Is this a good business? | Equity Agent | `equity_company_analysis.md` |
| Do the financials support the story? | Financial Statement Analysis Skill | `financial_statement_analysis.md` |
| Is the company in an attractive industry position? | Sector & Industry Analysis Agent | `sector_context.md` |
| Is the current price attractive? | Valuation & Expectations Agent | `valuation_expectations.md` |
| What does the market already believe? | Market Positioning Agent | `market_positioning.md` |
| What recent or upcoming events matter? | News & Catalysts Agent | `news_catalysts.md` |
| Which macro variables matter? | Macro Agent | `macro_sensitivity.md` |
| What can break the thesis? | Risk / Red Team Agent | `risk_red_team.md` |
| What is the final conclusion? | Investment Committee Agent | `final_investment_memo.md` |

## 10. Relationship to Equity Agent

The Equity Agent does not own the full workflow.

It owns only:

```text
equity_company_analysis.md
```

Its output should answer:

```text
Is this a good business?
```

The workflow as a whole answers:

```text
Is this an attractive investment now?
```

## 11. Relationship to Original Company Deep-Dive Prompt

The original company deep-dive prompt is implemented as a workflow rather than a single-agent task.

| Original Prompt Area | Workflow Owner |
|---|---|
| Business model | Equity Agent |
| Financial statement analysis | Financial Statement Analysis Skill |
| Valuation / embedded expectations | Valuation & Expectations Agent |
| Consensus and sentiment | Market Positioning Agent |
| Market narrative | Market Positioning / Market Sense |
| Scenario analysis | Investment Committee Agent |
| Sector analysis | Sector & Industry Analysis Agent |
| Competitive analysis | Equity Agent |
| Macro sensitivity | Macro Agent |
| Non-obvious risks | Risk / Red Team Agent |
| Historical stock behavior | Market Positioning for expectation / reaction evidence; optional deferred technical / price-action input for trading signals |
| Recent news | News & Catalysts Agent |
| Three key questions | Workflow-level framework |
| Investment thesis | Investment Committee Agent |
| Sources | Evidence Collector Agent + all specialist agents |

## 12. Report Style Rule

All reports in the workflow should follow the clean main report / appendix structure:

```text
Main report:
Decision-useful analysis, concise conclusions, key drivers, and implications.

Appendix:
Confidence, evidence limits, missing data, source notes, and technical checks.
```

Critical caveats that change the conclusion must remain in the main report.

Technical caveats should go to the appendix.

This rule should later be promoted to the global report style policy for all agents.

## 13. Guardrails

The workflow must not:

- allow the Equity Agent to make the final investment decision;
- allow Investment Committee to produce a complete final memo without valuation and risk work;
- confuse business quality with stock attractiveness;
- treat market sentiment as proof of fundamentals;
- treat valuation multiples as sufficient embedded-expectations analysis;
- allow the Valuation & Expectations Agent to issue a final target price or buy/sell/hold recommendation;
- produce a long report without clear decision relevance;
- bury the main thesis breaker in a generic risk list;
- skip source limitations when evidence is incomplete.

## 14. Current Design Decisions Captured

1. Equity Deep Dive Workflow is separate from Equity Agent.
2. The workflow covers single-company public equity analysis only.
3. Comparison workflows are deferred.
4. The workflow has one default mode: Standard Investment-Oriented Equity Deep Dive.
5. The workflow is partially parallel after evidence collection.
6. Risk / Red Team should run after Equity Company Analysis and Valuation & Expectations.
7. Investment Committee runs after mandatory reports are available and after pre-IC evidence lock / freshness check.
8. Valuation and Risk are mandatory decision gates for a complete final decision memo and for any positive action; they are not automatic specialist vetoes over IC judgment.
9. Missing Market Positioning, News, or Macro creates timing / market-context limitations.
10. The workflow uses a clear output folder structure.
11. Evidence Collector is now defined by `evidence-collector-agent-prd.md`, `evidence-collection-method-skill-prd.md`, `evidence-pack-framework.md`, `source-registry-framework.md`, and `evidence-request-protocol.md`.
12. Valuation & Expectations is now defined by `valuation-expectations-agent-prd.md`, `valuation-expectations-method-skill-prd.md`, and `valuation-expectations-framework.md`.
13. Risk / Red Team is now defined by `risk-red-team-agent-prd.md`, `risk-red-team-method-skill-prd.md`, and `risk-red-team-framework.md`.
14. Market Positioning is now defined by `market-positioning-agent-prd.md`, `market-positioning-method-skill-prd.md`, and `market-positioning-framework.md`.
15. Technical / price-action analysis is intentionally deferred outside the core workflow; if used later, it must remain a lightweight input and cannot override valuation, evidence, or Investment Committee ownership.
