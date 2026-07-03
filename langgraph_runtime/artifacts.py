from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

DEFAULT_REPORT_ROOT = Path.home() / "OneDrive" / "Documents" / "Financial Agent Reports"


def default_run_dir(asset_identity: str, now: datetime | None = None) -> Path:
    safe_asset = "".join(ch for ch in asset_identity if ch.isalnum() or ch in (" ", "-", "_", ".")).strip() or "Unknown Asset"
    safe_asset = safe_asset.replace(" ", "_")
    stamp = (now or datetime.now()).strftime("%Y-%m-%d_%H%M%S")
    return DEFAULT_REPORT_ROOT / f"{safe_asset}_{stamp}"


def write_full_workflow_artifacts(state: dict[str, Any]) -> tuple[str, str]:
    output_dir = state.get("output_dir") or ""
    base = Path(output_dir) if output_dir else default_run_dir(str(state.get("asset_identity", "Unknown")))
    audit = base / "audit"
    specialists_dir = audit / "specialists"
    specialists_dir.mkdir(parents=True, exist_ok=True)

    report_path = base / "investment_report.md"
    audit_files = {
        audit / "run_metadata.md": _run_metadata(state),
        audit / "intake.md": _intake(state),
        audit / "sources.md": _sources(state),
        audit / "evidence_plan.md": _dict_doc("Evidence Plan", state.get("evidence_plan", {})),
        audit / "evidence_pack.md": _dict_doc("Evidence Pack", state.get("evidence_pack", {})),
        audit / "materiality_plan.md": _dict_doc("Materiality Gate", state.get("materiality_plan", {})),
        audit / "thesis_spine.md": _dict_doc("Thesis Spine", state.get("thesis_spine", {})),
        audit / "gates.md": _dict_doc("Gate Statuses", state.get("gate_statuses", {})),
        audit / "ic_synthesis.md": _dict_doc("IC Synthesis", state.get("ic_synthesis", {})),
    }
    _write_idempotent(report_path, _investment_report(state))
    for path, content in audit_files.items():
        _write_idempotent(path, content)
    for name, content in sorted((state.get("specialist_outputs") or {}).items()):
        _write_idempotent(specialists_dir / f"{name}.md", content.rstrip() + "\n")
    return str(report_path), str(audit)


