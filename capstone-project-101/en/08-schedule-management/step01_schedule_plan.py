"""Capstone Project 101 - Episode 8: schedule management example."""

from __future__ import annotations

from common import MilestonePlan


def run() -> dict[str, object]:
    """Run."""
    plan = MilestonePlan(
        milestones=["MVP", "Demo", "Final"],
        weeks={1: "setup", 2: "core", 3: "polish"},
        buffer_days=0.2 * 21,
    )
    return {"plan": plan, "progress": {"done": 12, "todo": 8, "blocked": 2}}


if __name__ == "__main__":
    print(run())
