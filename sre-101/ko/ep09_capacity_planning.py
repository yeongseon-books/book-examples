"""Sre 101 - Episode 9: Capacity planning."""

import numpy as np


def forecast_next(load_series: list[float]) -> float:
    """Forecast next."""
    x = np.arange(len(load_series), dtype=float)
    y = np.array(load_series, dtype=float)
    if len(load_series) < 2:
        return float(y[-1]) if len(load_series) == 1 else 0.0
    slope, intercept = np.polyfit(x, y, 1)
    return float(intercept + slope * len(load_series))


def headroom_ok(
    current_load: float, capacity: float, min_headroom_ratio: float = 0.2
) -> bool:
    """Headroom ok."""
    if capacity <= 0:
        return False
    return (capacity - current_load) / capacity >= min_headroom_ratio
