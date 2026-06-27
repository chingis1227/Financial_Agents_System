# Portfolio Fit Method Skill PRD

## Purpose

The Portfolio Fit Method Skill defines the operational method for producing `portfolio_fit.md`.

It translates the Portfolio Fit Agent PRD and Portfolio Fit Framework into a gated, step-by-step analytical process.

The method is not a portfolio optimizer, suitability engine, asset-class model, valuation method, or final investment decision process.

Primary references:

```text
portfolio-fit-agent-prd.md
portfolio-fit-framework.md
```

## Core Doctrine

Portfolio fit is a portfolio-function judgment, not an investment recommendation.

The method must preserve four distinctions:

1. Generic Role vs User-Specific Fit.
2. Portfolio Benefit vs Investment Attractiveness.
3. Diversifier vs Hedge.
4. Portfolio-fit implication vs final capital action.

The method must not use numerical scoring, exact position sizing, target weights, or final action labels.

## Depth by Materiality

The method uses a gated sequence with flexible depth.

All mandatory gates must be passed, but the output does not need to be equally long for every request.

For a simple direct-call generic role request, the method may produce a short output if it preserves:

- Position Context;
- Generic Role;
- User-Specific Fit Status;
- Investment Attractiveness line if relevant;
- key reason;
- key caveat;
- prohibited-language guardrails.

For a full workflow or IC input, the method should produce the full `portfolio_fit.md` structure.

Do not force immaterial tax, benchmark, currency, or liquidity sections. Do not omit material constraints.

## Required Analytical Steps

## 1. Scope & Position Context Gate

Before any analysis, establish:

```yaml
asset_or_instrument:
instrument_type:
request_type:
position_context:
user_intent:
stated_objective:
inferred_objective_if_any:
horizon:
risk_profile_if_known:
portfolio_context_available:
```

### Request Type

Classify the request as one or more of:

- generic role;
- personalized fit;
- overlap / concentration check;
- hedge / diversifier question;
- comparison by portfolio function;
- capital-action support;
- watchlist / monitoring context;
- open-ended portfolio construction request.

### Position Context

Position Context must be one of:

- New Position;
- Existing Position;
- Add to Existing Position;
- Reduce / Exit Question;
- Watchlist / Monitoring Context;
- Unknown Position Context.

If unknown, use:

```text
Position Context: Unknown Position Context
```

Do not omit the field.

### Objective Handling

Distinguish stated objective from inferred objective.

If the user states an objective, record it as stated.

If the objective is not stated but can be cautiously inferred from the wording, record it separately:

```yaml
stated_objective: Not provided
inferred_objective_if_any: possible inflation hedge, inferred from user wording
inference_confidence: Low | Moderate
```

Do not treat inferred objective as user-confirmed fact.

### Risk Profile Handling

Do not infer the user’s risk profile from the asset.

Crypto, leveraged products, or volatile equities may indicate asset risk, but they do not prove the user is aggressive or speculative.

If risk profile is unknown, write:

```text
Risk Profile: Not provided
```

### Scope Routing

If the request is open-ended portfolio construction, do not proceed as Portfolio Fit.

Examples requiring routing:

- “Build me a portfolio.”
- “What should I add to my portfolio?”
- “What is my ideal allocation?”
- “Which set of assets should cover all my portfolio roles?”

Route to a future Portfolio Construction / advisory workflow or Investment Committee workflow if tied to a concrete decision.

## 2. Context Sufficiency & Evidence Readiness Gate

Determine whether there is enough context for:

1. Generic Role.
2. User-Specific Fit.

### Generic Role Readiness

Generic Role can proceed if:

- the asset or exposure is identifiable;
- the instrument type is sufficiently clear;
- basic asset properties can be assessed.

If not, Generic Role is Blocked.

### User-Specific Fit Readiness

User-Specific Fit requires enough context for the specific question, usually:

- current exposure to asset or similar exposure;
- major positions or exposure buckets;
- objective;
- horizon;
- risk profile;
- liquidity constraints if material;
- benchmark / currency / tax / account constraints if material.

A full brokerage statement is not required.

However, the method must not personalize beyond the context provided.

