from __future__ import annotations

import re
from dataclasses import dataclass, asdict
from typing import Any

SPECIALIST_PREFIXES: dict[str, str] = {
    "RISK": "risk-red-team-agent",
    "VAL": "valuation-expectations-agent",
    "MACRO": "macro-agent",
    "NEWS": "news-catalysts-agent",
    "PORTFOLIO": "portfolio-fit-agent",
    "SECTOR": "sector-industry-analysis-agent",
    "EVIDENCE": "evidence-collector",
    "POSITIONING": "market-positioning-agent",
    "INTEL": "market-intelligence-agent",
    "EQUITY": "equity-agent",
    "ETF": "etf-agent",
    "COMMODITY": "commodity-agent",
    "CRYPTO": "crypto-agent",
    "FI": "fixed-income-agent",
    "WINNERS": "structural-winners-discovery-agent",
    "IC": "investment-committee-agent",
}

ASSET_ALIASES: list[tuple[str, str, str]] = [
    ("microsoft", "Microsoft", "equity"), ("msft", "Microsoft", "equity"),
    ("nvidia", "Nvidia", "equity"), ("nvda", "Nvidia", "equity"),
    ("apple", "Apple", "equity"), ("aapl", "Apple", "equity"),
    ("tesla", "Tesla", "equity"), ("tsla", "Tesla", "equity"),
    ("bitcoin", "Bitcoin", "crypto"), ("btc", "Bitcoin", "crypto"),
    ("ethereum", "Ethereum", "crypto"), ("eth", "Ethereum", "crypto"),
    ("qqq", "QQQ", "etf"), ("schg", "SCHG", "etf"), ("tlt", "TLT", "fixed_income"),
    ("gold", "Gold", "commodity"), ("золото", "Gold", "commodity"),
    ("oil", "Oil", "commodity"), ("нефть", "Oil", "commodity"),
]

QUICK_WORDS = ("quick", "short", "fast", "brief", "preliminary", "быстро", "коротко", "глянь", "кратко")
NEWS_WORDS = ("today", "latest", "now", "why did", "rise", "fell", "fall", "упал", "упала", "вырос", "сегодня", "почему", "новост")
BUY_WORDS = ("buy", "invest", "hold", "sell", "add", "trim", "exit", "purchase", "покуп", "инвест", "держ", "продав", "стоит ли", "проанализ")
RISK_WORDS = ("risk", "risks", "red team", "риск", "риски")
THEME_WORDS = ("theme", "beneficiaries", "winners", "structural winners", "тема", "бенефициар", "победител")
COMPARISON_WORDS = (" vs ", " versus ", " or ", " compare", "which is better", "или", "сравни", "лучше")

@dataclass(frozen=True)
class RouteDecision:
    detected_intent: str
    route: str
    asset_identity: str
    asset_class: str
    horizon: str
    position_context: str
    missing_context: list[str]
    target_agent: str = ""
    required_questions: int = 0
    freshness_required: bool = False
    route_card: str = ""

    def as_state_update(self) -> dict[str, Any]:
        d = asdict(self)
        d.pop("target_agent", None)
        d.pop("required_questions", None)
        d.pop("freshness_required", None)
        d.pop("route_card", None)
        return d


