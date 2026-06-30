# Portfolio Fit Framework

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: Portfolio Fit  
Contributors: Investment Committee; Risk Red Team; asset-class agents  
Used by: Portfolio Fit Agent; portfolio-fit skill; IC synthesis  
Primary reference for: portfolio-fit questionnaire and scenario examples  
Supporting reference for: personalization, privacy-preserving fit, and implementation context  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: Medium  
Last reviewed: 2026-06-28  
Review trigger: Review when portfolio-fit skill, sizing rules, privacy rules, or suitability examples change.  
Owner review needed: No  
Split/index status: Indexed in implementation/reference-library-index.md  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->


## 1. Purpose

The Portfolio Fit Framework defines how the Financial Agent System assesses the role of an asset, instrument, or exposure inside a portfolio.

Core question:

> What role could this asset play in the portfolio, and what portfolio risks does it add or reduce?

The framework does not determine whether the asset is intrinsically attractive, cheap, expensive, or worth buying. It evaluates portfolio function, fit, constraints, and risks.

## 2. Methodological Foundation

The framework uses a qualitative portfolio-management approach with quantitative support.

External methodology anchors include:

- portfolio objectives and constraints;
- liquidity needs;
- time horizon;
- tax and regulatory constraints;
- diversification;
- concentration risk;
- implementation practicality;
- risk-driver exposure.

The system does not implement a quantitative optimizer, efficient-frontier engine, or automated suitability model.

Quantitative inputs may support judgment, but the final verdict is not a mechanical score.

Methodology reference sources:

- CFA Institute — Basics of Portfolio Planning and Construction;
- CFA Institute — Asset Allocation with Real-World Constraints;
- CFA Institute — Overview of Asset Allocation;
- FINRA — Concentration Risk;
- FINRA — Asset Allocation and Diversification;
- Investor.gov — Diversification.

## 3. Core Philosophy

Portfolio fit is different from investment attractiveness.

An asset may be:

- attractive but redundant;
- useful as a diversifier but unattractive at current valuation;
- reasonable for an existing position but weak for a new position;
- useful if replacing similar exposure but problematic if added on top;
- suitable for one objective but unsuitable for another;
- a valid portfolio role but still not something the user must own.

A valid portfolio role does not create an obligation to own the asset.

Portfolio role means:

> The asset could perform a function if valuation, risk, implementation, and user constraints also support inclusion.

It does not mean:

> The asset should be bought.

## 4. Scope

The Portfolio Fit Agent owns:

- generic portfolio role;
- user-specific portfolio fit when sufficient context is provided;
- overlap and concentration assessment;
- qualitative exposure bucket analysis;
- diversification and correlation interpretation;
- horizon-fit;
- role-objective match;
- liquidity, drawdown, currency, benchmark, tax-aware, and implementation constraints when material;
- qualitative sizing caveats;
- replacement / funding logic without trade instructions;
- portfolio-fit comparison across multiple candidate assets;
- structured handoff to the Investment Committee Agent.

The scope is intentionally broad because portfolio fit depends on multiple constraints. The ownership boundary is strict: the agent assesses fit only, not final capital action.

## 5. Non-Scope

The Portfolio Fit Agent does not own:

- final buy / sell / hold decisions;
- exact position sizing;
- target portfolio weights;
- portfolio construction from scratch;
- full asset allocation;
- tax advice;
- legal or fiduciary suitability determinations;
- full financial planning;
- full valuation;
- full risk verdict;
- full asset-class analysis;
- final Investment Committee synthesis.

It must not say:

- “buy”;
- “sell”;
- “add now”;
- “exit”;
- “allocate 5%”;
- “target weight 3–7%”;
- “this is suitable for you” as a formal suitability conclusion;
- “safe investment”;
- “guaranteed hedge”;
- “optimal allocation”.

## 6. Routing Boundary: Portfolio Fit vs Portfolio Construction

Portfolio Fit evaluates a specific asset, instrument, exposure, or defined set of candidates against a portfolio role.

Allowed requests:

- “What role could NVDA play in my portfolio?”
- “Is gold a diversifier for this portfolio?”
- “Do I already have too much AI exposure?”
- “Which of these assets better fits as an inflation hedge?”
- “Does this ETF overlap with my existing holdings?”

Out of scope for Portfolio Fit:

