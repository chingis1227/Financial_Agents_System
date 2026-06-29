# Market Pattern Library

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: Market Sense  
Contributors: Market Intelligence; Market Positioning; Macro Agent; News & Catalysts; asset-class agents  
Used by: Market Sense Agent; market-sense-hypothesis-engine skill; Market Intelligence; Market Positioning  
Primary reference for: market-pattern selection index and usage rules  
Supporting reference for: pattern hypothesis generation across asset-class and market-reaction workflows  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: Medium  
Last reviewed: 2026-06-28  
Review trigger: Review when pattern taxonomy, market-sense skill, or split-file coverage changes.  
Owner review needed: Yes - cross-domain pattern ownership should remain visible.  
Split/index status: Index file with domain split references  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->


## 1. Purpose

This library supports the active Market Sense Agent and `market-sense-hypothesis-engine` skill.

It is a practical reference for identifying recurring market interpretation patterns without turning those patterns into unsupported predictions. It helps the agent ask: what pattern might this resemble, what observable evidence supports it, what does not fit, what false positives are possible, and what should be checked next?

This file is a hypothesis aid, not a forecasting engine.

## 2. How to Use This Library

### Core Rules

- A pattern is not proof.
- A pattern is a hypothesis structure.
- Do not force a pattern when evidence is weak.
- Report only relevant pattern matches.
- Always state what matches and what does not match.
- Always identify false-positive risks.
- Separate observable evidence from interpretation.
- If no pattern clearly fits, say so.
- Never use a pattern alone to justify a final investment decision.

### Required Pattern-Match Output

```md
## Pattern Match

### Candidate Pattern
### What Matches
### What Does Not Match
### Analogy Strength
Weak / Moderate / Strong
### False-Positive Risks
### What to Verify
```

### Evidence Status

Use the Market Sense evidence-status system:

- Confirmed
- Plausible
- Weak
- Speculative
- Unsupported

A pattern should rarely be labeled `Confirmed` unless several independent evidence channels support it.

### Confidence

Use Low / Medium / High. Keep confidence low when the price move is small, only one evidence channel supports the pattern, there is no positioning or cross-asset confirmation, or a simpler explanation exists.

## 3. Source Framework

For advisory pattern work, do not rely on phrases such as “the market fears,” “investors are rotating,” or “this is priced in” without observable support.

### Earnings, Guidance, and Expectations Sources

Use for: earnings beat already priced in; guidance matters more than reported results; good news / bad price action; valuation reset despite stable fundamentals.

Preferred sources:

