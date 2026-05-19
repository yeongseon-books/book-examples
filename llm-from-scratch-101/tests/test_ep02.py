"""Tests for ep02 in Llm From Scratch 101."""

import numpy as np
from common import Embedding, positional_encoding


def test_embedding_and_positional_shape() -> None:
    """Test embedding and positional shape."""
    emb = Embedding(20, 8)
    idx = np.array([[1, 2, 3, 4]])
    out = emb(idx) + positional_encoding(4, 8)[None, :, :]
    assert out.shape == (1, 4, 8)
