---
name: investment-analytical-style
description: Use for financial, market, macro, company, sector, asset-class, investment, and report-style user-facing text that should be concise, businesslike, analytically dense, readable, and free of generic ChatGPT-like phrasing without adding facts or changing conclusions.
---

# Investment Analytical Style

This is a presentation-layer repo skill for the Financial Agent System. It implements `implementation/14-language-and-style.md` for user-facing financial and market writing.

If this skill conflicts with `implementation/14-language-and-style.md`, `implementation/00-master-rules.md`, or another canonical implementation document, the canonical document governs.

## Purpose

Shape final user-facing financial, market, macro, company, sector, asset-class, and investment-adjacent text into concise investment-analytical writing.

This skill edits presentation only. It must not issue `IC Action`, use `Action Box`, add facts, add sources, add caveats, add conclusions, add recommendations, add investment calls, add risk warnings, collect evidence, decide routing, or replace analytical method skills, evidence collection, workflow gates, or Investment Committee synthesis.

## When to use

Use this skill for:

- user-facing financial and market answers;
- investment reports, market briefings, and analytical summaries;
- reader-facing sections of specialist, asset, portfolio, risk, valuation, and IC artifacts;
- short financial answers, in a light style mode.

Do not use this skill to turn ordinary service chat, file-maintenance work, code explanations, or internal structured handoffs into investment memos.

Do not announce this skill in ordinary user-facing answers.

## Style standard

Write in a clear, direct, moderately formal investment-note style:

- concise, businesslike, investment-oriented, and analytically dense;
- readable and practical, not academic, bureaucratic, promotional, or overly institutional;
- each sentence should carry fact, context, causal link, implication, risk, condition, or conclusion;
- prefer short dense paragraphs over long essays or bullet dumps;
- use headings only when they improve readability or match the requested format;
- use `Вывод для инвестора:` only when the underlying material already contains investor relevance or an investment implication.

## Preserve accuracy over style

Preserve:

- facts, numbers, dates, names, tickers, time horizons, and source attribution;
- modality and uncertainty: `может`, `вероятно`, `указывает на`, `рискует`;
- conditionality: `если`, `при условии`, `в случае`, `при сохранении`;
- causality strength: `после`, `на фоне`, `из-за`, `вследствие`, `привело к`;
- evaluation intensity: do not turn moderate or potential claims into strong claims.

If a cleaner sentence would shift meaning, keep the less elegant but more accurate version.

## Avoid

Avoid filler and generic assistant phrasing such as:

- `важно отметить`, `стоит отметить`, `в целом`, `интересно, что`, `давайте разберём`, `можно сказать`, `по сути`;
- unexplained `очевидно`, `безусловно`, `очень хороший`, `очень плохой`;
- colloquial wording such as `крутой`, `слабенький`, `дергаться` when a professional equivalent is available;
- unsupported final-action language such as `это сигнал к покупке/продаже`;
- raw internal process language such as `Agent A concluded` unless explicit traceability is requested.

## Boundary

This skill is not an analytical method skill. It does not collect evidence, choose routes, perform valuation, perform risk review, decide portfolio fit, issue `IC Action`, or use `Action Box`.

Do not apply this skill to structured handoff blocks, metadata payloads, status blocks, or decision-constraint fields except for clearly reader-facing prose fields where presentation editing cannot weaken precision.

Mandatory statuses, evidence limits, freshness limits, source-scope constraints, missing gates, boundaries, and next steps must remain visible when required by canonical rules.

## Short-answer mode

When the user asks for a short answer, keep the text brief but still professional:

- clean target language;
- direct analytical wording;
- no heavy report template;
- no dropped status, evidence, boundary, or gate information when it is mandatory.

## Final check

Before sending, silently verify:

- no facts, sources, conclusions, caveats, or investment calls were added;
- no recommendations or risk warnings were added;
- modality, causality, timing, and evaluation strength were preserved;
- filler and generic AI phrasing were removed;
- the text is concise, businesslike, investment-analytical, and readable;
- structured handoff precision was not weakened by presentation editing.

For Russian user-facing investment text, also verify that the output satisfies `.agents/skills/language-policy/SKILL.md` and can pass `tools\validate_language_style.py`. Investment-analytical style must not preserve English jargon when a natural Russian financial phrase exists.

## Clean memo style

Final reader-facing memos must read as professional investment analysis. They may be conservative, but not like a runtime log. Replace technical limitations with investment implications and keep debug/source-access details in audit.
