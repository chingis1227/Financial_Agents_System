# Investment Committee and Report Schemas

Status: Canonical synthesis and report-schema contract

## 1. Investment Committee contract

Canonical final memo artifact: `final_investment_memo.md`. Legacy references to `investment_committee_memo.md` should be treated as aliases during migration, not as the preferred new artifact name.

The Investment Committee Agent is the final synthesis and decision-support layer. It is downstream-only. It owns `Investment View` and `IC Action` only when gates permit. It must not invent facts, override evidence readiness, hide material conflicts, provide exact trade instructions, or convert specialist verdicts into final action without required synthesis.

Required inputs for Complete Final Memo:
- Intake context.
- Evidence pack and pre-IC evidence lock.
- Lead asset or theme analysis.
- Valuation / expectations analysis when price, entry point, upside/downside, or capital allocation is decision-relevant.
- Risk / Red Team review when final action is requested.
- Implementation / vehicle-quality review when vehicle, wrapper, liquidity, fees, custody, spreads, tax, access, or structure can materially affect the result.
- Material specialist reports where relevant.

Allowed IC output artifacts:

| Artifact / output | Status use | Action Box allowed | Use |
|---|---|---:|---|
| `final_investment_memo.md` | Complete Final Memo | Yes | Required evidence and decision-gate reports are sufficient for the stated scope. |
| `limited_ic_draft.md` / Limited IC Draft | Limited | No | Analysis is useful, but missing gates, source scope, freshness, conflicts, or workflow exclusions constrain conclusion strength. |
| `decision_prep_memo.md` / Decision-Prep Memo | Preliminary or Limited | No | User needs an actionable preparation summary before final IC gates are complete. |
| `evidence_gap_memo.md` / Evidence Gap Memo | Limited or Blocked | No | Decision-critical evidence, freshness, or upstream reports are missing or unreliable. |

Positive IC actions require sufficient evidence, valuation / expectations support, risk review, lead analysis, material context modules, and implementation quality when material. If those gates are missing, the IC output must be Limited or Blocked and must use a gate-aware non-final artifact unless the final request is explicitly for a blocked/negative IC response. Final cautionary IC Actions follow narrower evidence standards: Hard Avoid requires strong disqualifying evidence; Defer / Not Actionable may be final when IC has enough evidence to conclude readiness is insufficient; Watchlist may be final when the idea is supported but lacks a defined trigger, price, catalyst, risk resolution, or implementation readiness for positive action. Missing data alone does not justify Hard Avoid.

## 2. Final memo style rules

The memo must be a professional investment memo, not an internal transcript.

Do not write:
- "The Equity Agent said..."
- "The Risk Agent output..."
- "The Evidence Collector believes..."

Write integrated conclusions instead:
- "Business quality is strong, but valuation is the main constraint."
- "The risk profile is manageable only if margin durability holds."
- "The setup is not actionable until valuation or catalyst evidence improves."

Final memos must be layered:
1. Decision summary / Action Box when a Complete Final Memo is allowed.
2. Main decision-oriented memo.
3. Key risks, monitoring, and what would change the view.
4. Appendices for evidence quality, source limits, specialist detail, valuation detail, and audit trail if explicitly requested.

Raw agent transcripts must not be the main memo. Specialist detail may be summarized or moved to appendices.

## 3. Required report metadata

All report artifacts should include:

```text
Subject:
Request type:
Workflow:
Produced by:
As-of date/time:
Output status: Complete / Limited / Blocked / Preliminary
Evidence status:
Source scope:
Key limitations:
Decision boundary:
Downstream handoff:
```

IC-level artifacts should additionally include:

```text
Analysis Status:
IC Action Status:
Decision Confidence:
Time Horizon:
Freshness status:
Included / Excluded Modules and Why:
```

### Freshness top block

Every IC-level artifact must show freshness near the top when the request depends on current or near-current information.

```text
As-of date/time:
Freshness status: Current / Stale risk / Needs refresh
Freshness-sensitive items:
- price / valuation snapshot
- earnings / filings
- news / catalysts
- rates / spreads / FX / volatility
- ETF flows / liquidity / holdings
- crypto liquidity / custody / regulation
Current-action impact:
```

