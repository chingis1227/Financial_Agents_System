# Theme / Opportunity Intake Router PRD

## 1. Purpose

The Theme / Opportunity Intake Router handles requests that begin from a theme, narrative, event, sector, industry, macro shift, structural change, or opportunity area rather than a single asset.

Its purpose is to clarify the investment angle, select the correct opportunity or sector route, and prevent theme-first requests from becoming unsupported buy / sell recommendations.

## 2. Core Question

```text
Is the user asking for a theme map, investable candidates, structural winners, sector analysis, thesis testing, or thematic monitoring?
```

## 3. Primary Responsibilities

The Theme / Opportunity Intake Router owns:

- theme-first request clarification;
- selection between opportunity discovery, structural winners discovery, sector / industry analysis, thematic ranking, thesis testing, and monitoring;
- asking up to 3 relevant theme-intake questions;
- defining the investment universe;
- preserving missing context;
- creating a theme-level intake block;
- preventing premature final investment recommendations.

## 4. Non-Responsibilities

The Theme / Opportunity Intake Router does not:

- issue final buy / sell recommendations;
- perform full asset-level analysis;
- rank assets as final investments without asset-level evidence;
- perform full valuation or risk review for each candidate;
- automatically launch full company deep dives without user approval.

## 5. Theme-First Default

Theme-first requests default to opportunity discovery, not immediate buy / sell recommendations.

The default logic:

```text
theme -> transmission channels -> value chain -> beneficiaries / losers -> investable instruments -> candidate shortlist -> recommended deep dives
```

## 6. Contextual Intake Rule

The router asks up to 3 relevant questions when needed.

Possible theme intake questions:

```text
1. Which instruments should be considered: stocks, ETFs, commodities, crypto, bonds, or all?
2. Which geography or market should be prioritized?
3. What horizon matters most?
4. Do you want a broad opportunity map or focused candidate shortlist?
5. How much risk is acceptable?
6. Are there existing candidate assets to include?
```

Do not ask questions already answered by the user.

## 7. Main Theme Routes

| User Intent | Route | Output | Limitation |
|---|---|---|---|
| “Where can I invest in this theme?” | Opportunity discovery | Opportunity discovery memo | No final buy / sell |
| “Best ideas in this theme” | Thematic ranking | Ranked candidate list | Not full deep dives |
| “Future winners / next X” | Structural winners discovery | Structural winners memo | Requires later asset analysis |
| “Analyze this industry” | Sector / industry analysis | Sector or industry report | Not final asset decision |
| “Check my theme thesis” | Thesis testing | Thesis validation note | May recommend next routes |
| “What should I monitor?” | Thematic monitoring | Monitoring plan | Needs thesis clarity |
| “Theme + specific asset” | Mixed route via Asset Router | Asset analysis with theme lens | Not full theme discovery unless requested |
| “Theme vs theme” | Thematic comparison | Comparison memo | Not final asset allocation |

## 8. Opportunity Discovery Route

Use when the user asks where to invest in a broad theme, event, or narrative.

Examples:

```text
“AI power demand is increasing — where can I invest?”
“Defense spending is rising — what are the opportunities?”
“Nuclear renaissance investment opportunities.”
```

The output should include:

- theme overview;
- transmission channels;
- value chain;
- likely beneficiaries and losers;
- investable instruments;
- candidate shortlist;
- recommended next deep dives.

It must not issue final buy / sell recommendations.

## 9. Thematic Ranking Route

Use when the user asks for top ideas inside a theme.

Examples:

```text
“Top 5 stocks for AI power.”
“Best ETFs for uranium.”
“Most interesting companies benefiting from electrification.”
```

The route should produce a ranked candidate list based on:

- exposure purity;
- business or asset quality;
- valuation sanity check;
- liquidity;
- risk;
- strength of link to the theme;
- next analysis required.

The ranking is a prioritization for further work, not a final investment decision.

## 10. Structural Winners Discovery Route

Use when the user asks for:

- future winners;
- next [known winner];
- hidden beneficiaries;
- picks-and-shovels beneficiaries;
- structural winners;
- long-term compounding candidates inside a theme.

Examples:

```text
“Find future winners in robotics.”
“Who could be the next Vertiv?”
“Find hidden beneficiaries of grid expansion.”
```

This route should use the Structural Winners Discovery Agent and method.

Output:

```text
structural_winners_memo.md
candidate_watchlist.md
```

