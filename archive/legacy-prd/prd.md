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

### 3.1 Human-Readable Investment Report Standard

All user-facing reports must read like natural professional investment writing, not like internal system transcripts, agent logs, or robotic summaries.

The intended reader experience is:

> After reading the report, the reader should understand the investment picture, the key evidence, the main trade-offs, the decision logic, and what matters next without needing to inspect every underlying specialist file.

Reports should be structured and disciplined, but they should not feel like a machine-filled template. They should be suitable to send to a serious investment reader who expects clear reasoning, natural language, and practical judgment.

All agents should:

- integrate evidence into a coherent investment narrative rather than listing disconnected findings;
- use natural investment language such as “valuation,” “risk profile,” “macro backdrop,” “competitive position,” “market expectations,” “catalysts,” and “portfolio role”;
- provide enough context for the reader to enter the topic and understand why the conclusion follows;
- preserve the most important and relevant findings from specialist work without turning the report into an agent-by-agent recap;
- explain tensions, trade-offs, and implications in plain professional language;
- maintain clear structure while avoiding a dry, overly compressed, or form-like style;
- avoid generic AI phrasing, filler, and vague statements that do not improve investment understanding.

Agents should not write user-facing reports as:

- internal process logs;
- “Agent A said / Agent B said” summaries;
- disconnected bullet dumps;
- one-line conclusions without supporting context;
- long undisciplined essays that bury the decision.

Specialist reports, appendices, and evidence notes may identify source reports, files, and analytical inputs for traceability. The main user-facing narrative should synthesize those inputs naturally.

### 3.2 Decision Confidence Standard

When an agent presents an investment action, recommendation, prioritization, or decision-relevant conclusion, it should not use a bare conviction label without explanation.

The preferred user-facing construct is:

```text
Decision Confidence: High / Moderate / Low / Insufficient Basis
Why: [plain-language explanation of why confidence is at this level]
What would raise confidence: [specific evidence, price move, catalyst, risk reduction, or confirmation]
What would lower confidence: [specific deterioration, missing evidence, adverse data, or thesis-breaker]
```

Decision Confidence is not a probability forecast and should not be presented as mathematical precision. It explains how strongly the system stands behind the decision based on evidence quality, valuation, risk/reward, thesis durability, uncertainty, and missing data.

Agents should avoid vague wording such as:

- “Conviction: Medium” without explanation;
- “Confidence: High” without saying why;
- unexplained Low / Medium / High labels;
- false precision disguised as confidence.

For specialist reports that do not own the final investment action, confidence should describe the strength of the analytical finding or evidence base, not a buy/sell recommendation. The final Investment Committee memo should use Decision Confidence in the Action Box whenever it presents a final action.

### 3.3 Action Label Practical Meaning Standard

When an agent presents an action label, recommendation label, status label, priority label, or similar decision label, the label must be explained in practical terms.

The system should avoid labels that are technically correct but not useful to the reader, such as:

- “Watchlist / Wait” without saying what waiting means;
- “Hold” without saying what to do with an existing position;
- “High Priority” without saying what should happen next;
- “Limited” without explaining the practical limitation.

For investment actions, the preferred user-facing construct is:

```text
Action: [Buy / Add / Hold / Watchlist / Avoid / Reduce / Blocked / etc.]
Practical Meaning: [what the reader should practically do or not do]
Primary Reason: [the main reason for the action]
Decision Confidence: [High / Moderate / Low / Insufficient Basis + why]
Reassessment Trigger: [what would cause the action to be revisited]
```

For asset-specific investment memos, the system should use natural reader-facing labels when the action differs depending on whether the reader already owns the asset:

```text
For a New Position: [action label]
For Existing Holders: [action label]
```

The system should avoid awkward internal labels such as “New Money Action” in the main memo.

Examples:

```text
Action: Do Not Initiate Yet
Practical Meaning: Do not initiate a new position at the current price. Keep the asset under review and reassess if valuation improves or evidence strengthens that the market is underestimating durable growth.
```

```text
Action: Phased Entry
Practical Meaning: A small initial position may be reasonable, but avoid full allocation until valuation improves or the next earnings report confirms demand durability.
```

```text
Action: Blocked — No Decision
Practical Meaning: Do not make an investment decision from the current evidence base. The missing or unreliable data must be resolved before a responsible action can be recommended.
```

The goal is to make every action understandable to a reader who does not know the system’s internal labels.

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

The core target system should support the following asset classes:

1. Equities
2. ETFs
3. Commodities, including oil
4. Crypto assets
5. Bonds / fixed income instruments

Rates should not be treated as a separate primary asset route by default. Rates are a macro factor and should be handled by the Macro Agent because they influence equities, commodities, crypto, bonds, and ETFs.

## 7. ETF Treatment

ETFs should be treated as wrappers over underlying exposures, not as a single generic asset type.

Dedicated ETF design documents:

```text
etf-agent-prd.md
etf-analysis-method-skill-prd.md
etf-analysis-framework.md
```

The ETF workflow should include both:

1. ETF-specific wrapper analysis.
2. Underlying exposure analysis.

### 7.1 ETF-Specific Analysis

For ETFs, the system should collect and analyze:

- exact instrument identity, including issuer, exchange, domicile, ISIN / CUSIP where available, share class, trading currency, accumulation / distribution policy, and hedging status;
- holdings, using full issuer holdings files where available;
- top holdings and concentration when full holdings are unavailable, with explicit limitations;
- index, methodology, weighting scheme, rebalance, and reconstitution rules;
- active ETF process and style drift where relevant;
- expense ratio in context of peers and exposure quality;
- AUM, fund age, issuer quality, and closure risk;
- performance history as backward-looking evidence, not as a forward-looking recommendation;
- tracking difference and tracking error where relevant;
- liquidity, bid-ask spread, premium / discount, and implementation caveats;
- yield source and sustainability for income-oriented ETFs;
- tax, domicile, wrapper, listing, and access caveats where relevant;
- ETF-specific risks;
- overlap with other ETFs, existing portfolio holdings, and look-through exposures where data allows.

### 7.2 Underlying Exposure Routing

After identifying the ETF's exposure, the system should route to the relevant underlying playbook:

- equity ETF -> equity / sector / industry route;
- commodity ETF -> ETF wrapper analysis plus commodity route;
- bond ETF -> ETF wrapper analysis plus fixed income / macro / rates route;
- crypto ETF -> ETF wrapper analysis plus crypto route;
- thematic ETF -> ETF wrapper analysis plus theme, holdings, and industry route;
- factor ETF -> ETF methodology / factor exposure analysis plus market / sector context where relevant;
- multi-asset ETF -> allocation-style exposure route;
- active ETF -> ETF active-management mode plus relevant underlying route;
- leveraged, inverse, options-income, synthetic, volatility-linked, or derivative-heavy ETF -> ETF special-risk mode plus Risk / Red Team when material.

### 7.3 ETF Agent Role

The ETF Agent owns ETF wrapper quality, exposure diagnosis, holdings analysis, methodology interpretation, peer comparison, overlap / false-diversification analysis, and vehicle-quality verdict.

It does not own final buy / sell / hold recommendations, exact sizing, final portfolio suitability, tax advice, legal advice, full company valuation, full macro analysis, full commodity thesis, full crypto thesis, full fixed-income credit / duration model, or final Investment Committee synthesis.

The primary ETF artifact is:

```text
etf_analysis.md
```

It is modular and may run as a single ETF review, ETF comparison, ETF discovery / shortlist, ETF overlap analysis, ETF replacement / substitution review, thematic purity check, complex ETF special-risk review, active ETF review, or ETF-vs-direct-holding wrapper tradeoff.

### 7.4 ETF Data Freshness and Source Discipline

For current ETF investment analysis, the system should refresh decision-relevant ETF data when internet access is available:

- holdings;
- AUM;
- expense ratio;
- methodology;
- performance;
- yield;
- liquidity;
- premium / discount;
- peer metrics;
- overlap inputs.

Primary sources should be issuer, index provider, prospectus / filings, official exchange, and official NAV / premium-discount sources. Reputable market-data providers, Morningstar, ETF.com, ETF Database, ETF Research Center, and similar tools may be used as fallback or comparison sources. ETFRC overlap may be used as a secondary overlap source / sanity check, not as a substitute for issuer holdings where available.

### 7.5 ETF Output Discipline

ETF Agent may produce investment implications and a vehicle-quality verdict such as:

