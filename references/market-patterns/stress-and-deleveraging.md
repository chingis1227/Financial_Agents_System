# Market Pattern Library - Stress and Deleveraging

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: Market Sense  
Contributors: Risk Red Team; Fixed Income Agent; Market Intelligence  
Used by: Market Sense Agent; Risk Red Team; Market Intelligence  
Primary reference for: stress and deleveraging market patterns  
Supporting reference for: risk-gate context and market-stress interpretation  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: High  
Last reviewed: 2026-06-28  
Review trigger: Review quarterly or when stress indicators, credit-market structures, or deleveraging channels change.  
Owner review needed: No  
Split/index status: Domain split file  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->

## 10. Stress / Deleveraging Patterns

## Pattern 17: Credit Stress Leak-Through

### Description
Stress begins in credit or funding markets and leaks into equities, commodities, FX, or broader risk assets.

### Typical Setup
Credit spreads widen; lower-quality debt underperforms; funding tightens; equity volatility rises later; levered companies underperform.

### What Usually Drives It
Rising default risk, funding pressure, reduced risk appetite, tighter lending standards, and higher required risk premium.

### Confirming Evidence
HY spreads widen; IG spreads follow; banks/credit-sensitive sectors weaken; VIX rises; levered companies underperform; issuance becomes harder or expensive.

### Disconfirming Evidence
Credit spreads remain tight; equity selloff is valuation-only; funding stable; stress isolated to one issuer/sector.

### Common False Positives
Calling equity volatility credit stress without spread confirmation; ignoring sector-specific causes; treating normal spread widening as systemic.

### Cross-Asset Clues
HY OAS, BBB OAS, bank equities, VIX, dollar funding indicators, levered equities, corporate bond ETFs.

### Investment Meaning
If credit stress is real, equity downside can broaden and valuation support may be unreliable. Financial strength becomes more important.

### What to Check Next
HY/IG spreads, banks/brokers, credit ETF liquidity, issuance conditions, levered underperformance, funding stress indicators.

### Confidence Guidance
Low if equities down only; medium if spreads widen with vol; high if credit, funding, banks, volatility, and levered assets confirm.

### Useful Source Types
FRED credit spreads; Fed/IMF/OFR reports; corporate bond ETFs; VIX; bank sector performance.

## Pattern 18: Forced Deleveraging

### Description
Investors sell because they must reduce leverage, meet margin calls, satisfy redemptions, or cut risk, not necessarily because fundamentals changed.

### Typical Setup
Sharp cross-asset liquidation; correlations rise; liquid assets sold first; volatility spikes; funding or margin pressure appears; price moves exceed news magnitude.

### What Usually Drives It
Margin calls, risk limits, VaR shocks, redemptions, dealer balance-sheet constraints, and liquidity spirals.

### Confirming Evidence
Unrelated assets sell off together; volatility spikes; liquidity deteriorates; bid/ask spreads widen; safe liquid assets sold; credit/funding stress increases.

### Disconfirming Evidence
Selloff concentrated in assets with clear fundamental news; liquidity normal; credit/funding stable; correlations remain low.

### Common False Positives
Labeling ordinary risk-off as forced deleveraging; assuming causality without funding/liquidity evidence; ignoring fundamentals.

### Cross-Asset Clues
VIX, credit spreads, Treasury liquidity, dollar funding, gold/liquid asset selling, high-beta/leveraged assets, correlation spikes.

### Investment Meaning
Forced selling can create overshoot, but catching it requires evidence that forced pressure is exhausting and liquidity is stabilizing.

### What to Check Next
Cross-asset correlation, volatility, credit spreads, funding indicators, liquidity conditions, signs of stabilization after forced selling.

### Confidence Guidance
Low with sharp selloff only; medium with broad liquidation and vol spike; high with funding stress, credit stress, liquidity deterioration, and cross-asset liquidation.

### Useful Source Types
VIX; FRED credit spreads; Fed/OFR/IMF reports; liquidity data; cross-asset market data.

---
