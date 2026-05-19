"""Devops 101 - Episode 3: Cd and deployment."""

from __future__ import annotations


def simulate_canary(version: str) -> dict[str, object]:
    """Simulate canary."""
    phases = [10, 50, 100]
    timeline = []
    for traffic in phases:
        timeline.append(
            {
                "phase": f"canary-{traffic}",
                "version": version,
                "traffic_percent": traffic,
                "healthy_instances": 10,
                "unhealthy_instances": 0,
            }
        )
    return {
        "strategy": "canary",
        "timeline": timeline,
        "zero_downtime": _is_healthy(timeline),
    }


def _is_healthy(timeline: list[dict[str, object]]) -> bool:
    """Is healthy."""
    return all(
        item["healthy_instances"] > 0 and item["unhealthy_instances"] == 0
        for item in timeline
    )
