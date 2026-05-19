"""Capstone Project 101 - Episode 1: Presentation flow."""

from __future__ import annotations


def run() -> dict[str, object]:
    """Run."""
    return {
        "story": ["problem", "solution", "demo", "result", "next"],
        "slides": {"problem": 2, "solution": 3, "demo": 1, "result": 2, "next": 1},
        "demo_steps": ["login", "core_action", "result_view"],
        "qna": ["why_this_stack", "how_we_tested", "what_we_cut"],
        "minutes": {"talk": 8, "demo": 5, "qna": 7},
    }


if __name__ == "__main__":
    print(run())
