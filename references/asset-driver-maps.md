# Asset Driver Maps

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: Driver Dominance  
Contributors: Market Sense; Equity Agent; ETF Agent; Fixed Income Agent; Commodity Agent; Crypto Agent; Macro Agent  
Used by: driver-dominance-analysis skill; Market Sense Agent; asset-class agents  
Primary reference for: cross-asset driver-map selection and driver checklist design  
Supporting reference for: market interpretation; asset-class setup analysis; driver-dominance handoffs  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: Medium  
Last reviewed: 2026-06-28  
Review trigger: Review when asset-driver taxonomy, driver-dominance skill, or major market-structure assumptions change.  
Owner review needed: Yes - cross-asset ownership should remain visible.  
Split/index status: Indexed in implementation/reference-library-index.md  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->


## 1. Purpose

This reference supports the active `driver-dominance-analysis` skill and Market Sense Agent.

It defines the normal driver map for major asset types. Its purpose is not to decide which driver dominates now. Its purpose is to define which drivers should be checked before making a market interpretation.

The driver dominance analysis skill should use this file to ask:

- Which drivers usually matter for this asset?
- Which drivers are currently active?
- Which drivers point in the same direction?
- Which drivers conflict?
- Which driver or driver cluster appears marginally dominant now?

## 2. Core Rule

A driver map is not a conclusion.

```text
asset-driver-maps.md = what usually matters.
driver-dominance-analysis = what matters most right now.
```

Markets react to marginal changes in expectations, not static facts.

## 3. Standard Driver Map Template

Each asset driver map should follow this structure:

```md
## Asset Driver Map: [Asset Type]

### Core Drivers

### Normal Directional Logic

### Regime Sensitivity

### Cross-Asset Confirmation

### Common Driver Conflicts

### What Usually Matters Most
```

---

## 4. Asset Driver Map: Gold

## Core Drivers

- Real yields
- US dollar
- Fed policy expectations
- Inflation expectations
- Geopolitical risk
- Central bank buying
- ETF flows
- Futures positioning
- Liquidity
- Crisis / safe-haven demand

## Normal Directional Logic

| Driver | Usually Positive When | Usually Negative When |
|---|---|---|
| Real yields | Real yields fall | Real yields rise |
| US dollar | Dollar weakens | Dollar strengthens |
| Fed expectations | Rate cuts / easier policy expected | Higher-for-longer / tighter policy expected |
| Inflation expectations | Inflation fear rises while real yields remain contained | Inflation raises expected tightening / real yields |
| Geopolitics | Risk creates safe-haven demand | Headline risk fades or was priced in |
| Central bank buying | Official demand rises | Official demand slows |
| ETF flows | ETF inflows rise | ETF outflows rise |
| Positioning | Underowned / shorts cover | Crowded longs unwind |
| Liquidity | Liquidity expands | Liquidity tightens / cash demand rises |

## Regime Sensitivity

- Inflation scare: mixed; positive if inflation fear dominates, negative if real yields / Fed tightening dominate.
- Growth scare: often positive if safe-haven demand and lower yields dominate.
- Liquidity rally: often positive if real yields and dollar fall.
- Risk-off: usually positive, unless forced deleveraging or dollar/real-yield strength dominates.
- Fed repricing shock: usually negative if real yields and dollar rise.
- Geopolitical shock: positive only if market sees real escalation or safe-haven flow confirmation.

## Cross-Asset Confirmation

- DXY
- 10-year real yields
- Treasury yields
- Inflation breakevens
- Silver
- Gold miners
- Gold ETF flows
- CFTC gold positioning
- VIX / risk sentiment

## Common Driver Conflicts

- Geopolitics positive vs real yields negative.
- Inflation fear positive vs Fed tightening negative.
- Safe-haven demand positive vs dollar strength negative.
- Central bank demand positive vs ETF outflows negative.
- Long-term monetary distrust positive vs short-term real-rate pressure negative.

## What Usually Matters Most