- Company earnings releases, 10-Q, 10-K, and investor relations materials.
- Earnings call transcripts.
- [FactSet Earnings Insight](https://www.factset.com/earningsinsight).
- [FactSet earnings research](https://insight.factset.com/topic/earnings).
- S&P / FactSet / Visible Alpha / Koyfin / other estimate sources where accessible.
- Academic background on post-earnings announcement drift, e.g. [QuantPedia PEAD overview](https://quantpedia.com/strategies/post-earnings-announcement-effect).

Limitations: consensus data may be delayed, incomplete, or paywalled; a headline beat is not enough without guidance, forward estimates, and price reaction.

### Narrative and Behavioral Finance Sources

Use for: narrative exhaustion; narrative acceleration; reflexive momentum; overreaction / underreaction; market story shifts.

Preferred conceptual sources:

- Robert Shiller / Yale materials on narrative economics: [Yale Insights](https://insights.som.yale.edu/insights/narrative-economics-how-stories-go-viral), [Yale Online](https://online.yale.edu/courses/narrative-economics).
- CFA Institute behavioral finance materials, including [Market Efficiency vs. Behavioral Finance](https://rpc.cfainstitute.org/blogs/enterprising-investor/2024/market-efficiency-vs-behavioral-finance-which-strategy-delivers-better-returns).
- CFA Digest summary of investor psychology and under-/overreaction: [CFA Digest PDF](https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/cfa-digest/1999/dig-v29-n2-480-pdf.pdf).
- SEC / Investor.gov behavioral investing material: [Investor Bulletin](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-72).

Verification sources: price reaction, estimate revisions, sector/peer confirmation, valuation expansion or compression, flows, positioning, and news volume.

### Positioning, Crowding, and Flow Sources

Use for: crowded trade unwind; positioning squeeze; forced covering; rotation from leaders to laggards; crowded momentum reversal.

Preferred data sources:

- [CFTC Commitments of Traders](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm).
- [CFTC COT public reporting](https://publicreporting.cftc.gov/stories/s/Commitments-of-Traders/r4w3-av2u/).
- [FINRA Equity Short Interest Data](https://www.finra.org/finra-data/browse-catalog/equity-short-interest/data).
- [FINRA Short Interest Reporting](https://www.finra.org/filing-reporting/regulatory-filing-systems/short-interest).
- [OCC options volume and open interest](https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/daily-volume).
- [Cboe daily options market statistics](https://www.cboe.com/markets/us/options/market-statistics/daily/).

Conceptual sources: [AQR — Momentum Crashes](https://www.aqr.com/Insights/Research/Journal-Article/Momentum-Crashes), [Value and Momentum Everywhere](https://pages.stern.nyu.edu/~lpederse/papers/ValMomEverywhere.pdf).

Limitations: positioning data is often delayed or incomplete; crowding should not be asserted without observable participation, flow, or positioning evidence.

### Macro, Rates, and Liquidity Sources

Use for: Fed repricing shock; liquidity rally despite weak fundamentals; growth scare; inflation scare; risk rally despite bad macro data; safe-haven failing because rates / dollar dominate.

Preferred sources:

- [Federal Reserve Financial Stability Report](https://www.federalreserve.gov/publications/financial-stability-report.htm).
- Federal Reserve research on monetary policy and markets, e.g. [FEDS paper on the Fed and stock market](https://www.federalreserve.gov/econres/feds/files/2026023pap.pdf).
- [Chicago Fed research on monetary policy and stock market reactions](https://www.chicagofed.org/publications/economic-perspectives/2023/5).
- [IMF Global Financial Stability Report](https://www.imf.org/en/publications/gfsr).
- [BIS Working Paper: Funding liquidity risk](https://www.bis.org/publ/work316.pdf).
- [ECB work on market and funding liquidity](https://www.ecb.europa.eu/press/financial-stability-publications/fsr/special/html/ecb.fsrart202305_01~830184261b.en.html).
- FRED credit spreads: [HY OAS](https://fred.stlouisfed.org/series/BAMLH0A0HYM2), [BBB OAS](https://fred.stlouisfed.org/series/BAMLC0A4CBBB).

Useful variables: nominal yields, real yields, yield curve, Fed pricing, DXY, credit spreads, volatility, liquidity proxies, sector leadership.

### Volatility, Stress, and Deleveraging Sources

Use for: forced deleveraging; credit stress leak-through; volatility shock; liquidity spiral; risk-off / flight-to-quality claims.

Preferred sources:

- [Cboe VIX methodology](https://cdn.cboe.com/resources/indices/Volatility_Index_Methodology_Cboe_Volatility_Index.pdf).
- [S&P Dow Jones Indices VIX introduction](https://www.spglobal.com/spdji/en/vix-intro/).
- Brunnermeier and Pedersen, [Market Liquidity and Funding Liquidity](https://www.princeton.edu/~markus/research/papers/liquidity.pdf).
- [Federal Reserve Financial Stability Report](https://www.federalreserve.gov/publications/financial-stability-report.htm).
- [Office of Financial Research reports](https://www.financialresearch.gov/reports/).

Useful variables: VIX, volatility term structure, credit spreads, funding stress indicators, liquidity, bid/ask spreads, correlations, high-beta de-risking.

### Commodity and Geopolitical Sources

Use for: geopolitical headline without supply shock; commodity supply shock repricing; demand slowdown repricing; safe-haven failure; oil / energy / metals regime shifts.

Preferred sources:

- [EIA Short-Term Energy Outlook](https://www.eia.gov/outlooks/steo/).
- [EIA: What drives crude oil prices](https://www.eia.gov/finance/markets/crudeoil/spot_prices.php).
- [IEA Oil Market Report](https://www.iea.org/reports/oil-market-report-june-2026).
- [OPEC Monthly Oil Market Report](https://www.opec.org/monthly-oil-market-report.html).
- [World Bank Commodity Markets](https://www.worldbank.org/en/research/commodity-markets).
- [ECB: Geopolitical risk and oil prices](https://www.ecb.europa.eu/press/economic-bulletin/focus/2024/html/ecb.ebbox202308_02~ed883ebf56.en.html).

Useful variables: spot and futures curve, inventories, supply disruptions, demand revisions, logistics constraints, rates and real yields, ETF flows, futures positioning.

## 4. Pattern Categories

## Detailed Pattern Files

This file is now the index and usage guide. Use the split files below for detailed pattern bodies. These files are supporting references only; no pattern file can justify a final IC Action or evidence lock by itself.

| Pattern area | File | Main patterns |
|---|---|---|
| Event reactions / earnings | `market-patterns/event-reactions-and-earnings.md` | Good News, Bad Price Action; Bad News, Strong Price Action; Earnings Beat Already Priced In; Guidance Matters More Than Reported Results |
| Expectations / narratives | `market-patterns/expectations-and-narratives.md` | Narrative Exhaustion; Narrative Acceleration / Reflexive Momentum; Valuation Reset Despite Stable Fundamentals |
| Positioning / flows | `market-patterns/positioning-and-flows.md` | Crowded Trade Unwind; Positioning Squeeze; Rotation from Leaders to Laggards |
| Macro / rates / liquidity | `market-patterns/macro-rates-liquidity.md` | Fed Repricing Shock; Liquidity Rally Despite Weak Fundamentals; Growth Scare; Inflation Scare |
| Cross-asset / regimes | `market-patterns/cross-asset-regimes.md` | Safe-Haven Fails Because Dollar / Rates Dominate; Risk Rally Despite Bad Macro Data |
| Stress / deleveraging | `market-patterns/stress-and-deleveraging.md` | Credit Stress Leak-Through; Forced Deleveraging |
| Commodities / geopolitics | `market-patterns/commodities-and-geopolitics.md` | Geopolitical Headline Without Supply Shock; Commodity Supply Shock Repricing |
| Examples and source map | `market-patterns/examples-and-source-map.md` | Optional future patterns; example applications; source-map references |

## Crypto Treatment

This library does not create crypto-specific patterns unless existing pattern evidence supports the analogy. Crypto workflows should use relevant cross-asset, positioning, liquidity, stress, or risk-sentiment patterns only as supporting context, with crypto evidence, source, custody, liquidity, regulatory, and tokenomics checks governed by the Crypto Agent, Evidence Layer, and Risk Red Team contracts.

## 14. Pattern Selection Decision Tree

Use this decision tree before selecting specific patterns. The goal is to avoid forcing every situation into the most familiar pattern.

```text
1. Is there a specific event, headline, earnings release, macro print, or policy announcement?
   Yes -> Start with Event Reaction Patterns.
   No  -> Continue.

2. Is the key signal a mismatch between expected and actual price reaction?
   Yes -> Use Expected vs Actual Reaction, then check Event Reaction and Narrative patterns.
   No  -> Continue.

3. Is the move unusually large relative to the news?
   Yes -> Check Positioning / Flow patterns and Stress / Deleveraging patterns.
   No  -> Continue.

4. Are rates, real yields, the dollar, liquidity, or central-bank expectations moving materially?
   Yes -> Check Macro / Rates / Liquidity patterns.
   No  -> Continue.

5. Are several asset classes moving together in a regime-like way?
   Yes -> Check Cross-Asset / Regime patterns.
   No  -> Continue.

6. Are credit spreads, volatility, funding stress, or liquidity conditions deteriorating?
   Yes -> Check Stress / Deleveraging patterns.
   No  -> Continue.

7. Is the situation driven by commodity supply/demand or geopolitical risk?
   Yes -> Check Commodity / Geopolitical patterns.
   No  -> Continue.

8. Is the dominant story widely known, popular, or no longer moving price?
   Yes -> Check Expectations / Narrative patterns.
   No  -> Continue.

9. If no clear pattern fits:
   State: No clear pattern confirmed. Evidence is insufficient.
```

## Final Reminder

A market pattern is a hypothesis aid, not a forecast, recommendation, IC Action, or evidence lock. Use the pattern files to structure questions, then verify with current evidence and the relevant canonical workflow.
