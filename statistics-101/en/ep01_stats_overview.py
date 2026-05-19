from __future__ import annotations

import numpy as np


def run_demo() -> dict[str, float]:
    data = np.array([3, 5, 7, 7, 10, 12, 15], dtype=float)
    return {
        "count": float(data.size),
        "mean": float(np.mean(data)),
        "median": float(np.median(data)),
        "min": float(np.min(data)),
        "max": float(np.max(data)),
        "q1": float(np.percentile(data, 25)),
        "q3": float(np.percentile(data, 75)),
    }


if __name__ == "__main__":
    print(run_demo())