Not fixed. In the short term, real yields, USD, Fed expectations, and positioning often dominate. In longer regimes, central bank demand, inflation confidence, crisis demand, and monetary trust can matter more.

---

## 5. Asset Driver Map: Oil

## Core Drivers

- Global demand expectations
- Physical supply
- OPEC+ policy
- Inventories
- Spare capacity
- Geopolitical supply risk
- USD
- Refining margins / product demand
- Futures curve
- Positioning
- Global growth cycle

## Normal Directional Logic

| Driver | Usually Positive When | Usually Negative When |
|---|---|---|
| Demand | Demand expectations rise | Growth / demand slowdown |
| Supply | Supply disruptions / cuts | Supply growth / disruptions resolved |
| OPEC+ | Cuts or discipline | Output increases / quota cheating |
| Inventories | Drawdowns | Builds |
| Spare capacity | Limited spare capacity | Ample spare capacity |
| Geopolitics | Real supply or transit disruption | Headline risk without disruption |
| USD | Dollar weakens | Dollar strengthens |
| Refining margins | Product demand strong | Product cracks weaken |
| Futures curve | Backwardation strengthens | Contango / curve weakens |
| Positioning | Underowned / short covering | Crowded longs unwind |

## Regime Sensitivity

- Commodity shock: supply, inventories, spare capacity, and curve dominate.
- Growth scare: demand and inventories dominate.
- Inflation scare: oil can rise as inflation input, unless policy tightening hurts demand.
- Geopolitical shock: durable impact requires physical supply or transit risk.
- Liquidity rally: can support oil if growth expectations also improve.

## Cross-Asset Confirmation

- Brent / WTI spread
- Futures curve
- EIA inventories
- IEA / OPEC supply-demand revisions
- Energy equities
- Refining margins
- USD
- Inflation breakevens
- Shipping / transit indicators where available

## Common Driver Conflicts

- Geopolitical risk positive vs demand slowdown negative.
- OPEC cuts positive vs non-OPEC supply growth negative.
- Inventory draws positive vs weak product demand negative.
- Inflation hedge positive vs Fed tightening / recession risk negative.

## What Usually Matters Most

Physical supply-demand balance, inventory trend, and futures curve usually matter most for durable moves. Headlines matter only when they change the probability of real supply disruption.

---

## 6. Asset Driver Map: Broad Equity Index

## Core Drivers

- Earnings expectations
- Valuation multiples
- Rates / discount rate
- Real yields
- Inflation expectations
- Fed policy expectations
- Liquidity / financial conditions
- Credit spreads
- Market breadth
- Risk appetite
- Sector leadership
- Positioning / flows

## Normal Directional Logic

| Driver | Usually Positive When | Usually Negative When |
|---|---|---|
| Earnings | EPS expectations rise | EPS expectations fall |
| Valuation | Multiples expand | Multiples compress |
| Rates | Yields / real yields fall | Yields / real yields rise |
| Inflation | Disinflation without growth damage | Inflation scare / margin pressure |
| Fed expectations | Easier policy / cuts | Higher-for-longer / tightening |
| Liquidity | Financial conditions ease | Financial conditions tighten |
| Credit | Spreads tighten | Spreads widen |
| Breadth | Participation broadens | Leadership narrows |
| Risk appetite | Volatility falls | Volatility rises |
| Positioning | Underowned / inflows | Crowded / outflows |

## Regime Sensitivity

- Growth scare: earnings and credit dominate.
- Inflation scare: rates, margins, and Fed expectations dominate.
- Liquidity rally: rates, financial conditions, and risk appetite dominate.
- Fed repricing shock: real yields and multiples dominate.
- Earnings season: forward guidance and revision breadth dominate.

## Cross-Asset Confirmation

- Treasury yields
- Real yields
- Credit spreads
- VIX
- Dollar
- Equal-weight vs cap-weight index
- Cyclicals vs defensives
- Small caps vs large caps
- Earnings revision breadth
- Sector leadership

## Common Driver Conflicts

- Weak macro negative for earnings but positive for rate cuts.
- Strong growth positive for earnings but negative if it raises yields.
- Falling yields positive for valuation but negative if driven by recession fear.
- Index strength can hide narrow leadership.

