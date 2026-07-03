"""Global public-equity resolver for TASK-013 AGENT runs.

This resolver is intentionally public/no-key first. It uses deterministic
static seeds for tests and well-known cases, and can enrich US-listed identity
from the SEC company tickers feed in live paths.
"""

from __future__ import annotations

from typing import Any

from .source_fetchers import http_json, now_iso

SEC_COMPANY_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"

PRIVATE_COMPANY_ALIASES: dict[str, str] = {
    "openai": "OpenAI",
    "space x": "SpaceX",
    "spacex": "SpaceX",
    "stripe": "Stripe",
    "anthropic": "Anthropic",
    "databricks": "Databricks",
}

STATIC_EQUITY_IDENTITIES: dict[str, dict[str, Any]] = {
    "MSFT": {
        "ticker": "MSFT",
        "company_name": "Microsoft Corporation",
        "cik": "0000789019",
        "exchange": "NASDAQ",
        "country": "United States",
        "currency": "USD",
        "instrument_classification": "us_common_equity",
        "security_type": "equity",
        "aliases": ["microsoft", "microsoft corporation"],
        "ir_url": "https://www.microsoft.com/en-us/Investor",
    },
    "AAPL": {
        "ticker": "AAPL",
        "company_name": "Apple Inc.",
        "cik": "0000320193",
        "exchange": "NASDAQ",
        "country": "United States",
        "currency": "USD",
        "instrument_classification": "us_common_equity",
        "security_type": "equity",
        "aliases": ["apple", "apple inc", "apple inc."],
        "ir_url": "https://investor.apple.com/",
    },
    "NVDA": {
        "ticker": "NVDA",
        "company_name": "NVIDIA Corporation",
        "cik": "0001045810",
        "exchange": "NASDAQ",
        "country": "United States",
        "currency": "USD",
        "instrument_classification": "us_common_equity",
        "security_type": "equity",
        "aliases": ["nvidia", "nvidia corporation"],
        "ir_url": "https://investor.nvidia.com/",
    },
    "GOOGL": {
        "ticker": "GOOGL",
        "company_name": "Alphabet Inc.",
        "cik": "0001652044",
        "exchange": "NASDAQ",
        "country": "United States",
        "currency": "USD",
        "share_class": "Class A",
        "instrument_classification": "us_share_class",
        "security_type": "equity",
        "aliases": ["alphabet", "google", "alphabet class a"],
        "ir_url": "https://abc.xyz/investor/",
    },
    "GOOG": {
        "ticker": "GOOG",
        "company_name": "Alphabet Inc.",
        "cik": "0001652044",
        "exchange": "NASDAQ",
        "country": "United States",
        "currency": "USD",
        "share_class": "Class C",
        "instrument_classification": "us_share_class",
        "security_type": "equity",
        "aliases": ["alphabet class c"],
        "ir_url": "https://abc.xyz/investor/",
    },
    "META": {
        "ticker": "META",
        "company_name": "Meta Platforms, Inc.",
        "cik": "0001326801",
        "exchange": "NASDAQ",
        "country": "United States",
        "currency": "USD",
        "instrument_classification": "us_common_equity",
        "security_type": "equity",
        "aliases": ["meta", "facebook"],
        "ir_url": "https://investor.fb.com/",
    },
    "BRK.B": {
        "ticker": "BRK.B",
        "price_ticker": "BRK-B",
        "company_name": "Berkshire Hathaway Inc.",
        "cik": "0001067983",
        "exchange": "NYSE",
        "country": "United States",
        "currency": "USD",
        "share_class": "Class B",
        "instrument_classification": "us_share_class",
        "security_type": "equity",
        "aliases": ["berkshire hathaway", "brk-b", "brk b"],
        "ir_url": "https://www.berkshirehathaway.com/reports.html",
    },
    "BABA": {
        "ticker": "BABA",
        "company_name": "Alibaba Group Holding Limited",
        "cik": "0001577552",
        "exchange": "NYSE",
        "country": "China",
        "currency": "USD",
        "instrument_classification": "adr_or_foreign_issuer_us_listing",
        "security_type": "adr",
        "is_adr": True,
        "underlying_issuer": "Alibaba Group Holding Limited",
        "aliases": ["alibaba"],
        "ir_url": "https://www.alibabagroup.com/en-US/ir",
    },
    "TSM": {
        "ticker": "TSM",
        "company_name": "Taiwan Semiconductor Manufacturing Company Limited",
        "cik": "0001046179",
        "exchange": "NYSE",
        "country": "Taiwan",
        "currency": "USD",
        "instrument_classification": "adr_or_foreign_issuer_us_listing",
        "security_type": "adr",
        "is_adr": True,
        "underlying_issuer": "Taiwan Semiconductor Manufacturing Company Limited",
        "aliases": ["tsmc", "taiwan semiconductor"],
        "ir_url": "https://investor.tsmc.com/",
    },
    "ASML.AS": {
        "ticker": "ASML.AS",
        "company_name": "ASML Holding N.V.",
        "exchange": "Euronext Amsterdam",
        "country": "Netherlands",
        "currency": "EUR",
        "instrument_classification": "non_us_listed_equity",
        "security_type": "equity",
        "aliases": ["asml", "asml holding"],
        "ir_url": "https://www.asml.com/en/investors",
    },
    "7203.T": {
        "ticker": "7203.T",
        "company_name": "Toyota Motor Corporation",
        "exchange": "Tokyo Stock Exchange",
        "country": "Japan",
        "currency": "JPY",
        "instrument_classification": "non_us_listed_equity",
        "security_type": "equity",
        "aliases": ["toyota", "toyota motor"],
        "ir_url": "https://global.toyota/en/ir/",
    },
    "9988.HK": {
        "ticker": "9988.HK",
        "company_name": "Alibaba Group Holding Limited",
        "exchange": "Hong Kong Stock Exchange",
        "country": "Hong Kong / China",
        "currency": "HKD",
        "instrument_classification": "non_us_listed_equity",
        "security_type": "equity",
        "underlying_issuer": "Alibaba Group Holding Limited",
        "aliases": ["alibaba hong kong", "alibaba hk"],
        "ir_url": "https://www.alibabagroup.com/en-US/ir",
    },
    "NESN.SW": {
        "ticker": "NESN.SW",
        "company_name": "Nestle S.A.",
        "exchange": "SIX Swiss Exchange",
        "country": "Switzerland",
        "currency": "CHF",
        "instrument_classification": "non_us_listed_equity",
        "security_type": "equity",
        "aliases": ["nestle", "nesn"],
        "ir_url": "https://www.nestle.com/investors",
    },
}


