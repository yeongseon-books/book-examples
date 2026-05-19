"""Tests for 01 what is data science in Data Science 101."""

from _loader import load_module

m = load_module("01-what-is-data-science.py")


def test_episode_01_demo_accuracy() -> None:
    """Test episode 01 demo accuracy."""
    result = m.run_demo(seed=42)
    assert result["rows"] == 500.0
    assert result["accuracy"] > 0.7
