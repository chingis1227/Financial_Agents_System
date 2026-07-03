---
name: evidence-document-parser
description: Extracts evidence records from public HTML, PDF, and raw-text financial documents for Evidence Pack support.
---

# Evidence Document Parser

Runtime status: MVP infrastructure. Canonical source of truth: `implementation/04-evidence-layer.md`.

## Purpose

Turn accessible financial documents into structured evidence records for downstream Evidence Pack support.

## When to use

Use this skill when a workflow is supplied with, or discovers, document evidence such as:

- earnings releases;
- investor-relations presentations;
- annual, interim, or quarterly reports;
- SEC filing HTML;
- PDF fact sheets;
- public news or article pages;
- transcripts or raw text.

## What you get

A parser result with source metadata, text blocks, table-like rows, extracted financial claims, confidence, limitations, and warnings that can be merged into an Evidence Pack.

## What it will not do

It will not provide investment analysis, recommendation language, or final IC synthesis. It is evidence infrastructure only.

## Required canonical documents

Use only the canonical documents needed for the task:

- `implementation/00-master-rules.md`
- `implementation/01-documentation-control.md`
- `implementation/04-evidence-layer.md`
- `implementation/15-documentation-sync-contract.md` when changing parser behavior, tests, or docs

## Step sequence

The parser is an evidence supplier. It:

1. records source metadata, access status, and retrieval time;
2. extracts text blocks and table-like content from HTML, PDF, or raw text;
3. finds financial numeric claims;
4. normalizes value, unit, period, comparison basis, and source location where visible;
5. writes claim-level evidence records that can be merged into an Evidence Pack.

## Output contract

Parser output uses `schema_version: document_parser_result.v1` and includes:

- `source`
- `text_blocks`
- `tables`
- `extracted_claims`
- `warnings`

Minimum claim fields are `claim`, `metric`, `value`, `unit`, `period`, `claim_type`, `source_location`, `support_status`, `confidence`, and `limitations`.

## Guardrails

The parser must not:

- issue `IC Action`;
- provide buy, sell, hold, add, trim, or exit recommendations;
- use paywalled snippets as proof when content is not actually available;
- upgrade weak source tiers beyond the existing evidence hierarchy;
- mix GAAP and non-GAAP / adjusted metrics without labeling the distinction;
- invent missing financial metrics or periods.

If a metric is absent or ambiguous, return `Not Found`, lower confidence, or a limitation instead of guessing.

## Failure states

- `Available`: source was parsed and text was extracted.
- `Partial`: source was reachable but extraction is incomplete.
- `Unsupported`: source format or parser dependency is unavailable, such as scanned PDF or missing `pypdf`.
- `Inaccessible`: source could not be retrieved.
- `Not Found`: expected financial claims were not detected.

## Runtime boundary

This skill maps to local Automation Lab Python infrastructure under:

```text
automation_lab/agent_data/document_parser.py
automation_lab/agent_data/article_parser.py
automation_lab/agent_data/pdf_parser.py
automation_lab/agent_data/financial_claim_extractor.py
automation_lab/agent_data/evidence_pack_merge.py
```

It is not an MCP server, not an OpenAI Agents SDK runtime, and not a specialist agent.

## Evidence Pack integration

Parsed claims become additional claim-support rows with:

```text
Claim
Claim type
Materiality
Source / tier
Source date
Freshness
Support status
Access
Location
Limitation
```

Parser output remains supporting audit/evidence material. Final investment decisions remain gated by the full workflow and Investment Committee synthesis.

## Quality checks

- Parser returns structured source metadata and retrieval time.
- Parser preserves source location where available, including PDF page numbers.
- Ambiguous units, periods, or GAAP/non-GAAP basis lower confidence or add limitations.
- Paywalled/inaccessible content remains pointer-only unless content is actually available.
- Parser tests and required project validators pass after behavior changes.