def canonical_ticker(raw: str) -> str:
    token = raw.strip().upper().replace("/", ".")
    if token == "BRK-B":
        return "BRK.B"
    return token


def _tokens_for_identity(ticker: str, identity: dict[str, Any]) -> list[str]:
    tokens = [ticker.lower(), ticker.lower().replace(".", "-"), ticker.lower().replace(".", " ")]
    tokens.extend(str(alias).lower() for alias in identity.get("aliases", []))
    return sorted(set(tokens), key=len, reverse=True)


def _prompt_has_token(prompt: str, token: str) -> bool:
    import re

    return bool(re.search(rf"(?<![a-z0-9.\-]){re.escape(token)}(?![a-z0-9.\-])", prompt.lower()))


def detect_equity_mentions(prompt: str) -> list[str]:
    mentions: list[str] = []
    for ticker, identity in STATIC_EQUITY_IDENTITIES.items():
        if any(_prompt_has_token(prompt, token) for token in _tokens_for_identity(ticker, identity)):
            mentions.append(ticker)
    return sorted(set(mentions))


def _looks_complex(prompt: str) -> bool:
    import re

    text = prompt.lower()
    instrument_patterns = [
        r"\bpreferred\b",
        r"\bpreference\s+shares?\b",
        r"\boptions?\b",
        r"\bwarrants?\b",
        r"\brights\s+(?:issue|offering|instrument|security|ticker)\b",
        r"\bunits?\s+(?:instrument|security|ticker|offering)\b",
        r"\botc(?:-like)?\b",
        r"[.\-]pr(?:[.\-]?[a-z])?\b",
        r"(?:^|[\s.:-])pfd(?:[\s.:-]|$)",
        r"-[pP]\b",
    ]
    return any(re.search(pattern, text) for pattern in instrument_patterns)


