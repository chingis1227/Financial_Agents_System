# market_sense.md - QQQ vs SCHG for long-term U.S. growth exposure

## Handoff metadata
- Artifact: `market_sense.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Owner: Market Sense Agent
- Producing agent/skill/workflow: Market Sense Agent / smoke-test handoff
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Partial; official ETF/index data plus limited current market snapshot
- Freshness status: ETF/index data current to late May / June 2026 where cited; intraday snapshot limited
- Source scope: Public sources only
- Evidence limits: No full holdings-attribution model, ETF flow data, defined move window, or pre-IC evidence lock
- Key limitations: No full holdings-attribution model, ETF flow data, defined move window, or pre-IC evidence lock
- Missing gates: Full evidence pack; valuation; risk; portfolio fit; implementation checks; IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To ETF Analysis, Market Positioning, Macro, Valuation, Risk, and IC as driver map
- Required follow-up: Run holdings-attribution and rates/breadth/sector cross-checks over exact move window

## Market sense summary

Likely driver cluster for QQQ/SCHG moves is mega-cap growth, AI/semiconductors, and discount-rate sensitivity. If QQQ outperforms SCHG, first check Nasdaq-100-specific tech/semiconductor concentration. If SCHG outperforms QQQ, check broader large-cap growth breadth and non-Nasdaq growth sectors.


## Structured handoff
- Artifact: `market_sense.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Scope: Driver hypotheses, alternatives, and cross-checks for growth ETF moves
- Owner: Market Sense Agent
- Producing agent/skill/workflow: Market Sense Agent / smoke-test handoff
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Partial; official ETF/index data plus limited current market snapshot
- Freshness status: ETF/index data current to late May / June 2026 where cited; intraday snapshot limited
- Source scope: Public sources only
- Evidence limits: No full holdings-attribution model, ETF flow data, defined move window, or pre-IC evidence lock
- Key limitations: No full holdings-attribution model, ETF flow data, defined move window, or pre-IC evidence lock
- Key findings: Dominant driver likely mega-cap growth / AI / semis plus rate sensitivity; spread depends on Nasdaq concentration vs broader growth breadth
- Missing gates: Full evidence pack; valuation; risk; portfolio fit; implementation checks; IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation or trade instruction.
- Downstream handoff: To ETF Analysis, Market Positioning, Macro, Valuation, Risk, and IC as driver map
- Required follow-up: Run holdings-attribution and rates/breadth/sector cross-checks over exact move window
