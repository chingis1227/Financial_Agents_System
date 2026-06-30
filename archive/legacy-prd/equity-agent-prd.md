# Equity Agent — Product Requirements Document

## 1. Purpose

The Equity Agent is the lead company-analysis agent for public listed equities.

Its core question is:

```text
Is this a good business, why, what does the thesis depend on, what could change the view, and what must be checked separately before a final investment decision?
```

The Equity Agent evaluates company quality. It does not issue final buy/sell recommendations, target prices, position sizes, or portfolio decisions.

## 2. Scope

The Equity Agent covers global public equities.

The system is US-first in source depth, but global-compatible:

- For US-listed companies: 10-K, 10-Q, 8-K, DEF 14A, earnings releases, transcripts, investor presentations.
- For non-US companies: annual reports, interim reports, exchange filings, local regulator filings, investor presentations, IFRS/GAAP disclosures.
- For ADRs: underlying issuer reports should be used where possible.

Private companies, startups, VC-style analysis, and private-market diligence are out of scope.

## 3. Role in the System

The Equity Agent owns company-quality analysis.

It is responsible for:

- business model;
- revenue model;
- customer and demand logic;
- pricing power;
- revenue and margin durability;
- competitive position;
- moat;
- management quality;
- company-specific vulnerabilities;
- key thesis variables;
- monitoring signals;
- handoff notes for other agents.

It does not own:

- final investment recommendation;
- target price;
- position sizing;
- full valuation;
- full risk verdict;
- market timing;
- portfolio fit;
- final synthesis.

Final synthesis belongs to the Investment Committee Agent.

## 4. Default Mode

The default mode is:

```text
Standard Investment-Oriented Equity Deep Dive
```

There are no quick / standard / deep variants in the target design.

The default output is:

```text
equity_company_analysis.md
```

## 5. Required Direct Inputs

The Equity Agent should use:

```text
evidence_pack.md
financial_statement_analysis.md
sector_context.md
material news/catalyst notes, if already available
```

The Evidence Collector Agent is responsible for the base evidence pack. The Equity Agent may request or perform targeted evidence checks if a critical fact is missing.

## 6. Required Parallel Reports in Full Equity Workflow

A full investment-oriented equity workflow also requires:

```text
valuation_expectations.md
risk_red_team.md
market_positioning.md
news_catalysts.md
macro_sensitivity.md
```

These are not all direct inputs into the Equity Agent. They are parallel specialist reports used by the Investment Committee Agent for the final memo.

## 7. Final Synthesis

The final investment memo is produced by:

```text
Investment Committee Agent -> final_investment_memo.md
```

The Equity Agent contributes the company-quality view but does not make the final investment decision.

## 8. Core Output Structure

The Equity Agent output should use simple, reader-friendly headings:

```text
1. Short View
2. What the Company Does
3. How the Company Makes Money
4. Why Customers Buy
5. Why the Company Can Win
6. Where the Company Can Lose
7. What the Financials Say About the Business
8. Management Quality
9. What the Thesis Depends On
10. What Would Change the View
11. What to Monitor
12. What Must Be Checked Separately
13. Appendix
```

## 9. Short View Requirements

The Short View must answer:

```text
Business view:
Company-level stance:
Why it matters:
Main thing that can break the view:
What must be checked separately:
```

Allowed company-level stances:

```text
High-quality business candidate
Promising but valuation-dependent
Watch-only until evidence improves
Weak business quality
Avoid on business quality
Needs more evidence
```

Forbidden language:

```text
Buy
Sell
Short
Target price
Position size
Final recommendation
```

## 10. Business Quality vs Stock Attractiveness

The Equity Agent must separate:

```text
Business quality != stock attractiveness
```

The agent may conclude that a company is a high-quality business, but it must not conclude that the stock is attractive without Valuation & Expectations analysis.

## 11. Main Report vs Appendix Rule

The main report should be clean, practical, and decision-useful.

Technical material belongs in the appendix:

- confidence by key conclusion;
- evidence limits;
- missing data;
- source notes;
- targeted evidence checks needed.

Critical caveats that change the conclusion must remain in the main text.

This rule should later be elevated into a global report-style standard for all agents.

## 12. Handoff Rules

The Equity Agent must explicitly identify what needs to be checked separately:

- Valuation & Expectations: what is already priced in?
- Risk / Red Team: what could break the thesis?
- Market Positioning: what does the market already believe?
- News & Catalysts: what recent or upcoming events matter?
- Macro: which macro variables matter?
- Investment Committee: final synthesis and decision.

## 13. Guardrails

The Equity Agent must not:

- treat revenue growth as business quality;
- treat market leadership as moat;
- treat high margins as proof of pricing power;
- treat confident management language as management quality;
- confuse business quality with stock attractiveness;
- convert a company analysis into a final investment recommendation;
- bury the main vulnerability in a long generic risk list;
- use SWOT or Porter frameworks as visible filler;
- overstate confidence when evidence is incomplete.

## 14. Relationship to Original Company Deep-Dive Prompt

The original company deep-dive prompt is decomposed across the target system.

| Original Prompt Block | Primary Owner | Equity Agent Role |
|---|---|---|
| Business model | Equity Agent | Primary owner |
| Financial statement analysis | Financial Statement Analysis Skill | Uses and interprets output |
| Valuation | Valuation & Expectations Agent | Handoff |
| Consensus and sentiment | Market Positioning Agent | Handoff |
| Market narrative | Market Positioning / Market Sense | Handoff / context |
| Scenario analysis | Investment Committee Agent | Provides company inputs |
| Sector analysis | Sector & Industry Analysis Agent | Uses sector context |
| Competitive analysis | Equity Agent | Primary owner |
| Macro sensitivity | Macro Agent | Handoff |
| Non-obvious risks | Risk / Red Team Agent | Provides company-specific inputs |
| Historical stock metrics | Market Positioning for expectation / reaction evidence; optional deferred technical / price-action input for trading signals | Market Positioning designed; technical / price-action input deferred outside the core design |
| Recent news | News & Catalysts Agent | Handoff / material context |
| Three key questions | Workflow-level framework | Equity owns business-quality question |
| Investment thesis | Investment Committee Agent | Provides company-quality input |
| Sources | Evidence Collector + all agents | Follows source discipline |

## 15. Current Design Decisions Captured

1. Equity Agent is the lead company-analysis agent for listed equities.
2. Scope is global public equities with US-first source depth.
3. Private companies and startup analysis are out of scope.
4. Equity Agent owns company-quality analysis, not final investment decisions.
5. Equity Agent requires Financial Statement Analysis and Sector / Industry context for full investment-oriented work.
6. Equity Agent uses but does not replace Valuation, Risk, Market Positioning, News, and Macro agents.
7. Equity Agent produces `equity_company_analysis.md`.
8. Final synthesis belongs to the Investment Committee Agent.
9. Main report stays clean; technical confidence and source mechanics go to appendix.
10. Critical caveats that change the conclusion remain in the main text.
