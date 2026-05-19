"""Tests for ep09 in Probability 101."""

import pytest
from ko.ep09_lln_clt import run


def test_ep09_lln_clt():
    """Test ep09 lln clt."""
    out = run(25_000, 36)
    assert out["sample_mean_of_means"] == pytest.approx(out["expected"], abs=0.02)
    assert out["sample_mean_std"] == pytest.approx(out["clt_std"], abs=0.02)