```text
clean broad-market core candidate
pure but concentrated thematic satellite
diluted theme proxy
poor diversifier due to high overlap
income product with NAV erosion risk
tactical trading vehicle, not core holding
```

ETF Agent must not issue final action language such as buy, sell, hold, exact allocation, guaranteed income, risk-free, best ETF overall, or perfect diversification.

## 8. Intake and Routing Architecture

The Intake and Routing layer is now defined by three dedicated PRDs:

```text
master-intake-router-prd.md
asset-intake-router-prd.md
theme-opportunity-intake-router-prd.md
```

### 8.1 Master Intake Router

The system should have a top-level Master Intake Router.

Its purpose is not to analyze the asset or theme. Its purpose is to classify the incoming request and decide which intake route should handle it.

The Master Intake Router should classify requests into:

1. Asset-first requests
2. Theme-first requests
3. Mixed requests
4. Direct specialist calls
5. Comparison requests
6. Evidence / source verification requests
7. Educational requests
8. Update / refresh requests
9. Monitoring requests
10. Portfolio-role requests
11. Unclear requests

### 8.2 Classification Behavior

The Master Intake Router should classify the request automatically when the intent is clear.

If the request is unclear or ambiguous, it should ask a concise clarifying question or offer a short menu of likely routes.

Examples:

- “Analyze Nvidia” → Asset-first workflow.
- “Defense spending is rising — where can I invest?” → Theme-first workflow.
- “Analyze Lockheed Martin as a beneficiary of rising defense budgets” → Asset analysis with thematic context.
- Ambiguous request → ask whether the user wants specific asset analysis or opportunity discovery around a theme.

The system should use contextual intake, not a mechanical questionnaire:

```text
Ask 1-3 relevant questions when context is materially incomplete.
If the user already provided enough context, route immediately.
Record missing non-blocking context rather than stopping the workflow unnecessarily.
```

### 8.3 Asset Intake Router

For asset-first requests, the Asset Intake Router should identify the asset class, resolve ambiguous instruments, determine whether the request is full or focused, and collect only the most useful missing context.

Potential intake fields:

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

These are not mandatory questions in every interaction. The router should normally ask no more than three relevant questions before launch.

Output depth should not be a default intake parameter. Agents should operate at one standard working depth unless the workflow explicitly supports a different output profile. Output profiles such as quick brief, standard memo, and deep dive may be added as explicit workflow options later.

Generic asset analysis defaults to the full asset-first investment workflow. Focused requests remain focused:

```text
“Analyze Nvidia” -> full asset-first workflow
“Should I buy Nvidia?” -> full asset-first workflow
“Nvidia valuation only” -> valuation route
“What are Tesla's risks?” -> risk route
“Why did Bitcoin rise today?” -> market reaction route
```

ETFs should be routed as wrapper analysis plus underlying exposure analysis. Bonds and bond ETFs require fixed income analysis plus macro context. Commodities and crypto assets require their own asset-class routes rather than being reduced to generic macro or equity analysis.

### 8.4 Theme / Opportunity Intake Router

For theme-first requests, the system should clarify:

- the theme, event, or narrative;
- the desired investment angle;
- the relevant geography or market if applicable;
- the investment horizon if known;
- whether the user wants broad opportunity discovery or already has candidate assets in mind.

The result should be an Opportunity Discovery Memo, not an immediate final buy/sell recommendation.

Theme-first requests default to opportunity discovery:

```text
theme -> transmission channels -> value chain -> beneficiaries / losers -> investable instruments -> candidate shortlist -> recommended deep dives
```

Requests for sectors, industries, or value chains should route to Sector / Industry Analysis. Requests for “future winners,” “hidden beneficiaries,” “next X,” or structural winners should route to Structural Winners Discovery. Requests for “top ideas” inside a theme should route to thematic ranking, not full asset-level analysis of every candidate.

Theme-first outputs may recommend candidates for deeper work, but they do not make a candidate investment-actionable. A candidate becomes investment-actionable only after asset-level evidence, valuation, risk review, and final synthesis.

### 8.5 Routing Control Rules

The system should follow these routing control rules:

- Central routing / orchestration controls agent launch.
- Agents may recommend next checks, but they do not launch other agents by themselves.
- Direct specialist calls remain scoped and may recommend handoffs without automatically expanding into a full workflow.
- Narrow requests must not be expanded into full workflows unless the user explicitly requests a full decision, the selected route already includes mandatory downstream steps, or the user approves the expansion.
- If a request contains several major tasks, the router should propose an ordered staged plan and ask for confirmation.
- If a request depends on current prices, recent news, earnings, market reaction, or an update after an event, fresh data is mandatory.
- Requests about consensus, crowding, ownership, flows, short interest, or what the market appears to believe should route to Market Positioning rather than being treated as generic valuation.
- Requests that provide a user thesis should route to thesis testing before being expanded into asset, valuation, risk, macro, or theme work.
- Explicit user requests for quick, brief, deep, or detailed output may change format, but they must not lower evidence requirements for investment actions.
- Positive investment actions require sufficient valuation work, risk review, and evidence readiness. If these gates are unavailable, the route should produce a Limited or Blocked output rather than an unsupported action.
- If a request is impossible or unsafe as stated, the router should block the problematic part and offer a safe alternative such as scenario analysis, evidence verification, or a list of missing data.

### 8.6 Intake Artifact

For full workflows, the router should create a short `intake.md` or equivalent structured intake block.

It should include:

```text
Original request
Route classification
Selected route
Asset / theme / instrument
User intent
Known horizon
Known portfolio context
Clarifying questions and answers
Missing context
Freshness requirement
Planned downstream modules
Scope limitations
Language mode
```

For direct specialist calls or short focused outputs, a separate `intake.md` is not mandatory, but the report should still state scope, exclusions, missing context, and next possible steps.

## 9. Agent Architecture

The system should use a hybrid architecture with three analytical agent categories:

1. Asset-class agents
2. Opportunity / Discovery agents
3. Cross-functional agents

### 9.1 Asset-Class Agents

Core target asset-class agents:

- Equity Agent
- ETF Agent
- Commodity Agent
- Crypto Agent
- Fixed Income Agent

These agents understand the specific structure, risks, and analytical logic of each asset class.

### 9.1A ETF Agent Role

The ETF Agent is the ETF wrapper, exposure-quality, and overlap-analysis layer.

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

It owns:

- ETF identity verification;
- holdings breakdown and concentration analysis;
- index / methodology / weighting / rebalance review;
- active ETF, factor ETF, thematic ETF, and complex ETF special modes;
- fee, AUM, liquidity, issuer, tracking, yield, premium / discount, and structure review;
- peer comparison by use-case fit;
- overlap and false-diversification analysis;
- ETF discovery / shortlist, replacement / substitution, and ETF-vs-direct-holding wrapper tradeoff modes;
- vehicle-quality verdict and role-candidate framing;
- structured handoffs to Evidence Collector, Sector / Industry, Macro, Fixed Income, Commodity, Crypto, Market Positioning, Portfolio Fit, Risk / Red Team, and Investment Committee.

It does not own final buy / sell / hold recommendations, exact position sizing, final portfolio suitability, personalized tax advice, legal advice, full underlying asset-class thesis, or final Investment Committee synthesis.


### 9.1B Equity Agent Role

The Equity Agent is now defined as the lead company-analysis agent for public listed equities.

It answers:

```text
Is this a good business, why, what does the thesis depend on, what could change the view, and what must be checked separately before a final investment decision?
```

The Equity Agent owns company-quality analysis, including business model, revenue model, customer and demand logic, competitive position, moat, management quality, company-specific vulnerabilities, key thesis variables, and monitoring signals.

It does not own final buy/sell recommendations, target prices, position sizing, full valuation, full risk verdict, market timing, portfolio fit, or final synthesis.

Dedicated Equity Agent design documents:

- `equity-agent-prd.md`
- `equity-company-analysis-method-skill-prd.md`
- `equity-company-analysis-framework.md`
- `equity-deep-dive-workflow.md`

The Equity Deep Dive Workflow is separate from the Equity Agent. The Equity Agent produces `equity_company_analysis.md`; the full workflow coordinates evidence collection, financial statement analysis, sector context, valuation, market positioning, news, macro, risk red-team work, and final Investment Committee synthesis.

