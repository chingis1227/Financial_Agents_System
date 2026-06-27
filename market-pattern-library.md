# Market Pattern Library

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

The Market Sense Agent should not rely on phrases such as “the market fears,” “investors are rotating,” or “this is priced in” without observable support.

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

1. Event Reaction Patterns
2. Expectations / Narrative Patterns
3. Positioning / Flow Patterns
4. Macro / Rates / Liquidity Patterns
5. Cross-Asset / Regime Patterns
6. Stress / Deleveraging Patterns
7. Commodity / Geopolitical Patterns

---

## 5. Event Reaction Patterns

## Pattern 1: Good News, Bad Price Action

### Description
A positive headline, earnings result, macro release, or policy development fails to lift the asset, or the asset falls after apparently good news.

### Typical Setup
Strong run-up before the event; bullish consensus; stretched valuation; upside positioning; headline positive but details or guidance less impressive.

### What Usually Drives It
Good news was already expected, the bar was higher than the headline, investors sell the news, or another factor matters more.

### Confirming Evidence
Pre-event rally; negative reaction on high volume; muted forward estimate revisions; peers fail to confirm; options implied move was high; guidance disappoints relative to expectations.

### Disconfirming Evidence
Broad market selloff explains the move; details were actually negative; liquidity shock affected all assets; price reverses quickly.

### Common False Positives
Calling normal post-event volatility “priced in”; ignoring broader market weakness; missing negative details in guidance or margins.

### Cross-Asset Clues
Sector peers, relevant ETFs, options implied move vs realized move, rates if rate-sensitive, credit if balance-sheet risk matters.

### Investment Meaning
The issue may be expectations, positioning, or valuation rather than fundamentals. It can weaken timing even if the long-term thesis remains intact.

### What to Check Next
Pre-event price run, consensus expectations, guidance, forward revisions, peer reaction, options pricing, volume, broader market move.

### Confidence Guidance
Low if only one noisy session; medium if run-up plus weak reaction; high if price, revisions, positioning, and peers confirm.

### Useful Source Types
Price reaction; company release; filings; transcript; FactSet; options data; peer moves.

## Pattern 2: Bad News, Strong Price Action

### Description
A negative headline, earnings miss, macro shock, or regulatory event fails to push the asset lower, or the asset rises despite bad news.

### Typical Setup
Asset already sold off; consensus bearish; short interest or put demand elevated; event is less bad than feared; guidance stabilizes.

### What Usually Drives It
Bad news was already priced in, uncertainty falls, shorts cover, expectations were too low, or forward details are better than headline results.

### Confirming Evidence
Underperformance before event; elevated short interest or bearish options; price rises after negative headline; estimates do not fall materially; peers stabilize.

### Disconfirming Evidence
Broad market rally explains move; price rise is temporary; delayed fundamental impact not yet reflected; liquidity/index flow distorted move.

### Common False Positives
Confusing short-covering bounce with thesis improvement; treating “less bad” as “good”; ignoring deteriorating fundamentals.

### Cross-Asset Clues
Peer reaction, credit spreads, options skew, sector ETF flows, short interest.

### Investment Meaning
The known risk may already be discounted, but the move can still be a temporary positioning bounce.

### What to Check Next
Was the bad news already known? Did guidance change? Did estimates fall? Was short covering likely? Did credit or peers confirm?

### Confidence Guidance
Low for one-day bounce; medium with bearish positioning; high if estimates stabilize and asset holds gains.

### Useful Source Types
Price data; FINRA short interest; options data; company releases; transcripts; credit spreads.

## Pattern 3: Earnings Beat Already Priced In

### Description
A company beats consensus, but the stock does not rise or sells off because investors already expected the beat or needed a stronger forward revision.

### Typical Setup
History of beats; rally into earnings; upward revisions before report; large implied move; valuation embeds strong execution.

### What Usually Drives It
The beat was not a true surprise; guidance was not raised enough; margins, bookings, backlog, or cash flow disappointed; the market wanted acceleration.

### Confirming Evidence
Strong pre-earnings performance; positive estimate revisions before earnings; unchanged guidance; muted forward revisions; management tone less confident than headline numbers.

### Disconfirming Evidence
Broad risk-off explains decline; beat included one-offs; report had genuine negative surprise; later revisions turn materially positive.

### Common False Positives
Assuming consensus equals buy-side expectations; ignoring revenue quality, margins, or guidance; treating any post-earnings decline as “priced in.”

### Cross-Asset Clues
Peer earnings reactions, sector ETF reaction, options implied move, analyst revisions, valuation multiple change.

### Investment Meaning
The company may still be strong, but future upside may require continued upward revisions rather than ordinary beats.

### What to Check Next
Pre-earnings rally, revision path, guidance vs expectations, forward EPS/revenue revisions, margin and cash-flow quality, peer reactions.

### Confidence Guidance
Low without estimate data; medium with run-up and muted guidance; high if revisions are flat/down after a pre-priced beat.

### Useful Source Types
Company release; transcript; FactSet; options data; peer reports.

## Pattern 4: Guidance Matters More Than Reported Results

### Description
The market reacts more to forward guidance, management tone, or forward indicators than to the reported quarter.

### Typical Setup
Reported results are backward-looking; business is entering a cycle transition; demand, bookings, backlog, or pricing are changing; investors focus on next-year earnings.

### What Usually Drives It
Markets price forward expectations. Guidance changes alter the earnings path more than the latest quarter.

### Confirming Evidence
Stock reaction aligns with guidance; analysts revise future estimates; management tone changes; backlog/orders/retention/pricing shift; peers with similar exposure move together.

### Disconfirming Evidence
Reaction is macro-driven; guidance is immaterial; reported results include a serious cash-flow or balance-sheet issue; market reaction reverses.

### Common False Positives
Overinterpreting vague management language; ignoring actual financial deterioration; confusing conservative guidance with weak demand.

### Cross-Asset Clues
Sector peers, suppliers/customers, estimate revisions, credit market reaction, relevant commodity or FX move.

### Investment Meaning
The key variable is forward estimate direction. A reported beat may not matter if the next leg of earnings is questioned.

### What to Check Next
Guidance vs prior/consensus, analyst revisions, management tone, forward indicators, peer read-through, segment-level guidance.

### Confidence Guidance
Low without transcript or estimate data; medium if price reaction matches guidance; high if revisions and peers confirm.

### Useful Source Types
Earnings release; call transcript; FactSet; company guidance history; peer commentary.

---

## 6. Expectations / Narrative Patterns

## Pattern 5: Narrative Exhaustion

