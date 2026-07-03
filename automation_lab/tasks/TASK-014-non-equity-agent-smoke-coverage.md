# TASK-014 — Full non-equity AGENT smoke coverage

Status: Complete

## Goal

Add executable, validated AGENT smoke paths for ETF/fund, fixed income, crypto, commodity, and multi-asset comparison while preserving Financial Agent System as the source of truth.

## Value

The Automation Lab can now run the same production-like package pattern beyond equities: route → intake → source preflight → evidence pack → specialist handoffs → IC synthesis → reader-facing report → audit → validation.

## Dependencies

- Financial Agent System route cards and canonical rules.
- Existing Automation Lab `agent-run`, source preflight, evidence pack, specialist artifact, report, and validation framework.
- Existing Codex SDK live specialist launcher.

## Scope

- Extend `agent-run` and `agent-intake` beyond public equities to supported smoke identities: SPY/ETF, TLT/fixed income, BTC/crypto, GLD/commodity, and MSFT-SPY-BTC/multi-asset comparison.
- Create route-specific specialist sets and required-specialist gates.
- Create public/no-key source preflight records for non-equity workflows.
- Keep Complete semantics truthful: historical fixture is deterministic regression only; live requires real Codex SDK thread metadata for completed live specialists.
- Add unittest coverage for non-equity report/audit/validation packages.

## Out of scope

- Moving investment logic into Automation Lab.
- Adding paid-data dependencies or hidden API keys.
- Building a scheduler, dashboard, queue, or OpenAI Agents SDK runtime.
- Claiming Complete live specialist execution when live Codex SDK specialists fail, time out, or lack thread ids.

## Test plan

```powershell
.\.venv\Scripts\python.exe -m unittest tests.test_agent_run_cli.AgentRunTask011Tests.test_non_equity_agent_routes_create_report_audit_and_validate tests.test_agent_run_cli.AgentRunTask011Tests.test_agent_intake_spy_asks_exactly_five_and_stops
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py"
```

## Definition of Done

- ETF/fund, fixed income, crypto, commodity, and multi-asset historical fixture AGENT runs create `investment_report.md` plus `audit/`.
- Each package includes source preflight, provider results, evidence pack, specialist handoffs, run manifest, and validation files.
- `validate-agent-run` passes for the generated packages.
- README and ROADMAP document the new execution paths and limitations.
