# Sector & Industry Analysis Framework

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: Sector & Industry Analysis  
Contributors: Structural Winners Discovery; Equity Agent; Market Intelligence  
Used by: Sector & Industry Analysis Agent; sector-industry-analysis skill  
Primary reference for: sector and industry analysis framework examples  
Supporting reference for: theme workflows, discovery candidates, and asset-level review context  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: Medium  
Last reviewed: 2026-06-28  
Review trigger: Review when sector workflow, discovery taxonomy, or industry-analysis modules change.  
Owner review needed: No  
Split/index status: Indexed in implementation/reference-library-index.md  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->


## 1. Purpose

This framework defines the professional reference playbook for investment-oriented sector and industry analysis. It is the long-form reference behind the Sector & Industry Analysis Agent and the Sector & Industry Analysis Method.

The objective is to form a practical investment understanding of a sector: how it works, how it makes money, what drives it, where value is created, who captures profit, who loses, what risks the market may underestimate, what is already priced in, and which metrics should be monitored.

The analysis should follow a Pareto principle. Focus on the small set of factors that explain most of the investment relevance. Include only information that affects growth, margins, ROIC, risk, valuation, competitive advantage, catalysts, public-market investability, or the investment conclusion.

## 2. Core Questions

Every sector analysis should answer eight core questions:

1. What is this sector, and how does it make money?
2. Is the market growing, stagnating, or shrinking?
3. Is growth structural, cyclical, temporary, or mixed?
4. Where in the value chain is the main profit pool?
5. Who are the key players, and who is gaining or losing share?
6. Which 3–5 drivers actually move the sector?
7. Is the sector cheap, fair, expensive, or too uncertain relative to business quality?
8. Which 3–5 metrics will show whether the thesis is working or breaking?

Other details should be added only when they help answer these questions.

## 3. Sector Decision Card Template

Use qualitative labels, not numeric scores.

```text
Sector Attractiveness: Attractive / Neutral / Weak / Too Uncertain
Growth Quality: Structural / Cyclical / Temporary / Mixed
Profit Pool Clarity: High / Medium / Low
Valuation Context: Attractive / Fair / Expensive / Too Uncertain
Risk Level: Low / Medium / High
Confidence: High / Medium / Low
Further Work: Deep Dive / Watch / Avoid / Run Structural Winners / Run Equity Deep Dive
```

The decision card is not a buy/sell recommendation. It is a sector-level diagnostic summary.

## 4. Scope and Boundaries

Define the sector before analyzing it.

Cover:

- what is included;
- what is excluded;
- geography;
- investment horizon;
- relevant customer segment;
- whether the topic is an industry, sector, or broad theme;
- whether a subsector map is required.

Definitions:

```text
Industry = defined business activity with similar products, customers, and economics.
Sector = broader grouping that may contain multiple industries.
Theme = cross-sector driver or narrative.
```

If the user asks about a broad theme such as AI, energy transition, or robotics, first define practical boundaries and map the major subsectors. Do not blend different business models into one conclusion when economics, valuation, risks, or drivers differ.

## 5. Evidence Requirements

### 5.1 Evidence Plan

Standalone sector analysis should begin with an Evidence Plan.

Required categories:

- market size / growth;
- segmentation / subsectors;
- value chain / profit pool;
- key players / market share;
- sector economics / margin / ROIC;
- supply, demand, and capacity where relevant;
- valuation context;
- catalysts and risks;
- monitoring metrics.

For each category, define preferred source types, freshness expectations, why the data matters, and whether proxy data is acceptable.

### 5.2 Advisory Source Notes

Canonical evidence authority: `implementation/04-evidence-layer.md` governs evidence readiness and source authority. This section provides advisory sector/industry source examples only.

Priority sources:

1. SEC EDGAR and regulatory filings.
2. Company annual reports, 10-K, 20-F, 10-Q, quarterly reports, and regulatory filings.
3. Company investor relations, presentations, earnings releases, and transcripts.
4. Government statistics and regulators.
5. Industry associations.
6. ETF / index providers where sector exposure context matters.
7. Reputable public industry reports.
8. Reputable financial media.
9. Company TAM slides only as low-confidence unless corroborated.