### Description
A dominant market story stops producing upside even when supportive news continues. The narrative may be widely known, crowded, or already embedded in valuation.

### Typical Setup
Strong multi-month run; high media/investor attention; valuation expansion; positive news no longer moves price; marginal buyers harder to find.

### What Usually Drives It
The story becomes consensus, expectations rise faster than fundamentals, valuation leaves little room for normal good news, and the buyer base becomes saturated.

### Confirming Evidence
Weak reaction to positive headlines; multiple compression; slowing revisions; leaders stop outperforming; theme ETF flows slow/reverse; sentiment one-sided.

### Disconfirming Evidence
Fundamentals accelerate faster than valuation compresses; revisions remain strong; new buyer base emerges; pullback is broad market-driven.

### Common False Positives
Calling normal consolidation exhaustion; assuming popular narratives are automatically exhausted; ignoring macro volatility.

### Cross-Asset Clues
Theme ETFs, sector leaders vs laggards, revision breadth, valuation dispersion, options positioning, fund flows.

### Investment Meaning
The thesis may remain valid, but the market may need a new surprise, lower valuation, or broader confirmation for the next leg higher.

### What to Check Next
Does good news still work? Are estimates rising? Are flows slowing? Are leaders losing relative strength? What new information would restart the narrative?

### Confidence Guidance
Low if narrative is popular but price action remains strong; medium if reaction weakens; high if weak reaction, slowing revisions, crowding, and multiple compression align.

### Useful Source Types
Price reaction; estimate revisions; ETF/fund flows; options data; valuation history; news volume.

## Pattern 6: Narrative Acceleration / Reflexive Momentum

### Description
A narrative strengthens because price action itself validates the story. Rising prices attract attention, flows, analyst upgrades, and more buyers.

### Typical Setup
Strong theme with visible winners; price momentum attracts attention; analyst revisions follow price; new capital flows into the theme.

### What Usually Drives It
Price action becomes evidence, flows reinforce fundamentals, investors extrapolate recent growth, and thematic demand amplifies repricing.

### Confirming Evidence
Strong relative performance; rising volume/flows; analyst upgrades or estimate revisions; thematic peers move together; valuation expands alongside fundamentals.

### Disconfirming Evidence
Move isolated to one name; estimates do not improve; flows absent/reversing; move driven by one-off event.

### Common False Positives
Confusing short squeeze with durable narrative acceleration; treating media attention as fundamental evidence; ignoring valuation risk.

### Cross-Asset Clues
Related equities/ETFs, supplier/customer moves, options activity, revision breadth, fund flows.

### Investment Meaning
Momentum can persist while adoption rises, but risk grows as expectations become embedded. Fundamentals must keep validating the story.

### What to Check Next
Are estimates rising or just prices? Is move broadening? Are flows confirming? Is valuation expanding faster than fundamentals?

### Confidence Guidance
Low with price momentum only; medium with price and news confirmation; high with price, flows, revisions, and peer confirmation.

### Useful Source Types
Price data; estimate revisions; ETF/fund flows; analyst notes where accessible; earnings transcripts.

## Pattern 7: Valuation Reset Despite Stable Fundamentals

### Description
The asset declines because the valuation multiple compresses even though current fundamentals remain stable.

### Typical Setup
Rates rise; growth expectations moderate; risk appetite weakens; sector multiples compress; company executes but stock underperforms.

### What Usually Drives It
Higher risk premium, higher discount rates, prior multiple too high, or sector-wide derating.

### Confirming Evidence
Estimates stable while price falls; multiple compresses; high-multiple peers derate; rates/real yields/spreads move against the asset; no company-specific deterioration.

### Disconfirming Evidence
Estimates falling; margins/cash flow deteriorate; company-specific risk emerges; peers do not derate.

### Common False Positives
Calling fundamental deterioration a valuation reset; ignoring guidance cuts; assuming all multiple compression is macro-driven.

### Cross-Asset Clues
Rates, real yields, sector multiples, peer performance, credit spreads, growth vs value factor performance.

### Investment Meaning
Potential opportunity if fundamentals are durable, but only if the old valuation was not dependent on unrealistic assumptions.

### What to Check Next
Forward estimates, multiple history, peer derating, rates/real yields, guidance, implied growth after derating.

### Confidence Guidance
Low without estimate data; medium if price falls while estimates stable; high if broad peer derating and macro confirmation align.

### Useful Source Types
Valuation data; estimate revisions; rates; real yields; peer multiples; company guidance.

---

## 7. Positioning / Flow Patterns

## Pattern 8: Crowded Trade Unwind

### Description
A widely held long or short position reverses sharply as investors exit simultaneously, often for positioning reasons rather than immediate fundamental change.

### Typical Setup
Consensus trade; high fund ownership, ETF flows, or futures positioning; low perceived risk; stretched valuation; small catalyst triggers large move.

### What Usually Drives It
Too many investors own the same exposure; stops/risk limits force exits; liquidity is insufficient; good news no longer attracts new buyers.

### Confirming Evidence
Move larger than news; prior strong inflows/positioning; ownership concentration; correlated unwind across crowded assets; rising volatility and volume.

### Disconfirming Evidence
Major fundamental shock explains move; positioning was not crowded; move isolated and liquidity normal; asset recovers quickly.

### Common False Positives
Calling every sharp selloff a crowded unwind; using anecdotal crowding without data; ignoring fundamental news.

### Cross-Asset Clues
Related ETFs/futures, factor performance, options skew, CFTC positioning, short interest, volatility.

### Investment Meaning
Crowded unwind can create overshoot and opportunity, but may also show that the marginal buyer base is exhausted.

### What to Check Next
Was the trade widely owned? What changed fundamentally? Are flows reversing? Is liquidity deteriorating? Are forced sellers likely still present?

### Confidence Guidance
Low without positioning data; medium with sharp move and one-sided positioning; high when positioning, flows, cross-asset unwind, and liquidity stress align.

### Useful Source Types
CFTC COT; FINRA short interest; ETF/fund flows; OCC/Cboe options; volume/liquidity data.

## Pattern 9: Positioning Squeeze

### Description
Price moves sharply against a crowded position, forcing participants to cover or chase, which amplifies the move.

### Typical Setup
High short interest or one-sided futures positioning; catalyst moves price against crowded side; liquidity limited; options positioning amplifies hedging flows.

### What Usually Drives It
Forced covering/selling, stop-loss cascades, dealer hedging, thin liquidity, surprise catalyst contradicting consensus positioning.

### Confirming Evidence
High short interest or extreme futures positioning; sharp move through technical levels; high volume; options activity consistent with squeeze; move larger than news.

