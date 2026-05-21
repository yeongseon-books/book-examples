"""Capstone Project 101 - Episode 7: choosing the tech stack example."""

from __future__ import annotations

from common import score_stack


def run() -> dict[str, object]:
    """Run."""
    familiar = {"FastAPI": 4, "Flask": 5, "Django": 2}
    learning_cost = {"FastAPI": 2, "Flask": 1, "Django": 4}
    ops = {"FastAPI": 2, "Flask": 1, "Django": 3}
    score = score_stack(familiar, learning_cost, ops)
    return {"pick": max(score, key=score.get), "score": score}


if __name__ == "__main__":
    print(run())
