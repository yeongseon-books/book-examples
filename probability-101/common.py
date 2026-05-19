"""Shared utilities and domain models for Probability 101."""

from __future__ import annotations

import numpy as np


def make_rng(seed: int = 42) -> np.random.Generator:
    """Make rng."""
    return np.random.default_rng(seed)
