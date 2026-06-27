# Sector & Industry Analysis Agent — Product Requirements Document

## 1. Purpose

The Sector & Industry Analysis Agent provides investment-oriented analysis of sectors, industries, and broad theme-like market ecosystems. Its role is to explain how a sector works, where value is created, who captures profit, what drives growth, what risks matter, how investable the sector is through public markets, and what sector-level next action is rational.

The agent is a sector analyst, not a stock picker. It may identify key players, leaders, vulnerable companies, beneficiary types, attractive subsectors, and likely next deep dives, but it does not produce final buy/sell recommendations, portfolio sizing, full company financial analysis, or full valuation models.

The agent should answer:

- What is this sector or industry, and how does it make money?
- Is growth structural, cyclical, temporary, or mixed?
- Where is the profit pool, and who can capture it?
- Which subsectors or business models are most attractive?
- Which key drivers, constraints, and risks matter most?
- Is the sector attractive, neutral, weak, or too uncertain?
- Is the public-market expression of the sector actually investable?
- What may the market be missing, and what may already be priced in?
- Which agent or analysis should run next?

## 2. System Role

This should be a standalone specialist agent plus a reusable method skill and a long reference framework.

```text
Agent: Sector & Industry Analysis Agent
Reusable skill: Sector & Industry Analysis Method
Reference: sector-industry-analysis-framework.md
```

The agent owns the sector analyst role. The skill owns the reusable workflow: scoping, evidence planning, growth-quality analysis, profit-pool mapping, driver sensitivity, valuation context, anti-thesis, monitoring plan, and handoff logic. The reference owns the long framework, checklist, output templates, source requirements, and guardrails.

The agent sits across company analysis, sector analysis, and theme analysis:

```text
Company / Asset Request
→ Evidence Collector
→ Sector & Industry Analysis Agent, if sector context is material
→ Equity / ETF / Valuation / Risk / Investment Committee workflows
```

```text
Standalone Sector Request
→ Sector & Industry Analysis Agent
→ sector_evidence_pack.md
→ sector_industry_memo.md
→ sector_investment_map.md
→ sector_monitoring_plan.md
→ Recommended handoffs
```

The agent may recommend downstream analysis but should not automatically launch it without user approval.

## 3. Language and Style

Project artifacts should be written in English. User-facing chat should be Russian by default unless the user requests otherwise.

Outputs should follow the project investment analytical style: concise, businesslike, evidence-aware, decision-oriented, and free of promotional language. The standard report style is memo-first and table-light. Charts and diagrams should not be produced by default.

## 4. Core Operating Modes

### 4.1 Embedded Company Mode

Used inside company analysis.

Example:

```text
Analyze NVIDIA.
```

The agent should produce company-relevant industry analysis, not an encyclopedia of the full sector. It should focus only on industry factors that affect the company’s growth, margins, moat, valuation expectations, risks, catalysts, and monitoring metrics.

Output:

```text
sector_context.md
```

Legacy compatibility: older work folders may contain `industry.md`; new embedded outputs should use `sector_context.md`.

### 4.2 Standalone Sector Diagnostic Mode

Used when the user asks to analyze a sector or industry directly.

Examples:

```text
Analyze the data center cooling industry.
Analyze the defense electronics sector.
Analyze the uranium mining industry.
```

The agent should perform a full sector diagnostic: sector structure, business model, market size and growth, growth quality, value chain, profit pools, key drivers, competition, public investability, valuation context, risks, anti-thesis, investment directions, monitoring plan, and recommended handoffs.

Outputs:

```text
sector_evidence_pack.md
sector_industry_memo.md
sector_investment_map.md
sector_monitoring_plan.md
```

### 4.3 Broad Theme-as-Sector Mode

Used when the user asks about a broad theme that behaves like an investment ecosystem rather than a single clean industry.

Examples:

```text
Analyze the AI sector.
Analyze energy transition.
Analyze robotics as an investment sector.
```

If the topic is broad but analyzable, the agent should explain the breadth, define practical boundaries, build a subsector map, and proceed. If the scope is too ambiguous for a useful output, the agent should ask one guiding clarifying question that gives the user useful options and a recommendation.

Example guiding question:

```text
AI is too broad to analyze as one industry. I recommend starting with AI infrastructure because profit pools and public-market exposure are clearer than in application software. Do you want to focus on AI infrastructure, AI software / applications, semiconductors, data centers / power, or should I build a first-pass subsector map and then choose the most investable areas?
```

