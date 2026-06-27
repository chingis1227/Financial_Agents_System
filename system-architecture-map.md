# Financial Agent System — System Architecture Map

## 1. Purpose of This Document

This document defines the conceptual architecture of the Financial Agent System for the design-to-implementation transition.

It explains how agents, skills, references, workflows, and reports relate to each other. It is intended to reduce architectural confusion and provide a stable map for later PRDs, agent charters, skill specifications, workflow documents, and report templates.

This document is not an implementation file. It does not create agents or skills. It is the architecture-level source of truth for how active agents, skills, references, workflows, and report artifacts connect to the product-level PRD.

## 1A. Documentation Integration Rule

During the system build phase, no new agent, skill, workflow, reference, or report-template document should remain disconnected from the architecture map.

After creating or materially changing any design document, the system documentation must be checked and updated as needed:

1. Add the new agent, skill, reference, workflow, or report artifact to the relevant architecture section.
2. Update ownership boundaries if the new document changes who owns an analytical block.
3. Update agent-to-skill relationships and handoff rules.
4. Update workflow sequencing if the new document changes orchestration.
5. Update report artifact names and folder structures if output naming changes.
6. Remove stale references and revise open architecture questions that have been resolved.
7. Check that `prd.md` and `system-architecture-map.md` remain aligned.
8. Add the exact filename to the active documentation registry in `prd.md` or explicitly classify it as archive, scratch, or non-active support material.

Design work is not considered complete until the new document is connected back to the system map and the active documentation registry.

## 2. Core Mental Model

The system uses the following conceptual layers:

```text
Agent = role / responsible analyst
Skill = reusable method / workflow instructions
Reference = long playbook, checklist, template, or source guide
Workflow = orchestration logic / when to run whom
Report = output artifact
```

Agents do not physically contain skills. Agents use skills.

Skills are not exclusive to one agent. A skill can be shared by multiple agents when the methodology is reusable.

References are detailed supporting materials used by skills, such as long checklists, domain playbooks, templates, source lists, or analytical frameworks.

## 3. Relationship Between Agents, Skills, and References

### 3.1 Agent

An agent defines responsibility, scope, boundaries, and expected output.

Examples:

- Equity Agent
- Valuation & Expectations Agent
- Risk / Red Team Agent
- News & Catalysts Agent
- Investment Committee Agent

An agent answers the question:

> Who is responsible for this analytical task?

### 3.2 Skill

A skill defines a reusable method for doing a type of work.

Examples:

- equity-company-analysis
- financial-statement-analysis
- valuation-expectations
- risk-red-team
- news-catalysts
- market-positioning-method
- investment-committee-synthesis

A skill answers the question:

> How should this type of analysis be done?

### 3.3 Reference

A reference contains detailed supporting material that should not be embedded directly into an agent definition.

Examples:

- equity-company-analysis-framework.md
- valuation-expectations-framework.md
- commodity-analysis-framework.md
- commodity-family-playbooks.md
- risk-red-team-framework.md
- source-registry-framework.md
- investment_committee_template.md
- full-agent-system-build-roadmap.md

A reference answers the question:

> What detailed checklist, template, or source guide supports the skill?

### 3.4 Workflow

A workflow defines the orchestration sequence.

Examples:

- asset-first workflow
- equity-deep-dive-workflow.md
- theme-first workflow
- direct specialist call workflow
- investment committee synthesis workflow

A workflow answers the question:

> When should each agent or skill be used, and in what order?

### 3.5 Report

A report is the output artifact created by an agent or workflow.

Examples:

- evidence_pack.md
- equity_company_analysis.md
- financial_statement_analysis.md
- valuation_expectations.md
- risk_red_team.md
- news_catalysts.md
- market_positioning.md
- final_investment_memo.md

A report answers the question:

> What was produced and saved from the analysis?

### 3.6 User-Facing Report Standard

Reports are not internal agent logs. They are the user-facing analytical artifacts of the system.

Every user-facing report should read like a clear professional investment memo: structured, evidence-aware, natural, and decision-useful. The reader should be able to understand the topic, the key facts, the analytical tensions, and the practical implication without reading every underlying handoff.

Agents may use structured handoffs, appendices, and evidence files internally, but the main report narrative should synthesize the analysis in natural investment language. It should not default to mechanical phrasing such as “Agent A concluded...” or “Agent B said...” unless explicit traceability is required.

The expected report style is:

- coherent narrative, not disconnected findings;
- enough context to let the reader enter the topic quickly;
- clear distinction between fact, interpretation, uncertainty, and judgment;
- concise but substantive explanation of valuation, risk, macro, business quality, market expectations, catalysts, and portfolio implications where relevant;
- no generic AI phrasing, filler, or robotic template language;
- no dry one-line conclusion when the request requires real analytical immersion.

This standard applies to all specialist reports, final Investment Committee memos, discovery outputs, monitoring plans, and future Markdown artifacts.

### 3.7 Reader Layer and Verification Layer

The system separates every serious analytical output into two conceptual layers:

```text
Reader Layer = the main report that explains the investment picture clearly.
Verification Layer = evidence trail, data-quality notes, limitations, and anti-hallucination controls.
```

The reader layer should be natural, professional, and easy to read. It should synthesize the analysis without overwhelming the reader with internal file references, source mechanics, or agent-by-agent process language.

The verification layer should make the report auditable. It should preserve enough detail to confirm that material claims are supported by evidence, specialist work, user-provided data, or explicitly labeled assumptions.

The verification layer may live in:

- `evidence_pack.md`;
- specialist reports;
- structured handoffs;
- compact report appendices;
- Evidence & Data Quality sections;
- internal pre-final evidence checks.

The main report should not hide uncertainty. If a data limitation is material to the investment conclusion, it belongs in the main report as a caveat and in the verification layer as a data-quality note.

### 3.8 Decision Confidence Standard

When a report presents an investment action, recommendation, prioritization, or other decision-relevant conclusion, it should explain confidence in a way that is useful to a reader.

The preferred format is:

```text
Decision Confidence: High / Moderate / Low / Insufficient Basis
Why: [why confidence is at this level]
What would raise confidence: [specific confirming evidence or conditions]
What would lower confidence: [specific adverse evidence or conditions]
```

Decision Confidence should not be a bare label. It should clarify why the decision is more or less reliable, what prevents confidence from being higher, and what evidence would change the view.

Specialist agents may use analytical confidence or evidence confidence where appropriate, but they should not imply final buy/sell conviction unless they explicitly own the final action. The Investment Committee Agent owns final Decision Confidence for the final memo.

### 3.9 Action Label Practical Meaning

Any user-facing action label, recommendation label, status label, priority label, or decision label must include practical meaning.

The reader should not have to infer what “Watchlist,” “Hold,” “Limited,” “High Priority,” or “Blocked” means operationally.

For investment actions, the default construct is:

```text
Action: [label]
Practical Meaning: [what to do or not do]
Primary Reason: [main reason]
Decision Confidence: [level + why]
Reassessment Trigger: [what would change the action]
```

For asset-specific memos where the action differs for a prospective buyer versus an existing holder, use natural reader-facing labels:

```text
For a New Position: [action label]
For Existing Holders: [action label]
```

Avoid awkward internal labels such as “New Money Action” in the main memo.

This rule applies across the system wherever an agent gives a decision-relevant label. Specialist agents that do not own the final investment action should use this rule for their own statuses, priorities, blockers, and handoff implications without implying a final buy/sell decision.

## 4. Agent Categories

The system organizes active and deferred analytical roles into five broad categories.

### 4.1 Router / Intake Agents

These agents classify and route requests. They do not perform investment analysis.

Defined package:

```text
master-intake-router-prd.md
asset-intake-router-prd.md
theme-opportunity-intake-router-prd.md
```

Primary function:

- classify user request;
- ask 1-3 relevant clarifying questions when needed;
- route to asset-first, theme-first, mixed, direct specialist, comparison, update, monitoring, evidence verification, educational, portfolio-role, or blocked / clarification workflows;
- create a structured intake block or `intake.md`;
- detect freshness requirements;
- prevent narrow requests from expanding into full workflows without user approval.

The Master Intake Router performs top-level classification. The Asset Intake Router handles asset-specific context and asset-class route selection. The Theme / Opportunity Intake Router handles theme, sector, structural-winner, and opportunity-discovery route selection.


### 4.2 Opportunity / Discovery Agents

These agents convert themes, industries, and structural questions into investable candidate maps. They do not produce final buy/sell recommendations.

Active examples:

- Structural Winners Discovery Agent
- Sector & Industry Analysis Agent when the request is a sector diagnostic rather than candidate discovery

Future Opportunity Discovery / Future Winners variants may be added only if they do not duplicate Structural Winners Discovery.

Primary function:

- map themes and industries into value chains;
- identify bottlenecks, control points, hidden beneficiaries, and candidate companies;
- produce candidate shortlists and watchlists;
- recommend next deep-dive analyses without automatically launching them.

### 4.3 Asset-Class Lead Agents

These agents lead analysis for specific asset classes.

Examples:

