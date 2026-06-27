# Master Intake Router PRD

## 1. Purpose

The Master Intake Router is the top-level request classification layer for the Financial Agent System.

Its purpose is not to analyze assets, themes, markets, risks, valuation, or portfolios. Its purpose is to understand what the user is asking, classify the request, select the appropriate route, and pass structured intake context to the relevant downstream router, specialist route, or workflow.

The Master Intake Router prevents the system from guessing, over-expanding, launching unnecessary work, or treating a narrow question as a full investment decision.

## 2. Core Question

```text
What type of investment task is the user asking for, and which route should handle it?
```

## 3. Primary Responsibilities

The Master Intake Router owns:

- initial request classification;
- detection of asset-first, theme-first, mixed, direct-specialist, comparison, educational, evidence-check, update, monitoring, portfolio-role, and unclear requests;
- short clarification when the request cannot be routed responsibly;
- creation of a structured intake block;
- selection of the downstream router or direct specialist route;
- prevention of uncontrolled workflow expansion;
- language-mode handling;
- freshness requirement detection;
- blocked / unsafe request handling.

## 4. Non-Responsibilities

The Master Intake Router does not:

- perform investment analysis;
- issue buy / sell / hold recommendations;
- produce valuation conclusions;
- perform risk review;
- gather full evidence;
- write final investment memos;
- independently run specialist agents beyond route selection;
- override Evidence Collector readiness constraints;
- invent missing user intent, missing facts, or missing data.

## 5. Routing Architecture

The system uses an orchestrated hybrid workflow.

```text
Master Intake Router
  -> Asset Intake Router
  -> Theme / Opportunity Intake Router
  -> Direct Specialist Route
  -> Educational Response Route
  -> Evidence Verification Route
  -> Unclear Request Clarification
```

The Master Intake Router classifies the request first. Specialized routers then collect route-specific context and launch the appropriate workflow.

## 6. Main Route Classes

| Request Type | Trigger | Downstream Route |
|---|---|---|
| Asset-first | Specific asset or instrument named | Asset Intake Router |
| Theme-first | Theme, event, narrative, macro shift, or opportunity area | Theme / Opportunity Intake Router |
| Mixed asset + theme | Specific asset plus thematic lens | Asset Intake Router with theme context |
| Direct specialist | User names or clearly requests one analytical lens | Direct specialist route |
| Comparison | User compares assets, themes, sectors, or instruments | Classified by comparison type |
| Market reaction | “Why did it rise / fall?”, “after earnings”, “today” | Market reaction route |
| Evidence / source check | Verify claim, source, fact, or news | Evidence Collector verification mode |
| Educational | Explain concept or method | Educational response route |
| Update | “Update”, “what changed since last time” | Update route |
| Monitoring | “What should I track?”, “watch this thesis” | Monitoring route |
| Portfolio role | “Role in portfolio”, hedge, core / satellite | Portfolio fit route |
| Unclear | Request lacks enough context | Clarification menu |

## 7. Clarification Philosophy

The router should avoid both extremes:

- not enough clarification, causing wrong routing;
- excessive questionnaire behavior, causing friction.

Default rule:

```text
Ask 1-3 relevant questions only when they materially improve routing or analysis quality.
Do not ask standard intake questions mechanically.
If the request is already clear, route immediately.
```

For unclear or underspecified requests, the router should offer a short menu of 2-3 likely routes rather than guessing.

## 8. Language Mode

Default language policy:

```text
Chat with user: Russian by default.
Project documentation and generated Markdown artifacts: English by default.
```

The router should record language mode in the intake block when relevant.

If the user explicitly requests another language, this should be captured as part of intake context.

## 9. Freshness Detection

The router must flag a freshness requirement when the request depends on current or recent information.

Fresh data is mandatory for requests involving:

- today;
- yesterday;
- current price;
- current valuation;
- latest earnings;
- recent news;
- market reaction;
- after earnings;
- after a central bank decision;
- after a regulatory event;
- update / refresh requests;
- “why did it move?” questions.

If freshness is required, downstream agents must use current sources and timestamp the analysis.

## 10. Route Map

| User Intent | Main Route | Output | Key Limitation |
|---|---|---|---|
| “Analyze Nvidia” | Full asset-first workflow | Final investment memo | Requires evidence, valuation, and risk review |
| “Is Nvidia expensive?” | Valuation & expectations route | Valuation report | No final buy / sell action |
| “What are Nvidia’s risks?” | Risk route | Risk / red-team report | Preliminary if thesis or valuation is missing |
| “Why did Nvidia fall today?” | Market reaction route | Market reaction note | Requires fresh data |
| “What changed after earnings?” | Update or market reaction route | Update note | Prior analysis needed for full update |
| “Compare Nvidia and AMD” | Comparison route | Comparative decision note | Not full deep dives unless requested |
| “AI power demand — where invest?” | Theme opportunity route | Opportunity discovery memo | No final buy / sell |
| “Find future winners in robotics” | Structural winners route | Candidate discovery memo | Requires later asset-level analysis |
| “Analyze data center cooling industry” | Sector / industry route | Industry analysis | Not final asset decision |
| “Check my Nvidia thesis” | Thesis testing route | Thesis validation note | May recommend next routes |
| “Is the AI trade crowded?” | Market positioning route | Market positioning note | Crowding must be evidence-graded; data may be limited |
| “What has the market priced into Tesla?” | Valuation or market positioning route by main intent | Valuation or positioning report | No final action without full workflow |
| “Check this claim / source” | Evidence verification route | Verification note | No investment conclusion |
| “Explain duration” | Educational route | Explanation | No asset analysis |
| “What should I buy now?” | Idea search after clarification | Candidate shortlist | Requires horizon, instruments, and risk tolerance |
| “Role of gold in portfolio?” | Portfolio fit route | Portfolio role note | Needs portfolio context for personalization |
| “Should I buy Nvidia?” | Full asset-first workflow | Final memo | Positive action requires valuation + risk review |