## What Usually Matters Most

Depends on regime. Over short periods, rates, liquidity, and positioning can dominate. Over medium periods, earnings revisions, credit conditions, and breadth become more important.

---

## 7. Asset Driver Map: Individual Growth Equity

## Core Drivers

- Revenue growth expectations
- Earnings revisions
- Gross / operating margin trajectory
- TAM / growth runway
- Valuation multiple
- Rates / discount rate
- Competitive position
- Product cycle
- Management guidance
- Risk appetite
- Positioning / crowding
- Liquidity

## Normal Directional Logic

| Driver | Usually Positive When | Usually Negative When |
|---|---|---|
| Revenue growth | Growth accelerates / beats expectations | Growth slows / misses expectations |
| Earnings revisions | Forward estimates rise | Forward estimates fall |
| Margins | Margins expand | Margins compress |
| TAM / runway | Market opportunity expands | TAM questioned / saturation risk |
| Valuation | Multiple supported by revisions | Multiple compresses |
| Rates | Real yields fall | Real yields rise |
| Competition | Moat strengthens | Competition/disruption rises |
| Guidance | Raised guidance | Lowered or cautious guidance |
| Risk appetite | High-beta demand rises | Risk aversion rises |
| Positioning | Underowned / shorts cover | Crowded longs unwind |

## Regime Sensitivity

- Fed repricing shock: discount rate and valuation multiples dominate.
- Earnings acceleration: revisions can dominate rates.
- Risk-off: high-beta and long-duration pressure usually rises.
- Liquidity rally: multiple expansion can dominate weak current earnings.
- Narrative exhaustion: strong fundamentals may not help if expectations are too high.

## Cross-Asset Confirmation

- Sector peers
- Growth vs value factors
- Nasdaq / relevant index
- Treasury yields / real yields
- Analyst revisions
- Options positioning
- ETF / fund flows
- Customer / supplier read-throughs

## Common Driver Conflicts

- Higher rates negative vs earnings revisions positive.
- Strong revenue growth positive vs valuation already stretched.
- Good earnings positive vs guidance not good enough.
- Strong story positive vs crowded positioning negative.

## What Usually Matters Most

For high-growth equities, forward revisions and guidance often dominate around earnings. Rates and liquidity dominate when macro repricing is sharp. Valuation matters most when expectations stop rising.

---

## 8. Asset Driver Map: AI / Semiconductor Equity

## Core Drivers

- AI capex expectations
- Data center revenue growth
- Hyperscaler spending
- Gross margin
- Supply constraints / capacity
- Earnings revisions
- Product cycle
- Export restrictions
- Competition / custom silicon
- Semiconductor cycle
- Valuation multiple
- Rates / discount rate
- Risk appetite
- Positioning / crowding

## Normal Directional Logic

| Driver | Usually Positive When | Usually Negative When |
|---|---|---|
| AI capex | Hyperscaler capex expectations rise | Capex discipline / slowdown fears rise |
| Data center growth | Revenue accelerates | Growth decelerates |
| Margins | Gross margins expand / hold high | Margin pressure rises |
| Supply | Tight supply supports pricing | Supply catches up / pricing pressure |
| Revisions | EPS/revenue estimates rise | Estimates fall |
| Product cycle | New products strengthen moat | Delays / weak adoption |
| Export controls | Restrictions limited / manageable | Restrictions expand |
| Competition | Moat remains strong | Custom silicon / rivals gain share |
| Cycle | Semis upcycle | Downcycle / inventory correction |
| Valuation | Growth justifies premium | Multiple too high vs revisions |
| Rates | Discount pressure falls | Rates/real yields rise |
| Positioning | Underowned / new buyers | Crowded longs unwind |

## Regime Sensitivity

- AI momentum: earnings revisions, capex expectations, and narrative dominate.
- Fed repricing shock: rates pressure can matter, but may be overridden by revisions.
- Narrative exhaustion: good news may not move price if expectations are too high.
- Export restriction shock: regulatory/geopolitical driver can dominate.
- Semiconductor cycle: inventory and end-market demand matter more in cyclical downturns.