Paid data sources should not be assumed unless the user provides access.

### 5.3 Anti-Hallucination Rules

- No verified source means no factual claim.
- Market size and growth data require source, date, and reliability note.
- TAM estimates must be separated from realistic addressable market.
- Company claims must be checked against independent evidence where possible.
- Profit-pool claims require evidence or must be labeled as analytical inference.
- Proxies must be labeled as proxies.
- If evidence is weak, stale, or inconsistent, confidence must be reduced.
- If evidence is insufficient, “too uncertain” is an acceptable conclusion.

## 6. Sector Structure and Business Model

Describe the sector clearly and economically.

Cover:

- what the sector sells;
- who buys;
- what customers pay for;
- key products and services;
- main revenue models;
- most important 2–4 segments;
- whether the market is fragmented or consolidated;
- top players where data is available;
- adjacent markets and substitutes;
- what is outside scope.

Avoid building a deep ecosystem map unless it affects profit pool, risks, valuation, or investment conclusion.

## 7. Market Size, Growth, and TAM Discipline

Cover only decision-relevant data:

- current market size;
- TAM if reliable and relevant;
- SAM if TAM is too broad or inflated;
- SOM only if analysis begins from a specific company;
- historical growth over 3–5 years;
- forecast growth over 3–5 years;
- faster-growing segments;
- whether growth comes from volume, price, mix, M&A, cyclical recovery, or structural demand;
- source, data date, and reliability note.

Do not overbuild TAM methodology unless it changes the conclusion. Treat inflated TAM claims as narrative, not fact, unless corroborated.

## 8. Growth Quality Assessment

Classify sector dynamics into structural, cyclical, and temporary drivers.

Structural growth may come from:

- technology adoption;
- demographic change;
- infrastructure investment;
- regulation;
- penetration growth;
- customer behavior change;
- energy transition;
- digitalization;
- automation.

Cyclical factors may include:

- rates;
- GDP;
- consumer income;
- corporate capex;
- inventories;
- commodity prices;
- capacity utilization;
- credit cycle.

Temporary factors may include:

- one-time order spikes;
- pull-forward demand;
- subsidies;
- temporary shortages;
- temporary price spikes;
- news-driven hype;
- short-term narratives.

The analysis should identify whether growth is translating into margins, free cash flow, and returns on capital. Revenue growth alone is not enough.

## 9. Key Drivers and Constraints

Select only 3–5 drivers that actually move the sector.

For each driver, state:

- how it affects revenue;
- how it affects margins;
- who wins;
- who loses;
- whether the market may underestimate or overestimate it;
- which metric shows that the driver is strengthening or weakening.

Separate:

- primary vs secondary factors;
- short-term vs structural factors;
- growth drivers vs constraints;
- technology, regulatory, macro, behavioral, and supply-side drivers.

End the section by naming the drivers without which the sector thesis does not work.

## 10. Value Chain, Profit Pool, and Value Capture

Analyze only what helps determine where value is created and retained.

Cover:

- chain layers;
- upstream suppliers;
- downstream customers;
- distribution;
- critical resources;
- bottlenecks;
- dependencies;
- enabling players;
- substitutes and competing technologies;
- where revenue is created;
- where profit is retained;
- who controls the customer;
- who controls resources, technology, capacity, or distribution;
- who captures upside when the market grows;
- who bears costs without capturing profit.

Growth is not enough if the profit pool belongs to private companies, customers, suppliers, or non-investable players.

## 11. Subsector Map

Use this section when the sector is broad.

For each important subsector, cover:

- what it does;
- role in the sector;
- size and growth where reliable data exists;
- margin and capital intensity;
- cyclicality;
- key players;
- main drivers;
- main risks;
- investment interest: high / medium / low / too uncertain.

Do not mix different economics into one blended conclusion.

## 12. Competitive Structure and Key Players

Describe competitive logic without long company profiles.

Cover:

- top key players;
- leaders;
- challengers;
- enabling players;
- share gainers and losers where evidence exists;
- basis of competition: price, product, service, brand, technology, scale, distribution;
- pricing power;
- barriers to entry;
- substitution risk;
- adjacent-player disruption.

Use Porter Five Forces, SWOT, PESTEL, and lifecycle analysis as internal filters, not as large report sections.

For each key company, use no more than 2–3 sentences:

1. Why the company matters.
2. Which sector driver it depends on.
3. Main sector-level risk.

## 13. Sector Economics and Relevant Metrics

Do not use the same metrics for every industry. First identify the economic logic of the sector.

Core questions:

- Does the sector earn money through volume, price, subscription, commission, spread, utilization, capacity, assets, transactions, or mix?
- What most affects margins: scale, raw materials, wages, logistics, capacity utilization, R&D, customer acquisition cost, churn, funding cost, regulation, or competition?
- How capital-intensive is the sector?
- How quickly do investments convert into revenue and cash flow?
- Does the sector have pricing power?
- Does the sector create economic value, or only revenue growth?

Select only 3–5 key metrics for the industry.

Examples:

- Software: net revenue retention, churn, ARR growth, Rule of 40, gross margin, CAC payback, pricing power.
- Industrials: orders, backlog, book-to-bill, capacity utilization, capex, operating margin, free cash flow conversion.
- Consumer: volume versus price, same-store sales, gross margin, inventory, brand strength, channel mix.
- Banks: net interest margin, deposits, loan growth, cost of risk, CET1, ROE, price-to-book.
- Energy: commodity price, cost of supply, production volumes, reserve life, capex discipline, free cash flow, balance sheet.
- Real estate: occupancy, rent growth, cap rates, NAV, debt maturity, interest coverage, leverage.
- Telecom: ARPU, churn, subscriber growth, capex intensity, leverage, free cash flow yield.
- Semiconductors: wafer capacity, utilization, ASP, gross margin, capex cycle, inventory, design wins.
- Insurance: combined ratio, premium growth, loss ratio, investment income, reserve adequacy.
- Payments: transaction volume, take rate, active accounts, cross-border volume, fraud losses, operating leverage.

## 14. Valuation Context

Do not build a full valuation model. Provide decision-relevant context.

Cover:

- current sector multiples;
- historical range;
- premium or discount versus the broad market;
- premium or discount versus the sector’s own history;
- relevant sector-specific valuation metrics;
- whether earnings are normalized, depressed, or near cycle peak;
- whether leaders deserve premiums;
- whether cheap companies are value opportunities or structural traps;
- what the market appears to price in.

Do not conclude cheap or expensive from a multiple alone. Valuation must be tied to business quality, cycle stage, growth durability, margins, ROIC, and risk.

## 15. Public Market Investability

A sector can be attractive while the available securities are unattractive.

Analyze:

- whether the main profit pool is accessible through public companies;
- whether quality listed pure plays exist;
- whether ETFs or baskets are good or diluted proxies;
- whether the best assets are private;
- whether public companies are weak proxies;
- whether the available exposure is already crowded or expensive.

Use this conclusion explicitly when needed:

```text
Great theme, weak public-market expression.
```

## 16. Beneficiaries, Dependencies, and Second-Order Effects

Identify who benefits and who loses from changes in:

- demand;
- price;
- capacity;
- rates;
- capex;
- regulation;
- technology;
- customer behavior;
- market share;
- input costs.

Second-order effects:

- companies benefiting through suppliers, infrastructure, or distribution;
- apparent beneficiaries without pricing power;
- companies that benefit first but later face margin pressure;
- changes in one chain layer affecting economics of another layer;
- dependencies between companies, segments, and chain layers.

## 17. Risks, Catalysts, and Sector Debates

Cover only material points.

Potential opportunities:

- growth faster than expected;
- margin expansion;
- structural demand driver;
- constrained supply;
- improving pricing power;
- valuation below history;
- upward earnings revisions;
- new catalyst;
- better risk/reward in a subsector.

