# Financial Statement Analysis Skill — Product Requirements Document

## 1. Purpose

The `financial-statement-analysis` skill is a reusable analytical playbook for diagnosing the financial quality of public companies and, secondarily, corporate issuers with available financial statements.

The skill should not produce a buy/sell recommendation, target price, fair value estimate, or full valuation conclusion. Its purpose is to determine what the financial statements reveal about the economic quality, durability, risk, reinvestment profile, and financial resilience of the business.

The skill should produce a structured Markdown diagnostic memo that can be used by the Equity Agent, Valuation & Expectations Agent, Risk / Red Team Agent, Fixed Income Agent when relevant, and Investment Committee Agent.

## 2. Scope

### 2.1 Primary Scope

The primary use case is public company analysis, especially listed equities with accessible filings, annual reports, quarterly reports, earnings releases, investor presentations, and investor relations materials.

### 2.2 Secondary Scope

The skill should also support analysis of corporate bond issuers or credit-relevant operating companies when financial statements are available.

In issuer / credit-relevant contexts, the skill should add a conditional credit lens focused on leverage, coverage, maturities, liquidity, refinancing risk, and cash-flow resilience.

### 2.3 Out of Scope

The skill is not designed to analyze commodities, crypto assets, ETFs as standalone assets, sovereign bonds, or macro instruments. It may support ETF analysis only indirectly when the ETF holds operating companies whose financial statements are being analyzed.

## 3. Core Analytical Objective

The skill should answer:

> What do the financial statements reveal about the financial quality, durability, risk, and reinvestment profile of the business?

It should classify the company’s financial quality as one of:

- Strong
- Solid
- Mixed
- Weak
- Distressed
- Insufficient evidence

This classification is not an investment recommendation. It is a financial-quality judgment to support downstream analysis.

## 4. Depth Standard

The default depth should be a standard professional diagnostic.

The skill should use:

- 5–10 years of historical data when available and relevant;
- recent quarterly data when needed to understand trend changes;
- key financial statement metrics;
- historical self-comparison;
- financial-quality peer comparison;
- warning signal screening;
- materiality-based footnote review;
- investment implications and downstream handoff notes.

The skill should not build a full three-statement model by default and should not perform full forensic accounting unless red flags justify escalation.

## 5. Source Policy

The skill must follow a source-first policy with filings preferred.

Preferred sources include:

- 10-K filings;
- 10-Q filings;
- annual reports;
- quarterly reports;
- earnings releases;
- official company investor relations materials;
- investor presentations;
- audited financial statements where available.

Secondary financial data sources may be used for convenience, peer comparison, market data, or pre-calculated metrics, but they should not override primary filings for material reported financial figures.

If data conflicts:

- primary filings and company reports win for reported financials;
- discrepancies should be explained when material;
- conflicting figures should not be averaged without a clear rationale;
- fiscal year vs calendar year, reported vs adjusted metrics, continuing operations vs consolidated results, currency, and units must be distinguished;
- unresolved conflicts must be recorded in Evidence Limits.

No verified source means no factual claim.

## 6. Required Analytical Modules

### 6.1 Key Financial Metrics

The skill should collect and analyze the most relevant financial metrics, including revenue, gross profit, operating income, EBITDA where relevant, net income, EPS, operating cash flow, free cash flow, capex, debt, cash, net debt, leverage, liquidity, ROIC, ROE, ROA, dilution, dividends, buybacks, and other company-specific metrics when material.

### 6.2 Growth Quality

The skill should analyze whether growth is high quality, durable, and economically meaningful.

It should distinguish, when evidence allows:

- organic vs acquired growth;
- volume vs price growth;
- mix effects;
- FX effects;
- one-off or pull-forward demand;
- cyclical vs structural growth;
- segment-level growth drivers.

### 6.3 Margin Quality

The skill should analyze gross, operating, EBITDA, and net margin trends where applicable.

It should explain whether margin changes are driven by:

- operating leverage;
- pricing power;
- cost discipline;
- input costs;
- mix shift;
- scale effects;
- accounting adjustments;
- temporary or one-off factors.

