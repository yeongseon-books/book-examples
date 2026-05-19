"""Tests for 02 problem to data problem in Data Science 101."""

from _loader import load_module

m = load_module("02-problem-to-data-problem.py")


def test_episode_02_spec_valid() -> None:
    """Test episode 02 spec valid."""
    spec = m.make_data_problem_spec()
    assert m.validate_spec(spec)
    assert spec["metric"] == "f1"
