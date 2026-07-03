# Language and Style Presentation Layer

Status: Canonical language-and-style authority

## 1. Purpose

This document governs user-facing language selection, Russian-language cleanup, and investment-analytical presentation style for the Financial Agent System.

It is a presentation-layer authority. It does not replace evidence collection, source discipline, routing, agent ownership, skill method contracts, Investment Committee gates, report schemas, or final action boundaries.

Master output standards, statuses, gates, confidence, source display, and artifact naming remain governed by `implementation/00-master-rules.md`. Documentation registry and source precedence remain governed by `implementation/01-documentation-control.md`.

## 2. Language defaults

Use two separate language categories:

| Output type | Default language |
|---|---|
| Internal project documentation, canonical implementation documents, custom-agent TOML, repo-skill files, workflow/runbook files, README, and project-control Markdown | English unless explicitly requested otherwise. |
| User-facing chat answers, analytical summaries, investment reports, market briefings, and generated user-facing report artifacts | Language of the user's request unless the user explicitly requests another language. |

A Russian user request produces a Russian user-facing answer and Russian user-facing report content by default. User-facing Markdown reports are not treated as internal project documentation merely because they are saved as `.md` files.

Explicit language instructions override the request language:

- Russian request plus `in English`, `English report`, or equivalent -> English user-facing output.
- English request plus `на русском`, `русский отчёт`, or equivalent -> Russian user-facing output.
- `bilingual` / `двуязычно` -> bilingual output only for the requested scope.
- Mixed-language request -> use the explicitly requested target language; if none is specified, use the dominant user-request language.

## 3. Artifact language convention

For generated user-facing report artifacts:

- file names remain English for system stability, for example `final_investment_memo.md` or `limited_ic_draft.md`;
- machine-readable metadata fields remain English, for example `Artifact Type`, `Language`, `Analysis Status`, and `IC Action Status`;
- reader-facing title, headings, table labels, captions, and body text use the target output language;
- include `Language: Russian` or another target-language metadata value when the artifact content is not English.

## 4. Russian language policy

When the target output is Russian, apply strict Russian-language mode:

- write natural Russian, not mixed Russian-English text;
- translate generic financial, market, business, legal, and analytical terms when a clear Russian equivalent exists;
- translate reader-facing headings, table columns, labels, captions, and link text;
- avoid English-Russian hybrids such as `AWS-сделка`, `AI-выручка`, `Fed-релиз`, `Reuters-отчёт`, or `guidance-обновление`;
- preserve modality, uncertainty, numbers, dates, causality, and source attribution.

English may remain in Russian output only when it is required for precision or identity:

- company, brand, product, platform, protocol, source, and media names, such as Nvidia, Apple, AWS, Reuters, Bloomberg, Ethereum;
- tickers, instruments, indexes, and standard market abbreviations, such as AAPL, BTC, ETH, S&P 500, Nasdaq Composite, VIX, ETF, IPO, EPS, ARR, EBITDA, GAAP, non-GAAP, FOMC, SEC, API, JSON, and SQL;
- official filing, form, law, regulation, document, or release names when exactness matters, such as Form 8-K, 10-Q, S-1, or Regulation S-K;
- code, commands, filenames, file paths, URLs, variables, JSON/YAML/SQL keys, API fields, and technical identifiers;
- short direct quotes when exact wording matters, paired with Russian translation when useful.

Preferred Russian renderings include:

| English term | Russian rendering |
|---|---|
| guidance | прогноз менеджмента / прогноз компании |
| price action | динамика цен / динамика акций / динамика индекса |
| market reaction | реакция рынка |
| investor takeaway | вывод для инвестора |
| upside | потенциал роста |
| downside | риск снижения / потенциал падения |
| tailwind | попутный фактор |
| headwind | сдерживающий фактор |
| bull case | позитивный сценарий |
| bear case | негативный сценарий |
| earnings | отчётность / финансовые результаты, depending on context |
| earnings report | отчётность |
| earnings per share | прибыль на акцию |
| revenue | выручка |
| free cash flow | свободный денежный поток |
| Treasury yields | доходности казначейских облигаций США |
| rate cut / rate hike | снижение ставки / повышение ставки |

Source names may remain in English, but source statements should be rendered in Russian. Example: `Reuters reported that Nvidia raised guidance` becomes `Reuters сообщило, что Nvidia повысила прогноз менеджмента`.

Do not write the final Russian answer by drafting an English answer and translating it mechanically. Use English-language sources as evidence material and write the final user-facing text directly in natural Russian.

## 5. Investment-analytical style

Apply investment-analytical style to financial, market, investment, macro, company, sector, asset-class, and report-style user-facing outputs.

