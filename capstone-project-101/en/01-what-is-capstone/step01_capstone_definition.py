"""Capstone Project 101 - Episode 1: Capstone definition."""

from __future__ import annotations


def run() -> dict[str, object]:
    """Run."""
    title = "Class Timetable Conflict Checker"
    users = ["student", "advisor"]
    value = "Reduce course registration time"
    metric = "User confirms conflicts within 30 seconds"
    demo = "demo.mp4 + readme.md"
    return {
        "title": title,
        "users": users,
        "value": value,
        "metric": metric,
        "demo": demo,
        "success": True,
    }


if __name__ == "__main__":
    print(run())
