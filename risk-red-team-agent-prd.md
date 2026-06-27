# Risk / Red Team Agent PRD

## Purpose

The Risk / Red Team Agent is a thesis-breaker module for public listed equity analysis.

It does not produce a generic list of risks. Its purpose is to challenge the combined investment thesis after business-quality and valuation work have been completed.

The agent asks:

> How can this investment thesis fail?

The agent focuses on material, economically plausible, thesis-relevant failure modes. It must not break the thesis mechanically or include every negative possibility.

## Core Question

```text
How can this investment thesis fail, and what evidence would show that it is failing?
```

## Role in the System

The Risk / Red Team Agent runs after Equity Company Analysis and Valuation & Expectations.

```text
Financial Statement Analysis:
What are the financial realities?

Equity Agent:
Is this a good business?

Valuation & Expectations Agent:
What is already priced in?

Risk / Red Team Agent:
How can the thesis fail?

Investment Committee Agent:
Should this become an investment decision?
```

The agent may receive early escalation from upstream work if critical red flags are found, including accounting issues, governance concerns, liquidity stress, regulatory overhangs, or broken business economics.

## Primary Output

```text
risk_red_team.md
```

## Ownership

The agent owns:

- thesis failure map;
- critical assumption challenge;
- material failure path analysis;
- downside scenario integrity check;
- bear case challenge;
- risk challenge verdict;
- thesis invalidation triggers;
- early warning indicators;
- accounting and governance red flag gate;
- balance sheet and liquidity fragility gate;
- market expectations and positioning risk gate;
- permanent capital impairment risk assessment;
- tail risk identification when thesis-relevant;
- risk watchlist;
- excluded / deprioritized risk rationale;
- structured challenge requests to upstream agents and Investment Committee.

## Non-Ownership

The agent does not own:

- final buy / sell / hold recommendation;
- target price;
- position sizing;
- portfolio construction;
- full valuation model;
- full macro thesis;
- full legal adjudication;
- final Investment Committee synthesis;
- generic risk taxonomy without thesis relevance.

## Core Design Principles

### 1. Thesis-breaker, not risk-list generator

The agent must challenge the specific investment thesis. It should not produce a generic risk inventory.

Every major risk must answer:

```text
What assumption breaks?
How does it break?
Where does it hit the economics?
Why does the market care?
What evidence would confirm or disconfirm it?
```

### 2. Anti-overbreaking discipline

The agent must not become a forced-bear-case generator.

A failure path is valid only if it is:

- material;
- economically plausible;
- logically connected to the thesis;
- tied to thesis-critical assumptions or priced-in expectations;
- supported by a clear transmission mechanism;
- capable of being monitored, confirmed, or disconfirmed.

The agent should not write "if everything goes wrong, the thesis fails." It should identify realistic ways the thesis can fail.

### 3. Materiality-first

A risk enters the main report only if it passes at least one of the following tests:

```text
Price-in test:
The risk relates to expectations already embedded in valuation.

Thesis-critical test:
If the assumption fails, the core thesis no longer works.

Downside-asymmetry test:
Probability may be moderate, but downside damage is disproportionate.

Early-evidence test:
There are early signs in financials, competition, customer behavior, pricing, governance, accounting, regulation, or market expectations.
```

Low-relevance, generic, low-impact, or unconnected risks should be excluded, deprioritized, or placed on a watchlist.

### 4. Risk maturity test

A risk is mature enough for the main failure map only if it has:

```text
1. clear assumption link;
2. clear transmission mechanism;
3. current evidence or explicit evidence gap;
4. confirmation / disconfirmation trigger;
5. thesis damage assessment.
```

If the risk does not pass this test, it should not appear as a top failure path.

### 5. Plausible failure paths first; tail risks separately

The main report should focus on 3-7 material and plausible failure paths, with emphasis on the top 3.

Tail risks should be included separately only when they are thesis-relevant or could create permanent capital impairment.

### 6. Risk cards, not default tables

Failure paths should be written as compact risk cards or short analytical sections.

