# Reference Library Cleanup Plan

Status: Canonical reference-governance document

## 1. Purpose

Reference documents support agents and workflows. They must not act as hidden PRDs, hidden agents, or conflicting source-policy documents.

## 2. Reference ownership rules

Each reference should eventually include:

```text
Status: Supporting Reference
Owner: [agent/workflow]
Used by: [agents/skills]
Not responsible for: final decision, evidence readiness, routing, IC action
```

## 3. Keep as supporting references

| Reference group | Documents | Owner / used by |
|---|---|---|
| Asset driver maps | `asset-driver-maps.md` | Market Sense, Driver Dominance, asset agents. |
| Market patterns | `market-pattern-library.md` | Market Sense, Market Intelligence, Positioning. |
| Commodity playbooks | `commodity-family-playbooks.md` | Commodity Agent. |
| Fixed income playbooks | `fixed-income-instrument-playbooks.md` | Fixed Income Agent. |
| Macro references | `macro-block-playbooks.md`, `macro-regime-framework.md`, `macro-sensitivity-framework.md`, `macro-g3-fx-regional-policy-overlay.md`, `macro-expectations-surprise-framework.md`, `macro-indicator-cadence-source-registry.md` | Macro Agent. |
| Source references | `source-registry-framework.md`, domain source overlays | Evidence Collector and relevant domain agents. |
| Market news references | `market-news-source-framework.md`, `market-materiality-filter.md` | Market Intelligence, News & Catalysts, Evidence Collector. |

## 4. Merge rules

When a reference repeats Agent PRD or Method Skill content:

- Move ownership, inputs, outputs, and gates to Agent Contract.
- Move procedural steps to Skill Contract.
- Keep examples, taxonomies, labels, diagnostic questions, and playbook logic in the reference.

## 5. Split rules

Split only when size or mixed ownership creates operational ambiguity.

High-priority split candidate:
- `market-pattern-library.md`

Suggested split:

```text
market-pattern-library.md              # index and usage rules
market-patterns/rates-and-yields.md
market-patterns/equities.md
market-patterns/commodities.md
market-patterns/crypto.md
market-patterns/fx-and-dollar.md
market-patterns/risk-sentiment.md
```

Do not split references just for aesthetics. Split when it improves retrieval, ownership, or conflict prevention.

## 6. Source hierarchy consolidation

Source hierarchy belongs to the Evidence Layer and Source Registry.

Domain references may specify preferred sources and freshness nuances, but they must not downgrade the central evidence standard.

## 7. Acceptance criteria

Reference cleanup is complete when:

- Each reference has owner/used-by metadata.
- Large references have indexes or are split where needed.
- No reference conflicts with canonical agent contracts.
- Source rules point back to Evidence Layer and Source Registry.