If freshness is material and not current, structural analysis may proceed, but current entry-point conclusions and positive IC Action remain Limited or Blocked.

## 4. IC Action labels and decision boxes

### Action Box

`Action Box` is reserved for `final_investment_memo.md` only when the Complete Final Memo gates are satisfied or when IC is issuing an explicitly supported negative / cautionary final action. Non-final IC artifacts, specialist outputs, discovery reports, market reaction notes, and portfolio-fit reports must not use `Action Box`.

Required Action Box fields:

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

### Decision-Prep Box

Use `Decision-Prep Box`, not `Action Box`, for Limited IC Drafts, Decision-Prep Memos, and Evidence Gap Memos.

Required Decision-Prep Box fields:

```text
Preliminary / Limited View:
IC Action Status: Limited / Blocked
What can be concluded now:
Missing gates:
Source / freshness limits:
Decision mode assumptions:
Needed for final IC Action:
```

### Controlled IC Action labels

Final IC Action labels must use this controlled set:

| IC Action label | Use |
|---|---|
| Initiate | Start a new exposure when full positive-action gates are satisfied for the stated horizon and context. |
| Add | Increase an existing exposure when full positive-action gates are satisfied and portfolio context permits. |
| Maintain / Hold | Continue an existing exposure; do not use for a user with no position unless clearly framed as a scenario. |
| Trim | Reduce an existing exposure when valuation, risk, portfolio fit, or thesis change supports reduction. |
| Exit | Fully leave an existing exposure when thesis, risk, valuation, or implementation quality no longer supports holding. |
| Watchlist | Idea is interesting but needs a trigger, better price, catalyst, evidence, risk resolution, or implementation improvement before action. |
| Defer / Not Actionable | Current decision is not ready because gates, data, source quality, setup, or user context are insufficient. |
| Hard Avoid | Strong disqualifying evidence exists; not a substitute for missing data. |

`Buy`, `Sell`, `Strong Buy`, `Strong Sell`, `Trade now`, or free-form broker-style labels are not canonical IC Action labels. Specialist and asset reports must not use IC Action labels as their own final decisions.

### Watchlist vs Defer / Not Actionable vs Hold

- `Maintain / Hold` applies to an existing position and means keep exposure within the stated horizon and constraints.
- `Watchlist` means the idea may be attractive, but needs a defined trigger before final action.
- `Defer / Not Actionable` means a decision should not be made now because evidence, gates, source scope, valuation, risk, implementation, or user context is insufficient.
- `Hard Avoid` requires a strong disqualifier such as fraud, insolvency, broken instrument mechanics, severe liquidity failure, unacceptable custody/security risk, or equivalent material red flag.

### Negative / cautionary final action matrix

| IC Action label | Required evidence | Allowed artifact | Action Box | Status treatment |
|---|---|---|---:|---|
| Hard Avoid | Strong disqualifying evidence; not merely missing data. | `final_investment_memo.md` when IC can support the final warning; otherwise specialist warning or Evidence Gap Memo. | Yes only in final memo | Complete for cautionary / negative action, or Blocked if evidence is insufficient. |
| Defer / Not Actionable | Enough evidence to conclude readiness is insufficient, or decision-critical gates are absent. | `final_investment_memo.md` for a final readiness decision; `limited_ic_draft.md` / `decision_prep_memo.md` when still preliminary or scoped. | Yes only in final memo | Complete for readiness decision, or Limited / Blocked when evidence is still incomplete. |
| Watchlist | Supported thesis or quality plus missing trigger, price, catalyst, risk resolution, or implementation readiness. | `final_investment_memo.md` for final IC Watchlist; non-final artifacts when gates are incomplete. | Yes only in final memo | Complete for Watchlist decision when evidence is sufficient; otherwise Limited. |
| Maintain / Hold | Existing-position context plus sufficient evidence for continuing exposure under stated horizon. | `final_investment_memo.md`; scenario-only discussion if no position context exists. | Yes only in final memo | Complete when position context and gates are sufficient; otherwise Limited / scenario-only. |

## 5. Core report schemas

### Evidence pack

Artifact: `evidence_pack.md`

