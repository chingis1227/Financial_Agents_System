# Sector & Industry Analysis Method — Skill PRD

## 1. Purpose

The Sector & Industry Analysis Method is a reusable analytical skill for conducting investment-oriented sector, industry, and broad theme-as-sector analysis.

The method helps agents determine how a sector works, where value is created, who captures profit, what drives growth, how public-market investors can express the thesis, what risks matter, and which next analyses should run.

The skill should be usable by:

- Sector & Industry Analysis Agent;
- Equity Agent when company analysis requires industry context;
- ETF Agent when sector or thematic exposure needs sector-thesis context;
- Structural Winners Discovery Agent when a broad theme requires sector mapping first;
- Investment Committee Agent as a reference when synthesizing sector reports.

## 2. Core Philosophy

Sector analysis is useful only when it changes an investment decision. The method should focus on the 20% of sector facts that explain most of the investment relevance: growth, margins, ROIC, risk, valuation, competitive advantage, catalysts, and public-market investability.

Core principles:

```text
Great sector ≠ great investment.
Large TAM ≠ value capture.
Fast revenue growth ≠ attractive economics.
No verified source → no factual claim.
```

The method should not create an encyclopedia. Each major section should answer:

```text
What does this mean for the investment decision?
```

## 3. Method Boundaries

The method is a sector-analysis method, not a company-selection or final recommendation method.

It does:

- define sector boundaries;
- map subsectors when needed;
- analyze business models and sector economics;
- assess growth quality;
- identify value-chain structure and profit pools;
- identify key drivers, constraints, risks, and catalysts;
- assess public-market investability;
- provide valuation context;
- produce sector-level next actions and handoffs.

It does not:

- produce final buy/sell recommendations;
- perform full company financial analysis;
- build full valuation models or price targets;
- rank stocks as final investment recommendations;
- perform ETF holdings or structure analysis;
- replace Macro, Risk, Valuation, Equity, ETF, or Structural Winners agents.

## 4. Default Analytical Sequence

```text
1. Classify the request: embedded company, standalone sector, or broad theme-as-sector.
2. Define scope, geography, horizon, and decision context.
3. Build an Evidence Plan.
4. Gather or request evidence through Evidence Collector.
5. Define sector structure and business model.
6. Assess market size, growth, and growth quality.
7. Map subsectors if business models differ materially.
8. Map value chain and profit pools.
9. Identify 3–5 key drivers and constraints.
10. Analyze competitive structure and key players.
11. Assess driver sensitivity: winners and losers.
12. Assess public-market investability.
13. Provide valuation context and what is already priced in.
14. Identify what the market may be missing.
15. Build anti-thesis and thesis-breaker checks.
16. Define monitoring metrics.
17. Produce investment directions and recommended handoffs.
18. Record material data limitations and proxy use.
```

## 5. Scope Classification

The method should distinguish among:

```text
Industry = defined business activity with similar products, customers, and economics.
Sector = broader grouping that may contain multiple industries.
Theme = cross-sector driver or narrative.
```

Routing logic:

```text
Industry → standalone sector diagnostic.
Sector → diagnostic plus subsector map if needed.
Theme → broad theme-as-sector mode or theme / opportunity workflow.
Opportunity search → Structural Winners Discovery Agent.
```

If the user asks to understand structure, use Sector & Industry Analysis. If the user asks to find companies, winners, or beneficiaries, route or hand off to Structural Winners Discovery.

## 6. Evidence Plan Method

Before standalone analysis, define the evidence needed and why it matters.

Evidence categories:

- market size and growth;
- segmentation / subsectors;
- value chain and profit pool;
- key players and market share;
- sector economics, margin, ROIC, and cash conversion;
- supply / demand / capacity where relevant;
- valuation context;
- catalysts and risks;
- monitoring metrics.

For each category, specify:

- preferred source types;
- freshness requirement;
- why it matters to the investment conclusion;
- whether proxy data is acceptable.

## 7. Evidence Hierarchy

### 7.1 Tier 1 — Primary / Official Sources

Preferred:

- SEC EDGAR;
- company filings and regulatory filings;
- 10-K, 20-F, 10-Q, annual and quarterly reports;
- company investor relations materials;
- earnings releases and transcripts;
- government statistics;
- regulators;
- industry associations;
- official exchange, index, or ETF issuer data where relevant.

### 7.2 Tier 2 — Reputable Secondary Sources

Acceptable when primary sources are unavailable or need context:

- Reuters;
- Bloomberg;
- Financial Times;
- Wall Street Journal;
- S&P Global;
- Morningstar;
- reputable public industry research;
- reputable financial media.

### 7.3 Tier 3 — Narrative / Sentiment Sources

Use only as idea triggers or sentiment signals:

- podcasts;
- YouTube;
- social media;
- Reddit;
- Substack;
- informal newsletters;
- interviews without corroboration.

Tier 3 inputs must not be treated as verified factual evidence without stronger corroboration.

## 8. Freshness and Missing Data Method

Use the freshest reliable data when freshness matters.

Freshness matters especially for:

- valuation multiples;
- sector market data;
- company financials;
- market size and growth estimates;
- capacity, backlog, orders, and supply-demand data;
- regulatory developments;
- catalysts and news;
- forecasts and consensus expectations.

If direct data is unavailable:

- state that direct data is unavailable;
- use a logically relevant proxy only when appropriate;
- label the proxy clearly;
- do not present proxy data as original data;
- lower confidence when evidence is stale, inconsistent, indirect, or incomplete.

## 9. Market Size / Growth / TAM Method

Market size analysis should be useful, sourced, and proportionate.

Include:

- current market size when reliable data exists;
- historical growth over 3–5 years, where available;
- forecast growth over 3–5 years, where reliable;
- TAM / SAM only when decision-relevant;
- fastest-growing segments;
- source, date, and reliability note.

Do not turn the report into a TAM consulting deck. Separate inflated TAM claims from realistic addressable market. Treat company TAM slides as low-confidence unless corroborated by independent sources.

## 10. Growth Quality Method

Evaluate whether sector growth is economically attractive.

Questions:

- Is growth structural, cyclical, temporary, or mixed?
- Is growth driven by volume, price, mix, subsidies, cycle, M&A, or durable demand?
- Does revenue growth convert into margins?
- Does growth convert into free cash flow?
- Does the sector generate ROIC above cost of capital?
- Are public investors able to access the profit pool?
- Is the growth already priced into listed securities?

Preferred output labels:

```text
Growth Quality: Structural / Cyclical / Temporary / Mixed
```

## 11. Value Chain and Profit Pool Method

Map only what helps identify value capture.

Ask:

- What does the sector sell?
- Who buys it?
- What does the customer pay for?
- Which chain layers create revenue?
- Which chain layers retain profit?
- Who controls customers, resources, technology, capacity, or distribution?
- Who has pricing power?
- Who carries costs without capturing upside?
- Are the profitable layers investable through public markets?

The method should explicitly avoid assuming that demand growth benefits all companies equally.

## 12. Subsector Map Method

Use this when a sector is broad or contains materially different business models.

For each subsector, identify:

- role in sector;
- business model;
- key drivers;
- economics and capital intensity;
- cyclicality;
- key players;
- main risks;
- investment interest: high / medium / low / too uncertain;
- next analysis.

Do not force one blended conclusion when economics, drivers, risk, or valuation differ across subsectors.

## 13. Driver Selection Method

Choose only 3–5 drivers that actually move the sector.

For each driver, state:

- impact on revenue;
- impact on margins;
- who wins;
- who loses;
- whether the market may underestimate or overestimate the driver;
- which metric shows that the driver is strengthening or weakening.

Classify drivers where useful:

- primary vs secondary;
- structural vs cyclical;
- short-term vs long-term;
- growth driver vs constraint;
- technological, regulatory, macroeconomic, behavioral, or supply-side.

## 14. Competitive Structure Method

Use Porter Five Forces, SWOT, PESTEL, and lifecycle analysis as internal filters, not as large mandatory report sections.

Assess:

- key players;
- leaders, challengers, enablers, substitutes;
- market share direction where sourced;
- basis of competition: price, product, service, brand, technology, scale, distribution;
- barriers to entry;
- buyer power;
- supplier power;
- substitute risk;
- pricing power;
- disruption risk.

For key players, use concise profiles:

```text
Why it matters.
Which driver it depends on.
Main sector-level risk.
```

Do not perform full company financial analysis.

## 15. Driver Sensitivity Method

Run practical “what if” tests:

- If demand rises, who earns the most?
- If prices fall, who loses money first?
- If rates stay high, who cannot finance growth?
- If capacity is scarce, who has spare or constrained capacity?
- If regulation tightens, who benefits from scale?
- If technology becomes cheaper, who is cannibalized?
- Who controls the customer?
- Who controls the profitable chain layer?
- Who grows with the market but fails to earn economic profit?

