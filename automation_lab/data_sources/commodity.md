# Commodity Data Sources Draft

Status: Draft for TASK-003
Scope: Automation Lab only; not canonical Financial Agent System policy.

## Source: U.S. Energy Information Administration API

- What it provides: Energy data including oil, natural gas, electricity, petroleum inventories, production, consumption, and related time series.
- Freshness: Series-specific; many datasets follow weekly, monthly, or annual release schedules.
- Free/paid: Free API; registration/API key required.
- Automatable: Yes, via EIA API.
- Fallback if unavailable: EIA downloadable tables, FRED energy series, or official release pages.
- Notes: Official public source for U.S. energy fundamentals.
- Reference: https://www.eia.gov/opendata/documentation.php

## Source: CFTC Commitments of Traders reports

- What it provides: Futures and options positioning by trader categories for reportable markets, including many commodity contracts.
- Freshness: Weekly; reports describe Tuesday open interest and are published on a schedule.
- Free/paid: Free public source.
- Automatable: Yes/partial via CFTC public reporting environment and downloadable datasets.
- Fallback if unavailable: CFTC static report downloads or vendor mirrors with caution.
- Notes: Useful for positioning context, not spot price or fundamental supply/demand data.
- Reference: https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm

## Source: Alpha Vantage commodity APIs

- What it provides: Commodity market data among broader financial data APIs.
- Freshness: Endpoint and plan dependent.
- Free/paid: Free tier plus paid plans; API key required.
- Automatable: Yes, via API.
- Fallback if unavailable: EIA for energy fundamentals, FRED for macro commodity series, exchange/issuer pages for instruments.
- Notes: Useful for prototype price checks; production use requires licensing/rate-limit review.
- Reference: https://www.alphavantage.co/documentation/

## Source: FRED API

- What it provides: Commodity-related economic time series and price proxies where available.
- Freshness: Series-specific.
- Free/paid: Free; API key required for web service requests.
- Automatable: Yes, via API.
- Fallback if unavailable: Original agency/exchange/provider pages.
- Notes: Good normalized history for macro commodity context; not a full futures market feed.
- Reference: https://fred.stlouisfed.org/docs/api/fred/


