"""Compatibility wrappers for earlier TASK-011 MSFT/equity imports."""

from .equity_preflight import build_equity_source_preflight


def build_msft_source_preflight(prompt: str, answers: list[str], mode: str) -> dict:
    return build_equity_source_preflight(prompt=prompt, answers=answers, mode=mode, ticker="MSFT")
