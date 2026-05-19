"""Software Engineering 101 - Episode 9: Debt."""

from __future__ import annotations

from common import todo_count


def debt_scorer(code_text: str) -> dict[str, int]:
    """Debt scorer."""
    counts = todo_count(code_text)
    score = counts["TODO"] * 2 + counts["FIXME"] * 3
    return {"todo": counts["TODO"], "fixme": counts["FIXME"], "debt_score": score}


def prioritization_matrix(impact: int, effort: int) -> str:
    """Prioritization matrix."""
    if impact >= 7 and effort <= 4:
        return "quick-win"
    if impact >= 7 and effort > 4:
        return "major-project"
    if impact < 7 and effort <= 4:
        return "fill-in"
    return "thankless"
