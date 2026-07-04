# Equity internal full workflow Workflow Runbook

```yaml
contract_type: Workflow
status: Runtime Runbook
runbook_status: Runtime Runbook
authority_level: Subordinate to canonical implementation documents
owner: Asset Intake Router / Investment Committee Agent
used_by:
  - Concrete public-equity investment-action requests
  - Equity large-workflow analysis
produces:
  - evidence_pack.md
  - macro_sensitivity.md
  - sector_context.md
  - equity_company_analysis.md
  - financial_statement_analysis.md
  - valuation_expectations.md
  - risk_red_team.md
  - driver_dominance_analysis.md
  - portfolio_fit.md
  - decision_prep_memo.md # internal IC-stage artifact; saved user-facing output remains investment_report.md
  - limited_ic_draft.md # internal IC-stage artifact; saved user-facing output remains investment_report.md
  - evidence_gap_memo.md # internal IC-stage artifact; saved user-facing output remains investment_report.md
  - final_investment_memo.md # internal IC-stage artifact; saved user-facing output remains investment_report.md
consumes:
  - raw_user_request
  - user_context_when_available
  - public_market_and_company_sources
  - user_source_scope_constraints
  - upstream_handoff_artifacts
evidence_required: true
final_output_owner: Investment Committee Agent
decision_boundary: This runbook orchestrates the Equity internal full workflow. It does not create new decision rules, does not let non-IC agents issue IC Action, does not allow final positive IC Action unless all required gates pass, and does not allow personalized final IC Action when portfolio context is not closed.
known_gaps:
  - none
```

Authority: this is an executable runtime runbook assembled from `implementation/00-master-rules.md`, `implementation/04-evidence-layer.md`, `implementation/05-routing-and-workflows.md`, `implementation/06-agent-contracts.md`, `implementation/07-investment-committee-and-report-schemas.md`, and `implementation/13-codex-runtime-architecture.md`. It also inherits template, method-skill, QA, and language behavior from `implementation/03-contract-templates.md`, `implementation/09-system-acceptance-qa.md`, `implementation/11-skill-contracts.md`, and `implementation/14-language-and-style.md`. If this runbook conflicts with those canonical documents, the canonical documents govern and the conflict is a source issue under `implementation/01-documentation-control.md`.

## Trigger

Use this workflow for a public listed equity when the user asks whether to invest, buy, add, hold, sell, start exposure, or evaluate the stock for a capital-allocation horizon, unless the user explicitly requests a short / fast / `QUICK:` / quick take / preliminary output. The default execution mode is `Agent workflow with spawned subagents` with relevant subagents by default. If required subagents are unavailable, fail, or are not actually spawned, record `Production Blocked - subagents unavailable`, mark the workflow Blocked, and do not imply agent workflow execution.

Microsoft-like request routing example:

```text
"Should I invest in Microsoft if I do not own it, horizon 3+ years?"
```

Route: Master Intake Router -> Asset Intake Router -> Equity internal full workflow. Treat Microsoft as a public listed equity unless the instrument is ambiguous. Because the user says they do not own it and gives a 3+ year horizon, this is a concrete equity investment-action request, not a Quick Take. If the user does not provide portfolio composition, risk tolerance, objective, or exposure limits, continue the internal full workflow but mark Portfolio Fit and IC Action Status as Limited and use `decision_prep_memo.md` by default if portfolio context is the only missing final-action gate.

## When to use

Use when the request requires IC-level decision preparation or final decision support for a public equity and the asset identity is clear enough to route. If ticker, listing, share class, currency, or instrument type can materially change the conclusion, ask the minimum clarifying question before the decision workflow. Proceed with an explicit safe assumption and Limited status only when the identity is obvious enough that the assumption does not materially change the route.

## What you get