- “What should I add to my portfolio?”
- “Build me a portfolio.”
- “What is my ideal allocation?”
- “How should I distribute my capital?”
- “What exact weights should I use?”

Open-ended portfolio construction requests should route to a future Portfolio Construction / advisory workflow or to Investment Committee synthesis if tied to a specific investment decision.

## 7. Core Analytical Layers

Portfolio fit has two separate layers.

### 7.1 Generic Role

Generic Role answers:

> What role can this asset normally play based on its own properties?

Examples:

- satellite growth exposure;
- inflation-sensitive diversifier;
- defensive income exposure;
- speculative alternative exposure;
- liquidity reserve;
- tactical commodity exposure;
- watchlist candidate.

Generic Role can usually be assessed without user portfolio context.

### 7.2 User-Specific Fit

User-Specific Fit answers:

> Given the user’s actual portfolio, horizon, objective, and constraints, does this asset improve the portfolio?

If context is missing, the agent must not pretend to know personalized fit.

Use:

```text
User-Specific Fit: Limited — current holdings, exposure size, risk profile, horizon, and objective were not fully provided.
```

or:

```text
User-Specific Fit: Blocked — personalized portfolio-fit assessment requires at least minimal portfolio context.
```

## 8. Portfolio Context Levels

### 8.1 No Portfolio Context

The agent may provide:

- Generic Role;
- typical use cases;
- typical risks;
- “Do Not Use As” warning where material;
- questions needed for personalization.

It must not provide personalized fit.

### 8.2 Partial Context

Partial context can support qualitative personalized fit if the user provides enough of:

1. current exposure to the asset or similar exposure;
2. major current positions or exposure buckets;
3. investment horizon;
4. risk profile;
5. objective for the asset.

### 8.3 Sufficient Context

Sufficient context does not require a full brokerage statement.

User-Specific Fit may be Complete if the context is sufficient for the specific question, including:

- current exposure to the asset or similar exposure;
- major holdings or exposure buckets;
- horizon;
- risk profile;
- objective;
- liquidity constraints if material;
- benchmark, tax/account, or currency constraints if material.

## 9. Minimal Personalized-Fit Intake

When personalized fit is requested but context is missing, ask up to five short questions:

1. Do you already hold this asset or similar exposure?
2. What are the 3–5 largest positions or exposure buckets in the portfolio?
3. What is the investment horizon for this idea?
4. What is the risk profile: conservative, balanced, aggressive, or speculative?
5. What is the objective: growth, income, hedge, diversification, tactical exposure, inflation protection, liquidity, or watchlist?

The agent may still provide Generic Role first.

## 10. Position Context Taxonomy

The agent must identify capital context where possible:

- New Position;
- Existing Position;
- Add to Existing Position;
- Reduce / Exit Question;
- Watchlist / Monitoring Context;
- Unknown Position Context.

Use the system-standard wording “New Position,” not internal capital-flow jargon.

When relevant, separate:

```text
For a New Position:
For an Existing Position:
For Add to Existing Position:
For Reduce / Exit Question:
```

Opening, holding, adding, and reducing can have different portfolio-fit conclusions.

## 11. Portfolio Objective Hierarchy

If the user provides multiple goals, the agent must identify:

- primary objective;
- secondary objectives;
- conflicting objectives;
- which objective the asset actually serves.

Example:

```text
Bitcoin may serve speculative growth / alternative exposure, but it does not serve liquidity or capital preservation.
```

This prevents the agent from treating one instrument as if it can satisfy incompatible goals.

## 12. Canonical Portfolio Role Categories

### 12.1 Core

A potential long-term base exposure.

Core should be assigned conservatively.

Broad diversified exposures more naturally fit Core than single names, narrow themes, crypto, leveraged products, or complex instruments.

Single-name “Core” requires explicit caveat:

> Business quality and conviction do not remove concentration risk.

Core does not imply exact size, permanent holding, or “must own” status.

### 12.2 Core Candidate

For broad ETFs, diversified funds, cash-like instruments, or diversified bond exposures, prefer “Core Candidate” before “Core.”

A broad ETF is not automatically Core. It still requires checks for:

- benchmark fit;
- geography;
- currency;
- overlap with existing funds;
- factor concentration;
- fees;
- liquidity;
- tracking;
- whether it improves or duplicates the current portfolio.

### 12.3 Satellite

A return-seeking or thematic exposure around the portfolio core.

Common examples:

- single-name growth stock;
- narrow sector exposure;
- thematic ETF;
- crypto exposure;
- high-conviction cyclical exposure.

### 12.4 Tactical

A time-sensitive or regime-dependent exposure.

Examples:

- event-driven exposure;
- rate-cycle trade;
- commodity cycle exposure;
- short-term dislocation exposure;
- market-positioning setup.

### 12.5 Hedge

An exposure intended to protect against a specific risk.

The agent must specify the risk being hedged:

- inflation;
- recession;
- equity drawdown;
- USD weakness;
- interest-rate shock;
- commodity shock;
- credit stress.

An asset must not be called a hedge merely because historical correlation was low.

### 12.6 Diversifier

An exposure that adds a different source of risk or return and may reduce dependence on existing portfolio drivers.

A Diversifier is not necessarily a Hedge.

### 12.7 Watchlist

An asset that may become portfolio-relevant, but current evidence, valuation, risk, timing, or portfolio context does not support a stronger fit conclusion.

### 12.8 Avoid-for-Portfolio

An asset may be interesting in isolation but unsuitable for the stated portfolio objective or current portfolio structure.

Examples:

- worsens concentration;
- mismatches horizon;
- mismatches liquidity needs;
- duplicates existing risk;
- too complex for intended role;
- not appropriate for stated objective.

## 13. Negative Fit Is a Valid Output

Weak Fit, Not Suitable, and Avoid-for-Portfolio are useful outputs, not failures.

The agent should explain what risk is being prevented.

Examples:

- avoiding redundant exposure;
- avoiding hidden concentration;
- avoiding liquidity mismatch;
- avoiding misuse of an instrument;
- avoiding a hedge that does not actually hedge the stated risk.

Sometimes “do not add exposure” is the most valuable portfolio-fit conclusion.

## 14. Diversifier vs Hedge

The agent must strictly distinguish Diversifier and Hedge.

A Diversifier:

- reduces dependence on existing risk drivers;
- may behave differently across regimes;
- does not need to offset a specific loss.

A Hedge:

- protects against a defined risk;
- has a plausible economic mechanism;
- may still fail in some regimes;
- is never guaranteed.

Examples:

- Gold may be a diversifier and sometimes a crisis hedge, but not a guaranteed hedge.
- Bitcoin may be speculative alternative exposure, but not a reliable hedge by default.
- Commodity producer equities are not the same as direct commodity hedges.
- Long-duration bonds may hedge recession risk but can worsen inflation / rate-shock risk.

## 15. Fit Verdict Scale

No numerical score.

### Strong Fit

The asset clearly supports the stated portfolio role and does not introduce disproportionate overlap, concentration, liquidity, drawdown, or implementation problems based on available context.

Strong Fit does not mean “buy.”

### Reasonable Fit

The asset has a logical portfolio role, but there are meaningful limitations or trade-offs.

### Conditional Fit

The asset fits only under specific conditions, such as:

- appropriate horizon;
- limited exposure;
- replacement of overlapping exposure;
- stronger valuation / risk-reward support;
- better evidence;
- different macro regime;
- confirmed liquidity.

### Weak Fit

The asset has a weak role because benefits are outweighed by overlap, concentration, horizon mismatch, liquidity issues, drawdown risk, or objective mismatch.

### Not Suitable

The asset does not fit the stated portfolio objective or user context.

This does not necessarily mean the asset is fundamentally bad.

## 16. Status Layer

Status is separate from verdict.

### Generic Role Status

- Complete;
- Limited;
- Blocked.

### User-Specific Fit Status

- Complete;
- Limited;
- Blocked.

User-Specific Fit is:

- Complete when context is sufficient for the specific question;
- Limited when context is partial, stale, proxy-based, or incomplete;
- Blocked when personalization or sizing is requested without minimum context.

## 17. Fit Confidence

Fit Confidence is separate from Status.

Values:

- High;
- Moderate;
- Low.

Confidence measures the stability of the portfolio-fit judgment under uncertainty.

High confidence does not mean strong fit. The agent may have high confidence that an asset is a weak fit.

## 18. Judgment Matrix

The final verdict should synthesize:

1. role-objective match;
2. overlap and concentration;
3. horizon-fit;
4. drawdown and volatility compatibility;
5. liquidity and implementation constraints;
6. currency, tax, benchmark, or account constraints when material;
7. evidence and context quality;
8. replacement / funding logic;
9. distinction between portfolio benefit and investment attractiveness;
10. monitoring burden.

