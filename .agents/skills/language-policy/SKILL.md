---
name: language-policy
description: Use for Russian user-facing answers, Russian-target reports, English-to-Russian translation, mixed English/Russian cleanup, and Russian financial/market/business text where unnecessary English or Run-glish should be removed while preserving allowed names, tickers, official titles, code, paths, and technical identifiers.
---

# Language Policy

This is a presentation-layer repo skill for the Financial Agent System. It implements `implementation/14-language-and-style.md` for Russian user-facing output.

If this skill conflicts with `implementation/14-language-and-style.md`, `implementation/00-master-rules.md`, or another canonical implementation document, the canonical document governs.

## Purpose

Produce natural Russian user-facing text, not mixed Russian-English text, when the target output is Russian.

Use strict Russian mode by default: translate a word or phrase when it can be expressed naturally and accurately in Russian.

This skill is not an analytical method. It must not issue `IC Action`, use `Action Box`, add facts, add sources, add caveats, add conclusions, add recommendations, add investment calls, add risk warnings, collect evidence, decide routing, or replace analytical method skills, evidence collection, workflow gates, or Investment Committee synthesis.

## When to use

Use this skill when:

- the user writes in Russian and no other output language is explicitly requested;
- the user asks for a Russian report, Russian summary, translation, cleanup, or Russian-target market/financial/business text;
- a user-facing report artifact has `Language: Russian`;
- mixed English/Russian text needs normalization.

Do not announce this skill in ordinary user-facing answers.

## What to preserve

Preserve facts, structure, headings, tables, Markdown, numbers, dates, modality, uncertainty, source attribution, causality, and point of view.

Do not add analysis, facts, sources, caveats, conclusions, recommendations, investment calls, or risk warnings when the task is translation or cleanup.

## Allowed English in Russian output

English may remain only for:

- company, brand, source, product, platform, protocol, and project names: Nvidia, Apple, AWS, Reuters, Bloomberg, Ethereum;
- tickers, indexes, instruments, and standard abbreviations: AAPL, BTC, ETH, S&P 500, Nasdaq Composite, VIX, ETF, IPO, EPS, ARR, EBITDA, GAAP, non-GAAP, FOMC, SEC, API, JSON, SQL;
- official forms, filings, laws, regulations, document or release titles when exactness matters: Form 8-K, 10-Q, S-1, Regulation S-K;
- code, commands, filenames, file paths, URLs, variables, JSON/YAML/SQL keys, API fields, placeholders, and technical identifiers;
- short direct quotes when exact wording matters, with Russian translation when useful.

Translate the surrounding words even when an English name remains.

## Required Russian terminology

Use Russian terms unless context clearly requires otherwise:

- `guidance` -> `прогноз менеджмента` / `прогноз компании`;
- `price action` -> `динамика цен` / `динамика акций` / `динамика индекса`;
- `market reaction` -> `реакция рынка`;
- `investor takeaway` -> `вывод для инвестора`;
- `upside` -> `потенциал роста`;
- `downside` -> `риск снижения` / `потенциал падения`;
- `tailwind` -> `попутный фактор`;
- `headwind` -> `сдерживающий фактор`;
- `bull case` -> `позитивный сценарий`;
- `bear case` -> `негативный сценарий`;
- `earnings` -> `отчётность` / `финансовые результаты`, depending on context;
- `earnings report` -> `отчётность`;
- `earnings per share` -> `прибыль на акцию`;
- `revenue` -> `выручка`;
- `free cash flow` -> `свободный денежный поток`;
- `Treasury yields` -> `доходности казначейских облигаций США`;
- `rate cut` / `rate hike` -> `снижение ставки` / `повышение ставки`.

Avoid hybrids such as `AWS-сделка`, `AI-выручка`, `Fed-релиз`, `Reuters-отчёт`, and `guidance-обновление`. Use `сделка с AWS`, `выручка от ИИ`, `релиз ФРС`, `сообщение Reuters`, and `обновление прогноза`.

## Reports and artifacts

For Russian user-facing report artifacts:

- keep the filename in English when it is a system artifact name;
- keep machine-readable metadata fields in English;
- write reader-facing titles, headings, table labels, captions, and body text in Russian;
- include `Language: Russian` when metadata is present.

## Final check

Before sending Russian output, silently verify:

- no unexplained English remains outside allowed categories;
- headings, labels, and table columns visible to the reader are translated;
- numbers, dates, currencies, percentages, periods, and units are accurate;
- companies, tickers, indexes, forms, URLs, code, paths, and technical identifiers are preserved correctly;
- no awkward English-Russian hybrids remain;
- modality, uncertainty, causality, and evaluation strength were not shifted.
- no facts, sources, caveats, conclusions, recommendations, investment calls, or risk warnings were added.
