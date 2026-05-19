"""Tests for ep01 in Portfolio Project 101."""

from ko.ep01_portfolio_scorer import score_portfolio_project


def test_ep01_portfolio_scorer() -> None:
    """Test ep01 portfolio scorer."""
    score = score_portfolio_project(
        {"has_demo": True, "has_tests": True, "has_readme": True}
    )
    assert score == 60
