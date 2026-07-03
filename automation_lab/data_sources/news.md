# News Data Sources Draft

Status: Draft for TASK-003
Scope: Automation Lab only; not canonical Financial Agent System policy.

## Source: SEC EDGAR company submissions

- What it provides: Filing-driven corporate events and disclosures, including 8-Ks, 10-Qs, 10-Ks, proxy statements, and other public filings.
- Freshness: Filing-driven; near-current for public filings after SEC processing.
- Free/paid: Free public source.
- Automatable: Yes, via SEC EDGAR APIs.
- Fallback if unavailable: Issuer investor-relations pages and SEC filing search pages.
- Notes: Useful official source for issuer disclosures; not a general news feed.
- Reference: https://www.sec.gov/search-filings/edgar-application-programming-interfaces

## Source: Issuer investor-relations newsrooms

- What it provides: Company press releases, earnings releases, event announcements, presentations, and webcasts.
- Freshness: Issuer-specific and event-driven.
- Free/paid: Free public pages, but automation terms vary by issuer/site vendor.
- Automatable: Partial; RSS feeds, structured pages, and PDFs vary by issuer.
- Fallback if unavailable: SEC 8-K filings, press-release wires, or archived issuer pages.
- Notes: Best for company-specific narrative and management materials; needs timestamp and URL capture.

## Source: Government and central-bank release pages/APIs

- What it provides: Policy statements, data releases, calendars, speeches, minutes, and official macro/regulatory announcements.
- Freshness: Release-calendar or event-driven.
- Free/paid: Free public sources.
- Automatable: Partial/yes depending on agency API, RSS, or page structure.
- Fallback if unavailable: FRED/BLS/BEA/Treasury/EIA pages and archived releases.
- Notes: Useful before secondary media for policy and macro facts.

## Source: Commercial market news APIs

- What it provides: Aggregated market news, headlines, metadata, and sometimes article text/summaries depending on vendor rights.
- Freshness: Real-time or near-real-time depending on vendor and plan.
- Free/paid: Usually paid for reliable market coverage and redistribution rights.
- Automatable: Yes if licensed API access exists.
- Fallback if unavailable: Primary filings/releases and public source pages; avoid unsupported paywalled scraping.
- Notes: Licensing, redistribution, and copyright constraints must be reviewed before storing or displaying article content.

