"""미니 학습 루프 시뮬레이션"""

from __future__ import annotations

import numpy as np


def main() -> None:
    x = np.array([0.0, 1.0, 2.0, 3.0], dtype=float)
    y = np.array([1.0, 3.0, 5.0, 7.0], dtype=float)
    weight = 0.0
    bias = 0.0
    learning_rate = 0.1

    for epoch in range(1, 16):
        pred = weight * x + bias
        error = pred - y
        loss = float(np.mean(error**2))
        grad_w = float(np.mean(2 * error * x))
        grad_b = float(np.mean(2 * error))
        weight -= learning_rate * grad_w
        bias -= learning_rate * grad_b
        print(f"epoch={epoch:02d} loss={loss:.4f} weight={weight:.4f} bias={bias:.4f}")

    print("학습이 진행될수록 손실이 감소하는 패턴을 확인하세요.")


if __name__ == "__main__":
    main()