No mechanical formula such as “4 of 6 checks passed = Reasonable Fit.”

## 19. Canonical Portfolio-Fit Flags

### 19.1 Concentration Warning

The asset increases already meaningful exposure to a single name, sector, factor, geography, currency, theme, asset class, issuer, wrapper, or liquidity source.

### 19.2 Overlap Warning

The asset duplicates existing exposure more than the user may realize.

### 19.3 Role Mismatch

The asset does not match the stated objective.

### 19.4 Horizon Mismatch

The asset’s volatility, drawdown, liquidity, catalyst profile, or valuation sensitivity does not fit the horizon.

### 19.5 Liquidity Constraint

The instrument may be difficult to enter, exit, rebalance, custody, or monitor.

### 19.6 Personalized Fit Blocked

The user requested personalized portfolio fit, but minimum portfolio context is missing.

## 20. Overlap Analysis

Overlap must be assessed through exposure buckets, not only tickers.

Relevant dimensions:

- single-name exposure;
- sector / industry;
- geography;
- currency;
- market-cap style;
- factor exposure;
- theme exposure;
- asset-class exposure;
- duration;
- credit risk;
- commodity beta;
- liquidity profile;
- issuer / sponsor / wrapper exposure;
- custody / counterparty exposure.

Example:

A user may hold different ETFs, but if all are dominated by US mega-cap growth, the portfolio may be less diversified than it appears.

## 21. Concentration Analysis

Use qualitative exposure bands:

- No meaningful exposure;
- Small exposure;
- Moderate exposure;
- Large exposure;
- Concentrated exposure;
- Unknown exposure.

Specify concentration type:

- single-name;
- sector / industry;
- theme;
- factor;
- geography;
- currency;
- asset class;
- liquidity;
- issuer / wrapper / counterparty.

## 22. Correlation Treatment

Correlation is a supporting signal, not the core truth.

If using numerical correlation, state:

- period;
- end date;
- source;
- comparison asset / benchmark / portfolio proxy.

Anti-correlation-overfit rule:

> Historical correlation is descriptive, not a promise. The agent must not overfit portfolio-fit conclusions to past correlations, especially for assets whose behavior changes across inflation, recession, liquidity, or crisis regimes.

The agent must consider:

- regime shifts;
- stress correlation;
- economic rationale;
- liquidity-driven correlation changes;
- common holdings;
- common risk drivers.

An asset must not be called a hedge simply because past correlation was low.

## 23. Horizon-Fit

Horizon-fit is mandatory.

### Short-term / weeks to months

Key constraints:

- liquidity;
- event risk;
- volatility;
- price gaps;
- tactical catalyst dependence.

### 6–12 months

Key constraints:

- catalyst timing;
- valuation setup;
- macro regime;
- positioning risk.

### 1–3 years

Key constraints:

- thesis durability;
- cyclicality;
- drawdown tolerance;
- valuation risk;
- business or asset-class cycle.

### 3–5+ years

Key constraints:

- structural role;
- compounding durability;
- long-run diversification;
- inflation / currency / regime exposure;
- ability to hold through drawdowns.

## 24. Role-Objective Match

The agent must explicitly test whether the asset matches the user’s stated purpose.

Common objectives:

- growth;
- income;
- hedge;
- diversification;
- inflation protection;
- capital preservation;
- tactical exposure;
- liquidity;
- watchlist.

Examples:

- Gold may be a diversifier, but not income.
- A high-growth stock may be a satellite, but not a hedge.
- Long-duration bonds may diversify recession risk but can be poor inflation protection.
- Cash / T-bills support liquidity and optionality, but not long-term growth.

## 25. Drawdown Compatibility

Drawdown compatibility is separate from ordinary volatility.

Relevant stress risks:

- single-name gap risk;
- factor unwind;
- duration shock;
- commodity crash;
- crypto liquidity cascade;
- credit spread widening;
- FX shock;
- ETF liquidity or tracking stress;
- correlation breakdown;
- forced selling dynamics.

The output should explain whether the drawdown profile fits the user’s horizon, risk profile, and objective.

## 26. Liquidity, Implementation, and Monitoring Burden

Liquidity and implementation are fit constraints.

Consider:

- trading liquidity;
- bid/ask spread;
- fund liquidity;
- lock-ups;
- redemption structure;
- ETF tracking and premium / discount behavior;
- futures roll mechanics;
- crypto custody and exchange liquidity;
- bond market liquidity;
- ability to rebalance;
- operational complexity.

Monitoring burden can reduce fit.

The agent should consider whether the asset requires:

- frequent reassessment;
- catalyst monitoring;
- regulatory monitoring;
- roll / tracking monitoring;
- custody / security monitoring;
- macro regime monitoring;
- issuer / credit monitoring.

If the user wants a passive or low-maintenance role, high monitoring burden weakens fit.

## 27. Behavioral and Implementation Suitability

The agent may assess whether an instrument is difficult to hold, understand, or implement.

Relevant issues:

- extreme volatility;
- complex payoff;
- leverage;
- path dependency;
- required monitoring;
- custody friction;
- tax/account complexity;
- risk of misunderstanding exposure;
- risk of abandoning the position during expected drawdowns.

The agent must not psychoanalyze the user.

Use:

```text
This instrument may be difficult to hold through drawdowns and requires active monitoring.
```

## 28. Currency Exposure

Currency exposure should be assessed when material.

Relevant factors:

- user’s base currency or spending currency;
- USD exposure in a non-USD portfolio;
- hedged vs unhedged share class;
- EM currency risk;
- commodity USD pricing;
- foreign bond FX risk;
- crypto USD liquidity dynamics.

The agent should not make a full FX forecast.

## 29. Benchmark Awareness

Use benchmark context only if:

- user provides one;
- portfolio is clearly benchmark-aware;
- question concerns active risk or benchmark-relative exposure.

Do not impose a benchmark by default.

Benchmark relevance may include:

- off-benchmark exposure;
- benchmark-heavy overlap;
- active risk;
- sector or factor deviation;
- diversification away from benchmark concentration.

## 30. Tax-Aware Caveat

The agent may flag tax relevance but must not provide tax advice.

Tax may matter for:

- dividend / income assets;
- bonds;
- commodity funds;
- crypto;
- realized gains on trimming;
- taxable vs retirement accounts;
- ETF structure;
- jurisdiction-specific treatment.

If tax context may materially affect fit, mark it as a limitation or constraint.

## 31. Replacement / Funding Logic

The agent may discuss whether fit depends on what the asset replaces or how it is funded.

Allowed:

```text
The fit improves if this replaces overlapping mega-cap growth exposure rather than being added on top.
```

Allowed:

```text
If funded from cash, portfolio risk rises. If funded from similar exposure, incremental concentration may be lower.
```

Not allowed:

```text
Sell X and buy Y.
```

Replacement logic is not a trade instruction.

## 32. Fit-Relevant Alternatives

The agent may mention alternatives when they clarify portfolio role.

Examples:

- If the objective is income, bonds or dividend strategies may be more direct.
- If the objective is inflation protection, commodity exposure may be more direct than producer equity.
- If the objective is lower volatility, a broad ETF may fit better than a single-name stock.
- If the objective is liquidity, T-bills may fit better than long-duration bonds or crypto.

Do not turn fit-relevant alternatives into a full investment ranking. If the user requests a comparison, restrict the output to portfolio-fit comparison or route to the appropriate comparison / Investment Committee workflow.

## 33. Multi-Asset Portfolio-Fit Comparison

The agent may compare multiple assets by portfolio function.

It must first identify the stated role:

- diversifier;
- hedge;
- income;
- growth satellite;
- inflation protection;
- liquidity reserve;
- tactical exposure;
- reduce concentration.

Comparison should answer:

> Which asset best performs the stated portfolio function?

Suggested format:

| Asset | Role Fit | Main Benefit | Main Portfolio Risk | Better If |
|---|---|---|---|---|

Allowed:

- “best fit for inflation hedge role”;
- “better diversifier under provided context”;
- “weaker fit for liquidity reserve.”

Prohibited unless IC / valuation / risk workflow is invoked:

- “best investment”;
- “most attractive asset”;
- “highest expected return”;
- “buy this one.”

## 34. Do Not Use As

When material, include a short “Do Not Use As” warning.

This is mandatory for complex or easily misunderstood instruments, including:

- leveraged ETFs;
- inverse ETFs;
- covered-call ETFs;
- futures-based commodity products;
- illiquid funds;
- crypto yield products;
- structured products;
- instruments with path dependency or embedded leverage.

