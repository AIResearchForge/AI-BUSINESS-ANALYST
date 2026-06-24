"""Przykładowe pomysły do testów Business Analyst."""

from pathlib import Path

EXAMPLE_IDEAS_FILE = Path(__file__).parent / "example_ideas.txt"


def load_example_ideas() -> list[str]:
    """Wczytuje przykładowe pomysły z pliku."""

    if not EXAMPLE_IDEAS_FILE.exists():
        return [
            "Aplikacja do nauki języków dla dzieci",
            "Platforma do wynajmu mieszkań na krótki termin",
            "Aplikacja do zamawiania jedzenia z restauracji",
            "Serwis do sprzedaży używanych ubrań online",
        ]

    with open(EXAMPLE_IDEAS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


__all__ = ["load_example_ideas"]
