"""Shared utilities and domain models for Developer Career 101."""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import dataclass


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    """Clamp."""
    return max(low, min(high, value))


def parse_markdown_sections(markdown: str) -> dict[str, str]:
    """Parse markdown sections."""
    sections: dict[str, list[str]] = {}
    current = "_preamble"
    sections[current] = []
    for line in markdown.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections.setdefault(current, [])
            continue
        sections[current].append(line)
    return {k: "\n".join(v).strip() for k, v in sections.items()}


def has_star_bullet(line: str) -> bool:
    """Has star bullet."""
    text = line.lower()
    has_action = bool(
        re.search(r"\b(cut|reduced|increased|built|designed|implemented)\b", text)
    )
    has_number = bool(re.search(r"\d", text))
    has_result = bool(re.search(r"\b(by|to|from|serving|result)\b", text))
    return (
        line.strip().startswith(("-", "*")) and has_action and has_number and has_result
    )


def keyword_score(text: str, keywords: Iterable[str]) -> int:
    """Keyword score."""
    lowered = text.lower()
    return sum(2 if k in lowered else 0 for k in keywords)


@dataclass
class RubricScorer:
    """Rubric scorer."""

    weights: dict[str, float]

    def score(self, values: dict[str, float]) -> tuple[float, dict[str, float]]:
        """Score."""
        weighted: dict[str, float] = {}
        total = 0.0
        for key, weight in self.weights.items():
            component = clamp(values.get(key, 0.0), 0.0, 10.0) / 10.0 * weight * 100.0
            weighted[key] = round(component, 2)
            total += component
        return round(total, 2), weighted
