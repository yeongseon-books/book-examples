"""Tests for ep07 in Llm From Scratch 101."""

import numpy as np
from common import sample_topk


def test_greedy_like_sampling_is_deterministic_with_seed() -> None:
    """Test greedy like sampling is deterministic with seed."""
    logits = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
    np.random.seed(0)
    a = sample_topk(logits, top_k=1, temperature=1.0)
    np.random.seed(0)
    b = sample_topk(logits, top_k=1, temperature=1.0)
    assert a == b == 4
