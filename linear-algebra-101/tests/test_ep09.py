"""Tests for ep09 in Linear Algebra 101."""

from conftest import load_episode


def test_ep09_pca_variance():
    """Test ep09 pca variance."""
    out = load_episode("09-pca").run()
    assert out["ratio"][0] > 0.95
    assert out["z"].shape[1] == 1
