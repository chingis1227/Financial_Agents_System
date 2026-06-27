# Macro Indicator Cadence, Source, and Priority Registry

## Purpose

This registry defines the Macro Agent's source hierarchy, cadence rules, freshness expectations, indicator priority tiers, and dynamic escalation rules.

It exists to prevent two common failures:

1. daily fake-refresh of slow official data; and
2. stale market data in current macro conclusions.

## Source-Purpose Labels

Every material source should be labeled:

```text
official_release
market_pricing
survey
nowcast
institutional_research
news_context
proxy
```

## Source Hierarchy

### Tier A — Primary / Official

- central banks: Fed, ECB, BoJ, BoE where relevant;
- statistical agencies: BLS, BEA, Census, Eurostat, national statistical agencies, Japan Statistics Bureau;
- treasuries / finance ministries: U.S. Treasury, Japan MOF, national debt offices;
- regulators and official financial stability reports;
- official exchange / market data where available;
- official IMF, BIS, OECD, World Bank datasets and reports.

### Tier B — Market Data / Professional Data

- market data providers;
- exchange prices;
- futures, OIS, swaps, options-implied data;
- credit spread datasets;
- volatility indexes;
- central bank data portals and FRED where it republishes official data.

### Tier C — Institutional Research / Practitioner Interpretation

- recognized asset managers and macro research providers;
- bank strategy research if source is known and methodology is clear;
- professional macro notes from PIMCO, BlackRock, Bridgewater, AQR, Wellington, Capital Group, and similar sources.

Institutional research can inform interpretation but should not replace official data for factual claims.

### Tier D — News Context

Use reputable news for:

- event reporting;
- policy remarks;
- market reaction context;
- geopolitical / supply shock flags.

News alone should not support regime conclusions unless it reports an official action or directly observable market event.

### Tier E — Proxy

Proxy evidence must be labeled and claim strength limited.

## Freshness Rules

### Fresh Market Data Required

For current, market-sensitive analysis, refresh:

```text
Treasury yields
real yields
yield curve
DXY
EUR/USD
USD/JPY
oil
gold
copper
VIX / MOVE
credit spreads
equity indexes
market-implied policy path
```

### Carry-Forward Allowed with Timestamp

Slow official releases may be carried forward until the next scheduled release:

```text
CPI / PCE / PPI
NFP / unemployment / JOLTS / wages
ISM / PMI
GDP / national accounts
Tankan
SLOOS
ECB / BoJ / Fed projections
financial stability reports
structural data
```

Required fields:

```text
latest_release_used
data_as_of
next_known_release, if known
revision_risk
```

## Indicator Priority Tiers

### Tier 1 — Regime-Defining / High Market Impact

Indicators that can materially affect macro regime, policy expectations, rates, FX, credit, or broad risk appetite.

Examples:

```text
CPI / core CPI
PCE / core PCE
NFP / unemployment / wages
initial and continuing jobless claims when turning
FOMC decisions / SEP / press conference
Fed funds / OIS / futures-implied policy path
2Y / 10Y / 30Y Treasury yields
real yields
2s10s / 3m10y curve
ISM / PMI when near turning points
oil shock when inflation or real income transmission is material
HY / IG credit spreads when moving materially
DXY / EUR/USD / USD/JPY when policy divergence or FX stress is material
ECB / BoJ decisions when relevant
```

### Tier 2 — Confirmation / Transmission Indicators

Indicators that confirm or challenge the Tier 1 signal and explain transmission.

Examples:

```text
retail sales / control group
real PCE
real disposable income
industrial production
housing starts / permits
mortgage rates
JOLTS quits / openings
inflation expectations / breakevens
PPI / import prices
Treasury auctions / refunding
TGA / RRP / reserves
SLOOS / bank lending
credit issuance / refinancing conditions
VIX / MOVE
sector leadership / breadth
Bund yields / BTP-Bund spread
JGB yields / Tankan
Euro area wages / services inflation
```

### Tier 3 — Early Warning / Context / Tail-Risk Indicators

Indicators that matter as early warnings or context but should not alone drive regime verdicts.

Examples:

```text
mortgage delinquencies
auto loan delinquencies
credit card delinquencies
consumer confidence
regional Fed surveys
CEO confidence
small business surveys
inventory ratios
shipping / freight indicators
commodity ratios such as copper/gold
crypto leverage / funding stress
single-country Europe data outside core countries unless asset-specific
single-company or anecdotal survey evidence
```

## Dynamic Escalation Rules

Each indicator has a default tier, but current weight can rise or fall.

Escalation factors:

```text
freshness
surprise_vs_consensus
market_reaction
cross_block_confirmation
transmission_strength
revision_risk
early_warning_status
current_regime_relevance
source_quality
```

### Escalate Tier 3 to Tier 2 when:

- it confirms a deterioration already visible in Tier 1 or Tier 2 indicators;
- it has a clear transmission channel;
- it is moving persistently, not one noisy observation;
- it appears across related indicators or segments;
- market pricing begins reacting.

