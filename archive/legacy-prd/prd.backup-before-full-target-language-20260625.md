# Financial Agent System — Product Requirements Document

## 1. Purpose

This project is a personal financial agent system designed to support investment decision-making across multiple asset classes.

The system should help transform raw investment questions, asset ideas, macro themes, news narratives, and market observations into structured, evidence-based investment analysis and practical decision support.

The goal is not to produce generic research papers or long sell-side style reports. The goal is to support real personal capital allocation decisions by helping answer questions such as:

- Should I invest in this company, ETF, commodity, crypto asset, or bond?
- Is this asset attractive at the current price?
- What is already priced in?
- What are the key drivers, risks, catalysts, and thesis breakers?
- What role could this asset play in a portfolio?
- What should be monitored after the analysis?
- If a major theme or event emerges, what investable opportunities could express that theme?

The system is intended for personal professional use. It should be rigorous, source-aware, and decision-oriented, but the final outputs should remain readable and useful rather than overly technical or compliance-heavy.

## 2. Language Policy

The default communication language with the user in chat is Russian unless the user requests otherwise.

All project documentation, agent definitions, workflow files, skills, prompts, reports, and generated Markdown artifacts should be written in English.

## 3. Global Writing Style Requirement

All agents must structure and write their analytical outputs in the investment-analytical style defined by the global skill:

`C:\Users\ShumeikoYe\.codex\skills\investment-analytical-style\SKILL.md`

This requirement applies to:

- specialist agent reports;
- evidence-based analytical summaries;
- Opportunity Discovery Memos;
- Investment Committee memos;
- monitoring plans;
- future agent-generated Markdown artifacts.

The style should be concise, businesslike, investment-oriented, and analytically dense. Agents should avoid conversational, generic, emotional, or “ChatGPT-like” phrasing. Each paragraph should carry useful investment information: fact, context, causal link, implication, risk, condition, or conclusion.

The style requirement does not override factual accuracy, source discipline, or uncertainty handling. Agents must preserve:

- facts;
- numbers;
- dates;
- tickers;
- source attribution;
- conditionality;
- uncertainty;
- causality;
- strength of judgment.

Agents must not use the style skill to add unsupported analysis, new facts, investment calls, caveats, or conclusions. The style is a writing and structuring standard, not a substitute for evidence or reasoning.

All agent definitions created later should explicitly reference this style requirement.

## 4. Core Product Principles

### 4.1 Decision-Oriented, Not Research-for-Research

The system should not merely collect information. It should synthesize relevant information into investment reasoning.

The final output should help the user understand:

- what matters;
- why it matters;
- what could go right;
- what could go wrong;
- what is already reflected in the price;
- where the market may be wrong;
- what should be done or monitored next.

### 4.2 Modular but Coherent

Agents should be created only when a function is reusable and meaningful. The system should avoid creating many disconnected agents without a clear workflow.

Each agent should have a clear role, scope, output format, and relationship to the overall workflow.

### 4.3 Evidence First, Analysis Second

Agents should gather relevant evidence before making conclusions.

Important factual claims should be supported by sources, metrics, or clearly stated assumptions. The system should not invent facts, figures, events, sources, links, or conclusions.

### 4.4 Internal Rigor, Reader-Friendly Outputs

The system should maintain strict evidence discipline internally, but final reports should not read like technical audit logs.

Detailed source tracking should live primarily in the evidence pack and specialist reports. The final Investment Committee memo should surface only the evidence notes, caveats, and limitations that materially affect the investment decision.

## 5. Primary Use Cases

### 5.1 Asset-First Investment Analysis

The user provides a specific asset or instrument, such as:

- an individual company;
- an ETF;
- a commodity;
- a crypto asset;
- a bond or fixed income instrument.

Examples:

- “Analyze Nvidia.”
- “Should I invest in gold?”
- “Analyze TLT.”
- “Is Bitcoin attractive on a 12-month horizon?”
- “Analyze Fabrinet as a 5-year investment.”

The system should route the request through the appropriate asset-specific and cross-functional analysis modules and produce an Investment Committee synthesis memo.

### 5.2 Theme-First Opportunity Discovery

The user provides a theme, event, narrative, macro shift, or geopolitical development and asks where investment opportunities may exist.

Examples:

- “Defense spending may expand due to rising geopolitical conflict. Where can I invest?”
- “AI power demand is increasing. What assets benefit?”
- “Oil shock risk is rising. What should I look at?”
- “Nuclear renaissance investment opportunities.”

The system should not immediately produce a buy/sell recommendation. Instead, it should produce an Opportunity Discovery Memo that maps the theme into investable opportunities.

The output should include:

- theme overview;
- transmission channels;
- value chain mapping;
- likely beneficiaries and losers;
- investable instruments;
- shortlist of candidates;
- recommended candidates for deeper asset-level analysis.


