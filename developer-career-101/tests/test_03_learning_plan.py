"""Tests for 03 learning plan in Developer Career 101."""

from tests.test_01_what_is_developer_career import load


def test_03_plan_respects_prereq_and_hours():
    """Test 03 plan respects prereq and hours."""
    mod = load("03-learning-plan.py")
    plan = mod.build_12_week_plan("backend", weekly_hours=6, current_skills=set())
    flat = [task for week in plan for task in week["tasks"]]
    assert flat.index("python-basics") < flat.index("http-api")
    assert flat.index("python-basics") < flat.index("database")
    assert all(week["hours"] <= 6 for week in plan)