- Equity Agent
- ETF Agent
- Commodity Agent
- Crypto Agent
- Fixed Income Agent

Primary function:

- understand the structure and economics of a specific asset class;
- coordinate asset-specific analysis;
- use relevant skills and specialist inputs;
- produce asset-class specialist reports.

### 4.4 Specialist / Cross-Functional Agents

These agents apply analytical lenses across asset classes.

Active examples:

- Evidence Collector Agent
- Sector & Industry Analysis Agent
- Macro Agent
- Market Intelligence Agent
- News & Catalysts Agent
- Market Sense Agent
- Valuation & Expectations Agent
- Risk / Red Team Agent
- Market Positioning Agent
- Portfolio Fit Agent

Deferred optional input:

- Technical / price-action analysis, only as a lightweight non-core timing and risk lens if added later.

Primary function:

- answer specialized cross-asset questions;
- provide modular analytical inputs;
- support asset-class agents and the Investment Committee Agent.

### 4.5 Synthesis Agent

The synthesis agent produces the final investment memo.

Example:

- Investment Committee Agent

Primary function:

- synthesize specialist reports and evidence;
- identify tensions and trade-offs;
- produce a decision-oriented investment memo;
- avoid internal agent references in the final user-facing synthesis.

## 5. Specialist / Cross-Functional Agents — Big Picture

### 5.1 Evidence Collector Agent

Core question:

> What do we know, how reliable is it, what supports each material claim, what is missing, and which downstream agents can responsibly proceed?

The Evidence Collector Agent is the system's evidence control tower.

Responsibilities:

- create and maintain the shared evidence base;
- produce `evidence_pack.md` as a claim-support artifact, not a source dump;
- use `source-registry-framework.md` and domain evidence playbooks;
- classify source tier, evidence type, claim support, claim strength, materiality, freshness, and access status;
- timestamp sources with source date, accessed date, data period, freshness requirement, freshness status, and as-of note;
- identify missing, stale, proxied, contradicted, inaccessible, paywalled, lower-confidence, or weak evidence;
- maintain the Downstream Readiness Matrix;
- distinguish Analytical Evidence Sufficiency from Decision Evidence Sufficiency;
- accept structured evidence requests from specialist agents;
- register material specialist-discovered evidence before it supports decision-relevant conclusions;
- perform pre-IC evidence lock / freshness checks;
- preserve public evidence separately from private user context.

Does not:

- make investment decisions;
- produce valuation conclusions;
- issue risk verdicts;
- write final investment thesis;
- interpret market psychology or driver dominance;
- assign portfolio role or sizing;
- turn weak sources into strong conclusions.

Defined package:

```text
evidence-collector-agent-prd.md
evidence-collection-method-skill-prd.md
evidence-pack-framework.md
source-registry-framework.md
evidence-request-protocol.md
```

Primary artifacts:

```text
evidence_pack.md
evidence_readiness_note.md
evidence_verification_note.md
evidence_request_log.md
missing_data_log.md
evidence_refresh_log.md
private_context_note.md
data/[bounded_snapshot].csv
```

Evidence status:

```text
Complete Evidence
Limited Evidence
Blocked Evidence
```

Readiness status:

```text
Ready
Ready with Caveat
Limited
Blocked
Not Required
```

The Evidence Collector may constrain downstream output status. If IC readiness is Blocked, the Investment Committee Agent may produce only a Blocked Final Memo / No Decision output. If IC readiness is Limited, the IC Agent may produce only a Limited Final Memo unless the limitation is resolved or is not decision-critical.

Operating modes:

```text
Equity Evidence Mode
ETF Evidence Mode
Commodity Evidence Mode
Crypto Evidence Mode
Fixed Income Evidence Mode
Macro Evidence Mode
Sector / Industry Evidence Mode
Theme / Opportunity Evidence Mode
Market Positioning Evidence Mode
News / Catalysts Evidence Mode
Claim / Source Verification Mode
Readiness Check Mode
```

Likely domain playbooks / references:

- equity evidence playbook;
- ETF evidence playbook;
- commodity evidence playbook;
- crypto evidence playbook;
- fixed income evidence playbook;
- macro evidence playbook;
- news / catalysts evidence playbook;
- market positioning evidence playbook / initially `market-positioning-framework.md`;
- sector / industry evidence playbook;
- theme / opportunity evidence playbook.


### 5.1A Structural Winners Discovery Agent

Core question:

> Which public companies could become long-term structural winners inside this theme, industry, or value chain?

Responsibilities:

- interpret a theme, industry, similar-company pattern, or failed-company contrast;
- map the value chain and identify where value may accrue;
- identify bottlenecks, scarce capacity, control points, platform dynamics, and mission-critical niches;
- build a bounded longlist of public-company candidates, up to 30 names;
- filter candidates into Tier 1, Tier 2, Tier 3, watch-only, and rejected groups;
- distinguish business quality from stock attractiveness;
- perform valuation sanity checks, not full valuation models;
- identify hidden / second-order beneficiaries;
- provide candidate cards, watchlist output, and recommended next analyses.

Does not:

- produce final buy/sell recommendations;
- call any company "the next NVIDIA";
- perform full financial statement analysis;
- produce a full DCF or price target;
- perform portfolio-fit analysis or position sizing;
- automatically launch downstream agents without user approval.

Dedicated design documents:

- `structural-winners-discovery-agent-prd.md`;
- `structural-winner-discovery-method-skill-prd.md`;
- `structural-winner-discovery-framework.md`.

Likely skills / references:

- `structural-winner-discovery-method-skill-prd.md` / structural-winner-discovery-method skill;
- `structural-winner-discovery-framework.md` reference;
- evidence_pack.md for deep discovery runs, if created;
- Financial Statement Analysis skill as a downstream handoff;
- Valuation & Expectations Agent as a downstream handoff;
- Risk / Red Team Agent as a downstream handoff.

Primary output artifacts:

- structural_winners_memo.md;
- candidate_watchlist.md.

Architectural position:

```text
Theme / Industry input
  ↓
Theme / Opportunity Intake Router
  ↓
Structural Winners Discovery Agent
  ↓
Candidate shortlist / watchlist
  ↓
Financial Statement Analysis / Valuation & Expectations / Risk Red Team / Company Deep Dive, if approved
  ↓
Investment Committee Agent, if a final decision memo is requested
```

### 5.1B Sector & Industry Analysis Agent

Core question:

> How does this sector or industry work, where is the profit pool, and is there a rational public-market way to express the thesis?

Responsibilities:

- analyze sector structure and business models;
- assess market size, growth, and growth quality;
- map subsectors when a sector or theme is broad;
- identify value-chain structure, bottlenecks, and profit pools;
- identify 3-5 key drivers and constraints;
- explain driver sensitivity, winners, and losers;
- analyze competitive structure and key players without full company deep dives;
- assess public-market investability;
- provide valuation context, not full valuation models;
- identify what the market may be missing and what may already be priced in;
- formulate the sector anti-thesis and thesis breakers;
- create monitoring metrics and recommended handoffs.

Does not:

- produce final buy/sell recommendations;
- perform portfolio sizing;
- perform full company financial analysis;
- build full DCF or detailed valuation models;
- analyze ETF holdings or ETF structure;
- perform broad macro regime analysis;
- perform deep news monitoring;
- create charts or diagrams by default;
- use numeric scoring.

Core modes:

```text
1. Embedded Company Mode
2. Standalone Sector Diagnostic Mode
3. Broad Theme-as-Sector Mode
```

Dedicated design documents:

- `sector-industry-analysis-agent-prd.md`;
- `sector-industry-analysis-method-skill-prd.md`;
- `sector-industry-analysis-framework.md`.

Likely skills / references:

- `sector-industry-analysis-method-skill-prd.md` / sector-industry-analysis-method skill;
- `sector-industry-analysis-framework.md` reference;
- investment-analytical-style skill;
- language-policy skill when producing user-facing summaries;
- Evidence Collector Agent and `source-registry-framework.md`.

Primary output artifacts:

Embedded company workflow:

- sector_context.md.

Legacy compatibility: `industry.md` may be read from older work folders, but new embedded sector outputs should use `sector_context.md`.

Standalone sector workflow:

- sector_evidence_pack.md;
- sector_industry_memo.md;
- sector_investment_map.md;
- sector_monitoring_plan.md.

Architectural position:

```text
Company / Sector / Theme input
  ->
Evidence Collector Agent
  ->
Sector & Industry Analysis Agent
  ->
Industry context / sector diagnostic / investment map / monitoring plan
  ->
Structural Winners Discovery / Equity / Valuation / Risk / Macro / ETF / News handoff, if approved
  ->
Investment Committee Agent, if a final synthesis memo is requested
```

### 5.1C ETF Agent

The ETF Agent is the ETF wrapper, exposure-quality, methodology, and overlap-analysis layer.

Dedicated design documents:

```text
etf-agent-prd.md
etf-analysis-method-skill-prd.md
etf-analysis-framework.md
```

It answers:

```text
What does this ETF actually own, what exposure does it provide, how good is the wrapper, how does it compare with alternatives, and what risks or overlaps are hidden?
```

