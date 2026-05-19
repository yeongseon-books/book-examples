"""Tests for ep08 in Linear Algebra 101."""

import numpy as np
from conftest import load_episode


def test_ep08_svd_reconstruction():
    """Test ep08 svd reconstruction."""
    out = load_episode("08-matrix-decomposition").run()
    assert np.allclose(out["a"], out["recon"], atol=1e-10)
    assert np.linalg.norm(out["a"] - out["rank1"]) > 1e-3
