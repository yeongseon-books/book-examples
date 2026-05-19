from __future__ import annotations


def generate_star_talking_points(facts: dict[str, str]) -> list[str]:
    return [
        f"Situation: {facts.get('situation', '')}",
        f"Task: {facts.get('task', '')}",
        f"Action: {facts.get('action', '')}",
        f"Result: {facts.get('impact', '')}",
    ]