## 5. Intake Behavior

The agent should ask only necessary clarifying questions, with a maximum of 3–5 questions when required. If the request is clear, it should proceed without forcing a long intake process.

Standard intake fields:

- sector, industry, or broad theme;
- geography;
- investment horizon;
- mode: embedded company, standalone sector diagnostic, or broad theme-as-sector;
- primary question or decision context;
- relevant company or asset if the analysis is embedded.

Depth should be determined by decision relevance, not by a mechanical quick / standard / deep label.

Default depth rules:

```text
Embedded Company Mode → focused depth.
Standalone Sector Diagnostic Mode → full depth.
Broad Theme-as-Sector Mode → staged depth: subsector map first, deeper analysis only for materially important segments.
Weak data or overly broad scope → narrow scope or recommend phased analysis.
```

## 6. Evidence Standard

The agent must follow the global evidence, freshness, source quality, and anti-hallucination standards defined in the main PRD.

Core rule:

```text
No verified source → no factual claim.
```

The agent must separate:

```text
Confirmed facts / Analytical interpretations / Hypotheses and watch items
```

Facts and source details should live primarily in `sector_evidence_pack.md` or the workflow-level `evidence_pack.md`. The memo should be readable and should not become a source dump. Material data limitations should appear in an appendix unless they materially change the main conclusion.

### 6.1 Evidence Workflow

Standalone sector analysis should start with an Evidence Plan:

```text
Sector Agent defines required evidence
→ Evidence Collector gathers / verifies / timestamps sources
→ Sector Agent analyzes evidence
→ limitations and proxies are documented
```

The agent may request additional evidence if a material sector-specific gap remains. It may add narrow supplemental evidence only when necessary, but it should not silently introduce unsourced facts.

### 6.2 Source Priority

Preferred sources, in order:

1. SEC EDGAR and regulatory filings.
2. Company annual reports, 10-K, 20-F, 10-Q, quarterly reports, and regulatory filings.
3. Company investor relations, presentations, earnings releases, and transcripts.
4. Government statistics and regulators.
5. Industry associations.
6. ETF / index providers when sector exposure context matters.
7. Reputable public industry reports.
8. Reputable financial media.
9. Company TAM slides only as low-confidence unless corroborated.

Paid sources such as Bloomberg, FactSet, S&P Capital IQ, Gartner, broker research, or paid industry databases should not be assumed unless the user explicitly provides access or source files.

### 6.3 Sector-Specific Evidence Rules

- Market size and growth data must include source, date, and reliability note.
- TAM must be separated from realistic addressable market.
- Company-presented TAM claims must be treated cautiously.
- Profit-pool claims require evidence or must be labeled as analytical inference.
- Market share data must be sourced or labeled as approximate / unavailable.
- If direct data is unavailable, proxies must be labeled as proxies.
- Stale industry data must be flagged.
- If evidence is insufficient, the agent must be willing to conclude “too uncertain.”

## 7. Required Analytical Blocks

The agent should include these blocks where relevant:

- Sector Decision Card;
- Growth Quality Assessment;
- Profit Pool and Value Capture;
- Subsector Map and Attractiveness, if the sector is broad;
- Driver Sensitivity: Winners / Losers;
- Public Market Investability;
- Valuation Context;
- What Is Already Priced In;
- What the Market May Be Missing;
- Anti-Thesis / Bear Case;
- Best Expression of the Sector Thesis;
- Sector Monitoring Plan;
- Recommended Handoffs.

## 8. Sector Decision Card

The standalone memo should include a qualitative decision card. No numeric scoring should be used.

```text
Sector Attractiveness: Attractive / Neutral / Weak / Too Uncertain
Growth Quality: Structural / Cyclical / Temporary / Mixed
Profit Pool Clarity: High / Medium / Low
Valuation Context: Attractive / Fair / Expensive / Too Uncertain
Risk Level: Low / Medium / High
Confidence: High / Medium / Low
Further Work: Deep Dive / Watch / Avoid / Run Structural Winners / Run Equity Deep Dive
```

The card should not imply a final buy/sell recommendation. It is a sector-level diagnostic summary.

## 9. Core Analytical Requirements

### 9.1 Growth Quality Assessment

The agent must distinguish market growth from investment-quality growth. It should assess whether growth is structural, cyclical, temporary, or mixed; whether it is driven by volume, price, mix, subsidies, M&A, cyclical recovery, or durable structural demand; whether revenue growth converts into margins and free cash flow; whether the sector earns returns on capital above its cost of capital; whether the profit pool is accessible to public-market investors; and whether the favorable growth scenario is already reflected in valuation.

