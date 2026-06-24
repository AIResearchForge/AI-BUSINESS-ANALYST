"""Funkcje pomocnicze dla Business Analyst."""

import re
from typing import List, Dict, Any


def extract_market_potential(text: str) -> float:
    """Wyciąga Market Potential z odpowiedzi."""
    match = re.search(r"Market Potential:\s*([\d.]+)/10", text)
    if match:
        return float(match.group(1))
    return 0.0


def extract_competition(text: str) -> str:
    """Wyciąga poziom konkurencji z odpowiedzi."""
    match = re.search(r"Competition:\s*(Low|Medium|High)", text, re.IGNORECASE)
    if match:
        return match.group(1)
    return "Unknown"


def extract_chance(text: str) -> int:
    """Wyciąga Estimated Chance z odpowiedzi."""
    match = re.search(r"Estimated Chance:\s*(\d+)%", text)
    if match:
        return int(match.group(1))
    return 0


def format_report(idea: str, market: str, competitors: str, finance: str) -> str:
    """Tworzy sformatowany raport startupowy."""

    report = f"Pomysł: {idea}\n\n"
    report += "📊 ANALIZA RYNKU:\n"
    report += f"{market}\n\n"
    report += "🏆 KONKURENCJA:\n"
    report += f"{competitors}\n\n"
    report += "💰 MONETYZACJA I RYZYKA:\n"
    report += f"{finance}\n"

    return report


__all__ = [
    "extract_market_potential",
    "extract_competition",
    "extract_chance",
    "format_report",
]
