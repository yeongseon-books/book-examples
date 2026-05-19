"""Tests for ep03 in Linear Algebra 101."""

import numpy as np
from conftest import load_episode


def test_ep03_inverse_roundtrip():
    """Test ep03 inverse roundtrip."""
    out = load_episode("03-matrices").run()
    assert np.allclose(out["a"] @ out["inv"], np.eye(2), atol=1e-10)
    assert np.isclose(out["det"], 1.0)
