"""Tests for ep07 in Probability 101."""

import pytest
from ko.ep07_discrete_distributions import run


def test_ep07_discrete_distributions():
    """Test ep07 discrete distributions."""
    out = run()
    assert out["bernoulli_pmf_1"] == pytest.approx(0.3)
    assert out["binom_pmf_3"] > 0
    assert out["poisson_pmf_2"] > 0
    assert out["geom_pmf_4"] > 0