### 5.2A Structural Winners Discovery

The system should support a more focused theme / industry discovery mode for finding public-company candidates that may become long-term structural winners.

This mode is handled by the Structural Winners Discovery Agent and the Structural Winner Discovery Method.

It starts from:

- a theme or industry;
- a value-chain question;
- a similar-company pattern;
- a failed or known company contrast.

Examples:

- "Find structural winner candidates in AI power demand."
- "Find companies with an early-Vertiv-like profile."
- "Where are the hidden picks-and-shovels beneficiaries of robotics?"
- "Why did solar manufacturers fail to capture value, and where are better clean-energy bottlenecks?"

The output should not be a final buy/sell recommendation. It should produce:

- a structural winners discovery memo;
- a candidate watchlist;
- candidate tiers;
- valuation sanity checks;
- red-team risks;
- recommended next deep dives.

This mode should bridge broad theme-first opportunity discovery and full asset-level company analysis.

### 5.2B Sector / Industry Analysis

The system should support professional sector and industry analysis as both a standalone diagnostic workflow and an embedded specialist input inside company analysis.

This mode is handled by the Sector & Industry Analysis Agent and the Sector & Industry Analysis Method.

It starts from:

- a specific industry;
- a broader sector;
- a broad theme that behaves like an investment ecosystem;
- a company analysis where industry structure materially affects the thesis.

Examples:

- "Analyze the data center cooling industry."
- "Analyze AI infrastructure as an investment sector."
- "Analyze NVIDIA, including the relevant industry context."
- "Map the defense electronics sector and identify which subsectors deserve deeper work."

The output should not be a final buy/sell recommendation. It should produce:

- sector structure and business-model analysis;
- market size, growth, and growth-quality assessment;
- value-chain and profit-pool analysis;
- public-market investability assessment;
- valuation context, not a full valuation model;
- anti-thesis and thesis breakers;
- sector-level investment directions and recommended handoffs;
- monitoring metrics.

This mode should bridge asset-level company analysis, broad theme analysis, and structural winner discovery.

### 5.3 Direct Specialist Agent Calls

The user may directly call a specialist agent without running the full workflow.

Examples:

- “Macro Agent, analyze the impact of rates on gold.”
- “Valuation Agent, look only at Nvidia valuation.”
- “Risk Agent, red-team the uranium thesis.”

The system must not break when an individual agent is called directly.

Every specialist agent should be independently callable and workflow-compatible. It should be able to:

- accept a scoped request;
- ask clarifying questions if required;
- perform its analysis;
- save a Markdown report;
- follow system-wide evidence standards;
- remain compatible with the broader orchestration workflow.

## 6. Supported Asset Classes

The first version should support the following asset classes:

1. Equities
2. ETFs
3. Commodities, including oil
4. Crypto assets
5. Bonds / fixed income instruments

Rates should not be treated as a separate primary asset route at the start. Rates are a macro factor and should be handled by the Macro Agent because they influence equities, commodities, crypto, bonds, and ETFs.

## 7. ETF Treatment

ETFs should be treated as wrappers over underlying exposures, not as a single generic asset type.

The ETF workflow should include both:

1. ETF-specific analysis
2. Underlying exposure analysis

### 7.1 ETF-Specific Analysis

For ETFs, the system should collect and analyze:

- holdings;
- expense ratio;
- performance;
- issuer;
- AUM;
- ETF-specific risks;
- liquidity where relevant;
- structure and tracking considerations where relevant.

### 7.2 Underlying Exposure Routing

After identifying the ETF’s exposure, the system should route to the relevant underlying playbook:

- equity ETF → equity / sector / industry route;
- commodity ETF → commodity route;
- bond ETF → fixed income / macro / rates route;
- crypto ETF → crypto route;
- thematic ETF → theme, holdings, and industry route;
- multi-asset ETF → allocation-style route.

## 8. Intake and Routing Architecture

### 8.1 Master Intake Router

The system should have a top-level Master Intake Router.

Its purpose is not to analyze the asset or theme. Its purpose is to classify the incoming request and decide which intake route should handle it.

The Master Intake Router should classify requests into:

1. Asset-first requests
2. Theme-first requests
3. Mixed requests
4. Unclear requests

### 8.2 Classification Behavior

The Master Intake Router should classify the request automatically when the intent is clear.

If the request is unclear or ambiguous, it should ask the user a concise clarifying question.

Examples:

- “Analyze Nvidia” → Asset-first workflow.
- “Defense spending is rising — where can I invest?” → Theme-first workflow.
- “Analyze Lockheed Martin as a beneficiary of rising defense budgets” → Asset analysis with thematic context.
- Ambiguous request → ask whether the user wants specific asset analysis or opportunity discovery around a theme.

### 8.3 Asset Intake Router