The output should identify winners and losers by business model or beneficiary type, not default to stock recommendations.

## 16. Public Market Investability Method

Assess whether investors can express the thesis through public securities.

Questions:

- Is the main profit pool public or private?
- Are there quality listed pure plays?
- Are public companies direct beneficiaries or weak proxies?
- Are ETFs / baskets useful or diluted?
- Is exposure too concentrated in already expensive winners?
- Are there second-order or adjacent public beneficiaries?

If sector structure is attractive but public investability is weak, state it directly.

Example:

```text
The sector may be structurally attractive, but the public-market expression is weak, diluted, private-heavy, or already overvalued.
```

## 17. Valuation Context Method

Provide sector valuation context without building a formal model.

Assess:

- relevant multiples;
- current multiples versus historical range;
- sector premium / discount versus broad market;
- leader premium versus quality;
- earnings cycle stage;
- risk of multiple compression;
- whether cheap companies are cheap for structural reasons;
- what the market appears to price in.

Use labels:

```text
Valuation Context: Attractive / Fair / Expensive / Too Uncertain
```

No price targets. No DCF. No final buy/sell recommendation.

## 18. What the Market May Be Missing Method

Identify plausible misperceptions only when evidence supports them.

Common categories:

- wrong profit-pool location;
- underestimated bottleneck;
- overestimated TAM;
- structural growth mistaken for temporary hype;
- temporary pull-forward mistaken for structural growth;
- hidden second-order beneficiaries;
- obvious leaders already pricing in too much success;
- cheap companies with structural impairment.

## 19. Anti-Thesis Method

Formulate the strongest bear case against the sector thesis.

Ask:

- What must happen for the sector to become a poor investment?
- What risk may the market underestimate?
- Where could growth fail to become profit?
- Where could public investors fail to access the profit pool?
- Where could valuation leave no margin of safety?
- What indicator would first show that the thesis is breaking?

The anti-thesis should attack the core thesis, not list generic risks.

## 20. Monitoring Metrics Method

Select 3–5 metrics that best track sector thesis health.

Metrics should show:

- whether the thesis is working;
- whether sector growth is strengthening or weakening;
- whether margins are improving or deteriorating;
- whether competitive position is changing;
- whether valuation expectations are becoming more or less demanding;
- whether catalysts or thesis breakers are emerging.

For each metric, specify:

- source / where to monitor;
- frequency;
- what confirms the thesis;
- what weakens or breaks the thesis.

## 21. Handoff Method

Recommend next analysis without triggering it automatically.

Handoff options:

- Structural Winners Discovery Agent;
- Equity Agent;
- Valuation & Expectations Agent;
- Risk / Red Team Agent;
- Macro Agent;
- ETF Agent;
- News & Catalysts Agent;
- Investment Committee Agent if final synthesis is requested.

Each handoff should specify:

```text
Next agent / Why needed / Question to answer / Priority
```

## 22. Output Style Rules

- Write in English for project artifacts and reports.
- Use a readable investment memo style.
- Keep tables limited and compact.
- Do not create charts or diagrams by default.
- Do not use numeric scoring.
- Use qualitative labels and concise judgment.
- Include enough detail to support a serious investment decision, but avoid encyclopedia-style history.
- Use “too uncertain” when evidence does not support a confident conclusion.

## 23. Reference Framework Requirement

The user’s original Russian sector-analysis prompt should be professionalized into an English reference file:

```text
sector-industry-analysis-framework.md
```

The reference should preserve the core ideas:

- Pareto focus on decision-relevant factors;
- market size, growth, and TAM discipline;
- structural vs cyclical vs temporary growth;
- value-chain and profit-pool analysis;
- sector economics and relevant metrics;
- valuation context;
- beneficiaries, dependencies, and second-order effects;
- anti-thesis;
- monitoring metrics;
- source reliability and freshness rules.

It should add professional safeguards:

- anti-hallucination standard;
- evidence hierarchy;
- freshness requirements;
- proxy-data handling;
- public investability analysis;
- explicit handoff logic;
- no final buy/sell recommendations;
- no numeric scoring;
- no charts by default.

## 24. Future Extensions

Potential extensions:

- comparative sector mode;
- sector-specific evidence playbooks;
- metric library by industry;
- sector-specific report templates;
- structured JSON outputs;
- automated monitoring workflows;
- visual value-chain maps when explicitly requested.
