# Canonical Architecture — Financial Agent System

Status: Canonical implementation architecture

Rule authority: statuses, decision labels, positive-action gate, confidence, source display, writing style, and artifact naming are governed by `implementation/00-master-rules.md`.

## 1. System model

The Financial Agent System is an agents-first investment-analysis system. It turns user requests into structured, evidence-aware investment analysis through routing, evidence control, specialist analysis, and final synthesis.

Core flow:

```text
User request
→ Intake / Routing
→ Evidence plan and collection
→ Lead asset / theme / specialist workflow
→ Supporting specialist reports
→ Evidence readiness / pre-IC lock
→ Investment Committee synthesis, when an investment decision is requested
→ Final user-facing memo or Limited/Blocked output
```

## 2. Component categories

| Category | Components | Responsibility |
|---|---|---|
| Router / Intake Agents | Master Intake Router, Asset Intake Router, Theme / Opportunity Intake Router | Classify request, select workflow, identify context, prevent premature conclusions. |
| Evidence Layer | Evidence Collector, Evidence Collection Skill, Evidence Pack, Source Registry | Control source quality, freshness, claim support, missing data, readiness, and evidence lock. |
| Asset-Class Lead Agents | Equity, ETF, Fixed Income, Commodity, Crypto | Own asset-specific analysis and specialist verdicts. They do not own final IC action. |
| Theme / Discovery Agents | Sector & Industry Analysis, Structural Winners Discovery | Map sectors/themes and discover candidates. They do not make candidates investment-actionable. |
| Specialist Agents | Valuation, Risk / Red Team, News & Catalysts, Market Positioning, Macro, Portfolio Fit, Market Sense, Market Intelligence | Add cross-functional context and constraints. They cannot override Evidence or IC. |
| Skills | Domain methods and analysis procedures | Execute repeatable analytical methods inside an agent or workflow. |
| Frameworks / References | Playbooks, maps, source frameworks, pattern libraries | Support analysis; they are not runtime decision owners. |
| Investment Committee Agent | Final synthesis agent | Produces final decision-support memo when required gates are satisfied. |

## 3. Owner / contributor rule

Each analytical block has exactly one owner. Other agents may contribute context, challenges, or handoff inputs, but they do not silently take over the owner’s decision boundary.

Examples:
- Evidence Collector owns readiness, not valuation or investment view.
- Valuation owns valuation / expectations analysis, not final action.
- Risk / Red Team owns thesis failure analysis, not hidden recommendation.
- Portfolio Fit owns role/suitability context, not buy/sell action.
- Investment Committee owns final synthesis, not raw evidence gathering.

## 4. Orchestration and handoff rule

Agents do not freely call each other or create hidden peer conversations. Handoffs are workflow-controlled.

Allowed handoff forms:
- Structured handoff block inside a report.
- Evidence request or readiness challenge through the evidence protocol.
- Workflow-defined downstream dependency.
- IC synthesis consuming completed reports.

Disallowed behavior:
- A specialist issuing final buy/sell/hold action outside IC.
- An agent silently overriding Evidence Collector readiness.
- IC inventing unsupported facts.
- Reference documents acting as hidden agents.

## 5. Standard statuses

| Status | Meaning |
|---|---|
| Complete | Required inputs are sufficient for the stated scope. |
| Limited | Analysis can proceed, but material limitations constrain conclusion strength. |
| Blocked | Required information is missing or unreliable enough that the output must not make the requested conclusion. |
| Preliminary | Narrow or early output allowed before full workflow completion; cannot be treated as final decision support. |

Specialized labels such as `Complete Risk Review` or `Limited Valuation` are allowed when they map back to these base statuses.

## 6. Decision labels

| Label | Owner | Use |
|---|---|---|
| Specialist Verdict | Asset-class agents and specialists | Domain-specific analytical conclusion. Not final IC action. |
| Actionability Label | Domain owner where explicitly defined, including asset-class, specialist, or discovery agents | Indicates setup quality or required next step, but not final allocation or IC action. |
| Vehicle Quality Verdict | ETF and similar vehicle analysis | Wrapper/vehicle quality assessment. Not final portfolio action. |
| Investment View | Investment Committee | Final synthesized view for the memo. |
| IC Action | Investment Committee | Decision-support action label such as Initiate, Add, Maintain / Hold, Trim, Exit, Watchlist, Defer / Not Actionable, or Hard Avoid. |

## 7. Positive action gate

No positive IC action may be issued unless the following are sufficient for the requested decision:

1. Evidence readiness.
2. Valuation / expectations work, where price or capital allocation is decision-relevant.
3. Risk / Red Team review, where thesis risk or downside matters.
4. Lead asset/theme analysis.
5. Material specialist reports where relevant.

If any required gate is missing, the output must be Limited or Blocked and include follow-up requirements.

## 8. Approved edge-case architecture behavior

These rules define the owner / contributor model in common ambiguous cases. They are canonical architecture behavior for implementation.

### 8.1 Fast answers, personal context, and final action

