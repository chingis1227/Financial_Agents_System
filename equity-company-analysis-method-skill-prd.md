# Equity Company Analysis Method — Skill PRD

## 1. Purpose

The Equity Company Analysis Method is the core skill used by the Equity Agent to analyze a public company as a business.

It answers:

```text
Is this a good business, why, what does the thesis depend on, and what would change the view?
```

The skill does not produce final buy/sell recommendations, target prices, or position sizing.

## 2. Relationship to Equity Agent

The Equity Agent defines the role, workflow, inputs, outputs, and handoffs.

This skill defines the analytical method.

## 3. Core Analytical Principle

The method should identify the few company variables that matter most.

It should not produce an encyclopedic company profile. Every section should connect to business quality, durability, moat, management, thesis variables, or required handoffs.

## 4. Required Method Blocks

The skill uses twelve analytical blocks:

```text
1. What the Company Does
2. How the Company Makes Money
3. Why Customers Buy
4. Revenue and Margin Durability
5. Why the Company Can Win
6. Where the Company Can Lose
7. Management Quality
8. Financial Read-Through
9. What the Thesis Depends On
10. What Would Change the View
11. What to Monitor
12. What Must Be Checked Separately
```

## 5. Method Block 1 — What the Company Does

The agent must explain the company simply.

Required questions:

- What does the company sell?
- Who are the customers?
- What customer problem does it solve?
- Why does the customer pay?
- Can the business be explained in two sentences?

Template:

```text
[Company] sells [product/service] to [customer type].
Customers pay because [problem solved / value delivered], and the business mainly depends on [key demand or usage driver].
```

If the business cannot be explained simply, the agent must say why it is complex.

## 6. Method Block 2 — How the Company Makes Money

The agent must identify the revenue engine.

Required checks:

- revenue sources;
- segment mix;
- geography mix;
- product / service mix;
- pricing model;
- recurring vs transactional revenue;
- volume vs price;
- customer concentration;
- contract length;
- backlog;
- retention / churn, if relevant;
- gross margin logic;
- capital intensity.

Key question:

```text
Is revenue repeatable, predictable, and high quality, or is it one-off, cyclical, price-driven, or customer-concentrated?
```

## 7. Method Block 3 — Why Customers Buy

The agent must assess demand quality.

Required checks:

- customer problem;
- mission-criticality;
- discretionary vs required spend;
- purchase frequency;
- replacement cycle;
- structural vs cyclical demand;
- price sensitivity;
- economic sensitivity;
- regulatory demand drivers;
- technology adoption drivers;
- demand slowdown triggers.

Required output:

```text
Demand Quality: Structural / Cyclical / Mixed / Temporary / Unclear
```

## 8. Method Block 4 — Revenue and Margin Durability

The agent must assess whether growth and margins are durable.

Required checks:

- recurring revenue;
- repeat purchase;
- retention;
- churn;
- backlog;
- contract duration;
- customer concentration;
- pricing power;
- gross margin stability;
- operating leverage;
- input-cost pass-through;
- capital intensity;
- cyclicality;
- margin ceiling;
- margin floor;
- risk of margin mean reversion.

Required outputs:

```text
Revenue durability: Strong / Moderate / Weak / Unclear
Margin durability: Strong / Moderate / Weak / Unclear
Pricing power: Strong / Moderate / Weak / Unclear
```

## 9. Method Block 5 — Why the Company Can Win

The agent must analyze competitive advantage.

Required checks:

- value-chain position;
- proximity to profit pool;
- direct competitors;
- indirect competitors;
- substitutes;
- differentiation;
- scale advantage;
- switching costs;
- network effects;
- brand advantage;
- data advantage;
- ecosystem advantage;
- regulatory advantage;
- IP advantage;
- distribution advantage;
- market share direction;
- evidence in margins, retention, pricing, growth, or customer behavior.

Anti-bugs:

```text
Market leader != moat
High growth != moat
Management claim != moat
```

## 10. Method Block 6 — Where the Company Can Lose

The agent must identify business-model vulnerabilities.

Required checks:

- competitive pressure;
- substitution risk;
- technology disruption;
- regulation;
- customer concentration;
- supplier dependence;
- platform dependence;
- pricing pressure;
- margin compression;
- market saturation;
- cyclicality;
- management execution risk;
- capital allocation mistakes.

Required output:

```text
Main business vulnerability:
[one clear vulnerability, not a generic risk list]
```

## 11. Method Block 7 — Management Quality

The agent must assess management as a core part of business quality.

Required checks:

- track record;
- prior promise vs delivery;
- guidance accuracy;
- strategic consistency;
- capital allocation;
- M&A discipline;
- buyback discipline;
- dividend discipline;
- reinvestment discipline;
- insider ownership;
- incentive alignment;
- dilution / SBC;
- communication quality;
- promotional behavior;
- governance red flags.

Required output:

```text
Management Quality: Strong / Moderate / Weak / Unclear
```

## 12. Method Block 8 — Financial Read-Through

The skill must not redo the full financial statement analysis.

It must interpret what the financials say about the business.

Required checks from Financial Statement Analysis:

- revenue growth quality;
- gross margin trend;
- operating margin trend;
- FCF conversion;
- ROIC;
- working capital;
- capex intensity;
- R&D efficiency;
- sales and marketing efficiency;
- dilution;
- leverage;
- segment economics;
- capital allocation.