def classify_request(prompt: str) -> RouteDecision:
    raw = prompt.strip()
    lower = raw.casefold()
    prefix_match = re.match(r"^\s*([A-Z]+)\s*:\s*(.*)$", raw)
    prefix = prefix_match.group(1).upper() if prefix_match else ""
    body = prefix_match.group(2) if prefix_match else raw
    body_lower = body.casefold()

    if prefix == "BLOCKED" or "unroutable" in lower or "cannot route" in lower:
        return RouteDecision("blocked", "blocked", "Unknown", "unknown", "Unknown", "Unknown", ["blocked_or_unroutable_request"], route_card="workflows/route_cards/investment_request_router.md")

    assets = _detect_assets(body_lower if prefix else lower)
    asset_identity, asset_class = _asset_identity_and_class(assets)
    horizon = _detect_horizon(lower)
    position_context = _detect_position_context(lower)
    freshness_required = any(word in lower for word in NEWS_WORDS)

    if prefix == "QUICK":
        return RouteDecision("quick_take", "quick_take", asset_identity, asset_class, horizon, position_context, [], required_questions=3, freshness_required=freshness_required, route_card="workflows/route_cards/quick_take.md")
    if prefix == "AGENT":
        route = _full_route_for_asset(asset_class, assets, body_lower)
        return RouteDecision("full_agent_workflow", route, asset_identity, _route_asset_class(route, asset_class), horizon, position_context, _missing_context_for_full(horizon, position_context, strict=False), required_questions=5, freshness_required=freshness_required, route_card=f"workflows/route_cards/{route}.md")
    if prefix in SPECIALIST_PREFIXES:
        specialist_class = _prefix_asset_class(prefix, asset_class)
        return RouteDecision("direct_specialist", "direct_specialist", asset_identity, specialist_class, horizon, position_context, [], target_agent=SPECIALIST_PREFIXES[prefix], freshness_required=freshness_required, route_card="workflows/route_cards/direct_specialist.md")
    if prefix:
        return RouteDecision("needs_clarification", "needs_clarification", asset_identity, asset_class, horizon, position_context, [f"Unknown command prefix: {prefix}"], route_card="workflows/route_cards/investment_request_router.md")

    if any(word in lower for word in QUICK_WORDS):
        return RouteDecision("quick_take", "quick_take", asset_identity, asset_class, horizon, position_context, [], required_questions=3, freshness_required=freshness_required, route_card="workflows/route_cards/quick_take.md")
    if any(word in lower for word in RISK_WORDS) and asset_identity != "Unknown" and not any(word in lower for word in BUY_WORDS):
        return RouteDecision("direct_specialist", "direct_specialist", asset_identity, asset_class, horizon, position_context, [], target_agent="risk-red-team-agent", freshness_required=freshness_required, route_card="workflows/route_cards/direct_specialist.md")
    if any(word in lower for word in COMPARISON_WORDS) and len(assets) >= 2:
        return RouteDecision("comparison", _comparison_route(assets), asset_identity, "multi_asset" if len({a[2] for a in assets}) > 1 else asset_class, horizon, position_context, _missing_context_for_comparison(horizon, position_context), required_questions=5, freshness_required=freshness_required, route_card="workflows/route_cards/multi_asset_comparison.md")
    if freshness_required and asset_identity != "Unknown" and not any(word in lower for word in BUY_WORDS):
        return RouteDecision("market_news_update", "market_news_update", asset_identity, asset_class, horizon, position_context, [], freshness_required=True, route_card="workflows/route_cards/direct_specialist.md")
    if any(word in lower for word in THEME_WORDS) and asset_identity == "Unknown":
        return RouteDecision("theme_discovery", "theme_discovery", "Theme", "theme", horizon, position_context, [], required_questions=5, freshness_required=freshness_required, route_card="workflows/route_cards/multi_asset_comparison.md")
    if asset_identity != "Unknown" and any(word in lower for word in BUY_WORDS):
        route = _full_route_for_asset(asset_class, assets, lower)
        # Ordinary buy/investment prompts should route by default, but ambiguous missing context pauses later.
        strict_missing = "стоит ли" in lower or "should i buy" in lower or "should i invest" in lower
        return RouteDecision("full_agent_workflow", route, asset_identity, _route_asset_class(route, asset_class), horizon, position_context, _missing_context_for_full(horizon, position_context, strict=strict_missing), required_questions=5, freshness_required=freshness_required, route_card=f"workflows/route_cards/{route}.md")

    if asset_identity == "Unknown":
        return RouteDecision("needs_clarification", "needs_clarification", asset_identity, asset_class, horizon, position_context, ["asset_identity"], route_card="workflows/route_cards/investment_request_router.md")
    return RouteDecision("quick_take", "quick_take", asset_identity, asset_class, horizon, position_context, [], required_questions=3, freshness_required=freshness_required, route_card="workflows/route_cards/quick_take.md")