For asset-first requests, the system should collect up to five key pieces of context before launching analysis.

Required intake questions:

1. Instrument / asset  
   What asset or instrument should be analyzed?

2. Decision type  
   What decision is the user trying to make? Examples: buy, hold, add, reduce, sell, compare, understand move, watchlist.

3. Investment horizon  
   What is the relevant investment horizon?

4. Current exposure / portfolio context  
   Does the user already own the asset or related exposure? Is exposure small, meaningful, large, concentrated, or indirect through ETFs/themes?

5. Primary thesis / concern / question to test  
   What is the main idea, concern, or hypothesis the analysis should test?

Output depth should not be an intake parameter in the first version. Agents should operate at one default working depth. Output profiles such as quick brief, standard memo, and deep dive may be added later.

### 8.4 Theme / Opportunity Intake Router

For theme-first requests, the system should clarify:

- the theme, event, or narrative;
- the desired investment angle;
- the relevant geography or market if applicable;
- the investment horizon if known;
- whether the user wants broad opportunity discovery or already has candidate assets in mind.

The result should be an Opportunity Discovery Memo, not an immediate final buy/sell recommendation.

## 9. Agent Architecture

The system should use a hybrid architecture with three analytical agent categories:

1. Asset-class agents
2. Opportunity / Discovery agents
3. Cross-functional agents

### 9.1 Asset-Class Agents

Initial asset-class agents:

- Equity Agent
- ETF Agent
- Commodity Agent
- Crypto Agent
- Fixed Income Agent

These agents understand the specific structure, risks, and analytical logic of each asset class.


### 9.2 Opportunity / Discovery Agents

Initial opportunity / discovery agent:

- Structural Winners Discovery Agent

The Structural Winners Discovery Agent answers:

```text
Which public companies could become long-term structural winners inside this theme, industry, or value chain?
```

It uses:

```text
Structural Winner Discovery Method
```

Core responsibilities:

- map themes and industries into value chains;
- identify bottlenecks, scarce capacity, control points, platform dynamics, mission-critical niches, and hidden second-order beneficiaries;
- build a bounded longlist of up to 30 public-company candidates;
- filter candidates into Tier 1, Tier 2, Tier 3, watch-only, and rejected groups;
- distinguish business quality from stock attractiveness;
- perform valuation sanity checks, not full valuation models;
- produce `structural_winners_memo.md` and `candidate_watchlist.md`;
- recommend next analyses such as Financial Statement Analysis, Valuation & Expectations, Risk / Red Team, or Company / Equity Deep Dive.

It does not:

- give final buy/sell recommendations;
- call any company "the next NVIDIA";
- perform full financial statement analysis;
- perform portfolio-fit analysis or position sizing;
- automatically launch downstream agents without user approval.

### 9.3 Cross-Functional Agents

Initial cross-functional agents:

- Evidence Collector Agent
- Macro Agent
- News & Catalysts Agent
- Valuation & Expectations Agent
- Risk / Red Team Agent
- Sector & Industry Analysis Agent
- Market Positioning Agent
- Technical Agent
- Portfolio Fit Agent
- Investment Committee Agent

Additional agents may be added later only if their function is reusable and does not duplicate existing responsibilities.

### 9.4 Sector & Industry Analysis Agent Role

The Sector & Industry Analysis Agent should function as a sector analyst, not a stock picker.

Its role is to identify:

- how a sector or industry makes money;
- whether growth is structural, cyclical, temporary, or mixed;
- where the sector profit pool sits;
- which subsectors and business models are most attractive;
- which key drivers, constraints, and risks matter most;
- whether public-market investors can access the main profit pool;
- what may already be priced in;
- what the market may be missing;
- what should be monitored;
- which downstream agent should run next.

It should operate in three core modes:

```text
1. Embedded Company Mode - focused industry context for a company analysis.
2. Standalone Sector Diagnostic Mode - full sector / industry analysis.
3. Broad Theme-as-Sector Mode - subsector mapping for broad themes that are not single industries.
```

It should produce `industry.md` in embedded company workflows and `sector_evidence_pack.md`, `sector_industry_memo.md`, `sector_investment_map.md`, and `sector_monitoring_plan.md` in standalone sector workflows.

It does not:

- give final buy/sell recommendations;
- perform portfolio sizing;
- perform full company financial analysis;
- build full DCF or detailed valuation models;
- analyze ETF holdings or ETF structure;
- perform broad macro regime analysis;
- perform deep news monitoring;
- use numeric scoring;
- create charts or diagrams by default.

### 9.5 Risk / Red Team Agent Role

The Risk / Red Team Agent should function as a Thesis Breaker Agent, not a generic risk-list generator.

Its role is to identify:

- how the investment thesis could fail;
- which assumptions are most fragile;
- which risks the market may be underestimating;
- what a realistic downside scenario looks like;
- which early warning indicators should be monitored;
- where the prevailing narrative may be wrong;
- what would make the investment idea invalid.

The output should help the Investment Committee Agent understand thesis fragility, downside paths, and monitoring priorities.

## 10. Evidence Architecture

### 10.0 Data Access Strategy

The system should use an open-source hybrid data access strategy with minimal APIs.

The default assumption is that the user will not manually provide source files, documents, datasets, or paid data access. The system should be able to collect required information independently from public, reliable, and accessible sources.

Paid data providers are out of scope for the first version. The system should not assume access to Bloomberg, FactSet, Refinitiv, S&P Capital IQ, paid broker research, or other premium databases unless explicitly added later.

The system may use:

- official public websites;
- company investor relations pages;
- SEC filings and other regulatory filings;
- ETF issuer websites and fact sheets;
- public PDF reports;
- public CSV, Excel, Word, HTML, or text files;
- official press releases;
- central bank and government websites;
- reputable secondary news sources;
- public APIs where they materially improve reliability or repeatability.

APIs should be used selectively, not excessively. The system should avoid requiring dozens of API integrations at the start. Public API keys may be added when useful, but the initial architecture should work through a combination of public websites, official documents, downloadable files, and a small number of high-value public APIs.

Data extraction may involve reading, downloading, parsing, or summarizing public HTML pages, PDFs, CSV files, Excel files, Word documents, regulatory filings, issuer fact sheets, and official reports.

User-provided documents are allowed as an optional future input, but they are not the default operating model.

The core rule remains:

> No verified source means no factual claim.

If a required data point cannot be found, accessed, parsed, or verified, the agent must not invent it or imply that it was checked.

### 10.0.1 Source Registry

The system should eventually include a dedicated `source_registry.md` file.

`source_registry.md` should act as the shared source-of-truth for data sources. It should define:

- allowed source categories;
- preferred sources by domain;
- source quality tier;
- access method: API, official website, PDF, CSV, HTML, filing, search, or other public file;
- freshness expectations;
- limitations;
- sources that should be avoided or treated as low-confidence.

The source registry should not replace domain evidence playbooks. It should define where data may come from, while domain evidence playbooks should define how those sources are used in each type of analysis.

The source access rule should be registry-first, not registry-only. Agents should first use `source_registry.md`. If required data is not available through the registry, they may use controlled web fallback under the source hierarchy:

1. official / primary sources first;
2. reputable secondary sources second;
3. low-confidence sources only as hypothesis, narrative, or sentiment inputs;
4. any useful new source should be recorded in the evidence pack;
5. repeated useful sources should later be considered for inclusion in `source_registry.md`.

Relationship between components:

- `source_registry.md` = where reliable data can be found;
- domain evidence playbooks = how to collect and interpret domain-specific evidence;
- Evidence Collector Agent = coordinates evidence collection using the registry and playbooks;
- specialist agents = analyze evidence and may request additional collection when needed.

### 10.1 Evidence Collector Agent

The Evidence Collector Agent should coordinate evidence collection.

Its role is to:

- determine what evidence is needed for the current request;
- call or follow the relevant domain evidence playbooks;
- create the initial evidence pack;
- timestamp evidence;
- track key sources;
- separate facts from interpretation;
- identify missing or unavailable data;
- provide a clean evidence base to specialist agents.

The Evidence Collector should not make investment decisions.

### 10.2 Domain Evidence Playbooks / Skills

The system should not rely on one giant Evidence Collector that knows every possible source in detail.

Instead, evidence gathering should be organized through domain-specific evidence playbooks or skills.

Examples:

#### Macro Evidence Playbook

Primary source categories:

- FRED;
- Federal Reserve;
- U.S. Treasury;
- BLS;
- BEA;
- central banks;
- official government statistics;
- yield curve and rates data;
- inflation and employment data;
- liquidity and credit indicators.

#### Equity Evidence Playbook

Primary source categories:

- SEC filings;
- 10-K;
- 10-Q;
- 8-K;
- company investor relations;
- earnings releases;
- earnings call transcripts;
- investor presentations;
- segment data;
- guidance.

#### ETF Evidence Playbook

Primary source categories:

- ETF issuer website;
- ETF fact sheet;
- holdings file;
- AUM data;
- expense ratio;
- index methodology;
- performance data;
- liquidity and structure information.

#### Commodity Evidence Playbook

Primary source categories may include:

- official supply/demand data;
- inventories;
- futures curve data;
- producer reports;
- government energy or commodity agencies;
- OPEC / IEA / EIA where relevant for oil;
- relevant industry bodies.

#### Crypto Evidence Playbook

Source categories may include:

- protocol documentation;
- official network data where available;
- exchange data;
- ETF flow data where relevant;
- on-chain metrics if available;
- regulatory sources;
- reputable market data providers.