Required sections:
1. Evidence summary.
2. Source inventory.
3. Material claim support map.
4. Freshness map.
5. Missing data and access limitations.
6. Proxy evidence and caveats.
7. Contradictions.
8. Readiness matrix by downstream agent.
9. Pre-IC evidence lock, when applicable.

### Equity company analysis

Artifact: `equity_company_analysis.md`

Required sections:
1. Short view.
2. What the company does.
3. How the company makes money.
4. Why customers buy.
5. Revenue and margin durability.
6. Why the company can win.
7. Where the company can lose.
8. Management quality.
9. Financial read-through.
10. Thesis dependencies.
11. What would change the view.
12. Monitoring triggers.
13. Structured handoff.

### Financial statement analysis

Artifact: `financial_statement_analysis.md`

Required sections:
1. Financial quality summary.
2. Revenue quality.
3. Margin structure.
4. Cash flow and FCF conversion.
5. Balance sheet and liquidity.
6. Working capital.
7. Share count / dilution / capital allocation.
8. Accounting quality and red flags.
9. Handoff to Equity, Valuation, Risk, and IC.

### ETF analysis

Artifact: `etf_analysis.md`

Required sections:
1. ETF identity.
2. Intended use case.
3. Exposure diagnosis.
4. Holdings and concentration.
5. Index / methodology / active process.
6. Cost, AUM, liquidity, and structure.
7. Performance and risk history.
8. Yield and distributions, if relevant.
9. Peer comparison and overlap, if relevant.
10. Special vehicle risks.
11. Vehicle Quality Verdict.
12. Structured handoff.

### Fixed income analysis

Artifact: `fixed_income_analysis.md`

Required sections:
1. Instrument identity.
2. Yield, spread, and carry.
3. Duration, curve, and convexity.
4. Credit / issuer / obligor quality.
5. Liquidity and structure.
6. Call, prepayment, extension, and covenant risks.
7. Downside scenario.
8. Compensation verdict.
9. Structured handoff.

### Commodity analysis

Artifact: `commodity_analysis.md`

Required sections:
1. Executive view.
2. Commodity identity and instrument context.
3. Demand map.
4. Supply map.
5. Inventories / reserves / trade flows.
6. Futures curve / roll / carry.
7. Macro sensitivity.
8. Geopolitics and policy.
9. Logistics / storage / transport.
10. Cost curve / marginal cost.
11. Substitution risk.
12. Valuation context.
13. Specialist verdict and actionability label.
14. Monitoring triggers and handoff.

### Crypto analysis

Artifact: `crypto_analysis.md`

Required sections:
1. Executive view.
2. Asset identity and classification.
3. Investment-grade viability gate.
4. Core thesis and anti-thesis.
5. Network economics / value accrual.
6. Real adoption quality.
7. Tokenomics / value capture.
8. Market structure and liquidity.
9. Macro / liquidity transmission.
10. Regulation.
11. Security / custody / protocol risk.
12. Team / roadmap / governance.
13. Valuation / implied expectations.
14. Specialist verdict.
15. Monitoring and handoff.

### Valuation & expectations

Artifact: `valuation_expectations.md`

Required sections:
1. Valuation summary.
2. What is priced in.
3. Current valuation snapshot.
4. Absolute and quality-adjusted valuation.
5. Primary and supporting methods.
6. Scenario-implied valuation range.
7. Return bridge.
8. Margin of safety and asymmetry.
9. Valuation risks.
10. What must be true.
11. Monitoring signals.
12. Handoff to Risk and IC.

### Risk / Red Team

Artifact: `risk_red_team.md`

Required sections:
1. Risk executive summary.
2. Core thesis under attack.
3. Critical assumptions map.
4. Thesis failure map.
5. Bear case challenge.
6. Mandatory risk gates.
7. Risk watchlist.
8. Tail risks.
9. Excluded / deprioritized risks.
10. Priority challenge requests.
11. Handoff to IC.

### News & catalysts

Artifact: `news_catalysts.md`

Required sections:
1. Material recent events.
2. Active carryover events.
3. Upcoming catalyst map.
4. Negative news check.
5. Event status and source confidence.
6. Price / thesis relevance.
7. Handoff.

