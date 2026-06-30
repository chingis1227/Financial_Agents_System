# Full Agent System Build Roadmap

## Purpose

This file tracks the design status of the full Financial Agent System and the final architecture audit for implementation planning.

The goal is not to produce a rough v0 or shallow v1. The goal is to progressively design the full, coherent version of the system across all required agents, skills, workflows, frameworks, handoffs, evidence rules, and safety guardrails.

## Working Standard

For every agent or major module, the design process should follow this standard:

1. Use `grill-me` before saving major design files.
2. Ask one design question at a time.
3. Provide a recommended answer for each question.
4. Pressure-test the design like an investment professional, not like a generic assistant.
5. Use professional, reliable, and relevant methodology sources where useful.
6. Prefer primary, official, institutional, practitioner, or recognized expert sources.
7. Avoid generic blogs, unsourced summaries, and AI-generated methodology as core sources.
8. Distinguish external professional methodology from this system's own design decisions.
9. Draft in chat first when the design is material.
10. Save files only after explicit user approval.
11. After saving or materially changing files, update connected system documentation.
12. Run consistency checks after every completed package.

The assistant should act as an expert design partner for every question: practical, critical, investment-oriented, and focused on how the system will actually be used.

## Required Documentation Integration

For every agent, skill, framework, workflow, or reference file created or materially changed, update the relevant system-level files.

At minimum, check:

```text
prd.md
system-architecture-map.md
related workflow files
related agent PRDs
related skill PRDs
related frameworks / references
```

A document is not considered finished until it is connected back into the system architecture.

Each completed agent package should normally include:

```text
[agent-name]-agent-prd.md
[agent-name]-method-skill-prd.md
[agent-name]-framework.md
```

Some modules may legitimately be skills or references rather than agents, but that ownership decision must be explicit.

## Required Guardrails for Every Agent / Skill

Every agent and skill should be checked for:

- clear role and purpose;
- core question;
- ownership boundaries;
- non-ownership boundaries;
- required inputs;
- preferred inputs;
- primary output artifact;
- workflow position;
- direct-call behavior where relevant;
- structured handoff fields;
- source hierarchy;
- data freshness rules;
- timestamp discipline;
- evidence quality requirements;
- anti-hallucination rules;
- missing-data handling;
- confidence / limitation handling;
- appendix rules;
- prohibited actions;
- prohibited wording where relevant;
- no hidden recommendations unless the agent explicitly owns final action;
- edge cases and blocked / limited output states where applicable;
- consistency with `prd.md`, `system-architecture-map.md`, and related workflows.

## Professional Source Standard

Use professional sources where they materially improve the design.

Preferred sources include:

- CFA Institute;
- official regulators and exchanges;
- company filings and official reports;
- major asset managers and institutional investment firms;
- recognized practitioner research;
- reputable accounting, audit, consulting, and due diligence firms;
- recognized academics / textbooks / professional frameworks;
- official data provider documentation where data handling is relevant.

Do not overquote sources. Summarize methodology and explain how it informs system design.

## Completed Agent / Module Design Register

## Priority 1 вЂ” Orchestration Foundation

### 1. Intake / Routing Layer

Status: designed package saved. Core files: `master-intake-router-prd.md`, `asset-intake-router-prd.md`, `theme-opportunity-intake-router-prd.md`.

Goal: define how the system starts, classifies requests, and routes work.

Completed checklist:

- design `master-intake-router-prd.md` вЂ” completed;
- design `asset-intake-router-prd.md` вЂ” completed;
- design `theme-opportunity-intake-router-prd.md` вЂ” completed;
- define asset-first / theme-first / mixed / direct-specialist routing вЂ” completed;
- define minimum intake questions вЂ” completed: contextual 1-3 question intake;
- define when agents run sequentially, in parallel, or conditionally вЂ” completed: gated hybrid workflow;
- clarify whether agents communicate directly or through structured handoffs and report artifacts вЂ” completed;
- define direct specialist call behavior вЂ” completed;
- update `prd.md`, `system-architecture-map.md`, and workflow files вЂ” completed at architecture level.