#### Fixed Income Evidence Playbook

Source categories may include:

- Treasury data;
- central bank data;
- yield curves;
- credit spreads;
- inflation data;
- issuer documents;
- rating agency data where accessible;
- fund/ETF issuer data for bond funds.

#### Sentiment / Positioning Evidence Playbook

Source categories may include:

- CFTC COT data;
- ETF flows;
- fund flows;
- options data where accessible;
- volatility and skew;
- market breadth;
- reputable market commentary;
- social or narrative sources only as sentiment signals, not confirmed facts.

### 10.3 Evidence Pack

Each workflow run should create a shared `evidence_pack.md`.

Example report structure:

- `intake.md`
- `evidence_pack.md`
- specialist reports
- `investment_committee.md`

The evidence pack should contain the key factual base used by the analysis.

### 10.4 Evidence Pack Ownership

The Evidence Collector owns the evidence pack.

Specialist agents may add additional evidence, but only in clearly labeled additional evidence sections.

Simple structure:

```md
# Evidence Pack

## Core Evidence

## Additional Evidence Log

### Added by Macro Agent
- Source:
- Date accessed:
- Key fact / data point:
- Why it matters:
```

This avoids both bottlenecks and chaotic source collection.

### 10.5 Minimum Evidence Entry Format

For the first version, each evidence entry should include:

- source / link;
- date accessed;
- key fact or data point;
- why it matters.

If the evidence is a numerical metric or time-sensitive data, the entry should also include publication date and/or observation period when available.

### 10.6 Missing Data and Proxy Handling

The system should continue analysis when non-fatal data gaps exist, but it must not hide or invent missing data.

Rules:

- missing or unverified data must be recorded in `evidence_pack.md`;
- agents may use proxies only when the proxy is logically relevant;
- proxies must not be presented as the original unavailable data;
- specialist reports should note material data limitations when they affect that specialist analysis;
- the final Investment Committee memo should mention missing data or proxy limitations only when they materially affect the decision, risk, timing, sizing logic, or monitoring plan.

Examples:

- If direct ETF flow data is unavailable, AUM change may be used as a proxy only if clearly labeled.
- If current ETF AUM cannot be verified, the final memo should not include technical source caveats unless vehicle scale or liquidity materially affects the investment decision.

## 11. Source Quality and Anti-Hallucination Standard

### 11.1 General Standard

The system must follow a strict anti-hallucination policy:

- Agents must not invent facts, figures, events, sources, links, or conclusions.
- Important factual claims must be based on sources, data, or clearly stated assumptions.
- If an agent does not know, cannot find data, or has weak evidence, it must say so.
- Agents must not pretend that information is verified if it is not verified.
- Agents should separate facts from interpretation.
- Agents should check before finalizing that they have not introduced unsupported claims.

### 11.2 Facts vs Interpretations

Factual claims require evidence.

Interpretations are allowed, but they should be presented as interpretations, not as facts.

Example:

- Fact: “Revenue increased X% in FY2025 according to the company’s 10-K.”
- Interpretation: “This suggests demand remained resilient.”

### 11.3 Source Hierarchy

The system should follow a source hierarchy.

#### Tier 1 — Primary / Official Sources

Highest confidence:

- SEC filings;
- company investor relations;
- company reports;
- central banks;
- government statistics;
- ETF issuers;
- exchanges and official market data;
- original research reports if directly available.

#### Tier 2 — Reputable Secondary Sources

Useful and acceptable, but lower than primary sources:

- Reuters;
- Bloomberg;
- Financial Times;
- Wall Street Journal;
- New York Times business reporting;
- S&P Global;
- Morningstar;
- other reputable financial data or news providers.

#### Tier 2.5 — Reported Institutional Claims

This covers situations where a reputable secondary source reports a claim from a credible institution, but the original report is not directly available.

Example:

Reuters reports that Goldman Sachs raised its S&P 500 target.

These claims are allowed, but must be framed accurately:

- the reporting source must be named;
- the original institution must be named;
- the agent must not imply it reviewed the original report if it did not;
- confidence should be lower than direct primary-source evidence;
- the entire thesis should not rely solely on such claims.

Correct phrasing:

“Reuters reported that Goldman Sachs raised its S&P 500 target to X; the original Goldman report was not directly reviewed.”

#### Tier 3 — Low-Confidence / Sentiment / Narrative Sources

Examples:

- YouTube;
- podcasts;
- Substack;
- social media;
- Reddit;
- interviews;
- informal newsletters;
- user notes.

These can be used as:

- idea triggers;
- hypotheses;
- narrative signals;
- sentiment inputs.

They must not be treated as confirmed factual evidence unless corroborated by stronger sources.

### 11.4 Standard Choice

The system should use a combined standard:

- strict standards for facts;
- flexibility for interpretations;
- domain-specific requirements by agent.

Macro, equity, ETF, and fixed income analysis should generally require stronger sourcing.

Sentiment, technical, and market positioning analysis may use more flexible inputs, but must label weak inputs appropriately and avoid treating them as verified facts.

### 11.5 Silent Pre-Final Evidence Check

Every agent must run a silent pre-final evidence check before saving or finalizing its report.

The check should not be shown to the user. It should verify that:

- unsupported facts were not added;
- interpretations were not presented as facts;
- uncertainty was not strengthened beyond the evidence;
- key numbers and dates have evidence support;
- missing data was not invented;
- proxies were not presented as original data;
- source quality was respected;
- conclusions follow from the available evidence.

## 12. Freshness Requirements

Agents should use the freshest available data when freshness matters. Freshness requirements should depend on data type, not a single universal rule.

Agents should not rely on stale data if newer data is available.

For important data, agents should capture:

- publication date;
- observation date or period;
- date accessed;
- source;
- freshness limitations where relevant.

If data freshness cannot be verified, the agent should avoid overconfident conclusions.

Indicative freshness expectations:

- price and market data: latest available;
- news and catalysts: latest available relevant reporting;
- macro releases: latest official release;
- company financials: latest filing, earnings release, or company report;
- ETF holdings: latest issuer holdings file where available;
- ETF expense ratio and AUM: latest issuer fact sheet or issuer page where available;
- index methodology: latest available methodology, not necessarily daily;
- industry structure: recent enough for the investment thesis;
- narrative and sentiment sources: freshness depends on the topic and market relevance.

## 13. Output and File Structure

### 13.1 Markdown Reports

Each agent should save its output as a Markdown report.

For an asset-first workflow, an example structure may be:

```text
reports/
  NVDA/
    2026-06-23/
      intake.md
      evidence_pack.md
      macro.md
      industry.md
      company.md
      valuation_expectations.md
      news_catalysts.md
      market_positioning.md
      risk_red_team.md
      portfolio_fit.md
      investment_committee.md
```

For a theme-first workflow, an example structure may be:

```text
reports/
  themes/
    defense_spending/
      2026-06-23/
        intake.md
        evidence_pack.md
        macro_geopolitical.md
        value_chain_map.md
        opportunity_discovery.md
        candidate_shortlist.md
```

For a standalone sector / industry workflow, an example structure may be:

```text
reports/
  sectors/
    ai_infrastructure/
      2026-06-23/
        intake.md
        sector_evidence_pack.md
        sector_industry_memo.md
        sector_investment_map.md
        sector_monitoring_plan.md
```

Exact structure may evolve later.

### 13.2 Source Display Rule

Detailed source lists should live in `evidence_pack.md` and specialist reports.

The final Investment Committee memo should not list 50 sources or become a bibliography.

The final memo should include only:

- key evidence-backed findings;
- materially important caveats;
- a short “Key Evidence Notes / Limitations” section if needed.


### 13.3 Specialist Report Structure

Specialist reports should generally follow an Evidence -> Analysis -> Investment Implications structure.

The exact section names may vary by agent, but the underlying logic should remain consistent:

1. evidence / key data;
2. analysis;
3. investment implications.

Agent-specific adaptations are allowed:

- Macro: Data -> Regime -> Asset Implications;
- Valuation: Metrics -> Expectations -> Mispricing Risk;
- Risk: Risk Map -> Thesis Breakers -> Mitigants;
- ETF: Vehicle Data -> Underlying Exposure -> ETF Suitability;
- News / Catalysts: Recent Events -> Catalyst Path -> Price Relevance;
- Sector / Industry: Evidence Plan -> Sector Structure -> Profit Pool -> Investment Implications.

This structure is intended to reduce hallucination risk by separating what was found from what it means for the investment case.

## 14. Investment Committee Agent

### 14.1 Role

The Investment Committee Agent is the final synthesis layer.

It reads the specialist reports, `evidence_pack.md`, and intake context, then produces the final investment synthesis memo.

The Investment Committee Agent should synthesize, not conduct new research. It should not independently search for new data or introduce new source material that was not captured in the evidence pack or specialist reports.

If the Investment Committee Agent identifies a material evidence gap, it should limit the conclusion, recommend additional evidence collection, or suggest running another specialist/evidence step. It should not fill the gap with unsupported assumptions.

It should not simply aggregate or quote the other agents. It should think like a CIO or portfolio manager who has already reviewed the analytical work and now explains the investment case clearly.

It should not write:

- “The Macro Agent said...”
- “The Valuation Agent concluded...”

Instead, it should produce a natural synthesis:

- “The asset remains fundamentally attractive, but the current valuation already reflects much of the growth story.”
- “The thesis depends most on revenue durability, margin resilience, and a stabilization in the rates environment.”