Tables are optional and should be used only when they improve clarity, such as for compact assumption maps, gate summaries, or appendix evidence notes.

### 7. Top-3 depth rule

The top 3 failure paths should receive full treatment:

- assumption link;
- why it matters;
- transmission mechanism;
- evidence today;
- counter-evidence;
- valuation link;
- invalidation trigger;
- early warning indicators;
- impairment type.

Additional failure paths may be shorter if they are material but less decision-critical.

### 8. Transmission mechanism required

No risk is decision-useful unless the agent explains the transmission mechanism.

Examples:

- revenue growth;
- pricing power;
- gross margin;
- operating leverage;
- FCF conversion;
- working capital;
- capital intensity;
- ROIC / WACC spread;
- leverage and refinancing;
- valuation multiple;
- investor confidence;
- governance discount;
- regulatory liability;
- thesis credibility.

### 9. Valuation link required

Each major failure path must explain how it connects to valuation or market expectations.

The agent should assess whether the risk is:

```text
Already reflected in valuation
Understated in valuation
Missing from valuation downside
Not valuation-relevant yet
```

The agent does not own the valuation model, but it must challenge whether the downside case is severe enough.

### 10. Qualitative judgment, no false precision

Risk scoring should be qualitative unless strong quantitative evidence exists.

Default fields:

```text
Likelihood: Low / Medium / High
Impact: Moderate / High / Severe
Evidence Strength: Weak / Mixed / Strong
Time Horizon: Near-term / Medium-term / Long-term
Thesis Damage: Limited / Material / Thesis-breaking
```

Numerical probabilities should be used only when supported by market-implied data, historical datasets, option-implied signals, credit spreads, sector statistics, or model sensitivities.

### 11. Temporary vs structural vs permanent impairment

The agent must distinguish:

```text
Temporary impairment:
Short-term earnings, sentiment, or multiple pressure without long-term thesis damage.

Structural impairment:
Long-term deterioration in moat, pricing power, unit economics, ROIC, terminal value, or capital intensity.

Permanent impairment risk:
Potential irreversible capital loss through dilution, insolvency, fraud, regulatory ban, secular decline, or destructive leverage / M&A.
```

### 12. Evidence gap as risk

If a thesis-critical assumption cannot be supported with adequate evidence, the evidence gap itself may become a risk.

This does not automatically break the thesis. It may:

- reduce review status to Limited;
- trigger a Priority Challenge Request;
- move a risk to Watchlist;
- escalate if the gap concerns accounting, governance, liquidity, or hard red flags.

### 13. Cross-report tension without internal agent references

The agent should identify analytical tensions across the input reports, but the final report should not say:

```text
The Equity Agent said...
The Valuation Agent concluded...
```

Instead, it should translate tensions into natural investment language.

Example:

```text
The investment case combines a strong moat assumption with a valuation that already embeds durable premium growth. This creates limited room for evidence of pricing pressure or market-share loss.
```

Internal agent names may appear only in workflow handoff or challenge requests.

### 14. No hidden recommendation rule

The agent may issue a risk challenge verdict, but must not give investment recommendations.

Allowed:

```text
Thesis Intact
Thesis Impaired
Thesis At Risk
Thesis Broken
Blocked
```

Not allowed:

```text
Buy
Sell
Avoid
Reduce
Add
Position size
Target price
```

Final investment action belongs to the Investment Committee Agent.

### 15. Risk-to-action separation

The agent may recommend analytical or workflow actions:

- investigate;
- validate;
- rerun sensitivity;
- escalate;
- monitor;
- request upstream review.

It must not recommend investment actions.

## Output Status

Every output must be classified as:

```text
Complete Risk Review
Limited Risk Review
Blocked Risk Review
Preliminary Risk Scan
```

### Complete Risk Review

Used when the core thesis, valuation expectations, financials, and key evidence are available enough to assess material failure paths and issue a decision-useful risk challenge verdict.

### Limited Risk Review

Used when risk analysis is possible but important evidence gaps remain, such as incomplete customer data, segment economics, financial details, market expectations, competitive evidence, or source quality.

