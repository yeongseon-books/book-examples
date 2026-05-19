"""Tests for ep01 in Linear Algebra 101."""

from conftest import load_episode


def test_ep01_shapes():
    """Test ep01 shapes."""
    out = load_episode("01-what-is-linear-algebra").run()
    assert out["v_shape"] == (2,)
    assert out["a_shape"] == (2, 2)