def _write_idempotent(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = content if content.endswith("\n") else content + "\n"
    if path.exists() and path.read_text(encoding="utf-8-sig") == normalized:
        return
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(normalized, encoding="utf-8")
    tmp.replace(path)


def _investment_report(state: dict[str, Any]) -> str:
    if _is_russian_report(state):
        return _investment_report_ru(state)
    return _investment_report_en(state)


def _investment_report_en(state: dict[str, Any]) -> str:
    ic = state.get("ic_synthesis") or {}
    asset = state.get("asset_identity", "Unknown")
    prepared = datetime.now().strftime("%Y-%m-%d %H:%M")
    portfolio_context_missing = _portfolio_context_missing(state)
    valuation_status = ((state.get("gate_statuses") or {}).get("valuation") or {}).get("status", "")
    evidence_pack = state.get("evidence_pack") or {}
    lines = [
        f"# Investment report — {asset}",
        f"Prepared: {prepared}",
        "",
        "## Executive summary",
        _reader_summary(state, ic),
        "",
        "## Working view",
        "This is a decision-preparation view, not a final personalized recommendation. A final personal decision would require current source-backed evidence, valuation work, risk review, and portfolio context that are sufficient for the requested decision.",
        "",
        "## Investment View",
        "- Asset / Business Quality: source-backed quality work is still needed before relying on the view.",
        "- Valuation Support: price and expectations must be tested separately from business quality.",
        "- Entry Setup: timing depends on valuation, catalyst, positioning, and risk evidence.",
        "- Portfolio Role: role is described only at the level supported by the context provided.",
        "",
        "## Quality vs Entry",
        "A high-quality asset can still have an unattractive entry setup, and a tactical entry setup does not by itself prove asset quality. This report keeps those views separate.",
        "",
        "## Key Internal Conflicts",
        "- Quality vs Valuation.",
        "- Catalyst vs Crowding.",
        "- Long-term thesis vs Current setup.",
        "- Macro tailwind/headwind vs Asset-specific risk.",
        "- Standalone attractiveness vs Portfolio fit.",
        "",
        "## Key reasons",
        f"- The request was centered on {asset}, so the report keeps the asset-level review separate from personal allocation decisions.",
        "- The available materials identify the evidence, valuation, risk, and portfolio questions that need to be resolved before a final personal decision.",
        "- Detailed checks are retained in the verification package rather than shown as technical mechanics in this reader report.",
        "",
        "## Key risks",
        "- Current market evidence, valuation inputs, and risk metrics should be verified with dated sources before using this as decision support.",
        "- Personal suitability depends on existing exposures, objectives, time horizon, risk tolerance, constraints, and concentration limits.",
    ]
    if evidence_pack.get("freshness_required"):
        lines.append("- Current market or news-sensitive claims require timestamped source refresh before any entry-point conclusion.")
    lines.extend([
        "",
        "## Valuation / expectations summary",
        _valuation_summary(valuation_status),
        "",
        "## Portfolio role",
        _portfolio_role_summary(portfolio_context_missing),
        "",
        "## What Would Change Our Mind",
        "- Positive triggers: stronger source-backed evidence, better valuation support, lower risk asymmetry, or clearer portfolio role.",
        "- Negative triggers: evidence contradiction, valuation deterioration, risk trigger activation, or portfolio concentration/overlap concerns.",
        "",
        "## Monitoring Triggers",
        "- Evidence refresh, valuation update, risk review, catalyst follow-through, positioning/crowding check, and portfolio-overlap review.",
        "",
        "## What would make this personal or final",
        "- Current position, approximate portfolio weight, overlapping exposures, objective, time horizon, risk tolerance, liquidity needs, tax constraints, and any prohibited instruments.",
        "- Dated source evidence for price, valuation, benchmark comparison, historical prices, risk metrics, and material news or filings.",
        "- A completed review showing that valuation, risk, evidence quality, and portfolio role all support the same conclusion.",
        "",
        "## Source note",
        _source_note(evidence_pack),
    ])
    return "\n".join(lines)


def _investment_report_ru(state: dict[str, Any]) -> str:
    ic = state.get("ic_synthesis") or {}
    asset = state.get("asset_identity", "Unknown")
    prepared = datetime.now().strftime("%Y-%m-%d %H:%M")
    portfolio_context_missing = _portfolio_context_missing(state)
    valuation_status = ((state.get("gate_statuses") or {}).get("valuation") or {}).get("status", "")
    evidence_pack = state.get("evidence_pack") or {}
    lines = [
        f"# Инвестиционный отчёт — {asset}",
        f"Подготовлено: {prepared}",
        "",
        "## Краткий вывод",
        _reader_summary_ru(state, ic),
        "",
        "## Рабочий взгляд",
        "Это подготовительный взгляд, а не финальная персональная рекомендация. Для персонального решения нужны актуальные источники, оценка стоимости, проверка рисков и портфельный контекст, достаточные для запрошенного решения.",
        "",
        "## ?????????????? ??????",
        "- ???????? ?????? ??? ???????: ???????? ????? ??????????? ??????????? ?? ????????????? ??????.",
        "- ????????? ?????? ?????????: ???? ? ???????? ????? ????????? ???????? ?? ???????? ??????? ??? ??????.",
        "- ????? ?????: ??????? ?? ?????? ?????????, ?????????????, ???????????????? ? ??????.",
        "- ??????????? ????: ??????????? ?????? ?? ?????? ?????????? ?????????.",
        "",
        "## ???????? ?????? ????? ?????",
        "Качественный актив может иметь слабую точку входа, а тактическая точка входа сама по себе не доказывает качество актива. Отчёт разделяет эти два слоя.",
        "",
        "## ???????? ?????????? ????????????",
        "- ???????? ?????? ?????? ?????????.",
        "- ??????????? ?????? ??????????? ????????????????.",
        "- ???????????? ????? ?????? ??????? ????? ?????.",
        "- ?????-????????? ??? ????????? ????? ?????? ?????????????? ????? ??????.",
        "- ??????????????? ????????????????? ?????? ???? ? ????????.",
        "",
        "## Ключевые аргументы",
        f"- Запрос сфокусирован на {asset}, поэтому отчёт отделяет анализ актива от персонального решения о доле в портфеле.",
        "- Доступные материалы показывают, какие вопросы по источникам, оценке стоимости, рискам и портфелю нужно закрыть перед персональным решением.",
        "- Подробные проверки сохранены в пакете проверки, а не вынесены в основной читательский отчёт как технические детали.",
        "",
        "## Ключевые риски",
        "- Рыночные данные, оценочные вводные и риск-метрики нужно проверить по датированным источникам перед использованием отчёта для решения.",
        "- Персональная применимость зависит от текущих позиций, целей, горизонта, риск-профиля, ограничений и допустимой концентрации.",
    ]
    if evidence_pack.get("freshness_required"):
        lines.append("- Текущие рыночные или новостные выводы требуют обновления источников с датой и временем перед выводом о точке входа.")
    lines.extend([
        "",
        "## Оценка стоимости и ожиданий",
        _valuation_summary_ru(valuation_status),
        "",
        "## Портфельная роль",
        _portfolio_role_summary_ru(portfolio_context_missing),
        "",
        "## ??? ??????? ??????",
        "- ?????????? ????????: ????? ??????? ?????????????? ??????????? ?????, ?????? ????????? ?????? ?????????, ???? ?????????? ?????? ??? ???????? ???? ? ????????.",
        "- ?????????? ????????: ???????????? ? ??????????, ????????? ?????? ?????????, ???????????? ????-???????? ??? ???????? ????????????/??????????? ? ????????.",
        "",
        "## ??? ???????????",
        "- ?????????? ??????????, ?????? ?????????, ???????? ??????, ???????? ?????????????, ???????????????? ? ??????????? ? ????????.",
        "",
        "## Что нужно для персонального или финального вывода",
        "- Текущая позиция, примерная доля в портфеле, пересекающиеся экспозиции, цель, горизонт, риск-профиль, потребность в ликвидности, налоговые ограничения и запрещённые инструменты.",
        "- Датированные источники по цене, оценке стоимости, benchmark-сравнению, историческим ценам, риск-метрикам, существенным новостям и отчётности.",
        "- Завершённая проверка, где оценка стоимости, риски, качество источников и портфельная роль поддерживают один и тот же вывод.",
        "",
        "## Источники",
        _source_note_ru(evidence_pack),
    ])
    return "\n".join(lines)


def _reader_summary(state: dict[str, Any], ic: dict[str, Any]) -> str:
    if state.get("final_status") == "Blocked":
        return "The available material is not enough for a decision-oriented conclusion. The report identifies what would need to be collected or verified before the view can be used."
    if ic.get("ic_action_status") == "Eligible for IC Action":
        return "The available materials indicate that a committee-level decision may be prepared, subject to the report body and source record."
    return "The available material supports a structured working view, but a final positive action is not available until the evidence, valuation, risk, and portfolio items are resolved."


def _reader_summary_ru(state: dict[str, Any], ic: dict[str, Any]) -> str:
    if state.get("final_status") == "Blocked":
        return "Доступных материалов недостаточно для вывода, ориентированного на решение. Отчёт показывает, что нужно собрать или проверить перед использованием вывода."
    if ic.get("ic_action_status") == "Eligible for IC Action":
        return "Доступные материалы позволяют подготовить решение на уровне комитета при условии, что это поддержано текстом отчёта и источниками."
    return "Доступные материалы поддерживают рабочий взгляд, но финальное позитивное действие недоступно, пока не закрыты вопросы по источникам, оценке стоимости, рискам и портфелю."


def _valuation_summary(valuation_status: str) -> str:
    if valuation_status == "Pass":
        return "Valuation and expectations work is available in the verification package and should be read alongside the key risks before any action-oriented use."
    return "A source-backed valuation and expectations view is still needed before price can support a decision-oriented conclusion."


def _valuation_summary_ru(valuation_status: str) -> str:
    if valuation_status == "Pass":
        return "Оценка стоимости и ожиданий доступна в пакете проверки; её нужно читать вместе с ключевыми рисками перед любым действием."
    return "Перед финальным выводом, ориентированным на действие, нужна оценка стоимости и ожиданий, подтверждённая источниками."


def _portfolio_context_missing(state: dict[str, Any]) -> bool:
    return state.get("position_context") == "Unknown" or not (state.get("user_context") or {}).get("portfolio_context")


def _portfolio_role_summary(portfolio_context_missing: bool) -> str:
    opening = (
        "Portfolio role is described in general terms because personal portfolio context was not provided."
        if portfolio_context_missing
        else "Portfolio role reflects the available portfolio context, while exact sizing remains outside this report."
    )
    bullets = [
        opening,
        "",
        "- Potential role: the asset may serve as core, satellite, hedge, income, cyclical, or defensive exposure only if its evidence-backed characteristics match the investor's objective and risk budget.",
        "- What it is not: this is not an exact allocation, trade instruction, or substitute for reviewing current holdings and constraints.",
        "- Portfolio risks to assess: concentration, overlap with existing holdings, correlation, drawdown tolerance, liquidity, currency or tax exposure, and monitoring burden.",
        "- Data needed for a personal decision: existing holdings, approximate weights, benchmark, objective, horizon, risk tolerance, constraints, and source-backed risk and performance metrics.",
    ]
    return "\n".join(bullets)


def _portfolio_role_summary_ru(portfolio_context_missing: bool) -> str:
    opening = (
        "Портфельная роль дана в общем виде, так как персональный портфельный контекст не указан."
        if portfolio_context_missing
        else "Портфельная роль учитывает доступный портфельный контекст, но точный размер позиции остаётся вне рамок этого отчёта."
    )
    bullets = [
        opening,
        "",
        "- Возможная роль: актив может быть core / satellite / hedge / income / cyclical / defensive exposure только если его подтверждённые характеристики совпадают с целью и риск-бюджетом инвестора.",
        "- Чем это не является: это не точная аллокация, не торговая инструкция и не замена проверке текущих позиций и ограничений.",
        "- Портфельные риски: концентрация, пересечение с текущими позициями, корреляция, переносимость просадки, ликвидность, валютные или налоговые факторы и нагрузка по мониторингу.",
        "- Данные для персонального решения: текущие позиции, примерные веса, benchmark, цель, горизонт, риск-профиль, ограничения, а также подтверждённые риск-метрики и показатели доходности.",
    ]
    return "\n".join(bullets)


def _source_note(evidence_pack: dict[str, Any]) -> str:
    sources = [
        str(source)
        for source in (evidence_pack.get("sources") or [])
        if "dry-run" not in str(source).casefold() and "synthetic" not in str(source).casefold()
    ]
    if not sources:
        return "No live source list is shown in this reader report. Detailed source and verification records are kept with the saved materials."
    first_sources = "; ".join(str(source) for source in sources[:3])
    if len(sources) > 3:
        first_sources += "; additional sources are kept with the saved materials."
    return first_sources


def _source_note_ru(evidence_pack: dict[str, Any]) -> str:
    sources = [
        str(source)
        for source in (evidence_pack.get("sources") or [])
        if "dry-run" not in str(source).casefold() and "synthetic" not in str(source).casefold()
    ]
    if not sources:
        return "Актуальный список источников не показан в этом читательском отчёте. Подробные источники и проверки сохранены вместе с материалами отчёта."
    first_sources = "; ".join(str(source) for source in sources[:3])
    if len(sources) > 3:
        first_sources += "; дополнительные источники сохранены вместе с материалами отчёта."
    return first_sources


def _is_russian_report(state: dict[str, Any]) -> bool:
    text = " ".join(str(state.get(key, "")) for key in ("original_user_request", "normalized_request"))
    return any("\u0400" <= char <= "\u04ff" for char in text)


def _run_metadata(state: dict[str, Any]) -> str:
    return "\n".join([
        "# Run metadata",
        "",
        f"Run ID: {state.get('run_id', '')}",
        f"Thread ID: {state.get('thread_id', '')}",
        f"Mode: {state.get('mode', 'dry_run')}",
        f"Route: {state.get('route', '')}",
        f"Decision mode: {state.get('decision_mode', '')}",
        f"Portfolio Fit Level: {state.get('portfolio_fit_level', 0)}",
        f"Completed LangGraph nodes: {', '.join(state.get('completed_nodes') or [])}",
        "Subagent claim: No Codex subagents are claimed by this LangGraph runtime; these are LangGraph nodes.",
    ])


def _intake(state: dict[str, Any]) -> str:
    return "\n".join([
        "# Intake",
        "",
        f"Original request: {state.get('original_user_request', '')}",
        f"Normalized request: {state.get('normalized_request', '')}",
        f"Detected intent: {state.get('detected_intent', '')}",
        f"Asset identity: {state.get('asset_identity', '')}",
        f"Asset class: {state.get('asset_class', '')}",
        f"Horizon: {state.get('horizon', '')}",
        f"Position context: {state.get('position_context', '')}",
        f"Decision mode: {state.get('decision_mode', '')}",
        f"Materiality plan: see audit/materiality_plan.md",
        f"Thesis spine: see audit/thesis_spine.md",
        f"Missing context: {', '.join(state.get('missing_context') or []) or 'None'}",
    ])


def _sources(state: dict[str, Any]) -> str:
    pack = state.get("evidence_pack") or {}
    sources = pack.get("sources") or []
    lines = ["# Sources", "", "Source freshness must be visible when material.", ""]
    if not sources:
        lines.append("- No live sources collected. Dry-run outputs are synthetic and Limited.")
    else:
        for source in sources:
            lines.append(f"- {source}")
    return "\n".join(lines)


def _dict_doc(title: str, data: Any) -> str:
    return f"# {title}\n\n{_markdown_kv(data)}"


def _markdown_kv(data: Any, indent: int = 0) -> str:
    pad = "  " * indent
    if isinstance(data, dict):
        if not data:
            return f"{pad}- Empty"
        lines: list[str] = []
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                lines.append(f"{pad}- {key}:")
                lines.append(_markdown_kv(value, indent + 1))
            else:
                lines.append(f"{pad}- {key}: {value}")
        return "\n".join(lines)
    if isinstance(data, list):
        if not data:
            return f"{pad}- Empty"
        return "\n".join(f"{pad}- {item}" for item in data)
    return f"{pad}{data}"
