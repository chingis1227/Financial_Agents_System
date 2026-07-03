"""Asset identity helpers for QUICK snapshots."""

from __future__ import annotations

import json
import re
from typing import Any

MSFT_IDENTITY = {
    "ticker": "MSFT",
    "company_name": "Microsoft Corporation",
    "security_type": "equity",
    "currency": "USD",
    "cik": "0000789019",
    "source": "Automation Lab MSFT identity seed plus SEC public identifiers",
}

QUICK_ASSET_IDENTITIES: dict[str, dict[str, Any]] = {
    "MSFT": MSFT_IDENTITY,
    "SPY": {
        "ticker": "SPY",
        "company_name": "SPDR S&P 500 ETF Trust",
        "security_type": "etf",
        "currency": "USD",
        "source": "Automation Lab ETF identity seed",
    },
    "BTC": {
        "ticker": "BTC",
        "company_name": "Bitcoin",
        "security_type": "crypto",
        "currency": "USD",
        "source": "Automation Lab crypto identity seed",
        "price_ticker": "BTC-USD",
    },
    "TLT": {
        "ticker": "TLT",
        "company_name": "iShares 20+ Year Treasury Bond ETF",
        "security_type": "bond_etf",
        "currency": "USD",
        "source": "Automation Lab bond ETF identity seed",
    },
    "GLD": {
        "ticker": "GLD",
        "company_name": "SPDR Gold Shares",
        "security_type": "commodity_etf",
        "currency": "USD",
        "source": "Automation Lab commodity ETF identity seed",
    },
}

COMPARISON_IDENTITY = {
    "ticker": "MSFT-SPY-BTC",
    "company_name": "MSFT vs SPY vs BTC",
    "security_type": "multi_asset_comparison",
    "currency": "USD",
    "components": [
        {field: QUICK_ASSET_IDENTITIES[ticker][field] for field in ("ticker", "company_name", "security_type", "currency", "source")}
        for ticker in ("MSFT", "SPY", "BTC")
    ],
    "source": "Automation Lab comparison identity seed",
}


def detect_quick_asset_identity(prompt: str) -> dict[str, Any] | None:
    """Detect the limited TASK-008/TASK-009 QUICK pilot identities."""
    text = prompt.lower()
    has_msft = bool(re.search(r"\bmsft\b", text) or "microsoft" in text)
    has_spy = bool(re.search(r"\bspy\b", text) or "s&p 500 etf" in text or "s and p 500 etf" in text)
    has_btc = bool(re.search(r"\bbtc\b", text) or "bitcoin" in text)
    if has_msft and has_spy and has_btc and (" vs " in text or "compare" in text or "comparison" in text):
        return json.loads(json.dumps(COMPARISON_IDENTITY))
    if has_msft:
        return dict(QUICK_ASSET_IDENTITIES["MSFT"])
    if has_spy:
        return dict(QUICK_ASSET_IDENTITIES["SPY"])
    if has_btc:
        return dict(QUICK_ASSET_IDENTITIES["BTC"])
    if re.search(r"\btlt\b", text) or "long duration treasury etf" in text or "long-duration treasury etf" in text:
        return dict(QUICK_ASSET_IDENTITIES["TLT"])
    if re.search(r"\bgld\b", text) or "gold etf" in text:
        return dict(QUICK_ASSET_IDENTITIES["GLD"])
    return None


def quick_identity_slug(identity: dict[str, Any] | None) -> str:
    if not identity:
        return "UNKNOWN"
    ticker = str(identity.get("ticker") or "UNKNOWN")
    return re.sub(r"[^A-Z0-9]+", "-", ticker.upper()).strip("-") or "UNKNOWN"


def quick_fixture_slug(identity_or_ticker: dict[str, Any] | str) -> str:
    ticker = identity_or_ticker.get("ticker") if isinstance(identity_or_ticker, dict) else identity_or_ticker
    return re.sub(r"[^a-z0-9]+", "_", str(ticker).lower()).strip("_")
