from __future__ import annotations

from common import clamp_score


def score_portfolio_project(flags: dict[str, bool]) -> int:
    weights = {
        "has_demo": 20,
        "has_tests": 20,
        "has_readme": 20,
        "has_deploy": 20,
        "has_monitoring": 10,
        "has_ci": 10,
    }
    score = sum(weight for key, weight in weights.items() if flags.get(key, False))
    return clamp_score(score)
