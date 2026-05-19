"""Statistics 101 - Episode 2: Mean median variance std mode."""

from __future__ import annotations

import numpy as np


def run_demo() -> dict[str, float]:
    """Run demo."""
    data = np.array([1, 2, 2, 3, 4, 5, 5, 5], dtype=float)
    mean_manual = float(np.sum(data) / data.size)
    median_manual = float(np.sort(data)[data.size // 2])
    var_manual = float(np.sum((data - mean_manual) ** 2) / data.size)
    std_manual = float(np.sqrt(var_manual))
    values, counts = np.unique(data, return_counts=True)
    mode_manual = float(values[np.argmax(counts)])
    return {
        "mean_manual": mean_manual,
        "mean_numpy": float(np.mean(data)),
        "median_manual": median_manual,
        "median_numpy": float(np.median(data)),
        "var_manual": var_manual,
        "var_numpy": float(np.var(data)),
        "std_manual": std_manual,
        "std_numpy": float(np.std(data)),
        "mode_manual": mode_manual,
    }


if __name__ == "__main__":
    print(run_demo())
