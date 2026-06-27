# Canonical Skill Contracts

Status: Canonical skill-contract layer

## Contract rule

Skills are repeatable analytical methods used by agents or workflows. They do not own final routing, evidence readiness, or IC action unless explicitly part of the owning agent. Every skill below follows the standard template from `implementation/03-contract-templates.md`.

## Evidence Collection Method Skill

Status: Canonical  
Used by: Evidence Collector Agent  
Source: `evidence-collection-method-skill-prd.md`

### Purpose

Collect, classify, verify, and structure evidence for downstream analysis.

### Trigger conditions

- Evidence plan is required for any workflow or specialist output.

### Required inputs

- Intake block
- Selected workflow
- Evidence profile
- Subject/instrument/theme
- Existing source notes or user-provided context

### Step sequence

1. Define claim universe and materiality
2. Select source hierarchy and domain overlays
3. Collect and timestamp sources
4. Classify claim/source/freshness/access/support
5. Identify missing data, contradictions, and proxy evidence
6. Produce evidence pack, readiness matrix, and evidence requests
7. Perform pre-IC evidence lock where needed

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not make investment, valuation, risk, or portfolio conclusions.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when evidence is partial/stale/proxy-heavy; Blocked when decision-critical support is unavailable.

### Quality checks

- Material claims have support status and missing data is visible.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Equity Company Analysis Method Skill

Status: Canonical  
Used by: Equity Agent  
Source: `equity-company-analysis-method-skill-prd.md`

### Purpose

Analyze company business quality and thesis durability.

### Trigger conditions

- An equity company-quality report is required or requested.

### Required inputs

- Company/ticker identity
- Evidence pack
- Financial analysis where available
- Sector/news context where material

### Step sequence

1. Define business and revenue model
2. Assess customer value and demand quality
3. Analyze revenue/margin durability
4. Assess competitive position and management quality
5. Read through financial evidence
6. Define thesis dependencies, breakpoints, and monitoring triggers

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not convert business quality into final stock action.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when company/financial evidence is partial; Blocked when identity or core business evidence is missing.

### Quality checks

- Business quality is separated from stock attractiveness.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Financial Statement Analysis Skill

Status: Canonical  
Used by: Equity Agent; Valuation; Risk; IC  
Source: `financial-statement-analysis-skill-prd.md`

### Purpose

Diagnose financial quality and risk from statements.

### Trigger conditions

- Financial quality is material to company analysis, valuation, risk, or IC.

### Required inputs

- Latest statements
- Historical financials
- Segment/share count/capital allocation data where available

### Step sequence

1. Analyze revenue quality
2. Analyze margin structure
3. Analyze cash flow and FCF conversion
4. Analyze balance sheet and liquidity
5. Analyze working capital/accounting quality
6. Analyze dilution and capital allocation
7. Identify red flags and trend breaks

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not invent missing financial line items or replace valuation.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when history is partial; Blocked when core financial data is unavailable.

### Quality checks

- Financial trends and risks are clear for Equity, Valuation, Risk, and IC.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Valuation & Expectations Method Skill

Status: Canonical  
Used by: Valuation & Expectations Agent  
Source: `valuation-expectations-method-skill-prd.md`

### Purpose

Assess whether market price is justified by realistic expectations.

### Trigger conditions

- Price/action or valuation context is decision-relevant.

### Required inputs

- Price/market cap/EV
- Financial history and forecast inputs
- Business-quality assumptions
- Peer/historical/consensus context where available

### Step sequence

1. Check data integrity
2. Select valuation context and methods
3. Reverse-engineer implied expectations
4. Build scenario valuation range
5. Build return bridge
6. Reconcile methods and risks
7. Define monitoring signals

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not present point target as truth or issue final IC action.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when inputs are partial/proxy; Blocked when core price/financial/capital-structure inputs are missing.

### Quality checks

- IC can see what is priced in and what must be true.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Risk / Red Team Method Skill

Status: Canonical  
Used by: Risk / Red Team Agent  
Source: `risk-red-team-method-skill-prd.md`

### Purpose

Challenge the thesis and identify material failure paths.

### Trigger conditions

- A thesis, final action, or risk challenge is requested.

### Required inputs

- Core thesis
- Evidence pack
- Lead analysis
- Valuation context for Complete Review
- Relevant specialists

### Step sequence

