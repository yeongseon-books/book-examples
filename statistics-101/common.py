"""Shared utilities and domain models for Statistics 101."""

from __future__ import annotations

from typing import Any

import numpy as np

SEED = 42


def rng() -> np.random.Generator:
    """Rng."""
    return np.random.default_rng(SEED)


def as_float(value: Any) -> float:
    """As float."""
    return float(np.asarray(value).item())