Financial Statement Analysis is a skill-owned module, not a separate agent. It produces `financial_statement_analysis.md` through `financial-statement-analysis-skill-prd.md`; Equity, Valuation & Expectations, Risk / Red Team, Fixed Income, and Investment Committee may consume that output.



### 9.1C Commodity Agent Role

The Commodity Agent is the commodity asset-class specialist. It analyzes commodities and commodity-linked exposures through physical supply / demand, inventories, reserves, futures curve, marginal cost, geopolitics, policy, storage / logistics, macro sensitivity, valuation-context, and instrument-aware lenses.

Dedicated design documents:

```text
commodity-agent-prd.md
commodity-analysis-method-skill-prd.md
commodity-analysis-framework.md
commodity-family-playbooks.md
```

It answers:

```text
What is the real commodity market telling us, and does that support or weaken the investment thesis for this commodity exposure?
```

Primary output artifacts:

```text
commodity_analysis.md
commodity_market_regime.md
```

The Commodity Agent owns commodity identity, physical demand and supply analysis, demand mapping by industry / country / central bank / strategic reserve buyer where material, supply mapping by region / producer group / cost curve / geology / project pipeline / OPEC or policy actor, inventory and reserve distinction, futures curve / roll / carry interpretation, commodity-specific macro sensitivity, geopolitics and policy transmission, storage / logistics / transport analysis, substitution risk, commodity valuation context without precise price targets, first-pass commodity-specific risk and trap checks, actionability labels without buy / sell / hold recommendations, and structured handoffs.

It does not own final buy / sell / hold recommendations, exact position sizing, full ETF wrapper analysis, full equity underwriting of producers / miners / energy companies, full portfolio suitability, full macro regime analysis, full market positioning analysis, personalized tax or legal advice, precise fair value targets, or final Investment Committee synthesis.

Commodity analysis is physical-balance-first. Narratives such as AI copper demand, central bank gold buying, OPEC control, energy transition demand, or uranium scarcity must be translated into testable data claims before they support a thesis.

Key ownership boundaries:

- ETF Agent owns commodity ETF / ETC wrapper quality; Commodity Agent owns the underlying commodity thesis and commodity-specific roll / curve implications.
- Equity Agent owns full analysis of commodity producers, miners, energy companies, royalty companies, and streamers; Commodity Agent owns the underlying commodity cycle / beta.
- Macro Agent owns the full macro regime; Commodity Agent owns commodity-specific macro sensitivity.
- Market Positioning Agent owns deep consensus, positioning, and crowding work; Commodity Agent owns basic commodity-relevant positioning checks.
- Risk / Red Team owns independent thesis-breaker challenge; Commodity Agent owns first-pass commodity-native trap checks.
- Investment Committee owns final action.

### 9.1D Crypto Agent Role

The Crypto Agent is the crypto asset-class specialist. It analyzes direct crypto assets and crypto-linked exposures through network fundamentals, tokenomics, value capture, market structure, liquidity, regulation, security, custody, macro transmission, and valuation-context lenses.

Dedicated design documents:

```text
crypto-agent-prd.md
crypto-analysis-method-skill-prd.md
crypto-analysis-framework.md
crypto-data-source-and-metric-framework.md
```

It answers:

```text
Is this crypto asset or crypto-market setup investable on a fundamental, market-structure, regulatory, liquidity, security, and valuation-context basis?
```

Primary output artifacts:

```text
crypto_analysis.md
crypto_market_regime.md
```

The Crypto Agent owns crypto asset identity, economic classification, investment-grade viability gates, tokenomics, value capture, network economics, DeFi / staking / lending economics as a risk layer, on-chain evidence interpretation, derivatives and leverage setup, ETF-flow and structural demand / supply interpretation, corporate crypto treasury impact, stablecoin liquidity, tokenization / RWA value-capture tests, BTC and ETH overlays, crypto-specific macro / liquidity transmission, regulatory impact, security / custody / protocol risk, scenario setup, monitoring triggers, and structured handoffs.

It does not own final buy / sell / hold recommendations, exact position sizing, tax advice, legal advice, custody setup instructions, operational DeFi or staking recommendations, final ETF wrapper analysis, full equity analysis for crypto-linked stocks, full macro regime analysis, final risk verdict, or final Investment Committee synthesis.

Crypto Agent uses a strict source and freshness discipline. Setup-sensitive questions require fresh data for price, flows, funding, open interest, liquidations, stablecoin liquidity, regulatory events, hacks / depegs, and ETF flows. Weak, stale, dashboard-derived, paywalled, social-media-based, or proxy-level evidence must reduce conclusion strength or produce a Limited / Blocked output.

Default horizon is 6-36 months for ordinary crypto investment analysis, with 3-5 year framing allowed for BTC or ETH long-term thesis work. Current-entry or fast-moving questions require a separate setup overlay because the investment thesis is not the same as the current entry setup.

Key guardrail:

```text
Crypto asset quality != current market setup != final investment action.
```

### 9.1E Fixed Income Agent Role

The Fixed Income Agent is the fixed-income asset-class specialist. It analyzes bonds, bond funds, bond ETFs, credit instruments, and fixed-income-linked exposures through yield, duration, curve, credit, spread, liquidity, structure, optionality, inflation, FX, and downside-scenario lenses.

Dedicated design documents:

```text
fixed-income-agent-prd.md
fixed-income-analysis-method-skill-prd.md
fixed-income-framework.md
fixed-income-instrument-playbooks.md
```

It answers:

```text
Does this fixed-income instrument or exposure offer adequate risk-adjusted compensation for the yield, duration, credit, spread, liquidity, structure, inflation, FX, and downside risks being taken?
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

The Fixed Income Agent owns fixed-income instrument classification, yield and spread interpretation, duration / curve / convexity risk, issuer and obligor credit quality, spread compensation, liquidity, call / prepayment / extension risk, individual bond vs fund economics, fixed-income compensation / relative-value assessment, downside scenario analysis, specialist verdicts, monitoring triggers, and structured handoffs.

It does not own final buy / sell / hold recommendations, exact sizing, final portfolio suitability, personalized tax advice, legal advice, full macro regime analysis, ETF wrapper-quality analysis, full private-credit underwriting without documents, structured-credit cash-flow modeling, or final Investment Committee synthesis.

Key ownership boundaries:

- Macro Agent owns rates, inflation, policy, FX, liquidity, and macro regime; Fixed Income Agent owns how those drivers affect a specific instrument or fixed-income exposure.
- ETF Agent owns bond ETF wrapper quality; Fixed Income Agent owns underlying fixed-income exposure quality.
- Portfolio Fit Agent owns final portfolio suitability; Fixed Income Agent provides role-candidate framing.
- Risk / Red Team owns independent thesis-breaker challenge; Fixed Income Agent escalates high-yield, distressed, private, structured, subordinated, opaque, or asymmetric cases.
- Investment Committee owns final action.

Key guardrail:

```text
Yield alone is never sufficient evidence of attractiveness.
```



### 9.2 Opportunity / Discovery Agents

Core target opportunity / discovery agent:

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

Core target cross-functional agents:

- Evidence Collector Agent
- Macro Agent
- Market Intelligence Agent
- News & Catalysts Agent
- Market Sense Agent
- Valuation & Expectations Agent
- Risk / Red Team Agent
- Sector & Industry Analysis Agent
- Market Positioning Agent
- Portfolio Fit Agent
- Investment Committee Agent

Technical / price-action analysis is not a core active agent in the current target system. It is a deferred optional input that may be added later only as a lightweight timing and risk lens. It must not become a trading system, override fundamentals, or take final-action ownership from the Investment Committee Agent.

Additional agents are permitted only if their function is reusable, decision-relevant, and does not duplicate existing responsibilities.

### 9.3A Macro Agent Role

The Macro Agent is the macro regime, macro transmission, and asset-specific macro sensitivity layer.

It answers:

```text
Which macro variables, policy shifts, liquidity conditions, FX moves, and cross-asset signals materially affect this investment decision, and through what transmission channel?
```

The agent can run as a standalone macro analyst or as an embedded specialist in asset, sector, theme, ETF, commodity, crypto, fixed income, portfolio, and Investment Committee workflows.

Core modes:

```text
Market Pulse Mode
Weekly Delta Mode
Event-Driven Mode
Monthly / Full Macro Regime Mode
Asset-Specific Macro Sensitivity Mode
```

Standalone Macro outputs:

```text
macro_market_pulse.md
macro_weekly_delta.md
macro_event_update.md
macro_regime_baseline.md
```

Embedded workflow output:

```text
macro_sensitivity.md
```

Internal state files:

```text
macro_block_states/
  growth_labor_state.md
  inflation_commodities_state.md
  rates_fed_curve_state.md
  liquidity_credit_state.md
  cross_asset_confirmation_state.md
  g3_fx_regional_policy_state.md
