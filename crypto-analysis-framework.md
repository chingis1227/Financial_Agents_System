# Crypto Analysis Framework

## Purpose

This framework defines the standard structure for Crypto Agent outputs.

Primary artifacts:

```text
crypto_analysis.md
crypto_market_regime.md
```

The framework is modular. It should produce a professional investment memo, not a dashboard dump.

## Output 1 — crypto_analysis.md

### 1. Executive View

Include asset, classification, analysis status, specialist verdict, setup quality, main support, main risk, what would improve the setup, and what would break the thesis. Do not use final buy / sell / hold language.

### 2. Asset Identity and Classification

Include asset name and ticker, chain / protocol, native vs wrapped exposure, economic category, primary use case, market cap / FDV where available, liquidity status, and source / as-of note for decision-critical data.

### 3. Investment-Grade Viability Gate

Include identity verification, liquidity quality, source quality, tokenomics availability, value-capture mechanism, team / roadmap / governance visibility, major red flags, and viability status.

Allowed statuses:

```text
Investment-grade
Watchlist
Speculative
Not investment-grade based on available evidence
Insufficient evidence
```

### 4. Core Thesis and Anti-Thesis

Explain why the asset may have durable value, why that thesis may be wrong, whether value depends on adoption / liquidity / scarcity / fees / regulation / narrative, what evidence is strongest, and what evidence is weak.

### 5. Network Economics / Value Accrual

Use the value-accrual ladder:

- user-paid fees;
- protocol revenue / retained economics;
- validator / miner / sequencer economics;
- tokenholder value link;
- burn / staking / fee-share / collateral / gas demand;
- subsidy / emissions dependency;
- economic sustainability;
- main caveat.

Core rule:

```text
Fees != revenue != tokenholder value.
```

### 6. Real Adoption Quality

Include reported activity, possible distortion, organic demand evidence, incentive / subsidy dependency, stickiness, and investment implication.

### 7. Tokenomics / Value Capture

Required for non-BTC assets. Include circulating supply, total / max supply, market cap vs FDV, emissions, unlock schedule, insider / foundation / VC allocation, treasury holdings, token utility, revenue or value-capture link, and dilution / sell-pressure risk.

### 8. Market Structure and Liquidity

Include where material: price and volume, liquidity quality, CEX / DEX split, spot vs futures confirmation, funding, open interest, basis, liquidation risk, options signal where available, and exchange or counterparty concentration.

### 9. Structural Demand / Supply

Include for BTC, ETH, major assets, and supply-sensitive tokens: ETF flows, cumulative ETF demand, ETF AUM, corporate treasury demand, miner / validator / foundation selling, token unlocks, supply issuance, forced-seller risk, and demand durability.

### 10. Macro / Liquidity Transmission

Include current crypto macro sensitivity, main macro variable, real rates / USD / liquidity relevance, Nasdaq / risk-asset correlation, stablecoin liquidity signal, BTC dominance / ETH-BTC where relevant, and what would change the regime.

### 11. Regulatory Impact

Separate:

```text
Regulatory Catalyst
Regulatory Regime Impact
```

Include what changed, affected assets / business models, bullish interpretation, bearish interpretation, unresolved uncertainty, investment relevance, and source quality.

### 12. Security / Custody / Protocol Risk

Include critical dependency, known incidents, control / governance concentration, custody or counterparty exposure, bridge / oracle / smart-contract risk, risk severity, evidence quality, and investment relevance.

### 13. Team / Roadmap / Governance

Include core responsible entities, roadmap execution, governance control points, developer / ecosystem activity, centralization risk, and investment relevance.

### 14. Conditional Modules

Use when material:

- BTC Overlay: ETF flows, corporate treasury demand, issuance / halving / miner selling, real rates / USD / liquidity, BTC dominance, long-term holder behavior, cycle metrics, digital gold vs liquidity beta regime.
- ETH Overlay: fees, burn / issuance, staking, validator economics, L2 leakage / value capture, DeFi / stablecoin / RWA settlement, MEV, ETH/BTC, ETF staking issue, roadmap / governance.
- DeFi / Staking / Lending Economics: source of yield, who pays it, sustainability, tokenholder value link, subsidy dependency, smart-contract / oracle / bridge / slashing risk.
- Stablecoin Liquidity / Settlement: supply trend, exchange liquidity signal, chain / protocol relevance, reserve / depeg / regulatory risk, investment implication.
- Tokenization / RWA Reality Check: actual adoption, chain / venue, economic beneficiary, token value-capture link, evidence quality, main caveat.
- Derivatives / Leverage Setup: funding, open interest, spot vs futures confirmation, liquidation risk, basis / carry, options signal if available, interpretation, what would invalidate the reading.
- On-Chain Evidence: metric, what it suggests, why it matters, known distortions, confirmation needed, investment implication.
- Narrative / Sentiment Heat: dominant narrative, evidence / proxy, what looks crowded, what looks neglected, risk of narrative exhaustion, confirmation needed, investment relevance.
- Historical / Cycle Context: what resembles prior cycles, what is structurally different now, why the analogy may fail, what confirms it, what contradicts it, investment relevance.
- Exposure Vehicle Tradeoff: direct asset, ETF, crypto-linked equity, miner / exchange / treasury proxy, cleanest exposure, lower operational burden, main wrapper risk, main equity-proxy risk, required handoff.

### 15. Valuation / Implied Expectations Context

Include current price appears to require, main valuation anchor, main valuation risk, what would justify current valuation, and what would break it. Do not issue exact price targets by default.

### 16. Scenario Setup

Include bull case, base case, bear case, key driver separating the cases, evidence that would move toward bull, and evidence that would move toward bear.

### 17. Edge Case Appendix