1. Check input completeness
2. Extract thesis and assumptions
3. Apply materiality/anti-overbreaking discipline
4. Identify failure paths and bear case
5. Run mandatory risk gates
6. Include counter-evidence and challenge requests
7. Issue risk challenge verdict

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not create generic risk lists or hidden recommendations.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when thesis/evidence exists but valuation/risk detail is incomplete; Blocked when core thesis is undefined.

### Quality checks

- Risks have transmission mechanism and valuation link where required.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Investment Committee Synthesis Method Skill

Status: Canonical  
Used by: Investment Committee Agent  
Source: `investment-committee-synthesis-method-skill-prd.md`

### Purpose

Integrate evidence and specialist reports into final decision-support memo.

### Trigger conditions

- Final decision-support output is requested.

### Required inputs

- Intake context
- Evidence pack and pre-IC lock
- Lead analysis
- Valuation and Risk when decision-relevant
- Material specialist reports

### Step sequence

1. Check required inputs and evidence lock
2. Identify core debate and assumptions
3. Integrate business, valuation, risk, catalyst, macro, positioning, and portfolio context
4. Apply positive-action gate
5. Produce Action Box, Investment View, IC Action, confidence, monitoring, and follow-up requests

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not invent facts, expose internal transcript, or provide exact position sizing.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when useful but constrained; Blocked when required evidence/valuation/risk/lead analysis is missing.

### Quality checks

- Memo is decision-oriented, evidence-constrained, and includes monitoring.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## ETF Analysis Method Skill

Status: Canonical  
Used by: ETF Agent  
Source: `etf-analysis-method-skill-prd.md`

### Purpose

Analyze ETF vehicle quality and exposure.

### Trigger conditions

- ETF/fund analysis or comparison is requested.

### Required inputs

- Ticker/fund identity
- Issuer holdings/fund documents
- Index/methodology
- Cost/AUM/liquidity/distribution data

### Step sequence

1. Verify fund identity
2. Separate fund vs share-class issues
3. Analyze holdings/exposure/concentration
4. Analyze methodology/active process
5. Assess cost/AUM/liquidity/structure
6. Assess yield/overlap/special risks
7. Produce Vehicle Quality Verdict

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not issue final portfolio action, tax/legal advice, or exact execution plan.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when issuer data is stale/partial; Blocked when identity/holdings/methodology cannot be verified.

### Quality checks

- Vehicle quality and exposure purity are clear.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Fixed Income Analysis Method Skill

Status: Canonical  
Used by: Fixed Income Agent  
Source: `fixed-income-analysis-method-skill-prd.md`

### Purpose

Analyze compensation and risk for fixed-income instruments.

### Trigger conditions

- Fixed-income instrument or exposure review is requested.

### Required inputs

- Instrument identity/terms
- Yield/spread/duration data
- Issuer/obligor credit evidence
- Liquidity/structure evidence

### Step sequence

1. Verify instrument and terms
2. Analyze yield/spread/carry
3. Analyze duration/curve/convexity
4. Assess credit and liquidity
5. Assess call/prepayment/extension/covenants
6. Build downside scenario
7. Issue compensation verdict

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not provide final allocation or exact execution plan.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when market/credit data is partial; Blocked when terms or pricing/credit evidence are missing.

### Quality checks

- Compensation for duration/credit/liquidity/structure risk is clear.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Commodity Analysis Method Skill

Status: Canonical  
Used by: Commodity Agent  
Source: `commodity-analysis-method-skill-prd.md`

### Purpose

Analyze commodity setup through balance, curve, macro, policy, logistics, and instrument context.

### Trigger conditions

- Commodity setup, regime, or instrument analysis is requested.

### Required inputs

- Commodity/instrument identity
- Demand/supply/inventory evidence
- Curve/market data
- Macro/policy/logistics context

### Step sequence

1. Classify commodity family and mode
2. Build demand map
3. Build supply map
4. Analyze inventories/reserves/flows
5. Analyze cost curve and curve/roll/carry
6. Analyze macro/geopolitics/logistics/substitution
7. Assess instrument context
8. Produce verdict, actionability label, triggers

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not issue precise price target or final buy/sell/hold.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when physical data is delayed/proxy-heavy; Blocked when identity or decision-critical balance data is unavailable.

### Quality checks

- Setup, balance, risks, and handoffs are clear.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Crypto Analysis Method Skill

Status: Canonical  
Used by: Crypto Agent  
Source: `crypto-analysis-method-skill-prd.md`

### Purpose