```

The Macro Agent uses internal playbooks for Growth & Labor, Inflation & Commodities, Rates / Fed / Yield Curve, Liquidity & Credit, and Cross-Asset Macro Confirmation. It also uses conditional overlays for G3 FX & Regional Policy and Macro Expectations / Surprise.

The agent must separate `Confirmed Macro Regime` from `Current Risk Overlay`. Regime changes require professional combined evidence across depth, diffusion, duration, transmission, and market discounting; one data print or one market move normally changes risk overlay or trigger watch rather than confirmed regime.

The Macro Agent must follow strict freshness and anti-hallucination discipline. Fresh market data are mandatory for current market-sensitive conclusions about yields, FX, DXY, EUR/USD, USD/JPY, oil, gold, volatility, credit spreads, and market-implied policy paths. Slow official releases may be carried forward only with timestamp discipline.

The agent does not own final buy / sell / hold decisions, exact position sizing, final valuation, final priced-in / mispriced verdicts, single-security positioning, technical trading signals, final risk verdicts, or final Investment Committee synthesis.

Dedicated Macro design documents:

```text
macro-agent-prd.md
macro-analysis-method-skill-prd.md
macro-sensitivity-framework.md
macro-regime-framework.md
macro-indicator-cadence-source-registry.md
macro-block-playbooks.md
macro-g3-fx-regional-policy-overlay.md
macro-expectations-surprise-framework.md
```

### 9.3B Portfolio Fit Agent Role

The Portfolio Fit Agent is the portfolio-role and portfolio-constraint layer.

It answers:

```text
What role could this asset play in the portfolio, and what portfolio risks does it add or reduce?
```

It separates generic asset role from user-specific portfolio fit. It may assess overlap, concentration, diversification, horizon-fit, role-objective match, liquidity, drawdown, implementation burden, currency, benchmark relevance, and tax-aware caveats where material.

It does not own final buy / sell / hold decisions, exact position sizing, target portfolio weights, portfolio construction from scratch, full valuation, full risk verdict, tax advice, fiduciary suitability, or final Investment Committee synthesis.

Dedicated Portfolio Fit design documents:

```text
portfolio-fit-agent-prd.md
portfolio-fit-method-skill-prd.md
portfolio-fit-framework.md
```

### 9.3C News & Catalysts Agent Role

The News & Catalysts Agent is the asset-specific and theme-specific event materiality layer.

The dedicated design is defined in:

```text
news-catalysts-agent-prd.md
news-catalysts-method-skill-prd.md
news-catalysts-framework.md
```

It answers:

```text
What changed recently, what still matters, what could move the asset next, and what event risks or catalyst failures must the investment process consider?
```

The agent is cross-asset with domain-specific modes for equities, ETFs, commodities, crypto, fixed income, sectors, and themes.

It owns:

- recent event review;
- active carryover event identification;
- upcoming catalyst mapping;
- event materiality;
- negative news check with source and window boundaries;
- directional event impact assessment;
- catalyst failure flags;
- structured handoffs to Evidence Collector, Valuation & Expectations, Risk / Red Team, Market Positioning, Market Sense, Macro, asset-class agents, and Investment Committee.

It does not own:

- final investment recommendations;
- target prices;
- full valuation modeling;
- position sizing;
- hedge sizing;
- trading instructions;
- full Market Sense interpretation.

The primary output is:

```text
news_catalysts.md
```

For full asset-first investment workflows, News & Catalysts is normally required as a freshness and timing module. For focused specialist workflows, it is conditional and should run when recent events, upcoming catalysts, event risk, or timing materially affect the scoped question.

### 9.4 Valuation & Expectations Agent Role

The currently designed Valuation & Expectations Agent module evaluates whether the current market price of a public equity is justified by realistic expectations for growth, margins, cash flows, returns on capital, risk, and required return.

For commodities, the Commodity Agent owns commodity valuation context such as price support versus physical balance, curve, inventories, marginal / incentive cost, and macro sensitivity, while avoiding precise final price targets and final investment actions.

For crypto assets, the Crypto Agent owns crypto valuation context and implied expectations analysis, while avoiding precise final price targets and final investment actions.

For fixed income instruments, the Fixed Income Agent owns fixed-income compensation / relative-value analysis: whether yield, spread, carry, and downside adequately compensate for duration, credit, liquidity, structure, inflation, FX, and scenario risk.

ETF valuation remains outside the current detailed valuation module unless a separate reusable need is identified.

It answers:

```text
What is already priced in, and are those expectations reasonable?
```

The agent follows an expectations-adjusted value doctrine. It is reverse-expectations-led: DCF, multiples, peer analysis, historical ranges, and scenario valuation are tools used to understand what the current price implies, not standalone sources of truth.

The Valuation & Expectations Agent owns:

- current valuation snapshot;
- absolute and quality-adjusted valuation;
- earnings, EPS, cash-flow, enterprise-value, and asset-based valuation where relevant;
- sector-specific valuation method selection;
- market-implied expectations;
- reverse DCF / reverse expectations when economically meaningful;
- scenario-implied valuation ranges, not single-point target prices;
- return bridge;
- valuation asymmetry;
- margin of safety as an input to Investment Committee;
- valuation risk flags;
- misleading metric flags;
- value trap, quality trap, and growth trap tests;
- terminal value and long-duration dependency checks;
- multiple durability assessment;
- liquidity, float, market-access, regulatory/legal, and SOTP valuation caveats where material;
- monitoring signals tied to implied expectations;
- structured handoff to Risk / Red Team and Investment Committee.

It does not own final buy/sell/hold recommendations, final target prices, position sizing, portfolio construction, technical timing, final risk verdict, full macro thesis, full legal/risk adjudication, or final Investment Committee synthesis.

Dedicated Valuation & Expectations design documents:

- `valuation-expectations-agent-prd.md`
- `valuation-expectations-method-skill-prd.md`
- `valuation-expectations-framework.md`

The agent produces `valuation_expectations.md`. It may classify the output as `Complete Valuation`, `Limited Valuation`, or `Blocked Valuation` depending on data availability and reliability. It must follow source hierarchy, timestamp discipline, and anti-hallucination rules; unsupported valuation numbers must not be invented.

### 9.5 Sector & Industry Analysis Agent Role

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

It should produce `sector_context.md` in embedded company workflows and `sector_evidence_pack.md`, `sector_industry_memo.md`, `sector_investment_map.md`, and `sector_monitoring_plan.md` in standalone sector workflows. `industry.md` is a legacy alias only; downstream agents should first look for `sector_context.md` and use `industry.md` only when reading older work folders.

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

### 9.6 Risk / Red Team Agent Role

The Risk / Red Team Agent is the designed thesis-breaker module for public listed equity analysis. It challenges the combined company-quality and valuation thesis; it must not produce a generic risk list or force a bearish case without material evidence and a clear mechanism.

It answers:

```text
How can this investment thesis fail, and what evidence would show that it is failing?
```

The agent owns:

- thesis failure map;
- critical assumption challenge;
- 3-7 material and economically plausible failure paths, with top-3 depth;
- downside scenario integrity check and bear case challenge;
- thesis invalidation triggers and early warning indicators;
- accounting and governance red flag gate;
- balance sheet and liquidity fragility gate;
- market expectations and positioning risk gate;
- risk watchlist for potentially material but immature risks;
- tail risks only when thesis-relevant;
- excluded / deprioritized risk rationale;
- risk challenge verdict;
- structured challenge requests to upstream work and Investment Committee.

The agent does not own final buy/sell/hold recommendations, target prices, position sizing, portfolio construction, full valuation models, full macro thesis, final legal adjudication, or final Investment Committee synthesis.

Dedicated Risk / Red Team design documents:

- `risk-red-team-agent-prd.md`
- `risk-red-team-method-skill-prd.md`
- `risk-red-team-framework.md`

The agent produces `risk_red_team.md`. It may classify the output as `Complete Risk Review`, `Limited Risk Review`, `Blocked Risk Review`, or `Preliminary Risk Scan` depending on input completeness and evidence quality.

The report must read as a coherent thesis failure map. Each major failure path should connect assumption, failure mode, transmission mechanism, evidence, valuation link, thesis damage, and invalidation / monitoring triggers. Main failure paths should be written as risk cards rather than large default tables. Technical evidence quality notes should usually sit in the appendix unless they change the risk verdict.

### 9.7 Market Positioning Agent Role

The currently designed Market Positioning Agent module evaluates what the market appears to believe, how visible expectations have changed, how investors appear positioned, and whether the setup creates expectation, crowding, neglect, or positioning risk.

It is conceptually cross-asset, but the current detailed implementation is equity-first. Non-equity positioning rules should be expanded alongside ETF, Commodity, Crypto, and Fixed Income agents.

It answers:

```text
What does the market appear to believe, how is it positioned, and does that create expectation or positioning risk or opportunity?
```

The Market Positioning Agent owns:

- visible market expectations;
- consensus and estimate revision context;
- analyst rating and target-direction interpretation as visible sell-side expectations;
- ownership and holder-base context;
- short interest and squeeze-risk context;
- ETF / fund / sector / theme flow context where relevant;
- options positioning as supporting evidence, not direct sentiment translation;
- observable narrative and sentiment evidence;
- crowding and neglect classification;
- event-bar and expectations-reset interpretation;
- signal contradiction analysis;
- positioning archetype classification;
- structured handoff to Valuation & Expectations, Risk / Red Team, News & Catalysts, Market Sense / Macro, and Investment Committee.

It does not own final buy / sell / hold recommendations, add / reduce / exit actions, position sizing, final target prices, valuation attractiveness, reverse DCF, final “priced in” valuation conclusions, technical trading signals, full news / catalyst discovery, macro regime analysis, final risk verdict, or final Investment Committee synthesis.

Dedicated Market Positioning design documents:

- `market-positioning-agent-prd.md`
- `market-positioning-method-skill-prd.md`
- `market-positioning-framework.md`

The agent produces `market_positioning.md` or, for narrow direct calls, a focused positioning note. It may classify output as `Complete Market Positioning`, `Limited Market Positioning`, or `Blocked Market Positioning`, and should also provide channel-level status for consensus / revisions, ratings / targets, ownership / holder base, flows, short interest, options, narrative / sentiment, and price reaction / volume.

Market Positioning is normally a context module in full equity workflows, but it becomes a conditional decision-relevant gate when expectations, crowding, positioning, event reaction, or narrative saturation are material to the investment case. Missing positioning work may therefore create timing / market-context limitations, a Limited Final Memo, or a blocked specific conclusion when the positioning question is material.

The Market Positioning Agent must follow channel-specific source hierarchy and freshness rules. It should prefer direct, dated, sourceable, repeatable evidence over interpreted, anecdotal, or narrative evidence. Stale data may support lag-aware conclusions, but not current-position claims.

### 9.8 Market Sense Agent Role

The Market Sense Agent is the cross-asset market interpretation and hypothesis layer.

It answers:

```text
What logic is the market trading right now, and what hypotheses should be tested?
```

The agent converts market movement, news, macro context, positioning, valuation context, cross-asset behavior, and narrative signals into disciplined, evidence-labeled hypotheses. It should normally produce multiple plausible hypotheses rather than a single overconfident explanation.

The Market Sense Agent owns:

- market-behavior hypothesis formation;
- expected-reaction versus actual-reaction interpretation;
- cross-asset narrative and driver interpretation;
- separation of fact, interpretation, hypothesis, evidence, counter-evidence, and confidence;
- hypothesis disconfirmation conditions and next checks;
- handoffs to Market Positioning, News & Catalysts, Macro, Valuation & Expectations, Risk / Red Team, asset-class agents, and Investment Committee.

It does not own final buy / sell / hold decisions, position sizing, target prices, source verification, primary news collection, full positioning analysis, or final Investment Committee synthesis.

Dedicated Market Sense design documents:

- `market-sense-agent-prd.md`
- `market-sense-hypothesis-engine-skill-prd.md`
- `market-pattern-library.md`
- `driver-dominance-analysis-skill-prd.md`
- `asset-driver-maps.md`

Driver Dominance is a skill used by Market Sense to identify dominant market drivers; it is not a standalone final-decision agent. Market Sense may form evidence-labeled hypotheses but must not replace Market Positioning, News & Catalysts, Macro, Evidence Collector, or Investment Committee ownership.

Primary outputs:

```text
market_sense_report.md
market_sense_brief.md
```

Use `market_sense_report.md` for asset / theme-specific market-behavior hypotheses. Use `market_sense_brief.md` for broad market mode. For narrow direct calls, the output may be a focused market-sense note. Any market psychology phrase such as "risk-off," "pain trade," "priced in," "crowded," or "narrative exhaustion" must be tied to observable evidence and alternative explanations.

### 9.9 Market Intelligence Agent Role

The Market Intelligence Agent is the broad market news, event, and data-monitoring layer.

It answers:

```text
What happened across markets that matters for investors?
```

The agent identifies, verifies, filters, and summarizes important market-relevant developments across macroeconomics, central banks, governments, regulators, major companies, commodities, geopolitics, credit, rates, crypto, and global markets.

The Market Intelligence Agent owns:

- broad-market event discovery;
- factual confirmation and source-status labeling;
- market-materiality filtering;
- concise investor takeaways;
- affected-driver tagging;
- escalation to Market Sense, Macro, News & Catalysts, asset-class agents, or Investment Committee when deeper interpretation is required.

It does not perform deep Market Sense interpretation, Driver Dominance analysis, pattern matching, asset-specific catalyst review, valuation, portfolio fit, or final investment recommendations.

Dedicated Market Intelligence design documents:

- `market-intelligence-agent-prd.md`
- `market-intelligence-briefing-skill-prd.md`
- `market-news-source-framework.md`
- `market-materiality-filter.md`

Primary output:

```text
market_intelligence_brief.md
```

## 10. Evidence Architecture

### 10.0 Data Access Strategy

The system should use an open-source hybrid data access strategy with minimal APIs.

The default assumption is that the user will not manually provide source files, documents, datasets, or paid data access. The system should be able to collect required information independently from public, reliable, and accessible sources.

Paid data providers are out of scope for the core target system by default. The system should not assume access to Bloomberg, FactSet, Refinitiv, S&P Capital IQ, paid broker research, or other premium databases unless the user explicitly provides access or the architecture is later extended to include them.

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

APIs should be used selectively, not excessively. The system should avoid requiring dozens of API integrations in the baseline architecture. Public API keys may be added when useful, but the core architecture should work through a combination of public websites, official documents, downloadable files, and a small number of high-value public APIs.

Data extraction may involve reading, downloading, parsing, or summarizing public HTML pages, PDFs, CSV files, Excel files, Word documents, regulatory filings, issuer fact sheets, and official reports.

User-provided documents are allowed as an optional future input, but they are not the default operating model.

The core rule remains:

> No verified source means no factual claim.

If a required data point cannot be found, accessed, parsed, or verified, the agent must not invent it or imply that it was checked.

### 10.0.1 Source Registry

The system includes a dedicated source registry framework:

```text
source-registry-framework.md
```

The source registry is not merely a static list of websites. It is a quality-control framework that defines:

- source admission principles;
- source tiers;
- source categories by domain;
- controlled fallback rules;
- source lifecycle management;
- source access status;
- low-confidence and pointer-only source rules;
- claim-strength boundaries.

The source access rule is registry-first, not registry-only. Agents should first use the source registry and the relevant domain evidence playbook. If required data is not available, stale, inaccessible, or paywalled, the Evidence Collector may use controlled fallback research under the source hierarchy.

Controlled fallback sources must be labeled, tiered, timestamped, and limited to the claim strength they can responsibly support. Useful fallback sources may be recommended as registry candidates, but they do not become approved sources automatically.

The core source-quality rule is:

```text
Weak sources may generate questions, not conclusions.
```

AI-generated summaries, SEO-like pages, automated summaries, and unsourced aggregators are pointer-only. They may help discover leads for verification, but they must not support material factual claims, valuation inputs, risk conclusions, or final Investment Committee decision logic.

Relationship between components:

- `source-registry-framework.md` = how sources are admitted, tiered, restricted, and retired;
- domain evidence playbooks = how approved source categories are applied in each asset class or specialist domain;
- Evidence Collector Agent = coordinates evidence collection, readiness, and source discipline;
- specialist agents = analyze evidence and may request additional collection through structured requests.

### 10.1 Evidence Collector Agent

The Evidence Collector Agent is the system's evidence control tower.

Its detailed design package is:

```text
evidence-collector-agent-prd.md
evidence-collection-method-skill-prd.md
evidence-pack-framework.md
source-registry-framework.md
evidence-request-protocol.md
```

Core question:

```text
What do we know, how reliable is it, what supports each material claim, what is missing, and which downstream agents can responsibly proceed?
```

Responsibilities:

- create and maintain the shared evidence base;
- produce `evidence_pack.md` as a claim-support evidence artifact;
- timestamp sources by source date, accessed date, data period, freshness requirement, freshness status, and as-of note;
- classify source tier, evidence type, claim support, claim strength, and materiality;
- maintain a downstream readiness matrix;
- distinguish analytical evidence sufficiency from decision evidence sufficiency;
- identify missing, stale, proxied, contradicted, inaccessible, paywalled, lower-confidence, or weak evidence;
- preserve public evidence separately from private user context;
- accept structured evidence requests from downstream agents;
- register material specialist-discovered evidence before it supports decision-relevant conclusions;
- perform a pre-Investment Committee evidence lock / freshness check.

The Evidence Collector does not make investment decisions, valuation conclusions, risk verdicts, final thesis conclusions, market-sense interpretations, or portfolio decisions.

### 10.1.1 Evidence Status and Readiness

Evidence status is based on decision materiality, not source count.

The system uses:

```text
Complete Evidence
Limited Evidence
Blocked Evidence
```

The Evidence Collector must also produce downstream readiness statuses:

```text
Ready
Ready with Caveat
Limited
Blocked
Not Required
```

A readiness label must include practical meaning. For example, `Limited` must explain what the downstream agent may do, what it may not claim, and what evidence would be needed for a Complete output.

The Evidence Collector must distinguish:

```text
Analytical Evidence Sufficiency
Decision Evidence Sufficiency
```

A workflow may proceed analytically while remaining Limited or Blocked for final IC action.

### 10.1.2 Evidence Profiles

The Evidence Collector supports workflow-driven evidence profiles:

```text
Verification Profile
Readiness Profile
Standard Evidence Profile
Full Decision Evidence Profile
Discovery Evidence Profile
```

Verification and readiness tasks may be narrow. Full Investment Committee workflows require decision-grade evidence coverage. Theme-first and discovery workflows use Discovery Evidence, which can support opportunity mapping and candidate shortlists, but not final buy / sell actions without later asset-first decision evidence.

### 10.1.3 Evidence Pack

Each workflow run should normally create a shared `evidence_pack.md`.

The evidence pack is not a source dump. It should be organized around material claims, evidence readiness, downstream usability, and limitations.

Standard evidence pack structure is defined in:

```text
evidence-pack-framework.md
```

The default structure includes:

- Evidence Pack Header;
- Evidence Readiness Summary;
- Downstream Readiness Matrix;
- Key Supported Claims;
- Claim Support Map;
- Evidence by Analytical Area;
- Missing / Stale / Proxied Evidence;
- Contradictions and Unresolved Evidence Conflicts;
- Source Quality and Access Notes;
- Downstream Evidence Handoff Blocks;
- Evidence Requests and Refresh Notes;
- Source Register Appendix;
- Data Snapshot Appendix, if applicable.

Default asset-first and general workflows should use:

```text
evidence_pack.md
```

Workflow-specific exceptions are allowed when they improve clarity:

```text
sector_evidence_pack.md
theme_evidence_pack.md
evidence_readiness_note.md
evidence_verification_note.md
private_context_note.md
```

### 10.1.4 Claim Support and Evidence Type

Every material claim in the evidence pack should receive a support status:

```text
Supported
Partially Supported
Proxy-Supported
Contradicted
Unsupported
Unable to Verify
Stale / Needs Refresh
Not Material for Current Workflow
```

Every material evidence item should be classified by evidence type:

```text
Reported Fact
Official Guidance / Management Statement
Market Data
Estimate / Consensus Data
Model Output
Regulatory / Legal Disclosure
News Report
Analyst / Practitioner Interpretation
User-Provided Context
Proxy Evidence
Assumption
```

The system must preserve the boundary between reported facts, management statements, source opinions, estimates, model outputs, assumptions, proxy evidence, and user-provided context.

### 10.1.5 Missing Data, Proxy Data, and Contradictions

Missing data must be classified by materiality:

```text
Critical
Material
Contextual
Optional
Not Material
```

Proxy evidence may be used only when logically relevant, clearly labeled, and bounded. A proxy may support cautious inference or an open risk item, but it must not be presented as direct evidence or used to remove a material limitation.

Material source conflicts must be registered through a contradiction protocol. Official / primary sources govern official facts, but management statements should not automatically override external evidence. Unresolved material contradictions reduce readiness and must remain visible downstream.

### 10.1.6 Evidence Requests and Specialist-Discovered Evidence

Downstream agents may request additional evidence through:

```text
evidence-request-protocol.md
```

Structured requests must identify the target claim, materiality, required evidence, preferred source type, freshness need, decision impact, and whether the evidence is required for a Complete report.

Specialist agents may discover additional evidence, but material specialist-discovered evidence must be registered in the evidence pack before it supports decision-relevant conclusions or final IC synthesis.

Specialist agents may challenge Evidence Collector readiness only through the documented readiness challenge protocol. Silent override is prohibited.

### 10.1.7 Pre-IC Evidence Lock

Before Investment Committee synthesis, the Evidence Collector should perform a pre-IC evidence lock / freshness check.

Allowed lock statuses:

```text
Locked
Locked with Caveats
Refresh Required
Blocked
```

The evidence lock should confirm freshness, registered specialist additions, unresolved gaps, unresolved contradictions, decision evidence sufficiency, and allowed IC output status.

The Evidence Collector does not block the existence of a final memo, but it constrains the allowed output status:

```text
IC Readiness: Complete -> Complete Final Memo allowed
IC Readiness: Limited -> Limited Final Memo only unless limitations are resolved
IC Readiness: Blocked -> Blocked Final Memo / No Decision only
```

Positive IC actions require sufficient valuation / expectations evidence and Risk / Red Team evidence.

### 10.2 Domain Evidence Playbooks / Skills

The system should not rely on one giant Evidence Collector that knows every possible source in detail.

Instead, evidence gathering should be organized through domain-specific evidence playbooks or skills. Detailed domain playbooks should be created or expanded alongside the corresponding asset-class and specialist agents.

Initial domain playbook areas include:

- equity evidence;
- ETF evidence;
- commodity evidence;
- crypto evidence;
- fixed income evidence;
- macro evidence;
- news / catalysts evidence;
- market positioning evidence;
- sector / industry evidence;
- theme / opportunity discovery evidence.

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

### 11.6 Reader Layer and Verification Layer

The system should separate the reader experience from the verification trail.

The main report is the reader layer. It should read like a natural professional investment memo: clear, coherent, structured, and decision-useful. It should not be cluttered with audit mechanics, excessive source lists, internal file references, or agent-process narration.

The appendix, evidence pack, specialist reports, and internal checks are the verification layer. This layer preserves traceability, source discipline, data quality notes, and anti-hallucination controls without making the main report feel like a technical log.

For every material user-facing report, the system should preserve enough verification detail to answer:

- What evidence or specialist work supports the main conclusion?
- Which material factual claims are source-backed?
- Which claims are interpretations or assumptions?
- Which data points are missing, stale, weak, proxied, or uncertain?
- Which conclusions should be limited because the evidence base is incomplete?

This verification layer may appear as a compact appendix, evidence-quality section, evidence pack reference, or structured handoff, depending on the report type. It should be available for review, but it should not dominate the main memo.

### 11.7 Material Claim Support Rule

No material factual claim may appear in a user-facing report unless it is supported by at least one of the following:

- the evidence pack;
- a specialist report;
- user-provided data;
- a cited primary or reputable secondary source;
- an explicitly labeled assumption or interpretation.

If support is weak, unavailable, indirect, stale, or based on a proxy, the report must say so in the verification layer and, when material to the decision, in the main memo.

The Investment Committee Agent must be especially strict: it should not introduce new factual claims that are absent from the evidence pack or specialist reports unless the workflow explicitly permits targeted evidence refresh.

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
- macro market variables such as yields, real yields, DXY, EUR/USD, USD/JPY, oil, gold, volatility, credit spreads, and market-implied policy paths: latest available when the request is current, market-sensitive, event-driven, or investment-decision relevant;
- company financials: latest filing, earnings release, or company report;
- ETF holdings: latest issuer holdings file where available;
- ETF expense ratio and AUM: latest issuer fact sheet or issuer page where available;
- index methodology: latest available methodology, not necessarily daily;
- industry structure: recent enough for the investment thesis;
- narrative and sentiment sources: freshness depends on the topic and market relevance.

## 13. Output and File Structure

### 13.0 Documentation Integration Rule

While the system is still being designed, every newly created or materially updated agent, skill, workflow, reference, or report-template document must be integrated back into the system documentation.

After creating or changing a document, the following checks are required:

1. Update `prd.md` if the change affects system scope, agent list, workflow design, output structure, open questions, or current design decisions.
2. Update `system-architecture-map.md` if the change affects agent responsibilities, skill relationships, workflow sequencing, ownership boundaries, report artifacts, or handoffs.
3. Update any directly related agent PRD, skill PRD, framework, or workflow file if cross-references changed.
4. Remove or revise stale references, old artifact names, outdated ownership assumptions, and contradicted open questions.
5. Verify that the new document is logically connected to the rest of the system rather than existing as an isolated file.
6. Run a light consistency check for naming, file references, markdown structure, and encoding.

This rule is mandatory during the build phase. A document is not considered finished until the relevant system-level documents have been updated.

### 13.0A Active Documentation Registry and Lifecycle

The following top-level Markdown files are active design documents unless explicitly marked as archive / reminder below. `prd.md` is the product-level source of truth and `system-architecture-map.md` is the architecture-level source of truth. Each active document must remain connected to one of those source-of-truth documents or to a directly referenced package document.

System-level documents:

```text
prd.md
system-architecture-map.md
full-agent-system-build-roadmap.md
final-architecture-audit.md
```

Router / intake documents:

```text
master-intake-router-prd.md
asset-intake-router-prd.md
theme-opportunity-intake-router-prd.md
asset-driver-maps.md
```

Asset-class and asset-analysis documents:

```text
equity-agent-prd.md
equity-company-analysis-method-skill-prd.md
equity-company-analysis-framework.md
equity-deep-dive-workflow.md
financial-statement-analysis-skill-prd.md
etf-agent-prd.md
etf-analysis-method-skill-prd.md
etf-analysis-framework.md
commodity-agent-prd.md
commodity-analysis-method-skill-prd.md
commodity-analysis-framework.md
commodity-family-playbooks.md
crypto-agent-prd.md
crypto-analysis-method-skill-prd.md
crypto-analysis-framework.md
crypto-data-source-and-metric-framework.md
fixed-income-agent-prd.md
fixed-income-analysis-method-skill-prd.md
fixed-income-framework.md
fixed-income-instrument-playbooks.md
```

Opportunity, sector, and discovery documents:

```text
sector-industry-analysis-agent-prd.md
sector-industry-analysis-method-skill-prd.md
sector-industry-analysis-framework.md
structural-winners-discovery-agent-prd.md
structural-winner-discovery-method-skill-prd.md
structural-winner-discovery-framework.md
```

Evidence, sources, and data-quality documents:

```text
evidence-collector-agent-prd.md
evidence-collection-method-skill-prd.md
evidence-pack-framework.md
evidence-request-protocol.md
source-registry-framework.md
```

Cross-functional specialist and synthesis documents:

```text
investment-committee-agent-prd.md
investment-committee-synthesis-method-skill-prd.md
investment-committee-memo-framework.md
macro-agent-prd.md
macro-analysis-method-skill-prd.md
macro-sensitivity-framework.md
macro-regime-framework.md
macro-indicator-cadence-source-registry.md
macro-block-playbooks.md
macro-g3-fx-regional-policy-overlay.md
macro-expectations-surprise-framework.md
market-intelligence-agent-prd.md
market-intelligence-briefing-skill-prd.md
market-news-source-framework.md
market-materiality-filter.md
market-sense-agent-prd.md
market-sense-hypothesis-engine-skill-prd.md
market-pattern-library.md
driver-dominance-analysis-skill-prd.md
market-positioning-agent-prd.md
market-positioning-method-skill-prd.md
market-positioning-framework.md
news-catalysts-agent-prd.md
news-catalysts-method-skill-prd.md
news-catalysts-framework.md
portfolio-fit-agent-prd.md
portfolio-fit-method-skill-prd.md
portfolio-fit-framework.md
risk-red-team-agent-prd.md
risk-red-team-method-skill-prd.md
risk-red-team-framework.md
valuation-expectations-agent-prd.md
valuation-expectations-method-skill-prd.md
valuation-expectations-framework.md
```

Archive / non-active support documents:

```text
prd.backup-before-full-target-language-20260625.md
НАПОМИНАНИЕ.md
.scratch_macro_prompts/
```

Archive, reminder, and scratch documents are not implementation sources of truth. If any archived or scratch content becomes active, it must be promoted into the registry above and connected to the relevant architecture section.

### 13.1 Markdown Reports

Each agent should save its output as a Markdown report.

For an asset-first workflow, an example structure may be:

```text
reports/
  NVDA/
    2026-06-23/
      intake.md
      evidence_pack.md
      financial_statement_analysis.md
      sector_context.md
      equity_company_analysis.md
      valuation_expectations.md
      market_positioning.md
      news_catalysts.md
      macro_sensitivity.md
      risk_red_team.md
      portfolio_fit.md
      final_investment_memo.md
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
        structural_winners_memo.md
        candidate_watchlist.md
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

