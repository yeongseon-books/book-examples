"""Cloud Computing 101 - Episode 1: Architecture review."""

from __future__ import annotations


def record(service: str, action: str, **payload: object) -> dict[str, object]:
    """Record."""
    return {"ok": True, "service": service, "action": action, "payload": payload}


def well_architected_review(scores: dict[str, int]) -> dict[str, object]:
    """Well architected review."""
    pillars = [
        "operational_excellence",
        "security",
        "reliability",
        "performance_efficiency",
        "cost_optimization",
    ]
    total = sum(scores[p] for p in pillars)
    average = round(total / len(pillars), 2)
    grade = "pass" if average >= 80 else "improve"
    return record("architecture", "review", average=average, grade=grade)