| Case | Required behavior |
|---|---|
| User asks for buy / sell / hold immediately. | The system may provide a fast Preliminary / Quick Take, but final `IC Action` belongs only to the Investment Committee after required gates. |
| User omits horizon, objective, risk tolerance, or position context. | Provide a bounded preliminary answer with explicit assumptions, or ask only the minimum clarifying question needed. Do not issue final `IC Action` until decision-critical context is sufficient. |
| User asks for personal decision support. | The system may provide personalized decision-support using supplied context, but must not issue exact trade instructions or exact position sizing as a final instruction. Label the mode, such as Asset Analysis, Portfolio Fit, or IC Decision Support. |
| User asks for a fast answer even though a full decision is needed. | Provide `Quick Take / Preliminary` only, and offer Full IC Memo for final decision support. |
| User asks for an update to a prior memo. | Use a delta-update: prior view, what changed, what did not change, thesis impact, and new status. If the prior memo is unavailable, request it or perform fresh analysis. Material changes require renewed IC review. |

### 8.2 Evidence, freshness, and unavailable data

| Case | Required behavior |
|---|---|
| Current data is required. | Attempt to obtain current evidence by default. If unavailable, structural analysis may proceed, but action-oriented conclusions must be Limited or Blocked. |
| Sources conflict. | Apply source hierarchy, show material `Evidence Conflict`, and constrain the conclusion. IC may continue only if it explains why the conflict does not break the thesis. |
| Premium, private, or paywalled data is material. | Produce a Public-data view where useful, mark the limitation, provide a Premium-data checklist, and keep final action Limited or Blocked when the missing data is decision-critical. |
| Evidence Collector blocks readiness. | Final IC memo and positive action are blocked. Non-decision work such as frameworks, scenarios, preliminary analysis, and checklists may continue with clear limitations. |
| News, rumors, and market reaction are mixed. | Separate confirmed, unconfirmed, and market-implied claims. Rumors may be mentioned but not treated as facts. Market reaction analysis should compare the asset, peers, sector, and broader market where relevant. |

### 8.3 Agent ownership and conflict resolution

| Case | Required behavior |
|---|---|
| User directly calls a specialist. | Direct specialist calls are allowed, but the specialist stays inside scope, states boundaries, and cannot issue final `IC Action`. Missing inputs produce Preliminary, Limited, or Blocked status. |
| Specialist and lead asset views disagree. | IC resolves the synthesis and must show material disagreement. Lead agents and specialists do not silently override each other. |
| Risk review is negative. | Risk Agent does not own final veto, but can create a gate failure if downside, risk controls, or thesis failure modes are insufficiently bounded. |
| Evidence readiness fails. | Evidence Collector owns readiness and can block final decision support. IC cannot override failed evidence readiness by inventing facts. |
| Multiple agents contribute to one workflow. | Each analytical block has one owner. Contributors may add context, challenges, constraints, or handoff notes, but do not take over the owner boundary. |

### 8.4 Asset, theme, comparison, and portfolio behavior

| Case | Required behavior |
|---|---|
| Request compares multiple asset classes. | Relevant asset-class lead agents own their own analysis. The user receives a scenario-based comparison; final cross-asset action requires IC synthesis. |
| Theme / discovery request produces candidates. | Discovery may rank candidates and assign Actionability Labels as analysis priorities, not buy / sell recommendations. Candidates become actionable only through asset-level workflow and IC. |
| Portfolio Fit is requested but portfolio data is missing. | Provide generic fit by investor scenario with explicit assumptions, plus a data checklist. Do not give final personalized portfolio fit without portfolio context. |
| Request may be new buy, hold, add, trim, or exit. | Distinguish these actions. If position context is missing, provide a scenario matrix or ask for position size, entry price, and portfolio weight before final personal decision support. |
| User asks for the "best" asset without defining "best". | Use standard criteria and scenario winners by default, and require objective clarification before final IC Action. |

### 8.5 Valuation, time horizon, and implementation

| Case | Required behavior |
|---|---|
| Asset does not support classic valuation. | Use the asset-class valuation equivalent or expectations analysis. Assets without cash flows require stronger risk review before positive action. |
| Business / theme quality is high but price is expensive. | Separate quality verdict from investment view. Positive action requires valuation / expectations support. Non-IC agents may flag Watchlist / Defer as next-step signals; final Watchlist / Defer IC Action belongs to IC. |
| Time horizon is ambiguous. | Separate short-term and long-term views. Short-term uses market sense, news, positioning, and event context; long-term uses thesis, valuation, risk, and portfolio fit. Final IC Action must include Time Horizon. |
| Idea is attractive but implementation is poor. | Positive action requires implementation check. Weak liquidity, vehicle quality, custody, spreads, fees, or accessibility can limit the output to Watchlist / Defer and should trigger alternative implementation suggestions. |
| User wants all details. | Final memo remains decision-oriented and readable. Detailed evidence, specialist summaries, assumptions, and deep dives belong in appendices or follow-up sections, not raw agent transcripts. |

## 9. Product vs architecture source split

- `prd.md` remains a product-level draft source. It should not resolve detailed architecture conflicts.
- `system-architecture-map.md` remains a legacy architecture draft source. It is superseded by this canonical architecture where conflicts exist.
- Canonical implementation documents define active build behavior.