Report structure may vary by workflow, but artifact names must remain stable enough for downstream agents to find the right input. New report names should use lowercase snake_case, describe the analytical role rather than the producing agent, and be added to the relevant workflow or agent PRD before use.

### 13.2 Source Display Rule

Detailed source lists should live in `evidence_pack.md` and specialist reports.

The final Investment Committee memo should not list 50 sources or become a bibliography.

The final memo should include only:

- key evidence-backed findings;
- materially important caveats;
- a short “Key Evidence Notes / Limitations” section if needed.

### 13.2A Evidence & Data Quality Appendix

Material analytical reports should include, or link to, a compact verification layer such as an “Evidence & Data Quality Appendix.”

This appendix should not replace the main report and should not interrupt the reader’s flow. Its purpose is to preserve reliability and auditability.

When relevant, it should include:

- materials reviewed;
- source types used;
- evidence quality by major analytical area;
- stale, missing, proxied, or weak data;
- key assumptions;
- major limitations;
- whether the report status is Complete, Limited, or Blocked.

The appendix should be concise. It should not become a full bibliography when `evidence_pack.md` already contains detailed source records.


### 13.3 Specialist Report Structure

Specialist reports should generally follow an Evidence -> Analysis -> Investment Implications structure.

The exact section names may vary by agent, but the underlying logic should remain consistent:

1. evidence / key data;
2. analysis;
3. investment implications.

Agent-specific adaptations are allowed:

- Macro: Data -> Regime -> Asset Implications;
- Valuation: Metrics -> Implied Expectations -> Scenario Range -> Mispricing Risk;
- Risk: Thesis Failure Map -> Material Failure Paths -> Invalidation Triggers;
- ETF: Vehicle Data -> Underlying Exposure -> ETF Suitability;
- News / Catalysts: Recent Events -> Catalyst Path -> Price Relevance;
- Sector / Industry: Evidence Plan -> Sector Structure -> Profit Pool -> Investment Implications.

This structure is intended to reduce hallucination risk by separating what was found from what it means for the investment case.

## 14. Investment Committee Agent

The Investment Committee Agent is the final synthesis and decision layer of the system.

The detailed design is defined in:

```text
investment-committee-agent-prd.md
investment-committee-synthesis-method-skill-prd.md
investment-committee-memo-framework.md
```

### 14.1 Role

The Investment Committee Agent reads the evidence pack, intake context, lead asset analysis, valuation / expectations work, risk review, and other relevant specialist reports, then produces the final investment committee memo.

It is the system's final professional judgment layer. It should think like a senior investment decision-maker: integrate the evidence, resolve tensions, explain the investment picture, and produce a clear, practical, evidence-backed final view.

