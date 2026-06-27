# Risk / Red Team Framework

## Objective

This framework defines the practical checklist used by the Risk / Red Team Agent when producing `risk_red_team.md`.

The framework is designed for public listed equities.

The output must be a clear, connected, decision-useful thesis failure map. It should not be a generic risk list.

## Core Output Structure

```text
## Risk / Red Team Review

## 1. Risk Executive Summary
## 2. Core Thesis Under Attack
## 3. Critical Assumptions Map
## 4. Thesis Failure Map
## 5. Bear Case Challenge
## 6. Mandatory Risk Gates
## 7. Risk Watchlist
## 8. Tail Risks
## 9. Excluded / Deprioritized Risks
## 10. Priority Challenge Requests
## 11. Handoff to Investment Committee

## Appendix
A. Evidence Quality Notes
B. Source Limitations
C. Confidence Notes
D. Omitted Risk Rationale
E. Technical Checks
```

## Main Report Rules

The main report must be:

- clear;
- structured;
- connected;
- concise;
- low-table;
- decision-useful.

The report should read as:

```text
assumption -> failure path -> transmission mechanism -> evidence -> thesis damage -> trigger / monitoring
```

Move technical detail to appendix unless it changes the verdict.

## Risk Executive Summary Template

Keep this section short.

```text
Risk Challenge Verdict:
Risk Review Status:
Top Thesis-Breaking Concern:
Main Reason:
What Would Change the View:
Priority Challenge Request:
```

## Core Thesis Under Attack Template

```text
Core Thesis:
What Is Priced In:
Key Return Drivers:
Key Thesis Dependencies:
```

Do not refer to internal agents in the main report. Translate input-report tensions into natural investment language.

## Critical Assumptions Map

Identify the assumptions that carry the thesis:

```text
Growth durability:
Margin sustainability:
Pricing power:
Moat persistence:
Customer / demand durability:
ROIC and reinvestment runway:
FCF conversion:
Capital intensity:
Balance sheet resilience:
Valuation multiple durability:
Catalyst timing:
Market expectations:
```

A compact table is allowed here if it improves clarity.

## Failure Path Risk Card Template

Use risk cards, not default tables.

```text
### Failure Path [Number] — [Name]

Assumption Under Attack:

Why It Matters:

Transmission Mechanism:

Valuation Link:

Evidence Today:

Counter-Evidence:

What Would Confirm It:

What Would Disconfirm It:

Thesis Invalidation Trigger:

Early Warning Indicators:

Impairment Type:
Temporary / Structural / Permanent-risk

Time Horizon:
Near-term / Medium-term / Long-term

Likelihood:
Low / Medium / High

Impact:
Moderate / High / Severe

Evidence Strength:
Weak / Mixed / Strong

Thesis Damage:
Limited / Material / Thesis-breaking

Valuation Treatment:
Already reflected / Understated / Missing / Not valuation-relevant yet
```

## Risk Maturity Test

Before including a risk in the main failure map, verify:

```text
[ ] Clear assumption link
[ ] Clear transmission mechanism
[ ] Current evidence or explicit evidence gap
[ ] Confirmation / disconfirmation trigger
[ ] Thesis damage assessment
[ ] Valuation or market expectations link
```

If the risk does not pass this test, move it to Watchlist, Excluded / Deprioritized, or Appendix.

## Bear Case Challenge Template

```text
Is the valuation bear case severe enough?

Which assumptions are stressed?

Which assumptions are not stressed enough?

Could the bear case become the base case?

What could make downside worse than the current bear case?

Does downside include multiple compression, FCF deterioration, balance sheet pressure, and confidence effects where relevant?
```

## Mandatory Risk Gates

### Accounting / Governance Red Flag Gate

```text
Status:
Clear / Watch / Escalate / Blocked

Main Finding:
Required Escalation:
```

Checklist:

```text
[ ] Auditor qualified opinion
[ ] Material weakness in internal controls
[ ] Restatements
[ ] Late filings
[ ] Aggressive revenue recognition
[ ] Recurring one-off adjustments
[ ] Earnings vs operating cash flow divergence
[ ] Related-party opacity
[ ] Insider selling / pledging
[ ] Weak shareholder rights
[ ] Questionable capital allocation
[ ] Regulatory investigations
```

### Balance Sheet / Liquidity Fragility Gate

```text
Status:
Clear / Watch / Escalate / Blocked

Main Finding:
Required Escalation:
```