### 6.4 Earnings Quality

The skill should assess whether reported earnings reflect durable economic profitability.

It should examine:

- GAAP vs non-GAAP gap;
- recurring vs non-recurring adjustments;
- stock-based compensation exclusions;
- restructuring and acquisition-related adjustments;
- tax effects;
- unusual gains or charges;
- persistence of adjustments over time.

Non-GAAP metrics may be used, but they must be reconciled and challenged. Non-GAAP figures should not be accepted uncritically.

### 6.5 Cash Conversion and Free Cash Flow

The skill should analyze whether earnings convert into cash.

It should examine:

- operating cash flow vs net income;
- free cash flow trend;
- FCF margin;
- FCF conversion;
- capex intensity;
- working capital impact;
- cash taxes and cash interest where relevant;
- recurring vs temporary cash-flow effects.

### 6.6 Balance Sheet Resilience

The skill should evaluate financial flexibility and downside resilience.

It should analyze:

- cash and liquidity;
- debt and net debt;
- net leverage;
- debt-to-equity and debt-to-assets where relevant;
- interest coverage;
- liquidity ratios;
- asset quality;
- off-balance-sheet obligations when material.

### 6.7 Working Capital Signals

The skill should review working capital as a source of financial-quality signals.

It should examine:

- receivables growth vs revenue growth;
- days sales outstanding where relevant;
- inventory growth vs revenue growth;
- inventory turns where relevant;
- payables and supplier financing signals;
- working-capital tailwinds or drags;
- signs of demand weakness, channel stuffing, inventory overbuild, or collection stress.

### 6.8 ROIC and Reinvestment Quality

The skill should evaluate whether the business creates value through reinvestment.

It should analyze:

- ROIC trend;
- ROE and ROA where useful;
- invested capital growth;
- capital intensity;
- reinvestment runway;
- whether growth appears to create or destroy value;
- whether ROIC likely exceeds the company’s cost of capital, with appropriate uncertainty if WACC is not directly estimated.

### 6.9 Capital Allocation

The skill should assess how management uses cash.

It should review:

- dividends;
- buybacks;
- share count change;
- M&A;
- capex;
- R&D investment;
- debt repayment;
- balance between growth investment and shareholder returns;
- whether capital allocation appears disciplined, value-creating, or risky.

### 6.10 Segment-Level Analysis

Segment-level analysis is mandatory when disclosed.

If reportable segments are available, the skill should analyze:

- segment revenue;
- segment growth;
- segment operating income or margin where available;
- contribution to total revenue and profit;
- which segments drive growth;
- which segments create or dilute margin;
- segment mix effects;
- segment-level cyclicality or risk.

If segment data is unavailable or incomplete, the limitation must be recorded.

### 6.11 Peer Financial Quality Comparison

The skill should include peer comparison for financial quality, not valuation.

It should compare the company to 3–6 closest peers where possible across:

- revenue growth;
- margins;
- FCF conversion;
- ROIC / ROE / ROA;
- leverage;
- liquidity;
- capex intensity;
- R&D intensity where relevant;
- SBC and dilution where relevant.

The skill may propose peers if the user does not provide them. Peer selection should include rationale and limitations.

The skill must not compare valuation multiples such as P/E, EV/EBITDA, EV/Sales, or P/FCF. Those belong to the Valuation & Expectations Agent.

### 6.12 Management Guidance Credibility

Management guidance credibility should be included when verifiable.

The skill should review:

- management guidance vs actual results;
- beat / miss pattern;
- conservative vs aggressive guidance style;
- consistency of communication;
- changes in guidance credibility over time.

If data is unavailable or difficult to verify, the skill should mark the section as Insufficient evidence rather than inventing a conclusion.

### 6.13 Conditional Credit Lens

The skill should include a credit lens when the company has material debt, weak cash flow, refinancing risk, or when the request relates to bonds / fixed income.

The credit lens should cover:

- debt load and net leverage;
- interest coverage;
- debt maturity profile;
- liquidity runway;
- refinancing risk;
- downside cash-flow resilience;
- credit implication for equity holders or bondholders.