It should synthesize existing evidence and reports. It should not conduct new research by default.

### 14.2 Downstream-Only Rule

The Investment Committee Agent is not a direct-call opinion agent.

It should run only after the orchestrator / workflow has confirmed that required inputs are available.

If called without required inputs, it must not improvise a final view. It should return:

```text
No Decision — More Work Required
```

with the required workflow steps.

### 14.3 Required Inputs for Complete Company / Asset-First Memo

A Complete Final Memo normally requires:

1. intake context;
2. evidence pack;
3. lead asset analysis;
4. valuation / expectations analysis;
5. risk / red team review;
6. relevant context modules where material, such as macro, news / catalysts, market positioning, sector context, and portfolio fit.

Positive actions require sufficient valuation / expectations analysis and Risk / Red Team review.

### 14.4 Primary Output

The primary output is:

```text
final_investment_memo.md
```

During future operating workflows, the report should be saved automatically once the workflow has been launched and required inputs are ready. The agent should not ask the user separately whether to save the report during normal system operation.

### 14.5 Final Memo Style

The final memo should be a natural professional investment committee memo, not an internal system transcript.

The reader should be able to understand the investment picture without reading every specialist report.

The memo should not write:

- “The Equity Agent said...”
- “The Valuation Agent concluded...”
- “The Risk Agent output...”