### Evidence Classification

Classify available inputs as:

- public market / instrument data;
- specialist-derived inputs;
- user-provided private context;
- assumptions / proxies.

Record as-of dates where available.

Freshness cannot be implied by the report date. Distinguish:

- report date;
- market data as-of date;
- holdings / factsheet date;
- portfolio context as-of date;
- correlation / volatility / drawdown period end date.

If private portfolio context is stale or undated:

- do not make precise current-overlap claims;
- use “based on provided context” language;
- usually downgrade User-Specific Fit to Limited.

### Readiness Status

Assign:

```yaml
generic_role_status: Complete | Limited | Blocked
user_specific_fit_status: Complete | Limited | Blocked
```

If User-Specific Fit is Blocked but Generic Role is possible, continue with Generic Role and clearly mark the user-specific limitation.

## 3. Minimal Intake Branch

If the user asks for personalized fit but context is insufficient, ask up to five questions:

1. Do you already hold this asset or similar exposure?
2. What are the 3–5 largest positions or exposure buckets in the portfolio?
3. What is the investment horizon for this idea?
4. What is the risk profile: conservative, balanced, aggressive, or speculative?
5. What is the objective: growth, income, hedge, diversification, tactical exposure, inflation protection, liquidity, or watchlist?

Do not ask for unnecessary full portfolio data if the specific question can be answered with exposure buckets.

Do not block Generic Role if Generic Role is possible.

## 4. Capital-Action Support Branch

If the user asks whether to add, sell, hold, reduce, exit, or initiate, Portfolio Fit may support the decision only from a portfolio-fit perspective.

The method may answer:

```text
From a portfolio-fit perspective, adding exposure appears weak because it increases existing concentration.
```

It must not answer:

```text
Do not add.
```

or:

```text
Sell / hold / initiate.
```

If a final capital action is requested, state that final action requires Investment Committee synthesis and, where relevant, valuation, risk, thesis, and evidence support.

## 5. Function-First Comparison Branch

If multiple assets are being compared, first identify the stated portfolio function:

- diversifier;
- hedge;
- income;
- growth satellite;
- inflation protection;
- liquidity reserve;
- tactical exposure;
- concentration reduction;
- watchlist role.

If the function is not stated, ask for it or infer cautiously from the user’s wording and mark the inference.

Compare assets only on fit for that function.

Allowed conclusion:

```text
Best fit for the stated portfolio function appears to be [asset], subject to the stated limitations.
```

Not allowed:

```text
Best investment overall is [asset].
```

If the user wants general attractiveness, expected return, valuation, or full ranking, route to comparison / Investment Committee workflow.

## 6. Generic Role Classification

Classify the asset’s generic role using the canonical role categories:

- Core;
- Core Candidate;
- Satellite;
- Tactical;
- Hedge;
- Diversifier;
- Watchlist;
- Avoid-for-Portfolio.

Apply role discipline:

- assign Core conservatively;
- prefer Core Candidate for broad ETFs or diversified exposures before Core;
- do not call an asset a Hedge unless a specific hedged risk and mechanism are identified;
- do not treat a Diversifier as a Hedge;
- do not frame a valid role as a reason the asset must be owned.

If the asset has no clear role, say so.

## 7. Objective and Horizon Fit

Assess whether the asset matches:

- primary objective;
- secondary objectives;
- conflicting objectives;
- horizon.

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

If objectives conflict, identify the conflict.

Example:

```text
The asset may serve speculative growth, but it does not serve liquidity or capital preservation.
```

Horizon-fit must be explicit.

The same asset may be reasonable for a 3–5 year structural role and weak for a 3-month liquidity-sensitive objective.

## 8. Overlap and Concentration Analysis

Assess overlap through exposure buckets, not only tickers.

Check:

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
- issuer / wrapper / counterparty exposure.

Assign qualitative concentration band where possible:

- No meaningful exposure;
- Small exposure;
- Moderate exposure;
- Large exposure;
- Concentrated exposure;
- Unknown exposure.

If overlap or concentration is based on proxy data, label the proxy and downgrade confidence if material.

If private portfolio context is stale or undated, do not write current overlap as fact. Use:

```text
Based on the provided portfolio context, overlap may be high.
```

not:

```text
You currently have high overlap.
```

## 9. Diversification and Correlation Analysis

Assess whether the asset diversifies existing risk drivers.

If numerical correlation is used, state:

- period;
- end date;
- source;
- compared asset / benchmark / proxy.

Apply anti-correlation-overfit discipline:

- historical correlation is descriptive, not a promise;
- do not assume stability across regimes;
- do not call something a hedge merely because past correlation was low;
- consider stress correlations and common risk drivers.

## 10. Risk Constraint Analysis

Assess material constraints:

- liquidity;
- drawdown compatibility;
- volatility;
- implementation complexity;
- monitoring burden;
- behavioral / holding-period risk;
- currency exposure;
- benchmark relevance;
- tax-aware caveat.

Do not force every constraint into the report when immaterial, but do not omit a material constraint.

For complex instruments, include “Do Not Use As.”

Mandatory complex-instrument cases include:

- leveraged ETFs;
- inverse ETFs;
- covered-call ETFs;
- futures-based commodity products;
- illiquid funds;
- crypto yield products;
- structured products;
- path-dependent or embedded-leverage instruments.

## 11. Replacement / Funding Logic

Assess whether the fit depends on what the asset replaces or how it is funded.

Allowed:

```text
Fit improves if the exposure replaces overlapping mega-cap growth exposure rather than being added on top.
```

Not allowed:

```text
Sell X and buy Y.
```

Do not issue trade instructions.

## 12. Portfolio Benefit vs Investment Attractiveness

Explicitly separate:

```text
Portfolio Benefit:
Investment Attractiveness:
```

If there is no specialist support, write:

```text
Investment Attractiveness: Not determined by this agent.
```

or:

```text
Investment Attractiveness: Not determined; requires valuation, risk, and thesis support.
```

If specialist reports are available, summarize only the dependency:

```text
Investment Attractiveness: Based on specialist inputs, [brief dependency], but final decision belongs to the Investment Committee Agent.
```

Portfolio fit cannot repair a weak or unsupported investment thesis.

If fit is strong but thesis / valuation / risk support is weak or unknown, say:

```text
The portfolio role exists, but a positive capital action is not supported without valuation, risk, and thesis support.
```

## 13. Assign Verdict, Statuses, and Confidence

Assign:

```yaml
fit_verdict: Strong Fit | Reasonable Fit | Conditional Fit | Weak Fit | Not Suitable
generic_role_status: Complete | Limited | Blocked
user_specific_fit_status: Complete | Limited | Blocked
fit_confidence: High | Moderate | Low
```

Verdict assignment must be judgment synthesis, not formula.

The method should identify the 1–3 decisive drivers behind the verdict.

Do not use:

- numerical scores;
- “N of M checks passed” logic;
- probability language;
- conviction-as-performance-forecast language.

High confidence can apply to a Weak Fit.

## 14. Build Portfolio-Fit Flags

Raise flags when material:

- Concentration Warning;
- Overlap Warning;
- Role Mismatch;
- Horizon Mismatch;
- Liquidity Constraint;
- Personalized Fit Blocked.

Do not over-flag immaterial issues.

Every major flag must appear in the Investment Committee handoff.

## 15. Build “What Would Change the Fit”

Identify practical triggers that would change the portfolio-fit conclusion, such as:

- user reduces overlapping exposure;
- objective changes;
- horizon changes;
- portfolio liquidity needs change;
- ETF holdings change;
- correlation behavior changes in stress;
- liquidity deteriorates;
- macro regime changes;
- valuation / risk-reward support strengthens or weakens;
- investment thesis support improves or deteriorates.

Avoid generic “if facts change” language.

## 16. Construct `portfolio_fit.md`

Use memo-first structure.

At minimum include:

- Portfolio Fit Verdict;
- Scope Boundary;
- Context Used;
- Generic Role;
- User-Specific Fit;
- Investment Attractiveness line;
- Role-Objective Match;
- Overlap & Concentration;
- Diversification / Correlation View;
- Liquidity / Drawdown / Implementation Constraints;
- Replacement / Funding Logic where material;
- What Would Change the Fit;
- Evidence & Data Quality;
- Limitations & Missing Context;
- Investment Committee Handoff.