Responsibilities:

- verify ETF identity, including issuer, exchange, domicile, ISIN / CUSIP where available, share class, trading currency, distribution policy, and hedge status;
- separate fund-level exposure analysis from share-class-level implementation analysis;
- analyze holdings, top holdings, concentration, and look-through risk drivers;
- use full issuer holdings files when available and explicitly label top-holdings-only limitations;
- analyze index methodology, weighting, rebalance, reconstitution, active process, and holdings drift;
- analyze fees, AUM, issuer quality, liquidity, tracking, premium / discount, yield, structure, and closure risk;
- support active ETF, factor ETF, thematic ETF, commodity ETF, bond ETF, crypto ETF, leveraged / inverse ETF, options-income ETF, synthetic ETF, and volatility-linked ETF modes;
- compare ETF peers by use-case fit rather than universal best ranking;
- detect overlap and false diversification across ETFs, portfolio holdings, sectors, countries, factors, duration, credit, commodity beta, and crypto beta where data allows;
- support ETF discovery / shortlist, ETF replacement / substitution, ETF-as-expression-of-theme, and ETF-vs-direct-holding wrapper tradeoff modes;
- produce `etf_analysis.md` with vehicle-quality verdict and role-candidate framing;
- provide structured handoffs to Evidence Collector, Sector / Industry, Macro, Fixed Income, Commodity, Crypto, Market Positioning, Portfolio Fit, Risk / Red Team, and Investment Committee.

The ETF Agent does not own final buy / sell / hold recommendations, exact position sizing, final portfolio suitability, personalized tax advice, legal advice, full underlying asset-class thesis, or final Investment Committee synthesis.

User-facing ETF reports should avoid bureaucratic Complete / Limited / Blocked labels by default. Limitations should be written as plain data notes, while internal readiness states remain available for orchestration and handoff discipline.



### 5.1D Commodity Agent

The Commodity Agent is the commodity asset-class specialist.

Dedicated design documents:

```text
commodity-agent-prd.md
commodity-analysis-method-skill-prd.md
commodity-analysis-framework.md
commodity-family-playbooks.md
```

Primary output artifacts:

```text
commodity_analysis.md
commodity_market_regime.md
```

Core responsibilities:

- verify commodity identity, benchmark, region, and exposure type;
- analyze physical supply / demand, including industry, country, central bank, government, reserve, and end-market demand where material;
- separate commercial inventories, exchange stocks, strategic reserves, above-ground stocks, geological reserves / resources, and spare capacity;
- interpret futures curve, roll yield, carry, contango, backwardation, and commodity-specific instrument implications;
- analyze marginal cost, cost curve, incentive price, capex cycle, and supply response without treating cost as a guaranteed price floor;
- analyze geopolitics, policy, sanctions, OPEC / producer policy, export bans, strategic reserve release / refill, logistics, storage, transport, and substitution risk;
- produce commodity valuation context and actionability labels without final buy / sell / hold recommendations;
- use commodity-family playbooks for oil / refined products, natural gas / LNG, gold / precious metals, industrial metals / critical minerals, uranium, agriculture / softs, and broad commodity baskets;
- produce specialist verdicts, monitoring triggers, confidence-by-block, and structured handoffs.

Key ownership boundaries:

- ETF Agent owns ETF / ETC wrapper quality; Commodity Agent owns the underlying commodity thesis and commodity-specific roll / curve implications.
- Equity Agent owns full underwriting of commodity producers, miners, energy companies, royalty companies, and streamers; Commodity Agent owns the underlying commodity cycle / beta.
- Macro Agent owns full macro regime; Commodity Agent owns commodity-specific macro sensitivity.
- Market Positioning Agent owns deep consensus, positioning, and crowding; Commodity Agent owns basic commodity-relevant positioning checks.
- Risk / Red Team owns independent challenge; Commodity Agent owns first-pass commodity-native traps.
- Investment Committee owns final action.

Commodity analysis must be physical-balance-first, source-aware, and narrative-skeptical. Narratives such as AI copper demand, central bank gold buying, OPEC control, energy transition demand, or uranium scarcity must be translated into testable data claims before they support a thesis.

### 5.1E Crypto Agent

The Crypto Agent is the crypto asset-class specialist.

Dedicated design documents:

```text
crypto-agent-prd.md
crypto-analysis-method-skill-prd.md
crypto-analysis-framework.md
crypto-data-source-and-metric-framework.md
```

Primary output artifacts:

```text
crypto_analysis.md
crypto_market_regime.md
```

Core responsibilities:

- verify crypto asset identity and economic classification;
- apply investment-grade viability gates;
- analyze tokenomics, unlocks, emissions, supply, and value capture;
- analyze network economics, fees, burn, staking, validator / sequencer economics, and tokenholder value accrual;
- distinguish real adoption from subsidized activity, airdrop farming, vanity metrics, and mercenary liquidity;
- analyze crypto market structure, liquidity, derivatives, leverage, funding, open interest, basis, and liquidations;
- interpret spot BTC / ETH ETF flows and corporate crypto treasury demand as structural demand / supply inputs;
- analyze stablecoin liquidity, tokenization / RWA value capture, DeFi economics, custody, protocol security, governance, regulatory impact, and crypto-specific macro / liquidity transmission;
- maintain BTC and ETH dedicated overlays;
- produce specialist verdicts and structured handoffs, not final investment actions.

Default horizon is 6-36 months for ordinary crypto investment analysis, with 3-5 year framing allowed for BTC or ETH long-term thesis work. Current-entry, sharp-move, depeg, hack, ETF-flow, liquidation, funding, or regulatory-headline questions require a fast-moving setup overlay.

Key ownership boundaries:

- ETF Agent owns crypto ETF wrapper quality; Crypto Agent owns underlying token, network, adoption, regulation, security, custody, and speculative narrative analysis.
- Equity Agent owns full analysis of crypto-linked stocks; Crypto Agent owns crypto exposure mechanics and underlying market impact.
- Macro Agent owns full macro regime; Crypto Agent owns crypto-specific macro and liquidity transmission.
- News & Catalysts owns fresh event mapping; Crypto Agent owns crypto-specific investment impact.
- Risk / Red Team owns independent thesis-breaker challenge; Crypto Agent owns first-pass crypto-native risk analysis.
- Investment Committee owns final action.

The Crypto Agent must not recommend leverage, trades, yield-farming strategies, staking providers, lending pools, bridge routes, custody setup, final allocations, final price targets, or legal / tax conclusions.

### 5.1F Fixed Income Agent

The Fixed Income Agent is the fixed-income asset-class specialist.

Dedicated design documents:

```text
fixed-income-agent-prd.md
fixed-income-analysis-method-skill-prd.md
fixed-income-framework.md
fixed-income-instrument-playbooks.md
```

Primary output artifact:

```text
fixed_income_analysis.md
```

Optional focused artifacts:

```text
rates_duration_analysis.md
credit_spread_analysis.md
bond_etf_fixed_income_exposure.md
structured_credit_risk_note.md
private_credit_limited_review.md
```

Core question:

> Does this fixed-income instrument or exposure offer adequate risk-adjusted compensation for the yield, duration, credit, spread, liquidity, structure, inflation, FX, and downside risks being taken?

Core responsibilities:

- classify the fixed-income instrument, exposure, yield type, and horizon;
- distinguish individual bond repayment economics from bond fund / ETF rolling-exposure economics;
- analyze yield to maturity, yield to worst, SEC yield, distribution yield, real yield, tax-equivalent yield framework, and spread / OAS where relevant;
- analyze duration, curve, convexity, rate-shock, real-yield, and inflation sensitivity;
- analyze issuer / obligor credit quality, leverage, coverage, refinancing, seniority, collateral, covenants, and rating context;
- assess whether yield / spread / carry adequately compensates for duration, credit, liquidity, structure, FX, inflation, and downside risk;
- run fixed-income downside scenarios including rates up, rates down, curve shift, spread widening, credit deterioration, liquidity stress, call / prepayment / extension, inflation / real-rate shock, and FX shock where relevant;
- support rates / sovereign, corporate credit, high yield / distressed, muni, TIPS / inflation-linked, international / EM debt, floating-rate / loan, preferred / hybrid, convertible, securitized credit, private credit limited, bond ETF / fund, and cash-equivalent / liquidity-sleeve modes;
- produce fixed-income specialist verdicts, data-confidence notes, monitoring triggers, and structured handoffs.

Key ownership boundaries:

- Macro Agent owns policy path, inflation regime, real-yield regime, curve macro interpretation, liquidity, FX, and cross-asset macro context; Fixed Income Agent owns instrument-level sensitivity and compensation.
- ETF Agent owns bond ETF wrapper quality, fees, tracking, liquidity, NAV premium / discount, methodology, and holdings transparency; Fixed Income Agent owns underlying duration, credit, spread, yield, and compensation adequacy.
- Portfolio Fit Agent owns final portfolio suitability and sizing constraints; Fixed Income Agent provides role-candidate framing such as income sleeve, ballast candidate, credit carry, tactical duration, inflation-linked exposure, or not suitable as safe-income substitute.
- Risk / Red Team owns independent challenge; Fixed Income Agent escalates high-yield, distressed, private, structured, subordinated, opaque, asymmetric, unusually high-yielding, or "safe income" contradiction cases.
- Investment Committee owns final action.

