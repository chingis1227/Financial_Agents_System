# Crypto Data Source and Metric Framework

## Purpose

This framework defines source hierarchy, freshness rules, metric caveats, and fallback protocols for Crypto Agent analysis.

Crypto data is useful but uneven. The agent must separate primary data, professional data, dashboards, aggregators, and market commentary.

## Source Hierarchy

### Tier 1 — Primary / Official

Preferred for decision-critical claims:

- SEC;
- CFTC;
- Congress.gov;
- Federal Reserve;
- U.S. Treasury;
- IRS;
- FinCEN;
- official ETF issuer filings and prospectuses;
- ETF issuer flow / AUM pages where available;
- exchange official announcements;
- protocol documentation;
- governance forums;
- official roadmaps;
- blockchain explorers and raw chain data;
- audited reserve reports;
- official attestations;
- official foundation / protocol disclosures.

### Tier 2 — Professional / Institutional

Useful when methodology is visible:

- Coinbase Institutional;
- Galaxy;
- Bitwise;
- Fidelity Digital Assets;
- BlackRock / iShares;
- VanEck;
- Grayscale;
- ARK;
- CME;
- Kaiko;
- CCData;
- Chainalysis;
- Glassnode;
- CryptoQuant;
- Coin Metrics;
- professional research providers with transparent methodology.

Tier 2 sources may support decision-relevant conclusions, but methodology and as-of dates must be noted.

### Tier 3 — Aggregators / Dashboards

Useful for monitoring, proxies, and fallback:

- DefiLlama;
- Token Terminal;
- Dune dashboards;
- CoinGecko;
- CoinMarketCap;
- The Block data;
- DeFi dashboards;
- exchange dashboards;
- explorer-derived dashboards.

Dashboard data must not be treated as final truth without caveats.

### Tier 4 — Market Commentary / Social

Use only as narrative or sentiment context:

- X / Twitter;
- Substack;
- Telegram;
- YouTube;
- newsletters;
- influencer commentary;
- unofficial screenshots.

Tier 4 cannot support decision-grade conclusions by itself.

## Freshness Rules

### Same-Day / Near-Current Required When Setup Matters

- price;
- market cap;
- FDV;
- trading volume;
- funding rates;
- open interest;
- liquidations;
- ETF daily flows;
- major exchange outage;
- hack;
- depeg;
- regulatory headline;
- major protocol outage.

### Daily / Recent Required

- spot vs futures volume;
- exchange reserves and flows;
- ETF AUM;
- cumulative ETF flows;
- stablecoin supply;
- DeFi TVL;
- DEX / CEX activity;
- major on-chain metrics;
- BTC dominance;
- ETH/BTC;
- total crypto market capitalization.

### Weekly / Monthly Acceptable

- protocol fees;
- revenue-like metrics;
- developer activity;
- active-address trends;
- transaction trends;
- staking participation;
- validator economics;
- tokenization / RWA adoption;
- roadmap progress.

### Event-Driven

- regulation;
- ETF approvals and filings;
- protocol upgrades;
- token unlocks;
- governance votes;
- hacks and exploits;
- corporate treasury purchases;
- exchange listings and delistings.

## Enhanced Freshness Rules for Edge Cases

Some crypto questions require the freshest reliable data available. If current data are unavailable, the agent must reduce conclusion strength or mark the setup view as limited.

### ETH / L2 Value-Capture Debate

For questions about ETH fees, L2 migration, ETH value capture, or Ethereum thesis strength, use the freshest available data for L1 fees, burn, net issuance, blob fees, data availability demand, L2 activity, L2 sequencer economics where available, staking participation, validator economics, ETH/BTC, and ETH ETF flows where relevant.

If these data are stale or unavailable, the agent may discuss the framework but must not issue a strong current setup verdict.

### ETF Flow Reconciliation

For questions about ETF flows and price response, use fresh data for daily ETF net flows, cumulative flows, ETF AUM, BTC / ETH spot price, spot volume, futures open interest, funding, basis, liquidations, exchange reserves / flows where available, and macro-sensitive variables where material.

AUM change must not be treated as net flow unless adjusted for price movement.

### Derivatives / Leverage Fragility

For questions about rallies, selloffs, squeezes, liquidation risk, or fast-moving setup, use fresh data for funding, open interest, basis, liquidations, spot volume, futures volume, options skew where available, stablecoin liquidity, and major exchange events.

If derivatives data are unavailable, the agent must avoid strong claims about leverage-led or spot-led moves.

### Stablecoin Stress

For depeg, reserve, or stablecoin liquidity questions, use fresh data for peg price, depeg depth and duration, supply, redemptions where available, reserve / attestation updates, DEX pool balance, CEX liquidity, on-chain mint / burn, and regulatory or banking trigger.

### Hacks, Exploits, and Protocol Incidents

For hacks, exploits, outages, bridge failures, oracle failures, or governance emergencies, use current primary or near-primary evidence where possible:

- official protocol statement;
- post-mortem;
- explorer transactions;
- auditor / security firm note;
- exchange or bridge status page;
- governance forum;
- reputable incident tracker.

Price recovery is not evidence of risk resolution.

### Regulation

For regulatory edge cases, prioritize actual bill text, regulator release, court opinion, agency statement, ETF filing, enforcement document, and official exchange notice.

News summaries can support context, but the agent must separate:

```text
what changed
what remains uncertain
who benefits
who is pressured
what is not yet legally settled
```

### Tokenomics / Unlocks