A controlled sequence from intake through evidence, macro, sector / industry, equity analysis, financial statement analysis, valuation, risk review, portfolio fit, and IC synthesis. The sequence can run in two modes: `Agent workflow with spawned subagents` when relevant subagents are actually spawned and return structured handoffs, or `Production Blocked - subagents unavailable` when required subagents cannot actually be spawned or completed. The main session must not replace a blocked production run with non-delegated substitute analysis. The internal IC-stage artifact is selected by gate state; saved user-facing large-workflow output remains `investment_report.md`:

- `final_investment_memo.md` only when evidence and all required gates are sufficient, or when canonical IC rules independently allow a supported final negative / cautionary action.
- `decision_prep_memo.md` when the workflow is otherwise usable but user portfolio context is the missing final-action gate.
- `limited_ic_draft.md` when useful IC synthesis is possible but non-evidence, non-portfolio workflow gates remain incomplete.
- `evidence_gap_memo.md` when evidence, freshness, source access, or required upstream evidence is the main limitation.

## What it will not do

- It will not produce a final positive `IC Action` before evidence, valuation, risk, lead analysis, material context, implementation, and portfolio-fit gates are satisfied.
- It will not let Equity, Financial Statement Analysis, Valuation, Risk, or Portfolio Fit outputs become final buy/sell/hold decisions.
- It will not hide missing portfolio context by silently assuming the user profile.
- It will not label a non-final artifact as `final_investment_memo.md`.
- It will not use `Action Box` outside a valid `final_investment_memo.md`.

## Saved output package