Examples:

- volatile single-name equity should not be used as capital preservation;
- commodity producer equity should not be treated as pure commodity hedge;
- long-duration bond should not be treated as cash substitute;
- crypto should not be treated as stable liquidity reserve;
- covered-call ETF should not be treated as free income;
- narrow sector ETF should not be treated as broad diversification;
- inverse or leveraged ETF should not be treated as long-term core exposure.

## 35. Portfolio Benefit vs Investment Attractiveness

The agent must separate:

```text
Portfolio Benefit:
Investment Attractiveness:
```

Portfolio Benefit describes the function the asset may play.

Investment Attractiveness is not determined by the Portfolio Fit Agent unless received from specialist reports.

Use:

```text
The portfolio role exists, but a positive capital action is not supported without valuation, risk, and thesis support.
```

or:

```text
The asset may be fundamentally attractive, but the portfolio benefit is weak if the user already has large overlapping exposure.
```

## 36. Strong Fit Without Investment Case

An asset may receive Strong Fit from a portfolio-role perspective even if investment attractiveness is not proven.

The agent must clarify:

```text
Strong Fit means strong fit for the stated portfolio role. It is not a buy recommendation.
```

Capital action requires Investment Committee synthesis.

## 37. Qualitative Sizing Language

Exact position sizing is prohibited.

Forbidden:

- allocate 5%;
- target weight 3–7%;
- buy a small amount now;
- trim to X%;
- maximum position size should be Y%;
- small = 1–2%;
- medium-sized position without context;
- maximum exposure;
- numerical risk budget;
- trim down materially as hidden trade instruction;
- add gradually without IC action.

Allowed:

- small satellite exposure;
- not core-sized;
- avoid concentration;
- cap as speculative exposure;
- larger role only with stronger evidence and full portfolio context;
- exact sizing requires full portfolio context and is outside this agent’s scope.

## 38. Asset-Class Overlays

The Portfolio Fit Agent is cross-asset. It applies overlays without replacing asset-class specialist agents.

### 38.1 Single-Name Equities

Check:

- single-name concentration;
- sector / industry exposure;
- factor exposure;
- cyclicality;
- valuation sensitivity;
- liquidity;
- gap risk;
- overlap with ETFs and themes;
- role as core candidate, satellite, tactical, or watchlist.

Single-name equities should rarely be treated as hedges.

### 38.2 Equity ETFs / Funds

Check:

- look-through holdings;
- top holdings concentration;
- sector / geography / factor exposure;
- index methodology;
- expense ratio;
- liquidity;
- tracking;
- overlap with existing ETFs and single names;
- issuer / wrapper exposure.

Use look-through where practical. If unavailable, use exposure approximation and mark limitation.

### 38.3 Bonds / Fixed Income

Check:

- duration;
- yield;
- credit quality;
- spread exposure;
- curve exposure;
- inflation sensitivity;
- liquidity;
- currency;
- issuer concentration;
- role as income, diversifier, recession hedge, capital preservation, or tactical rate exposure.

Long-duration bonds should not be treated as cash substitutes.

### 38.4 Commodities

Check:

- physical commodity vs futures vs ETF vs producer equity;
- inflation sensitivity;
- geopolitical exposure;
- seasonality;
- futures curve / roll yield;
- volatility;
- liquidity;
- storage / structure issues;
- role as diversifier, inflation-sensitive exposure, tactical exposure, or hedge against specific shocks.

Commodity producer equities are not pure commodity exposure.

### 38.5 Crypto

Check:

- speculative beta;
- liquidity;
- custody;
- regulation;
- exchange / counterparty risk;
- drawdown profile;
- correlation regime;
- adoption narrative;
- ETF or wrapper structure;
- role as speculative satellite, alternative exposure, or watchlist.

Crypto should not be treated as stable liquidity reserve or reliable hedge by default.

### 38.6 Cash / T-Bills

Check:

- liquidity;
- optionality;
- reinvestment risk;
- inflation erosion;
- yield;
- currency;
- capital preservation;
- role as liquidity reserve, dry powder, or defensive allocation.

Cash-like exposure should not be treated as long-term growth.

### 38.7 Thematic Exposures

Check:

- hidden overlap with existing holdings;
- narrative concentration;
- valuation sensitivity;
- factor crowding;
- sector exposure;
- implementation vehicle;
- liquidity;
- role as satellite, tactical, watchlist, or avoid-for-portfolio.

