"""Azure Aca Deep Dive - Episode 1: Revision split."""

from __future__ import annotations

from common import as_json, traffic_total


def build_traffic() -> list[dict[str, object]]:
    """Build traffic."""
    return [
        {"revisionName": "orders--blue", "weight": 80},
        {"revisionName": "orders--green", "weight": 20},
    ]


def run() -> dict[str, object]:
    """Run."""
    traffic = build_traffic()
    return {
        "episode": 3,
        "mode": "multiple",
        "traffic": traffic,
        "weight_total": traffic_total(traffic),
    }


if __name__ == "__main__":
    print(as_json(run()))
