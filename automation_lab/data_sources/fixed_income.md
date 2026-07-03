# Fixed Income Data Sources Draft

Status: Draft for TASK-003
Scope: Automation Lab only; not canonical Financial Agent System policy.

## Source: U.S. Treasury Fiscal Data API

- What it provides: Treasury datasets, including debt, interest rates, fiscal statements, and related federal finance data.
- Freshness: Dataset-specific; many series are daily, monthly, or release-calendar driven.
- Free/paid: Free public source.
- Automatable: Yes, via documented API endpoints with filters and pagination.
- Fallback if unavailable: TreasuryDirect pages, Federal Reserve/FRED series, or downloaded CSV files.
- Notes: Strong primary public source for Treasury-related data.
- Reference: https://fiscaldata.treasury.gov/api-documentation/

## Source: FRED API

- What it provides: Economic and financial time series from FRED and ALFRED, including interest rates, spreads, Treasury yields, inflation, and macro indicators.
- Freshness: Series-specific; follows source release schedules.
- Free/paid: Free; API key required for web service requests.
- Automatable: Yes, via API.
- Fallback if unavailable: Original agency releases such as Treasury, Federal Reserve, BLS, or BEA.
- Notes: Excellent normalized time-series layer; always preserve source series IDs and timestamps.
- Reference: https://fred.stlouisfed.org/docs/api/fred/

## Source: SEC EDGAR APIs

- What it provides: Bond ETF/fund filings, issuer disclosures, and public-company debt disclosures where available in filings.
- Freshness: Filing-driven.
- Free/paid: Free public source.
- Automatable: Yes, via SEC EDGAR APIs.
- Fallback if unavailable: Issuer investor-relations pages, fund pages, or official offering documents.
- Notes: Useful for disclosure evidence, not a comprehensive bond pricing source.
- Reference: https://www.sec.gov/search-filings/edgar-application-programming-interfaces

## Source: Market-data vendors for bond ETFs and credit proxies

- What it provides: ETF prices, fixed-income ETF reference data, credit spreads, and benchmark proxies depending on vendor.
- Freshness: Vendor and plan dependent.
- Free/paid: Usually mixed or paid for reliable production coverage.
- Automatable: Partial/yes depending on vendor API.
- Fallback if unavailable: FRED/Treasury for rates and spreads; issuer pages for fund facts; exchange pages for ETF quotes.
- Notes: Direct bond pricing and TRACE-like coverage may require specialized licensing beyond TASK-003.