Fixed income analysis must not treat yield alone as attractiveness. It must not call bond funds principal-protected, imply hold-to-maturity economics for ETFs, accept ratings as conclusions, or use final buy / sell / hold language.


### 5.2 Macro Agent

Core question:

> Which macro variables, regimes, policy shifts, liquidity conditions, FX moves, and cross-asset signals materially affect this investment decision, and through what transmission channel?

Responsibilities:

- standalone macro analysis through Market Pulse, Weekly Delta, Event-Driven, and Full Macro Regime modes;
- embedded asset-specific macro sensitivity analysis through `macro_sensitivity.md`;
- confirmed macro regime vs current risk overlay separation;
- growth, labor, inflation, rates, central bank, liquidity, credit, FX, and cross-asset macro interpretation;
- G3 FX and regional policy overlay for DXY, EUR/USD, USD/JPY, ECB, BoJ, Europe, and Japan when material;
- macro expectations and surprise context, including consensus and market-implied policy paths;
- data freshness, indicator cadence, source hierarchy, and anti-hallucination discipline;
- material macro transmission chains into valuation, earnings, margins, credit, FX, portfolio risk, and thesis failure paths;
- structured handoffs to Valuation & Expectations, Risk / Red Team, Market Positioning, Market Sense, Portfolio Fit, and Investment Committee.

Core modes:

```text
Market Pulse Mode -> macro_market_pulse.md
Weekly Delta Mode -> macro_weekly_delta.md
Event-Driven Mode -> macro_event_update.md
Monthly / Full Macro Regime Mode -> macro_regime_baseline.md
Asset-Specific Macro Sensitivity Mode -> macro_sensitivity.md
```

Internal macro memory:

```text
macro_block_states/
  growth_labor_state.md
  inflation_commodities_state.md
  rates_fed_curve_state.md
  liquidity_credit_state.md
  cross_asset_confirmation_state.md
  g3_fx_regional_policy_state.md
```

Regime discipline:

- The Macro Agent separates `Confirmed Macro Regime` from `Current Risk Overlay`.
- Regime changes require depth, diffusion, duration, transmission, and market discounting.
- One release, one data point, or one market move normally updates risk overlay or trigger watch rather than the confirmed regime.
- Early warning indicators must be tracked seriously but cannot become regime verdicts without diffusion, transmission, and confirmation.

Freshness discipline:

- Fresh market data are mandatory for current conclusions about yields, FX, DXY, EUR/USD, USD/JPY, oil, gold, volatility, credit spreads, and market-implied policy paths.
- Slow official releases may be carried forward only with timestamp discipline.
- Limited / Blocked status is used internally and surfaced only when it materially affects the reader-facing conclusion.

Does not:

- analyze full company fundamentals;
- produce target price;
- write final decision memo.
- issue final buy / sell / hold recommendations;
- determine exact position sizing;
- make final priced-in / mispriced conclusions;
- replace Market Positioning or Market Sense for market-belief and reaction interpretation.

Likely skills / references:

- `macro-agent-prd.md`;
- `macro-analysis-method-skill-prd.md`;
- `macro-sensitivity-framework.md`;
- `macro-regime-framework.md`;
- `macro-indicator-cadence-source-registry.md`;
- `macro-block-playbooks.md`;
- `macro-g3-fx-regional-policy-overlay.md`;
- `macro-expectations-surprise-framework.md`.

### 5.3 Valuation & Expectations Agent

Core question:

> What is already priced in, and are those expectations reasonable?

The currently designed Valuation & Expectations Agent module covers public listed equities. It follows an expectations-adjusted value doctrine and evaluates whether the current market price is justified by realistic expectations for growth, margins, cash flows, returns on capital, risk, and required return.

For commodities, the Commodity Agent now owns commodity valuation context such as price support versus physical balance, curve, inventories, marginal / incentive cost, and macro sensitivity, while avoiding precise final price targets and final investment actions.

For crypto assets, the Crypto Agent owns crypto valuation context and implied expectations analysis, while avoiding precise final price targets and final investment actions.

For fixed income instruments, the Fixed Income Agent owns compensation / relative-value analysis: whether yield, spread, carry, and downside adequately compensate for duration, credit, liquidity, structure, inflation, FX, and scenario risk.

ETF valuation remains outside the current detailed valuation module unless a separate reusable need is identified.

Responsibilities:

- current valuation snapshot;
- absolute valuation and quality-adjusted valuation;
- earnings, EPS, cash-flow, enterprise-value, and asset-based valuation where relevant;
- sector-specific valuation method selection;
- primary valuation method and supporting method selection;
- market-implied expectations and reverse-expectations analysis;
- DCF / reverse DCF when economically meaningful;
- scenario-implied valuation ranges and uncertainty bands;
- return bridge;
- margin of safety as an Investment Committee input;
- valuation asymmetry;
- peer comparability scoring;
- historical valuation context as context, not verdict;
- consensus estimates as benchmark, not truth;
- management guidance credibility checks;
- estimate revisions as expectations signals;
- valuation risk flags;
- misleading metric flags;
- value trap, quality trap, and growth trap diagnostics;
- terminal value and long-duration dependency checks;
- multiple durability assessment;
- liquidity, float, market-access, regulatory/legal, and SOTP valuation caveats where material;
- monitoring signals tied to implied expectations;
- structured handoff to Risk / Red Team and Investment Committee.

Data discipline:

- follow source hierarchy and timestamp discipline;
- prioritize official, current, and verifiable data;
- do not invent unsupported valuation numbers;
- cross-check core calculations where data is available;
- classify each output as Complete Valuation, Limited Valuation, or Blocked Valuation.

Does not:

- issue final buy / sell / hold recommendations;
- issue single-point target prices;
- own position sizing or portfolio construction;
- own full business-quality analysis;
- own the full macro thesis;
- own full legal, regulatory, or credit-risk adjudication;
- replace Risk / Red Team analysis;
- replace Investment Committee synthesis.

Design package:

```text
valuation-expectations-agent-prd.md
valuation-expectations-method-skill-prd.md
valuation-expectations-framework.md
```

Output artifact:

```text
valuation_expectations.md
```

### 5.4 Risk / Red Team Agent

Core question:

> How can this investment thesis fail, and what evidence would show that it is failing?

Responsibilities:

- challenge the specific company thesis after business-quality and valuation work;
- identify thesis-critical assumptions and fragile expectations;
- build a coherent thesis failure map rather than a generic risk list;
- identify 3-7 material, economically plausible failure paths, with top-3 depth;
- require a clear transmission mechanism from risk to economics, valuation, balance sheet, or thesis credibility;
- challenge whether valuation downside and bear case assumptions are severe enough;
- define thesis invalidation triggers and early warning indicators;
- run accounting / governance, balance sheet / liquidity, and market expectations / positioning gates;
- distinguish temporary, structural, and permanent impairment risk;
- separate plausible failure paths, watchlist risks, tail risks, and excluded / deprioritized risks;
- issue a risk challenge verdict without issuing investment recommendations;
- create structured analytical challenge requests when further work is needed.

Does not:

- produce generic risk lists;
- break the thesis mechanically or create a forced bearish case;
- issue buy / sell / hold recommendations;
- issue target prices or position sizes;
- own the full valuation model;
- own final legal adjudication;
- replace Investment Committee synthesis.

Design package:

```text
risk-red-team-agent-prd.md
risk-red-team-method-skill-prd.md
risk-red-team-framework.md
```

Output artifact:

```text
risk_red_team.md
```

Output status:

```text
Complete Risk Review
Limited Risk Review
Blocked Risk Review
Preliminary Risk Scan
```

### 5.5 News & Catalysts Agent

Core question:

> What changed recently, and what could move the asset next?

Responsibilities:

- asset-specific and theme-specific recent event review;
- active carryover event identification;
- upcoming catalyst mapping;
- event materiality assessment;
- source status and timestamp discipline for material events;
- negative news check with explicit window and source boundaries;
- directional event impact assessment without full valuation modeling;
- catalyst failure flags;
- peer / sector read-through when materially relevant and clearly labeled as inference;
- light reaction mismatch checks with handoff to Market Sense / Market Positioning when needed;
- prep and follow-up work items for Tier 1 or high-decision-pressure catalysts;
- structured handoffs to Evidence Collector, Valuation & Expectations, Risk / Red Team, Market Positioning, Market Sense, Macro, asset-class agents, and Investment Committee.

Does not:

- summarize every headline;
- treat headlines as verified facts without source discipline;
- replace long-term business analysis;
- produce valuation conclusions;
- issue final buy / sell / hold / add / reduce / avoid recommendations;
- provide target prices, exact position sizing, hedge sizing, or trading instructions;
- perform full driver dominance or market psychology analysis.

