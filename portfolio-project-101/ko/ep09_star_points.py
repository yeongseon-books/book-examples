"""Portfolio Project 101 - Episode 9: Star points."""

from __future__ import annotations


def generate_star_talking_points(facts: dict[str, str]) -> list[str]:
    """Generate star talking points."""
    return [
        f"Situation: {facts.get('situation', '')}",
        f"Task: {facts.get('task', '')}",
        f"Action: {facts.get('action', '')}",
        f"Result: {facts.get('impact', '')}",
    ]