Key design question:

```text
Does the system use a strict pipeline, parallel specialist work, or an orchestrated hybrid workflow?
```

Recommended starting answer:

```text
Orchestrated hybrid workflow: routers classify requests, some evidence and specialist work runs in parallel, mandatory decision-gate work runs before final Investment Committee synthesis, and agents communicate through structured artifacts and challenge requests rather than free-form uncontrolled chat.
```

### 2. Evidence Collector Agent

Status: designed package saved. Core files: `evidence-collector-agent-prd.md`, `evidence-collection-method-skill-prd.md`, `evidence-pack-framework.md`, `source-registry-framework.md`, `evidence-request-protocol.md`.

Goal: create the evidence layer that supports every downstream agent.

Completed checklist:

- design `evidence-collector-agent-prd.md` вЂ” completed;
- design `evidence-collection-method-skill-prd.md` вЂ” completed;
- design `evidence-pack-framework.md` вЂ” completed;
- design `source-registry-framework.md` вЂ” completed;
- design `evidence-request-protocol.md` вЂ” completed;
- define `evidence_pack.md` structure вЂ” completed;
- define source hierarchy and source-tier rules вЂ” completed;
- define source freshness rules вЂ” completed;
- define timestamp discipline вЂ” completed;
- define missing-data, proxy, contradiction, and access-aware protocols вЂ” completed;
- define Complete / Limited / Blocked evidence readiness вЂ” completed;
- define downstream readiness matrix вЂ” completed;
- define analytical vs decision evidence sufficiency вЂ” completed;
- define pre-IC evidence lock вЂ” completed;
- connect to Equity, Valuation, Risk, Sector, Macro, News, Market Positioning, and Investment Committee вЂ” completed at architecture level.

Future work:

- create detailed domain evidence playbooks alongside remaining asset-class and specialist agents;
- add machine-readable evidence registries only if implementation later requires them.

## Priority 2 вЂ” Final Decision Layer

### 3. Investment Committee Agent

Status: designed package saved. Core files: investment-committee-agent-prd.md, investment-committee-synthesis-method-skill-prd.md, investment-committee-memo-framework.md.

Goal: final synthesis and decision memo.

Completed checklist:

- design `investment-committee-agent-prd.md` вЂ” completed;
- design `investment-committee-synthesis-method-skill-prd.md` вЂ” completed;
- design `investment-committee-memo-framework.md` вЂ” completed;
- define final decision ownership вЂ” completed;
- define `final_investment_memo.md` structure вЂ” completed;
- define action box rules вЂ” completed;
- define bull / base / bear synthesis вЂ” completed;
- define valuation and risk treatment вЂ” completed: no automatic specialist veto, but positive actions require sufficient valuation and Risk / Red Team review;
- define no-new-research rule unless explicitly allowed вЂ” completed;
- define no internal agent references in user-facing conclusions вЂ” completed;
- define condition-based action plan вЂ” completed;
- define monitoring plan ownership вЂ” completed;
- define when the final memo must be Complete / Limited / Blocked вЂ” completed.

## Priority 3 вЂ” Market Context Layer

### 4. Market Positioning Agent

Status: designed package saved. Core files: `market-positioning-agent-prd.md`, `market-positioning-method-skill-prd.md`, `market-positioning-framework.md`.

Goal: understand what the market already believes and how it is positioned.

Completed checklist:

- design `market-positioning-agent-prd.md` вЂ” completed;
- design `market-positioning-method-skill-prd.md` вЂ” completed;
- design `market-positioning-framework.md` вЂ” completed;
- define consensus, estimate revisions, ratings, short interest, ownership, flows, and options inputs where available вЂ” completed;
- separate Market Positioning from Market Sense вЂ” completed: evidence-backed positioning state vs market-behavior hypothesis engine;
- define `market_positioning.md` output вЂ” completed;
- define source reliability and data freshness rules вЂ” completed: channel-specific source hierarchy and freshness discipline;
- define handoffs to Valuation, Risk / Red Team, and Investment Committee вЂ” completed;
- define limitations when market positioning data is unavailable вЂ” completed: Complete / Limited / Blocked output plus channel-level statuses.

### 5. News & Catalysts Agent

Status: designed package saved. Core files: `news-catalysts-agent-prd.md`, `news-catalysts-method-skill-prd.md`, `news-catalysts-framework.md`.

Goal: identify what changed recently and what can move the asset next.

Completed checklist:

- design `news-catalysts-agent-prd.md` вЂ” completed;
- design `news-catalysts-method-skill-prd.md` вЂ” completed;
- design `news-catalysts-framework.md` вЂ” completed;
- define event materiality filter вЂ” completed: thesis / expectations / risk / timing / valuation relevance plus Tier 1 / Tier 2 / Tier 3 materiality;
- define freshness window вЂ” completed: 30-day recent news default, up to 90-day active carryover, 3-12 month upcoming catalyst window, and 24h-7d breaking / fast-moving mode;
- define source hierarchy for news вЂ” completed: primary / official preferred, top-tier professional reporting accepted with status labeling, domain source matrix added;
- separate asset-specific News & Catalysts from broad Market Intelligence вЂ” completed;
- define `news_catalysts.md` output вЂ” completed: memo-first report with event table, catalyst map, negative news check, handoffs, and evidence notes;
- include earnings, guidance, M&A, regulatory events, product events, management changes, and upcoming catalysts вЂ” completed through cross-asset event taxonomy and domain overlays;
- define catalyst failure and event-risk handoff to Risk / Red Team and Investment Committee вЂ” completed.

### 6. Macro Agent

Status: designed package saved. Core files: `macro-agent-prd.md`, `macro-analysis-method-skill-prd.md`, `macro-sensitivity-framework.md`, `macro-regime-framework.md`, `macro-indicator-cadence-source-registry.md`, `macro-block-playbooks.md`, `macro-g3-fx-regional-policy-overlay.md`, `macro-expectations-surprise-framework.md`.

Goal: identify macro variables that matter for the asset or thesis.

Completed checklist:

- design `macro-agent-prd.md` вЂ” completed;
- design `macro-analysis-method-skill-prd.md` вЂ” completed;
- design `macro-sensitivity-framework.md` вЂ” completed;
- design `macro-regime-framework.md` вЂ” completed;
- design `macro-indicator-cadence-source-registry.md` вЂ” completed;
- design `macro-block-playbooks.md` вЂ” completed;
- design `macro-g3-fx-regional-policy-overlay.md` вЂ” completed;
- design `macro-expectations-surprise-framework.md` вЂ” completed;
- define coverage: rates, inflation, USD, liquidity, credit, recession risk, policy, commodities where relevant вЂ” completed;
- define standalone modes: Market Pulse, Weekly Delta, Event-Driven, and Full Macro Regime вЂ” completed;
- define embedded `macro_sensitivity.md` output вЂ” completed;
- define asset-specific macro sensitivity rules вЂ” completed through material exposure mapping;
- separate Macro from Market Sense and Market Intelligence вЂ” completed: Macro owns regime / transmission / surprise context; Market Sense owns market-behavior interpretation; Market Positioning owns visible expectations / positioning;
- define source hierarchy, freshness rules, and indicator cadence / priority registry вЂ” completed;
- define scenario / sensitivity handling вЂ” completed: qualitative by default, bounded probabilities only when justified;
- define G3 FX / regional policy overlay for Europe, Japan, EUR/USD, USD/JPY, ECB, and BoJ вЂ” completed;
- define handoffs to Valuation, Risk / Red Team, Market Positioning, Market Sense, Portfolio Fit, and Investment Committee вЂ” completed.

