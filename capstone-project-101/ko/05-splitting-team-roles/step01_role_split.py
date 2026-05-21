"""Capstone Project 101 - 5편: splitting team roles 예제."""

from __future__ import annotations


def run() -> dict[str, object]:
    """Run."""
    members = ["A", "B", "C", "D"]
    primary = {"A": "lead", "B": "backend", "C": "frontend", "D": "data"}
    backup = {"backend": "C", "frontend": "B", "data": "A"}
    raci = {"deploy": ("A", "B"), "test": ("D", "C")}
    return {
        "members": members,
        "primary": primary,
        "backup": backup,
        "raci": raci,
        "review": "weekly",
    }


if __name__ == "__main__":
    print(run())
