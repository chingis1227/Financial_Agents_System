# Automation Lab Data Provider & Parsing Layer

This layer is data/evidence infrastructure for Automation Lab. It does not define investment rules, route decisions, agent behavior, or IC actions. Canonical source authority remains in the Financial Agent System implementation documents, especially `implementation/04-evidence-layer.md`.

## ProviderResult contract

Every provider returns the unified `ProviderResult` shape from `data_providers/base.py`, including provider identity, source tier, status, access, freshness, source date, raw/normalized paths, normalized data, claims, limitations, errors, and metadata.

Allowed source tiers: `Tier 1`, `Tier 2`, `Tier 3`, `Tier 4`, `Pointer-Only`.

Allowed statuses: `ok`, `partial`, `missing`, `error`, `disabled`.

## Providers

- `sec_provider`: SEC submissions, companyfacts, latest 10-K/10-Q/8-K/20-F/6-K/40-F.
- `fred_provider`: FRED official macro series; requires `FRED_API_KEY`, otherwise returns `disabled`.
- `treasury_provider`: official U.S. Treasury/Fiscal Data no-key path.
- `cftc_cot_provider`: official CFTC COT files and grain positioning parser.
- `usda_nass_provider`: USDA NASS QuickStats; requires `USDA_NASS_API_KEY`, otherwise returns `disabled`.
- `usda_wasde_provider`: USDA WASDE source wrapper and grain balance parser.
- `usda_psd_provider`: documented graceful-degradation stub.
- `etf_issuer_provider`: issuer fund pages/holdings, with TLT/iShares as first configured target.
- `public_price_provider`: Stooq first where suitable, Yahoo chart fallback.
- `search_discovery_provider`: Pointer-Only discovery; cannot support material claims.
- `eodhd_provider`: optional Tier 2 stub requiring `EODHD_API_KEY`.

## Parsers

`data_parsers/` contains lightweight parsers for CSV, HTML tables, PDF text/table wrappers, issuer ETF holdings, SEC filings/companyfacts, USDA WASDE, CFTC COT, and numeric normalization.

## Cache behavior

When persistence is enabled, provider runs write:

```text
automation_lab/data_runs/[timestamp]-[subject]/
  raw/
  normalized/
  provider_results.json
  source_inventory.json
  evidence_inputs.json
```

Generated runs stay local/ignored unless intentionally promoted as fixtures. Cache keys include provider id, query parameters, and source URL.

## Integration

- AGENT equity preflight attaches `data_provider_registry`, `data_provider_plan`, and `data_provider_results`.
- Non-equity AGENT preflight routes TLT/fixed income through ETF issuer + Treasury/FRED + public price attempts and commodity/grain routes through CFTC + USDA + public price/ETF issuer attempts.
- QUICK snapshots expose the provider registry/plan without claiming Evidence Collector evidence packs.
- Evidence Pack imports provider-derived claim rows while preserving legacy source-record support.

## Optional API keys

Set these only when you want live provider access:

```powershell
$env:FRED_API_KEY="..."
$env:USDA_NASS_API_KEY="..."
$env:PERPLEXITY_API_KEY="..."
$env:EODHD_API_KEY="..."
```

Missing keys must not crash workflows; providers return `disabled`/`partial` with explicit limitations.

## Tests

From `automation_lab/`:

```powershell
..\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py"
```

Provider-specific coverage lives in `tests/test_data_provider_layer.py`.