Checklist:

```text
[ ] Leverage risk
[ ] Debt maturity wall
[ ] Refinancing sensitivity
[ ] Interest coverage pressure
[ ] Covenant pressure
[ ] Liquidity runway
[ ] Working capital squeeze
[ ] Capex commitments
[ ] Lease / pension / off-balance sheet obligations
[ ] Debt-funded buybacks or dividends
[ ] Dilution risk
[ ] External capital dependence
```

### Market Expectations / Positioning Gate

```text
Status:
Clear / Watch / Escalate

Main Finding:
Required Escalation:
```

Checklist:

```text
[ ] Crowded long
[ ] Consensus darling
[ ] Valuation prices perfection
[ ] Fragile narrative stock
[ ] High short interest
[ ] Ownership concentration
[ ] Passive / ETF flow sensitivity
[ ] Sell-side consensus skew
[ ] Option-implied stress signals
[ ] Recent rerating unsupported by fundamentals
```

## Consensus / Narrative Challenge

Use only when material.

```text
What does the market appear to assume?

Where could consensus be complacent?

Where could consensus be too bearish?

What evidence would force an expectations reset?
```

## Sector-Specific Risk Overlay

Apply relevant sector lens.

```text
Banks:
credit losses, deposits, NIM, capital adequacy, duration risk.

REITs:
cap rates, occupancy, refinancing, tenant concentration.

SaaS / Software:
NRR, churn, CAC payback, SBC dilution, mature FCF margin.

Energy:
commodity price, reserves, decline rates, capex discipline, breakeven.

Semiconductors:
cycle, customer concentration, export controls, inventory, capex digestion.

Biotech:
trial failure, regulatory approval, cash runway, dilution.

Retail:
traffic, same-store sales, inventory, shrink, operating leverage.

Cyclicals:
peak earnings, normalized margins, backlog quality, working capital reversal.
```

## Risk Watchlist

Use for potentially material risks that are not mature enough for the main failure map.

Maximum 3-5 items.

```text
Risk:
Why Monitored:
What Would Move It Into Main Failure Map:
```

## Tail Risks

Include only if thesis-relevant.

```text
Tail Risk:
Why It Matters:
Potential Damage:
Why It Is Not a Main Failure Path:
Monitoring Signal:
```

## Excluded / Deprioritized Risks

Keep short.

```text
Risk:
Reason for Exclusion / Deprioritization:
Monitoring Condition:
```

## Priority Challenge Requests

Maximum 3-5.

```text
1. Owner:
   Request:
   Why It Matters:

2. Owner:
   Request:
   Why It Matters:
```

Use analytical actions only:

```text
Investigate
Validate
Rerun sensitivity
Escalate
Monitor
Request review
```

Do not use investment actions:

```text
Buy
Sell
Reduce
Add
Allocate
Set target price
```

## Handoff Block

Every report must end with:

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

## Appendix Guidance

Appendix may include:

```text
A. Evidence Quality Notes
B. Source Limitations
C. Confidence Notes
D. Omitted Risk Rationale
E. Technical Checks
```

Technical caveats stay in appendix.

Caveats that change the verdict stay in the main report.

Risk Confidence and Evidence Confidence should usually appear in appendix or handoff, unless they materially change the verdict.

## Plain-English Decision Clarity Test

Before finalizing, check whether a reader can understand after one read:

```text
What can break?
Why does it matter?
How does it flow through economics and valuation?
What evidence exists today?
What would confirm or disconfirm the risk?
Is valuation downside severe enough?
What must be monitored or escalated next?
What is the final risk challenge verdict?
```

If not, rewrite the report.

## Style Anti-Generic Rule

Avoid empty risk phrasing.

Weak:

```text
Competition risk remains a concern.
Macro uncertainty could pressure results.
Execution risk is important.
Regulation may be a headwind.
```

Better:

```text
Competition matters only if it forces discounting or market-share loss. The thesis would be materially weaker if pricing pressure reduces gross margin and causes the market to question the durability of the current premium multiple.
```

## Final Standard

A strong `risk_red_team.md` makes clear:

```text
what can break;
why it matters;
how it flows through economics and valuation;
what evidence exists today;
what would confirm or disconfirm the risk;
whether the valuation downside is severe enough;
what Investment Committee must monitor or challenge next.
```

A weak output is a disconnected list of generic risks.