## Cross-Asset Confirmation

- Semiconductor peers
- AI infrastructure stocks
- Hyperscaler capex commentary
- Supplier / memory / equipment names
- Nasdaq
- Treasury yields / real yields
- Forward EPS revisions
- Options positioning
- Valuation multiple trend

## Common Driver Conflicts

- AI earnings momentum positive vs rates negative.
- Capex boom positive vs customer concentration risk negative.
- Supply constraint positive for pricing vs capacity expansion risk.
- Strong narrative positive vs crowded positioning negative.

## What Usually Matters Most

When the AI narrative is active, forward revenue/EPS revisions and hyperscaler capex expectations can dominate. When revisions slow, valuation, positioning, and rates become more important.

---

## 9. Asset Driver Map: Banks / Financials

## Core Drivers

- Net interest margin expectations
- Yield curve shape
- Loan growth
- Deposit costs / deposit beta
- Credit quality
- Charge-offs / provisions
- Capital requirements
- Regulation
- Investment banking / capital markets activity
- Buybacks / capital return
- Funding conditions
- Economic growth
- Rates level and direction

## Normal Directional Logic

| Driver | Usually Positive When | Usually Negative When |
|---|---|---|
| NIM | Asset yields rise faster than deposit costs | Deposit costs rise / asset yields fall |
| Yield curve | Curve steepens constructively | Inversion / recessionary flattening |
| Loan growth | Healthy demand | Weak demand / credit tightening |
| Credit quality | Charge-offs low | Delinquencies / provisions rise |
| Capital | Excess capital / buybacks | Higher capital requirements |
| Regulation | Regulatory burden eases | Regulation tightens |
| Capital markets | IB/trading activity rises | Deal activity weakens |
| Funding | Stable deposits | Deposit flight / funding stress |
| Economy | Growth resilient | Recession risk rises |

## Regime Sensitivity

- Higher rates: positive if NIM expands, negative if credit/funding stress rises.
- Growth scare: credit quality and loan demand dominate.
- Credit stress: funding, capital, and asset quality dominate.
- Yield curve steepening: positive if growth-driven, mixed if inflation/policy shock-driven.

## Cross-Asset Confirmation

- Yield curve
- Credit spreads
- Bank stock index
- Regional bank performance
- Deposit trends
- Loan growth data
- CRE exposure indicators
- Capital markets activity
- VIX / funding stress

## Common Driver Conflicts

- Higher rates positive for NIM vs negative for credit losses.
- Steeper curve positive if growth improves vs negative if inflation risk rises.
- Buybacks positive vs regulatory capital pressure negative.
- Loan growth positive vs underwriting risk negative.

## What Usually Matters Most

In calm regimes, NIM and capital return matter. In stress regimes, funding stability, credit quality, and capital adequacy dominate.

---

## 10. Asset Driver Map: Commodity Producers

## Core Drivers

- Underlying commodity price
- Production volumes
- Cash costs / cost inflation
- Reserve life / resource quality
- Capex intensity
- Balance sheet
- Hedging exposure
- Political / jurisdiction risk
- FX
- Capital allocation
- ESG / permitting / regulation
- Operational execution

## Normal Directional Logic

| Driver | Usually Positive When | Usually Negative When |
|---|---|---|
| Commodity price | Underlying price rises | Underlying price falls |
| Production | Volumes grow / guidance met | Operational misses |
| Costs | Unit costs fall / stable | Cost inflation |
| Reserves | Resource life improves | Depletion / reserve cuts |
| Capex | Growth capex high-return | Capex overruns / poor ROI |
| Balance sheet | Low leverage | High leverage |
| Hedging | Hedges protect downside | Hedges cap upside |
| Jurisdiction | Stable policy | Tax/royalty/nationalization risk |
| FX | Local costs weaken vs revenue currency | Local currency cost inflation |
| Capital allocation | Disciplined returns | Dilutive M&A / poor capex |

