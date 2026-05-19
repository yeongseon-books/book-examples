"""Tests for ep03 in Probability 101."""

import pytest
from ko.ep03_conditional_probability import run


def test_ep03_conditional_probability():
    """Test ep03 conditional probability."""
    out = run(250_000)
    assert out["sim"] == pytest.approx(out["exact"], abs=0.01)