The Investment Committee Agent must identify key tensions and trade-offs across the analysis. It should explain what supports the thesis, what works against it, which factors matter most, and how those conflicts shape the final decision.

Example:

“The long-term industry thesis is attractive, but valuation and crowded positioning reduce the margin of safety. The decision therefore depends less on whether the company is high quality and more on whether future growth can exceed already elevated expectations.”

### 14.2 Final Report Style

The final report should be an investment synthesis memo, not a technical log.

It should answer:

- What is the main investment view?
- Why might this asset be attractive?
- What could drive upside?
- What is already priced in?
- Where could the market be wrong?
- What are the key assumptions?
- What are the main risks?
- What scenarios matter?
- What catalysts should be monitored?
- What role does the asset play in the portfolio?
- What should be done next?

### 14.3 Opening Structure

The final report should begin with:

1. Investment View  
   A concise, human-readable summary of the investment case, attractiveness, and main trade-off.

2. Action Box  
   A compact summary containing:

   - suggested action;
   - conviction;
   - horizon;
   - portfolio role;
   - main reason.

The action should not be a simplistic “buy 3% and get rich” style recommendation. It should be practical and conditional.

### 14.4 Recommended Final Memo Sections

The final memo should generally include:

1. Investment View
2. Action Box
3. Core Investment Thesis
4. 3–5 Thesis Pillars
5. What Is Priced In
6. Where the Market May Be Wrong
7. Key Drivers and Sensitivities
8. Bull / Base / Bear Cases
9. Risks and Thesis Breakers
10. Catalysts and Monitoring Plan
11. Portfolio Role
12. Next Steps
13. Key Evidence Notes / Limitations

### 14.5 Decision Style

The Investment Committee Agent should provide a decision with conditions.

It should not only say:

- buy;
- sell;
- avoid.

It should explain under what conditions the idea is attractive or unattractive.

Example style:

“The company appears attractive on a five-year horizon because of its role in a structurally growing supply chain and strong fundamentals. However, the current valuation already reflects meaningful optimism, and higher rates may pressure multiples. This argues against aggressive buying at current levels. A phased entry or watchlist approach may be more appropriate unless valuation improves or fundamentals continue to surprise positively.”

### 14.6 Condition-Based Action Plan

The final memo should include:

- what to do now;
- when to buy or add;
- when to wait;
- when to avoid or reduce;
- what indicators to monitor;
- what would change the view.

The system should avoid false precision in portfolio sizing unless the user explicitly provides full portfolio context and requests position sizing.

## 15. Monitoring Plan

The first version should not include a separate automated Thesis Tracker or Monitoring Agent.

However, every final Investment Committee memo should include a Monitoring Plan.

The Monitoring Plan should capture:

- key thesis variables;
- catalysts;
- thesis breakers;
- reassessment triggers;
- what new information could strengthen or weaken the thesis;
- when the thesis should be revisited.

Examples of monitoring variables:

- revenue growth;
- margins;
- valuation multiple;
- rates;
- liquidity;
- ETF flows;
- oil price;
- defense budgets;
- crypto regulation;
- supply/demand balance;
- credit spreads;
- central bank policy.

This creates “living thesis hooks” for future versions of the system, where a Thesis Tracker, Catalyst Monitor, Portfolio Watchlist Agent, or Macro Monitor may be added.

## 16. Theme-First Workflow Output

The Theme-first workflow should produce an Opportunity Discovery Memo.

It should not immediately produce a final buy/sell recommendation.

The Opportunity Discovery Memo should include:

- theme overview;
- why the theme matters;
- transmission channels;
- value chain map;
- beneficiaries and losers;
- relevant asset classes;
- investable instruments;
- ETFs, companies, commodities, bonds, or crypto assets where relevant;
- shortlist of candidates;
- risks and uncertainties;
- recommended next asset-level deep dives.

The purpose is to narrow a broad theme into investable candidates.


### 16.1 Structural Winners Discovery Output

When the user asks for future structural winners, hidden beneficiaries, picks-and-shovels candidates, or similar-company discovery inside a theme or industry, the Theme-first workflow may route to the Structural Winners Discovery Agent.

The Structural Winners Discovery Agent should produce:

```text
structural_winners_memo.md
candidate_watchlist.md
```

The output should include:

- plain-language summary;
- theme / industry interpretation;
- why now;
- value-chain map;
- bottlenecks and control points;
- hidden / second-order beneficiaries;
- longlist up to 30 companies;
- filtered shortlist;
- candidate tiers and cards;
- valuation sanity check;
- what the market may be missing;
- what may already be priced in;
- false positives / traps;
- red-team and disruption risks;
- recommended next analysis.

The output should remain readable and should not be dominated by tables. It should not produce a final buy/sell recommendation.

### 16.2 Sector / Industry Diagnostic Output