## Regime Sensitivity

- Commodity supply shock: commodity beta dominates.
- Demand slowdown: commodity price and volume expectations dominate.
- Inflation scare: producers may benefit from commodity prices but suffer cost inflation.
- Risk-off: equity risk and balance sheet can dominate commodity exposure.

## Cross-Asset Confirmation

- Underlying commodity spot/futures
- Futures curve
- Inventories
- Producer peers
- Cost inflation data
- FX
- Credit spreads
- Company guidance
- Government/regulatory news

## Common Driver Conflicts

- Commodity price positive vs cost inflation negative.
- High spot price positive vs hedges limiting upside.
- Resource growth positive vs capex overruns negative.
- Strong commodity thesis positive vs jurisdiction risk negative.

## What Usually Matters Most

Commodity price drives short-term moves, but costs, balance sheet, hedging, and jurisdiction risk determine equity sensitivity and durability.

---

## 11. Asset Driver Map: Bitcoin

## Core Drivers

- Global liquidity
- Real yields
- US dollar
- ETF flows
- Stablecoin supply
- Leverage / funding rates
- On-chain holder behavior
- Regulation
- Risk appetite
- Narrative cycle
- Halving / supply issuance narrative
- Institutional adoption

## Normal Directional Logic

| Driver | Usually Positive When | Usually Negative When |
|---|---|---|
| Liquidity | Global liquidity expands | Liquidity tightens |
| Real yields | Real yields fall | Real yields rise |
| Dollar | Dollar weakens | Dollar strengthens |
| ETF flows | Inflows accelerate | Outflows / inflows slow |
| Stablecoins | Supply expands | Supply contracts |
| Leverage | Healthy risk appetite | Overleveraged longs liquidate |
| On-chain | Long-term holders accumulate | Distribution rises |
| Regulation | Clarity / institutional access | Restrictive enforcement |
| Risk appetite | High beta demand rises | Risk-off / deleveraging |
| Narrative | Adoption / digital gold story strengthens | Narrative fatigue / skepticism rises |

## Regime Sensitivity

- Liquidity rally: liquidity, dollar, real yields dominate.
- Risk-off: leverage and high-beta risk dominate.
- ETF adoption regime: flows dominate.
- Fed repricing shock: real yields and dollar dominate.
- Narrative acceleration: price, flows, and institutional adoption reinforce.

## Cross-Asset Confirmation

- DXY
- Real yields
- Nasdaq / high beta
- Crypto equities
- Spot Bitcoin ETF flows
- Stablecoin supply
- Funding rates
- Liquidations
- On-chain accumulation/distribution metrics
- Volatility

## Common Driver Conflicts

- ETF inflows positive vs dollar/real-yield pressure negative.
- Digital gold narrative positive vs high-beta risk-off behavior negative.
- Halving narrative positive vs liquidity tightening negative.
- Institutional adoption positive vs regulatory risk negative.

## What Usually Matters Most

In the short term, liquidity, dollar, ETF flows, leverage, and risk appetite often dominate. In longer cycles, adoption, regulation, supply narrative, and global liquidity matter.

---

## 12. Asset Driver Map: Long-Duration Bonds / TLT

## Core Drivers

- Nominal yields
- Real yields
- Inflation expectations
- Fed policy expectations
- Growth expectations
- Term premium
- Treasury supply / fiscal concerns
- Risk-off demand
- Liquidity
- Foreign demand
- Duration positioning

## Normal Directional Logic

| Driver | Usually Positive When | Usually Negative When |
|---|---|---|
| Nominal yields | Yields fall | Yields rise |
| Real yields | Real yields fall | Real yields rise |
| Inflation expectations | Inflation expectations fall | Inflation expectations rise |
| Fed expectations | Rate cuts expected | Higher-for-longer expected |
| Growth | Growth scare / recession risk | Growth acceleration |
| Term premium | Term premium falls | Term premium rises |
| Supply/fiscal | Supply concern fades | Supply/fiscal premium rises |
| Risk-off | Flight to quality | Risk-on / inflation shock |
| Liquidity | Market functioning improves | Liquidity stress / cash selling |
| Positioning | Shorts cover | Crowded longs unwind |