### Disconfirming Evidence
No crowded positioning evidence; major fundamental repricing explains move; liquidity deep/orderly; no follow-through.

### Common False Positives
Calling momentum a squeeze without positioning evidence; assuming high short interest always means squeeze risk; ignoring real thesis change.

### Cross-Asset Clues
Short interest, futures positioning, options open interest, borrow data, related asset moves.

### Investment Meaning
A squeeze can be violent but temporary. It does not validate fundamentals unless post-squeeze evidence confirms.

### What to Check Next
Short interest/days to cover, futures positioning, options strikes, borrow cost, catalyst quality, whether estimates changed.

### Confidence Guidance
Low with price move only; medium with high short interest/positioning; high with extreme positioning, catalyst, volume, and options/flow confirmation.

### Useful Source Types
FINRA short interest; CFTC COT; OCC/Cboe options; market data; securities lending data if available.

## Pattern 10: Rotation from Leaders to Laggards

### Description
Market leadership shifts away from prior winners into laggards, defensives, cyclicals, value, small caps, or other underowned areas.

### Typical Setup
Prior leaders crowded/expensive; macro regime changes; rates shift; earnings breadth improves; investors seek cheaper or underowned exposure.

### What Usually Drives It
Profit-taking, broadening participation, factor rotation, valuation dispersion normalization, fund rebalancing after concentrated leadership.

### Confirming Evidence
Prior leaders underperform while laggards rally; breadth improves; equal-weight beats cap-weight; sector/factor performance changes; flows move to neglected areas.

### Disconfirming Evidence
Rotation lasts only one or two sessions; revisions remain concentrated; leaders regain strength quickly; move driven by index rebalance or technical flow.

### Common False Positives
Treating a short-term reversal as durable rotation; ignoring earnings breadth; mistaking short covering for fundamental improvement.

### Cross-Asset Clues
Equal-weight vs cap-weight, sector ETFs, factor returns, small caps vs large caps, credit spreads, earnings revision breadth.

### Investment Meaning
Rotation can change opportunity set and timing; it may reduce near-term upside for crowded leaders and improve tactical opportunity in underowned areas.

### What to Check Next
Is breadth improving? Are revisions broadening? Are flows confirming? Is macro regime changing? Are leaders breaking down or consolidating?

### Confidence Guidance
Low for one-day reversal; medium with multi-session leadership shift; high when breadth, flows, revisions, and macro/factor confirmation align.

### Useful Source Types
Index/sector performance; factor returns; ETF flows; estimate revisions; market breadth.

---

## 8. Macro / Rates / Liquidity Patterns

## Pattern 11: Fed Repricing Shock

### Description
Markets reprice because expectations for central bank policy change, affecting rates, equities, FX, credit, commodities, and duration-sensitive assets.

### Typical Setup
Inflation/employment/Fed communication surprises; yield curve moves; Fed pricing shifts; dollar and real yields move.

### What Usually Drives It
Change in expected policy path, real rates, discount rates, liquidity expectations, or risk premium.

### Confirming Evidence
Treasury yields and Fed funds futures move materially; dollar moves; growth equities/gold/crypto/bonds react consistently; credit spreads or volatility respond.

### Disconfirming Evidence
Move isolated; rates do not move; company-specific news explains action; earnings momentum overwhelms rate move.

### Common False Positives
Attributing every equity move to rates; ignoring earnings revisions; confusing nominal yield moves with real yield moves.

### Cross-Asset Clues
Treasury yields, real yields, DXY, gold, Bitcoin, Nasdaq/growth, credit spreads, VIX.

### Investment Meaning
The key question is whether policy repricing changes valuation, earnings path, liquidity support, or risk appetite.

### What to Check Next
Fed funds futures, Treasury curve, real yields, breakevens, dollar, sectors/factors, credit spreads.

### Confidence Guidance
Low if rates move modestly; medium if rates and rate-sensitive assets move together; high if policy catalyst and cross-asset moves align.

### Useful Source Types
Fed communications; Treasury/FRED data; Fed pricing; DXY; real yields; credit spreads.

## Pattern 12: Liquidity Rally Despite Weak Fundamentals

### Description
Risk assets rise even though earnings, macro data, or fundamentals look weak because liquidity, policy expectations, financial conditions, or risk appetite dominate.

### Typical Setup
Easing expectations rise; real yields fall; credit spreads tighten; volatility declines; weak data is interpreted as supportive for policy easing.

### What Usually Drives It
“Bad news is good news” regime, lower discount rates, easing liquidity expectations, short covering, risk re-leveraging.

### Confirming Evidence
Weak data with falling yields and rising equities; credit spreads tighten; VIX declines; high-beta and long-duration assets outperform; dollar weakens if easing dominates.

### Disconfirming Evidence
Earnings revisions improve materially; rally is company-specific; credit spreads widen; yields rise; liquidity proxies do not confirm.

### Common False Positives
Calling every weak-data rally liquidity-driven; ignoring earnings resilience; confusing short-covering bounce with liquidity regime.

### Cross-Asset Clues
Yields, real yields, credit spreads, VIX, high beta vs low volatility, crypto/speculative assets, dollar.

### Investment Meaning
Rally may be vulnerable if policy expectations reverse or earnings weakness becomes too large to ignore.

### What to Check Next
Are financial conditions easing? Are yields falling for good or bad reasons? Is credit confirming? Are revisions deteriorating?

### Confidence Guidance
Low if only equities rally; medium if equities rally with lower yields/vol; high if yields, credit, volatility, high beta, and liquidity proxies confirm.

### Useful Source Types
Fed/central bank data; FRED yields/spreads; IMF/Fed financial stability; VIX; cross-asset data.

## Pattern 13: Growth Scare

### Description
Markets begin pricing weaker growth, recession risk, or demand slowdown. Risk assets, cyclicals, commodities, credit, and yields may move in a growth-negative direction.

### Typical Setup
Weak employment, PMI, retail sales, production, or guidance; cyclicals underperform defensives; yields fall; spreads widen; commodities weaken.

### What Usually Drives It
Earnings expectations fall, demand outlook deteriorates, investors seek defensives/duration, and credit risk rises.

### Confirming Evidence
Cyclicals underperform defensives; credit spreads widen; commodities decline; earnings revisions weaken; small caps underperform.

### Disconfirming Evidence
Weak data offset by strong earnings; credit spreads tight; cyclicals and commodities hold up; policy easing dominates positively.

### Common False Positives
Confusing disinflation with growth scare; treating one weak print as regime shift; ignoring policy support.

### Cross-Asset Clues
Treasury yields, credit spreads, cyclicals vs defensives, commodities, small caps, earnings revisions.

