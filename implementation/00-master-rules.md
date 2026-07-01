# Master Implementation Rules

Status: Canonical master-rule authority

## 1. Purpose

This document is the single rule authority for statuses, gates, decision labels, output standards, evidence display, freshness, user-facing style, and artifact naming.

Other implementation documents may restate these rules only as local application notes. If another implementation document conflicts with this file on these topics, this file governs.

Documentation registry, source-of-truth precedence, archive handling, and source issue severity are governed by `implementation/01-documentation-control.md`.

## 2. Base statuses

| Status | Meaning | Allowed use |
|---|---|---|
| Complete | Required inputs are sufficient for the stated scope. | Full report or Complete Final Memo when all required gates pass. |
| Limited | Analysis can proceed, but material limitations constrain conclusion strength. | Bounded conclusion with explicit limitations and follow-up needs. |
| Blocked | Required information is missing or unreliable enough that the requested conclusion must not be made. | Blocked output with required next steps only. |
| Preliminary | Narrow or early output before full workflow completion. | Scan, early read, direct specialist output, or Quick Take; not final decision support. |

### User-facing status labels

Internal statuses remain the implementation authority, but user-facing outputs must pair the status with a plain-language label and one-sentence meaning.

| Internal status | Recommended user-facing label | User meaning |
|---|---|---|
| Preliminary | Quick Take / Preliminary | Useful early read; not a final IC decision. |
| Limited | Limited / Needs more data | Usable only within stated constraints. |
| Blocked | Cannot conclude / Blocked | The requested conclusion must not be made until required information is available. |
| Complete | Complete for stated scope | Sufficient for the defined scope; not a guarantee of correctness. |

Specialized labels such as `Limited Valuation`, `Complete Risk Review`, or `Blocked IC Action` are allowed only when they map back to a base status and include a short explanation.

### Dual-status rule

User-facing outputs that could be mistaken for decision support must separate:

```text
Analysis Status: readiness of the analysis that was actually performed.
IC Action Status: whether final IC-level decision support is allowed.
```

Examples:

```text
Analysis Status: Complete for available evidence
IC Action Status: Limited - positive action is not allowed until valuation and risk review are complete
```

The analysis may be Complete, Limited, Preliminary, or Blocked independently from the IC Action Status. A complete specialist analysis does not imply a complete IC action.

## 3. Decision labels

| Label | Owner | Meaning |
|---|---|---|
| Specialist Verdict | Asset-class or specialist agent | Domain-specific conclusion, not final action. |
| Actionability Label | Domain owner where explicitly defined, including asset-class, specialist, or discovery agents | Setup-quality or next-step-priority label, not portfolio instruction. |
| Vehicle Quality Verdict | ETF / wrapper analysis | Quality of wrapper/exposure, not portfolio action. |
| Quality Verdict | Asset-class or domain owner | Business, asset, theme, or vehicle quality; not a statement that the asset is a good purchase now. |
| Valuation / Expectations Support | Valuation owner or asset-class equivalent | Whether price, expectations, or scenario payoff support the proposed decision. |
| Investment View | Investment Committee | Integrated final view in the memo. |
| IC Action | Investment Committee | Final decision-support action label. |

Quality, theme strength, or vehicle quality cannot by itself unlock a positive IC action.

## 4. IC actions and gates

### Positive action gate

A positive IC action requires all decision-relevant gates:

1. Evidence readiness is Complete or explicitly sufficient for the proposed action.
2. Valuation / expectations work is sufficient when price, upside/downside, or capital allocation is decision-relevant.
3. Risk / Red Team review is sufficient when thesis risk, downside, or final action is requested.
4. Lead asset/theme analysis is available.
5. Material context modules are present or explicitly non-material.
6. Implementation quality is acceptable when the chosen vehicle, liquidity, fees, custody, spreads, tax, access, or wrapper structure can materially affect the result.
7. Portfolio Fit / user-context gates are closed for any personalized final action, including current position, objective, horizon, risk tolerance, exposure, constraints, overlap, and sizing context when material.

If any required gate fails, the IC Action Status must be Limited or Blocked.