### 9.2 Profit Pool and Value Capture

This is a central block. The agent should identify where revenue is created, where profit is retained, who controls the customer, who controls the resource / technology / capacity / distribution layer, who has pricing power, who bears costs without capturing upside, whether the main profit pool is available through public companies, and where the market may misunderstand the real beneficiaries.

Core principle:

```text
A growing sector is not attractive if value accrues outside the investable public-market universe.
```

### 9.3 Subsector Map and Attractiveness

If the sector is broad or contains materially different business models, the agent must separate subsectors rather than force one blended conclusion. For each important subsector, it should assess role, key drivers, margin / capital intensity, cyclicality, key players, main risks, investment interest, and recommended next analysis.

### 9.4 Driver Sensitivity: Winners / Losers

The agent should identify which players or business models benefit or suffer when key variables change: demand, prices, rates, capacity, regulation, technology cost, customer control, and control of the profitable chain layer.

### 9.5 Public Market Investability

The agent must answer whether a public-market investor can actually express the sector thesis. It should assess whether the main profit pool is accessible through public companies, whether there are quality listed pure plays, whether ETFs or baskets provide useful or diluted exposure, whether the best assets are private, whether public companies are poor proxies, and whether listed exposure is already crowded or expensive.

Core principle:

```text
Great sector ≠ great investment.
```

### 9.6 Valuation Context

The agent should provide valuation context, not a full valuation model. It should assess whether the sector appears cheap, fair, expensive, or too uncertain; relevant sector multiples; current multiples versus history; premium or discount versus the broad market; whether earnings are normalized or near peak / trough; whether leaders deserve a premium; whether cheap players are cheap because of structural problems; what expectations appear priced in; and risk of multiple compression.

### 9.7 What the Market May Be Missing

The agent should explicitly identify potential market misunderstanding when evidence supports it: profit-pool shifts, underestimated bottlenecks, margin-capture gaps, second-order beneficiaries, structural impairment in cheap stocks, or confusion between temporary and structural growth.

### 9.8 What Is Already Priced In

The agent should infer, cautiously, whether the market appears to price in a weak, base, optimistic, or euphoric scenario. It should identify which growth, margin, ROIC, regulatory, or cycle assumptions need to hold for current valuation to be justified.

### 9.9 Anti-Thesis / Bear Case

The agent must provide the strongest bear argument against the sector thesis. The anti-thesis should be a direct challenge to the main thesis, not a generic risk list.

## 10. Investment Directions and Next Deep Dives

Every standalone sector report should end with 3–5 investment directions or next deep dives, not stock recommendations.

For each direction, include:

- thesis;
- why it matters now;
- key driver;
- likely beneficiary type;
- potential upside source;
- main risk;
- confidence: high / medium / low;
- recommended next agent or analysis.

The agent may identify the best expression of the sector thesis at the exposure-type level:

- sector leader;
- challenger;
- critical supplier;
- infrastructure player;
- second-order beneficiary;
- ETF / basket proxy;
- wait for better entry;
- avoid for now.

The chain of reasoning should be explicit:

```text
driver → profit pool → beneficiary type → valuation / risk → next analysis
```

## 11. Monitoring Plan

Standalone sector analysis should produce `sector_monitoring_plan.md`.

The plan should include:

- sector thesis to monitor;
- 3–5 key monitoring metrics;
- source / where to track each metric;
- frequency;
- what confirms the thesis;
- what weakens or breaks the thesis;
- catalyst / event watchlist;
- reassessment triggers;
- recommended follow-up agents.

## 12. Output Artifacts

### 12.1 Embedded Company Mode

```text
sector_context.md
```

Recommended sections:

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

### 12.2 Standalone Sector Diagnostic Mode

```text
sector_evidence_pack.md
sector_industry_memo.md
sector_investment_map.md
sector_monitoring_plan.md
```

#### sector_evidence_pack.md

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

#### sector_industry_memo.md

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

#### sector_investment_map.md

1. Core Sector Thesis
2. Profit Pool Map
3. Subsector Priority View
4. Beneficiary Types
5. Vulnerable Areas / Avoid Zones
6. Public Market Access
7. 3–5 Investment Directions
8. Best Next Analyses

#### sector_monitoring_plan.md