If debt is not material, the skill should briefly state that no material credit constraint was identified from available evidence.

### 6.14 Targeted Footnote Review

The skill should perform a targeted, materiality-based footnote review.

It should review relevant notes when material, including:

- revenue recognition;
- stock-based compensation;
- lease obligations;
- debt maturities;
- acquisitions and purchase accounting;
- restructuring charges;
- impairments;
- litigation and contingencies;
- tax items;
- pension obligations;
- customer concentration;
- related-party transactions.

The goal is not a full audit, but a financial-quality risk screen.

### 6.15 Driver Decomposition

The skill should include simple driver decomposition when useful.

It should explain what drives financial performance, such as:

- revenue growth: volume, price, mix, FX, acquisitions;
- margin change: gross margin, opex leverage, input costs, pricing, mix;
- ROE / ROIC: margin, turnover, leverage, capital intensity;
- FCF change: earnings, working capital, capex, SBC, taxes;
- EPS change: earnings growth, buybacks, dilution, tax, and interest.

This should be practical and investment-oriented, not an academic exercise.

### 6.16 Reported vs Normalized Performance

The skill should distinguish reported performance from normalized performance when material.

Normalization may be relevant when results are distorted by:

- cyclicality;
- one-off gains or losses;
- restructuring;
- M&A;
- FX;
- abnormal demand;
- inventory cycle;
- commodity price cycle;
- pandemic or post-pandemic distortion;
- unusually high or low margins.

The skill should provide a normalized financial-quality view when needed, but it should not produce a fair value or target price.

## 7. Financial Quality Warning Signals

The skill must include a compact warning signal screen.

Each warning signal should use one of the following statuses:

- No material issue
- Watch
- Material concern
- Insufficient evidence

The warning signal table should include:

- earnings quality;
- GAAP vs non-GAAP gap;
- stock-based compensation / dilution;
- FCF vs net income gap;
- working capital stress;
- receivables growth vs revenue growth;
- inventory build;
- margin compression;
- debt maturity / refinancing risk;
- interest burden;
- acquisition dependence;
- one-off gains or charges;
- aggressive adjustments;
- capex intensity;
- customer concentration if visible in filings.

Suggested format:

```md
| Warning Signal | Status | Evidence | Investment Relevance |
|---|---|---|---|
```

## 8. Forecast-Readiness, Not Forecasting

The skill should not build a full forecast or valuation model.

Instead, it should provide forecast-readiness inputs for the Valuation & Expectations Agent, such as:

- sustainable revenue growth considerations;
- normalized margin view;
- FCF conversion quality;
- capex intensity;
- working-capital assumptions;
- reinvestment needs;
- leverage constraints;
- key financial assumptions that are fragile or uncertain.

The skill must not state fair value, target price, expected return, or upside/downside percentage.

## 9. Required Output Format

The skill should produce a Markdown memo with a compact structured summary block.

Recommended structure:

```md
## Financial Statement Analysis

## 1. Structured Summary
## 2. Executive Financial Quality View
## 3. Key Financial Metrics
## 4. Growth Quality
## 5. Segment-Level Financial Analysis
## 6. Margin Quality
## 7. Earnings Quality
## 8. Cash Conversion and Free Cash Flow
## 9. Balance Sheet Resilience
## 10. Working Capital Signals
## 11. ROIC and Reinvestment Quality
## 12. Capital Allocation
## 13. Peer Financial Quality Comparison
## 14. Management Guidance Credibility
## 15. Credit Lens, If Relevant
## 16. Targeted Footnote Review
## 17. Financial Quality Warning Signals
## 18. Forecast Inputs for Valuation
## 19. Investment Implications
## 20. Handoff Notes
## 21. Evidence Limits and Missing Data
```

### 9.1 Structured Summary

The structured summary should include:

```md
## Structured Summary

- Financial quality classification:
- Key financial strengths:
- Key financial concerns:
- Warning signals:
  - Earnings quality:
  - FCF conversion:
  - Leverage:
  - Working capital:
  - Dilution / SBC:
- Forecast inputs for valuation:
  - Sustainable revenue growth:
  - Normalized margin:
  - FCF conversion:
  - Capex intensity:
  - Reinvestment quality:
- Handoff priority:
```

