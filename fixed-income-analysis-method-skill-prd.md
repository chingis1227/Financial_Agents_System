# Fixed Income Analysis Method Skill PRD

## Purpose

This skill defines how to analyze fixed income instruments and produce `fixed_income_analysis.md`.

The method is risk-adjusted, downside-first, evidence-aware, source-aware, and horizon-aware.

## Core Method Sequence

## Step 1 - Confirm User Intent

Classify the request as:

- educational;
- full instrument review;
- credit quality check;
- rates / duration risk;
- income / yield trap check;
- bond ETF exposure review;
- comparison / replacement;
- monitoring / update;
- private / structured limited review.

Narrow questions receive narrow answers.

Investment verdicts require decision-grade evidence.

## Step 2 - Identify the Instrument

Determine:

- issuer / fund / obligor;
- instrument type;
- ticker / CUSIP / ISIN where available;
- maturity;
- coupon type;
- currency;
- seniority;
- secured / unsecured status;
- callable / puttable / convertible / inflation-linked / floating-rate status;
- ETF / fund vs individual bond;
- public vs private / opaque instrument.

If the instrument cannot be verified, block the investment-quality verdict.

## Step 3 - Establish Horizon

Identify:

- trading horizon;
- income horizon;
- hold-to-maturity intent;
- liability-matching horizon;
- tactical rates horizon;
- portfolio sleeve horizon.

If missing, state assumptions.

## Step 4 - Set Instrument Mode

Apply the relevant mode:

- Rates / Sovereign;
- Corporate Credit;
- High Yield / Distressed;
- Municipal;
- Inflation-Linked;
- International / EM Debt;
- Floating-Rate / Loan;
- Preferred / Hybrid;
- Convertible;
- Securitized Credit;
- Bond ETF / Fund;
- Private Credit Limited;
- Cash-Equivalent / Liquidity Sleeve.

## Step 5 - Gather Evidence

Collect:

- instrument terms;
- market price and yield;
- spread / OAS where relevant;
- duration / convexity;
- credit ratings;
- issuer financials;
- debt maturity schedule;
- liquidity data;
- fund holdings and yield metrics;
- macro handoff where relevant;
- news / catalyst data where material.

## Step 6 - Apply Freshness Discipline

Decision-critical market data require as-of date / time.

If current price, yield, spread, curve, or NAV data are missing, do not issue a strong current attractiveness verdict.

## Step 7 - Classify Yield Type

Identify and explain:

- yield to maturity;
- yield to worst;
- yield to call;
- SEC yield;
- distribution yield;
- coupon yield;
- real yield;
- tax-equivalent yield;
- spread / OAS.

Do not treat high distribution yield as expected return.

## Step 8 - Analyze Current Market Compensation

Assess whether the yield / spread compensates for:

- duration risk;
- curve risk;
- credit risk;
- expected loss;
- liquidity;
- optionality;
- inflation;
- FX;
- structure;
- reinvestment risk.

## Step 9 - Analyze Duration / Curve / Convexity

Check:

- effective / modified duration;
- maturity;
- key-rate exposure where available;
- curve steepening / flattening sensitivity;
- convexity;
- extension / prepayment risk;
- approximate price impact under rate shocks.

## Step 10 - Analyze Credit Quality

For credit instruments, evaluate:

- issuer quality;
- leverage;
- interest coverage;
- free cash flow;
- liquidity;
- maturity wall;
- refinancing risk;
- rating / outlook / watch;
- seniority;
- collateral;
- covenant context;
- spread vs risk.

## Step 11 - Analyze Liquidity

Assess:

- issue size;
- trading depth;
- bid/ask;
- ETF AUM and volume;
- fund liquidity vs underlying liquidity;
- redemption terms;
- private lock-up;
- market stress behavior.

## Step 12 - Analyze Legal-Economic Structure

Check:

- seniority;
- secured status;
- covenants;
- call / put schedule;
- sinking fund;
- conversion terms;
- coupon deferral;
- collateral;
- tranche structure;
- jurisdiction.

## Step 13 - Analyze Individual Bond vs Fund Economics

For individual bonds, distinguish mark-to-market risk from repayment economics.

For funds, analyze rolling exposure, NAV risk, distribution risk, duration drift, credit drift, and liquidity mismatch.

## Step 14 - Analyze Macro Transmission

Use Macro Agent input for:

- policy path;
- real yields;
- inflation;
- curve regime;
- liquidity;
- credit cycle;
- USD / FX;
- recession risk.

Do not replace Macro Agent's regime view. Challenge contradictions through structured handoff.

## Step 15 - Run Scenario Set

Minimum scenarios:

- rates up;
- rates down;
- curve shift;
- spread widening;
- credit deterioration;
- liquidity stress;
- call / prepayment / extension;
- inflation / real-rate shock;
- FX shock where relevant.

Use bounded scenario math where evidence supports it.

## Step 16 - Compare Alternatives

Compare against relevant alternatives:

- Treasury curve;
- rating / maturity bucket;
- peer bonds;
- bond ETFs;
- money market / bills / CDs;
- IG vs HY;
- TIPS vs nominal bonds;
- muni vs taxable equivalent;
- active vs passive fund;
- cash-like alternatives.

## Step 17 - Run Yield Trap Checklist

Check whether high yield reflects:

- credit stress;
- subordination;
- illiquidity;
- call risk;
- duration risk;
- stale price;
- distressed pricing;
- structural opacity;
- dividend / coupon deferral risk;
- FX or political risk;
- fund distribution artifact.

## Step 18 - Determine Risk / Red Team Need

Escalate complex, asymmetric, opaque, distressed, private, structured, high-yielding, or "safe income" contradiction cases.

## Step 19 - Determine Specialist Verdict

Use controlled verdict labels.

Include:

- rationale;
- primary risk;
- compensation view;
- data confidence;
- what would change the verdict.

## Step 20 - Produce Monitoring Triggers

Generate instrument-specific monitoring triggers.

## Step 21 - Produce Structured Handoffs

Prepare handoffs to:

- Macro;
- ETF;
- Risk / Red Team;
- Portfolio Fit;
- Investment Committee;
- Evidence Collector.

## Step 22 - Silent Pre-Final Check

Before finalizing, verify:

- no final buy / sell / hold language;
- yield is not treated as sufficient;
- data freshness is disclosed;
- individual bond vs fund economics are correct;
- missing data reduces claim strength;
- specialist verdict matches evidence quality;
- required risk escalation is included;
- prohibited safety language is avoided.

## Language

The skill produces Markdown deliverables in English by default.

Chat discussion with the user may be in Russian.

## Relationship to Global Standards

This skill must follow:

- global investment analytical writing style;
- language policy;
- evidence discipline;
- anti-hallucination rules;
- no final action language outside the Investment Committee.