### Market positioning

Artifact: `market_positioning.md`

Required sections:
1. Positioning summary.
2. What the market appears to believe.
3. What is already priced in.
4. Crowding / neglect.
5. Event bar / revision momentum.
6. Positioning risk or opportunity.
7. Handoff.

### Macro sensitivity

Artifact: `macro_sensitivity.md`

Required sections:
1. Material macro drivers.
2. Growth / inflation / rates / liquidity / FX sensitivity.
3. Cross-asset confirmation.
4. Freshness and data caveats.
5. Thesis relevance.
6. Handoff.

### Portfolio fit

Artifact: `portfolio_fit.md`

Required sections:
1. Generic role fit.
2. User-specific fit, if portfolio context exists.
3. Existing exposure / overlap.
4. Risk, liquidity, volatility, concentration, FX, tax caveats where relevant.
5. Monitoring burden.
6. Handoff to IC.

### Sector and discovery reports

Artifacts:
- `sector_industry_memo.md`
- `sector_investment_map.md`
- `sector_monitoring_plan.md`
- `structural_winners_memo.md`
- `candidate_watchlist.md`

Required logic:
- Outputs may identify attractive directions or candidates.
- Outputs must not make final investment actions.
- Candidate-to-asset handoff is required before actionability.

## 6. Investment Committee report schemas

### Complete Final Memo

```yaml
contract_type: Report
status: Canonical
artifact: final_investment_memo.md
owner: Investment Committee Agent
used_by:
  - Financial Agent System final decision-support workflows
produces:
  - reader-facing Complete Final Memo
consumes:
  - intake_context
  - evidence_pack_with_pre_ic_lock
  - lead_asset_or_theme_analysis
  - valuation_expectations_report_when_relevant
  - risk_red_team_report_when_final_action_requested
  - material_specialist_reports
  - implementation_vehicle_quality_when_material
evidence_required: true
decision_boundary: May issue Investment View and IC Action only when gates permit; no exact trade instruction or unsupported facts.
status_values:
  - Complete
known_gaps:
  - none
```

#### When to use

Use when the user requests final IC-level decision support and required evidence, valuation, risk, lead analysis, material modules, and implementation checks are sufficient for the stated scope.

#### What you get

A layered decision memo with Action Box, integrated thesis, gate status, evidence limits, risks, valuation, monitoring, and view-change triggers.

#### What it will not do

It will not expose raw agent transcripts, provide exact allocation/trade instructions, hide material conflicts, or issue positive action when gates are incomplete.

#### Required metadata

- Subject:
- Request type:
- Workflow:
- Produced by: Investment Committee Agent
- As-of date/time:
- Output status: Complete
- Evidence status:
- Analysis Status:
- IC Action Status:
- Source scope:
- Freshness status:
- Time Horizon / N/A:
- Decision Confidence / Not Rateable:
- Key limitations:
- Included / Excluded Modules and Why:
- Decision boundary:
- Downstream handoff:

#### Required sections

1. Action Box.
2. Freshness top block, when freshness is material.
3. Investment View.
4. IC Action.
5. Why this action, not the alternatives.
6. What matters most.
7. Core thesis.
8. Key assumptions.
9. Included / Excluded Modules and Why.
10. Evidence synthesis and limitations.
11. Evidence / Specialist Conflict, if material.
12. Valuation and expectations.
13. Risks and thesis breakers.
14. Catalysts / timing / positioning / macro where material.
15. Portfolio fit where relevant.
16. Monitoring plan.
17. What would change the view.
18. Evidence & Data Quality Appendix when limitations affect the conclusion.
19. Follow-up requests if any residual non-blocking limitations remain.

#### Optional sections

- Plain-English Take when the user requests simple explanation.
- Prior memo delta-update block when updating an available prior memo.
- Audit Trail appendix only when explicitly requested.

#### Handoff block

```text
Downstream relevance:
Required follow-up:
Decision constraints:
Monitoring owner / cadence:
Evidence refresh needed:
Next review trigger:
```
#### Status and failure rules