## 11. Route Precedence Rule

When a request could fit multiple routes, the router should prioritize the user's main intent.

Default precedence:

1. explicit user instruction;
2. capital action request;
3. asset-specific request;
4. focused analytical lens;
5. theme / opportunity request;
6. educational request.

Examples:

- “Should I buy Nvidia after earnings?” -> full asset workflow with earnings context.
- “Was Nvidia expensive after earnings?” -> valuation route with earnings context.
- “Why did Nvidia fall after earnings?” -> market reaction route.
- “Explain why earnings matter for valuation” -> educational route.

The router should not launch all plausible routes by default. It should select the main route and attach secondary elements as context.

## 12. Comparison Handling

The Master Intake Router first determines the type of comparison.

```text
Asset vs asset -> Asset Intake Router
Theme vs theme -> Theme / Opportunity Intake Router
Asset vs theme -> Mixed route
Sector vs asset -> Mixed route
Multi-asset-class comparison -> Asset Intake Router with multiple asset modules
```

The system should not create a separate Comparison Router at this stage.

## 13. Multi-Task Requests

If a request contains multiple major tasks, the router should split it into stages and ask the user to confirm the order.

Example:

```text
User: Analyze Nvidia, compare it with AMD, and tell me whether to buy.
Recommended sequence:
1. Nvidia asset analysis
2. AMD comparison layer
3. Final decision synthesis
```

Small related tasks may be combined without confirmation.

## 14. Direct Specialist Calls

Direct specialist calls remain scoped.

A direct specialist route:

- does not automatically expand into a full workflow;
- must state what is in scope and out of scope;
- may recommend next handoffs;
- cannot launch those handoffs without user approval unless they are part of an already selected full workflow.

## 15. No Uncontrolled Expansion

The router must not expand a narrow request into a full workflow unless:

- the user explicitly requests a full decision;
- the selected route already includes mandatory downstream steps;
- the user approves the expansion.

Focused requests may recommend next steps, but should not silently launch them.

## 16. Output Format vs Evidence Requirements

If the user explicitly asks for a quick, brief, deep, or highly detailed answer, the router may adapt the output format.

However, format depth does not reduce evidence requirements.

```text
Short format can compress the answer.
It cannot justify unsupported investment actions.
```

For example, “Quickly tell me whether to buy Nvidia” may produce a brief preliminary view, but it must not issue a confident positive action unless valuation, risk review, and evidence readiness requirements are met.

## 17. Agent Communication Rule

Agents communicate through structured artifacts, reports, handoff blocks, evidence requests, and challenge requests.

They should not rely on uncontrolled free-form internal chat.

Every material inter-agent request should be traceable.

## 18. Prior Analysis Lookup

For update, refresh, reassessment, or “what changed” requests, the router should first check whether a prior analysis exists.

If prior analysis exists, route to the update workflow.

If prior analysis does not exist, route to market reaction, event analysis, or fresh full analysis depending on user intent.

Prior analysis should not be overwritten. New updates should create a new work folder and reference the previous analysis.

## 19. Intake Block

The Master Intake Router creates a short structured intake block.

For full workflows, this may become `intake.md`.

For narrow requests, the intake block may be embedded in the specialist report.

Minimum structure:

```text
Original request:
Route classification:
Selected route:
Asset / theme / instrument:
User intent:
Known horizon:
Known portfolio context:
Clarifying questions and answers:
Missing context:
Freshness requirement:
Planned downstream modules:
Scope limitations:
Language mode:
```

## 20. Work Folder and File Saving Rule

For future operating workflows:

- full asset or theme workflows should create a work folder and report artifacts;
- short educational or narrow chat answers should not create files by default;
- direct specialist reports may create files if the output is a substantive report or if the user requests saving.

Recommended full-workflow folder naming:

```text
YYYY-MM-DD_[asset-or-theme]_[route-type]/
```

Examples:

```text
2026-06-26_nvidia_equity_deep_dive/
2026-06-26_gold_commodity_analysis/
2026-06-26_ai_power_opportunity_discovery/
2026-06-26_apple_vs_microsoft_comparison/
```

During system design work, new design files should still be saved only after explicit user approval.

## 21. Safety and Refusal Rules

The router must block or redirect requests that ask for:

- guaranteed returns;
- exact prediction of future price movement;
- fabricated data;
- insider information;
- exact position sizing in workflows that do not own sizing, or without sufficient portfolio-construction context;
- unsupported investment conclusions.

Safe alternatives include:

- scenario analysis;
- risk analysis;
- evidence verification;
- valuation ranges;
- conditions for reassessment;
- list of missing data.

## 22. Routing Status

The router may assign one of the following statuses:

```text
Routed
Routed with Missing Context
Clarification Required
User Approval Required
Blocked as Requested
```

These are routing statuses, not investment conclusions.

## 23. Output Status

The Master Intake Router itself does not assign final investment status.

It may constrain the workflow route, but final output status belongs to the relevant workflow or final owner.

## 24. Success Criteria

The Master Intake Router succeeds when:

- the request is routed correctly;
- unnecessary questions are avoided;
- necessary clarification is requested;
- context is preserved for downstream agents;
- narrow requests remain narrow;
- full workflows are launched only when appropriate;
- current-data requirements are detected;
- unsafe or impossible requests are redirected safely.