Themes should not be treated as broad diversification merely because they contain many holdings.

## 39. Evidence and Source Rules

In full workflows, Portfolio Fit should use Evidence Collector outputs.

Inputs may include:

- `evidence_pack.md`;
- asset-class specialist reports;
- Risk / Red Team report;
- Macro report;
- Market Positioning report;
- News & Catalysts report;
- Valuation / Expectations report;
- user-provided private portfolio context.

In direct-call mode, the agent may use available sources itself, but must label input type:

- public market / instrument data;
- specialist-derived input;
- user-provided private context;
- assumptions / proxies.

## 40. Freshness Rules

Separate public data freshness from private portfolio context freshness.

### 40.1 Public Market / Instrument Data

Use as-of dates where available:

- price / market data;
- ETF holdings date;
- fund factsheet date;
- bond yield / duration / spread date;
- crypto market cap / liquidity / flows date;
- correlation / volatility / drawdown period and end date.

### 40.2 Private User Portfolio Context

Mark as:

```text
Portfolio context provided by user, as of [date if known].
```

If the date is unknown or stale:

- User-Specific Fit usually becomes Limited;
- current overlap should not be treated as exact;
- ask user to refresh major exposures for Complete status.

Private portfolio context must not be treated as public market evidence.

## 41. Private Context Handling

Private user portfolio data must be minimized and separated from public evidence.

Avoid unnecessarily repeating:

- full holdings list;
- exact weights;
- brokerage details;
- account-level private information;
- personally identifying financial details.

Prefer summarized exposure language:

```text
large existing US mega-cap growth exposure
```

## 42. Assumptions and Proxies

Proxies are allowed but must be labeled.

Examples:

- sector exposure as proxy for overlap;
- top holdings as proxy for ETF look-through;
- broad asset-class behavior as proxy for correlation;
- “I have a lot of tech” as qualitative concentration signal.

The agent must state:

- what proxy was used;
- why it is relevant;
- what it does not prove;
- whether it downgrades status or confidence.

## 43. Direct-Call Behavior

If called directly without sufficient context:

1. provide Generic Role if possible;
2. mark User-Specific Fit as Limited or Blocked;
3. ask minimal personalized-fit intake questions;
4. avoid exact sizing;
5. avoid final capital action language.

Example:

```text
Generic Role: Satellite growth exposure.
User-Specific Fit: Limited — current holdings, exposure size, risk profile, horizon, and objective were not provided.
To personalize the fit, I need: current exposure, major portfolio buckets, horizon, risk profile, and objective.
```

## 44. Standard `portfolio_fit.md` Structure

```text
## Portfolio Fit

## 1. Portfolio Fit Verdict
- Fit Verdict:
- Generic Role Status:
- User-Specific Fit Status:
- Fit Confidence:
- Primary Portfolio Benefit:
- Primary Portfolio Risk:

## 2. Scope Boundary
This analysis assesses portfolio fit based on the provided context. It does not provide exact position sizing, tax advice, or a final buy/sell decision.

## 3. Context Used
- Asset / instrument:
- Position context:
- User objective:
- Primary objective:
- Secondary objectives:
- Conflicting objectives:
- Horizon:
- Risk profile:
- Known current exposure:
- Portfolio context source and date:
- Public data as-of dates:
- Specialist reports used:

## 4. Generic Role
- Generic role:
- Why this role fits the asset:
- Do Not Use As:

## 5. User-Specific Fit
- User-specific fit:
- For a New Position:
- For an Existing Position:
- For Add to Existing Position:
- For Reduce / Exit Question:
- Key caveat:

## 6. Role-Objective Match
- Stated objective:
- Match / mismatch:
- Explanation:

## 7. Overlap & Concentration
- Existing overlap:
- Exposure bucket overlap:
- Concentration band:
- Concentration source:
- Warning flag if applicable:

## 8. Diversification / Correlation View
- Diversifier vs hedge classification:
- Correlation evidence, if used:
- Regime caveat:

## 9. Liquidity / Drawdown / Implementation Constraints
- Liquidity:
- Drawdown compatibility:
- Implementation complexity:
- Monitoring burden:
- Behavioral / holding-period risk:

## 10. Replacement / Funding Logic
- More coherent if:
- Less coherent if:
- No trade instruction:

## 11. Fit-Relevant Alternatives
- Alternative role considerations, if material:

## 12. What Would Change the Fit
- Trigger 1:
- Trigger 2:
- Trigger 3:

## 13. Evidence & Data Quality
- Public market / instrument data:
- Specialist-derived inputs:
- Private user context:
- Assumptions / proxies:
- Freshness limitations:

## 14. Limitations & Missing Context
- Limitation:
- Missing context:
- Effect on status / confidence:

## 15. Investment Committee Handoff
- Generic Role:
- User-Specific Fit:
- Fit Verdict:
- Generic Role Status:
- User-Specific Fit Status:
- Fit Confidence:
- Position Context:
- Primary Portfolio Benefit:
- Primary Portfolio Risk:
- Overlap / Concentration Warning:
- Horizon-Fit:
- Role-Objective Match:
- Qualitative Sizing Caveat:
- What Would Change the Fit:
- Limitations / Missing Context:
```