### Investment Meaning
Growth-sensitive assets may face pressure; defensive duration assets may benefit if inflation is not dominant.

### What to Check Next
Breadth of weak data, earnings revisions, credit spreads, commodity demand indicators, sector leadership, central bank reaction function.

### Confidence Guidance
Low with one data point; medium with weak data plus sector rotation; high with macro, credit, commodities, revisions, and leadership alignment.

### Useful Source Types
Official macro data; FRED spreads; sector/factor performance; earnings revisions; commodity data.

## Pattern 14: Inflation Scare

### Description
Markets price higher inflation risk, often leading to higher yields, pressure on duration assets, commodity sensitivity, and uncertainty around central bank policy.

### Typical Setup
Inflation data surprises higher; oil/commodities rise; wage/services inflation sticky; central bank turns hawkish; yields rise.

### What Usually Drives It
Higher expected policy rates, higher discount rates, margin pressure, real income pressure, and commodity/wage cost concerns.

### Confirming Evidence
Nominal yields rise; real yields and/or breakevens rise; dollar strengthens if policy repricing dominates; long-duration equities underperform; rate-cut expectations fade.

### Disconfirming Evidence
Inflation surprise is narrow/one-off; breakevens do not move; real yields fall; equities rally because growth dominates; central bank downplays data.

### Common False Positives
Treating oil shock as broad inflation scare without second-round evidence; ignoring base effects; confusing higher growth with higher inflation.

### Cross-Asset Clues
Nominal yields, real yields, breakevens, dollar, gold, commodities, growth vs value, credit spreads.

### Investment Meaning
Inflation scares can pressure long-duration assets and support inflation-sensitive exposures, depending on whether the market sees growth-positive, margin-negative, or policy-tightening effects.

### What to Check Next
Inflation components, breakevens vs real yields, Fed pricing, commodity drivers, sector leadership, margin sensitivity.

### Confidence Guidance
Low with one print; medium if yields/breakevens confirm; high if inflation data, rates, policy pricing, commodities, and factors align.

### Useful Source Types
Official inflation data; FRED yields/breakevens; Fed communications; commodity data; sector performance.

---

## 9. Cross-Asset / Regime Patterns

## Pattern 15: Safe-Haven Fails Because Dollar / Rates Dominate

### Description
An asset expected to benefit from risk aversion or geopolitical stress, especially gold, fails to rally or declines because dollar strength, real yields, or positioning pressure dominate.

### Typical Setup
Geopolitical/risk-off headlines; dollar rises; real yields rise; gold or safe havens underperform; prior positioning already long.

### What Usually Drives It
Real yields raise opportunity cost, dollar strength pressures assets, safe-haven premium was already priced, or investors sell liquid winners to raise cash.

### Confirming Evidence
Gold falls while DXY and real yields rise; miners underperform bullion; gold ETF flows weak; futures positioning crowded long; safe-haven assets mixed.

### Disconfirming Evidence
Strong ETF inflows or central bank demand; gold rallies despite higher yields; dollar/real yields not moving; weakness due to unrelated technical factor.

### Common False Positives
Assuming geopolitics always lifts gold; ignoring prior positioning; looking only at headlines rather than cross-asset reaction.

### Cross-Asset Clues
DXY, real yields, miners, silver, Treasury yields, ETF flows, CFTC gold positioning.

### Investment Meaning
Buying safe-haven assets may be less about geopolitics and more about a view that rates/dollar pressure will stop dominating.

### What to Check Next
Real yields, DXY, ETF flows, futures positioning, miners vs bullion, Fed pricing, whether geopolitical risk creates real financial stress.

### Confidence Guidance
Low without rates/dollar data; medium if gold falls with rising DXY and real yields; high if rates, dollar, positioning, ETF flows, and miners confirm.

### Useful Source Types
FRED real yields; DXY; CFTC COT; ETF flows; gold/miner prices; macro news.

## Pattern 16: Risk Rally Despite Bad Macro Data

### Description
Risk assets rally after weak macro data because investors interpret the data as increasing the probability of policy easing, lower rates, or liquidity support.

### Typical Setup
Weak macro data; yields fall; rate-cut expectations rise; equities rally, especially duration/high beta; credit spreads stable or tighter.

### What Usually Drives It
Bad news becomes good news under an easing reaction function; discount-rate relief outweighs growth concern; defensive positioning unwinds.

### Confirming Evidence
Yields fall; rate-cut pricing rises; equities rally; credit spreads do not widen; high-duration/high-beta assets outperform; dollar weakens if easing dominates.

### Disconfirming Evidence
Credit spreads widen; cyclicals collapse; earnings revisions deteriorate; central bank pushes back; rally fades quickly.

### Common False Positives
Confusing rate relief with true growth confidence; ignoring credit stress; assuming all weak-data rallies are sustainable.

### Cross-Asset Clues
Treasury yields, Fed funds futures, credit spreads, high beta vs defensives, dollar, VIX.

### Investment Meaning
Rally is vulnerable if weak growth damages earnings or central banks resist the market’s easing interpretation.

### What to Check Next
Did data change policy expectations? Did credit confirm? Did earnings-sensitive sectors rally? Did central bank speakers validate?

### Confidence Guidance
Low without rates confirmation; medium with yields down and equities up; high if rates, credit, volatility, and sectors confirm.

### Useful Source Types
Official macro releases; rates/Fed pricing; FRED spreads; VIX; sector performance.

---

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

## 11. Commodity / Geopolitical Patterns

## Pattern 19: Geopolitical Headline Without Supply Shock

### Description
A geopolitical event creates headlines and temporary volatility, but the commodity or related asset does not sustain a move because physical supply, demand, inventories, or transit routes are not materially affected.

### Typical Setup
Military/diplomatic/geopolitical headline; initial commodity spike; no confirmed physical disruption; inventories/spare capacity cushion shock; market fades move.

### What Usually Drives It
Headline risk premium appears briefly, but physical market does not confirm shortage. Traders wait for real disruption evidence.

### Confirming Evidence
Price spike fades; no confirmed supply loss; futures curve does not tighten; inventories adequate; shipping/transit data show limited disruption; related equities do not confirm.

### Disconfirming Evidence
Physical supply loss confirmed; inventories draw; futures curve tightens; shipping routes/export flows disrupted; agencies revise supply lower.

### Common False Positives
Assuming no immediate move means no risk; ignoring delayed effects; treating political statements as physical evidence.

### Cross-Asset Clues
Spot vs futures curve, energy equities, shipping/tanker data, inventories, refined products, producer-country FX.

### Investment Meaning
The market may require confirmed supply disruption, not just geopolitical tension, for a durable commodity move.

