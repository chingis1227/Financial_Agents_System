# Direct Specialist Route Card

Status: Runtime route card
Authority: Subordinate to master rules and agent/skill contracts.

## Trigger

Use when the user explicitly asks for one specialist command, such as `RISK:`, `VAL:`, `MACRO:`, `NEWS:`, `PORTFOLIO:`, `SECTOR:`, `EVIDENCE:`, `POSITIONING:`, `INTEL:`, `EQUITY:`, `ETF:`, `COMMODITY:`, `CRYPTO:`, `FI:`, `WINNERS:`, or `IC:`.

## Required first action

Map the prefix to exactly one target agent. Confirm scope only if ambiguous. Do not expand to `AGENT:` unless the user asks for the large agent workflow.

## Specialist command mapping

| Prefix | Target agent |
|---|---|
| `RISK:` | `risk-red-team-agent` |
| `VAL:` | `valuation-expectations-agent` |
| `MACRO:` | `macro-agent` |
| `NEWS:` | `news-catalysts-agent` |
| `PORTFOLIO:` | `portfolio-fit-agent` |
| `SECTOR:` | `sector-industry-analysis-agent` |
| `EVIDENCE:` | `evidence-collector` |
| `POSITIONING:` | `market-positioning-agent` |
| `INTEL:` | `market-intelligence-agent` |
| `EQUITY:` | `equity-agent` |
| `ETF:` | `etf-agent` |
| `COMMODITY:` | `commodity-agent` |
| `CRYPTO:` | `crypto-agent` |
| `FI:` | `fixed-income-agent` |
| `WINNERS:` | `structural-winners-discovery-agent` |
| `IC:` | `investment-committee-agent` |

## Required modules

Only the requested specialist method plus evidence/source limitations needed for that scope.

## Allowed output

Specialist Verdict, Risk Box, Valuation Box, Evidence Gap Memo, market brief, committee-prep handoff, or scoped specialist summary. Every direct specialist output must include a visible boundary line that begins exactly:

```text
Boundary: Not an IC Action
```

## Forbidden output

- No `Action Box`.
- No final `IC Action` from any specialist command, including `IC:`.
- No final buy/sell/hold/add/trim/exit recommendation from any specialist command, including `IC:`.
- No expansion into the large agent workflow without `AGENT:` or an explicit user request.

## Downgrade rules

If the specialist cannot support the requested conclusion, return Limited / Blocked with minimum next step and IC gates required for final decision support.

## Validation expectations

Every specialist command prefix must map to exactly one target agent, remain specialist-scoped, and forbid final action language, including for `IC:`.
