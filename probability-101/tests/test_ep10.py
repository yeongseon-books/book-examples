"""Tests for ep10 in Probability 101."""

from ko.ep10_naive_bayes_ml import run


def test_ep10_naive_bayes():
    """Test ep10 naive bayes."""
    out = run()
    assert out["accuracy"] >= 0.75
    assert out["n_test"] == 4