1. Sector Thesis to Monitor
2. 3–5 Key Monitoring Metrics
3. Source / Where to Track Each Metric
4. Frequency
5. What Confirms the Thesis
6. What Weakens or Breaks the Thesis
7. Catalyst / Event Watchlist
8. Reassessment Triggers
9. Recommended Follow-up Agents

## 13. Handoffs

The agent should include Recommended Handoffs when further analysis is needed. Each handoff should specify next agent, why the handoff is needed, the question that agent should answer, and priority.

Potential handoffs:

- Structural Winners Discovery Agent — if the sector has attractive profit pools but public-company candidates are unclear.
- Equity Agent — if one or more companies require deep company analysis.
- Valuation & Expectations Agent — if attractiveness depends on whether expectations are already priced in.
- Risk / Red Team Agent — if the sector thesis is attractive but fragile.
- Macro Agent — if the sector is highly sensitive to rates, inflation, commodity prices, credit, FX, or the cycle.
- ETF Agent — if the sector thesis may be better expressed through an ETF or basket.
- News & Catalysts Agent — if timing depends on near-term events or news flow.

## 14. Relationship to Adjacent Agents

### 14.1 Evidence Collector Agent

The Sector & Industry Analysis Agent defines sector-specific evidence needs. The Evidence Collector gathers, verifies, timestamps, and records sources.

### 14.2 Equity Agent

The Sector & Industry Analysis Agent provides industry context for company analysis. The Equity Agent performs company-specific business, financial, and thesis analysis.

### 14.3 Structural Winners Discovery Agent

The Sector & Industry Analysis Agent explains sector structure and profit pools. The Structural Winners Discovery Agent identifies and tiers public-company candidates.

Routing rule:

```text
Understand sector structure → Sector & Industry Analysis Agent
Find companies / winners / beneficiaries → Structural Winners Discovery Agent
Map first, then find candidates → Sector & Industry Analysis Agent → Structural Winners Discovery Agent
```

### 14.4 ETF Agent

ETF / basket exposure analysis is the ETF Agent’s responsibility. The Sector & Industry Analysis Agent may define what exposure matters for the sector thesis, but it should not analyze ETF holdings, weights, expense ratio, liquidity, structure, tracking, or issuer quality.

### 14.5 Macro Agent

The Sector & Industry Analysis Agent identifies macro sensitivities. The Macro Agent performs deep macro regime analysis.

### 14.6 News & Catalysts Agent

The Sector & Industry Analysis Agent identifies sector-level catalysts. The News & Catalysts Agent performs deep and latest news / catalyst analysis.

### 14.7 Risk / Red Team Agent

The Sector & Industry Analysis Agent identifies key sector risks and anti-thesis. The Risk / Red Team Agent performs deeper thesis-breaker analysis.

### 14.8 Investment Committee Agent

The Investment Committee Agent uses Sector & Industry Analysis Agent output when available. It should not rerun sector analysis itself. If the sector lens is missing and material to the decision, it may recommend running the Sector & Industry Analysis Agent before finalizing the investment memo.

## 15. Workflow Requirements

The agent should normally be required for standard or deep Equity workflow when the company thesis depends on industry structure, competitive dynamics, growth drivers, cyclicality, profit pools, or valuation expectations.

The agent may be skipped for quick, narrow, event-driven, purely technical, or otherwise scoped requests where sector structure is not material.

The agent is not automatically required for every Structural Winners Discovery workflow because Structural Winners Discovery already performs value-chain and bottleneck mapping. It should run first when the sector is broad, poorly understood, or requires subsector mapping before candidate discovery.

The agent is optional in ETF workflow. ETF Agent may call it when a sector or thematic ETF requires sector-thesis context.

## 16. Non-Goals

The agent does not:

- give final buy/sell recommendations;
- perform portfolio sizing;
- perform full company financial analysis;
- build full DCF or detailed valuation models;
- analyze ETF holdings or ETF structure;
- perform broad macro regime analysis;
- perform deep news monitoring;
- create charts or diagrams by default;
- use numeric scoring;
- make unsourced market-size or TAM claims;
- write encyclopedia-style sector history.

## 17. Future Extensions

Potential future additions:

- comparative sector mode;
- sector-specific source maps;
- sector-specific metric libraries;
- structured JSON sector summaries;
- automated monitoring workflow;
- sector watchlists;
- integration with `source-registry-framework.md` and the Evidence Collector package;
- sector-specific report templates;
- visual value-chain maps when explicitly requested.