Likely skills / references:

- `news-catalysts-agent-prd.md`;
- `news-catalysts-method-skill-prd.md`;
- `news-catalysts-framework.md`;
- public-equity catalyst-calendar discipline as an equity-specific methodological overlay.

Primary output:

```text
news_catalysts.md
```

Output status:

```text
Complete News & Catalysts Review
Limited News & Catalysts Review
Blocked News & Catalysts Review
Preliminary Catalyst Scan
```

### 5.6 Market Positioning Agent

Core question:

> What does the market appear to believe, how is it positioned, and does that create expectation or positioning risk or opportunity?

Responsibilities:

- visible market expectations;
- consensus and estimate revision context;
- analyst rating and target-direction interpretation as visible sell-side expectations;
- ownership and holder-base context;
- short interest and squeeze-risk context;
- ETF / fund / sector / theme flow context where relevant;
- options positioning as supporting evidence, not direct sentiment translation;
- observable narrative and sentiment evidence;
- price reaction and volume as evidence of expectation changes, not technical trading signals;
- crowding, neglect, squeeze, unwind, and event-bar diagnostics;
- signal contradiction analysis;
- positioning archetype classification;
- structured handoffs to Valuation & Expectations, Risk / Red Team, News & Catalysts, Market Sense / Macro, and Investment Committee.

Does not:

- issue final buy / sell / hold / add / reduce / exit / avoid actions;
- determine valuation attractiveness or final “priced in” valuation conclusions;
- build reverse DCF or target prices;
- replace full news / catalyst discovery;
- replace macro regime analysis;
- replace technical chart analysis, trading entries, support / resistance, or stop-loss logic;
- treat social, anecdotal, AI-generated, or narrative sources as verified positioning facts.

Likely skills / references:

- `market-positioning-agent-prd.md`;
- `market-positioning-method-skill-prd.md`;
- `market-positioning-framework.md`.

Primary output:

```text
market_positioning.md
```

Direct scoped output:

```text
focused_positioning_note.md
```

Output statuses:

```text
Complete Market Positioning
Limited Market Positioning
Blocked Market Positioning
```

The module is conceptually cross-asset, but the current detailed implementation is equity-first. It is normally a context module in full equity workflows and becomes a conditional decision-relevant gate when expectations, crowding, positioning, event reaction, or narrative saturation are material to the investment case.

### 5.7 Optional Technical / Price-Action Input — Deferred

Technical / price-action analysis is not an active core agent in the current target architecture.

If added later, it may answer only:

> What does observable price action suggest about timing risk, trend context, volatility, and drawdown behavior?

Allowed scope:

- trend and momentum context;
- volatility and drawdown context;
- post-catalyst price behavior;
- relative strength as supporting evidence;
- timing-risk caveats for Investment Committee consideration.

Hard limits:

- does not determine business quality;
- does not determine valuation attractiveness;
- does not issue trading instructions, stop-loss rules, or exact entries;
- does not override evidence, valuation, macro, risk, or portfolio constraints;
- does not become a trading system;
- does not become a required file or workflow blocker unless a future PRD explicitly promotes it into the active documentation registry.

### 5.8 Portfolio Fit Agent

Core question:

> What role could this asset play in the portfolio, and what portfolio risks does it add?

Responsibilities:

- generic portfolio role;
- user-specific portfolio fit when sufficient context is available;
- diversification, overlap, and concentration assessment;
- exposure-bucket and risk-driver analysis;
- horizon-fit and role-objective match;
- volatility, drawdown, liquidity, implementation, monitoring, currency, benchmark, and tax-aware caveat considerations where material;
- Core / Core Candidate / Satellite / Tactical / Hedge / Diversifier / Watchlist / Avoid-for-Portfolio classification;
- qualitative sizing caveats without exact position sizing;
- structured handoff to the Investment Committee Agent.

Does not:

- produce exact allocation or target weights;
- build a full portfolio from scratch;
- provide tax, legal, fiduciary, or full financial-planning advice;
- replace the Investment Committee Agent;
- produce final buy / sell / add / exit decisions.

Defined framework:

```text
portfolio-fit-framework.md
```

Defined package:

```text
portfolio-fit-agent-prd.md
portfolio-fit-method-skill-prd.md
portfolio-fit-framework.md
```

## 6. Owner / Contributor Model

Many analytical blocks require multiple agents. The system should distinguish:

```text
Primary Owner = agent responsible for final version of the block
Contributors = agents or skills that provide inputs
Final Synthesizer = Investment Committee Agent when the block affects the final decision memo
```

The goal is to avoid both duplication and ambiguity.

### 6.1 Material Claim Support

Every owner agent is responsible for ensuring that material factual claims in its report are supported by the evidence pack, specialist inputs, user-provided data, cited reliable sources, or clearly labeled assumptions.

Contributor agents are responsible for passing source quality, freshness, limitations, and confidence notes through their handoffs. The final owner may synthesize and rephrase the analysis, but must not remove material uncertainty or strengthen conclusions beyond the evidence.

The Investment Committee Agent is the final synthesizer for decision memos. It may turn specialist outputs into a natural investment narrative, but it must preserve the underlying evidence discipline and must not introduce unsupported new facts.

## 7. Ownership of Key Analytical Blocks from the Equity Deep-Dive Prompt

### 7.1 Market Narrative

Primary owner:

- Market Positioning Agent

Contributors:

- News & Catalysts Agent
- Valuation & Expectations Agent
- Risk / Red Team Agent where fear or narrative risk matters

Typical questions:

- What narrative currently dominates the stock?
- What expectations, consensus, and news are already reflected in the price?
- Where might expectations diverge from reality?
- How has sentiment changed over the last 3–12 months, and why?
- What is the market most afraid of right now?

Notes:

- “What is priced in?” is shared with the Valuation & Expectations Agent.
- “What changed perception?” is shared with the News & Catalysts Agent.

### 7.2 Scenario Analysis / Bull, Base, Bear Cases

Primary owner:

- Investment Committee Agent

Contributors:

- Valuation & Expectations Agent
- Risk / Red Team Agent
- Macro Agent
- News & Catalysts Agent
- Market Positioning Agent
- Equity Agent

Ownership by subcomponent:

| Scenario Component | Primary Input Owner |
|---|---|
| Bull / base / bear narrative | Investment Committee Agent |
| Scenario-implied valuation range | Valuation & Expectations Agent |
| Bear-case failure path | Risk / Red Team Agent |
| Upside drivers | Equity Agent, Valuation & Expectations Agent, News & Catalysts Agent |
| Macro conditions | Macro Agent |
| Catalysts | News & Catalysts Agent |
| Sentiment and crowding | Market Positioning Agent |
| Asymmetry | Investment Committee Agent |
| One thesis-killer risk | Risk / Red Team Agent |

Notes:

- The Investment Committee Agent writes the final scenario analysis.
- It should not invent valuation ranges not supported by the Valuation & Expectations Agent; single-point target prices are not a Valuation Agent output.
- Probabilities should be used carefully and only when evidence supports them; otherwise use qualitative likelihood and confidence.

### 7.3 Competitive Analysis

Primary owner:

- Equity Agent

Contributors:

- Financial Statement Analysis skill
- Valuation & Expectations Agent
- Risk / Red Team Agent
- Sector & Industry Analysis Agent / Sector & Industry Analysis Method

Typical questions:

- Who are the direct competitors?
- How does the company compare on revenue, margins, growth, and business model?
- What is the company’s moat?
- Are there network effects, switching costs, brand advantages, patents, scale economies, or other barriers?
- What is the competitive intensity?
- Is the company gaining or losing market share?
- What is the risk of competition or technological disruption?

Ownership by subcomponent:

| Competitive Component | Primary Owner |
|---|---|
| Competitor identification | Equity Agent |
| Porter’s Five Forces | Equity Agent |
| SWOT | Equity Agent |
| Moat / barriers to entry | Equity Agent |
| Revenue / margin / growth comparison | Financial Statement Analysis skill |
| Valuation comparison | Valuation & Expectations Agent |
| Disruption risk | Risk / Red Team Agent |
| Sector structure | Equity Agent or Sector & Industry Analysis Agent / Method |

### 7.4 Recent News and Events

Primary owner:

- News & Catalysts Agent

Contributors:

- Equity Agent
- Market Positioning Agent
- Risk / Red Team Agent

Typical questions:

- What were the key recent company news items?
- What sector events matter?
- Were there changes in management, strategy, or products?
- Was there M&A activity?
- Did any event change market perception of the company?

Notes:

- The agent should focus on materiality, not headline volume.
- News should be tied to thesis, timing, risk, or market perception.

### 7.5 Non-Obvious Risks

Primary owner:

- Risk / Red Team Agent

Contributors:

- Equity Agent
- Financial Statement Analysis skill
- Macro Agent
- News & Catalysts Agent
- Valuation & Expectations Agent
- Market Positioning Agent

Typical questions:

- What hidden risks are not reflected in the price?
- Is there customer concentration risk?
- Is management quality a risk?
- Could the product become obsolete or be substituted?
- Is there technological disruption risk?
- Is dilution a risk?
- Is there regulatory risk not yet in headlines?
- What does the market systematically underestimate or overestimate?

