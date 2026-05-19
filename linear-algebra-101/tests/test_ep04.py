"""Tests for ep04 in Linear Algebra 101."""

import numpy as np
from conftest import load_episode


def test_ep04_cosine_ordering():
    """Test ep04 cosine ordering."""
    out = load_episode("04-inner-product-and-distance").run()
    best = int(np.argmax(out["cosine"]))
    assert best == 0
    assert np.isclose(out["manhattan"][1], 1.0)