Analyze crypto asset viability, value accrual, adoption, tokenomics, liquidity, regulation, and security.

### Trigger conditions

- Crypto asset/regime analysis is requested.

### Required inputs

- Verified asset identity
- Network/tokenomics/adoption/liquidity data
- Regulatory/security/governance evidence
- Market data/flows where relevant

### Step sequence

1. Verify identity and category
2. Apply investment-grade viability gate
3. Analyze network economics/adoption/tokenomics
4. Analyze liquidity/structure/demand/supply
5. Analyze macro/liquidity/regulation/security/governance
6. Run edge-case checks
7. Produce verdict and monitoring triggers

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not give custody, yield-farming, leverage, legal/tax, or final buy/sell instructions.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when data is partial/fast-moving; Blocked when identity/tokenomics/security/liquidity evidence is unverifiable.

### Quality checks

- Viability, thesis, anti-thesis, risks, and triggers are clear.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Macro Analysis Method Skill

Status: Canonical  
Used by: Macro Agent  
Source: `macro-analysis-method-skill-prd.md`

### Purpose

Analyze macro sensitivity, regime context, surprises, and transmission into assets.

### Trigger conditions

- Macro sensitivity or macro regime context is material/requested.

### Required inputs

- Asset/theme context
- Relevant macro variables
- Fresh market data when current/action-sensitive

### Step sequence

1. Define macro channels
2. Separate sensitivity from generic macro essay
3. Check growth/inflation/rates/liquidity/credit/FX/commodity channels
4. Check freshness
5. Assess thesis relevance
6. Produce handoff

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not provide generic macro commentary unrelated to thesis.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when data is stale/partial; Blocked when decision-critical current data is unavailable.

### Quality checks

- Macro drivers and thesis relevance are explicit.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## News & Catalysts Method Skill

Status: Canonical  
Used by: News & Catalysts Agent  
Source: `news-catalysts-method-skill-prd.md`

### Purpose

Analyze recent events, catalyst path, event status, freshness, and investment relevance.

### Trigger conditions

- Recent events/catalysts are material or requested.

### Required inputs

- Subject and scope
- News/event sources
- Evidence freshness requirements

### Step sequence

1. Collect recent and carryover events
2. Classify event status
3. Assess source/date confidence
4. Map catalyst timing and thesis relevance
5. Run negative news check
6. Produce handoff

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not treat rumor as confirmed or issue final action from news alone.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when reporting is partial/low-confidence; Blocked when requested event cannot be verified.

### Quality checks

- Event status, freshness, and thesis relevance are clear.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Market Positioning Method Skill

Status: Canonical  
Used by: Market Positioning Agent  
Source: `market-positioning-method-skill-prd.md`

### Purpose

Analyze expectations, crowding, narrative saturation, event bar, and positioning risk.

### Trigger conditions

- Positioning/expectations/crowding is material or requested.

### Required inputs

- Asset/theme context
- Price action and market data
- Flow/positioning/sentiment/estimate evidence where available

### Step sequence

1. Assess market belief
2. Assess priced-in expectations
3. Assess crowding/neglect
4. Assess event bar/revision momentum
5. Identify positioning risk/opportunity
6. Produce handoff

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not claim positioning alone determines fundamental value.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when evidence is indirect/incomplete; Blocked when no usable positioning evidence exists.

### Quality checks

- Expectation bar and decision relevance are explicit.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Portfolio Fit Method Skill

Status: Canonical  
Used by: Portfolio Fit Agent  
Source: `portfolio-fit-method-skill-prd.md`

### Purpose

Assess generic role fit and user-specific portfolio fit.

### Trigger conditions

- Portfolio role/suitability is requested or material.

### Required inputs

- Asset/thesis
- User portfolio context where available
- Risk/valuation/asset reports where available

### Step sequence

1. Assess generic role
2. Assess user-specific fit if context exists
3. Check overlap/concentration/risk/liquidity/FX/tax caveats
4. Assess monitoring burden
5. Produce IC handoff

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not give exact allocation or final buy/sell action.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when user portfolio context is missing; Blocked when user-specific answer is required but context is unavailable.

### Quality checks

- Generic and user-specific fit are separated.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Sector & Industry Analysis Method Skill

Status: Canonical  
Used by: Sector & Industry Analysis Agent  
Source: `sector-industry-analysis-method-skill-prd.md`

### Purpose

Analyze sector structure, economics, profit pools, drivers, investability, risks, and monitoring.