It does not produce final buy / sell recommendations.

## 11. Sector / Industry Route

Use when the user asks to analyze an industry, sector, ecosystem, or value chain.

Examples:

```text
“Analyze the data center cooling industry.”
“Analyze defense electronics as a sector.”
“Map the nuclear energy value chain.”
```

The route should produce sector or industry analysis covering:

- market structure;
- value chain;
- profit pools;
- growth drivers;
- cyclicality;
- competition;
- public-market investability;
- risks;
- monitoring indicators;
- recommended handoffs.

If the user asks “where can I invest?”, use opportunity discovery instead.

## 12. Sector vs Opportunity Boundary

Sector / industry analysis explains structure, economics, profit pools, competition, and investability.

Opportunity discovery translates a theme or sector into candidate instruments.

If the user asks “analyze the industry,” use sector / industry analysis.

If the user asks “where can I invest,” use opportunity discovery.

## 13. Mixed Theme + Asset Requests

If the user names a specific asset plus a theme, the main route is asset-first.

Example:

```text
“Analyze Lockheed Martin as a beneficiary of rising defense budgets.”
```

The theme becomes an analytical lens.

The system should:

- analyze the specific asset;
- test whether the theme supports the thesis;
- briefly check whether there may be better ways to express the theme;
- recommend full opportunity discovery only if useful.

Do not automatically launch full theme discovery.

## 14. Thesis Testing Route

Use when the user brings a theme-level thesis.

Examples:

```text
“Data centers will create a power shortage — test this.”
“My uranium thesis depends on underinvestment in supply.”
“Check whether AI power demand is overhyped.”
```

The route should:

- formalize the thesis;
- identify key assumptions;
- identify confirming evidence;
- identify disconfirming evidence;
- identify required next routes;
- distinguish evidence strength from final investment action.

## 15. Thematic Monitoring Route

Use when the user asks what to track.

Examples:

```text
“What should I monitor for the uranium thesis?”
“What signals would break the AI power thesis?”
```

The output should include:

- key indicators;
- confirming signals;
- warning signals;
- thesis-breaker signals;
- data sources;
- update frequency;
- recommended follow-up actions.

## 16. Theme Comparison

Theme vs theme requests should be handled as thematic comparisons.

Examples:

```text
“AI power vs nuclear energy opportunities.”
“Defense stocks vs uranium as a geopolitical hedge.”
```

The output should compare:

- size of opportunity;
- investability;
- time horizon;
- valuation risk;
- crowding;
- cyclicality;
- downside risks;
- best next deep dives.

## 17. Theme-to-Asset Boundary

Theme-first outputs may recommend candidates for deeper work, but they do not validate any candidate as investable on their own.

A candidate becomes investment-actionable only after asset-level evidence, valuation, risk review, and final synthesis.

## 18. Evidence Standard

Theme-first workflows use discovery evidence.

Discovery evidence can support:

- opportunity mapping;
- value-chain analysis;
- candidate discovery;
- prioritization for further research.

It cannot support final asset-level buy / sell decisions without later asset-first decision evidence.

## 19. Freshness Rule

Fresh data is required for theme requests involving:

- recent events;
- policy changes;
- new legislation;
- current market narratives;
- recent commodity shocks;
- latest flows or positioning;
- current opportunity ranking.

Structural or educational sector analysis may use less time-sensitive sources but should still timestamp important data.

## 20. Theme Intake Block

The theme intake block should include:

```text
Original request:
Theme / event / narrative:
Route type:
Desired investment angle:
Instrument universe:
Geography / market:
Horizon:
Risk tolerance:
Existing candidates:
Clarifying questions and answers:
Missing context:
Freshness requirement:
Required modules:
Expected artifacts:
Scope limitations:
```

## 21. Output Discipline

Theme-first outputs should be practical but not overclaim.

They should end with:

- candidate shortlist;
- best next deep dives;
- evidence gaps;
- risks;
- what would change the ranking.

They should not end with final buy / sell instructions unless a later full asset-level workflow is completed.

## 22. Success Criteria

The Theme / Opportunity Intake Router succeeds when:

- the correct theme route is selected;
- the user’s desired investment angle is captured;
- the system avoids premature final recommendations;
- opportunity discovery leads to practical candidates;
- structural-winner searches are routed to the right method;
- sector analysis is separated from candidate search;
- missing evidence and limitations are explicit.

