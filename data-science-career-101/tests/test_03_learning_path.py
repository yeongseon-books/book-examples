from __future__ import annotations

from .conftest import load_module


mod = load_module("ko/03-learning-path.py")


def test_plan_is_12_weeks_and_respects_prerequisites() -> None:
    plan = mod.generate_12_week_plan("scientist", weekly_hours=12, current_skills=set())
    assert len(plan) == 12
    first_occurrence = {}
    for idx, row in enumerate(plan):
        first_occurrence.setdefault(row["topic"], idx)
    assert first_occurrence["statistics"] <= first_occurrence["ml_basics"]
    assert first_occurrence["python_basics"] <= first_occurrence["ml_basics"]