## 10. Handoff Notes

The final report should include handoff notes for downstream agents.

Suggested structure:

```md
## Handoff Notes

### For Equity Agent
- What the financials imply about business quality, durability, and competitive position.

### For Valuation & Expectations Agent
- Normalized revenue growth, margin, FCF conversion, capex, and reinvestment assumptions.

### For Risk / Red Team Agent
- Main financial fragilities, accounting concerns, leverage risks, or cash-flow weaknesses.

### For Investment Committee Agent
- The central financial trade-off that matters for the final decision.
```

## 11. Relationship to Other Agents and Skills

### 11.1 Equity Agent

The Equity Agent uses this skill to understand financial quality, business durability, segment economics, reinvestment profile, and financial red flags.

### 11.2 Valuation & Expectations Agent

The Valuation & Expectations Agent uses this skill for normalized financial inputs, but owns valuation multiples, fair value, target price, implied expectations, and upside/downside analysis.

### 11.3 Risk / Red Team Agent

The Risk / Red Team Agent uses this skill to identify financial fragilities, accounting concerns, debt risks, working capital stress, dilution risk, and thesis breakers.

### 11.4 Fixed Income Agent

The Fixed Income Agent may use this skill when analyzing corporate issuers, especially for leverage, liquidity, maturity profile, interest coverage, refinancing risk, and downside cash-flow resilience.

### 11.5 Investment Committee Agent

The Investment Committee Agent uses this skill as one evidence-backed input into the final synthesis. It should not treat the financial quality classification as a standalone investment recommendation.

## 12. Non-Goals

The skill should not:

- produce buy / hold / sell recommendations;
- calculate fair value or target price;
- produce expected return or upside/downside percentage;
- replace the Valuation & Expectations Agent;
- replace the Risk / Red Team Agent;
- perform full forensic accounting by default;
- build a full three-statement model by default;
- analyze commodities, crypto, ETFs, or sovereign bonds as standalone assets;
- use unsupported or unsourced numbers;
- treat non-GAAP metrics as automatically superior to GAAP metrics;
- compare valuation multiples in peer analysis.

## 13. Escalation Triggers

The skill should recommend deeper forensic, credit, or specialist review when it identifies material concerns such as:

- persistent gap between net income and cash flow;
- aggressive or recurring non-GAAP adjustments;
- rising receivables or inventory inconsistent with revenue growth;
- rapid margin deterioration;
- high or rising leverage;
- near-term maturity wall;
- weak interest coverage;
- repeated impairments or restructuring charges;
- material related-party transactions;
- unexplained share dilution;
- significant customer concentration;
- major unresolved data conflicts;
- insufficient evidence for key financial claims.

## 14. Current Design Decisions Captured

The following decisions are fixed for v0:

1. The skill is a reusable financial-quality diagnostic, not a valuation tool.
2. The default depth is standard professional diagnostic.
3. Forecasting is limited to forecast-readiness inputs.
4. A compact warning signal screen is mandatory.
5. Primary filings and company reports are preferred sources.
6. Peer comparison is included only for financial quality, not valuation.
7. Management guidance credibility is included when verifiable.
8. Output is a Markdown diagnostic memo with investment implications.
9. Final classification uses Strong / Solid / Mixed / Weak / Distressed / Insufficient evidence.
10. Handoff notes are required for downstream agents.
11. The skill is primarily for public companies and secondarily for corporate issuers.
12. A conditional credit lens is included when relevant.
13. Segment-level analysis is mandatory when disclosed.
14. Footnote review is targeted and materiality-based.
15. Non-GAAP metrics may be used only if reconciled and challenged.
16. Driver decomposition is included when useful.
17. Reported vs normalized performance must be separated when material.
18. Data conflict handling is mandatory.
19. The skill may propose peers with rationale and limitations.
20. Output includes a compact structured summary block for multi-agent handoff.
