# Fixed Income Instrument Playbooks

## Purpose

This file defines instrument-specific fixed income analysis playbooks.

The general Fixed Income Agent framework applies to all instruments. These playbooks determine which risks, sources, metrics, and traps matter most by instrument type.

## General Playbook Template

Each playbook should define:

- instrument identity;
- primary return drivers;
- required evidence;
- key metrics;
- common traps;
- scenario focus;
- preferred sources;
- handoffs;
- monitoring triggers.

## 1. Rates / Sovereign Bonds

### Coverage

Treasuries, Bunds, Gilts, JGBs, developed-market sovereign bonds, sovereign bond ETFs.

### Core Drivers

- nominal yield;
- real yield;
- inflation expectations;
- central bank path;
- curve shape;
- term premium;
- duration;
- fiscal credibility;
- currency for non-domestic sovereigns.

### Common Traps

- treating low default risk as low total risk;
- ignoring duration risk;
- assuming rates-down is always bullish without recession context;
- ignoring inflation / real return;
- treating long-duration bond ETFs as cash-like.

### Scenario Focus

- parallel rate shock;
- steepening / flattening;
- inflation surprise;
- real yield rise;
- recession rally vs inflation selloff.

### Handoffs

Macro for policy, inflation, real yields, and curve regime.

Portfolio Fit for ballast / hedge role.

## 2. Corporate Investment Grade

### Core Drivers

- Treasury yield;
- credit spread;
- issuer quality;
- leverage;
- interest coverage;
- maturity wall;
- sector cyclicality;
- liquidity;
- rating outlook;
- refinancing cost.

### Common Traps

- investment grade does not mean low total risk;
- long-duration IG can behave like rates exposure;
- spread may not compensate for downgrade risk;
- issuer fundamentals may deteriorate before ratings move.

### Scenario Focus

- rates up;
- spread widening;
- downgrade;
- refinancing pressure;
- liquidity stress.

## 3. High Yield / Distressed Credit

### Core Drivers

- spread compensation;
- default risk;
- recovery value;
- maturity wall;
- refinancing access;
- liquidity;
- covenant protection;
- sector stress;
- issuer-specific catalysts.

### Common Traps

- high coupon mistaken for attractive income;
- yield driven by distress;
- stale or illiquid pricing;
- weak recovery position;
- equity-like downside.

### Required Escalation

Risk / Red Team normally required.

## 4. Municipal Bonds

### Core Drivers

- tax-equivalent yield framework;
- issuer / obligor;
- general obligation vs revenue bond;
- fiscal health;
- revenue source;
- pension / debt burden;
- call features;
- rating / outlook;
- tax status;
- liquidity.

### Common Traps

- saying tax-free without caveats;
- ignoring AMT / state / account type;
- ignoring call risk;
- treating all munis as government-like;
- ignoring revenue-bond project risk.

### Handoff

Portfolio Fit and tax-aware caveat. No personalized tax advice.

## 5. Inflation-Linked Bonds / TIPS

### Core Drivers

- real yield;
- breakeven inflation;
- inflation carry;
- duration;
- indexation mechanics;
- deflation floor where applicable;
- tax treatment caveat.

### Common Traps

- assuming TIPS always win in inflation;
- ignoring real-yield duration losses;
- confusing nominal return with real return;
- ignoring fund duration.

### Handoff

Macro for inflation regime and real-yield context.

## 6. International / EM Debt

### Core Drivers

- hard currency vs local currency;
- sovereign balance sheet;
- reserves;
- external funding;
- current account;
- fiscal position;
- policy credibility;
- FX risk;
- political / sanctions risk;
- capital controls;
- legal jurisdiction;
- global USD liquidity.

### Common Traps

- higher yield as simple carry;
- ignoring FX loss;
- ignoring capital controls;
- ignoring legal jurisdiction;
- treating sovereign and corporate risk as identical.

### Handoff

Macro for USD, global liquidity, policy, and FX regime.

Risk / Red Team for political, default, capital-control, or sanctions risk.

## 7. Floating-Rate Notes / Bank Loans

### Core Drivers

- base rate;
- spread margin;
- reset frequency;
- floor;
- credit quality;
- leverage;
- covenant package;
- senior secured status;
- loan liquidity;
- refinancing;
- fund liquidity mismatch.

### Common Traps

- low rate duration does not mean low risk;
- income falls when base rates fall;
- loan funds may have liquidity mismatch;
- covenant-lite structures reduce protection.

## 8. Preferreds / Hybrid Capital

### Core Drivers

- subordination;
- coupon / dividend deferral;
- cumulative vs non-cumulative;
- call / reset structure;
- issuer capital;
- regulatory capital treatment;
- common equity buffer;
- liquidity;
- spread vs senior debt.

### Common Traps

- preferred yield is not senior bond yield;
- coupon can be deferred or cancelled;
- call assumptions can be wrong;
- equity-like downside in stress.