### Trigger conditions

- Sector/industry/theme-as-sector analysis is requested or embedded in equity workflow.

### Required inputs

- Sector/theme definition
- Evidence pack
- Relevant companies/subsectors
- User horizon/universe constraints

### Step sequence

1. Classify scope
2. Build evidence plan
3. Analyze structure/TAM/growth quality
4. Map value chain/profit pools/subsectors
5. Assess competition/drivers/valuation/investability
6. Build anti-thesis and monitoring
7. Produce sector outputs

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not make individual security final action.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when boundaries/data are partial; Blocked when scope/evidence is too weak.

### Quality checks

- Sector attractiveness, risks, and monitoring plan are clear.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Structural Winner Discovery Method Skill

Status: Canonical  
Used by: Structural Winners Discovery Agent  
Source: `structural-winner-discovery-method-skill-prd.md`

### Purpose

Discover and rank structural winner candidates within a theme.

### Trigger conditions

- Theme-driven candidate discovery is requested.

### Required inputs

- Theme/industry definition
- Discovery evidence
- Universe constraints
- Sector context where available

### Step sequence

1. Interpret theme
2. Map value chain
3. Identify candidate archetypes
4. Apply positive/negative criteria and disqualifiers
5. Assess evidence/customer/demand/moat/management
6. Rank candidates
7. Produce watchlist and handoff

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not make candidates investment-actionable.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when universe/evidence is partial; Blocked when theme cannot define a universe.

### Quality checks

- Candidates are ranked with rationale, caveats, and next-step handoff.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Driver Dominance Analysis Skill

Status: Canonical  
Used by: Market Sense Agent  
Source: `driver-dominance-analysis-skill-prd.md`

### Purpose

Explain which driver or driver cluster dominated a market move.

### Trigger conditions

- User asks why an asset moved or which driver mattered most.

### Required inputs

- Asset and price move
- Current market context
- Relevant asset-driver map
- Fresh market/evidence data where needed

### Step sequence

1. Define price move
2. Select driver map
3. Detect context and surprise
4. Check what was priced in
5. Build driver battle matrix
6. Identify dominant/supporting/opposing/ignored drivers
7. Provide confirmation, alternative explanation, confidence, implication

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not overstate causality from weak evidence.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when hypotheses are plausible but not confirmed; Blocked when price move/context is unavailable.

### Quality checks

- Dominant driver explanation is bounded and evidence-aware.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Market Sense Hypothesis Engine Skill

Status: Canonical  
Used by: Market Sense Agent  
Source: `market-sense-hypothesis-engine-skill-prd.md`

### Purpose

Generate plausible hypotheses for market moves or narrative shifts without overclaiming.

### Trigger conditions

- Market observation needs explanation but evidence is incomplete or multi-causal.

### Required inputs

- Market observation or price move
- Evidence freshness notes
- Pattern/reference context where relevant

### Step sequence

1. Define observation
2. Generate candidate hypotheses
3. Map evidence for/against each hypothesis
4. Assign confidence
5. Identify confirm/disconfirm signals
6. Produce implications and handoff

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not turn hypotheses into facts or recommendations.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when hypotheses are plausible but evidence is weak; Blocked when observation cannot be defined.

### Quality checks

- Hypotheses include evidence status and disconfirming tests.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.

## Market Intelligence Briefing Skill

Status: Canonical  
Used by: Market Intelligence Agent  
Source: `market-intelligence-briefing-skill-prd.md`

### Purpose

Produce market briefings that separate facts, relevance, and routing implications.

### Trigger conditions

- User asks for market briefing/update or workflow needs situational awareness.

### Required inputs

- Market news/data sources
- User scope, region, asset universe, or theme focus

### Step sequence

1. Collect material items
2. Separate facts from interpretation
3. Assess source/date confidence
4. Identify affected assets/themes
5. Route items to relevant agents
6. Produce briefing

### Output contract

- Must state scope, evidence status, output status, key limitations, and structured handoff.
- Must produce the artifact or report section defined in `implementation/07-investment-committee-and-report-schemas.md`.

### Guardrails

- Do not replace IC or issue final investment decision.
- Must follow statuses, confidence, evidence display, and writing rules in `implementation/00-master-rules.md`.

### Limited / Blocked rules

- Limited when source coverage is partial; Blocked when no reliable current sources are available.

### Quality checks

- Briefing is material, sourced, routed, and not decision-overclaiming.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