Ownership by subcomponent:

| Risk Component | Primary Input Owner |
|---|---|
| Customer concentration | Equity Agent / filings |
| Management quality | Equity Agent, News & Catalysts Agent |
| Capital allocation concerns | Financial Statement Analysis skill |
| Dilution / SBC | Financial Statement Analysis skill |
| Regulatory risk | News & Catalysts Agent, Risk / Red Team Agent |
| Disruption risk | Equity Agent, Risk / Red Team Agent |
| Overestimated / underestimated market view | Risk / Red Team Agent, Market Positioning Agent, Valuation & Expectations Agent |

### 7.6 Three Key Investment Questions

Primary owner:

- Investment Committee Agent

Contributors:

- Equity Agent
- Financial Statement Analysis skill
- Valuation & Expectations Agent
- Market Positioning Agent
- News & Catalysts Agent
- Macro Agent
- Optional technical / price-action input if explicitly used

Questions:

1. Is this a good business?
2. Is the current price attractive?
3. Is now a good time to enter?

Ownership by question:

| Question | Primary Inputs |
|---|---|
| Is this a good business? | Equity Agent, Financial Statement Analysis skill |
| Is the current price attractive? | Valuation & Expectations Agent |
| Is now a good time to enter? | Market Positioning Agent, News & Catalysts Agent, Macro Agent, optional technical / price-action input if explicitly used |

### 7.7 Final Investment Thesis

Primary owner:

- Investment Committee Agent

Contributors:

- All relevant specialist reports and evidence pack

Example thesis structure:

```text
I would buy / hold / watch / avoid [company] because [1–2 key structural drivers].
The market appears to underestimate / overestimate [specific divergence].
The relevant horizon is [time horizon].
The central valuation or expectation issue is [X].
The main risk is [Y].
The thesis should be reconsidered if [Z].
```

Notes:

- The final investment thesis should not be written by the Equity Agent alone.
- It belongs to the Investment Committee Agent because it must incorporate business quality, valuation, risks, expectations, catalysts, macro, timing, and portfolio role.
- The final thesis should not mention internal agents by name.

## 8. Full Asset-First Workflow — Big Picture

Example user request:

```text
Analyze Nvidia as a five-year investment.
```

Conceptual flow:

```text
User request
  ↓
Master Intake Router
  ↓
Asset Intake Router
  ↓
intake.md / structured intake block
  ↓
Evidence Collector Agent
  ↓
Parallel specialist work, where appropriate
  - Financial Statement Analysis
  - Sector & Industry Analysis
  - News & Catalysts
  - Market Positioning
  - Macro
  ↓
Asset-Class Lead Agent, e.g. Equity Agent -> equity_company_analysis.md
  ↓
Valuation & Expectations Agent -> valuation_expectations.md (scenario-implied valuation ranges, implied expectations, valuation risk flags)
  ↓
Risk / Red Team Agent -> risk_red_team.md
  ↓
Evidence Collector Agent -> pre-IC evidence lock / freshness check
  ↓
Investment Committee Agent
  ↓
final_investment_memo.md
```

For public equities, the detailed orchestration is defined in:

```text
equity-deep-dive-workflow.md
```

Routing and intake behavior is defined in:

```text
master-intake-router-prd.md
asset-intake-router-prd.md
theme-opportunity-intake-router-prd.md
```


## 8A Sector / Industry Diagnostic Workflow - Big Picture

Example user request:

```text
Analyze AI infrastructure as an investment sector.
```

Conceptual flow:

```text
User request
  ->
Master Intake Router
  ->
Theme / Opportunity Intake Router
  ->
Sector & Industry Analysis Agent
  ->
Evidence Plan
  ->
Evidence Collector Agent
  ->
Uses Sector & Industry Analysis Method
  ->
Outputs:
  - sector_evidence_pack.md
  - sector_industry_memo.md
  - sector_investment_map.md
  - sector_monitoring_plan.md
  ->
Recommended handoffs, if approved:
  - Structural Winners Discovery Agent
  - Equity Agent
  - Valuation & Expectations Agent
  - Risk / Red Team Agent
  - Macro Agent
  - ETF Agent
  - News & Catalysts Agent
```

The Sector & Industry Analysis Agent is a sector diagnostic layer. It should not produce final buy/sell decisions or replace the Investment Committee Agent.

## 8B Theme / Industry Structural Discovery Workflow - Big Picture

Example user request:

```text
Find structural winner candidates in AI power demand.
```

Conceptual flow:

```text
User request
  ↓
Master Intake Router
  ↓
Theme / Opportunity Intake Router
  ↓
Structural Winners Discovery Agent
  ↓
Uses Structural Winner Discovery Method
  ↓
Outputs:
  - structural_winners_memo.md
  - candidate_watchlist.md
  ↓
Recommended next analysis, if approved:
  - Financial Statement Analysis
  - Valuation & Expectations
  - Risk / Red Team
  - Company / Equity Deep Dive
```

The Structural Winners Discovery Agent is a discovery and screening layer. It should not produce a final buy/sell decision or replace the Investment Committee Agent.

## 9. Direct Specialist Call Workflow — Big Picture

Example user request:

```text
Risk Agent, red-team the Nvidia thesis.
```

Conceptual flow:

```text
User request
  ↓
Risk / Red Team Agent
  ↓
Uses risk-red-team skill
  ↓
Reads existing reports if available
  ↓
Uses supporting skills only if needed
  ↓
risk_red_team.md
```

Direct specialist calls should remain scoped. They should not automatically trigger the full asset-first workflow unless the user requests it.

For Risk / Red Team direct calls, the agent should classify the output as Complete Risk Review, Limited Risk Review, Blocked Risk Review, or Preliminary Risk Scan depending on whether existing Equity, Valuation, evidence, and market-context reports are available. Without valuation context, it must not present a full priced-in expectations or bear-case integrity review.

Direct Macro call:

For Macro direct calls, the agent should route by intent into Market Pulse, Weekly Delta, Event-Driven, Full Macro Regime, or Asset-Specific Macro Sensitivity mode. Current market-sensitive macro calls require fresh market data. Slow official releases may be carried forward only with timestamps. Standalone Macro outputs may include a mini evidence log; if later used in an Investment Committee workflow, the evidence should be registered into or revalidated by the Evidence Collector.

## 10. Example Agent-to-Skill Relationships

### 10.1 Equity Agent

Designed role:

- lead company-analysis agent for public listed equities;
- owns company-quality analysis, not final investment recommendations;
- answers whether the company is a good business, what the thesis depends on, what would change the view, and what must be checked separately.

Primary output:

- `equity_company_analysis.md`

Dedicated design documents:

- `equity-agent-prd.md`
- `equity-company-analysis-method-skill-prd.md`
- `equity-company-analysis-framework.md`
- `equity-deep-dive-workflow.md`
- `financial-statement-analysis-skill-prd.md`

Uses:

- `equity-company-analysis-method` skill;
- `equity-company-analysis-framework.md` reference;
- `financial-statement-analysis-skill-prd.md` / `financial_statement_analysis.md` skill-owned output;
- `sector_context.md` from Sector & Industry Analysis Agent;
- evidence pack from Evidence Collector Agent.

Does not own:

- final buy / sell recommendation;
- target price;
- position sizing;
- full valuation;
- full risk verdict;
- market timing;
- portfolio fit;
- final Investment Committee synthesis.

The Equity Deep Dive Workflow is separate from the Equity Agent. The workflow coordinates Evidence Collector, Financial Statement Analysis, Sector & Industry Analysis, Equity Company Analysis, Valuation & Expectations, Market Positioning, News & Catalysts, Macro, Risk / Red Team, and Investment Committee synthesis.

### 10.1A ETF Agent

Designed role:

- ETF wrapper, exposure-quality, methodology, and overlap-analysis specialist;
- owns `etf_analysis.md` and ETF vehicle-quality verdicts, not final investment actions;
- analyzes whether an ETF is a clean, diluted, risky, expensive, overlapping, or otherwise imperfect vehicle for the intended role.

Primary output:

- `etf_analysis.md`

Dedicated design documents:

- `etf-agent-prd.md`
- `etf-analysis-method-skill-prd.md`
- `etf-analysis-framework.md`

Uses:

- Evidence Pack and ETF Evidence Mode from Evidence Collector Agent;
- issuer holdings files, issuer fact sheets, prospectuses, index methodology documents, exchange data, NAV / premium-discount data, and reputable fallback market-data / overlap tools;
- Sector / Industry Analysis Agent when sector or thematic validity matters;
- Macro Agent when rates, inflation, FX, credit, liquidity, policy, or macro regime materially affect ETF risk / return;
- Fixed Income, Commodity, or Crypto Agents when the ETF wrapper depends on those underlying asset classes;
- Portfolio Fit Agent when overlap, false diversification, role suitability, or user portfolio context matters;
- Risk / Red Team Agent when ETF structure, leverage, derivatives, concentration, liquidity, yield, or theme narrative creates material thesis-breaking risk.

