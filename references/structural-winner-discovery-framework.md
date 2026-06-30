# Structural Winner Discovery Framework

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: Structural Winners Discovery  
Contributors: Sector & Industry Analysis; Equity Agent; Valuation/Expectations; Risk Red Team  
Used by: Structural Winners Discovery Agent; structural-winner-discovery skill  
Primary reference for: structural-winner discovery framework examples  
Supporting reference for: theme-to-asset handoffs and discovery ranking context  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: Medium  
Last reviewed: 2026-06-28  
Review trigger: Review when discovery workflow, candidate ranking language, or sector-analysis taxonomy changes.  
Owner review needed: No  
Split/index status: Indexed in implementation/reference-library-index.md  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->


## Purpose

This reference supports Structural Winners Discovery analysis. Active agent and skill behavior is governed by `implementation/06-agent-contracts.md` and `implementation/11-skill-contracts.md`.

It provides advisory discovery logic for identifying public companies that may become structural winners inside a theme, industry, value chain, or technology transition. It is a reference framework, not a standalone agent and not a final recommendation engine.

## Core Doctrine

Structural winner discovery is not a search for exciting stories. It is a search for companies that may control economically valuable bottlenecks, scarce capabilities, repeatable demand channels, or value-capture positions while avoiding businesses that only appear exposed to a theme.

Discovery output should remain candidate discovery. A candidate becomes investment-actionable only after the relevant canonical asset-level, evidence, valuation, risk, and IC gates are satisfied where required.

## Structural Winner Tests

### 1. Picks-and-Shovels Test

Ask whether the company supplies mission-critical tools, components, infrastructure, software, services, data, materials, or capacity that many theme participants need.

Positive indicators:

- multiple customer types need the product or service;
- demand is linked to industry capex, adoption, regulation, or infrastructure buildout;
- the company can benefit even if the final end-market winners are uncertain;
- the product is hard to substitute without operational, regulatory, or performance cost.

Common false positives:

- generic supplier with low switching costs;
- commodity input with no pricing power;
- exposure exists but is too small to affect company economics;
- demand is one-off rather than recurring or expanding.

### 2. Bottleneck Control Test

Ask whether the company controls a constraint that slows or enables the broader theme.

Relevant bottlenecks include:

- scarce technical know-how;
- manufacturing capacity;
- certification, qualification, or regulatory approval;
- installed base and service network;
- data access or workflow integration;
- distribution, procurement, or customer trust;
- specialized materials, components, or logistics.

A bottleneck is investment-relevant only if it can translate into revenue durability, margin resilience, pricing power, share gains, or capital efficiency.

### 3. Scarce Capacity Test

Ask whether supply is difficult to replicate quickly.

Scarcity may come from:

- long lead times;
- specialized labor;
- high qualification barriers;
- limited physical assets;
- hard-to-scale manufacturing process;
- exclusive partnerships;
- regulatory licenses;
- accumulated reliability record.

Do not treat scarcity as durable if competitors can add capacity quickly, customers can dual-source easily, or the constraint disappears when demand normalizes.

### 4. Value-Capture Test

Ask who actually captures the economics created by the theme.

A company may benefit from a theme only weakly if:

- it sells into the theme but has no pricing power;
- customers capture most of the value;
- the company must reinvest heavily to keep up;
- revenue grows but margins compress;
- dilution, capex, or working capital absorbs the upside;
- the product is important but commoditized.

Strong value capture normally requires some combination of pricing power, switching costs, differentiated capability, high incremental margins, recurring revenue, or privileged customer access.

### 5. Platform / Ecosystem Logic

Platform-like companies can become structural winners when usage, data, distribution, standards, or workflow integration reinforce the company position over time.

Check for:

- network effects;
- developer, partner, or customer ecosystem;
- expanding attach rate;
- cross-sell or upsell path;
- integration into mission-critical workflows;
- growing data advantage;
- standard-setting role.

Avoid platform language when the company is merely a product vendor without reinforcing adoption loops.

### 6. Smart Customer Demand

Prefer demand from sophisticated customers whose buying behavior validates mission-critical value.

Evidence may include:

- hyperscalers, industrial leaders, governments, utilities, defense primes, hospitals, labs, or other high-standard customers;
- repeat purchases or multi-year commitments;
- qualification wins;
- design wins;
- backlog quality;
- expansion within existing accounts;
- customer willingness to accept long lead times or premium pricing.

Customer logos alone are not enough. The analysis should test scale, recurrence, margin quality, and strategic importance.

### 7. R&D and Long-Term Management

Structural winners often reinvest ahead of visible demand.

Positive evidence:

- sustained R&D or engineering depth;
- product roadmap aligned with customer bottlenecks;
- disciplined capex with credible utilization path;
- management that explains value creation rather than promotion;
- capital allocation that protects long-term competitive position.

Negative evidence:

- promotional theme-chasing;
- serial pivots;
- large acquisitions to buy relevance;
- weak disclosure around segment economics;
- dilution-heavy growth with unclear return on capital.

## Horizon Discipline

Default discovery horizon is 5-10 years. Some infrastructure, industrial, energy, healthcare, defense, and platform transitions may require a 10-15 year horizon. A shorter 3-5 year horizon is acceptable only when adoption, revenue conversion, and evidence are already visible.

The agent should state the horizon explicitly and distinguish:

- near-term evidence;
- medium-term adoption path;
- long-term structural optionality.

## Candidate Classification

Use candidate tiers to prevent story inflation:

- Tier 1: strong structural fit with evidence of value capture and credible public-market relevance;
- Tier 2: plausible beneficiary but with unresolved economics, valuation, or evidence gaps;
- Tier 3: thematic exposure exists but strength or magnitude is uncertain;
- Watch-only: interesting but not yet investable or not enough evidence;
- Rejected: exposure is too weak, commoditized, promotional, structurally impaired, or not public-market actionable.

Tier labels are discovery labels, not buy / sell / hold recommendations.

## False Positives and Traps

Common traps:

- confusing revenue exposure with profit-pool ownership;
- assuming a large TAM creates attractive shareholder returns;
- treating every supplier as a picks-and-shovels winner;
- ignoring cyclicality, capex intensity, working capital, and dilution;
- missing customer bargaining power;
- ignoring competition from larger incumbents;
- overstating scarcity that can be replicated;
- confusing temporary shortage with durable bottleneck;
- treating valuation sanity checks as full valuation;
- calling a candidate "the next NVIDIA" or another historical winner.

## Evidence Requirements

Strong candidate claims should be supported by a mix of:

- company filings and investor materials;
- segment revenue, backlog, order, or capacity evidence where available;
- customer, contract, qualification, or design-win evidence;
- industry structure and value-chain evidence;
- peer comparison;
- margin, ROIC, reinvestment, and balance-sheet context;
- market recognition / crowding evidence when relevant.

If evidence is proxy-only, stale, inaccessible, or narrative-heavy, the candidate tier should be reduced or marked watch-only.

## Handoff Rules

Structural Winner Discovery should recommend downstream work rather than replace it:

- Equity Agent for company-quality analysis;
- Financial Statement Analysis skill for financial quality and resilience;
- Valuation & Expectations Agent for priced-in expectations;
- Risk / Red Team Agent for thesis failure paths;
- Market Positioning Agent for crowding and expectation risk;
- News & Catalysts Agent for event and catalyst checks;
- Investment Committee Agent for any final action decision.

## User-Facing Style

Write in professional investment language. Avoid hype, certainty, and guaranteed-winner phrasing. Candidate discovery should be clear enough for a user to decide which names deserve deeper analysis, not to act as a final investment memo.
