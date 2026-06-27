# Investment Committee and Report Schemas

Status: Canonical synthesis and report-schema contract

## 1. Investment Committee contract

Canonical final memo artifact: `final_investment_memo.md`. Legacy references to `investment_committee_memo.md` should be treated as aliases during migration, not as the preferred new artifact name.

The Investment Committee Agent is the final synthesis and decision-support layer. It is downstream-only.

Required inputs for Complete Final Memo:
- Intake context.
- Evidence pack and pre-IC evidence lock.
- Lead asset or theme analysis.
- Valuation / expectations analysis when price or capital allocation is decision-relevant.
- Risk / Red Team review when final action is requested.
- Material specialist reports where relevant.

Allowed statuses:

| Status | Use |
|---|---|
| Complete Final Memo | Required evidence and decision-gate reports are sufficient. |
| Limited Final Memo | Analysis is useful but constrained by material limitations. |
| Blocked Final Memo | Decision-critical evidence or required upstream work is missing. |

Positive IC actions require sufficient evidence, valuation, and risk review. If those gates are missing, the IC output must be Limited or Blocked.

## 2. Final memo style rules

The memo must be a professional investment memo, not an internal transcript.

Do not write:
- “The Equity Agent said...”
- “The Risk Agent output...”
- “The Evidence Collector believes...”

Write integrated conclusions instead:
- “Business quality is strong, but valuation is the main constraint.”
- “The risk profile is manageable only if margin durability holds.”
- “The setup is not actionable until valuation or catalyst evidence improves.”

## 3. Required report metadata

All report artifacts should include:

```text
Subject:
Request type:
Workflow:
Produced by:
As-of date:
Output status: Complete / Limited / Blocked / Preliminary
Evidence status:
Key limitations:
Downstream handoff:
```

## 4. Core report schemas

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

### Investment Committee memo

Artifact: `final_investment_memo.md`

Required sections:
1. Investment View.
2. IC Action.
3. Why this action, not the alternatives.
4. What matters most.
5. Core thesis.
6. Key assumptions.
7. Evidence synthesis and limitations.
8. Valuation and expectations.
9. Risks and thesis breakers.
10. Catalysts / timing / positioning / macro where material.
11. Portfolio fit where relevant.
12. Monitoring plan.
13. What would change the view.
14. Follow-up requests if Limited or Blocked.

## 5. Output standards inherited from master rules

All report schemas inherit these standards from `implementation/00-master-rules.md`:

- Decision Confidence must be included for final memos and major specialist verdicts.
- Final IC memos should include an Action Box when decision support is requested.
- User-facing source display should separate reader layer, verification layer, and appendix layer.
- Evidence & Data Quality Appendix is required when limitations affect the conclusion.
- Freshness must be stated for market-sensitive conclusions.
- Reports must use professional investment-writing style and avoid internal agent transcripts.
