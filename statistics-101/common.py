from __future__ import annotations

from typing import Any

import numpy as np

SEED = 42


def rng() -> np.random.Generator:
    return np.random.default_rng(SEED)


def as_float(value: Any) -> float:
    return float(np.asarray(value).item())
