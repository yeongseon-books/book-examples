"""Demonstrate LoRA rank decomposition with numpy"""

from __future__ import annotations

import numpy as np


def truncated_svd(matrix: np.ndarray, rank: int):
    """Truncated svd."""
    u, s, vt = np.linalg.svd(matrix, full_matrices=False)
    u_r = u[:, :rank]
    s_r = np.diag(s[:rank])
    vt_r = vt[:rank, :]
    return u_r @ s_r, vt_r


def main() -> None:
    """Main."""
    rng = np.random.default_rng(42)
    weight_update = rng.normal(size=(6, 6))
    for rank in (1, 2, 4):
        left, right = truncated_svd(weight_update, rank)
        approx = left @ right
        error = np.linalg.norm(weight_update - approx)
        params = left.size + right.size
        print(f"rank={rank}")
        print(f"  Approximation error: {error:.4f}")
        print(f"  Trainable parameters: {params}")
        print(approx)
        print()


if __name__ == "__main__":
    main()