Example:

```text
Mortgage delinquencies rising alone = Tier 3 early warning.
Mortgage delinquencies + tighter lending standards + falling real income + rising unemployment = Tier 2 credit / consumer confirmation.
```

### Escalate Tier 2 to Tier 1 when:

- it becomes the dominant transmission channel;
- it triggers policy repricing;
- it causes broad market reaction;
- it directly affects the asset or thesis under review.

Example:

```text
Treasury auctions are normally confirmation / rates supply evidence.
Repeated weak auctions + rising term premium + MOVE spike + long-end disorder can become Tier 1 fiscal / term-premium regime evidence.
```

### De-escalate when:

- data are stale;
- the indicator is not material to the current regime or asset;
- it is contradicted by stronger evidence;
- it lacks transmission;
- it is a one-off noisy move.

## Block-Level Registry

### Growth & Labor

| Indicator | Default Tier | Cadence | Freshness | Primary Source Type | Notes |
|---|---:|---|---|---|---|
| Nonfarm payrolls | 1 | Monthly | Latest official release | official_release | Check revisions and breadth |
| Unemployment rate | 1 | Monthly | Latest official release | official_release | Use Sahm-style change as recession flag, not sole verdict |
| Average hourly earnings | 1/2 | Monthly | Latest official release | official_release | Wage-inflation transmission |
| Initial jobless claims | 1/2 | Weekly | Latest weekly release | official_release | Escalates when trend breaks |
| Continuing claims | 2 | Weekly | Latest weekly release | official_release | Labor deterioration confirmation |
| Real personal income less transfers | 1 | Monthly | Latest official release | official_release | NBER-relevant activity measure |
| Real PCE | 1/2 | Monthly | Latest official release | official_release | Consumer demand confirmation |
| Retail sales control group | 2 | Monthly | Latest official release | official_release | Consumer / GDP tracking |
| ISM / PMI employment and new orders | 2 | Monthly | Latest release | survey | Leading / diffusion signal |
| Housing starts / permits | 2/3 | Monthly | Latest release | official_release | Rate-sensitive leading channel |
| Mortgage delinquencies | 3 | Monthly / quarterly | Latest available | official / institutional | Early warning, escalate only with confirmation |

### Inflation & Commodities

| Indicator | Default Tier | Cadence | Freshness | Primary Source Type | Notes |
|---|---:|---|---|---|---|
| CPI / core CPI | 1 | Monthly | Latest official release | official_release | Surprise vs consensus critical |
| PCE / core PCE | 1 | Monthly | Latest official release | official_release | Fed-preferred inflation measure |
| 3m / 6m annualized core inflation | 1/2 | Monthly | Latest calculated from official data | official_release | Momentum, but revision-aware |
| PPI | 2 | Monthly | Latest release | official_release | Pipeline pressure |
| Import prices | 2 | Monthly | Latest release | official_release | FX / imported inflation |
| Breakevens | 1/2 | Market | Fresh | market_pricing | Market inflation pricing |
| Inflation expectations surveys | 2 | Monthly | Latest release | survey | Household / market expectations |
| Oil / gasoline / diesel | 1/2 | Market | Fresh | market_pricing | Escalates in supply shocks |
| Natural gas / European gas | 2/3 | Market | Fresh when relevant | market_pricing | Europe energy sensitivity |
| Copper / industrial metals | 2/3 | Market | Fresh when relevant | market_pricing | Growth / China proxy, not stand-alone verdict |
| Inventories | 2 | Weekly / monthly | Latest release | official_release | Commodity confirmation |

### Rates, Fed & Yield Curve

| Indicator | Default Tier | Cadence | Freshness | Primary Source Type | Notes |
|---|---:|---|---|---|---|
| FOMC decision / statement | 1 | Event | Latest event | official_release | Official policy evidence |
| Fed Chair press conference | 1 | Event | Latest event | official_release | Reaction function evidence |
| SEP / dot plot | 1 | Quarterly | Latest release | official_release | Policy path signal, not promise |
| Fed minutes / speeches | 1/2 | Event | Latest material communication | official_release | Context, not always regime-defining |
| FedWatch / OIS / futures | 1 | Market | Fresh | market_pricing | Market pricing, not Fed intent |
| 2Y yield | 1 | Market | Fresh | market_pricing | Policy path sensitivity |
| 10Y yield | 1 | Market | Fresh | market_pricing | Discount rate / term premium |
| 30Y yield | 1/2 | Market | Fresh | market_pricing | Fiscal / duration pressure |
| Real yields | 1 | Market | Fresh | market_pricing | Valuation / gold / duration channel |
| Yield curve 2s10s / 3m10y | 1/2 | Market | Fresh | market_pricing | Recession / policy signal, not sole proof |
| Treasury auctions / refunding | 2 | Event | Latest event | official / market | Escalates with repeated stress |
| MOVE index | 2 | Market | Fresh | market_pricing | Rates volatility confirmation |