### What to Check Next
Confirmed supply loss, inventories, curve shape, agency revisions, shipping routes, related equities.

### Confidence Guidance
Low with headline only; medium if spike fades with no physical confirmation; high if physical data, curve, inventories, and agency reports confirm no sustained disruption.

### Useful Source Types
EIA STEO; IEA Oil Market Report; OPEC MOMR; World Bank Commodity Markets; ECB geopolitical/oil analysis; futures and inventory data.

## Pattern 20: Commodity Supply Shock Repricing

### Description
A commodity reprices because the market recognizes a real or probable physical supply constraint, not merely headline risk.

### Typical Setup
Confirmed production outage, export restriction, transit disruption, sanctions, weather event, or war-related supply loss; low inventories; limited spare capacity; curve tightens.

### What Usually Drives It
Physical supply-demand balance tightens, buyers bid for near-term supply, inventories become more valuable, and producers/substitutes reprice.

### Confirming Evidence
Official data confirm supply loss; inventories draw; curve moves into stronger backwardation; spot outperforms deferred contracts; producers rally; agencies revise deficit higher.

### Disconfirming Evidence
Disruption resolved; inventories ample; demand falls enough to offset supply loss; spare capacity fills gap; curve does not tighten.

### Common False Positives
Mistaking geopolitical headlines for physical shock; ignoring demand destruction; ignoring policy response, reserves, substitution, or positioning.

### Cross-Asset Clues
Futures curve, inventories, producer equities, product spreads, shipping data, producer/importer FX, inflation breakevens.

### Investment Meaning
A real supply shock can create durable price support, but the thesis must account for demand destruction, policy response, and positioning.

### What to Check Next
Size/duration of supply loss, inventories, curve shape, demand response, spare capacity, policy response, positioning, prior price move.

### Confidence Guidance
Low if supply risk is narrative only; medium with partial physical evidence and curve confirmation; high with official supply loss, inventory draw, curve tightening, and related asset confirmation.

### Useful Source Types
EIA, IEA, OPEC; World Bank commodity reports; futures curve; inventory data; producer reports; shipping/logistics sources.

## 12. Optional Future Patterns

Potential future additions:

- Demand slowdown repricing.
- Policy put / central-bank rescue expectation.
- Dollar squeeze.
- Volatility crush after event risk.
- Earnings revision inflection.
- Thematic capex boom exhaustion.
- Regulatory overhang repricing.
- Quality flight within a sector.
- Private-market stress leaking into public markets.
- Passive flow distortion.

## 13. Final Reminder

Market patterns are tools for disciplined interpretation. They should force every market read into a structured test:

```text
Hypothesis:
What matches:
What does not match:
Evidence status:
Confidence:
False-positive risk:
What to verify next:
Investment implication:
```

If the evidence is insufficient, the correct output is:

```text
No clear pattern confirmed. Evidence is insufficient.
```

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

## 15. Example Applications

These examples show how the library should be used. They are illustrative frameworks, not permanent market conclusions.

### Example 1: Gold Falls Despite Geopolitical Tension

#### Observable Facts

- Gold declines.
- Dollar rises.
- Real yields rise.
- Geopolitical headlines remain tense.
- Gold miners underperform bullion.

#### Candidate Pattern

Safe-Haven Fails Because Dollar / Rates Dominate.

#### What Matches

- Gold weakness occurs alongside stronger dollar and higher real yields.
- Miners confirm weaker gold risk appetite.
- Geopolitical headlines alone do not create a sustained safe-haven bid.

#### What Does Not Match / Counter-Hypothesis

- If ETF flows or central bank demand are strong, safe-haven demand may still be present.
- The move could be profit-taking after a prior rally rather than a regime change.

#### Evidence Status

Plausible, if real yields and DXY moves are confirmed.

#### Confidence

Medium only if rates, dollar, miners, and flows align. Low if only price action is known.

#### What to Check Next

- DXY.
- 10-year real yields.
- Gold ETF flows.
- CFTC gold positioning.
- Miners vs bullion.
- Fed pricing.

#### Investment Implication

Buying gold in this setup is not simply a geopolitical bet. It is mainly a bet that rates and dollar pressure will stop dominating marginal price action.

### Example 2: Nvidia Rises Despite Higher Yields

#### Observable Facts

- Nvidia rises or holds up.
- Treasury yields rise.
- Growth equities are mixed.
- AI-related peers or suppliers also perform well.
- Earnings revisions remain positive.

#### Candidate Pattern

Narrative Acceleration / Reflexive Momentum, with possible Fed Repricing Shock rejected or outweighed.

#### What Matches

- The stock is not trading primarily as a long-duration asset.
- Earnings revision momentum or AI infrastructure narrative may dominate discount-rate pressure.
- Peer confirmation supports an asset-specific or theme-specific driver.

#### What Does Not Match / Counter-Hypothesis

- Move could be passive flow, options-driven momentum, or short-term squeeze.
- If estimate revisions do not improve, price action may be momentum rather than fundamental repricing.

#### Evidence Status

Plausible if peer moves and estimate revisions confirm.

#### Confidence

Medium. High requires sustained revisions, peer confirmation, and evidence that rates are not the dominant driver.

#### What to Check Next

- Forward EPS and revenue revisions.
- Data center revenue expectations.
- Hyperscaler capex commentary.
- Semiconductor peer performance.
- Options positioning.
- Valuation multiple trend.

#### Investment Implication

The key risk may not be that the AI thesis is false. The key risk may be that expectations become so high that the stock requires continuous positive surprises.

### Example 3: Oil Spikes on Geopolitical Headline Then Fades

#### Observable Facts

- Oil spikes after geopolitical headline.
- Move fades within days.
- No confirmed physical supply loss.
- Futures curve does not materially tighten.
- Energy equities do not confirm the initial spike.

#### Candidate Pattern

Geopolitical Headline Without Supply Shock.

#### What Matches

- Headline created risk premium, but physical market did not confirm.
- Futures curve and equities failed to validate durable supply disruption.

#### What Does Not Match / Counter-Hypothesis

- Disruption may be delayed.
- Shipping routes, sanctions, insurance, or export flows may deteriorate later.

#### Evidence Status

Plausible if physical supply data and curve behavior confirm.

#### Confidence

Medium. High requires confirmation from inventories, curve, shipping/export data, and agency reports.

#### What to Check Next

- EIA / IEA / OPEC updates.
- Inventory data.
- Futures curve shape.
- Shipping or transit disruption.
- Producer equity reaction.
- Demand revisions.

#### Investment Implication