When the positive action gate is not satisfied:
- A positive `IC Action` is prohibited.
- The system may still provide a Preliminary or Limited stance when supported by available evidence.
- Non-IC agents may provide cautious / negative domain verdicts or Watchlist / Defer signals only as `Specialist Verdict` or `Actionability Label`, not as final `IC Action`.
- Final IC-level action labels such as Hard Avoid, Defer / Not Actionable, Watchlist, Maintain / Hold, Add, Initiate, Trim, or Exit belong only to the Investment Committee.
- The output must state what minimum evidence, valuation, risk, context, or implementation checks would be needed to unlock final decision support.

### Negative and cautionary outcomes

Positive action requires the full positive action gate. Negative / cautionary outcomes follow a separate rule:

| Outcome | Allowed when | Meaning |
|---|---|---|
| Hard Avoid | Strong disqualifying evidence exists, such as fraud, insolvency, severe liquidity failure, broken instrument, unacceptable implementation, or other material red flag. | The system can warn against initiating exposure even before every positive-action gate is complete. |
| Defer / Not Actionable | Evidence, valuation, risk, context, or implementation is insufficient. | The asset or idea is not yet decision-actionable; this is not the same as saying the asset is bad. |
| Watchlist | Thesis or quality may be interesting, but entry point, evidence, risk, implementation, or timing is not ready. | Monitoring / follow-up state, not a buy recommendation. |

A Hard Avoid needs a clearly stated disqualifying reason. If the issue is merely missing information, use Defer / Not Actionable instead.

Only IC may issue `IC Action: Hard Avoid`. Non-IC agents may flag a disqualifying `Specialist Verdict` or risk warning, with `Boundary: Not an IC Action`.

### Risk gate

Risk / Red Team does not own final IC Action and must not issue buy/sell/hold. It can create `Risk Gate: Failed` when downside, thesis failure modes, risk controls, leverage, liquidity, regulation, or other material risks are not sufficiently bounded. A failed Risk Gate prohibits positive IC Action until resolved.

## 5. Decision confidence standard

Every final memo and major specialist verdict should include decision confidence:

| Confidence | Use |
|---|---|
| High | Evidence is strong, current, internally consistent, and decision-critical uncertainties are bounded. |
| Medium | Evidence is usable but has meaningful limits, assumptions, or unresolved uncertainties. |
| Low | Evidence is incomplete, stale, proxy-heavy, contradictory, or scope-limited. |
| Not Rateable | Required evidence is too weak or missing; use Blocked or Preliminary output. |

`Decision Confidence` means confidence in the support for the conclusion, not certainty of the future price outcome. Every confidence label must include an evidence reason.

Example:

```text
Decision Confidence: Medium
Why: evidence is current, but valuation depends on unresolved margin assumptions.
Meaning: confidence in the conclusion support, not forecast certainty.
```

## 6. Output boxes

### Action Box standard

`Action Box` is reserved for IC-level final memos only. It must not appear in direct specialist reports, discovery outputs, market reaction notes, or non-IC workflow artifacts.

Final IC memos should include an Action Box when an IC-level decision-support output is requested.

Required fields:

```text
IC Action:
Investment View:
Decision Confidence:
Time Horizon:
Primary Reason:
Main Constraint:
What Would Change the View:
Monitoring Trigger:
Analysis Status:
IC Action Status:
```

Action Box practical meaning:
- It translates analysis into a decision-support stance.
- It does not provide exact trade instructions or exact position sizing.
- It must be constrained by evidence, valuation, risk, context, and implementation gates.

### Specialist mini-boxes

Specialist outputs may use scoped boxes, but they must not be called Action Box and must include a boundary statement.

Allowed examples:

```text
Specialist Verdict Box
Valuation Box
Risk Box
Discovery Box
Portfolio Fit Box
Market Reaction Box
Boundary: Not an IC Action.
```

## 7. Evidence display and data rules

### Evidence display and source standard

User-facing reports should not become bibliographies. They should display evidence in three layers:

1. Reader layer: concise source/date notes only where material.
2. Verification layer: evidence pack, claim support, source quality, freshness, contradictions.
3. Appendix layer: Evidence & Data Quality Appendix for limitations and source details.

Every final memo must include an Evidence & Data Quality Appendix or equivalent section when evidence limitations affect the conclusion.

### Evidence profiles

Use these evidence profiles by workflow:

| Evidence profile | Used for | Standard |
|---|---|---|
| Decision Evidence | Final investment action / IC memo | Highest standard; requires pre-IC evidence lock. |
| Analytical Evidence | Specialist analysis | Enough for bounded analysis; may be Limited. |
| Discovery Evidence | Theme / candidate discovery | Supports mapping and watchlists, not final actions. |
| Monitoring Evidence | Updates, catalysts, watchlist checks | Freshness and change detection matter most. |
| Market Reaction Evidence | Why-did-it-move analysis | Current market data and cross-asset confirmation matter most. |

### Freshness rule

Freshness depends on claim type:
- Market prices, yields, FX, spreads, volatility, ETF flows, crypto liquidity, and event-driven news require current or near-current data when used for action.
- Financial statements and filings require latest available official reporting.
- Slow-moving structural claims may use older sources if dated and still relevant.
- Stale decision-critical data causes Limited or Blocked IC Action Status.

When fresh data is required but unavailable, the system may provide structural, scenario, or educational analysis, but it must not issue a final IC Action or a current entry-point conclusion.

### Evidence conflicts

If sources conflict on a material claim, the main reader-facing report must show the conflict in plain language, using `Evidence Conflict` or a translated reader-facing label such as `Конфликт данных`. Do not hide material conflicts only in an appendix or audit file.

Required substance for material conflicts:

```text
Evidence Conflict / Конфликт данных:
What conflicts:
Why it matters:
Current treatment:
Impact on Analysis Status:
Impact on IC Action Status:
What would resolve it:
```

In ordinary reader-facing reports, keep the conflict explanation concise and natural; store the full conflict register in `audit`. Non-material conflicts that do not affect the investment conclusion may be stored only in `audit`.

Material unresolved conflicts must constrain the conclusion to Limited or Blocked when they are decision-critical.

### Paid, private, or unavailable data

Default assumption: the user does not manually provide paid datasets or private documents. Agents should use reliable public/accessible sources first, then controlled fallbacks.

If premium or private data is unavailable:
- Do not imply access to it.
- Provide a Public-data view where useful.
- Mark missing inputs and their effect on confidence/status.
- Provide a checklist of premium/private data that would upgrade the analysis.

### News, rumors, and market reaction

Market reaction analysis must separate:

```text
Confirmed Facts:
Unconfirmed / Rumor:
Market-Implied Signals:
Cross-check: asset vs peers / sector / broad market / relevant macro factors
Conclusion Status:
```

Rumors may be mentioned only as unconfirmed claims. They must not be treated as facts.

## 8. User-context and UX rules

### Question intake before investment answers

Before any `AGENT:` or ordinary routed full investment workflow, ask exactly 5 relevant, request-specific questions in one block. The questions must be tailored by asset type and should improve personalization, route quality, evidence scope, portfolio fit, implementation checks, or final IC synthesis. These questions are mandatory as a UX step but non-blocking:

- wait for the user's next message after asking the 5 questions;
- if the user answers all or some questions, use those answers and continue;
- if the user says "continue", "продолжай", "не знаю", "без уточнений", "как считаешь", "сам реши", or equivalent, continue with the approved baseline assumptions only;
- record the questions, answers, unanswered questions, and baseline assumptions in `audit`; do not add a separate assumptions block to `investment_report.md`;
- do not use missing answers to suppress a useful asset-level `AGENT:` workflow / internal full workflow when the asset and route are clear;
- ask blocking clarification separately before the 5 questions only when asset identity, instrument, source scope, or requested action cannot be safely routed.

For explicit `QUICK:` / short / fast / quick take / preliminary mode, ask exactly 3 relevant questions in one block, wait for the user's next message, and then answer in chat only. Quick mode must not create `investment_report.md` or `audit`.

Approved baseline assumptions after unanswered or partial intake are limited to:

- time horizon: 3-5 years when no horizon is stated;
- current position: no current position unless the user states otherwise;
- implementation: no leverage, options, or margin unless the user states otherwise;
- sizing: no exact position size without portfolio context;
- tax: no personalized tax recommendation.

Do not infer other defaults. The 5 `AGENT:` / full-workflow questions should be tailored by asset type. For example, Microsoft-like equity questions should cover objective, current broad/index/sector exposure, risk tolerance, entry style, and implementation constraints. Bitcoin-like questions should cover objective, volatility tolerance, existing crypto exposure, vehicle/custody preference, and jurisdiction/tax/custody constraints.