Does not own:

- final buy / sell / hold recommendation;
- exact position sizing;
- final portfolio suitability;
- personalized tax or legal advice;
- full company, macro, commodity, crypto, or fixed-income thesis;
- final Investment Committee synthesis.



### 10.1B Commodity Agent

Agent:

```text
Commodity Agent
```

Uses skills:

```text
Commodity Analysis Method Skill
```

Uses references:

```text
commodity-analysis-framework.md
commodity-family-playbooks.md
source-registry-framework.md
evidence-request-protocol.md
```

Produces:

```text
commodity_analysis.md
commodity_market_regime.md
```

May trigger:

```text
Evidence Collector Agent
Macro Agent
ETF Agent
Equity Agent
Market Positioning Agent
News & Catalysts Agent
Portfolio Fit Agent
Risk / Red Team Agent
Investment Committee Agent
```

### 10.1C Crypto Agent

Designed role:

- crypto asset-class specialist for direct crypto assets and crypto-linked exposures;
- owns `crypto_analysis.md` for specific assets and `crypto_market_regime.md` for broad crypto-market regime analysis;
- analyzes whether a crypto asset or market setup is investable on a fundamental, market-structure, regulatory, liquidity, security, and valuation-context basis;
- gives a crypto specialist verdict, not final investment action.

Dedicated design documents:

- `crypto-agent-prd.md`
- `crypto-analysis-method-skill-prd.md`
- `crypto-analysis-framework.md`
- `crypto-data-source-and-metric-framework.md`

Uses:

- Evidence Pack and Crypto Evidence Mode from Evidence Collector Agent;
- primary / official sources, professional crypto data providers, reputable dashboards with caveats, and social commentary only as narrative context;
- ETF Agent when the exposure is an ETF wrapper;
- Equity Agent when the question concerns crypto-linked stocks or treasury companies;
- Macro Agent when full rates, liquidity, USD, policy, credit, or cross-asset macro regime is material;
- Market Positioning and Market Sense when flows, crowding, narrative heat, driver dominance, or market reaction matter;
- News & Catalysts for fresh regulation, ETF, protocol, hack, governance, listing, treasury, and enforcement events;
- Risk / Red Team for thesis-breaking challenge;
- Portfolio Fit and Investment Committee for portfolio role and final synthesis.

Does not own:

- final buy / sell / hold recommendation;
- exact position sizing;
- legal, tax, or custody advice;
- operational DeFi, staking, lending, pool, bridge, or yield strategy recommendations;
- full ETF wrapper analysis;
- full equity analysis;
- full macro regime analysis;
- final risk verdict;
- final Investment Committee synthesis.


### 10.1D Macro Agent

Designed role:

- standalone and embedded macro regime, policy, liquidity, FX, and sensitivity layer;
- owns `macro_sensitivity.md` in asset workflows and `macro_market_pulse.md`, `macro_weekly_delta.md`, `macro_event_update.md`, and `macro_regime_baseline.md` in standalone macro workflows;
- separates confirmed macro regime from risk overlay;
- evaluates macro data relative to expectations and immediate market reaction without making final priced-in conclusions.

Dedicated design documents:

- `macro-agent-prd.md`
- `macro-analysis-method-skill-prd.md`
- `macro-sensitivity-framework.md`
- `macro-regime-framework.md`
- `macro-indicator-cadence-source-registry.md`
- `macro-block-playbooks.md`
- `macro-g3-fx-regional-policy-overlay.md`
- `macro-expectations-surprise-framework.md`

Uses:

- Evidence Pack when embedded in a full workflow;
- direct evidence collection and mini evidence log when called standalone;
- internal playbooks for Growth & Labor, Inflation & Commodities, Rates / Fed / Yield Curve, Liquidity & Credit, and Cross-Asset Macro Confirmation;
- conditional G3 FX & Regional Policy overlay when Europe, Japan, EUR/USD, USD/JPY, ECB, BoJ, or regional policy divergence is material;
- Macro Expectations & Surprise framework when consensus or market-implied expectations are relevant.

Does not own:

- final investment action;
- exact position sizing;
- final valuation or target price;
- final priced-in / mispriced verdict;
- single-security positioning;
- final risk verdict;
- final Investment Committee synthesis.

### 10.2 Valuation & Expectations Agent

Uses:

- `valuation-expectations-agent-prd.md` for role, ownership boundaries, and output rules;
- `valuation-expectations-method-skill-prd.md` for the analytical method;
- `valuation-expectations-framework.md` as the practical checklist and report framework;
- `financial_statement_analysis.md` when analyzing equities or corporate issuers;
- `equity_company_analysis.md` for company-quality inputs;
- `sector_context.md` for sector-specific valuation context;
- market data, consensus estimates, management guidance, estimate revisions, and peer data subject to source hierarchy, timestamp discipline, and anti-hallucination rules.

The agent produces `valuation_expectations.md` and hands off scenario-implied valuation ranges, implied expectations, valuation risk flags, confidence limits, and monitoring signals to Risk / Red Team and Investment Committee.

### 10.3 Risk / Red Team Agent

Uses:

- `risk-red-team-agent-prd.md` for role, ownership boundaries, and output rules;
- `risk-red-team-method-skill-prd.md` for the analytical method;
- `risk-red-team-framework.md` as the practical checklist and report framework;
- `equity_company_analysis.md` for the company-quality thesis and critical assumptions;
- `valuation_expectations.md` for priced-in expectations, scenario range, and downside case;
- `financial_statement_analysis.md` when financial fragility, accounting quality, or cash-flow quality matters;
- `sector_context.md` when sector structure and competitive pressure affect failure paths;
- `market_positioning.md` when expectations, crowding, or consensus complacency affects downside asymmetry;
- `news_catalysts.md` when event risk or catalyst failure matters;
- `macro_sensitivity.md` when rates, FX, liquidity, or macro regime are material to thesis failure.

The agent produces `risk_red_team.md` and hands off thesis failure paths, invalidation triggers, risk gates, challenge requests, and risk challenge verdict to the Investment Committee Agent. It may request upstream review, but it does not rewrite upstream reports or issue investment actions.

### 10.4 Investment Committee Agent

Defined package:

```text
investment-committee-agent-prd.md
investment-committee-synthesis-method-skill-prd.md
investment-committee-memo-framework.md
```

Likely uses:

- investment-committee-synthesis method skill;
- investment-committee-memo-framework.md;
- investment-analytical-style skill;
- language-policy skill where needed;
- evidence_pack.md;
- all relevant specialist reports.

The Investment Committee Agent is the final professional judgment layer. It is downstream-only: it should run after the orchestrator / workflow confirms that required inputs are ready.

It should not operate as a direct-call opinion agent. If required inputs are missing, it returns:

```text
No Decision — More Work Required
```

with required workflow steps or structured follow-up requests.

Primary output:

```text
final_investment_memo.md
```

For Company / Asset-first workflows, the agent normally requires:

- intake context;
- evidence pack;
- lead asset analysis;
- valuation / expectations analysis;
- risk / red team review;
- relevant context modules where material.

Positive actions require sufficient valuation / expectations analysis and Risk / Red Team review.

Core synthesis responsibilities:

- integrate specialist reports into a natural professional investment memo;
- avoid agent-by-agent narration in the main memo;
- reconcile contradictions and key tensions;
- distinguish investment thesis from entry setup;
- explain what is priced in;
- identify where the market may be wrong;
- define Bull / Base / Bear cases without fake probabilities;
- identify risks and thesis breakers;
- provide catalysts, monitoring signals, warning signals, and invalidation triggers;
- produce practical action language with Decision Confidence;
- preserve source discipline, freshness, and evidence limitations.

Action Box should use natural reader-facing labels such as:

```text
For a New Position: Do Not Initiate Yet
For Existing Holders: Maintain / Hold
```

rather than awkward internal labels such as “New Money Action.”

The agent must not provide exact position sizing. It may include only a light qualitative portfolio role.

The final memo includes a reader layer and a verification layer. The main memo should be readable and natural; the Evidence & Data Quality Appendix, evidence pack, and specialist reports preserve auditability.
### 10.5 Sector & Industry Analysis Agent

Likely uses:

- `sector-industry-analysis-method-skill-prd.md` / sector-industry-analysis-method skill;
- `sector-industry-analysis-framework.md` reference;
- investment-analytical-style skill;
- language-policy skill when producing user-facing summaries.

Likely downstream handoffs:

- Structural Winners Discovery Agent, when public-company candidate discovery is needed;
- Equity Agent, when specific companies require deep analysis;
- Valuation & Expectations Agent, when valuation expectations are central;
- Risk / Red Team Agent, when thesis fragility is high;
- Macro Agent, when macro sensitivity is material;
- ETF Agent, when ETF or basket expression is relevant;
- News & Catalysts Agent, when timing depends on fresh events.

The Sector & Industry Analysis Agent should remain a sector diagnostic layer. It should not become a final recommendation, stock-picking, ETF-analysis, or portfolio-construction layer.

