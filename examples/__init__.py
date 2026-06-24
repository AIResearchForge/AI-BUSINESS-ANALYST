"""Example ideas for Business Analyst tests."""

from pathlib import Path

EXAMPLE_IDEAS_FILE = Path(__file__).parent / "example_ideas.txt"


def load_example_ideas() -> list[str]:
    """Loads example ideas from file."""

    if not EXAMPLE_IDEAS_FILE.exists():
        return [
            "Language learning app for children",
            "Short-term apartment rental platform",
            "Food delivery app from restaurants",
            "Online used clothing sales service",
        ]

    with open(EXAMPLE_IDEAS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


__all__ = ["load_example_ideas"]
