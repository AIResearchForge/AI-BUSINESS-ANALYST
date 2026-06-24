"""Utility functions for Business Analyst."""

import re
from typing import List, Dict, Any


def extract_market_potential(text: str) -> float:
    """Extracts Market Potential from response."""
    match = re.search(r"Market Potential:\s*([\d.]+)/10", text)
    if match:
        return float(match.group(1))
    return 0.0


def extract_competition(text: str) -> str:
    """Extracts competition level from response."""
    match = re.search(r"Competition:\s*(Low|Medium|High)", text, re.IGNORECASE)
    if match:
        return match.group(1)
    return "Unknown"


def extract_chance(text: str) -> int:
    """Extracts Estimated Chance from response."""
    match = re.search(r"Estimated Chance:\s*(\d+)%", text)
    if match:
        return int(match.group(1))
    return 0


def format_report(idea: str, market: str, competitors: str, finance: str) -> str:
    """Creates a formatted startup report."""

    report = f"Idea: {idea}\n\n"
    report += "📊 MARKET ANALYSIS:\n"
    report += f"{market}\n\n"
    report += "🏆 COMPETITORS:\n"
    report += f"{competitors}\n\n"
    report += "💰 MONETIZATION AND RISKS:\n"
    report += f"{finance}\n"

    return report


__all__ = [
    "extract_market_potential",
    "extract_competition",
    "extract_chance",
    "format_report",
]
