"""Tests for 10 path to senior in Developer Career 101."""

from tests.test_01_what_is_developer_career import load


def test_10_gap_analysis_flags_weak_competencies():
    """Test 10 gap analysis flags weak competencies."""
    mod = load("10-path-to-senior.py")
    scorecard = mod.readiness_scorecard(
        {
            "technical_depth": 8,
            "mentorship": 4,
            "cross_functional": 5,
            "scope": 7,
            "impact": 5,
        }
    )
    assert "mentorship" in scorecard["gaps"]
    assert "cross_functional" in scorecard["gaps"]