- Complete when required IC gates are sufficient for the stated scope.
- Limited when useful synthesis is possible but material limitations constrain conclusion strength; use a non-final artifact unless the user requested a blocked/limited IC response explicitly.
- Blocked when decision-critical evidence or upstream work is missing or unreliable enough that the requested conclusion must not be made.
- Preliminary when the user requests a Quick Take or early read before full workflow completion; do not use `final_investment_memo.md`.

### Limited IC Draft

```yaml
contract_type: Report
status: Canonical
artifact: limited_ic_draft.md
owner: Investment Committee Agent
used_by:
  - scoped or incomplete final-decision workflows
produces:
  - reader-facing Limited IC Draft
consumes:
  - available_evidence_and_specialist_inputs
evidence_required: true
decision_boundary: Useful IC synthesis under explicit limits; no positive final IC Action.
status_values:
  - Limited
known_gaps:
  - none
```

#### When to use

Use when the user asks for IC-level synthesis but one or more material gates, source scopes, freshness checks, or specialist modules are incomplete and the available work still supports useful bounded analysis.

#### What you get

A decision-oriented limited IC synthesis with a Decision-Prep Box, visible scope limits, missing gates, current conclusions, scenario framing when needed, and follow-up required for final IC Action.

#### What it will not do

It will not use Action Box, issue positive final IC Action, hide excluded workflow blocks, or convert missing information into a final recommendation.

#### Required metadata

- Subject:
- Request type:
- Workflow:
- Produced by: Investment Committee Agent
- As-of date/time:
- Output status: Limited
- Evidence status:
- Analysis Status: Limited
- IC Action Status: Limited / Blocked
- Source scope:
- Freshness status:
- Time Horizon / N/A:
- Decision Confidence / Not Rateable:
- Key limitations:
- Included / Excluded Modules and Why:
- Decision boundary:
- Downstream handoff:

#### Required sections

1. Decision-Prep Box.
2. Scope and excluded gates.
3. Preliminary / Limited View.
4. What can be concluded now.
5. Missing gates and why they matter.
6. Evidence, freshness, and source limitations.
7. Conflicts or unresolved assumptions.
8. Scenario matrix when decision mode or user context is missing.
9. Needed for final IC Action.
10. Structured handoff / follow-up requests.

#### Optional sections

- General Portfolio Fit when personal portfolio context is unavailable.
- Prior memo delta-update block when a prior memo is available.
- Evidence & Data Quality Appendix when limitations are material.

#### Handoff block

```text
Downstream relevance:
Required follow-up:
Decision constraints:
Missing gates:
Evidence / freshness refresh needed:
Maximum allowed status before follow-up:
```

#### Status and failure rules

- Limited when the available analysis is useful but constrained by missing gates, source scope, freshness, conflicts, or excluded modules.
- Blocked when missing or unreliable information prevents even a bounded IC view; use `evidence_gap_memo.md` instead.
- Complete is not allowed for this artifact.
- Positive final IC Action is prohibited.

### Decision-Prep Memo

```yaml
contract_type: Report
status: Canonical
artifact: decision_prep_memo.md
owner: Investment Committee Agent
used_by:
  - preliminary decision-preparation workflows
produces:
  - reader-facing Decision-Prep Memo
consumes:
  - available_context_and_partial_workflow_outputs
evidence_required: true
decision_boundary: Prepares decision work; no final IC Action.
status_values:
  - Preliminary
  - Limited
known_gaps:
  - none
```

#### When to use

Use for early IC-level preparation, Quick Takes that need IC framing, or staged workflows where the user wants practical next-step guidance before final gates are complete.

#### What you get

A concise preparation memo with current working view, IC Action Status, evidence/freshness/source limits, missing gates, decision-mode assumptions, and the minimum work required to reach a Complete Final Memo.

#### What it will not do

It will not use Action Box, present a final IC Action, provide exact sizing/trade instructions, or imply current-market action when freshness is missing.

#### Required metadata

- Subject:
- Request type:
- Workflow:
- Produced by: Investment Committee Agent
- As-of date/time:
- Output status: Preliminary / Limited
- Evidence status:
- Analysis Status: Preliminary / Limited
- IC Action Status: Limited / Blocked
- Source scope:
- Freshness status:
- Decision mode assumptions:
- Time Horizon / N/A:
- Decision Confidence / Not Rateable:
- Key limitations:
- Included / Excluded Modules and Why:
- Decision boundary:
- Downstream handoff:

#### Required sections

1. Decision-Prep Box.
2. Decision mode and assumptions.
3. Current working view.
4. Evidence status, source scope, and freshness status.
5. Gate checklist.
6. Main uncertainties.
7. Most important next evidence or specialist work.
8. What would upgrade this to a Complete Final Memo.
9. Structured handoff / follow-up requests.

#### Optional sections

- Scenario matrix for new buyer / existing holder / add / trim / exit.
- General Portfolio Fit checklist.
- Fresh-data refresh checklist.

#### Handoff block

```text
Downstream relevance:
Required follow-up:
Decision constraints:
Minimum evidence needed:
Specialist modules needed:
Current-action limitation:
```

#### Status and failure rules

- Preliminary when the memo is an early read or Quick Take before full workflow completion.
- Limited when available evidence supports a bounded preparation view but material gates remain incomplete.
- Blocked when decision-critical evidence is missing; use `evidence_gap_memo.md` if the main output is a gap explanation.
- Complete and final positive IC Action are not allowed for this artifact.

### Evidence Gap Memo

```yaml
contract_type: Report
status: Canonical
artifact: evidence_gap_memo.md
owner: Investment Committee Agent
used_by:
  - blocked or evidence-constrained IC workflows
produces:
  - reader-facing Evidence Gap Memo
consumes:
  - evidence_pack_or_available_source_scope
evidence_required: true
decision_boundary: Explains why the requested IC conclusion is Limited or Blocked; no final positive action.
status_values:
  - Limited
  - Blocked
known_gaps:
  - none
```

#### When to use

Use when the requested IC conclusion cannot be made because decision-critical evidence, freshness, source access, provenance, or upstream work is missing, contradictory, stale, or unreliable.

#### What you get

A focused explanation of what blocks the decision, why it matters, the impact on Analysis Status and IC Action Status, and the minimum evidence or workflow needed to proceed.

#### What it will not do

It will not synthesize a final positive action, use Action Box, fill evidence gaps with assumptions, or treat user-provided / scoped sources as sufficient without provenance and sanity checks.

#### Required metadata

- Subject:
- Request type:
- Workflow:
- Produced by: Investment Committee Agent
- As-of date/time:
- Output status: Limited / Blocked
- Evidence status:
- Analysis Status: Limited / Blocked
- IC Action Status: Limited / Blocked
- Source scope:
- Freshness status:
- Time Horizon / N/A:
- Decision Confidence / Not Rateable:
- Key limitations:
- Blocking issues:
- Included / Excluded Modules and Why:
- Decision boundary:
- Downstream handoff:

#### Required sections

1. Decision-Prep Box with Limited or Blocked status, as applicable.
2. Requested conclusion.
3. Missing or unreliable evidence.
4. Source scope and freshness limits.
5. Impact on Analysis Status.
6. Impact on IC Action Status.
7. Minimum evidence needed to proceed.
8. Suggested follow-up workflow.
9. Structured handoff / evidence request.

#### Optional sections

- Evidence Conflict block when sources disagree.
- Public-data view when premium/private data is unavailable.
- User-file provenance and sanity-check notes.

#### Handoff block

```text
Downstream relevance:
Required follow-up:
Decision constraints:
Blocking evidence gaps:
Resolution standard:
Allowed interim output:
```

#### Status and failure rules

- Limited when some bounded analysis is possible but the requested conclusion is constrained.
- Blocked when the requested conclusion must not be made until required evidence or upstream work is available.
- Complete and positive final IC Action are not allowed for this artifact.
- `Hard Avoid` is allowed only through a final IC memo when strong disqualifying evidence exists; missing information alone remains Defer / Not Actionable or Blocked.
### Prior memo delta update

Use this block when updating an available prior memo:

```text
Prior View:
What Changed:
What Did Not Change:
Thesis Impact:
Action Impact:
Evidence / Gate Refresh Needed:
```

If the prior memo is unavailable, the output must state that it is a fresh analysis, not a true update of the prior memo.

