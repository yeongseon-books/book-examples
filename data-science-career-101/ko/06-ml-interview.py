from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from math import sqrt

import numpy as np
from numpy.typing import NDArray


def train_test_split_indices(
    n: int, test_ratio: float = 0.2, seed: int = 42
) -> tuple[NDArray[np.int_], NDArray[np.int_]]:
    rng = np.random.default_rng(seed)
    idx = np.arange(n)
    rng.shuffle(idx)
    test_size = max(1, int(round(n * test_ratio)))
    return idx[test_size:], idx[:test_size]


def k_fold_indices(
    n: int, k: int = 5, seed: int = 42
) -> list[tuple[NDArray[np.int_], NDArray[np.int_]]]:
    rng = np.random.default_rng(seed)
    idx = np.arange(n)
    rng.shuffle(idx)
    folds = np.array_split(idx, k)
    result = []
    for i in range(k):
        test_idx = folds[i]
        train_idx = np.concatenate([folds[j] for j in range(k) if j != i])
        result.append((train_idx, test_idx))
    return result


@dataclass
class KNNClassifier:
    k: int = 3
    x_train: NDArray[np.float_] | None = None
    y_train: NDArray[np.int_] | None = None

    def fit(self, x: NDArray[np.float_], y: NDArray[np.int_]) -> None:
        self.x_train = x
        self.y_train = y

    def _distance(self, a: NDArray[np.float_], b: NDArray[np.float_]) -> float:
        return sqrt(float(np.sum((a - b) ** 2)))

    def predict_one(self, x: NDArray[np.float_]) -> int:
        assert self.x_train is not None and self.y_train is not None
        distances = [
            (self._distance(x, row), int(label))
            for row, label in zip(self.x_train, self.y_train, strict=False)
        ]
        neighbors = sorted(distances, key=lambda item: item[0])[: self.k]
        votes: dict[int, int] = {}
        for _, label in neighbors:
            votes[label] = votes.get(label, 0) + 1
        return sorted(votes.items(), key=lambda item: (-item[1], item[0]))[0][0]

    def predict(self, x: NDArray[np.float_]) -> NDArray[np.int_]:
        return np.array([self.predict_one(row) for row in x])


def accuracy(y_true: Iterable[int], y_pred: Iterable[int]) -> float:
    true = list(y_true)
    pred = list(y_pred)
    correct = sum(1 for a, b in zip(true, pred, strict=False) if a == b)
    return correct / max(1, len(true))