Examples:

```text
High ROIC + low capex may indicate asset-light economics.
Revenue growth without FCF conversion weakens growth quality.
Stable gross margin during inflation may support pricing power.
M&A-driven growth without organic growth weakens business-quality evidence.
```

## 13. Method Block 9 — What the Thesis Depends On

The agent must identify 3-5 key thesis variables.

Format:

```text
Thesis Variable:
Why it matters:
Current evidence:
What would confirm it:
What would disconfirm it:
Who should monitor/check it:
```

Examples:

- organic growth durability;
- gross margin resilience;
- market share gains;
- customer retention;
- pricing power;
- capital allocation discipline;
- new product adoption;
- regulatory exposure.

## 14. Method Block 10 — What Would Change the View

The agent must identify 1-3 disconfirming signals.

Format:

```text
The company view should be reconsidered if:
1. [specific evidence]
2. [specific evidence]
3. [specific evidence]
```

Examples:

- organic growth falls below sector growth while peers keep gaining;
- gross margin compression persists despite easing input costs;
- retention deteriorates;
- management shifts toward expensive M&A;
- pricing increases begin to cause churn.

## 15. Method Block 11 — What to Monitor

The agent must identify 5-8 monitoring signals.

Possible metrics:

- organic revenue growth;
- segment growth;
- gross margin;
- operating margin;
- FCF conversion;
- retention / churn;
- backlog / bookings;
- market share;
- pricing actions;
- customer concentration;
- capex efficiency;
- R&D efficiency;
- management guidance accuracy;
- dilution / SBC;
- competitive wins/losses.

Rule:

```text
Monitor only what can change the company-quality view.
```

## 16. Method Block 12 — What Must Be Checked Separately

The agent must state what is outside Equity Agent ownership.

Required handoffs:

```text
Valuation & Expectations: what is already priced in?
Risk / Red Team: what breaks the thesis?
Market Positioning: what does the market already believe?
News & Catalysts: what can change perception or timing?
Macro: which macro variables matter?
Investment Committee: final synthesis and decision.
```

## 17. Required Output Template

```md
## Equity Company Analysis: [Company / Ticker]

## 1. Short View

Business view:
Company-level stance:
Why it matters:
Main thing that can break the view:
What must be checked separately:

## 2. What the Company Does

## 3. How the Company Makes Money

## 4. Why Customers Buy

## 5. Why the Company Can Win

## 6. Where the Company Can Lose

## 7. What the Financials Say About the Business

## 8. Management Quality

## 9. What the Thesis Depends On

## 10. What Would Change the View

## 11. What to Monitor

## 12. What Must Be Checked Separately

## 13. Appendix

### Confidence by Key Conclusion

### Evidence Limits

### Missing Data

### Source Notes

### Targeted Evidence Checks Needed
```

## 18. Main Report vs Appendix

The main report should be clean and practical.

Appendix contains:

- confidence by key conclusion;
- evidence limits;
- missing data;
- source notes;
- targeted evidence checks.

Critical caveats that change the conclusion must stay in the main text.

## 19. Guardrails

The skill must avoid these errors:

```text
Revenue growth != business quality
Market leader != moat
High margin != pricing power
Management confidence != management quality
Good business != good stock
Consensus != truth
SWOT != investment conclusion
```

## 20. Bad vs Better Reasoning

### Revenue Growth

Bad:

```text
The company is high quality because revenue is growing.
```

Better:

```text
Revenue growth supports the thesis only if it is organic, durable, profitable, and not dependent on temporary demand, M&A, or unsustainable customer concentration.
```

### Moat

Bad:

```text
The company has a moat because it is the market leader.
```

Better:

```text
Market leadership may indicate a moat only if supported by customer switching costs, pricing power, retention, scale economics, or persistent share gains.
```

### Pricing Power

Bad:

```text
The company has pricing power because margins are high.
```

Better:

```text
High margins support pricing-power evidence only if margins remain resilient during cost inflation or if price increases occur without volume loss or churn.
```

### Management

Bad:

```text
Management is strong because it sounds confident.
```

Better:

```text
Management quality depends on delivery against prior targets, capital allocation discipline, incentive alignment, communication quality, and evidence of per-share value creation.
```

### Business vs Stock

Bad:

```text
This is a good company, so the stock is attractive.
```

Better:

```text
The company may be high quality, but stock attractiveness depends on valuation, expectations, positioning, catalysts, and risk analysis.
```

## 21. Quality Checks

Before finalizing, the agent must check:

- Is the business explained clearly?
- Are business quality and stock attractiveness separated?
- Are the 3-5 thesis variables explicit?
- Is the main vulnerability clear?
- Are financials interpreted rather than duplicated?
- Are specialist handoffs explicit?
- Are technical caveats moved to appendix?
- Are conclusion-changing caveats kept in the main text?

## 22. Current Design Decisions Captured

1. The skill covers company-quality analysis only.
2. The skill includes method, workflow, output template, guardrails, and quality checks.
3. Financial Statement Analysis remains a separate skill.
4. Financial Read-Through interprets financial outputs rather than recalculating everything.
5. The main report is clean; confidence and source mechanics are in the appendix.
6. The skill prohibits final buy/sell language.