## Regime Sensitivity

- Growth scare: usually positive if inflation contained.
- Inflation scare: usually negative.
- Fed repricing shock: direction depends on cut/hike expectations and real yields.
- Risk-off: positive unless forced deleveraging or inflation shock dominates.
- Fiscal/supply concern: term premium can dominate Fed expectations.

## Cross-Asset Confirmation

- Treasury curve
- Real yields
- Inflation breakevens
- Fed funds futures
- Dollar
- Gold
- Equities / defensives
- Credit spreads
- Treasury auction data / supply concerns
- MOVE index where available

## Common Driver Conflicts

- Growth scare positive vs inflation scare negative.
- Risk-off demand positive vs forced cash liquidation negative.
- Rate-cut expectations positive vs rising term premium negative.
- Disinflation positive vs fiscal supply concern negative.

## What Usually Matters Most

For long-duration bonds, nominal yields, real yields, inflation expectations, Fed expectations, and term premium dominate. Context determines whether falling yields are bullish risk relief or recession stress.

---

## 13. Asset Driver Map: Credit / Corporate Bonds

## Core Drivers

- Treasury yields
- Credit spreads
- Default expectations
- Earnings / cash-flow resilience
- Leverage
- Refinancing conditions
- Liquidity
- Risk appetite
- Sector fundamentals
- Ratings / downgrades
- Maturity wall
- Covenant / capital structure risk

## Normal Directional Logic

| Driver | Usually Positive When | Usually Negative When |
|---|---|---|
| Treasury yields | Yields fall, all else equal | Yields rise, all else equal |
| Spreads | Spreads tighten | Spreads widen |
| Defaults | Default expectations fall | Default risk rises |
| Cash flow | Issuer fundamentals improve | Cash flow weakens |
| Leverage | Leverage declines | Leverage rises |
| Refinancing | Markets open / funding cheap | Refinancing risk rises |
| Liquidity | Market liquidity strong | Liquidity deteriorates |
| Risk appetite | Demand for carry rises | De-risking / outflows |
| Ratings | Upgrades / stable outlook | Downgrades / fallen angel risk |

## Regime Sensitivity

- Growth scare: spreads and default risk dominate.
- Liquidity rally: spread tightening can dominate weak fundamentals temporarily.
- Fed repricing shock: rates duration and spreads can move in opposite directions.
- Credit stress: spreads, liquidity, and refinancing dominate.
- Inflation scare: rates pressure and margin/cash-flow risk matter.

## Cross-Asset Confirmation

- HY OAS
- IG / BBB OAS
- Treasury yields
- Credit ETFs
- Equity of levered issuers
- Bank stocks
- VIX
- New issuance conditions
- Rating actions
- Default rates

## Common Driver Conflicts

- Treasury yields fall positive vs spreads widen negative.
- Carry demand positive vs deteriorating credit fundamentals negative.
- Strong economy positive for defaults vs higher rates negative for refinancing.
- Liquidity support positive vs issuer leverage negative.

## What Usually Matters Most

For credit returns, spread movement and default/refinancing risk often dominate. For high-quality long-duration credit, Treasury yield movement can also be a major driver.

---

## 14. Asset Driver Map: USD / FX-Sensitive Assets

## Core Drivers

- Interest rate differentials
- Real yield differentials
- Growth differentials
- Inflation differentials
- Central bank divergence
- Safe-haven demand
- Current account / external balance
- Commodity exposure
- Risk appetite
- Positioning
- Fiscal / political risk

## Normal Directional Logic

| Driver | Usually Positive for USD When | Usually Negative for USD When |
|---|---|---|
| Rate differentials | US rates rise vs peers | US rates fall vs peers |
| Real yields | US real yields rise | US real yields fall |
| Growth | US growth outperforms | Rest-of-world growth outperforms |
| Central banks | Fed more hawkish | Fed more dovish |
| Safe haven | Global risk-off | Global risk-on / carry demand |
| External balance | US external concern fades | External/fiscal concern rises |
| Commodity exposure | Commodity importers pressured | Commodity exporters benefit |
| Positioning | Underowned / shorts cover | Crowded longs unwind |