A durable oil trade requires evidence of physical supply disruption or sustained risk premium, not just geopolitical headlines.

### Example 4: Weak Macro Data, Equities Rally

#### Observable Facts

- Macro data disappoints.
- Treasury yields fall.
- Equities rally.
- Credit spreads remain stable or tighten.
- High-duration or high-beta assets outperform.

#### Candidate Pattern

Risk Rally Despite Bad Macro Data / Liquidity Rally Despite Weak Fundamentals.

#### What Matches

- Market interprets weak data as increasing odds of policy easing.
- Lower yields support duration and risk appetite.
- Credit does not confirm stress.

#### What Does Not Match / Counter-Hypothesis

- If credit spreads widen, the market may be shifting toward growth scare.
- If earnings revisions deteriorate sharply, liquidity support may not be enough.

#### Evidence Status

Plausible if rates, credit, volatility, and sector leadership confirm.

#### Confidence

Medium to High depending on cross-asset confirmation.

#### What to Check Next

- Fed funds futures.
- Treasury curve.
- Credit spreads.
- VIX.
- Sector leadership.
- Earnings revisions.

#### Investment Implication

The rally may be real in the short term but vulnerable if weak data begins damaging earnings or if central banks reject the easing interpretation.

### Example 5: Company Beats Earnings, Stock Falls

#### Observable Facts

- Reported EPS/revenue beat consensus.
- Stock falls after earnings.
- Stock had rallied into the print.
- Guidance is only maintained or slightly raised.
- Forward estimate revisions are muted.

#### Candidate Pattern

Earnings Beat Already Priced In / Good News, Bad Price Action.

#### What Matches

- Positive reported results did not create incremental upside.
- Pre-event rally suggests expectations were high.
- Guidance did not create a new earnings revision cycle.

#### What Does Not Match / Counter-Hypothesis

- Hidden negative detail may explain the move.
- Broad market selloff may dominate.
- The beat may be low quality due to one-offs or accounting items.

#### Evidence Status

Plausible if pre-event rally, guidance, and muted revisions are confirmed.

#### Confidence

Medium. High requires confirmation from revisions, peer behavior, and management commentary.

#### What to Check Next

- Guidance vs consensus.
- Forward EPS/revenue revisions.
- Margin and FCF quality.
- Peer reaction.
- Options implied move.
- Call transcript.

#### Investment Implication

The issue may be expectations and valuation rather than the current quarter. Future upside may require a higher-quality beat or stronger guidance.

## 16. High-Quality Source Map for Core Patterns

This section identifies the most reliable academic, official, and professional sources for strengthening the most important Market Sense patterns.

Use this source map as follows:

```text
Academic sources -> explain why a pattern can exist.
Official data sources -> verify whether the pattern is active.
Professional sources -> show how practitioners monitor the pattern.
```

A source does not confirm a pattern by itself. It supports the framework or provides data for verification.

### 16.1 Good News, Bad Price Action / Earnings Beat Already Priced In

Relevant patterns:

- Pattern 1: Good News, Bad Price Action
- Pattern 3: Earnings Beat Already Priced In
- Pattern 4: Guidance Matters More Than Reported Results

Core idea:

Stock prices react to surprises relative to expectations, not to whether the headline is simply good or bad. A reported beat can be insufficient if the market expected more, if guidance is weak, or if forward estimates fail to rise.

High-quality sources:

