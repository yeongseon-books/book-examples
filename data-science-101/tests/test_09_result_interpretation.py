"""Tests for 09 result interpretation in Data Science 101."""

from _loader import load_module

m = load_module("09-result-interpretation.py")


def test_episode_09_report_contains_importance() -> None:
    """Test episode 09 report contains importance."""
    report = m.interpret_results(seed=42)
    assert "INTERPRETATION REPORT" in report
    assert "top_feature_importance" in report
    assert "top_permutation_importance" in report