The style should be concise, businesslike, investment-oriented, analytically dense, and readable. Prefer paragraphs where each sentence carries fact, context, causal link, market relevance, risk, condition, or conclusion.

Use this style for:

- user-facing financial and market answers;
- specialist summaries intended for the user;
- market briefings and updates;
- user-facing investment reports and IC-facing reader sections;
- reader-facing conclusions, thesis summaries, risk sections, and monitoring triggers.

Do not use this style to:

- add facts, sources, caveats, conclusions, recommendations, investment calls, or risk warnings;
- override evidence status, freshness limits, missing gates, or IC boundaries;
- polish structured handoff blocks so heavily that status, evidence, limits, or decision constraints become less precise;
- turn ordinary service chat, file-maintenance discussion, or code tasks into investment memos.

For short answers, apply a light version: clean Russian or the requested language, direct analytical phrasing, no heavy memo template, and no unnecessary headings.

## 6. Presentation skills

The project uses two repo-scoped presentation skills as runtime adapters:

- `.agents/skills/language-policy/SKILL.md` for Russian language policy, translation, and Russian-target cleanup;
- `.agents/skills/investment-analytical-style/SKILL.md` for concise investment-analytical writing style.

These are presentation skills, not domain-analysis methods. They do not issue `IC Action`, use `Action Box`, collect evidence, decide routing, add facts, add sources, add caveats, add conclusions, add recommendations, add investment calls, add risk warnings, or replace asset, specialist, evidence, valuation, risk, portfolio, or Investment Committee workflows.

Former user-level global skill files may be used as source material during migration, but the project-owned runtime adapters and this canonical document govern project behavior. Do not make canonical project behavior depend on machine-specific absolute paths.

## 7. Quality checks

Before sending or saving Russian user-facing output, verify silently that:

- no unexplained English remains outside allowed categories;
- generic headings, table columns, labels, captions, and link text are translated;
- companies, tickers, indexes, official forms, URLs, code, file paths, and technical identifiers are preserved correctly;
- no awkward English-Russian hybrids remain;
- numbers, currencies, dates, percentages, periods, and units are accurate;
- modality, uncertainty, causality, timing, and evaluation strength are not shifted;
- the final text is concise, businesslike, investment-analytical when the subject is financial or market-related;
- mandatory statuses, boundaries, source limits, evidence limits, and missing IC gates remain visible where required.

For project validation, the same behavior is enforced by `tools\validate_language_style.py` and the fixture set `tests/behavior/language_style_cases.yaml`. Any change to Russian user-facing language policy, allowed English terms, forbidden Run-glish phrases, or investment-analytical presentation rules must update both the canonical rule and the validator fixtures.

The validator must reject generic untranslated investment jargon in Russian reports when a natural Russian phrase exists. Examples that must not pass in Russian reader-facing investment output include `growth exposure`, `headline earnings`, `profit pools`, `customer wins`, `customer-level exposure`, `downside-модель`, `upside/downside`, and English-Russian hybrids such as `HBM-конкуренция` when the meaning can be written naturally as `конкуренция в HBM`.

## 8. Stable behavior IDs

| Rule ID | Behavior |
|---|---|
| P14-LANG-01 | Russian user request produces Russian user-facing answer/report unless the user explicitly requests another language. |
| P14-LANG-02 | Internal project and runtime-control documents remain English by default. |
| P14-LANG-03 | User-facing Markdown reports may be Russian even when file names and metadata remain English. |
| P14-LANG-04 | Russian output uses strict Russian-language mode and avoids Run-glish. |
| P14-LANG-05 | English remains only for allowed identity, instrument, official-title, code, path, URL, and technical cases. |
| P14-LANG-06 | Financial and market user-facing outputs use concise investment-analytical style. |
| P14-LANG-07 | Presentation skills do not add facts, evidence, sources, conclusions, caveats, recommendations, investment calls, or risk warnings. |
| P14-LANG-08 | Structured handoffs preserve precision and are not rewritten into reader-style prose when that would weaken status or constraints. |
| P14-LANG-09 | Short answers use light style without dropping mandatory status, evidence, boundary, or gate information. |
| P14-LANG-10 | Explicit language switches such as `English report`, `русский отчёт`, and `bilingual` override default language detection. |


## Mandatory investment report presentation gate

Every user-facing investment report, investment memo, saved `investment_report.md`, direct investment summary, and IC-facing reader memo must pass the presentation layer before completion. For Russian output this always means `.agents/skills/language-policy/SKILL.md`; for all investment report prose this always means `.agents/skills/investment-analytical-style/SKILL.md`. This requirement is unconditional and does not depend on route, asset class, workflow mode, report length, or whether the user explicitly asked for language cleanup.
