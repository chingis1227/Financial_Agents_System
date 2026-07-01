# etf_analysis.md - QQQ vs SCHG for long-term U.S. growth exposure

## Handoff metadata
- Artifact: `etf_analysis.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Owner: ETF Agent
- Producing agent/skill/workflow: ETF Agent / smoke-test handoff
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; public issuer/index pages and broker holdings snapshot, not final evidence lock
- Freshness status: Current enough for smoke-test; market-sensitive fields require refresh
- Source scope: Public sources only
- Evidence limits: No full tracking-error, premium/discount, tax/access, or live spread analysis
- Key limitations: No full tracking-error, premium/discount, tax/access, or live spread analysis
- Missing gates: Valuation; risk; portfolio fit; tax/account constraints; full evidence lock
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To Valuation, Risk, Portfolio Fit, and IC as vehicle-quality input
- Required follow-up: Run portfolio overlap and implementation checks before final action

## ETF analysis summary

| Area | QQQ | SCHG | Implication |
|---|---|---|---|
| Wrapper | Invesco Nasdaq-100 ETF; expense ratio 0.18% | Schwab U.S. Large-Cap Growth ETF; expense ratio 0.040% | SCHG has cost edge; QQQ has trading-depth/use-case edge. |
| Exposure | Nasdaq-listed non-financial mega-cap growth / innovation | Broader U.S. large-cap growth style exposure | QQQ is narrower; SCHG is broader by holdings. |
| Concentration | Mega-cap/tech/semiconductor concentration | Broader but still top-heavy in mega-cap growth | Both need overlap and concentration review. |
| Implementation | Highly traded ETF, options ecosystem | Large low-cost ETF, normal implementation quality | Choice depends on role and execution needs. |

## Vehicle quality verdict - scoped

Both wrappers are high-quality for their stated exposures. The comparison is a role decision, not a final action decision.


## Structured handoff
- Artifact: `etf_analysis.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Scope: ETF wrapper, exposure purity, methodology, fees, concentration, liquidity, overlap, implementation risks
- Owner: ETF Agent
- Producing agent/skill/workflow: ETF Agent / smoke-test handoff
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; public issuer/index pages and broker holdings snapshot, not final evidence lock
- Freshness status: Current enough for smoke-test; market-sensitive fields require refresh
- Source scope: Public sources only
- Evidence limits: No full tracking-error, premium/discount, tax/access, or live spread analysis
- Key limitations: No full tracking-error, premium/discount, tax/access, or live spread analysis
- Key findings: QQQ is narrower Nasdaq-100/liquidity vehicle; SCHG is broader and cheaper large-cap growth vehicle; overlap and mega-cap concentration are high
- Missing gates: Valuation; risk; portfolio fit; tax/account constraints; full evidence lock
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation or trade instruction.
- Downstream handoff: To Valuation, Risk, Portfolio Fit, and IC as vehicle-quality input
- Required follow-up: Run portfolio overlap and implementation checks before final action