For FDV, unlock, low-float, or dilution-sensitive analysis, use the freshest available data for circulating supply, total / max supply, FDV, unlock schedule, insider / VC / foundation allocations, emissions, treasury holdings, liquidity depth, and relevant governance changes.

If unlock data are unavailable and decision-critical, analysis should be Limited or Blocked.

### Corporate Crypto Treasuries

For corporate treasury impact, use fresh data for crypto holdings, recent purchases / sales, financing method, debt / convert / preferred / ATM issuance, maturity schedule where available, equity premium / discount to crypto holdings, stock price and capital-market access, and crypto price sensitivity.

Crypto Agent analyzes underlying crypto-market impact. Equity Agent analyzes the company and stock.

## Access-Aware Fallback Protocol

If preferred data are unavailable:

1. Use the best accessible source.
2. Label the fallback source.
3. Explain why it is weaker.
4. Reduce conclusion strength.
5. Block decision-grade analysis if the missing data are critical.

Required wording:

```text
Metric unavailable from preferred source.
Using fallback proxy: [source / metric].
Limitation: [why this is weaker].
Evidence quality: Limited.
Conclusion strength: Directional, not decision-grade.
```

## Metric Rules and Caveats

### ETF Flows

Use issuer data where available, fund filings, reliable ETF flow trackers, AUM changes with price-adjustment caveat, cumulative flows, issuer concentration, and daily flow persistence.

```text
AUM change is not the same as net flow unless adjusted for price movement.
```

### On-Chain Metrics

Use on-chain only when tied to a specific question. Common metrics include active addresses, transaction count, fees, exchange reserves, realized cap, MVRV, NUPL-style metrics, holder cohorts, stablecoin supply, bridge volume, staking participation, validator count, DEX volume, and DeFi TVL.

Required interpretation fields:

```text
Metric:
What it suggests:
Known distortions:
Confirmation needed:
Investment implication:
```

On-chain metrics cannot be standalone thesis evidence.

### DeFi TVL

TVL must be tested for incentive-driven deposits, mercenary liquidity, recursive leverage, token price effects, double-counting, bridge dependency, concentration, withdrawal risk, and sustainable fee generation.

TVL growth is not automatically adoption.

### Protocol Revenue / Fees

Separate gross user fees, supply-side revenue, protocol revenue, treasury revenue, tokenholder value accrual, emissions, incentives, and net sustainability.

```text
Fees != revenue != tokenholder value.
```

### Tokenomics

Required fields where relevant: circulating supply, total supply, max supply, market cap, FDV, unlock schedule, emissions, insider allocation, team / VC / foundation allocation, treasury holdings, staking dilution, token utility, and value-capture mechanism.

Missing tokenomics data can block decision-grade analysis.

### Derivatives

Use funding, open interest, basis, futures curve, liquidations, options implied volatility, options skew, put/call data where available, and CME vs offshore venue split where relevant.

```text
Derivatives data can show market fragility or crowding, but it does not create a standalone investment thesis.
```

### Stablecoins

Assess total supply, USDT / USDC / DAI / synthetic stablecoin share, supply growth or contraction, exchange balances, mint / burn activity, depeg risk, reserve / attestation quality, regulatory risk, and chain-specific stablecoin settlement.

Do not state that any stablecoin is safe for cash storage.

### Tokenization / RWA

Assess actual assets tokenized, AUM, settlement volume, chain / venue, issuer, custodian, regulatory structure, user base, and whether value accrues to the token.

Core question:

```text
Does tokenization create durable economic value for this crypto asset?
```

### Corporate Crypto Treasuries

Assess entity, crypto held, purchases / sales, funding mechanism, debt / convert / equity issuance, ATM programs, reflexive loop, forced-seller risk, and materiality versus supply and ETF flows.

Crypto Agent analyzes market impact. Equity Agent analyzes the stock.

### Regulation

Use official and primary sources first: legislation text, regulator releases, enforcement actions, court opinions, official agency statements, ETF filings, and exchange notices.

Professional reporting may summarize events, but investment-impact conclusions must distinguish what changed, what remains uncertain, what assets are affected, and what business models are affected.

No legal advice.

### Sentiment / Narrative

Permitted as supporting setup evidence: Fear & Greed Index, search interest, social narrative heat, media attention, retail attention proxies, and narrative cycles.

```text
Sentiment can explain market behavior, but cannot justify investment quality.
```

### Cycle Metrics

Use as context, not forecast: halving cycle, drawdown history, realized cap, MVRV, BTC dominance, ETH/BTC cycles, prior leverage flushes, and prior regulatory shock analogies.

Required fields:

```text
What resembles prior cycles:
What is structurally different now:
Why the analogy may fail:
Current confirmation:
Current contradiction:
```

## Data Quality Labels

```text
Strong
Adequate
Limited
Weak
Unavailable
```

## Conclusion Strength Labels

```text
Decision-useful
Directional
Hypothesis only
Not supportable
```

## Freshness-Based Verdict Constraint

If the question is current setup-sensitive and fresh data are missing, the agent must not issue a supportive / unfavorable setup verdict or strong claim about flows, leverage, ETF impact, stablecoin stress, or regulatory impact.

Use:

```text
Setup quality: Limited / Inconclusive due to stale or incomplete current data.
```

## Blocking Conditions

Block or limit analysis when identity cannot be verified, liquidity is unreliable, tokenomics are unavailable, reserve / custody data are missing for stablecoins or wrapped assets, value capture cannot be tested, data are mostly social commentary, evidence conflicts cannot be resolved, or the user requests operational crypto advice rather than investment analysis.