### Liquidity & Credit

| Indicator | Default Tier | Cadence | Freshness | Primary Source Type | Notes |
|---|---:|---|---|---|---|
| Fed balance sheet | 2 | Weekly | Latest release | official_release | Liquidity context |
| Bank reserves | 2 | Weekly | Latest release | official_release | Funding system context |
| TGA | 2 | Daily / weekly | Latest available | official_release | Liquidity drain / add |
| ON RRP | 2 | Daily | Latest available | official_release | Money market plumbing |
| Net liquidity proxy | 2 | Derived | Latest components | proxy | Label as proxy |
| SOFR / EFFR / IORB spreads | 2 | Daily | Fresh when funding stress relevant | official / market | Plumbing stress |
| IG / HY spreads | 1/2 | Market | Fresh | market_pricing | Escalates with material widening |
| Distressed debt ratio | 2/3 | Periodic | Latest available | market / institutional | Credit stress confirmation |
| SLOOS | 1/2 | Quarterly | Latest release | official_release | Lending standards, important but lagged |
| Bank lending | 2 | Weekly / monthly | Latest release | official_release | Credit transmission |
| Consumer delinquencies | 3 | Monthly / quarterly | Latest available | official / institutional | Early warning |
| Credit-to-GDP gap | 3 | Quarterly | Latest available | BIS | Structural early warning |

### Cross-Asset Macro Confirmation

| Indicator | Default Tier | Cadence | Freshness | Primary Source Type | Notes |
|---|---:|---|---|---|---|
| S&P 500 / Nasdaq / Russell / equal-weight | 2 | Market | Fresh | market_pricing | Risk appetite / breadth context |
| Sector leadership | 2/3 | Market | Fresh when relevant | market_pricing | Cyclical vs defensive confirmation |
| Market breadth | 2 | Market | Fresh when relevant | market_pricing | Risk appetite quality |
| VIX | 1/2 | Market | Fresh | market_pricing | Equity vol stress |
| MOVE | 1/2 | Market | Fresh | market_pricing | Rates vol stress |
| Credit spreads | 1/2 | Market | Fresh | market_pricing | Cross-asset confirmation |
| Gold / copper / oil | 2 | Market | Fresh | market_pricing | Macro confirmation only with transmission |
| BTC / crypto | 3 | Market | Fresh when relevant | market_pricing | Liquidity beta / leverage proxy, label carefully |

### G3 FX & Regional Policy

| Indicator | Default Tier | Cadence | Freshness | Primary Source Type | Notes |
|---|---:|---|---|---|---|
| DXY | 1/2 | Market | Fresh | market_pricing | Global dollar conditions |
| EUR/USD | 1/2 | Market | Fresh | market_pricing | Fed-ECB divergence / Europe FX |
| USD/JPY | 1/2 | Market | Fresh | market_pricing | Fed-BoJ divergence / carry / intervention |
| ECB decision / deposit rate | 1 | Event | Latest event | official_release | Official policy stance |
| ECB projections | 1/2 | Quarterly | Latest release | official_release | Growth / inflation / wages / trade |
| Euro area HICP / core / services | 1 | Monthly | Latest official release | official_release | ECB reaction function |
| Euro area wages | 1/2 | Quarterly / periodic | Latest release | official_release | Services inflation persistence |
| Euro area PMI | 2 | Monthly | Latest release | survey | Growth momentum |
| Germany PMI / Ifo / manufacturing | 2 | Monthly | Latest release | survey / official | Manufacturing / export node |
| Bund yields / BTP-Bund spread | 2 | Market | Fresh when relevant | market_pricing | Sovereign / rates channel |
| BoJ decision / policy rate | 1 | Event | Latest event | official_release | Policy normalization |
| JGB yields | 1/2 | Market | Fresh | market_pricing | Japan rates / carry channel |
| BoJ Outlook | 1/2 | Quarterly | Latest release | official_release | Inflation / wages / growth view |
| Japan CPI / wages / real wages | 1/2 | Monthly | Latest release | official_release | Wage-price cycle |
| Tankan | 2 | Quarterly | Latest release | official_release | Business conditions |
| MOF intervention operations / language | 1/2 | Event / monthly | Latest official / credible report | official / news_context | Intervention risk |

## Anti-Hallucination Rules

- Do not invent latest values.
- Do not cite stale values as current.
- Do not infer central bank intent from market pricing alone.
- Do not treat a single early warning indicator as a crisis call.
- Do not use proxy data without labeling it.
- Do not make investment conclusions from macro data alone.
- If critical fresh data are unavailable, output Limited or Blocked.

## Professional Methodology Anchors

This registry reflects:

- NBER's multi-indicator cycle dating logic;
- Conference Board leading / coincident / lagging indicator structure;
- OECD CLI turning-point discipline;
- BIS early warning indicators for financial stress;
- Fed financial stability vulnerability categories;
- IMF financial soundness indicator logic.
