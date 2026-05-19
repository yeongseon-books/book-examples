"""Tests for 10 skills before graduation in Computer Science Major 101."""

from conftest import load_module


def test_skill_scoring_flags_gaps_below_threshold() -> None:
    """Test skill scoring flags gaps below threshold."""
    mod = load_module("ko/10-skills-before-graduation.py")
    report = mod.score_skills(
        {"algorithms": 4, "systems": 2, "network": 3, "writing": 1}, threshold=3
    )
    assert report["average"] == 2.5
    assert report["gaps"] == ["systems", "writing"]
    assert report["levels"]["algorithms"] == "strong"
    assert report["levels"]["network"] == "developing"