def _detect_assets(text: str) -> list[tuple[str, str, str]]:
    found: list[tuple[str, str, str]] = []
    seen = set()
    for alias, canonical, cls in ASSET_ALIASES:
        pattern = rf"(?<![\wА-Яа-яЁё]){re.escape(alias.casefold())}(?![\wА-Яа-яЁё])"
        if re.search(pattern, text):
            key = (canonical, cls)
            if key not in seen:
                found.append((alias, canonical, cls))
                seen.add(key)
    return found


def _asset_identity_and_class(assets: list[tuple[str, str, str]]) -> tuple[str, str]:
    if not assets:
        return "Unknown", "unknown"
    names = [a[1] for a in assets]
    classes = {a[2] for a in assets}
    identity = " vs ".join(names) if len(names) > 1 else names[0]
    return identity, (assets[0][2] if len(classes) == 1 else "multi_asset")


def _detect_horizon(text: str) -> str:
    m = re.search(r"(\d+)\s*(?:\+?\s*)?(year|years|yr|yrs|года|год|лет)", text, re.I)
    if m:
        return f"{m.group(1)} years"
    if "long term" in text or "долгоср" in text:
        return "Long term"
    return "Unknown"


def _detect_position_context(text: str) -> str:
    if "no current position" in text or "no position" in text or "позиции нет" in text or "нет позиции" in text:
        return "No current position"
    if "current position" in text or "есть пози" in text or "уже держ" in text:
        return "Current position disclosed"
    return "Unknown"


def _full_route_for_asset(asset_class: str, assets: list[tuple[str, str, str]], text: str) -> str:
    if len(assets) >= 2:
        if all(a[2] == "etf" for a in assets):
            return "multi_asset_comparison"
        return "multi_asset_comparison"
    if "bond etf" in text or asset_class == "fixed_income":
        return "fixed_income_full_cycle"
    if asset_class == "crypto":
        return "crypto_full_cycle"
    if asset_class == "commodity":
        return "commodity_full_cycle"
    if asset_class == "etf":
        return "etf_full_cycle"
    if asset_class == "multi_asset":
        return "multi_asset_comparison"
    return "equity_full_cycle"


def _comparison_route(assets: list[tuple[str, str, str]]) -> str:
    if len(assets) >= 2:
        return "multi_asset_comparison"
    return "etf_full_cycle"


def _route_asset_class(route: str, fallback: str) -> str:
    return {
        "equity_full_cycle": "equity",
        "crypto_full_cycle": "crypto",
        "commodity_full_cycle": "commodity",
        "fixed_income_full_cycle": "fixed_income",
        "etf_full_cycle": "etf",
        "multi_asset_comparison": "multi_asset",
    }.get(route, fallback)


def _prefix_asset_class(prefix: str, fallback: str) -> str:
    return {
        "ETF": "etf", "COMMODITY": "commodity", "CRYPTO": "crypto", "FI": "fixed_income",
        "EQUITY": "equity", "MACRO": "multi_asset", "SECTOR": "theme", "WINNERS": "theme",
    }.get(prefix, fallback)


def _missing_context_for_full(horizon: str, position_context: str, *, strict: bool) -> list[str]:
    missing: list[str] = []
    if horizon == "Unknown":
        missing.append("horizon")
    if position_context == "Unknown":
        missing.append("position_context")
    if strict:
        missing.append("risk_tolerance_or_decision_context")
    return missing


def _missing_context_for_comparison(horizon: str, position_context: str) -> list[str]:
    missing: list[str] = []
    if horizon == "Unknown":
        missing.append("comparison_horizon")
    if position_context == "Unknown":
        missing.append("portfolio_role_or_current_holdings")
    return missing