It should write naturally:

- “Valuation is the main constraint.”
- “The risk profile is manageable but asymmetric.”
- “The company quality case is strong, but the entry setup is less compelling.”

### 14.6 Output Depth

The Investment Committee Agent supports three output depths:

1. Brief Final View — 500–900 words, only when explicitly requested and when sufficient evidence exists.
2. Standard IC Memo — 1,500–3,000 words / 5–10 minute read, default for multi-agent workflows.
3. Full Committee Memo — longer memo only when explicitly requested.

### 14.7 Standard Company / Asset-First Memo Structure

Default section order:

```text
1. Investment View
2. Action Box
3. Why This Action, Not the Alternatives
4. What Matters Most
5. Investment Scorecard
6. Situation Overview
7. The Core Debate
8. Core Thesis
9. Key Assumptions
10. Integrated Evidence Synthesis
11. What Is Priced In
12. Where the Market May Be Wrong
13. Bull / Base / Bear Cases
14. Risks and Thesis Breakers
15. Catalysts and Monitoring Plan
16. Next Steps
17. Evidence & Data Quality Appendix
```

The structure is a default spine. It may be adapted for future sector, theme, ETF, commodity, crypto, and fixed income memo profiles.

### 14.8 Action Box Rules

For asset-first memos, the Action Box should usually distinguish:

```text
For a New Position: [action]
For Existing Holders: [action]
```

The Action Box should include:

- practical meaning;
- primary reason;
- Decision Confidence with explanation;
- time horizon;
- light qualitative portfolio role;
- reassessment trigger;
- Evidence Caveat only when material;
- market data / valuation as-of date when time-sensitive.

User-facing action labels should be natural, such as:

- Initiate Position;
- Build Gradually;
- Do Not Initiate Yet;
- Avoid;
- Add to Existing Position;
- Maintain / Hold;
- Reduce Exposure;
- Exit Position;
- No Decision — More Work Required.

### 14.9 Decision Confidence

The final memo should not use bare labels such as “Conviction: Medium.”

It should use Decision Confidence with explanation:

```text
Decision Confidence: High / Moderate / Low / Insufficient Basis
Why: ...
What would raise confidence: ...
What would lower confidence: ...
```

Decision Confidence is not a probability forecast.

### 14.10 No Exact Position Sizing

The Investment Committee Agent must not provide exact position sizing.

Prohibited:

- percentages;
- dollar amounts;
- exact weights;
- pseudo-precise sizing;
- “3–5% position”;
- “full position” or “half position” if used as sizing.

Allowed:

- qualitative portfolio role only;
- core candidate;
- satellite exposure;
- tactical exposure;
- hedge;
- diversifier;
- watchlist candidate;
- avoid-for-portfolio / not suitable for stated portfolio role;
- no clear portfolio role.

### 14.11 Evidence, Freshness, and Anti-Hallucination

The Investment Committee Agent must preserve the reader layer and verification layer distinction.

The main memo should be readable and natural. The appendix, evidence pack, and specialist reports provide verification.

No material factual claim may appear unless supported by the evidence pack, specialist report, user-provided data, cited reliable source, or explicitly labeled assumption / interpretation.

The agent must not launder weak evidence into strong claims.

Market-price and valuation-sensitive conclusions must state relevant as-of dates. If data is stale or incomplete, the memo should be Limited or Blocked depending on materiality.

### 14.12 Memo Status Handling

The agent supports:

- Complete Final Memo;
- Limited Final Memo;
- Blocked Final Memo.

Complete status does not need to be displayed prominently in the Action Box.

Limited memos should include a natural Evidence Caveat only when material.

Blocked memos must clearly start with:

```text
No Decision — More Work Required
Practical Meaning: Do not make an investment decision from the current evidence base.
```

and include required follow-up steps.

### 14.13 Follow-Up Requests

If the memo is Limited or Blocked, the agent should include structured follow-up requests to the relevant evidence or specialist agent.

The request should specify:

- target agent / module;
- reason;
- needed evidence or analysis;
- priority;
- whether the follow-up is required for a Complete Final Memo.
## 15. Monitoring Plan

The core target workflow does not require a separate automated Thesis Tracker or Monitoring Agent by default.

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
sector_context.md
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

These are optional extensions and should remain architecturally possible.

## 18. Closed Design Decisions and Non-Blocking Extensions

The core design no longer has open blocking documentation questions. Previous open questions are closed as follows:

| Prior question | Current decision |
|---|---|
| Remaining asset-class responsibilities | Equity, ETF, Commodity, Crypto, and Fixed Income responsibilities are defined in their dedicated PRDs, skills, frameworks, and playbooks. |
| Remaining cross-functional responsibilities | Evidence Collector, Macro, Market Intelligence, News & Catalysts, Market Sense, Valuation & Expectations, Risk / Red Team, Sector & Industry, Market Positioning, Portfolio Fit, and Investment Committee responsibilities are defined. |
| Exact agent file format | Use concise Markdown PRDs during the design phase. Implementation-specific agent files are deferred until technical architecture work starts and must not contradict these PRDs. |
| Remaining skill structure | Core reusable methods are captured as skill PRDs and supporting framework / playbook references. New skills require registry and architecture-map updates. |
| `AGENTS.md` structure | Deferred to implementation planning; not a product-design blocker. |
| `workflow.md` structure | Use workflow-specific Markdown documents now, with `equity-deep-dive-workflow.md` as the current detailed workflow reference. Additional workflow files may be created only when they add reusable orchestration logic. |
| Global report naming conventions | Markdown reports use lowercase snake_case names tied to analytical role, not agent identity. New report names must be documented before use. |
| Machine-readable summaries | Optional future extension; Markdown remains the canonical user-facing format. |
| Portfolio Fit Agent design | Completed in `portfolio-fit-agent-prd.md`, `portfolio-fit-method-skill-prd.md`, and `portfolio-fit-framework.md`. |
| Multi-asset comparisons | Handled through intake classification plus asset-class agents, Portfolio Fit, Valuation / compensation analysis where relevant, Risk / Red Team, and final Investment Committee synthesis. |
| Workflow diagrams | Optional future documentation aid; text workflows remain authoritative. |
| Roadmap / final audit | `full-agent-system-build-roadmap.md` and `final-architecture-audit.md` are current system-level control documents. |

Non-blocking extensions remain listed in Section 17. They should not be treated as missing core requirements.

## 19. Non-Goals for the Core Target System

The core target system should not attempt to:

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
- Valuation & Expectations Agent and Valuation & Expectations Method for expectations-led public equity valuation;
- Risk / Red Team Agent and Risk / Red Team Method for thesis failure analysis;
- Market Intelligence Agent for broad market event mapping;
- Market Sense Agent and Driver Dominance Analysis for evidence-labeled market-behavior hypotheses;
- Portfolio Fit Agent for portfolio role and suitability constraints;
- `full-agent-system-build-roadmap.md` and `final-architecture-audit.md` as system-level control documents;
- an Investment Committee Agent for final synthesis.

The final user-facing output should read like a thoughtful investment professional explaining the case clearly, not like a raw dump of agent outputs or a technical evidence audit.

## Global Skills Requirement — Analytical Style and Language Policy

All future or updated agents, skills, workflows, report templates, and user-facing summaries should follow two global skills when applicable:

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
