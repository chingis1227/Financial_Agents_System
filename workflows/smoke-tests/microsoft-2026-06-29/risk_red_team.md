# risk_red_team.md - Microsoft / MSFT

## Handoff metadata
- Artifact: `risk_red_team.md`
- Subject: Microsoft Corporation (`MSFT`), public equity, horizon 3+ years
- Scope: scoped risk and red-team gate input
- Owner: Risk / Red Team Agent
- Producing agent/skill/workflow: Risk / Red Team Agent / `risk-red-team` skill
- Workflow: Equity internal full workflow / Agent workflow with spawned subagents
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30 Europe/Budapest runtime context
- Output status: Limited
- Evidence status: Limited public-data risk review; sufficient for scoped risk mapping, not sufficient for final IC Action
- Freshness status: Current for FY26 Q3 earnings and the latest market snapshot; structural regulatory/security sources reviewed through 2025-2026 context
- Source scope: public sources only
- Evidence limits: missing full evidence lock, complete valuation model, portfolio context, customer-level AI ROI evidence, and proprietary cloud workload data
- Key limitations: risk gate is conditional; no trade instruction, exact position size, or final IC Action
- Key findings: public evidence does not force Risk Gate: Failed, but it does not clear a positive IC path
- Missing gates: Evidence lock, lead equity analysis, financial-statement analysis, valuation/expectations bridge, Portfolio Fit, IC synthesis
- Decision boundary: Boundary: Not an IC Action. Scoped risk input only.
- Decision constraints: No trade instruction, exact sizing, or IC Action.
- Downstream handoff: To Portfolio Fit and Investment Committee as risk-gate input only
- Required follow-up: Run downside scenarios for lower Azure growth, lower cloud margin, higher depreciation/capex intensity, OpenAI non-exclusivity, and regulatory drag

## Method summary

Risk Gate status: Limited / Conditional Risk Gate. Public evidence does not force `Risk Gate: Failed`, but it does not clear a positive IC pathway without explicit AI capex ROI, cloud-margin, and valuation-compression stress tests.

## Main risk clusters

1. AI capex ROI: capital intensity may outrun monetization and pressure free-cash-flow conversion.
2. Azure durability: growth could normalize faster than expectations embedded in the valuation.
3. Margin pressure: depreciation, power, data-center, and model costs may limit operating leverage.
4. OpenAI economics: dependency, economics, or strategic alignment could change.
5. Regulation and cybersecurity: antitrust, cloud, AI, and security trust issues can affect growth or margins.
6. Valuation compression: high-quality business fundamentals may still produce weak returns if the multiple compresses.

## Risk gate conclusion

The risk work supports continued analysis, not a final action. A final IC memo would need quantified downside scenarios and a clear statement that the thesis still works under adverse capex, margin, growth, and multiple assumptions.
## Scope note

This file is a structured handoff artifact for the spawned-subagent smoke test, not a full production standalone specialist report. Its conclusions are intentionally scoped and must be consumed with the evidence pack, valuation, risk, portfolio, and IC gates.

## Structured handoff

- Artifact: `risk_red_team.md`
- Subject: Microsoft Corporation (`MSFT`), public equity, horizon 3+ years
- Scope: scoped risk and red-team gate input
- Owner: Risk / Red Team Agent
- Producing agent/skill/workflow: Risk / Red Team Agent / `risk-red-team` skill
- Workflow: Equity internal full workflow / Agent workflow with spawned subagents
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30 Europe/Budapest runtime context
- Output status: Limited
- Evidence status: Limited public-data risk review; sufficient for scoped risk mapping, not sufficient for final IC Action
- Freshness status: Current for FY26 Q3 earnings and the latest market snapshot; structural regulatory/security sources reviewed through 2025-2026 context
- Source scope: public sources only
- Evidence limits: missing full evidence lock, complete valuation model, portfolio context, customer-level AI ROI evidence, and proprietary cloud workload data
- Key limitations: risk gate is conditional; no trade instruction, exact position size, or final IC Action
- Key findings: public evidence does not force Risk Gate: Failed, but it does not clear a positive IC path
- Missing gates: Evidence lock, lead equity analysis, financial-statement analysis, valuation/expectations bridge, Portfolio Fit, IC synthesis
- Decision boundary: Boundary: Not an IC Action. Scoped risk input only.
- Decision constraints: No trade instruction, exact sizing, or IC Action.
- Downstream handoff: To Portfolio Fit and Investment Committee as risk-gate input only
- Required follow-up: Run downside scenarios for lower Azure growth, lower cloud margin, higher depreciation/capex intensity, OpenAI non-exclusivity, and regulatory drag