### Reader-facing workflow output

Ordinary chat responses after an investment workflow must be reader-facing investment reports, not runtime logs. Do not show `Execution mode`, Runtime Execution Plan, agent lists, module status tables, technical gate tables, runtime gate metadata, handoff metadata, or canonical artifact names in ordinary chat unless the user explicitly asks for workflow/debug/audit detail. Do show reader-facing conclusion status, material limitations, and missing checks needed for a final personalized decision.

The full reader-facing report should follow the applicable IC report structure from `implementation/07-investment-committee-and-report-schemas.md`: Complete Final Memo when gates pass, Limited IC Draft / Decision-Prep Memo when gates are limited, or Evidence Gap Memo when evidence/freshness gaps drive the limitation. Technical metadata remains in the saved report/audit pack.

`investment_report.md` must start with a short preparation date. In Russian reports, reader-facing headings must be Russian and the report must apply `language-policy` and `investment-analytical-style`. Status of the conclusion, missing items for a final personalized decision, and a short list of key sources belong at the bottom of the report. Full source lists, technical metadata, agent lists, module status tables, technical gate tables, runtime gate metadata, and canonical artifact names belong in `audit` unless explicitly requested. Reader-facing reports still show conclusion status, material limitations, and missing checks needed for a final personalized decision in plain language.

After a full workflow, save outputs outside the project repository under:

```text
C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\[ASSET] yyyy-mm-dd hhmm\
```