## Priority 4 вЂ” Portfolio / Action Layer

### 7. Portfolio Fit Agent

Status: designed package saved. Core files: `portfolio-fit-agent-prd.md`, `portfolio-fit-method-skill-prd.md`, `portfolio-fit-framework.md`.

Goal: assess the role of the asset in a portfolio without false precision.

Completed checklist:

- design `portfolio-fit-agent-prd.md` вЂ” completed;
- design `portfolio-fit-method-skill-prd.md` вЂ” completed;
- design `portfolio-fit-framework.md` вЂ” completed;
- define portfolio role categories: Core, Core Candidate, Satellite, Tactical, Hedge, Diversifier, Watchlist, Avoid-for-Portfolio вЂ” completed in framework;
- define concentration, overlap, correlation, volatility, liquidity, drawdown, implementation, monitoring, currency, benchmark, and tax-aware caveat considerations вЂ” completed in framework;
- define when portfolio context is required вЂ” completed in framework with no / partial / sufficient context levels;
- prohibit exact position sizing inside Portfolio Fit вЂ” completed; exact sizing remains outside Portfolio Fit scope even when portfolio context is available;
- define `portfolio_fit.md` output вЂ” completed in framework;
- define handoff to Investment Committee вЂ” completed in framework.

## Priority 5 вЂ” Non-Equity Asset-Class Expansion

### 8. ETF Agent

Status: designed package saved. Core files: `etf-agent-prd.md`, `etf-analysis-method-skill-prd.md`, `etf-analysis-framework.md`.

Goal: analyze ETFs as wrappers over underlying exposures and determine whether an ETF is a clean, diluted, risky, overlapping, expensive, or otherwise imperfect vehicle for the intended investment role.

Completed checklist:

- design `etf-agent-prd.md` - completed;
- design `etf-analysis-method-skill-prd.md` - completed;
- design `etf-analysis-framework.md` - completed;
- cover holdings, exposure, fees, tracking, liquidity, issuer, structure, tax / wrapper issues where relevant - completed;
- define full-holdings vs top-holdings discipline - completed: use full issuer holdings when available; otherwise top-holdings analysis with explicit limitations;
- define index, methodology, weighting, rebalance, and reconstitution analysis - completed;
- define active ETF, factor ETF, thematic ETF, commodity ETF, bond ETF, crypto ETF, options-income, leveraged / inverse, synthetic, and volatility-linked special modes - completed;
- define underlying exposure routing - completed;
- define ETF overlap / false-diversification analysis - completed, including peer ETF and portfolio overlap where data allows;
- define peer comparison and ETF discovery / shortlist modes - completed;
- define ETF replacement / substitution and ETF-vs-direct-holding tradeoff modes - completed;
- define `etf_analysis.md` output - completed;
- define ETF-specific source hierarchy and freshness rules - completed: issuer-first with verified market-data fallbacks and source / as-of notes;
- define Complete / Limited / Blocked internal status behavior with non-bureaucratic user-facing limitations - completed;
- define handoffs to Evidence Collector, Sector / Industry, Macro, Fixed Income, Commodity, Crypto, Market Positioning, Portfolio Fit, Risk / Red Team, and Investment Committee - completed.

### 9. Commodity Agent

Status: designed package saved. Core files: `commodity-agent-prd.md`, `commodity-analysis-method-skill-prd.md`, `commodity-analysis-framework.md`, `commodity-family-playbooks.md`.

Goal: analyze commodities and commodity-linked investment exposures.

Completed checklist:

- design `commodity-agent-prd.md` - completed;
- design `commodity-analysis-method-skill-prd.md` - completed;
- design `commodity-analysis-framework.md` - completed;
- design `commodity-family-playbooks.md` - completed;
- cover supply / demand, inventories, futures curve, marginal cost, geopolitics, seasonality, macro sensitivity - completed;
- distinguish physical commodity, futures exposure, ETFs, ETCs, broad commodity baskets, producer equities, miners, royalty / streaming companies, and leveraged / inverse products - completed;
- define `commodity_analysis.md` output - completed;
- define `commodity_market_regime.md` output - completed;
- define source hierarchy and freshness rules - completed;
- define commodity-family playbooks for oil / refined products, natural gas / LNG, gold / precious metals, industrial metals / critical minerals, uranium, agriculture / softs, and broad commodity baskets - completed;
- define actionability labels, specialist verdicts, confidence-by-block, internal Complete / Limited / Blocked status behavior, and non-bureaucratic user-facing limitations - completed;
- update `prd.md`, `system-architecture-map.md`, `asset-intake-router-prd.md`, `source-registry-framework.md`, and connected ETF / valuation architecture references - completed.

### 10. Crypto Agent

Status: designed package saved. Core files: `crypto-agent-prd.md`, `crypto-analysis-method-skill-prd.md`, `crypto-analysis-framework.md`, `crypto-data-source-and-metric-framework.md`.

Goal: analyze crypto assets and crypto-linked investment exposures.

Completed checklist:

- design `crypto-agent-prd.md` - completed;
- design `crypto-analysis-method-skill-prd.md` - completed;
- design `crypto-analysis-framework.md` - completed;
- design `crypto-data-source-and-metric-framework.md` - completed;
- cover network usage, tokenomics, liquidity, custody, regulation, security, adoption, ETF flows, and technical risks - completed;
- define `crypto_analysis.md` output - completed;
- define `crypto_market_regime.md` output - completed;
- define source reliability and freshness rules - completed;
- define guardrails for speculative narratives and weak data - completed;
- define edge cases for weak value capture, ETF-flow reconciliation, ETH/L2 value capture, DeFi yield, token unlocks, stablecoin depegs, hacks, corporate treasuries, and crypto-linked equities - completed;
- update `prd.md`, `system-architecture-map.md`, `asset-intake-router-prd.md`, `source-registry-framework.md`, `evidence-collector-agent-prd.md`, and `valuation-expectations-agent-prd.md` - completed.

### 11. Fixed Income Agent

Status: designed package saved. Core files: `fixed-income-agent-prd.md`, `fixed-income-analysis-method-skill-prd.md`, `fixed-income-framework.md`, `fixed-income-instrument-playbooks.md`.

Goal: analyze bonds and fixed income instruments.

Completed checklist:

- design `fixed-income-agent-prd.md` - completed;
- design `fixed-income-analysis-method-skill-prd.md` - completed;
- design `fixed-income-framework.md` - completed;
- design `fixed-income-instrument-playbooks.md` - completed;
- cover duration, yield, curve, credit risk, spreads, liquidity, issuer quality, convexity, inflation sensitivity - completed;
- define government bond, corporate bond, bond ETF, and credit instrument distinctions - completed;
- define `fixed_income_analysis.md` output - completed;
- define source hierarchy and freshness rules - completed;
- define yield-type discipline, compensation framework, downside scenario set, individual bond vs fund economics, Risk / Red Team escalation, Complete / Limited / Blocked behavior, and fixed-income safety-language guardrails - completed;
- update `prd.md`, `system-architecture-map.md`, `asset-intake-router-prd.md`, `source-registry-framework.md`, `evidence-collector-agent-prd.md`, `etf-agent-prd.md`, and `valuation-expectations-agent-prd.md` - completed.


## Priority 6 — Equity, Discovery, Market Intelligence, and Skill-Only Modules

Status: completed and connected to the active registry.

Completed modules and ownership type:

```text
Equity Agent — agent-owned company-quality analysis
Financial Statement Analysis — skill-owned financial-quality diagnostic
Valuation & Expectations Agent — agent-owned expectations-led public-equity valuation
Risk / Red Team Agent — agent-owned thesis-failure analysis
Sector & Industry Analysis Agent — agent-owned sector diagnostic and sector_context.md output
Structural Winners Discovery Agent — agent-owned candidate discovery
Market Intelligence Agent — agent-owned broad market news brief
Market Sense Agent — agent-owned market-behavior hypothesis layer
Driver Dominance Analysis — skill-owned Market Sense method
```

Core files:

```text
equity-agent-prd.md
equity-company-analysis-method-skill-prd.md
equity-company-analysis-framework.md
equity-deep-dive-workflow.md
financial-statement-analysis-skill-prd.md
valuation-expectations-agent-prd.md
valuation-expectations-method-skill-prd.md
valuation-expectations-framework.md
risk-red-team-agent-prd.md
risk-red-team-method-skill-prd.md
risk-red-team-framework.md
sector-industry-analysis-agent-prd.md
sector-industry-analysis-method-skill-prd.md
sector-industry-analysis-framework.md
structural-winners-discovery-agent-prd.md
structural-winner-discovery-method-skill-prd.md
structural-winner-discovery-framework.md
market-intelligence-agent-prd.md
market-intelligence-briefing-skill-prd.md
market-news-source-framework.md
market-materiality-filter.md
market-sense-agent-prd.md
market-sense-hypothesis-engine-skill-prd.md
market-pattern-library.md
driver-dominance-analysis-skill-prd.md
asset-driver-maps.md
```

Completed checklist:

- define agent vs skill-only ownership — completed;
- define canonical output artifacts, including `sector_context.md`, `market_sense_report.md`, `market_sense_brief.md`, `structural_winners_memo.md`, and `candidate_watchlist.md` — completed;
- classify `industry.md` as a legacy alias only — completed;
- add active structural-winner reference framework — completed;
- connect active modules to `prd.md` and `system-architecture-map.md` — completed;
- keep optional technical / price-action, automation, dashboards, thesis tracking, and monitoring extensions non-blocking.

## Suggested Build Order

1. Intake / Routing Layer.
2. Evidence Collector Agent.
3. Equity / asset-class lead agents and required skill-owned diagnostics.
4. Valuation & Expectations and Risk / Red Team decision gates.
5. Market Positioning, News & Catalysts, Macro, Market Intelligence, and Market Sense context layers.
6. Portfolio Fit where portfolio context is decision-relevant.
7. Investment Committee Agent for final synthesis.
8. Optional future extensions only after active core workflows are stable.

## Final Architecture Audit

Status: completed as of 2026-06-27. Audit file: `final-architecture-audit.md`.

After all major agents are designed, run a final architecture audit before technical planning starts.

The audit must verify:

- exact system operating sequence;
- sequential vs parallel vs conditional execution;
- agent communication and handoff rules;
- direct-call behavior;
- workflow blockers;
- artifact names;
- source and freshness discipline;
- anti-hallucination rules;
- prohibited actions and wording;
- edge cases;
- Complete / Limited / Blocked statuses;
- consistency across `prd.md`, `system-architecture-map.md`, workflows, agent PRDs, skill PRDs, and frameworks.


## Comprehensive Documentation Audit Update

Comprehensive documentation audit update: completed on 2026-06-27.

Closed items:

- removed UTF-8 BOM markers from active Markdown files for consistent heading detection;
- replaced stale "future" wording for Market Intelligence and technical / price-action roles;
- converted open PRD and architecture questions into closed decisions or non-blocking extensions;
- added an active documentation registry to `prd.md`;
- clarified that Technical / price-action analysis is deferred and non-core;
- connected Market Sense, Market Intelligence, Equity, Financial Statement Analysis, Valuation, Risk / Red Team, Sector & Industry, Structural Winners, and Driver Dominance exact design files back into `prd.md` and `system-architecture-map.md`;
- classified backup, reminder, and scratch materials as non-active sources of truth;
- added the active `structural-winner-discovery-framework.md` reference and normalized output artifact naming.

