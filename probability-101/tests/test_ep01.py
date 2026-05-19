"""Tests for ep01 in Probability 101."""

import pytest
from ko.ep01_monte_carlo import run


def test_ep01_monte_carlo_basic():
    """Test ep01 monte carlo basic."""
    out = run(120_000)
    assert out["p_head"] == pytest.approx(0.5, abs=0.01)
    assert out["p_dice_even"] == pytest.approx(0.5, abs=0.01)