Save the user-facing report as `investment_report.md`. Save technical materials in `audit\`, including `run_metadata.md`, `sources.md`, the intake questions/answers, baseline assumptions used, and one `.md` handoff/report per actually run subagent or module. Create `audit\` for every full workflow, but do not show the audit path in ordinary chat unless the user explicitly asks for audit/debug details.

The ordinary chat response must output the full `investment_report.md` content exactly as saved, then end with only the saved-report line in the user-facing language. For Russian, use:

```text
Отчёт сохранён: [path]\investment_report.md
```

Do not show the audit path unless the user explicitly asks for audit/debug details.

### AGENT workflow execution default

User-facing runtime commands are `AGENT:`, `QUICK:`, and specialist prefixes. Existing file names, route IDs, smoke-test labels, and historical runbook terms may retain `full_cycle` / internal full workflow for compatibility, but internal full workflow is not a selectable user-facing mode.

`AGENT:` is the large agent workflow. It uses relevant spawned subagents when available and must not claim agent workflow execution unless subagents were actually spawned. If subagents are unavailable or are not actually spawned, record a non-spawned-subagent fallback only in audit metadata, mark the user-facing output Limited, and preserve all evidence, valuation, risk, portfolio, and IC gates. Do not advertise the fallback as a user-selectable mode. Ordinary concrete-asset investment-action prompts without a prefix still route through the router; recommended UX is `AGENT:` or `QUICK:`.

Agent workflow scope is relevant-complete, not literal-all-agents. Large workflows include macro context for every asset class. Equity internal full workflows additionally include sector / industry context by default. In `QUICK:` mode, macro and sector/industry are considered briefly inside the answer rather than as separate full modules.

### Action intent taxonomy

Classify action-oriented requests before deciding whether to answer immediately or ask for context:

| Intent level | Examples | Required behavior |
|---|---|---|
| Personal / final action | "Should I buy?", "What should I do with my position?", "How much should I buy?", "Should I sell my shares?" | If the request requires exact personal trade action, sizing, or existing-position handling and decision-critical personal context is missing, ask the minimum clarifying questions before giving an action-oriented conclusion. If the asset identity and capital-decision route are clear but portfolio context is missing, continue the concrete-asset `AGENT:` workflow / internal full workflow and mark Portfolio Fit / IC Action `Limited`; do not substitute silent assumptions or issue final `IC Action`. |
| Market action / investment attractiveness | "Is it a buy?", "Is it attractive here?", "Is gold a good setup now?" | Concrete-asset action requests route through the router; recommended explicit command is `AGENT:` unless the user asks for `QUICK:` / short / fast / quick take / preliminary output. Non-concrete setup questions or explicit Quick Takes may receive `Preliminary` / `Limited` market views, but Quick Take never issues final `IC Action`; if final gates are being completed, route to the gated large workflow / IC synthesis rather than the `QUICK:` route. |
| Analysis-only | "Analyze this company", "Value this company only", "What are the risks?", "What changed recently?" | Provide scoped analysis with status, evidence limits, boundary, and missing IC gates where relevant. |

When intent is ambiguous, use the safer level if the wording could reasonably be read as personal action. General analysis may continue with explicit scope limits.

### Blocking versus non-blocking context for AGENT workflow

| Missing item | Default behavior | Output effect |
|---|---|---|
| Asset identity, ticker/listing, instrument, wrapper, currency, maturity, or structure is materially ambiguous | Ask the minimum clarifying question before analysis | Block or limit until identity is resolved |
| User asks exact sizing, exact trade, or what to do with an existing personal position and position context is required | Ask the minimum personal context before personalized final action | No personalized final action until answered |
| Portfolio composition, risk tolerance, objective, or overlap is missing but the asset and route are clear | Continue `AGENT:` workflow / internal full workflow | Portfolio Fit is Limited / not personalized; IC Action Status remains Limited or Blocked |
| User explicitly requests `QUICK:` / short / fast / Quick Take | Provide Preliminary / Limited Quick Take | No final IC Action; if final gates are being completed, route to the gated large workflow / IC synthesis |

### Fast action requests

If the user explicitly asks for `QUICK:`, short, fast, preliminary, or Quick Take market-action answer, ask exactly 3 relevant questions first, then give `Quick Take / Preliminary` in chat only with no saved report/audit, and do not issue final `IC Action`. Quick Take never issues final IC Action; if final gates are being completed, route to the gated large workflow / IC synthesis. Concrete-asset investment action requests route through the router and should use `AGENT:` when the user asks whether to invest, buy, add, hold, sell, start exposure, or evaluate the asset for a stated horizon / portfolio decision, unless the user explicitly requests Quick Take. If the user asks for personal / final action and key blocking context is missing, ask for the minimum missing context first instead of giving an action conclusion.

Required pattern:

```text
Quick Take:
Status: Preliminary
IC Action Status: Limited or Blocked
Final IC Action: Not available in Quick Take; route to the gated large workflow / IC synthesis if final gates are complete or being completed
Needed for final IC Action:
```

### Missing personal context

If a user asks for exact personal buy/sell/hold/add/trim/exit guidance, existing-position handling, or sizing without decision-critical personal context, ask for only the minimum missing context needed before giving that personal action-oriented conclusion. If the same prompt is a concrete-asset investment-action request with clear identity and route, do not stop the asset work solely because portfolio context is missing: continue the `AGENT:` workflow / internal full workflow, mark Portfolio Fit / IC Action `Limited`, and withhold final `IC Action` until the personal gates are closed.

If the request is market action / investment attractiveness rather than personal action, first classify whether it is a concrete-asset investment-action request. For a concrete asset with capital-decision intent, route through the `AGENT:` workflow / internal full workflow by default and mark Portfolio Fit / IC Action `Limited` when non-blocking personal context is missing. Use a `Preliminary` or `Limited` scenario-based answer only for non-concrete setup questions, explicitly requested Quick Takes, or cases where the user explicitly asks for short / fast output.

Minimum context usually includes:
- current position: none / existing / considering add / considering trim or exit;
- time horizon;
- risk tolerance or objective;
- approximate portfolio weight or exposure when relevant.

### Unspecified decision mode

If the user does not specify whether the decision is new buy, hold, add, trim, exit, or watchlist, do not assume new buy. Provide a scenario matrix:

```text
Decision Mode: unspecified
New buyer:
Existing holder:
Considering adding:
Large / concentrated position:
Considering trim or exit:
Missing context for final action:
```

### Undefined "best"

If the user asks for the "best" asset without defining best, do not give one absolute winner. Use default criteria and scenario winners.

Default criteria:
- risk-adjusted return potential;
- valuation / expectations support;
- evidence quality;
- liquidity / implementability;
- portfolio usefulness.

### Time horizon

If time horizon is ambiguous, separate short-term and long-term views. Final IC Action must include `Time Horizon`; without it, the output remains Preliminary or Limited.

### Portfolio fit and privacy

If Portfolio Fit is requested without portfolio data, provide generic scenario-based fit and mark user-specific fit as Limited / not personalized.

The system should support privacy-preserving personalization through approximate buckets:

```text
Current exposure: none / small / medium / large
Horizon: short / medium / long
Risk tolerance: low / medium / high
Goal: growth / income / protection / speculation
```

If the user provides no context, answer only scenario-based and state that it is not personalized.

### Sizing and allocation

The system must not provide exact trade instructions or exact position sizing such as "buy exactly X%".

Allowed:
- illustrative sizing ranges by scenario;
- personalized decision-support ranges after Portfolio Fit workflow.

Not allowed:
- exact allocation as an instruction;
- precise position size without user context;
- leverage, custody, or yield-farming instructions that exceed the relevant workflow boundaries.

### Limited and Blocked next-step UX

`Limited` and `Blocked` outputs must not stop at a status label. They must include a short next-step block:

```text
What is missing:
Why it matters:
Minimum next step:
What can be done now:
```

The block should be concise and practical. Detailed checklists are optional when the user asks for full detail or when the missing data is complex.

### "No disclaimers" or "be decisive" requests

If the user asks for no disclaimers, no caveats, or a decisive answer, compress critical limitations but do not remove them. Status, evidence limits, missing gates, and non-IC boundaries are part of the answer, not optional legal boilerplate.

Allowed pattern:

```text
Short answer:
Status / boundary:
Main reason:
Needed for final action:
```

### Plain-English mode

If the user asks to explain simply, use plain-English explanation while preserving statuses, gates, confidence, and limitations.

Full memos may use:

```text
Plain-English Take:
Decision Impact:
What we know:
What we do not know:
Status:
Technical Appendix:
```

## 9. Workflow-boundary rules

### Direct specialist calls

Direct specialist calls are allowed. The specialist must:
- stay inside its scope;
- provide `Specialist Verdict`, not `IC Action`;
- state `Boundary: Not an IC Action`;
- list what would be required for IC-level decision support.

### Workflow handoff artifacts

large workflow / spawned-subagent workflow modules must leave structured handoff artifacts or artifact-equivalent summaries before downstream synthesis uses them. A valid handoff includes controlled artifact name, owner, producing agent/skill/workflow, workflow, execution mode, as-of date/time, output status, evidence status, freshness status, source scope, evidence limits, key limitations, missing gates, decision boundary, downstream handoff, and required follow-up.

IC synthesis must not treat unstructured chat, ownerless summaries, or handoffs missing evidence limits / missing gates as Complete upstream work. If a required handoff is incomplete, IC must request a corrected handoff or use a gate-aware Limited / Blocked artifact.

Non-IC handoff artifacts must not use `Action Box`, `IC Action`, final buy/sell/hold/add/trim/exit language, exact trade instructions, or exact position sizing. If action language could be inferred, the artifact must state `Boundary: Not an IC Action`.

### Cross-asset comparisons

For quick cross-asset comparisons, provide scenario-based comparison by role, not a universal ranking. If the user asks for a final choice, allocation, or action, relevant asset-class owners must provide their analysis and IC must synthesize.

### Theme and discovery outputs

Theme / discovery workflows may rank candidates, but only as `Discovery Ranking`, not `Buy Ranking`.

Allowed priority labels:
- High Priority for Asset-Level Review;
- Watchlist;
- Needs Evidence;
- Exclude / Low Relevance.

A discovery candidate becomes investment-actionable only after asset-level evidence, valuation / expectations, risk review, and IC synthesis.

### Asset-class valuation equivalents

If classic DCF or multiples are not applicable, use the asset-class valuation / expectations equivalent. If the valuation anchor is weak, require stronger risk review before positive action.

Examples:
- Crypto: liquidity, adoption, cycle, realized price or other network/market anchors, tokenomics, regulation, custody/security.
- Gold / commodities: real rates, dollar, cost curve, inventories, futures curve, supply/demand balance, positioning.
- Fixed income: yield, duration, credit spread, default/recovery, curve, structure.
- ETF / funds: underlying exposure valuation, methodology, fees, liquidity, tracking, holdings, wrapper quality.
- FX: rate differentials, policy, external balances, positioning.

### Implementation quality

If the implementation vehicle is material, positive action requires implementation check. Weak implementation quality must limit IC Action and trigger alternative routes.

Implementation review may cover:
- liquidity;
- fees;
- spreads;
- tracking;
- holdings / exposure purity;
- custody / counterparty;
- tax / jurisdiction;
- broker or access constraints.

### Updates to prior memos

Requests to update prior analysis must use delta-update when the prior memo is available:

```text
Prior View:
What Changed:
What Did Not Change:
Thesis Impact:
Action Impact:
Evidence / Gate Refresh Needed:
```

If the prior memo is unavailable, request it or perform fresh analysis with a clear disclaimer that it is not a true update of the prior view.

## 10. Report style and artifact rules

### Global investment-writing style

Project outputs should be concise, businesslike, investment-oriented, and analytically dense. Avoid generic, emotional, or conversational filler. Each paragraph should carry decision-relevant information. User-facing reports should integrate conclusions rather than expose internal agent transcripts.

### Language and style presentation layer

User-facing language selection, Russian language policy, and investment-analytical presentation-style activation are governed by `implementation/14-language-and-style.md`.

Default behavior:
- internal project documents and runtime-control files are written in English unless explicitly requested otherwise;
- user-facing answers and generated report content follow the user's requested language, with Russian output for Russian requests unless the user explicitly asks otherwise;
- Russian user-facing output uses strict Russian-language mode and should not contain unnecessary English or Run-glish;
- financial, market, investment, macro, company, sector, asset, and report-style user-facing outputs use concise investment-analytical style;
- presentation-style rules must not add facts, sources, caveats, conclusions, recommendations, investment calls, risk warnings, or override statuses, evidence limits, IC gates, or boundaries.

### Layered report rule

Even a full detailed memo must be layered:

1. Action Box only for `final_investment_memo.md`; Decision-Prep Box for non-final IC artifacts.
2. Main decision-oriented analysis.
3. Key risks and what would change the view.
4. Evidence, valuation, risk, and specialist summaries may be summarized in appendices; full assumptions stay in audit, while only decision-critical assumptions appear in reader-facing prose where they affect the analysis.

Raw agent transcripts are not the main report. They may be exported only as a debug or audit artifact when explicitly requested.

### Response depth rule

Match detail to the user's requested depth while preserving mandatory safety fields:

| Request depth | Expected shape |
|---|---|
| Quick question | Short answer plus 3-5 mandatory status, boundary, evidence, or next-step lines. |
| Standard analysis | Summary, key reasoning, limitations, and next steps. |
| Full memo | Layered artifact with decision-oriented main body and appendices. |

Concise output is acceptable only when it does not hide material status, evidence, IC-gate, or source-scope limits.

### What would change the view

IC memos must include `What Would Change the View` split into monitoring and action/view-change triggers.

```text
Monitoring Triggers:
Action / View-Change Triggers:
More positive if:
More negative if:
```

Where possible, use concrete metrics, thresholds, dates, events, KPI changes, or evidence requirements.

### Canonical artifact naming

Internal canonical final IC memo artifact: `final_investment_memo.md`. Saved user-facing large-workflow output remains `investment_report.md`.

`investment_committee_memo.md` is allowed as a legacy alias only when migrating older source documents; new internal IC schemas and workflows should use `final_investment_memo.md`, while user-facing saved output remains `investment_report.md`.

Every supporting artifact should include metadata:

```text
Artifact Type:
Owner:
Analysis Status:
IC Action Status:
Final / Supporting:
Supersedes:
Superseded By:
```

### Source-of-truth rule

Canonical implementation documents are source of truth. `PROJECT_STATE.md` summarizes current runtime state but does not override canonical rules. Legacy PRDs, drafts, old architecture maps, historical build logs, backups, archives, and audits are supporting or excluded according to `implementation/01-documentation-control.md` and cannot override canonical rules. If conflict exists, canonical wins.

## 11. Approved edge-case behavior table

Stable IDs in this table are used for QA traceability. If a rule changes, update both the detailed rule section and the matching QA row.

| Rule ID | # | Case | Canonical behavior |
|---|---:|---|---|
| P1-RULE-01-01 | 1 | Analysis partly ready but final action unavailable | Use separate `Analysis Status` and `IC Action Status`. |
| P1-RULE-01-02 | 2 | Personal buy/sell/hold without personal context | Ask the minimum blocking context before personalized final action; if asset identity and route are clear, continue the `AGENT:` workflow / internal full workflow with Portfolio Fit Limited. Explicit short/fast or non-concrete market-action questions may receive Preliminary/Limited scenario views. |
| P1-RULE-01-03 | 3 | Fresh data unavailable or stale | Give structural/scenario analysis only; block or limit current action. |
| P1-RULE-01-04 | 4 | Sources conflict | Show `Evidence Conflict`; constrain status if material. |
| P1-RULE-01-05 | 5 | User asks for one-line action | Give Quick Take / Preliminary only when the user explicitly requests a short / fast / one-line answer; otherwise concrete-asset investment action requests route to `AGENT:` / the internal full workflow. For personal final action with blocking missing context, ask first. |
| P1-RULE-01-06 | 6 | User asks for "best" without criteria | Use default criteria and scenario winners; no absolute winner. |
| P1-RULE-01-07 | 7 | New buy / hold / add / trim / exit unclear | If personal final action is requested, ask the minimum clarifier; otherwise provide an explicitly non-final scenario matrix and do not assume new buy. |
| P1-RULE-01-08 | 8 | High-quality asset but valuation weak | Separate Quality Verdict, Valuation Support, Investment View, and IC Action Status. |
| P1-RULE-01-09 | 9 | Risk review negative while others positive | Risk may create gate failure; IC remains final synthesis owner. |
| P1-RULE-01-10 | 10 | Specialist directly asked for final conclusion | Specialist gives scoped verdict plus boundary; no IC Action. |
| P1-RULE-01-11 | 11 | Cross-asset comparison | Quick view is scenario-based; final action requires asset-class work plus IC. |
| P1-RULE-01-12 | 12 | Discovery candidates look like buy list | Use Discovery Ranking and review priority, not Buy Ranking. |
| P1-RULE-01-13 | 13 | Portfolio Fit without portfolio data | Ask for minimum portfolio context before personal fit; generic fit may proceed only as Limited / not personalized with next steps. |
| P1-RULE-01-14 | 14 | Classic valuation not applicable | Use asset-class valuation / expectations equivalent; strengthen risk review when anchor is weak. |
| P1-RULE-01-15 | 15 | Good idea, weak implementation vehicle | Implementation check is required when material; suggest alternatives if weak. |
| P1-RULE-01-16 | 16 | User asks for short or detailed output | Use response depth layering; mandatory safety fields remain visible, and full detail stays decision-oriented. |
| P1-RULE-01-17 | 17 | Update prior memo | Use delta-update if prior memo exists; otherwise request it or fresh-analysis disclaimer. |
| P1-RULE-01-18 | 18 | Evidence readiness fails but user wants answer | Block IC Action; allow bounded analysis, scenarios, checklist, risk map. |
| P1-RULE-01-19 | 19 | News, rumors, and market reaction mixed | Separate confirmed, unconfirmed, and market-implied claims. |
| P1-RULE-01-20 | 20 | Exact sizing / allocation requested | Give illustrative ranges or portfolio-fit ranges only; no exact instruction. |
| P1-RULE-01-21 | 21 | Time horizon missing | Split short-term / long-term; final IC Action requires Time Horizon. |
| P1-RULE-01-22 | 22 | Confidence confused with forecast accuracy | Explain confidence as support for conclusion, not price certainty. |
| P1-RULE-01-23 | 23 | Action Box appears outside IC memo | Prohibit; use specialist mini-boxes with `Not an IC Action`. |
| P1-RULE-01-24 | 24 | Negative action before full positive gate | Hard Avoid only with strong disqualifying evidence; otherwise Defer / Not Actionable. |
| P1-RULE-01-25 | 25 | User asks what changes the view | Provide monitoring and action/view-change triggers. |
| P1-RULE-01-26 | 26 | User wants personal support without private details | Accept approximate buckets; otherwise scenario-based only. |
| P1-RULE-01-27 | 27 | User asks for simple explanation | Use plain-English mode without dropping gates/statuses. |
| P1-RULE-01-28 | 28 | Paid/private data unavailable | Provide Public-data view plus checklist; constrain confidence/status when material. |
| P1-RULE-01-29 | 29 | Many artifacts confuse final output | `final_investment_memo.md` is the internal canonical final IC artifact; saved user-facing large-workflow output remains `investment_report.md`; supporting artifacts need metadata. |
| P1-RULE-01-30 | 30 | Legacy/draft/backup used as source of truth | Canonical docs win; legacy is supporting/excluded by registry. |