## 45. Investment Committee Handoff Rules

The Portfolio Fit Agent has no hard veto power.

However, it may raise escalation flags that the Investment Committee Agent must address before positive capital action:

- Concentration Warning;
- Overlap Warning;
- Role Mismatch;
- Horizon Mismatch;
- Liquidity Constraint;
- Personalized Fit Blocked.

If a positive action is recommended despite a major Portfolio Fit flag, the IC memo must explain why.

## 46. Blocked and Limited States

### 46.1 Generic Role Blocked

Generic Role may be Blocked if:

- instrument cannot be identified;
- exposure is structurally unclear;
- available data is too weak to classify the asset.

### 46.2 User-Specific Fit Blocked

User-Specific Fit is Blocked if:

- user asks for personalized fit;
- minimum portfolio context is absent;
- agent cannot infer current exposure, horizon, objective, or risk profile.

### 46.3 Exact Sizing Blocked

Exact sizing is always outside Portfolio Fit scope.

Use:

```text
Exact sizing is blocked in this agent. Qualitative sizing caveats may be provided, but target weights require a separate portfolio-construction process and sufficient portfolio context.
```

## 47. Illustrative Examples

### 47.1 NVDA + QQQ

NVDA may be a satellite growth exposure. But if the user already holds QQQ, a semiconductor ETF, and other AI-linked holdings, Portfolio Fit should flag overlap and concentration risk.

### 47.2 Gold

Gold may be a diversifier and sometimes crisis-sensitive exposure. It should not be described as a guaranteed hedge or income asset.

### 47.3 Bitcoin

Bitcoin may be speculative alternative exposure. It should not be treated as a stable liquidity reserve or reliable hedge by default.

### 47.4 Long-Duration Bonds

Long-duration bonds may diversify recession risk, but they are not cash substitutes and can perform poorly in inflation or rate-shock regimes.

### 47.5 Broad Equity ETF

A broad ETF may be a Core Candidate, but not automatic Core. Existing benchmark exposure, geography, currency, factor concentration, and overlap still matter.

### 47.6 Covered-Call ETF

A covered-call ETF may provide income-like distributions, but it is not free yield. Upside sacrifice, tax treatment, volatility regime, and strategy mechanics matter.

### 47.7 Commodity Producer Equity

A commodity producer equity is not the same as direct commodity exposure. It adds equity-market, management, cost, jurisdiction, and balance-sheet risks.

## 48. Quality Control Checklist

Before finalizing `portfolio_fit.md`, verify:

- Generic Role and User-Specific Fit are separated.
- Portfolio Benefit and Investment Attractiveness are separated.
- A valid portfolio role is not framed as an obligation to own.
- No exact position size is given.
- No near-sizing language slips in.
- Final buy / sell / add / exit language is avoided.
- Position context is identified.
- Primary and conflicting objectives are addressed.
- Role-objective match is addressed.
- Horizon-fit is addressed.
- Overlap and concentration are addressed.
- Broad ETF is treated as Core Candidate, not automatic Core.
- Core is assigned conservatively.
- Diversifier and hedge are not confused.
- Liquidity, drawdown, implementation, and monitoring burden are addressed when material.
- Complex instruments include “Do Not Use As.”
- Private user context is separated from public evidence.
- Stale private context downgrades User-Specific Fit when relevant.
- Assumptions and proxies are labeled.
- Historical correlation is not overfit.
- Status and Fit Confidence are both included.
- IC handoff is structured.
- Any major escalation flag is explicit.
