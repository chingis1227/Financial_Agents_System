# Crypto Data Sources Draft

Status: Draft for TASK-003
Scope: Automation Lab only; not canonical Financial Agent System policy.

## Source: CoinGecko API

- What it provides: Crypto market prices, market capitalization, volume, coin metadata, tickers across exchanges, historical market data, categories, and on-chain DEX data through GeckoTerminal coverage.
- Freshness: Market-data dependent; real-time or near-real-time capabilities vary by endpoint and plan.
- Free/paid: Free/demo and paid API plans.
- Automatable: Yes, via REST endpoints; WebSocket and webhook capabilities are plan/product dependent.
- Fallback if unavailable: CoinMarketCap API, exchange APIs, or issuer/project pages for metadata.
- Notes: Good broad aggregator for first-pass crypto coverage; validate exchange composition and stablecoin/bridged-asset identifiers.
- Reference: https://docs.coingecko.com/

## Source: Binance market data APIs

- What it provides: Exchange-specific spot and derivatives market data, tickers, order books, trades, and candles for Binance-listed pairs.
- Freshness: Real-time or near-real-time exchange data depending on endpoint.
- Free/paid: Public market endpoints generally available; usage limits apply.
- Automatable: Yes, via API/websocket endpoints where available.
- Fallback if unavailable: CoinGecko/CoinMarketCap aggregators or other major exchange APIs.
- Notes: Exchange-specific data should not be treated as full-market coverage; useful for liquidity and price checks on listed pairs.
- Reference: https://developers.binance.com/docs

## Source: CoinMarketCap API

- What it provides: Crypto listings, quotes, metadata, market metrics, and historical datasets depending on plan.
- Freshness: Endpoint and plan dependent.
- Free/paid: Free/basic and paid plans; API key required.
- Automatable: Yes, via REST API.
- Fallback if unavailable: CoinGecko API, exchange APIs, or project/chain explorers for metadata.
- Notes: Useful alternative aggregator; licensing and plan limits need review before automation at scale.
- Reference: https://coinmarketcap.com/api/documentation/v1/


