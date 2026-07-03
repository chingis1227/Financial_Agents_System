# ETF Data Sources Draft

Status: Draft for TASK-003
Scope: Automation Lab only; not canonical Financial Agent System policy.

## Source: Issuer ETF pages

- What it provides: Fund objective, fees, holdings, sector/country exposures, distributions, documents, performance, and risk disclosures.
- Freshness: Issuer-specific; holdings are often daily or periodic, documents and distributions update on issuer schedules.
- Free/paid: Free public pages, but automation rights and robots/terms must be checked per issuer.
- Automatable: Partial; pages, CSV downloads, and PDFs vary by issuer and format stability.
- Fallback if unavailable: Fund prospectus/annual report via SEC EDGAR, ETF.com-style databases, or market-data vendors.
- Notes: Best first source for fund-specific facts; automation should store retrieval timestamp and issuer URL.

## Source: SEC EDGAR APIs

- What it provides: ETF and fund filings, prospectuses, shareholder reports, and filing metadata where available.
- Freshness: Filing-driven; not a complete daily holdings feed.
- Free/paid: Free public source.
- Automatable: Yes, via SEC EDGAR APIs.
- Fallback if unavailable: Issuer website documents and fund pages.
- Notes: Useful official-source support for legal documents, fees, risks, and formal disclosures.
- Reference: https://www.sec.gov/search-filings/edgar-application-programming-interfaces

## Source: Alpha Vantage

- What it provides: ETF/fund and market data coverage, including price histories and related financial market data.
- Freshness: Endpoint and plan dependent.
- Free/paid: Free tier plus paid plans; API key required.
- Automatable: Yes, via documented APIs.
- Fallback if unavailable: Nasdaq Data Link, FMP, issuer pages, or exchange data.
- Notes: Useful for prototype ETF price/return checks; holdings/expense facts should be reconciled to issuer documents.
- Reference: https://www.alphavantage.co/documentation/

## Source: Nasdaq Data Link

- What it provides: Market, fund, and reference datasets depending on publisher and subscription.
- Freshness: Dataset-specific.
- Free/paid: Mixed free and paid datasets.
- Automatable: Yes, via API and SDKs.
- Fallback if unavailable: Issuer pages, SEC filings, or other market-data vendors.
- Notes: Review each dataset license and update cadence before use.
- Reference: https://docs.data.nasdaq.com/