Potential risks:

- weaker demand;
- margin pressure;
- oversupply;
- stronger competition;
- regulatory deterioration;
- inflated valuation;
- peak earnings;
- overestimated TAM;
- temporary driver mistaken for structural growth;
- high uncertainty.

Catalysts over 3–12 months may include earnings, management guidance, EPS revisions, orders, backlog, inventory cycle, prices, rates, regulatory decisions, product launches, major contracts, capacity additions, commodity price changes, and M&A only if it can materially change the sector narrative.

Include the bull / bear debate and what must happen for each side to be right.

## 18. What the Market May Be Missing

Identify the main possible market misperception.

Potential cases:

- wrong profit-pool location;
- underappreciated bottleneck;
- overstated or understated growth durability;
- underestimated margin pressure;
- overlooked second-order beneficiaries;
- excessive focus on obvious leaders;
- failure to distinguish structural growth from cyclical recovery;
- assumption that public companies capture value when the profit pool is private or customer-owned.

## 19. What Is Already Priced In

Assess whether the sector appears to price in a weak, base, optimistic, or euphoric scenario.

Check:

- multiples versus history;
- multiples versus the broad market;
- earnings cycle stage;
- whether forward estimates already reflect growth;
- multiple-compression risk;
- growth, margin, and ROIC assumptions required by current valuation;
- what the market likely underestimates;
- what the market likely overestimates.

## 20. Investment Map

Show the ways an investor can express the sector thesis at the exposure-type level.

Possible expressions:

- sector leaders;
- challengers gaining share;
- suppliers of critical resources;
- infrastructure players;
- enabling companies;
- cyclical beneficiaries;
- defensive players;
- underappreciated second-order beneficiaries;
- ETF or basket proxies;
- companies where the good scenario is already priced in;
- companies that look cheap but have structural problems.

For each direction, state:

1. Which investment thesis it expresses.
2. Which driver it depends on.
3. Where the potential upside comes from.
4. What may already be priced in.
5. Main risk.
6. What must happen for the idea to work.
7. Whether it deserves deeper analysis.

Do not merely list tickers. Explain the causal chain:

```text
driver → profit pool → company type → valuation → risk → next action
```

## 21. Ranking Investment Directions

At the end of standalone analysis, list 3–5 most interesting investment directions inside the sector.

For each direction, include:

- thesis;
- why it matters now;
- key driver;
- potential upside source;
- main risk;
- horizon;
- confidence: high / medium / low;
- next analysis.

Do not include a direction unless the link between driver, profit pool, valuation, and catalyst is clear. If no attractive opportunities are visible, say so directly.

## 22. Anti-Thesis

Formulate the strongest bear argument against the sector.

Answer:

- What must happen for the sector to become a poor investment?
- What risk might the market underestimate?
- Where could the analyst confuse structural growth with cyclical recovery or temporary hype?
- Where could revenue growth fail to become profit growth?
- Where could the profit pool sit outside public companies?
- Where does valuation leave little margin of safety?
- Which indicator would first show that the thesis is wrong?

The anti-thesis should be a direct attack on the main thesis, not a formal risk list.

## 23. Monitoring Plan

Select 3–5 quarterly monitoring metrics.

Metrics should indicate:

- whether the thesis is working;
- whether the sector is deteriorating;
- whether structural growth is confirmed;
- whether margin pressure is emerging;
- whether key players’ competitive position is weakening;
- whether the market narrative has changed.

For each metric, include:

- source;
- monitoring frequency;
- confirming signal;
- weakening signal;
- thesis-breaking signal.

## 24. Final Investment Conclusion Template

The final standalone memo should include a concise sector-level conclusion. A useful format is eight sentences:

1. Whether the sector looks attractive, neutral, weak, or too uncertain.
2. Main reason for that conclusion.
3. Main growth or decline driver.
4. Whether growth is structural, cyclical, temporary, or mixed.
5. Where the main profit pool sits.
6. Which company types are the best beneficiaries.
7. Main risk that could break the thesis.
8. Next action: deep dive, skip, watch, wait for better entry, run Structural Winners, or analyze specific companies.