def _private_company(prompt: str) -> str | None:
    text = prompt.lower()
    for alias, name in PRIVATE_COMPANY_ALIASES.items():
        if alias in text:
            return name
    return None


def sec_company_ticker_lookup(ticker: str) -> dict[str, Any] | None:
    data = http_json(SEC_COMPANY_TICKERS_URL)
    normalized = canonical_ticker(ticker).replace(".", "-").upper()
    for item in data.values():
        if str(item.get("ticker", "")).upper() == normalized:
            cik = str(item.get("cik_str", "")).zfill(10)
            return {
                "ticker": canonical_ticker(ticker),
                "price_ticker": normalized,
                "company_name": item.get("title") or canonical_ticker(ticker),
                "cik": cik,
                "exchange": "US listed",
                "country": "United States",
                "currency": "USD",
                "instrument_classification": "us_common_equity",
                "security_type": "equity",
            }
    return None


def resolve_equity_request(prompt: str, mode: str = "mock") -> dict[str, Any]:
    """Resolve a user prompt into a public-equity instrument decision."""
    timestamp = now_iso()
    private_name = _private_company(prompt)
    if private_name:
        return {
            "status": "blocked",
            "instrument_classification": "private_company",
            "raw_input": prompt,
            "ticker": private_name.upper().replace(" ", "-"),
            "company_name": private_name,
            "security_type": "private_company",
            "confidence": "high",
            "block_reason": "Private companies are not ordinary public listed equity targets.",
            "limitations": ["Can be used only as ecosystem context or proxy search input."],
            "source_candidates": [{"provider": "static_private_company_guard", "status": "found", "retrieved_at": timestamp}],
            "retrieved_at": timestamp,
        }
    if _looks_complex(prompt):
        return {
            "status": "blocked",
            "instrument_classification": "complex_or_unsupported_instrument",
            "raw_input": prompt,
            "ticker": "COMPLEX-INSTRUMENT",
            "company_name": "Complex or unsupported equity-like instrument",
            "security_type": "complex_instrument",
            "confidence": "medium",
            "block_reason": "Preferred shares, options, warrants, rights, units, and complex OTC instruments are not ordinary equity targets in TASK-013.",
            "limitations": ["Ask for the ordinary common share / main listing."],
            "source_candidates": [{"provider": "static_complex_instrument_guard", "status": "found", "retrieved_at": timestamp}],
            "retrieved_at": timestamp,
        }
    mentions = detect_equity_mentions(prompt)
    if len(mentions) > 1:
        # Treat GOOG/GOOGL only as genuinely multiple if both explicit classes appear.
        if set(mentions) == {"GOOG", "GOOGL"}:
            pass
        else:
            return {
                "status": "blocked",
                "instrument_classification": "ambiguous",
                "raw_input": prompt,
                "ticker": "MULTIPLE-EQUITIES",
                "company_name": "Multiple equity instruments",
                "security_type": "ambiguous",
                "confidence": "high",
                "block_reason": "Single-equity AGENT runs support one equity at a time; use comparison workflow for multiple assets.",
                "limitations": mentions,
                "source_candidates": [{"provider": "static_equity_mentions", "status": "found", "tickers": mentions, "retrieved_at": timestamp}],
                "retrieved_at": timestamp,
            }
    ticker = mentions[0] if mentions else None
    if not ticker:
        import re

        raw_candidates = re.findall(r"(?<![A-Za-z0-9.])([A-Za-z0-9]{1,6}(?:[.\-][A-Za-z0-9]{1,4})?)(?![A-Za-z0-9.])", prompt)
        candidates = []
        blocked_tokens = {"AGENT", "QUICK", "ETF", "BTC", "USD", "SEC", "API", "10", "10K", "10Q", "20F", "6K"}
        for candidate in raw_candidates:
            upper = candidate.upper()
            ticker_like = any(ch.isdigit() for ch in candidate) or candidate == upper
            has_listing_suffix = "." in candidate or "-" in candidate
            if upper not in blocked_tokens and (ticker_like or has_listing_suffix):
                candidates.append(upper)
        if candidates:
            ticker = canonical_ticker(candidates[0])
    if not ticker:
        return {
            "status": "blocked",
            "instrument_classification": "ambiguous",
            "raw_input": prompt,
            "ticker": "UNRESOLVED",
            "company_name": "Unresolved equity request",
            "security_type": "ambiguous",
            "confidence": "low",
            "block_reason": "No clear public equity ticker or company identity was resolved.",
            "limitations": ["Provide a ticker, listing, or company name."],
            "source_candidates": [{"provider": "resolver", "status": "missing", "retrieved_at": timestamp}],
            "retrieved_at": timestamp,
        }
    identity = dict(STATIC_EQUITY_IDENTITIES.get(canonical_ticker(ticker), {}))
    if not identity and mode == "live":
        try:
            identity = sec_company_ticker_lookup(ticker) or {}
        except Exception as exc:
            identity = {
                "ticker": canonical_ticker(ticker),
                "company_name": canonical_ticker(ticker),
                "instrument_classification": "us_common_equity",
                "security_type": "equity",
                "exchange": "Unknown",
                "country": "Unknown",
                "currency": "USD",
                "resolver_error": str(exc),
            }
    if not identity:
        identity = {
            "ticker": canonical_ticker(ticker),
            "company_name": canonical_ticker(ticker),
            "exchange": "Unverified public market",
            "country": "Unknown",
            "currency": "USD",
            "instrument_classification": "us_common_equity" if "." not in canonical_ticker(ticker) else "non_us_listed_equity",
            "security_type": "equity",
        }
    identity.setdefault("ticker", canonical_ticker(ticker))
    identity.setdefault("company_name", identity["ticker"])
    identity.setdefault("security_type", "equity")
    identity.setdefault("instrument_classification", "us_common_equity")
    identity.setdefault("confidence", "medium" if identity["company_name"] == identity["ticker"] else "high")
    identity.setdefault("source_candidates", [])
    identity["source_candidates"] = [
        *identity.get("source_candidates", []),
        {
            "provider": "static_equity_seed" if canonical_ticker(ticker) in STATIC_EQUITY_IDENTITIES else "resolver_generic_or_sec",
            "status": "found",
            "retrieved_at": timestamp,
        },
    ]
    if identity.get("instrument_classification") == "adr_or_foreign_issuer_us_listing":
        identity.setdefault("is_adr", True)
        identity.setdefault("underlying_issuer", identity.get("company_name"))
        identity["adr_gate"] = {
            "underlying_issuer": identity.get("underlying_issuer") or identity.get("company_name"),
            "issuer_country": identity.get("country"),
            "trading_currency": identity.get("currency"),
            "reporting_basis": "SEC foreign issuer filings such as 20-F/6-K where available, plus issuer IR reports",
            "liquidity_check": "Required: ADR trading liquidity and underlying/local-line liquidity must be reviewed before any personal action.",
            "regulatory_delisting_risk": "Required: country, audit-access, sanctions, exchange, and delisting risks must be explicitly considered.",
        }
    if identity.get("instrument_classification") == "non_us_listed_equity" and not identity.get("ir_url"):
        identity.setdefault("limitations", []).append(
            "Direct non-US listing identity is unresolved beyond ticker format until issuer/exchange/regulator sources verify it."
        )
        identity["confidence"] = "low"
    identity["status"] = "resolved"
    identity["raw_input"] = prompt
    identity["retrieved_at"] = timestamp
    return identity


def clean_resolved_identity(identity: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in identity.items()
        if key not in {"aliases", "peer_context", "sector_context", "macro_context"}
    }
