"""Tests for ep09 in Statistics 101."""

from en.ep09_p_value_and_p_hacking import run_demo


def test_ep09_p_hacking_demo():
    """Test ep09 p hacking demo."""
    r = run_demo()
    assert r["min_bonferroni_p"] >= r["min_raw_p"]
    assert r["num_tests"] == 20.0
