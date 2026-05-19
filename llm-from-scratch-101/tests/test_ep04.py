"""Tests for ep04 in Llm From Scratch 101."""

import numpy as np
from common import TransformerBlock


def test_transformer_block_preserves_shape() -> None:
    """Test transformer block preserves shape."""
    x = np.random.randn(2, 5, 16)
    y = TransformerBlock(16, 2)(x)
    assert y.shape == x.shape