This is not a buy/sell recommendation.

## 25. Strong Reality-Test Questions

Use these questions when relevant:

1. If demand rises 20%, who earns the most?
2. If price falls 10%, who loses money first?
3. If rates stay high, who cannot finance growth?
4. If capacity becomes scarce, who has capacity?
5. If regulation tightens, who benefits from scale?
6. If technology becomes cheaper, who is cannibalized?
7. Where is the bottleneck: demand, supply, capital, technology, licenses, energy, labor, or distribution?
8. Who controls the customer?
9. Who controls the profitable chain layer?
10. Who grows with the market but does not earn attractive economics?
11. Who has high ROIC, and who only has revenue growth?
12. Which metric will first show that the thesis is breaking?
13. What is already priced in?
14. Where could the market be wrong?
15. Which 3 metrics should be monitored each quarter?

## 26. Output Templates

### 26.1 Embedded `sector_context.md`

`sector_context.md` is the canonical embedded company-workflow artifact. `industry.md` is a legacy alias only and should not be created for new runs.

```text
1. Industry Relevance to the Company
2. Sector / Industry Snapshot
3. Growth Quality and Key Drivers
4. Value Chain and Profit Pool Position
5. Competitive Structure
6. Industry Risks and Thesis Breakers
7. Valuation / Expectations Context
8. Monitoring Metrics
9. Implications for Company Analysis
10. Recommended Handoffs, if needed
```

### 26.2 Standalone `sector_industry_memo.md`

```text
1. Sector Decision Card
2. Executive View
3. Scope and Boundaries
4. Sector Structure and Business Model
5. Market Size, Growth, and Growth Quality
6. Subsector Map and Attractiveness
7. Value Chain, Profit Pool, and Value Capture
8. Key Drivers and Constraints
9. Competitive Structure and Key Players
10. Public Market Investability
11. Valuation Context
12. Risks, Anti-Thesis, and Thesis Breakers
13. Investment Directions and Next Deep Dives
14. Recommended Handoffs
15. Material Data Limitations Appendix
```

### 26.3 `sector_investment_map.md`

```text
1. Core Sector Thesis
2. Profit Pool Map
3. Subsector Priority View
4. Beneficiary Types
5. Vulnerable Areas / Avoid Zones
6. Public Market Access
7. 3–5 Investment Directions
8. Best Next Analyses
```

### 26.4 `sector_monitoring_plan.md`

```text
1. Sector Thesis to Monitor
2. 3–5 Key Monitoring Metrics
3. Source / Where to Track Each Metric
4. Frequency
5. What Confirms the Thesis
6. What Weakens or Breaks the Thesis
7. Catalyst / Event Watchlist
8. Reassessment Triggers
9. Recommended Follow-up Agents
```

### 26.5 `sector_evidence_pack.md`

```text
1. Evidence Plan
2. Source Summary
3. Market Size / Growth Evidence
4. Segmentation / Subsector Evidence
5. Value Chain / Profit Pool Evidence
6. Competitive / Key Player Evidence
7. Economics / Margin / ROIC Evidence
8. Valuation Context Evidence
9. Catalyst / Risk Evidence
10. Missing Data / Proxy Log
```

## 27. Guardrails

- Do not write a 100-page report.
- Do not omit decision-relevant analysis just to stay short.
- Do not add charts or diagrams by default.
- Do not build a deep ecosystem unless it affects profit pool, valuation, risk, or investment conclusion.
- Do not create a large M&A section unless M&A is a key sector driver.
- Do not use SWOT, Porter Five Forces, PESTEL, or lifecycle as big separate sections by default.
- Do not list every possible metric.
- Use relevant metrics for the specific industry.
- Keep tables limited and compact.
- Use qualitative labels, not numeric scoring.
- Separate facts, interpretations, and hypotheses.
- Record material data limitations.
- Do not make final buy/sell recommendations.
- Do not recommend position sizing.
- Do not treat sector attractiveness as security attractiveness.
