# financial_statement_analysis.md - Microsoft / MSFT

## Handoff metadata
- Artifact: `financial_statement_analysis.md`
- Subject: Microsoft Corporation (`MSFT`), public common stock
- Scope: scoped financial-statement quality input
- Owner: Financial Statement Analysis contributor
- Producing agent/skill/workflow: Financial Statement Analysis contributor / `financial-statement-analysis` skill
- Workflow: Equity Full Cycle / Delegated Full Agent Workflow
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30 Europe/Budapest; evidence through FY26 Q3 release/Form 10-Q dated 2026-04-29 plus FY2025 Form 10-K
- Output status: Complete
- Evidence status: Official public filings support the core scoped financial-statement claims
- Freshness status: Current for latest reviewed reported financial statements; FY26 Q4/FY2026 annual data not reviewed in this run
- Source scope: public data only; Microsoft IR, FY26 Q3 Form 10-Q, FY2025 Annual Report / Form 10-K
- Evidence limits: no private data; no post-Q3 internal data; valuation, current market price, risk, portfolio, and IC synthesis are outside this artifact
- Key limitations: capex/FCF and accounting-risk interpretation must be tested by Valuation, Risk / Red Team and IC before decision support
- Key findings: FY26 Q3 shows strong revenue and earnings growth; free-cash-flow conversion is pressured by AI infrastructure investment
- Missing gates: Evidence lock, Valuation, Risk, Portfolio Fit, implementation check if material, IC synthesis
- Decision boundary: Boundary: Not an IC Action. Scoped financial-statement view only.
- Decision constraints: No valuation conclusion, portfolio recommendation, trade instruction, sizing, or IC Action.
- Downstream handoff: To Valuation, Risk, Portfolio Fit, and IC as financial-quality input
- Required follow-up: Refresh with FY26 Q4/FY2026 annual results when filed; reconcile capex, leases, and cash conversion into valuation and risk scenarios

## Method summary

Microsoft's latest reviewed quarter shows strong revenue and earnings growth. Financial quality remains high, but free-cash-flow conversion is under pressure from AI infrastructure investment. Debt appears manageable on a debt-only basis, while leases, data-center commitments, tax disputes, and AI capex are material watch items.

## Key data used

- FY26 Q3 revenue: $82.9B.
- FY26 Q3 operating income: $38.4B.
- FY26 Q3 net income: $31.8B.
- FY26 Q3 diluted EPS: $4.27.
- FY26 Q3 operating cash flow: $46.7B.
- FY26 Q3 property and equipment additions: $30.9B.
- Cash and short-term investments: $78.3B at the reviewed balance-sheet date.

## Handoff implications

The financial-statement gate does not show an immediate accounting-quality failure signal in the reviewed material. It does, however, pass a major valuation and risk question downstream: infrastructure spend must be translated into depreciation, capex intensity, margins, free-cash-flow conversion, and return-on-invested-capital scenarios.
## Scope note

This file is a structured handoff artifact for the delegated smoke test, not a full production standalone specialist report. Its conclusions are intentionally scoped and must be consumed with the evidence pack, valuation, risk, portfolio, and IC gates.

## Structured handoff

- Artifact: `financial_statement_analysis.md`
- Subject: Microsoft Corporation (`MSFT`), public common stock
- Scope: scoped financial-statement quality input
- Owner: Financial Statement Analysis contributor
- Producing agent/skill/workflow: Financial Statement Analysis contributor / `financial-statement-analysis` skill
- Workflow: Equity Full Cycle / Delegated Full Agent Workflow
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30 Europe/Budapest; evidence through FY26 Q3 release/Form 10-Q dated 2026-04-29 plus FY2025 Form 10-K
- Output status: Complete
- Evidence status: Official public filings support the core scoped financial-statement claims
- Freshness status: Current for latest reviewed reported financial statements; FY26 Q4/FY2026 annual data not reviewed in this run
- Source scope: public data only; Microsoft IR, FY26 Q3 Form 10-Q, FY2025 Annual Report / Form 10-K
- Evidence limits: no private data; no post-Q3 internal data; valuation, current market price, risk, portfolio, and IC synthesis are outside this artifact
- Key limitations: capex/FCF and accounting-risk interpretation must be tested by Valuation, Risk / Red Team and IC before decision support
- Key findings: FY26 Q3 shows strong revenue and earnings growth; free-cash-flow conversion is pressured by AI infrastructure investment
- Missing gates: Evidence lock, Valuation, Risk, Portfolio Fit, implementation check if material, IC synthesis
- Decision boundary: Boundary: Not an IC Action. Scoped financial-statement view only.
- Decision constraints: No valuation conclusion, portfolio recommendation, trade instruction, sizing, or IC Action.
- Downstream handoff: To Valuation, Risk, Portfolio Fit, and IC as financial-quality input
- Required follow-up: Refresh with FY26 Q4/FY2026 annual results when filed; reconcile capex, leases, and cash conversion into valuation and risk scenarios
