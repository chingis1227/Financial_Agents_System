"""Source registry for TASK-013 global public-equity AGENT source preflight."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from .equity_resolver import STATIC_EQUITY_IDENTITIES, clean_resolved_identity

SOURCE_IMPORTANCE_LEVELS = {"required", "important", "nice_to_have"}

EQUITY_AGENT_IDENTITIES: dict[str, dict[str, Any]] = STATIC_EQUITY_IDENTITIES

SUPPORTED_EQUITY_TICKERS = tuple(EQUITY_AGENT_IDENTITIES.keys())


def clean_equity_identity(identity: dict[str, Any]) -> dict[str, Any]:
    return clean_resolved_identity(identity)


MSFT_AGENT_IDENTITY: dict[str, Any] = clean_equity_identity(EQUITY_AGENT_IDENTITIES["MSFT"])


@dataclass(frozen=True)
class AgentSourceDefinition:
    source_id: str
    name: str
    category: str
    importance: str
    primary: str
    fallbacks: tuple[str, ...]
    freshness_rule: str
    used_by: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["fallbacks"] = list(self.fallbacks)
        data["used_by"] = list(self.used_by)
        return data


SOURCE_REGISTRY: tuple[AgentSourceDefinition, ...] = (
    AgentSourceDefinition("identity", "Public equity identity", "identity", "required", "equity resolver + public listing identity source", ("SEC company tickers", "issuer investor relations", "exchange listing page",), "structural", ("evidence-collector", "equity-agent")),
    AgentSourceDefinition("sec_submissions", "SEC company submissions", "filings", "required", "SEC submissions API", ("SEC company filing page",), "retrieved_at required", ("evidence-collector", "news-catalysts-agent")),
    AgentSourceDefinition("latest_10k", "Latest Form 10-K", "filings", "required", "SEC submissions recent filings", ("SEC filing detail page",), "latest available annual filing", ("financial-statement-analysis", "equity-agent")),
    AgentSourceDefinition("latest_10q", "Latest Form 10-Q", "filings", "required", "SEC submissions recent filings", ("SEC filing detail page",), "latest available quarterly filing", ("financial-statement-analysis", "valuation-expectations-agent")),
    AgentSourceDefinition("recent_8k", "Recent Form 8-K / issuer event source", "events", "important", "SEC submissions recent filings", ("issuer investor relations news",), "recent filing-driven event", ("news-catalysts-agent", "evidence-collector")),
    AgentSourceDefinition("company_facts", "SEC company facts / XBRL", "fundamentals", "required", "SEC companyfacts API", ("latest filing text",), "retrieved_at required", ("financial-statement-analysis", "valuation-expectations-agent")),
    AgentSourceDefinition("current_price", "Current/recent public price", "market_data", "required", "Stooq public CSV", ("official exchange / issuer quote", "Yahoo public chart"), "latest market close for current/latest prompts", ("valuation-expectations-agent", "market-positioning-agent")),
    AgentSourceDefinition("historical_price", "Historical public price series", "market_data", "required", "Stooq historical CSV", ("official exchange / issuer quote", "Yahoo public chart range"), "dated public history", ("valuation-expectations-agent", "market-positioning-agent")),
    AgentSourceDefinition("filing_text", "Full filing text / HTML", "filings", "important", "SEC primary document URL", ("SEC filing detail page",), "document date", ("equity-agent", "risk-red-team-agent")),
    AgentSourceDefinition("ir_news", "Company IR / news / events", "events", "important", "issuer investor relations", ("SEC 8-K",), "event-driven", ("news-catalysts-agent", "equity-agent")),
    AgentSourceDefinition("public_news", "Recent public news/event scan", "events", "important", "issuer/public releases", ("SEC 8-K",), "lookback recorded", ("news-catalysts-agent", "market-positioning-agent")),
    AgentSourceDefinition("peer_context", "Peer / competitor context", "context", "important", "public mega-cap equity peer set", ("static peer context",), "structural", ("sector-industry-analysis-agent", "valuation-expectations-agent")),
    AgentSourceDefinition("sector_context", "Sector / industry context", "context", "important", "public sector context", ("static sector context",), "structural", ("sector-industry-analysis-agent", "equity-agent")),
    AgentSourceDefinition("macro_rates", "Macro / rates context", "macro", "important", "Treasury/Fed public pages", ("static rates context",), "latest available public macro context", ("macro-agent", "valuation-expectations-agent")),
    AgentSourceDefinition("secondary_market_pages", "Extra secondary market pages", "market_data", "nice_to_have", "public market pages", ("not required",), "opportunistic", ("market-positioning-agent",)),
    AgentSourceDefinition("additional_presentations", "Additional public presentation PDFs", "company_materials", "nice_to_have", "issuer presentation PDFs", ("not required",), "opportunistic", ("equity-agent",)),
)

REQUIRED_SOURCE_IDS = tuple(source.source_id for source in SOURCE_REGISTRY if source.importance == "required")
IMPORTANT_SOURCE_IDS = tuple(source.source_id for source in SOURCE_REGISTRY if source.importance == "important")
NICE_TO_HAVE_SOURCE_IDS = tuple(source.source_id for source in SOURCE_REGISTRY if source.importance == "nice_to_have")


def source_registry_snapshot() -> list[dict[str, Any]]:
    return [source.to_dict() for source in SOURCE_REGISTRY]


def source_definition(source_id: str) -> AgentSourceDefinition:
    for source in SOURCE_REGISTRY:
        if source.source_id == source_id:
            return source
    raise KeyError(source_id)


def supported_equity_identity(ticker: str) -> dict[str, Any]:
    normalized = ticker.upper()
    if normalized not in EQUITY_AGENT_IDENTITIES:
        raise KeyError(normalized)
    return clean_equity_identity(EQUITY_AGENT_IDENTITIES[normalized])


def supported_equity_metadata(ticker: str) -> dict[str, Any]:
    normalized = ticker.upper()
    if normalized not in EQUITY_AGENT_IDENTITIES:
        raise KeyError(normalized)
    return EQUITY_AGENT_IDENTITIES[normalized]