### Escalation

Risk / Red Team for AT1 / CoCo / loss-absorbing instruments.

## 9. Convertible Bonds

### Core Drivers

- issuer credit;
- bond floor;
- conversion price;
- conversion ratio;
- equity sensitivity;
- premium to conversion value;
- maturity;
- call features;
- coupon;
- option value;
- liquidity.

### Common Traps

- analyzing convertibles as plain bonds;
- ignoring equity downside;
- ignoring busted-convertible risk;
- ignoring dilution / settlement mechanics.

### Handoff

Equity Agent where equity thesis materially drives value.

## 10. Securitized Credit

### Coverage

MBS, ABS, CMBS, CLOs, structured credit ETFs / funds.

### Core Drivers

- collateral pool;
- tranche seniority;
- credit enhancement;
- prepayment risk;
- extension risk;
- servicer / manager quality;
- rating migration;
- liquidity;
- structural transparency.

### Common Traps

- treating structured yield as plain credit spread;
- ignoring tranche waterfall;
- ignoring prepayment / extension;
- relying on rating alone;
- analyzing without collateral data.

### Required Evidence

Offering / collateral / tranche data are required for decision-grade verdict.

Without them, output is Limited or Blocked.

## 11. Private Credit Limited Mode

### Coverage

Private credit funds, direct loans, unitranche, mezzanine, BDC-like exposure where relevant.

### Core Drivers

- borrower / sponsor;
- leverage;
- coverage;
- covenant package;
- collateral;
- seniority;
- maturity;
- base-rate sensitivity;
- valuation marks;
- liquidity lock-up;
- fees;
- PIK / amendment risk;
- manager quality.

### Common Traps

- smoothing of marks;
- opaque borrower data;
- illiquidity underestimated;
- covenants weaker than expected;
- yield from leverage and illiquidity mistaken for safety.

### Rule

No decision-grade private credit attractiveness verdict without sufficient documents.

## 12. Bond ETFs / Bond Funds

### Core Drivers

- underlying duration;
- yield type;
- credit distribution;
- maturity distribution;
- sector / issuer concentration;
- expense ratio;
- tracking;
- NAV premium / discount;
- fund liquidity;
- underlying liquidity;
- distribution stability;
- duration / credit drift.

### Common Traps

- treating fund as individual bond;
- using distribution yield as expected return;
- ignoring NAV volatility;
- ignoring liquidity mismatch;
- ignoring holdings drift.

### Handoff

ETF Agent owns wrapper. Fixed Income Agent owns underlying exposure.

## 13. Cash-Equivalent / Liquidity Sleeve

### Coverage

T-bills, short-term Treasuries, CDs, money market funds, ultra-short bond funds, short-duration ETFs, floating-rate cash alternatives.

### Core Drivers

- principal stability;
- maturity / WAM;
- credit exposure;
- deposit insurance caveat where relevant;
- NAV stability;
- liquidity;
- redemption terms;
- yield type;
- reinvestment risk;
- expense ratio;
- tax caveat.

### Common Traps

- cash-like yield mistaken for cash-equivalent safety;
- ultra-short funds hiding credit risk;
- floating-rate funds hiding credit / liquidity risk;
- CDs confused with marketable bonds;
- yield advantage too small for added risk.

## Monitoring Trigger Map

### Rates / Sovereigns

- yield level;
- real yield;
- breakevens;
- curve steepening / flattening;
- central bank repricing.

### Corporate IG / HY

- spread widening;
- downgrade / watch;
- leverage deterioration;
- FCF decline;
- maturity wall;
- refinancing cost;
- covenant breach.

### Bond ETFs

- duration drift;
- credit-quality drift;
- NAV discount;
- AUM decline;
- liquidity deterioration;
- distribution cut.

### Munis

- rating / outlook change;
- fiscal stress;
- revenue weakness;
- call / refunding event;
- tax-status issue.

### TIPS

- real yield move;
- breakeven move;
- inflation surprise;
- duration loss.

### EM Debt

- FX depreciation;
- reserves decline;
- sovereign spread widening;
- capital controls;
- political / sanctions risk.

### Loans / FRNs

- base-rate cuts;
- issuer deterioration;
- covenant-lite stress;
- refinancing risk;
- loan liquidity.

### Preferreds / Hybrids

- call / reset event;
- coupon deferral risk;
- capital stress;
- regulatory change.

### Structured Credit

- collateral deterioration;
- tranche downgrade;
- prepayment / extension shift;
- liquidity freeze.

### Private Credit

- NAV markdown;
- covenant amendment;
- PIK toggle;
- liquidity gate;
- disclosure deterioration.

### Cash-Like

- NAV instability;
- credit exposure creep;
- liquidity restriction;
- yield falling below alternatives;
- loss of guarantee / insurance condition.