- [Bernard & Thomas — Post-Earnings-Announcement Drift](https://ideas.repec.org/a/bla/joares/v27y1989ip1-36.html)  
  Use for: academic foundation that markets may underreact to earnings information and that earnings news can have delayed pricing effects.

- [JSTOR — Post-Earnings-Announcement Drift](https://www.jstor.org/stable/2491062)  
  Use for: original academic source when accessible.

- [FactSet Earnings Insight](https://www.factset.com/earningsinsight)  
  Use for: professional earnings-season data, surprise rates, valuation context, guidance, and estimate revisions.

- [FactSet Earnings Research](https://insight.factset.com/topic/earnings)  
  Use for: practical monitoring of earnings reactions, estimate revisions, and market expectations.

- [Management Forecasts and Analyst Forecast Revisions Around Earnings](https://pubsonline.informs.org/doi/10.1287/mnsc.2014.1920)  
  Use for: guidance and analyst revision interaction around earnings announcements.

How to strengthen the pattern:

- Add emphasis that “good news” must be evaluated against consensus, buy-side expectations, prior price move, and guidance.
- Require checking forward estimate revisions after the event.
- Distinguish reported beat from true expectation reset.
- Treat guidance and management tone as more important than historical results when the market is focused on the forward earnings path.

Evidence threshold:

- Low: only headline beat and stock decline are known.
- Medium: stock rallied into event, beat was expected, guidance did not improve, and price reaction was weak.
- High: pre-event run-up, muted/negative forward revisions, weak peer confirmation, and options/positioning evidence all align.

Useful checks:

- Pre-event price run.
- Consensus and estimate revision path.
- Guidance vs consensus.
- Forward EPS and revenue revisions.
- Peer reaction.
- Options implied move vs realized move.
- Transcript tone and key forward indicators.

### 16.2 Narrative Exhaustion / Reflexive Momentum

Relevant patterns:

- Pattern 5: Narrative Exhaustion
- Pattern 6: Narrative Acceleration / Reflexive Momentum
- Pattern 7: Valuation Reset Despite Stable Fundamentals

Core idea:

Narratives can shape how investors interpret facts, but narrative-based market interpretation must be tied to observable price, valuation, flow, and revision evidence.

High-quality sources:

- [Yale Insights — Robert Shiller, Narrative Economics](https://insights.som.yale.edu/insights/narrative-economics-how-stories-go-viral)  
  Use for: conceptual foundation that viral stories can influence economic behavior and market perception.

- [Yale Online — Narrative Economics](https://online.yale.edu/courses/narrative-economics)  
  Use for: broader conceptual background on narrative economics.

- [Baker & Wurgler — Investor Sentiment and the Cross-Section of Stock Returns](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=464843)  
  Use for: academic basis that investor sentiment can affect securities differently, especially those with subjective valuation or limits to arbitrage.

- [Barberis, Shleifer & Vishny — A Model of Investor Sentiment](https://shleifer.scholars.harvard.edu/publications/model-investor-sentiment)  
  Use for: underreaction and overreaction framework.

- [Shleifer & Vishny — The Limits of Arbitrage](https://shleifer.scholars.harvard.edu/publications/limits-arbitrage)  
  Use for: why mispricing or narrative-driven pricing can persist longer than expected.

How to strengthen the pattern:

- Define narrative as a market interpretation frame, not a story detached from evidence.
- Require evidence that the narrative affects price behavior: valuation expansion/compression, flow, revisions, peer moves, or weakening reaction to positive news.
- Add explicit false-positive: popularity alone is not narrative exhaustion.
- Add explicit false-positive: price momentum alone is not reflexive narrative without flows/revisions/peer confirmation.

Evidence threshold:

- Low: narrative is visible in media but price/revision/flow evidence is missing.
- Medium: price reaction and valuation behavior suggest the narrative matters.
- High: narrative evidence, price action, flows, estimate revisions, and peer/theme confirmation align.

Useful checks:

- Does good news still move the asset?
- Are estimates accelerating or slowing?
- Is valuation expanding faster than fundamentals?
- Are ETF/theme flows confirming?
- Are leaders still leading?
- Is narrative becoming consensus?

### 16.3 Crowded Trade Unwind / Positioning Squeeze

Relevant patterns:

- Pattern 8: Crowded Trade Unwind
- Pattern 9: Positioning Squeeze
- Pattern 10: Rotation from Leaders to Laggards

Core idea:

A large move may be driven by positioning, forced covering, or crowded exposure rather than a proportional change in fundamentals. Crowding must be evidenced, not asserted.

High-quality sources:

- [AQR — Momentum Crashes](https://www.aqr.com/Insights/Research/Journal-Article/Momentum-Crashes)  
  Use for: professional/academic explanation of momentum reversals and crash risk in crowded momentum regimes.

- [NBER — Momentum Crashes](https://www.nber.org/system/files/working_papers/w20439/w20439.pdf)  
  Use for: academic paper version of momentum crash research.

- [Shleifer & Vishny — Fire Sales in Finance and Macroeconomics](https://www.nber.org/system/files/working_papers/w16642/w16642.pdf)  
  Use for: forced selling and dislocated prices.

- [FINRA Short Interest Data](https://www.finra.org/finra-data/browse-catalog/equity-short-interest/data)  
  Use for: official short interest data for equities.

- [CFTC Commitments of Traders](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm)  
  Use for: official futures positioning.

- [OCC Options Volume / Open Interest](https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/daily-volume)  
  Use for: options activity and open interest.

- [Cboe Daily Options Statistics](https://www.cboe.com/markets/us/options/market-statistics/daily/)  
  Use for: options market activity and sentiment proxies.

How to strengthen the pattern:

- Require evidence of crowdedness before labeling a move “crowded unwind.”
- Separate short squeeze, long squeeze, factor unwind, and broad forced deleveraging.
- Add rule: high short interest is not automatically bearish; it can create squeeze risk.
- Add rule: a sharp move is not enough to infer forced positioning.

Evidence threshold:

- Low: large move with no positioning data.
- Medium: large move plus one positioning proxy, such as high short interest, extreme CFTC positioning, or heavy options concentration.
- High: positioning extreme, catalyst, high volume, cross-asset/factor confirmation, and liquidity stress align.

Useful checks:

- Short interest / days to cover.
- CFTC positioning.
- Options open interest and volume.
- ETF/fund flows.
- Volume and liquidity.
- Factor and peer moves.
- Whether fundamentals actually changed.

### 16.4 Safe-Haven Fails Because Dollar / Rates Dominate

Relevant patterns:

- Pattern 15: Safe-Haven Fails Because Dollar / Rates Dominate
- Pattern 19: Geopolitical Headline Without Supply Shock, when commodity/geopolitical context overlaps

Core idea:

A safe-haven asset such as gold may fail to rally during geopolitical stress if real yields, dollar strength, positioning, or prior pricing dominate marginal price action.

High-quality sources:

- [Chicago Fed — What Drives Gold Prices?](https://www.chicagofed.org/publications/chicago-fed-letter/2021/464)  
  Use for: official/professional analysis of gold drivers, including real rates, inflation expectations, and pessimism.

- [World Gold Council — Gold Demand Trends](https://www.gold.org/goldhub/research/gold-demand-trends)  
  Use for: professional data on ETF flows, central bank demand, bar/coin demand, and demand mix.

- [FRED](https://fred.stlouisfed.org/)  
  Use for: real yields, nominal yields, inflation breakevens, credit spreads, and other macro variables.

- [CFTC Commitments of Traders](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm)  
  Use for: gold futures positioning.

- [ECB — Geopolitical Risk and Oil Prices](https://www.ecb.europa.eu/press/economic-bulletin/focus/2024/html/ecb.ebbox202308_02~ed883ebf56.en.html)  
  Use for: distinction between geopolitical headlines and actual market impact, especially in commodities.

How to strengthen the pattern:

- State that gold can trade under different regimes: safe-haven, inflation hedge, real-yield asset, dollar-sensitive asset, central-bank demand asset.
- Require checking real yields and DXY before accepting a geopolitical explanation.
- Require checking ETF flows and futures positioning before claiming safe-haven demand or crowded long unwind.

Evidence threshold:

- Low: gold falls despite geopolitical headlines, but no rates/dollar/flow data is checked.
- Medium: gold falls while real yields and DXY rise.
- High: gold falls while real yields and DXY rise, ETF flows are weak/negative, futures positioning is long, and miners underperform bullion.

Useful checks:

- DXY.
- 10-year real yields.
- Inflation breakevens.
- Gold ETF flows.
- CFTC gold positioning.
- Miners vs bullion.
- Central bank demand if relevant.

### 16.5 Liquidity Rally Despite Weak Fundamentals / Risk Rally Despite Bad Macro Data

Relevant patterns:

- Pattern 12: Liquidity Rally Despite Weak Fundamentals
- Pattern 16: Risk Rally Despite Bad Macro Data

Core idea:

Weak macro data can support risk assets if the market believes it increases the probability of easier policy, lower rates, or looser financial conditions. This is only valid if cross-asset evidence confirms easing expectations and credit stress does not dominate.

High-quality sources:

- [Bernanke & Kuttner — What Explains the Stock Market’s Reaction to Federal Reserve Policy?](https://www.federalreserve.gov/pubs/feds/2004/200416/200416pap.pdf)  
  Use for: monetary policy surprises and equity market reaction.

- [NBER version — What Explains the Stock Market’s Reaction to Federal Reserve Policy?](https://www.nber.org/system/files/working_papers/w10402/w10402.pdf)  
  Use for: academic version and citation trail.

- [Chicago Fed — Monetary Policy and the Stock Market in the Covid Era](https://www.chicagofed.org/publications/economic-perspectives/2023/5)  
  Use for: policy, liquidity, and asset-price interaction.

- [San Francisco Fed — Monetary Policy and Financial Conditions](https://www.frbsf.org/research-and-insights/publications/economic-letter/2024/03/monetary-policy-and-financial-conditions/)  
  Use for: link between monetary policy, macro news, and financial conditions.

- [IMF Global Financial Stability Report](https://www.imf.org/en/publications/gfsr)  
  Use for: financial stability, liquidity, and risk appetite context.

- [Federal Reserve Financial Stability Report](https://www.federalreserve.gov/publications/financial-stability-report.htm)  
  Use for: financial conditions, leverage, vulnerabilities, and risk appetite context.

How to strengthen the pattern:

- Add distinction between “bad news is good news” and true growth scare.
- Require checking credit spreads: if spreads widen materially, weak data may be a growth-scare signal, not liquidity support.
- Require checking yields, Fed pricing, dollar, VIX, and high-beta leadership.

Evidence threshold:

- Low: weak data and equities up, but rates/credit/volatility not checked.
- Medium: weak data, yields lower, equities higher, volatility lower.
- High: weak data, rate-cut pricing rises, credit spreads stable/tighter, VIX falls, high-duration/high-beta assets outperform.

Useful checks:

- Fed funds futures / rate-cut pricing.
- Treasury yields and real yields.
- Credit spreads.
- VIX.
- Dollar.
- High beta vs defensives.
- Earnings revisions.

### 16.6 Fed Repricing Shock

Relevant patterns:

- Pattern 11: Fed Repricing Shock
- Pattern 7: Valuation Reset Despite Stable Fundamentals
- Pattern 14: Inflation Scare, when repricing is inflation-driven

Core idea:

Markets react to unexpected changes in the expected policy path, not merely to the level of rates. The same yield move can mean different things depending on whether it reflects growth, inflation, real-rate repricing, or policy communication.

High-quality sources:

- [Bernanke & Kuttner — What Explains the Stock Market’s Reaction to Federal Reserve Policy?](https://www.federalreserve.gov/pubs/feds/2004/200416/200416pap.pdf)  
  Use for: equity market reaction to unanticipated monetary policy changes.

- [NY Fed — Monetary Policy Surprises and Interest Rates](https://www.newyorkfed.org/research/staff_reports/sr99.html)  
  Use for: separating anticipated and unanticipated policy moves using futures markets.

- [Federal Reserve — The Effect of the Federal Reserve on the Stock Market](https://www.federalreserve.gov/econres/feds/files/2026023pap.pdf)  
  Use for: modern survey / extension on Fed effects, FOMC announcement effects, and stock returns.

- [Chicago Fed — Past and Future Effects of the Recent Monetary Policy Tightening](https://www.chicagofed.org/publications/chicago-fed-letter/2023/483)  
  Use for: policy transmission and forward guidance context.

How to strengthen the pattern:

- Require checking policy surprise, not just rate level.
- Separate nominal yields, real yields, and inflation breakevens.
- Check whether earnings revisions or sector fundamentals are overpowering rate pressure.
- Avoid automatically saying “rates up = growth stocks down.”

Evidence threshold:

- Low: asset moves and rates move, but policy expectations are not checked.
- Medium: yields, real yields, and rate expectations move in a consistent direction.
- High: policy catalyst, Fed pricing, real yields, dollar, sector/factor moves, and credit/volatility confirm.

Useful checks:

- Fed funds futures.
- Treasury curve.
- Real yields.
- Inflation breakevens.
- DXY.
- Growth vs value.
- Credit spreads.
- Central bank communication.

### 16.7 Credit Stress / Forced Deleveraging

Relevant patterns:

- Pattern 17: Credit Stress Leak-Through
- Pattern 18: Forced Deleveraging
- Pattern 8: Crowded Trade Unwind, when forced exits overlap with crowding

Core idea:

Stress-driven selling is different from ordinary risk-off. It requires evidence of credit stress, funding pressure, liquidity deterioration, or forced selling. A selloff alone is not enough.

High-quality sources:

- [Brunnermeier & Pedersen — Market Liquidity and Funding Liquidity](https://www.princeton.edu/~markus/research/papers/liquidity.pdf)  
  Use for: interaction between market liquidity, funding liquidity, and liquidity spirals.

- [BIS — Funding Liquidity Risk](https://www.bis.org/publ/work316.pdf)  
  Use for: funding liquidity risk and financial market stress.

- [Shleifer & Vishny — Fire Sales in Finance and Macroeconomics](https://www.nber.org/system/files/working_papers/w16642/w16642.pdf)  
  Use for: forced sales and dislocated prices.

- [Federal Reserve Financial Stability Report](https://www.federalreserve.gov/publications/financial-stability-report.htm)  
  Use for: leverage, vulnerabilities, liquidity, and financial stability monitoring.

- [Office of Financial Research Reports](https://www.financialresearch.gov/reports/)  
  Use for: financial stability, leverage, funding, and systemic risk monitoring.

- [FRED — ICE BofA US High Yield OAS](https://fred.stlouisfed.org/series/BAMLH0A0HYM2)  
  Use for: high-yield credit stress.

- [FRED — ICE BofA BBB Corporate OAS](https://fred.stlouisfed.org/series/BAMLC0A4CBBB)  
  Use for: investment-grade / BBB spread stress.

How to strengthen the pattern:

- Add rule: “risk-off” requires observable evidence.
- Add rule: forced deleveraging requires more than price decline; look for volatility, spreads, correlations, liquidity, and funding pressure.
- Add distinction between credit-led stress and equity valuation reset.

Evidence threshold:

- Low: equities sell off sharply, but credit/funding/liquidity not checked.
- Medium: equity volatility rises and credit spreads widen.
- High: credit spreads widen, volatility spikes, liquidity deteriorates, correlations rise, liquid assets are sold, and funding stress appears.

Useful checks:

- HY and BBB credit spreads.
- VIX and volatility term structure.
- Bank and broker equities.
- Corporate bond ETFs.
- Treasury market functioning.
- Cross-asset correlations.
- Liquidity / bid-ask where available.

## 17. How to Use the Source Map in Future Pattern Edits

When improving any pattern card, use this structure:

```md
### Stronger Research Basis
- Academic foundation:
- Official data sources:
- Professional monitoring sources:

### Evidence Upgrade
- Minimum evidence:
- Medium-confidence evidence:
- High-confidence evidence:

### Common Misuse to Avoid
- Unsupported interpretation:
- Better phrasing:
```

Example:

```text
Unsupported interpretation:
The market is scared.

Better phrasing:
Credit spreads widened, VIX rose, and high-beta assets underperformed, which supports a plausible hypothesis that risk appetite deteriorated.
```