When the user asks to analyze a sector, industry, or broad theme-as-sector, the workflow may route to the Sector & Industry Analysis Agent.

The Sector & Industry Analysis Agent should produce:

```text
sector_evidence_pack.md
sector_industry_memo.md
sector_investment_map.md
sector_monitoring_plan.md
```

For embedded company analysis, it should produce:

```text
industry.md
```

The standalone output should include:

- sector decision card;
- scope and boundaries;
- sector structure and business model;
- market size, growth, and growth quality;
- subsector map and attractiveness, if relevant;
- value chain, profit pool, and value capture;
- key drivers and constraints;
- competitive structure and key players;
- public-market investability;
- valuation context;
- what is already priced in;
- what the market may be missing;
- risks, anti-thesis, and thesis breakers;
- investment directions and next deep dives;
- recommended handoffs;
- monitoring metrics.

The output should be memo-first and table-light. It should not produce charts or diagrams by default and should not give a final buy/sell recommendation.

## 17. Future Extensions

Potential future additions:

- Thesis Tracker Agent
- Catalyst Monitoring Agent
- Portfolio Watchlist Agent
- Macro Monitor
- Automated report refreshes
- Output depth profiles: quick, standard, deep-dive
- Structured JSON outputs in addition to Markdown
- Scoring frameworks
- More formal valuation models
- GitHub-based versioning workflow
- Automated block diagrams and workflow maps

These are not required in the first version but should remain architecturally possible.

## 18. Current Open Design Questions

The following topics still need further discussion:

1. Detailed responsibilities of each asset-class agent.
2. Detailed responsibilities of each cross-functional agent.
3. Exact agent file format based on official OpenAI Codex documentation.
4. Exact remaining skill structure and which additional skills should be created beyond already designed skills.
5. Exact `AGENTS.md` structure.
6. Exact `workflow.md` structure.
7. Report naming conventions.
8. Whether reports should eventually include machine-readable summaries.
9. How detailed the Valuation & Expectations Agent should be.
10. How to design the Portfolio Fit Agent.
11. How to handle comparisons between multiple candidate assets.
12. How to represent workflows visually using block diagrams.

## 19. Non-Goals for the First Version

The first version should not attempt to:

- automate all monitoring;
- produce perfect portfolio allocation percentages;
- create a full institutional risk system;
- build a trading system;
- create a 50-page research report by default;
- treat weak narrative sources as verified facts;
- force every output into rigid scoring;
- make the final memo overly technical with long source lists.

## 20. Working Summary

The system should function as a modular, evidence-aware, multi-asset investment research and decision-support system.

It should support both:

- asset-first analysis;
- theme-first opportunity discovery;
- sector and industry diagnostic analysis;
- structural winners discovery inside themes, industries, and value chains.

It should use:

- a Master Intake Router;
- asset and theme intake routes;
- hybrid asset-class, opportunity / discovery, and cross-functional agents;
- an Evidence Collector with domain evidence playbooks;
- Markdown-based report artifacts;
- Sector & Industry Analysis Agent and Sector & Industry Analysis Method for sector diagnostics;
- Structural Winners Discovery Agent and Structural Winner Discovery Method for candidate discovery;
- an Investment Committee Agent for final synthesis.

The final user-facing output should read like a thoughtful investment professional explaining the case clearly, not like a raw dump of agent outputs or a technical evidence audit.

## Global Skills Requirement — Analytical Style and Language Policy

All future agents, skills, workflows, report templates, and user-facing summaries should follow two global skills when applicable:

1. Investment analytical writing style:

```text
C:\Users\ShumeikoYe\.codex\skills\investment-analytical-style\SKILL.md
```

Use this skill to keep analytical outputs concise, investment-oriented, businesslike, evidence-aware, and free of generic or overly conversational phrasing.

2. Language policy and Russian adaptation:

```text
C:\Users\ShumeikoYe\.codex\skills\language-policy\SKILL.md
```

Use this skill when user-facing communication, summaries, or translated outputs need to follow the project language policy. Default chat communication with the user is Russian, while project documentation, agent definitions, skill files, references, workflows, report artifacts, and Markdown deliverables should be written in English unless explicitly requested otherwise.

These two skills are global presentation and language standards. They do not replace evidence collection, reasoning, source discipline, or domain-specific analytical methods.

For Market Intelligence outputs, concise investor takeaways are allowed when they remain factual and driver-aware rather than becoming deep Market Sense interpretation.

Example acceptable style:

```text
Investor takeaway: A lower oil risk premium reduces near-term inflation pressure and can support bonds, consumer sectors, and airlines, while pressuring energy equities and reducing demand for defensive hedges.
```

This type of statement is allowed as concise market relevance. It should not become an unsupported final investment recommendation or a deep driver-dominance conclusion.
