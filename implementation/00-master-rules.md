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

If sources conflict on a material claim, the output must show `Evidence Conflict` in the main answer, not only in an appendix.

Required fields:

```text
Evidence Conflict:
What conflicts:
Why it matters:
Current treatment:
Impact on Analysis Status:
Impact on IC Action Status:
What would resolve it:
```

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

### Action intent taxonomy

Classify action-oriented requests before deciding whether to answer immediately or ask for context:

| Intent level | Examples | Required behavior |
|---|---|---|
| Personal / final action | "Should I buy?", "What should I do with my position?", "How much should I buy?", "Should I sell my shares?" | If decision-critical personal context is missing, ask the minimum clarifying questions before giving an action-oriented conclusion. Do not substitute silent assumptions. |
| Market action / investment attractiveness | "Is it a buy?", "Is it attractive here?", "Is gold a good setup now?" | A `Quick Take / Preliminary` or `Limited` market view is allowed when evidence supports it, but no final `IC Action` is allowed unless all gates pass. |
| Analysis-only | "Analyze this company", "Value this company only", "What are the risks?", "What changed recently?" | Provide scoped analysis with status, evidence limits, boundary, and missing IC gates where relevant. |

When intent is ambiguous, use the safer level if the wording could reasonably be read as personal action. General analysis may continue with explicit scope limits.

### Fast action requests

If the user asks for a short market-action answer, the system may give `Quick Take / Preliminary` and a cautious preliminary stance, but not final `IC Action`. If the user asks for personal / final action and key context is missing, ask for the minimum missing context first instead of giving an action conclusion.

Required pattern:

```text
Quick Take:
Status: Preliminary
IC Action Status: Limited or Blocked unless required gates pass
Needed for final IC Action:
```

### Missing personal context

If a user asks for personal / final buy/sell/hold/add/trim/exit guidance without decision-critical personal context, ask for only the minimum missing context needed before giving an action-oriented conclusion. The system may still offer to provide a non-personal, non-final analytical overview after the question is answered or if the user explicitly chooses general analysis.

If the request is market action / investment attractiveness rather than personal action, use a `Preliminary` or `Limited` scenario-based answer with visible assumptions and request the minimum context needed for final IC Action.

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

### Layered report rule

Even a full detailed memo must be layered:

1. Action Box only for `final_investment_memo.md`; Decision-Prep Box for non-final IC artifacts.
2. Main decision-oriented analysis.
3. Key risks and what would change the view.
4. Evidence, valuation, risk, specialist summaries, and assumptions in appendices.

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

Canonical final memo artifact: `final_investment_memo.md`.

`investment_committee_memo.md` is allowed as a legacy alias only when migrating older source documents; new schemas and workflows should use `final_investment_memo.md`.

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

Canonical implementation documents are source of truth. Legacy PRDs, drafts, old architecture maps, backups, archives, and audits are supporting or excluded according to `implementation/01-documentation-control.md` and cannot override canonical rules. If conflict exists, canonical wins.

## 11. Approved edge-case behavior table

Stable IDs in this table are used for QA traceability. If a rule changes, update both the detailed rule section and the matching QA row.

| Rule ID | # | Case | Canonical behavior |
|---|---:|---|---|
| P1-RULE-01-01 | 1 | Analysis partly ready but final action unavailable | Use separate `Analysis Status` and `IC Action Status`. |
| P1-RULE-01-02 | 2 | Personal buy/sell/hold without personal context | Ask the minimum missing context before giving an action-oriented conclusion; market-action questions may receive Preliminary/Limited scenario views. |
| P1-RULE-01-03 | 3 | Fresh data unavailable or stale | Give structural/scenario analysis only; block or limit current action. |
| P1-RULE-01-04 | 4 | Sources conflict | Show `Evidence Conflict`; constrain status if material. |
| P1-RULE-01-05 | 5 | User asks for one-line action | For market action, give Quick Take / Preliminary, not final IC Action; for personal final action with missing context, ask first. |
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
| P1-RULE-01-29 | 29 | Many artifacts confuse final output | `final_investment_memo.md` is canonical final; supporting artifacts need metadata. |
| P1-RULE-01-30 | 30 | Legacy/draft/backup used as source of truth | Canonical docs win; legacy is supporting/excluded by registry. |
