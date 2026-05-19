"""Tests for 01 what is data career in Data Science Career 101."""

from __future__ import annotations

from .conftest import load_module

mod = load_module("ko/01-what-is-data-career.py")


def test_engineer_fit_is_recommended_for_engineering_answers() -> None:
    """Test engineer fit is recommended for engineering answers."""
    answers = {f"q{i}": 1 for i in range(1, 11)}
    answers.update({"q3": 5, "q6": 5, "q8": 5})
    result = mod.assess_career_fit(answers)
    assert result["recommended_track"] == "engineer"