Equity large workflow saves the user-facing report outside the project repository as `investment_report.md` and creates an `audit\` folder with runtime metadata, sources, intake questions/answers, assumptions, and one `.md` handoff per actually run subagent or module. Ordinary chat reproduces `investment_report.md` exactly and ends only with the saved report path.

## Execution modes

Every Equity internal full workflow records one of these controlled values in `audit\run_metadata.md`; ordinary chat does not show the execution mode or Runtime Execution Plan unless explicitly requested:

| Execution mode | Use when | Runtime behavior | Required visibility |
|---|---|---|---|
| `Agent workflow with spawned subagents` | Default for ordinary Microsoft-like or other public-equity investment-action requests when relevant subagents are available and actually spawned. | Spawn only relevant subagents/custom-agent sessions, collect structured handoff artifacts or summaries, then synthesize through IC. | Record spawned agents, skipped relevant agents with reasons, handoff artifacts/summaries, and any spawn limitations in audit. |
| `Production Blocked - subagents unavailable` | Required when subagent spawning tooling is unavailable, blocked, required subagents fail, or no required subagents are actually spawned. | Stop the production workflow and report Blocked; do not synthesize non-delegated module analysis as a substitute for the live agent workflow. | Record the blocking reason in audit; do not write as if Evidence Collector, Equity Agent, Valuation, Risk, Portfolio Fit, or IC ran as independent subagents. |

If the user says "run all agents", run only all relevant Equity internal full workflow agents/modules, not literally every configured agent. The mere presence of unrelated agent names in this runbook does not authorize spawning them.

## Entry conditions

- Subject is a public equity or a stock-linked exposure where the owned instrument is equity.
- User intent is analysis-only, market action, personal/final action, or decision preparation.
- Source scope is known: full public-data workflow, user-restricted sources, provided-material only, or no-refresh.
- Time horizon is provided or can be split; final IC Action requires an explicit time horizon.
- Asset identity is resolved or safely assumed with visible limitations.

## Required agents and modules

| Runtime module | Owner | Required inputs | Required outputs | Status / handoff requirement |
|---|---|---|---|---|
| Master Intake Router | Master Intake Router | Raw user request, user context if available, source-scope constraints | `intake_block`, selected route, missing context, evidence profile | Status must reflect route confidence. Handoff route, intent, horizon, source scope, and missing context to Asset Intake and Evidence Collector. |
| Asset Intake Router | Asset Intake Router | `intake_block`, asset identifier, user intent, horizon, portfolio context by default | `asset_intake_block`, equity lead selection, required gate list | Must choose Equity route, identify required valuation/risk/portfolio gates, and not issue investment decisions. |
| Execution mode | Orchestrating runtime / router | User request wording, selected route, subagent-spawning availability, actual spawned subagents or blocking reason | `Execution mode: Production Blocked - subagents unavailable` or `Execution mode: Agent workflow with spawned subagents` | Required in `audit\run_metadata.md`. Spawned-subagent mode is valid only when relevant subagents are actually spawned. |
| Runtime Execution Plan | Orchestrating runtime / router | Selected Equity large-workflow route, execution mode, and required gate list | Audit plan with included modules, excluded modules, rationale, and module status table | Required in audit before large-workflow analysis. Every included module must have `Complete`, `Limited`, `Blocked`, `Not material`, or `Skipped with reason`. |
| Evidence Collector | Evidence Collector Agent / Evidence Collection skill | Intake, workflow plan, evidence profile, source scope, user materials | `evidence_pack.md`, readiness matrix, evidence requests, pre-IC evidence lock | Must classify claim support, source quality, freshness, conflicts, proxy evidence, and allowed IC artifact. No valuation, risk, portfolio, or IC conclusions. |
| Equity Agent | Equity Agent / Equity Company Analysis skill | `asset_intake_block`, `evidence_pack.md`, financial statement output by default, macro context, sector / industry context, and news context when material | `equity_company_analysis.md`, equity structured handoff | Produces business-quality and company-thesis analysis only. Must include `Boundary: Not an IC Action` if action language could be inferred. |
| Financial Statement Analysis | Financial Statement Analysis skill / equity workflow contributor | Evidence pack, filings/financial history, company model context | `financial_statement_analysis.md`, financial quality handoff | Required when financial quality, durability, accounting, cash flow, balance sheet, dilution, or capital allocation is decision-relevant. Must hand off to Equity, Valuation, Risk, and IC. |
| Valuation & Expectations | Valuation & Expectations Agent / skill | Evidence pack, lead equity analysis, current market data, financial history/forecast inputs | `valuation_expectations.md`, valuation structured handoff | Required when price, entry point, upside/downside, expected return, or capital allocation is decision-relevant. No final IC Action or exact price target as final truth. |
| Risk / Red Team | Risk / Red Team Agent / skill | Core thesis, evidence pack, lead analysis, valuation context, material specialist reports | `risk_red_team.md`, risk gate handoff | Required for final action requests. May fail a risk gate, but must not issue buy/sell/hold or final IC Action. |
| Portfolio Fit | Portfolio Fit Agent / skill | Asset thesis, user portfolio context if available, risk/valuation/asset reports | `portfolio_fit.md`, portfolio fit handoff | Required when portfolio role, sizing, personal suitability, or missing user context is material. Without portfolio data, provide only generic fit and mark personalized fit Limited. |
| Investment Committee | Investment Committee Agent / IC synthesis skill | Intake, evidence pack and pre-IC lock, lead analysis, valuation, risk, portfolio fit, material specialists | Internal IC-stage artifact: `final_investment_memo.md`, `decision_prep_memo.md`, `limited_ic_draft.md`, or `evidence_gap_memo.md`; saved user-facing output remains `investment_report.md` | Runs last. Owns `Investment View` and `IC Action` only when gates permit. Must select gate-aware artifact and preserve the Runtime Execution Plan summary. |

## Default context and additional conditional modules

These modules follow the audit Runtime Execution Plan and module status discipline. Macro and Sector / Industry Analysis are default equity context modules, not optional modules. News, market positioning, driver dominance, and implementation checks are additional conditional modules. When any module is excluded or limited, the audit status table must show `Not material`, `Limited`, `Blocked`, or `Skipped with reason`.

| Module | Owner | Include when | Required inputs when included | Required outputs / handoff | Status / exclusion rule |
|---|---|---|---|---|---|
| Sector & Industry Analysis | Sector & Industry Analysis Agent / skill | Default equity module; sector structure, competitive context, or profit-pool exposure informs thesis quality and risk | Evidence pack, company/subsector universe, horizon constraints, equity thesis context | `sector_context.md`, `sector_industry_memo.md`, or relevant sector handoff | Hand off sector relevance, limitations, and downstream IC relevance. If genuinely not material, record `Not material` or `Skipped with reason` in audit. |
| News & Catalysts | News & Catalysts Agent / skill | Request depends on latest, today, earnings, price action, recent events, or catalyst path | Evidence pack, recent events, filings/releases, market reaction context | `news_catalysts.md` with event status, source confidence, price/thesis relevance, and handoff | If freshness is material and not refreshed, mark `Limited` or `Blocked`; IC Action Status must be Limited or Blocked. |
| Market Positioning | Market Positioning Agent / skill | Consensus, crowding, flows, event bar, or revision momentum is material | Evidence pack, price/volume context, consensus or positioning proxies where available | `market_positioning.md` with expectations, crowding/neglect, event bar, and handoff | If included with weak data, mark `Limited`; if excluded, mark `Not material` or source-limited. |
| Driver Dominance | Driver Dominance Analysis skill / Market Sense contributor | Thesis or market reaction depends on one or a few dominant drivers, or competing drivers could change conclusion strength | Evidence pack, driver map, asset move or thesis-driver context, news/macro/positioning inputs where material | `driver_dominance_analysis.md` or driver-dominance handoff | If included, separate dominant, supporting, opposing, and ignored drivers. If excluded, mark `Not material` or `Skipped with reason`. |
| Macro Sensitivity | Macro Agent / Macro Analysis skill | Default module for every equity internal full workflow; rates, FX, liquidity, inflation, policy, or economic cycle may affect valuation, demand, discount rates, or risk appetite | Evidence pack, macro variables, transmission hypothesis, sector/company sensitivity | `macro_sensitivity.md` with transmission mechanism, scenarios, freshness caveats, and handoff | At least a short macro handoff is required unless explicit source scope or route rationale justifies limitation/skipping in audit; status follows evidence freshness and transmission confidence. |
| Implementation / vehicle quality | Asset Intake Router plus relevant wrapper / implementation review | The user asks through a wrapper, ADR, fund, option, illiquid listing, or structure where access/liquidity/fees/custody/tax can affect the result | Instrument identity, wrapper terms, liquidity/spread/fee/access data, custody/tax constraints where material | Implementation-quality handoff or appropriate asset/wrapper review | If material and unchecked, mark `Limited` or `Blocked`; positive IC Action is prohibited until resolved. |

Artifact naming note: `sector_context.md` follows the routing and workflow contract for embedded equity context. When a fuller sector artifact is produced, use the report-schema names such as `sector_industry_memo.md`; if canonical naming appears inconsistent in a future task, record it as a documentation-control source issue rather than resolving it inside this runbook.

## Sequence

1. **Classify the request.** Master Intake identifies request family, subject, instrument, action intent, time horizon, evidence profile, freshness needs, and missing context.
2. **Route the asset.** Asset Intake confirms the Equity route, the lead Equity Agent, required specialists, and any identity or implementation gates.
3. **Ask workflow intake questions.** Before starting the full workflow, ask exactly 5 equity-specific questions in one block and wait for the user's next message. If the user explicitly requested short / fast / `QUICK:` / quick take / preliminary mode, ask exactly 3 relevant questions and stay chat-only with no `investment_report.md` or `audit`.
4. **Record execution mode and the Runtime Execution Plan.** Before analysis, write `Execution mode`, included modules, excluded modules, route rationale, actual spawned subagents or blocking reason, and a module status table to `audit\run_metadata.md`. Ordinary chat hides this unless requested.
5. **Open evidence collection.** Evidence Collector builds `evidence_pack.md`, including source inventory, material claim map, freshness map, conflicts, missing data, source-scope limits, and readiness matrix.
6. **Run default context modules.** Run macro and sector / industry by default for equities after the evidence pack is opened. These modules may run in parallel with financial statement analysis, but Equity Agent must either consume their handoffs or record an audit-limited reason before relying on company-thesis conclusions.
7. **Run financial statement analysis.** Produce `financial_statement_analysis.md` when financial quality is decision-relevant. This may run staged or in parallel with context modules, but it must be available or explicitly Limited before valuation, risk, and IC synthesis rely on financial claims.
8. **Run equity company analysis.** Equity Agent produces `equity_company_analysis.md` using the evidence pack plus macro, sector / industry, financial statement, and news context where available or explicitly Limited. Output is a scoped specialist handoff, not final decision support.
9. **Run valuation and expectations.** Produce `valuation_expectations.md` for any investment-action, entry-point, expected-return, or valuation-sensitive request.
10. **Run risk red team.** Produce `risk_red_team.md` for final action or decision-preparation workflows. A failed risk gate prevents positive IC Action until resolved.
11. **Run portfolio fit.** Produce `portfolio_fit.md` when user-specific action, role, suitability, overlap, or sizing context matters. If portfolio context is missing, record `Portfolio Fit: Limited / not personalized` and General Portfolio Role Mode in audit, then pass a general Portfolio role handoff to IC.
12. **Perform pre-IC evidence lock.** Evidence Collector updates readiness, records unresolved gaps/conflicts, and states which IC artifact is allowed.
13. **Synthesize through IC.** IC integrates evidence and specialist handoffs, applies positive-action gates, resolves conflicts, and produces the correct internal IC-stage artifact: `final_investment_memo.md`, `decision_prep_memo.md`, `limited_ic_draft.md`, or `evidence_gap_memo.md`; saved user-facing output remains `investment_report.md`.

## Handoff artifact standard

Mandatory handoff behavior is governed by `workflows/handoff_artifact_standard.md`. Use the exact universal fields and structured handoff block from that file; do not create workflow-local aliases such as `Status`, `Downstream relevance`, or `Downstream consumers`.

In `Production Blocked - subagents unavailable`, mandatory artifacts may be written by the main session as artifact-equivalent summaries, but each included module must still be saved under `audit\` as its own clearly named `.md` handoff/report or module handoff file with the controlled artifact name and required fields. They must not be embedded as technical blocks in ordinary chat. In `Agent workflow with spawned subagents`, spawned subagents must return the structured artifact or artifact-equivalent summary before IC synthesis consumes it.

Minimum mandatory Equity large-workflow handoff set:

```text
evidence_pack.md
macro_sensitivity.md or macro_context.md
sector_context.md or sector_industry_analysis.md
equity_company_analysis.md
financial_statement_analysis.md
valuation_expectations.md
risk_red_team.md
portfolio_fit.md
IC-stage gate-aware artifact: decision_prep_memo.md by default when portfolio context is the remaining final-action gate; otherwise limited_ic_draft.md, evidence_gap_memo.md, or final_investment_memo.md only as allowed by IC schemas.
```

IC synthesis may use only validated structured handoff artifacts or artifact-equivalent summaries plus the audit Runtime Execution Plan, pre-IC evidence lock, and sanity-checked user context. If a required handoff lacks any controlled field from `workflows/handoff_artifact_standard.md`, IC must request the corrected handoff or downgrade to a gate-aware Limited/Blocked artifact.

Non-IC handoffs that could be mistaken for decision support must state `Boundary: Not an IC Action` and must not use `Action Box`, `IC Action`, final buy/sell/hold/add/trim/exit language, exact trade instructions, or exact position sizing.

## Module status rules

Use these status tokens exactly in module status tables: `Complete`, `Limited`, `Blocked`, `Not material`, `Skipped with reason`.

- `Complete`: required inputs and evidence are sufficient for that module's stated scope.
- `Limited`: useful output exists, but evidence, freshness, source scope, missing upstream inputs, or workflow exclusions constrain it.
- `Blocked`: the module cannot safely support the requested downstream conclusion.
- `Not material`: the module was considered and does not materially affect the stated decision route.
- `Skipped with reason`: the module was not run because the user scoped it out, data was unavailable, or another explicit workflow reason applies.

A large-workflow output is not valid unless every included module appears in the module status table with one of these statuses.


## Portfolio context gate

If portfolio context is not closed, the workflow must not issue a personalized final `IC Action`. For ordinary new-buy/add/hold/sell investment-action requests, missing portfolio context also blocks any final positive `IC Action`; use a gate-aware non-final artifact instead. Canonical negative or cautionary IC treatment may apply only when the higher-authority IC rules independently allow it, such as a strong disqualifying evidence case.

Portfolio context is treated as closed only when the information needed for the requested decision is available, usually including current position state, approximate exposure or portfolio weight when relevant, time horizon, risk tolerance or objective, and any material constraints. If those inputs are missing but the equity identity and investment-action route are clear:

- continue the Equity internal full workflow rather than downgrading silently to Quick Take;
- mark Portfolio Fit as `Limited` or not personalized in audit and use General Portfolio Role Mode;
- show the reader a `Portfolio role` / `Портфельная роль` section instead of Portfolio Fit failure wording;
- mark `IC Action Status` as `Limited` or `Blocked`;
- use `decision_prep_memo.md` by default when this is the only remaining final-action gate;
- do not use `final_investment_memo.md`, `Action Box`, or final `IC Action` language for the user-specific decision.

## Artifact selection rules

| Gate state | IC artifact | Allowed decision language | Required boundary |
|---|---|---|---|
| Evidence, lead analysis, valuation, risk, material context, implementation, and portfolio/user context are sufficient for the stated scope; or a narrow final negative/cautionary IC treatment is independently allowed by canonical IC rules | `final_investment_memo.md` | Controlled `IC Action` labels only; `Action Box` allowed. No personalized final action when portfolio context is not closed. | Must include Analysis Status, IC Action Status, Decision Confidence, Time Horizon, evidence/freshness notes, and view-change triggers. |
| Public-data internal full workflow is otherwise useful, but portfolio context is the missing final-action gate | `decision_prep_memo.md` | Working view only; no personalized final IC Action and no final positive IC Action; no `Action Box` | Must use Decision-Prep Box, mark IC Action Status Limited or Blocked, and list minimum portfolio context needed. |
| Useful IC synthesis is possible, but valuation, risk, implementation, specialist, or workflow gates remain incomplete for reasons other than primary evidence/freshness gaps | `limited_ic_draft.md` | Limited IC view only; no final positive IC Action; no `Action Box` | Must list missing gates, prohibited conclusions, and what would upgrade the memo. |
| Decision-critical evidence, freshness, source access, provenance, contradictions, or upstream evidence are missing or unreliable | `evidence_gap_memo.md` | Gap explanation and allowed interim view only; no final positive IC Action; no `Action Box` | Must identify missing evidence, why it matters, impact on Analysis Status and IC Action Status, and minimum evidence needed. |

## Microsoft-like request handling

For a request like `Should I invest in Microsoft, if I do not own it, horizon 3+ years?`:

1. Classify as a concrete public-equity investment-action request.
2. Select Equity internal full workflow, not Quick Take, unless the user explicitly asks for a short or preliminary answer.
3. Use `Agent workflow with spawned subagents` by default when relevant subagents are available and actually spawned; otherwise record `Production Blocked - subagents unavailable`, stop the production workflow, and do not imply agent workflow execution.
4. Include Master Intake, Asset Intake, Evidence Collector, Macro, Sector / Industry Analysis, Equity Agent, Financial Statement Analysis, Valuation, Risk Red Team, Portfolio Fit, and IC synthesis.
5. Treat missing portfolio composition, risk tolerance, objective, and exposure limits as non-blocking for the analytical workflow but blocking for personalized final IC Action and any ordinary final positive IC Action.
6. Produce `decision_prep_memo.md` by default if public evidence, valuation, risk, and lead analysis are sufficient but portfolio context is the remaining final-action gate.
7. Use `evidence_gap_memo.md` instead if current price, latest filings, news, valuation inputs, or other decision-critical evidence are stale, unavailable, contradictory, or not refreshed.
8. Do not use final buy/sell/hold wording or final positive `IC Action` unless all gates are complete.

## Completion rules

- **Complete internal full workflow / Final Memo allowed:** all included modules have valid status; evidence lock allows final memo; lead equity, financial statement analysis when material, valuation, risk, portfolio/implementation gates, and material context are sufficient; IC uses `final_investment_memo.md`.
- **Limited internal full workflow / Decision preparation:** all included modules have valid status, but at least one final-action gate is limited; IC uses `decision_prep_memo.md` or `limited_ic_draft.md`.
- **Evidence-constrained workflow:** evidence or freshness is decision-critical and insufficient; IC uses `evidence_gap_memo.md`.
- **Blocked workflow:** asset identity, source access, evidence reliability, or required upstream analysis is missing enough that even a bounded view would be unsafe; return only blocking issues, minimum next steps, and allowed interim scope.
- **Preliminary workflow:** only allowed when the user explicitly asks for Quick Take / preliminary / short / fast / `QUICK:` or when the output is a direct specialist early read.

## Runtime Execution Plan checklist

Before presenting an Equity large-workflow output, verify:

- `audit\run_metadata.md` records `Execution mode` as `Production Blocked - subagents unavailable` or `Agent workflow with spawned subagents`.
- Spawned-subagent mode is the default if relevant subagents are available and actually spawned; otherwise audit records `Production Blocked - subagents unavailable` and the workflow stops as Blocked.
- Audit records the selected route and why Equity internal full workflow was chosen; ordinary chat hides this unless requested.
- Included modules and excluded modules are listed in audit.
- Every included module has one valid status: `Complete`, `Limited`, `Blocked`, `Not material`, or `Skipped with reason`.
- Evidence Collector status and freshness treatment are recorded in audit and summarized in reader-facing prose when material.
- Macro, sector / industry, equity, financial statement analysis when material, valuation, risk, portfolio fit, and IC synthesis have handoff artifacts or audit-visible handoff summaries.
- Non-IC outputs do not contain final `IC Action`, `Action Box`, final buy/sell/hold labels, or exact sizing.
- If portfolio context is missing, Portfolio Fit and IC Action Status are Limited / not personalized, and `decision_prep_memo.md` is the default non-final artifact.
- If portfolio context is missing, ordinary `investment_report.md` presents this as a general Portfolio role section; technical Portfolio Fit status remains in audit.
- If evidence or freshness is the limiting gate, `evidence_gap_memo.md` is used.
- `final_investment_memo.md` appears only when all required gates pass.

## Acceptance checks

This runbook is ready when:

- A Microsoft-like public-equity investment-action request routes into this workflow.
- The workflow distinguishes audit-recorded `Production Blocked - subagents unavailable` from actual `Agent workflow with spawned subagents`.
- Ordinary Microsoft-like requests default to relevant spawned subagents by default; if required subagents did not run, the workflow records `Production Blocked - subagents unavailable`, stops as Blocked, and does not pretend subagents ran.
- Spawned-subagent workflows spawn only relevant subagents by default for full equity workflows and expose structured handoffs in audit.
- Module order is visible from Router to IC synthesis.
- Each module declares inputs, outputs, status treatment, and handoff requirement.
- The workflow distinguishes `decision_prep_memo.md`, `limited_ic_draft.md`, `evidence_gap_memo.md`, and `final_investment_memo.md`.
- Missing user portfolio context prevents personalized final IC Action and ordinary final positive IC Action, but does not stop the analytical internal full workflow.
- Evidence/freshness gaps route to `evidence_gap_memo.md`, not to a false final memo.
- Non-IC modules remain scoped and cannot issue final IC Action.

## Runtime Execution Plan update

The Runtime Execution Plan must show decision mode, Materiality Gate table, included modules, skipped modules with reason, Thesis Spine owner, and IC conflict-resolution requirement. The handoff must carry `thesis_spine_impact`, `materiality_status`, `quality_view_impact`, `entry_view_impact`, `monitoring_triggers`, and `what_would_change_view`. Optional market agents are materiality-triggered, not always-required, unless the prompt explicitly requests them or the decision mode makes them material.
