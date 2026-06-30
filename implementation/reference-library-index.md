# Reference Library Index

Status: Supporting operational index
Owner: Documentation Control
Last reviewed: 2026-06-29
Session 07 relocation verified: 2026-06-29

## Purpose

This index maps supporting references to their owners, allowed usage, freshness treatment, split/index state, and review notes. It is a navigation and QA aid only. The documentation registry in `implementation/01-documentation-control.md` remains the status authority, and canonical implementation documents govern active behavior.

## Governance rules

- References are advisory: they may provide examples, taxonomies, diagnostic questions, playbooks, source overlays, and domain nuance.
- References must not govern final decisions, evidence readiness, routing, IC Action, or agent ownership.
- Evidence Layer and Source Registry standards cannot be downgraded by domain source overlays.
- If this index conflicts with a file header, record a warning and apply the stricter interpretation until synchronized.
- Unregistered new reference files default to Draft/Advisory only until registered.
- Analytical labels are allowed; decision labels such as Buy, Sell, Add, Trim, Exit, or IC Action are not allowed as reference-owned labels.

## Reference map

| Reference | Owner | Contributors | Primary reference for | Supporting reference for | Freshness | Split/index status | Review note |
|---|---|---|---|---|---|---|---|
| `references/asset-driver-maps.md` | Driver Dominance | Market Sense; Equity Agent; ETF Agent; Fixed Income Agent; Commodity Agent; Crypto Agent; Macro Agent | cross-asset driver-map selection and driver checklist design | market interpretation; asset-class setup analysis; driver-dominance handoffs | Medium | Indexed reference file | Owner review needed |
| `references/commodity-analysis-framework.md` | Commodity Agent | Macro Agent; Market Sense; Valuation/Expectations; Risk Red Team | commodity analysis framework examples and domain structure | IC commodity context; macro/driver handoffs | Medium | Indexed reference file | No material warning |
| `references/commodity-family-playbooks.md` | Commodity Agent | Macro Agent; Market Sense; News & Catalysts | commodity-family playbooks | macro, catalyst, and supply/demand interpretation | Medium | Indexed reference file | No material warning |
| `references/crypto-analysis-framework.md` | Crypto Agent | Evidence Collector; Risk Red Team; Market Sense; Valuation/Expectations | crypto analysis framework examples and domain-specific modules | crypto risk, valuation-equivalent, liquidity, and adoption analysis | High | Indexed reference file | No material warning |
| `references/crypto-data-source-and-metric-framework.md` | Evidence Collector | Crypto Agent; Risk Red Team; Market Intelligence | crypto source and metric overlays | crypto evidence packs and source-quality checks | High | Indexed reference file | No material warning |
| `references/equity-company-analysis-framework.md` | Equity Agent | Financial Statement Analysis; Valuation/Expectations; Risk Red Team | equity company analysis framework examples | valuation, risk, financial statement, and IC equity context | Medium | Indexed reference file | No material warning |
| `references/equity-deep-dive-workflow.md` | Equity Agent | Router Layer; Evidence Collector; Investment Committee | equity deep-dive workflow examples | workflow sequencing examples only; canonical workflow contracts remain authoritative | Medium | Indexed reference file | No material warning |
| `references/etf-analysis-framework.md` | ETF Agent | Evidence Collector; Portfolio Fit; Risk Red Team; Valuation/Expectations | ETF vehicle and exposure analysis examples | implementation quality, vehicle-quality, and portfolio-fit context | Medium | Indexed reference file | No material warning |
| `references/evidence-pack-framework.md` | Evidence Collector | Investment Committee; asset-class agents; specialist agents | evidence-pack examples and source-display patterns | claim-support presentation and report appendices | Medium | Indexed reference file | No material warning |
| `references/evidence-request-protocol.md` | Evidence Collector | Router Layer; Investment Committee; asset-class agents | evidence request and missing-data protocol examples | handoff requests and gap checklists | Medium | Indexed reference file | No material warning |
| `references/fixed-income-framework.md` | Fixed Income Agent | Macro Agent; Risk Red Team; Valuation/Expectations | fixed-income analysis framework examples | duration, spread, credit, and macro-rate context | Medium | Indexed reference file | No material warning |
| `references/fixed-income-instrument-playbooks.md` | Fixed Income Agent | Macro Agent; Risk Red Team; Portfolio Fit | fixed-income instrument playbooks | implementation-quality and risk review context | Medium | Indexed reference file | No material warning |
| `references/investment-committee-memo-framework.md` | Investment Committee | Evidence Collector; asset-class agents; specialist agents | IC memo wording examples and decision-support presentation references | report-writing examples only; canonical report schemas govern final outputs | Medium | Indexed reference file | No material warning |
| `references/macro-block-playbooks.md` | Macro Agent | Market Sense; Evidence Collector; asset-class agents | macro block playbooks | asset-class macro context and driver analysis | Medium | Indexed reference file | No material warning |
| `references/macro-expectations-surprise-framework.md` | Macro Agent | Market Sense; Market Intelligence; Evidence Collector | macro expectations and surprise interpretation | market reaction and driver-dominance context | Medium | Indexed reference file | No material warning |
| `references/macro-g3-fx-regional-policy-overlay.md` | Macro Agent | Market Sense; Fixed Income Agent; Commodity Agent | G3, FX, and regional policy overlays | rates, FX, commodities, and cross-asset regime interpretation | High | Indexed reference file | No material warning |
| `references/macro-indicator-cadence-source-registry.md` | Macro Agent | Evidence Collector; Market Intelligence | macro indicator cadence and source overlays | macro freshness treatment and evidence packs | High | Indexed reference file | No material warning |
| `references/macro-regime-framework.md` | Macro Agent | Market Sense; asset-class agents; Risk Red Team | macro regime taxonomy and interpretation examples | asset-class sensitivity and IC context | Medium | Indexed reference file | No material warning |
| `references/macro-sensitivity-framework.md` | Macro Agent | asset-class agents; Valuation/Expectations; Risk Red Team | macro sensitivity mapping | asset-class risk, valuation, and scenario context | Medium | Indexed reference file | No material warning |
| `references/market-materiality-filter.md` | Market Intelligence | News & Catalysts; Evidence Collector; Market Sense | market-news materiality filtering | briefing inclusion decisions and catalyst triage | Medium | Indexed reference file | No material warning |
| `references/market-news-source-framework.md` | Market Intelligence | Evidence Collector; News & Catalysts; Macro Agent | market-news source overlays | news verification and market-context evidence packs | High | Indexed reference file | No material warning |
| `references/market-pattern-library.md` | Market Sense | Market Intelligence; Market Positioning; Macro Agent; News & Catalysts; asset-class agents | market-pattern selection index and usage rules | pattern hypothesis generation across asset-class and market-reaction workflows | Medium | Index | Owner review needed |
| `references/market-patterns/commodities-and-geopolitics.md` | Market Sense | Commodity Agent; Macro Agent; News & Catalysts | commodity and geopolitical market patterns | commodity catalyst and geopolitics interpretation | High | Domain split file | No material warning |
| `references/market-patterns/cross-asset-regimes.md` | Market Sense | Macro Agent; Commodity Agent; Risk Red Team | cross-asset and regime market patterns | safe-haven, risk-rally, and regime interpretation | Medium | Domain split file | No material warning |
| `references/market-patterns/event-reactions-and-earnings.md` | Market Sense | Market Intelligence; News & Catalysts; Equity Agent | event reaction and earnings-related market patterns | earnings, guidance, and event-reaction hypothesis generation | Medium | Domain split file | No material warning |
| `references/market-patterns/examples-and-source-map.md` | Market Sense | Market Intelligence; Evidence Collector; asset-class agents | market-pattern examples and source-map references | pattern QA, source-map upgrades, and example calibration | Medium | Domain split file | No material warning |
| `references/market-patterns/expectations-and-narratives.md` | Market Sense | Market Intelligence; Market Positioning; Valuation/Expectations | expectations and narrative market patterns | valuation-reset and narrative-risk hypothesis generation | Medium | Domain split file | No material warning |
| `references/market-patterns/macro-rates-liquidity.md` | Market Sense | Macro Agent; Fixed Income Agent; Market Intelligence | macro, rates, and liquidity market patterns | macro-reaction and cross-asset driver interpretation | High | Domain split file | No material warning |
| `references/market-patterns/positioning-and-flows.md` | Market Sense | Market Positioning; Market Intelligence; asset-class agents | positioning, crowding, squeeze, and flow patterns | positioning review and market-reaction context | High | Domain split file | No material warning |
| `references/market-patterns/stress-and-deleveraging.md` | Market Sense | Risk Red Team; Fixed Income Agent; Market Intelligence | stress and deleveraging market patterns | risk-gate context and market-stress interpretation | High | Domain split file | No material warning |
| `references/market-positioning-framework.md` | Market Positioning | Market Sense; Evidence Collector; asset-class agents | positioning, crowding, and flow framework examples | market-pattern and risk-context interpretation | High | Indexed reference file | No material warning |
| `references/news-catalysts-framework.md` | News & Catalysts | Market Intelligence; Evidence Collector; asset-class agents | catalyst taxonomy and news interpretation examples | market-intelligence and asset-class catalyst context | High | Indexed reference file | No material warning |
| `references/portfolio-fit-framework.md` | Portfolio Fit | Investment Committee; Risk Red Team; asset-class agents | portfolio-fit questionnaire and scenario examples | personalization, privacy-preserving fit, and implementation context | Medium | Indexed reference file | No material warning |
| `references/risk-red-team-framework.md` | Risk Red Team | Evidence Collector; asset-class agents; Investment Committee | risk challenge scenarios and red-team templates | risk-gate context and IC downside review | Medium | Indexed reference file | No material warning |
| `references/sector-industry-analysis-framework.md` | Sector & Industry Analysis | Structural Winners Discovery; Equity Agent; Market Intelligence | sector and industry analysis framework examples | theme workflows, discovery candidates, and asset-level review context | Medium | Indexed reference file | No material warning |
| `references/source-registry-framework.md` | Evidence Collector | domain agents; Market Intelligence; Investment Committee | source hierarchy overlays and source-quality examples | domain source selection and evidence pack construction | High | Indexed reference file | No material warning |
| `references/structural-winner-discovery-framework.md` | Structural Winners Discovery | Sector & Industry Analysis; Equity Agent; Valuation/Expectations; Risk Red Team | structural-winner discovery framework examples | theme-to-asset handoffs and discovery ranking context | Medium | Indexed reference file | No material warning |
| `references/valuation-expectations-framework.md` | Valuation/Expectations | asset-class agents; Investment Committee; Risk Red Team | valuation and expectations framework examples | asset-class valuation-equivalent and IC decision-prep context | Medium | Indexed reference file | No material warning |

## P9 readiness summary

- Supporting Reference and former Needs Split references have governance metadata headers.
- `references/market-pattern-library.md` is an index and usage guide; detailed pattern bodies live under `references/market-patterns/`.
- `references/asset-driver-maps.md` and `references/market-pattern-library.md` retain owner-review notes because they are cross-domain references.
- Residual `Needs Merge` files are not promoted by this index; only clear reference/playbook/source-overlay value may be selectively harvested in later cleanup.
