"""Tests for ep02 in Probability 101."""

from ko.ep02_sample_space import run


def test_ep02_sample_space():
    """Test ep02 sample space."""
    out = run()
    assert out["sample_space_size"] == 36
    assert out["p_sum_7"] == 6 / 36
    assert out["p_double"] == 6 / 36
