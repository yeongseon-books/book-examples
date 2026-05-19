"""Tests for ep04 in Operating Systems 101."""

from common import ep04_race_condition


def test_ep04_race_condition_structural_properties():
    """Test ep04 race condition structural properties."""
    out = ep04_race_condition(num_threads=10, increments=500)
    assert out["safe"] == out["expected"]
    assert out["unsafe"] < out["expected"]