### What Would Change the View

The block must be as concrete as evidence allows without inventing pseudo-precision.

```text
Monitoring Triggers:
Action / View-Change Triggers:
More positive if:
More negative if:
Threshold basis: explicit metric / directional / qualitative
```

## 7. P8-IC-01 approved edge-case behavior

| Rule ID | Case | Canonical IC report-schema behavior |
|---|---|---|
| P8-IC-01-01 | User requests final memo before required gates are complete. | Produce `limited_ic_draft.md`, `decision_prep_memo.md`, or `evidence_gap_memo.md`; do not present it as a Complete Final Memo. |
| P8-IC-01-02 | Non-final IC output needs a top summary. | Use `Decision-Prep Box`; `Action Box` is reserved for `final_investment_memo.md`. |
| P8-IC-01-03 | User asks for a short investment answer. | Provide Quick Take / Preliminary framing and no final IC Action unless gates are complete. |
| P8-IC-01-04 | Request depends on today / now / latest / earnings / price action and fresh data are missing. | Separate structural view from current-action view; current IC Action Status is Limited or Blocked. |
| P8-IC-01-05 | Evidence or specialists conflict on a material claim. | Show `Evidence / Specialist Conflict` in the main memo and constrain status if decision-critical. |
| P8-IC-01-06 | Decision mode is unspecified. | Use scenario matrix; do not assume new buy. |
| P8-IC-01-07 | User asks for personal decision without portfolio context. | Provide general scenario-based Portfolio Fit and request minimum context; no personalized final action. |
| P8-IC-01-08 | User wants a short readable final memo. | Use layered memo: decision summary, main memo, risks/triggers, appendices. |
| P8-IC-01-09 | User restricts workflow or source scope. | Respect scope, label artifact as Limited / source-scope constrained, and list prohibited conclusions. |
| P8-IC-01-10 | Strong disqualifying evidence appears before all positive gates. | IC may issue `Hard Avoid` only with strong disqualifier; missing data alone uses `Defer / Not Actionable`. |
| P8-IC-01-11 | User asks exact sizing, allocation, or trade instruction. | Provide only illustrative ranges or scenario constraints; no exact instruction. |
| P8-IC-01-12 | Specialist or asset report sounds like final recommendation. | Non-IC reports may use scoped verdicts only, with `Boundary: Not an IC Action`; no IC Action labels or Action Box. |
| P8-IC-01-13 | Workflow has many optional modules. | Use materiality-based modules and show `Included / Excluded Modules and Why`. |
| P8-IC-01-14 | Memo can become stale after publication. | Show As-of date/time and Freshness status near the top. |
| P8-IC-01-15 | Final action wording could drift. | Use controlled IC Action labels only. |
| P8-IC-01-16 | Watchlist, Defer, and Hold could be confused. | Distinguish them by user meaning: existing-position hold, trigger-based watchlist, or insufficient-readiness defer. |
| P8-IC-01-17 | Confidence could be read as price forecast certainty. | Define Decision Confidence as support for conclusion and include evidence reason. |
| P8-IC-01-18 | View-change triggers could be vague or pseudo-precise. | Use concrete triggers where evidence supports them; otherwise mark directional or qualitative basis. |
| P8-IC-01-19 | User asks to update a prior memo. | Use delta-update when prior memo is available; otherwise label output as fresh analysis, not a true update. |
| P8-IC-01-20 | User wants all details. | Keep main memo decision-oriented; put details in appendices and avoid raw transcript unless explicitly requested as audit material. |

## 8. Output standards inherited from master rules

All report schemas inherit these standards from `implementation/00-master-rules.md`:

- Decision Confidence must be included for final memos and major specialist verdicts.
- Final IC memos may include an Action Box only when the output is an IC-level final memo.
- Non-final IC outputs use `Decision-Prep Box` and gate-aware artifact names.
- User-facing source display should separate reader layer, verification layer, and appendix layer.
- Evidence & Data Quality Appendix is required when limitations affect the conclusion.
- Freshness must be stated for market-sensitive conclusions.
- Reports must use professional investment-writing style and avoid internal agent transcripts.
- Exact trade instructions and exact position sizing are prohibited.
