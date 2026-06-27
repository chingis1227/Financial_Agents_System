# Risk / Red Team Method Skill PRD

## Purpose

The Risk / Red Team Method Skill defines how the Risk / Red Team Agent challenges an investment thesis in a disciplined, materiality-first, evidence-aware framework.

The skill should help the agent avoid shallow conclusions such as:

```text
The company faces competition, regulation, macro risk, and execution risk.
```

Instead, it should produce conclusions such as:

```text
The thesis depends on sustained premium revenue growth and stable gross margins, both already embedded in valuation. The main failure path is not generic competition, but a pricing-power reset if new entrants force discounting and reduce gross margin by 300-500 bps. This would weaken FCF conversion, compress the valuation multiple, and make the current bear case too mild.
```

## Core Doctrine

```text
Risk analysis = thesis-critical assumption failure analysis.
```

The agent evaluates:

- what must be true for the thesis to work;
- which assumptions are most fragile;
- what is already priced in;
- how downside could materialize;
- whether current evidence supports or weakens the risk;
- whether valuation downside is severe enough;
- what would invalidate the thesis.

## Required Analytical Steps

## 1. Establish Input Completeness

Confirm availability of:

```text
equity_company_analysis.md
valuation_expectations.md
```

Then check for the broader packet:

```text
evidence_pack.md
financial_statement_analysis.md
sector_context.md
market_positioning.md
news_catalysts.md
macro_sensitivity.md
```

Classify the review as Complete, Limited, Blocked, or Preliminary.

## 2. Determine Operating Mode

Classify the task:

```text
Full Workflow Mode
Direct Call with Existing Reports
Direct Call without Reports
Blocked
```

If the agent lacks full inputs, it must clearly state what is missing and avoid overstating confidence.

## 3. Extract the Core Thesis

Identify:

- investment thesis;
- business-quality claim;
- valuation setup;
- market-implied expectations;
- expected return drivers;
- key catalysts;
- major assumptions from existing reports.

The agent should restate the thesis briefly before attacking it.

## 4. Build the Critical Assumptions Map

Identify assumptions that carry the thesis:

- growth durability;
- margin sustainability;
- pricing power;
- customer retention / demand durability;
- moat persistence;
- ROIC and reinvestment runway;
- FCF conversion;
- capital intensity;
- leverage and liquidity resilience;
- management capital allocation;
- valuation multiple durability;
- catalyst timing;
- market expectations.

## 5. Apply Anti-Overbreaking Discipline

The agent must not attack the thesis mechanically.

Do not include a risk unless it is:

- material;
- economically plausible;
- connected to a thesis-critical assumption;
- connected to priced-in expectations or downside asymmetry;
- supported by a clear transmission mechanism.

Avoid generic "everything can go wrong" analysis.

## 6. Apply Materiality Filter

Before including a risk, test whether it passes at least one:

```text
Price-in test
Thesis-critical test
Downside-asymmetry test
Early-evidence test
```

Exclude, deprioritize, or watchlist risks that are:

- generic;
- already fully reflected;
- low impact;
- not connected to thesis assumptions;
- unsupported by evidence;
- lacking a transmission mechanism.

## 7. Apply Risk Maturity Test

A risk can enter the main failure map only if it has:

```text
Assumption link:
Which thesis assumption breaks?

Transmission mechanism:
How does it hit revenue, margin, FCF, multiple, balance sheet, or thesis credibility?

Evidence:
What is visible today, or what critical evidence is missing?

Trigger:
What would confirm or disconfirm the risk?

Thesis damage:
Is the damage limited, material, thesis-breaking, temporary, structural, or permanent-risk?
```

If not mature, move it to Watchlist, Excluded / Deprioritized, or Appendix.

## 8. Identify 3-7 Failure Paths

For each material failure path, provide a risk card.

Required fields for top 3:

```text
Failure Path:
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
Time Horizon:
Likelihood:
Impact:
Evidence Strength:
Thesis Damage:
Valuation Treatment:
```

Additional failure paths may be shorter if less decision-critical.

## 9. Challenge the Bear Case

The agent does not own bull/base/bear valuation scenarios. That is owned by Valuation & Expectations.

The Risk / Red Team Agent must test:

- whether the bear case is severe enough;
- whether the right assumptions are stressed;
- whether multiple compression is included where relevant;
- whether downside ignores second-order effects;
- whether the bear case could become the base case;
- what could make downside worse than modeled.

## 10. Run Mandatory Risk Gates

### Accounting / Governance Red Flag Gate

Status:

```text
Clear / Watch / Escalate / Blocked
```

Check:

- auditor issues;
- material weakness in internal controls;
- restatements;
- late filings;
- aggressive revenue recognition;
- recurring one-off adjustments;
- earnings vs operating cash flow divergence;
- related-party opacity;
- insider selling / pledging;
- weak shareholder rights;
- questionable capital allocation;
- regulatory investigations.

### Balance Sheet / Liquidity Fragility Gate

Status:

```text
Clear / Watch / Escalate / Blocked
```

Check:

- leverage;
- debt maturity wall;
- refinancing sensitivity;
- interest coverage;
- covenant pressure;
- liquidity runway;
- working capital squeeze;
- capex commitments;
- lease / pension / off-balance sheet obligations;
- debt-funded buybacks or dividends;
- dilution risk;
- dependence on external capital markets.

### Market Expectations / Positioning Gate

Status:

```text
Clear / Watch / Escalate
```

Check only when relevant:

- crowded long;
- consensus darling;
- valuation prices perfection;
- fragile narrative stock;
- high short interest;
- ownership concentration;
- passive / ETF flow sensitivity;
- sell-side consensus skew;
- option-implied stress signals;
- recent rerating unsupported by fundamentals.

## 11. Challenge Consensus and Market Narrative

When material, assess:

```text
What does the market appear to assume?
Where could consensus be complacent?
Where could consensus be too bearish?
What evidence would force an expectations reset?
```

This is a risk overlay, not a replacement for Market Positioning.

## 12. Apply Sector-Specific Risk Overlays

Use the universal framework, but apply sector-specific risk lenses where relevant.

Examples:

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

## 13. Build Risk Watchlist

Use a short watchlist for potentially material risks that are not mature enough for the main failure map.

Template:

```text
Risk:
Why monitored:
What would move it into main failure map:
```

Maximum 3-5 items.

## 14. Separate Plausible Failure Paths from Tail Risks

Main failure paths should be plausible and material.

Tail risks should be listed separately only when they are:

- thesis-relevant;
- severe enough to matter;
- capable of permanent impairment;
- not already captured by normal downside.

## 15. Include Counter-Evidence

For each major failure path, identify evidence that weakens the red-team case.

The agent must avoid becoming a mechanical bear-case generator.

Counter-evidence may include:

- resilient margins;
- strong retention;
- improving competitive position;
- conservative valuation assumptions;
- strong balance sheet;
- management actions that reduce downside;
- evidence that the risk is already priced in.

## 16. Handle Cross-Report Tensions

If input reports imply conflicting assumptions, translate the conflict into investment language.

Do not write:

```text
The Equity Agent said...
The Valuation Agent said...
```

Write:

```text
The thesis depends on sustained pricing power despite rising competitive intensity. If discounting becomes visible, margin durability and the premium multiple would both be at risk.
```

## 17. Issue Risk Challenge Verdict

Allowed verdicts:

```text
Thesis Intact
Thesis Impaired
Thesis At Risk
Thesis Broken
Blocked
```

The verdict must be concise:

```text
Risk Challenge Verdict: Thesis At Risk

Reason:
The thesis depends on durable premium growth already embedded in valuation. Current evidence does not break the thesis, but margin sensitivity and competitive pricing signals make the valuation bear case insufficiently severe.
```

Do not give buy/sell/hold recommendations.

## 18. Create Priority Challenge Requests

If material gaps exist, issue 3-5 priority requests.

Examples:

```text
Valuation:
Rerun downside scenario with gross margin -300 bps and terminal multiple normalization.

Equity:
Validate switching-cost claim using retention, churn, pricing, customer concentration, and contract renewal evidence.

Financials:
Investigate operating cash flow divergence from net income and working capital quality.
```

If no requests are needed:

```text
No priority challenge requests.
```

Challenge requests are workflow actions, not investment actions.

## 19. Evidence Quality Discipline

The agent should not re-audit every upstream source.

It should selectively check source quality when a material failure path depends on a critical fact.

Check:

- source reliability;
- timestamp;
- primary vs secondary evidence;
- conflicting evidence;
- management claim vs independent evidence;
- missing segment / customer / market data;
- stale assumptions.

Main report includes evidence caveats only if they change the risk verdict.

Technical evidence notes go to appendix.

## 20. Plain-English Decision Clarity Test

Before finalizing, silently verify that a reader can understand after one read:

- what can break the thesis;
- why it matters;
- how it damages economics or valuation;
- what evidence supports or weakens the concern;
- what would prove the risk right or wrong;
- whether valuation downside is severe enough;
- what must be monitored or escalated next;
- what the final risk challenge verdict is.

If not, rewrite the report.

## Style Anti-Generic Rule

Avoid generic risk boilerplate.

Do not write:

```text
Competition risk remains a concern.
Macro uncertainty could pressure results.
Execution risk is important.
Regulation may be a headwind.
```

Write specific, causal, investment-relevant risk analysis:

```text
Competition matters only if it forces discounting or market-share loss. The thesis would be materially weaker if pricing pressure reduces gross margin and causes the market to question the durability of the current premium multiple.
```

## Appendix Requirements

The appendix may include:

- evidence quality by failure path;
- source limitations;
- stale data warnings;
- conflicting evidence;
- omitted risk rationale;
- confidence notes;
- sensitivity notes;
- technical checks.

## Final Standard

A good Risk / Red Team output does not say:

```text
The company has competition, macro, regulatory, and execution risk.
```

It says:

```text
The thesis depends on sustained premium growth, stable margins, and a durable valuation multiple. The most material failure path is a pricing-power reset: if competitive intensity forces discounting, gross margin and FCF conversion weaken, while the current premium multiple becomes harder to defend. This risk is not yet confirmed, but early pricing signals and limited bear-case margin stress make it the key issue for Investment Committee review.
```