Use this appendix when the report detects a material edge case.

```text
Edge Case Detected:
Why it matters:
Required check:
What the evidence shows:
What remains uncertain:
Effect on specialist verdict:
Required handoff:
```

Verdict impact rules:

- If the edge case weakens evidence quality, reduce Evidence Quality.
- If the edge case weakens investability but does not block analysis, use Watchlist or Speculative.
- If the edge case prevents decision-grade analysis, use Insufficient Evidence or Not Investment-Grade Based on Available Evidence.
- If the edge case belongs to another agent’s ownership, include a required handoff.
- If current data are stale for a setup-sensitive edge case, do not issue a strong setup-quality verdict.

Common edge case language:

```text
Protocol adoption appears stronger than token value capture. The asset may remain relevant as infrastructure, but the investment case for the token is weaker unless usage translates into durable tokenholder economics.
```

```text
ETF inflows are supportive demand, but price impact is being offset or muted by supply, hedging, leverage, macro pressure, or expectations already embedded in price.
```

```text
The current move appears more fragile if futures leverage and funding are rising faster than spot demand and structural flows.
```

```text
Tokenization growth is relevant only if it creates durable economic value for this token, not merely activity or brand association.
```

```text
A recovered peg reduces immediate market stress but does not eliminate reserve, redemption, custody, or regulatory risk unless the cause of the depeg is resolved.
```

```text
This request is outside the Crypto Agent’s investment-research mandate if it asks for a specific staking provider, pool, bridge route, or yield strategy. The agent may analyze yield economics and risk categories, but not recommend an operational strategy.
```

### 18. Crypto Specialist Verdict

Use:

```text
Investment-grade status:
Setup quality:
Evidence quality:
Key risk severity:
Practical meaning:
Main support:
Main weakness:
What would improve:
What would break:
```

Do not use a single numerical crypto score. Use qualitative labels with explanation instead.

### 19. Monitoring / Trigger Map

Include confirmation signals, warning signals, thesis breakers, and reassessment triggers.

### 20. Evidence Quality and Limitations

Include data freshness, source hierarchy, fallback data, dashboard-derived metrics, missing data, paywalled data, proxy-level conclusions, and blocked claims.

### 21. Structured Handoff

Use:

```text
Asset / Market Context:
- Asset:
- Classification:
- Analysis status:
- Evidence quality:
- Time sensitivity:

Specialist Verdict:
- Investment-grade status:
- Setup quality:
- Main support:
- Main weakness:
- Main unresolved question:

Valuation / Expectations:
- Current price appears to require:
- Main valuation anchor:
- Main valuation risk:
- What would justify current valuation:
- What would break it:

Market Structure:
- Liquidity setup:
- ETF / structural demand status:
- Derivatives / leverage risk:
- Stablecoin liquidity signal:
- Macro / liquidity sensitivity:

Crypto-Native Risks:
- Tokenomics / unlock risk:
- Security / custody / protocol risk:
- Regulatory risk:
- Governance / roadmap risk:

Required Downstream Work:
- ETF Agent:
- Macro Agent:
- Market Positioning:
- Market Sense:
- News & Catalysts:
- Equity Agent:
- Risk / Red Team:
- Portfolio Fit:
- Investment Committee:

Monitoring / Triggers:
- Confirmation signals:
- Warning signals:
- Thesis breakers:
```

## Output 2 — crypto_market_regime.md

Core sections:

1. Executive regime view.
2. Crypto market regime label.
3. BTC / ETH / altcoin leadership.
4. ETF and structural demand.
5. Stablecoin liquidity.
6. Derivatives and leverage.
7. Spot vs futures confirmation.
8. Macro / liquidity transmission.
9. Regulation and event risk.
10. On-chain and exchange-flow evidence.
11. Narrative / sentiment heat.
12. Scenario map.
13. Monitoring triggers.
14. Structured handoff.

## Crypto Market Regime Labels

Allowed labels:

- Liquidity Beta Regime;
- ETF / Structural Demand Regime;
- Leverage-Led Rally;
- Deleveraging / Liquidation Stress;
- Regulatory Repricing Regime;
- Network Fundamentals Regime;
- Stablecoin Liquidity Expansion;
- Stablecoin Liquidity Contraction;
- BTC-Dominance Defensive Regime;
- Altcoin Risk-On Regime;
- Idiosyncratic Protocol Event Regime.

Each label must include:

```text
Regime label:
Evidence:
Counter-evidence:
Confidence:
What would change the regime:
```

No numeric regime score is allowed.

## Comparison Framework

Crypto comparisons must be role-based.

```text
Comparison Question:
Which asset is stronger for [role / horizon / thesis]?
```

Compare cleaner exposure, fundamentals, market-structure setup, regulatory risk, value capture, fragility, valuation / expectations risk, and evidence quality. Do not rank assets as universally best overall.

## Monitoring / Trigger Framework

Confirmation signals may include ETF inflows stabilizing or accelerating, fees / revenue improving, staking participation remaining healthy, stablecoin supply expanding, real usage growing, regulatory clarity improving, or spot demand confirming price move.

Warning signals may include price rising on leverage without spot demand, overheated funding, persistent ETF outflows, weak ETH fees, rising token unlock pressure, contracting stablecoin supply, or governance / security issues.

Thesis breakers may include major hack / exploit, regulatory action blocking the core use case, structural value-capture failure, liquidity drying up, reserve / custody trust breaking, corporate treasury forced selling, or roadmap failure changing the core thesis.

Reassessment triggers may include major protocol upgrade, ETF approval or denial, CLARITY-style or stablecoin bill development, large unlock, major liquidation event, sustained ETH/BTC or BTC dominance break, or macro liquidity regime shift.