The full template is defined in `portfolio-fit-framework.md`.

### Short Mode

For simple direct-call answers, the method may produce a shorter answer instead of a full artifact if it preserves:

- Position Context;
- Generic Role;
- User-Specific Fit Status;
- Investment Attractiveness line if relevant;
- key reason;
- key caveat;
- no prohibited language.

Short mode must not bypass compliance checks.

## 17. Prepare Investment Committee Handoff

Include:

```yaml
generic_role:
user_specific_fit:
fit_verdict:
generic_role_status:
user_specific_fit_status:
fit_confidence:
position_context:
investment_attractiveness:
primary_portfolio_benefit:
primary_portfolio_risk:
overlap_concentration_warning:
horizon_fit:
role_objective_match:
qualitative_sizing_caveat:
what_would_change_the_fit:
limitations_missing_context:
portfolio_fit_flags:
```

If a major flag is present, make it explicit.

The handoff must not contain final action labels.

## 18. Conditional Challenge / Follow-Up Requests

If the output is limited by missing or weak data, create follow-up requests.

Possible requests:

### Evidence Collector

- missing ETF holdings;
- stale factsheet;
- missing liquidity data;
- missing bond duration / yield / credit data;
- missing correlation / volatility / drawdown period;
- unclear instrument structure.

### Risk / Red Team

- concentration risk may be severe;
- liquidity or drawdown profile may be unacceptable;
- hidden instrument risk;
- hedge claim needs challenge.

### Valuation & Expectations

- portfolio role exists but attractiveness is unknown;
- valuation / risk-reward determines whether role is actionable.

### Macro

- currency, rates, inflation, credit, commodity, or liquidity regime materially affects fit.

### Asset-Class Specialist

- ETF wrapper / holdings / tracking issue;
- bond duration / convexity / credit issue;
- crypto custody / liquidity / tokenomics issue;
- commodity vehicle / futures curve / roll-yield issue.

Do not automatically launch upstream agents in direct-call mode without user approval or orchestrator routing.

## 19. Pre-Output Compliance Gate

Before finalizing, verify:

- Position Context is included.
- Generic Role and User-Specific Fit are separated.
- Portfolio Benefit and Investment Attractiveness are separated.
- If no specialist support exists, Investment Attractiveness is “Not determined by this agent.”
- No action box is present.
- No action label is present.
- No final buy / sell / add / reduce / exit language is present.
- No silent escalation to IC conclusion is present.
- No “therefore do not add / hold / exit / buy” language is present.
- No exact sizing is present.
- No near-sizing or target-weight language is present.
- No “must own,” “should own,” “every portfolio needs,” or universal prescription language is present.
- Broad asset classes use role language, not universal prescription.
- Private portfolio context is minimized.
- Private context is not treated as public evidence.
- Stale private context downgrades User-Specific Fit where relevant.
- Stale private context is not used for precise current-overlap claims.
- Assumptions and proxies are labeled.
- Historical correlation is not overfit.
- Diversifier and Hedge are not confused.
- Complex instruments include “Do Not Use As.”
- Statuses and Fit Confidence are included.
- IC handoff is included when producing workflow artifact.
- Major flags appear in IC handoff.

## Style Anti-Generic Rule

The output should sound like a disciplined portfolio manager.

Avoid generic filler such as:

- “it depends on your goals” without specifying which goals;
- “diversification is important” without identifying actual exposure;
- “consider your risk tolerance” without explaining the relevant risk;
- “consult a financial advisor” as a substitute for analysis.

Use concrete portfolio language:

- overlap;
- concentration;
- horizon mismatch;
- liquidity constraint;
- drawdown compatibility;
- role-objective mismatch;
- replacement logic;
- investment-attractiveness dependency.

## Final Standard

A completed Portfolio Fit Method output should make clear:

- what role the asset can play;
- whether that role is generic or user-specific;
- what portfolio benefit it offers;
- what portfolio risk it adds;
- what context is missing;
- what would change the fit;
- what IC must consider before any positive capital action.