## Regime Sensitivity

- Risk-off: USD often strengthens as safe haven.
- Fed repricing shock: rate differentials dominate.
- Global growth rebound: USD may weaken if capital rotates abroad.
- Commodity shock: effects differ by importer/exporter exposure.
- Liquidity stress: USD funding demand can dominate.

## Cross-Asset Confirmation

- DXY
- Rate differentials
- Real yield differentials
- Fed vs ECB/BoJ/BoE expectations
- VIX
- Credit spreads
- Gold
- Commodities
- EM FX
- Cross-currency basis where available

## Common Driver Conflicts

- US growth strength positive for USD vs risk-on global rotation negative.
- Fed cuts negative for USD vs risk-off safe-haven demand positive.
- Commodity shock can strengthen exporter FX but weaken importer FX.
- Fiscal concerns negative vs high real yields positive.

## What Usually Matters Most

In short-term market reactions, rate differentials, real yields, Fed divergence, risk appetite, and positioning often dominate.

---

## 15. Asset Driver Map: Thematic ETFs

## Core Drivers

- Underlying holdings performance
- Theme narrative strength
- Earnings revisions of key holdings
- Valuation of key holdings
- ETF flows
- Concentration in top holdings
- Liquidity / bid-ask spreads
- Sector / factor exposure
- Macro sensitivity
- Regulatory / policy support
- Positioning / crowding
- Index methodology / rebalancing

## Normal Directional Logic

| Driver | Usually Positive When | Usually Negative When |
|---|---|---|
| Holdings | Top holdings outperform | Top holdings underperform |
| Narrative | Theme gains adoption | Narrative fades / becomes crowded |
| Revisions | Key holdings estimates rise | Estimates fall |
| Valuation | Valuation supported by growth | Multiple compression |
| ETF flows | Inflows rise | Outflows rise |
| Concentration | Leaders strong | Concentrated leaders reverse |
| Liquidity | Liquidity adequate | Liquidity weak / spreads widen |
| Macro | Macro supports theme | Macro pressures theme |
| Policy | Subsidies/regulation supportive | Policy/regulatory risk rises |
| Positioning | Underowned | Crowded trade unwind |
| Methodology | Rebalance favorable | Rebalance creates forced selling |

## Regime Sensitivity

- Narrative acceleration: flows and top holdings dominate.
- Narrative exhaustion: valuation, crowding, and flows dominate.
- Fed repricing shock: rate sensitivity of holdings dominates.
- Policy shock: subsidies, regulation, or government spending dominate.
- Risk-off: liquidity and high-beta exposure dominate.

## Cross-Asset Confirmation

- Top holdings
- Related sector ETFs
- ETF flows
- Valuation of top holdings
- Estimate revisions of top holdings
- Options/short interest where available
- Liquidity / bid-ask spreads
- Macro factors relevant to theme
- Policy news

## Common Driver Conflicts

- Strong theme positive vs top holdings overvalued.
- Inflows positive vs concentrated holdings risk.
- Policy support positive vs execution/earnings weakness.
- Long-term theme positive vs short-term rate sensitivity negative.

## What Usually Matters Most

Thematic ETFs are usually driven by top holdings, theme narrative, flows, and valuation. For concentrated ETFs, top holding behavior can dominate the stated theme.

---

## 16. Final Use Rule

Before explaining a price move, the Driver Dominance skill should:

1. Select the closest asset driver map.
2. Identify active drivers.
3. Separate static drivers from marginal changes.
4. Build the Driver Battle Matrix.
5. Identify the dominant driver or driver cluster.
6. Explain which drivers were ignored or overridden.
7. Only then check the Market Pattern Library.

If evidence is insufficient, the correct output is:

```text
Driver dominance cannot be determined with available evidence.
```
