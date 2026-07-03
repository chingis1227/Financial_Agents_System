from __future__ import annotations

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BEHAVIOR = ROOT / "tests" / "behavior"

# Reader-facing Russian investment text must not keep generic English
# investment jargon when a natural Russian equivalent exists. Keep this list
# focused on phrases that have already leaked into reports or are common
# Run-glish failure modes; do not include controlled labels or tickers here.
FORBIDDEN_RUSSIAN_PHRASES = {
    "growth exposure": "экспозиция на рост / доля, завязанная на рост",
    "headline earnings": "текущие / ближайшие финансовые результаты",
    "profit pools": "центры прибыли / источники прибыли",
    "customer wins": "выигранные клиенты / новые клиентские контракты",
    "customer-level exposure": "экспозиция по отдельным клиентам / концентрация на уровне клиентов",
    "downside-модель": "негативный сценарий / модель риска снижения",
    "upside/downside": "потенциал роста / риск снижения",
    "commodity-cycle": "сырьевой цикл / товарный цикл памяти",
    "price fixing": "ценовой сговор",
}

CONTROLLED_ENGLISH_LABELS = {
    "Action Box",
    "Analysis Status",
    "Decision Confidence",
    "Decision-Prep Box",
    "ETF",
    "FY2026",
    "FY2027",
    "GAAP",
    "HBM",
    "IC Action",
    "Investment View",
    "MU",
    "NASDAQ",
    "SCA",
    "SEC",
    "Watchlist",
    "non-GAAP",
}

ALLOWED_ABBREVIATION_HYBRID_PREFIXES = {
    # Keep this empty by default. Even when an abbreviation is allowed, the
    # Russian report should prefer "конкуренция в HBM" over "HBM-конкуренция".
}


def has_cyrillic(text: str) -> bool:
    return re.search(r"[\u0400-\u04FF]", text) is not None


def forbidden_phrase_issues(text: str) -> list[str]:
    lower = text.casefold()
    issues: list[str] = []
    for phrase, replacement in sorted(FORBIDDEN_RUSSIAN_PHRASES.items()):
        if phrase.casefold() in lower:
            issues.append(f"forbidden phrase `{phrase}`; use {replacement}")
    return issues


def hybrid_issues(text: str) -> list[str]:
    issues: list[str] = []
    # English-to-Russian hybrids such as AI-выручка, growth-exposure, HBM-конкуренция.
    pattern = re.compile(r"\b([A-Za-z]{2,})-([А-Яа-яЁё][А-Яа-яЁёA-Za-z]*)")
    for match in pattern.finditer(text):
        prefix = match.group(1)
        token = match.group(0)
        if prefix in ALLOWED_ABBREVIATION_HYBRID_PREFIXES:
            continue
        # Skip pure filing/form-like tokens only when the suffix is not Cyrillic
        # (the regex already requires Cyrillic, so most matches are true issues).
        issues.append(f"English-Russian hybrid `{token}`")

    # Russian-to-English hybrids such as риск-downside.
    reverse = re.compile(r"\b([А-Яа-яЁё][А-Яа-яЁё]+)-([A-Za-z]{2,})\b")
    for match in reverse.finditer(text):
        issues.append(f"Russian-English hybrid `{match.group(0)}`")
    return issues


def validate_russian_user_facing_text(text: str) -> list[str]:
    """Return language/style issues for Russian reader-facing investment text."""
    issues: list[str] = []
    # Even if the text was accidentally saved with corrupted Cyrillic, ASCII
    # Run-glish phrases are still detectable and must fail.
    issues.extend(forbidden_phrase_issues(text))
    if has_cyrillic(text):
        issues.extend(hybrid_issues(text))
    question_marks = text.count("?")
    if question_marks > 20 and question_marks / max(1, len(text)) > 0.03:
        issues.append("possible Cyrillic encoding corruption: excessive question marks")
    return issues


def load_cases() -> list[dict]:
    path = BEHAVIOR / "language_style_cases.yaml"
    if not path.exists():
        raise AssertionError(f"missing fixture: {path}")
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, list):
        raise AssertionError("language_style_cases.yaml must contain a JSON list")
    return data


def run_fixture_checks() -> list[tuple[str, bool, str]]:
    checks: list[tuple[str, bool, str]] = []
    for case in load_cases():
        cid = str(case.get("id", "<missing>"))
        text = str(case.get("text", ""))
        should_pass = bool(case.get("should_pass"))
        issues = validate_russian_user_facing_text(text)
        ok = not issues if should_pass else bool(issues)
        checks.append((f"language style fixture: {cid}", ok, "; ".join(issues)))
        for expected in case.get("expected_issues", []):
            checks.append(
                (f"{cid} expected issue: {expected}", any(str(expected) in issue for issue in issues), "; ".join(issues))
            )
    return checks


def run_doc_sync_checks() -> list[tuple[str, bool, str]]:
    checks: list[tuple[str, bool, str]] = []
    required_mentions = [
        ("AGENTS.md", "tools\\validate_language_style.py"),
        ("PROJECT_STATE.md", "tools\\validate_language_style.py"),
        ("implementation/15-documentation-sync-contract.md", "tools\\validate_language_style.py"),
        ("implementation/14-language-and-style.md", "language_style_cases.yaml"),
        (".agents/skills/language-policy/SKILL.md", "tools\\validate_language_style.py"),
        (".agents/skills/investment-analytical-style/SKILL.md", "tools\\validate_language_style.py"),
    ]
    for rel, token in required_mentions:
        path = ROOT / rel
        txt = path.read_text(encoding="utf-8-sig") if path.exists() else ""
        checks.append((f"{rel} mentions {token}", token in txt, rel))
    return checks


def main(argv: list[str]) -> int:
    checks: list[tuple[str, bool, str]] = []
    checks.extend(run_fixture_checks())
    checks.extend(run_doc_sync_checks())

    for raw_path in argv:
        path = Path(raw_path)
        text = path.read_text(encoding="utf-8-sig")
        issues = validate_russian_user_facing_text(text)
        checks.append((f"validate file: {path}", not issues, "; ".join(issues[:20])))

    failed = [c for c in checks if not c[1]]
    for name, ok, detail in checks:
        print(("PASS" if ok else "FAIL") + f" | {name}" + (f" | {detail}" if detail else ""))
    print(f"\nSummary: {len(checks) - len(failed)} passed / {len(checks)} total")
    if failed:
        print("\nFailures:")
        for name, _, detail in failed:
            print(f"- {name}" + (f" ({detail})" if detail else ""))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