### Blocked Risk Review

Used when a useful risk verdict cannot be issued due to missing core inputs, especially:

- missing equity company analysis;
- missing valuation expectations;
- no clear core thesis;
- no current valuation context;
- unresolved hard red flag requiring investigation.

### Preliminary Risk Scan

Used in direct specialist calls when the agent does not have the full workflow packet but can still identify early risk hypotheses.

## Direct Specialist Call Mode

The Risk / Red Team Agent must remain independently callable.

Modes:

```text
Full Workflow Mode:
Full deep-dive packet is available.

Direct Call with Existing Reports:
Some reports exist; classify as Complete, Limited, or Blocked based on input quality.

Direct Call without Reports:
The agent may produce a Preliminary Risk Scan, but must not pretend to have reviewed valuation or full evidence.

Blocked:
No clear asset, thesis, or context is available.
```

Without `valuation_expectations.md`, the agent cannot produce a complete priced-in expectations or bear-case integrity review.

## Evidence Collector Interface

The Risk / Red Team Agent should use `evidence_pack.md` as its primary evidence base and preserve Evidence Collector limitations around missing, stale, proxied, contradicted, or weak evidence.

If a thesis-critical risk area lacks adequate evidence, the agent should treat the evidence gap as a risk signal and, when needed, submit a structured request through `evidence-request-protocol.md`.

Material risk evidence discovered during red-team work must be registered back into the evidence pack before it supports decision-relevant conclusions or Investment Committee synthesis.

## Required Inputs

Minimum required inputs:

```text
equity_company_analysis.md
valuation_expectations.md
```

Preferred full input packet:

```text
evidence_pack.md
financial_statement_analysis.md
sector_context.md
equity_company_analysis.md
valuation_expectations.md
market_positioning.md
news_catalysts.md
macro_sensitivity.md
```

When `macro_sensitivity.md` is available, the Risk / Red Team Agent should consume the `macro_failure_paths` handoff. Macro-derived risks should be translated into thesis failure paths, invalidation triggers, and monitoring items without rewriting the macro regime call or overpromoting a single early-warning indicator into a crisis thesis.

## Report Style

The report must be clear, structured, connected, and decision-useful.

The main report should read as a coherent thesis failure map, not as a collection of disconnected risk notes.

Each failure path should follow a clear chain:

```text
assumption -> failure mode -> transmission mechanism -> evidence -> thesis damage -> invalidation trigger / monitoring
```

The report should use reader-first ordering:

1. top thesis-breaking concern;
2. other high decision-relevance failure paths;
3. risk watchlist;
4. tail risks;
5. excluded / deprioritized risks;
6. appendix.

The executive summary should be short and immediately useful.

## Required Handoff

The final section of `risk_red_team.md` must include a structured handoff block.

Required fields:

```text
risk_review_status:
risk_challenge_verdict:
core_thesis_under_attack:
top_failure_paths:
thesis_critical_assumptions:
bear_case_challenge:
valuation_downside_integrity:
accounting_governance_gate:
balance_sheet_liquidity_gate:
market_expectations_positioning_gate:
risk_watchlist:
tail_risks:
excluded_deprioritized_risks:
invalidation_triggers:
early_warning_indicators:
priority_challenge_requests:
risk_confidence:
handoff_note:
```

## Methodological Source Base

The agent should be grounded in professional risk analysis and investment process discipline, including:

- CFA Institute: material risk analysis, scenario analysis, risk management, financial reporting quality, corporate governance.
- BlackRock: exposure-first risk workflows, scenario analysis, stress testing, risk decomposition.
- J.P. Morgan Asset Management: risk governance, thresholds, stress testing, escalation.
- Morgan Stanley Counterpoint Global: moat durability, ROIC, value creation, expectations embedded in price.
- Oaktree / Howard Marks: permanent loss, uncertainty, margin of safety.
- GMO: valuation risk, quality, overpaying for growth.
- Professional due diligence practice: red flag review and deal-breaker identification.