### 10.6 Structural Winners Discovery Agent

Likely uses:

- `structural-winner-discovery-method-skill-prd.md` / structural-winner-discovery-method skill;
- `structural-winner-discovery-framework.md` reference;
- investment-analytical-style skill;
- language-policy skill when producing user-facing summaries.

Likely downstream handoffs:

- Financial Statement Analysis;
- Valuation & Expectations;
- Risk / Red Team;
- Company / Equity Deep Dive;
- Investment Committee Agent, only if a final synthesis memo is requested.

The Structural Winners Discovery Agent should remain a candidate-discovery layer, not a final recommendation layer.

## 11. Design Rule for Ambiguous Blocks

When an analytical block appears to belong to multiple agents, classify it using this rule:

```text
If the block asks “what happened / what exists?” → evidence or specialist agent.
If the block asks “how should this method be applied?” → skill.
If the block asks “what does this mean for the final investment decision?” → Investment Committee Agent.
If the block is long, reusable, or checklist-heavy → reference file under a skill.
```

## 12. Closed Architecture Decisions

No blocking architecture questions remain for the design repository. The prior open items are closed as follows:

1. Technical / price-action analysis is deferred and non-core; it is not a full active specialist agent.
2. The active target agent list is defined across routers, asset-class agents, opportunity / discovery agents, cross-functional specialists, and Investment Committee synthesis.
3. The active target skill and reference set is listed in the PRD documentation registry and connected through the package-level PRDs.
4. Reference files are intentionally framework / playbook documents, not implementation files.
5. Existing report naming uses lowercase snake_case and must be registered before new artifacts are introduced.
6. Agent Charter and Skill PRD templates are implementation-planning aids, not design blockers.
7. The source registry is detailed enough for current design; future additions must preserve source tier, freshness, evidence type, claim support, and data-quality status.
8. Workflow diagrams are optional visual aids; text workflows and PRDs remain authoritative.
9. `full-agent-system-build-roadmap.md` and `final-architecture-audit.md` are the active control documents for design completion and audit status.

## 13. Current Working Recommendation

For the full target system, use this principle:

- Keep custom agents concise and role-based.
- Put reusable analytical methods into skills.
- Put long checklists, templates, source lists, and detailed playbooks into references.
- Use workflows to define orchestration.
- Use reports as evidence-backed outputs.
- Use the Investment Committee Agent for final synthesis and decision framing.

This keeps the system modular without turning it into a single giant prompt or an uncontrolled collection of disconnected agents.

## 14. Market Sense Agent — Active Designed Agent

The system includes a Market Sense Agent as a cross-asset market interpretation layer.

### 14.1 Core Role

Core question:

> What logic is the market trading right now, and what hypotheses should be tested?

The Market Sense Agent should not function as an oracle or intuition simulator. It should operate as a disciplined hypothesis engine that converts market reaction, narrative, positioning, macro context, valuation context, and cross-asset behavior into testable hypotheses.

### 14.2 Scope

The Market Sense Agent can operate across:

- individual equities;
- ETFs;
- commodities;
- crypto assets;
- bonds / rates;
- sectors;
- macro themes;
- broad market regimes.

### 14.3 Relationship to Adjacent Agents

| Agent | Role |
|---|---|
| Market Intelligence Agent | Broad market news, event, and data monitoring; answers “what happened?” |
| Market Positioning Agent | Evidence-backed positioning state; visible expectations, revisions, ownership, flows, short interest, options, crowding / neglect indicators, and expectation-bar context |
| News & Catalysts Agent | Asset-specific or theme-specific recent events and catalysts |
| Macro Agent | Macro regime and economic / monetary drivers |
| Market Sense Agent | Interpretation layer; answers “what is the market trying to price, ignore, or reinterpret?” |

Market Positioning is the evidence-backed positioning-state layer. Market Sense is the market-behavior hypothesis layer.

### 14.4 Skill and Reference Structure

```text
Market Sense Agent
  design file: market-sense-agent-prd.md
  uses:
    market-sense-hypothesis-engine-skill-prd.md
    driver-dominance-analysis-skill-prd.md when driver hierarchy is required
    market-pattern-library.md reference
    asset-driver-maps.md reference
    market-positioning report, if available
    news-catalysts report, if available
    macro report, if available
    valuation-expectations report, if expectations matter
    optional technical / price-action input, if available and explicitly requested
```

### 14.5 Key Operating Rules

The Market Sense Agent must separate:

- facts;
- interpretations;
- hypotheses;
- evidence;
- counter-evidence;
- confidence;
- what would disconfirm the hypothesis;
- what to check next.

Each hypothesis should receive both:

- Evidence status: Confirmed / Plausible / Weak / Speculative / Unsupported;
- Confidence: Low / Medium / High.

Vague market psychology phrases are prohibited unless supported by observable evidence and alternative explanations. Examples include “market fears,” “investors are concerned,” “risk-off,” “smart money buying,” “geopolitics is pressuring,” “priced in,” “crowded trade,” “pain trade,” “rotation,” “liquidity rally,” and “narrative exhaustion.”

### 14.6 Expected vs Actual Reaction

When an event or major price move is involved, the Market Sense Agent should include an Expected Reaction vs Actual Reaction block:

```text
Expected reaction:
Actual reaction:
Deviation:
Possible explanation:
Investment implication:
What to verify:
```

### 14.7 Pattern Library

The Market Sense Agent should use a separate `market-pattern-library.md` reference. It should always check internally whether the situation resembles known market patterns, but report only relevant matches.

Pattern match output should include:

- candidate pattern;
- what matches;
- what does not match;
- analogy strength: Weak / Moderate / Strong;
- false-positive risks;
- what to verify next.

### 14.8 Output Types

For a specific asset or theme, the Market Sense Agent should produce `market_sense_report.md` / Market Sense Report with a hypothesis table.

For broad market mode, it should produce `market_sense_brief.md` / Market Sense Brief.

The agent may provide investment implications, but it must not produce a final investment recommendation, position size, or target price. Final decision-making belongs to the Investment Committee Agent.

### 14.9 Workflow Trigger

The Market Sense Agent is optional but recommended in asset-first workflows when market reaction or timing matters.

Triggers include:

- recent large price move;
- earnings or guidance event;
- macro shock;
- geopolitical event;
- crowded narrative;
- valuation extreme;
- user asks why an asset is moving;
- user asks whether now is a good entry point;
- asset behaves strangely relative to expected driver;
- strong divergence between fundamentals and price reaction;
- theme appears overheated or ignored.

## 15. Driver Dominance Analysis Skill — Designed Market Sense Skill

The Market Sense Agent should use a dedicated `driver-dominance-analysis` skill.

This is not a standalone agent in the target architecture. It is a specialized method inside Market Sense.

Core question:

> Which driver is currently dominating the asset's price reaction, and why did that driver matter more than other relevant drivers?

The skill should use:

```text
Market Sense Agent
  uses:
    driver-dominance-analysis skill
      references:
        asset-driver-maps.md
        market-pattern-library.md
```

Key concepts:

- marginal driver;
- level vs change;
- surprise vs expectations;
- priced-in check;
- cross-asset confirmation;
- Driver Battle Matrix;
- dominant driver or dominant driver cluster;
- ignored / overridden drivers;
- alternative explanation;
- qualitative confidence.

The dedicated PRD is:

```text
driver-dominance-analysis-skill-prd.md
```

The driver map reference is:

```text
asset-driver-maps.md
```

Current asset driver maps include:

1. Gold
2. Oil
3. Broad equity index
4. Individual growth equity
5. AI / semiconductor equity
6. Banks / financials
7. Commodity producers
8. Bitcoin
9. Long-duration bonds / TLT
10. Credit / corporate bonds
11. USD / FX-sensitive assets
12. Thematic ETFs

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

## 16. Market Intelligence Agent — Active Designed Agent

The system includes a Market Intelligence Agent as a broad market news brief agent.

Core question:

> What happened across markets that matters for investors?

This agent is separate from Market Sense Agent and News & Catalysts Agent.

```text
Market Intelligence Agent = broad market news and event map.
Market Sense Agent = interpretation and hypothesis layer.
News & Catalysts Agent = asset/theme-specific news and catalysts.
```

The Market Intelligence Agent uses:

```text
market-intelligence-agent-prd.md
market-intelligence-briefing-skill-prd.md
market-news-source-framework.md reference
market-materiality-filter.md reference
```

Default coverage:

```text
Global investor-relevant markets, US-first but global-aware.
```

Default time window:

```text
Last 24 hours, with 48–72h carryover for active drivers.
```

Default output:

```text
market_intelligence_brief.md
```

Item structure:

```md
- What happened:
- Confirmation / source basis:
- Market relevance:
- Concise investor takeaway:
- Affected drivers:
```

The agent may provide concise investor takeaways, but must not perform deep Market Sense interpretation, Driver Dominance analysis, pattern matching, or final investment recommendations.

Dedicated design package:

```text
market-intelligence-agent-prd.md
market-intelligence-briefing-skill-prd.md
market-news-source-framework.md
market-materiality-filter.md
```
