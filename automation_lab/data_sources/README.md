# Data Sources Draft

Status: TASK-003 draft
Scope: Automation Lab only
Last updated: 2026-07-01

## Purpose

This folder contains a first-pass map of automatable data sources for future Financial Agent Automation Lab workflows.

The map is intentionally practical and non-canonical: it helps the lab identify likely sources, freshness expectations, access constraints, and fallbacks before any source is wired into automated workflows.

## Authority boundary

Financial Agent System remains the source of truth for investment rules, evidence standards, source display, routing, agents, skills, validators, and IC gates.

These files do not redefine source authority or evidence policy for Financial Agent System.

## Files

- `equity.md` — equities, company fundamentals, filings, prices, ETF overlap where relevant.
- `crypto.md` — crypto spot markets, reference data, exchange/on-chain coverage.
- `etf.md` — ETF profiles, holdings, prices, issuer pages, filings.
- `fixed_income.md` — rates, Treasury data, bond ETF market proxies, credit/fund data.
- `commodity.md` — commodity prices, energy inventories, futures positioning, gold/oil references.
- `macro.md` — macroeconomic series, national accounts, labor, inflation, rates.
- `news.md` — issuer news, regulatory releases, central bank/government releases, market news.

## Common fields

Each asset-class file uses the same headings:

- Source
- What it provides
- Freshness
- Free/paid
- Automatable
- Fallback if unavailable
- Notes

## TASK-003 exclusions

- No authority ranking.
- No canonical source policy.
- No source-quality scoring.
- No credentials, secrets, or paid-account assumptions.
- No changes to the main Financial Agent System repository.

