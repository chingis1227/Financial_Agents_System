# Macro Data Sources Draft

Status: Draft for TASK-003
Scope: Automation Lab only; not canonical Financial Agent System policy.

## Source: FRED API

- What it provides: Broad economic and financial time series from FRED and ALFRED, including rates, inflation, labor, GDP-related series, credit, money, and market indicators.
- Freshness: Series-specific; follows original source release calendars and revisions.
- Free/paid: Free; API key required for web service requests.
- Automatable: Yes, via API.
- Fallback if unavailable: Original agency sources such as BLS, BEA, Treasury, Federal Reserve, and Census.
- Notes: Useful normalized macro time-series layer for prototypes; store series IDs and vintage/retrieval timestamp where possible.
- Reference: https://fred.stlouisfed.org/docs/api/fred/

## Source: Bureau of Labor Statistics Public Data API

- What it provides: Labor, employment, unemployment, wages, CPI/PPI, productivity, and other BLS time series.
- Freshness: Release-calendar driven; series update on BLS schedules.
- Free/paid: Free public API; registration is not required for public use, with higher limits available via registration.
- Automatable: Yes, via GET/POST API signatures.
- Fallback if unavailable: BLS release pages, downloadable tables, or FRED copies of BLS series.
- Notes: Useful original source for BLS series and release-specific details.
- Reference: https://www.bls.gov/bls/api_features.htm

## Source: Bureau of Economic Analysis API

- What it provides: BEA economic statistics and metadata, including national accounts and related datasets.
- Freshness: Release-calendar driven; subject to revisions.
- Free/paid: Free API key required.
- Automatable: Yes, via API.
- Fallback if unavailable: BEA release pages/downloads or FRED copies of selected BEA series.
- Notes: Useful original source for GDP/NIPA-related data.
- Reference: https://apps.bea.gov/api/signup/

## Source: U.S. Treasury Fiscal Data API

- What it provides: Federal fiscal datasets, Treasury rates/debt, statements, and related fiscal data.
- Freshness: Dataset-specific.
- Free/paid: Free public source.
- Automatable: Yes, via API.
- Fallback if unavailable: TreasuryDirect, FRED, or downloadable Treasury tables.
- Notes: Useful for rates/fiscal context and public-debt metrics.
- Reference: https://fiscaldata.treasury.gov/api-documentation/


