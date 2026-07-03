# Equity Data Sources Draft

Status: Draft for TASK-003
Scope: Automation Lab only; not canonical Financial Agent System policy.

## Source: SEC EDGAR APIs

- What it provides: Company submissions, filing metadata, and extracted XBRL company facts from public filings such as 10-K, 10-Q, and 8-K.
- Freshness: Filing-driven; updates depend on issuer submissions and SEC processing.
- Free/paid: Free public source.
- Automatable: Yes, via SEC EDGAR APIs.
- Fallback if unavailable: SEC company filing pages or issuer investor-relations filings.
- Notes: Useful official source for fundamentals and filing evidence, not real-time prices.
- Reference: https://www.sec.gov/search-filings/edgar-application-programming-interfaces

## Source: Alpha Vantage

- What it provides: Real-time and historical stock market data, ETFs, mutual funds, indices, economic indicators, FX, crypto, commodities, fundamentals, and technical indicators.
- Freshness: Market-data dependent; real-time or delayed access may depend on endpoint and plan.
- Free/paid: Free tier plus paid plans; API key required.
- Automatable: Yes, via documented JSON/CSV APIs.
- Fallback if unavailable: Nasdaq Data Link, Financial Modeling Prep, issuer filings for fundamentals, exchange/issuer pages for reference data.
- Notes: Useful for prototype price/fundamental retrieval, but production use needs license/rate-limit review.
- Reference: https://www.alphavantage.co/documentation/

## Source: Nasdaq Data Link

- What it provides: APIs, Python SDK, and Excel add-ins for market and alternative datasets; available datasets vary by publisher and license.
- Freshness: Dataset-specific; can range from real-time market feeds to delayed or periodic datasets.
- Free/paid: Mixed free and paid datasets.
- Automatable: Yes, via REST API and SDKs.
- Fallback if unavailable: SEC for filings/fundamentals; Alpha Vantage or FMP for prototype price/fundamental coverage.
- Notes: Treat each dataset separately for licensing, redistribution, and freshness.
- Reference: https://docs.data.nasdaq.com/

## Source: Financial Modeling Prep

- What it provides: Stock quotes, historical prices, financial statements, as-reported filing data, company reference data, and other financial endpoints.
- Freshness: Endpoint and plan dependent.
- Free/paid: Free and paid plans; API key required; licensing must be reviewed before display or redistribution.
- Automatable: Yes, via REST API.
- Fallback if unavailable: SEC EDGAR for filings; Alpha Vantage or Nasdaq Data Link for market data prototypes.
- Notes: Useful as a convenience layer, but primary-source checks remain important for filings.
- Reference: https://site.financialmodelingprep.com/developer/docs

