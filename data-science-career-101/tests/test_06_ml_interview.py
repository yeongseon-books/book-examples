from __future__ import annotations

import numpy as np

from .conftest import load_module


mod = load_module("ko/06-ml-interview.py")


def test_cv_folds_non_overlapping() -> None:
    folds = mod.k_fold_indices(30, k=5, seed=7)
    for train_idx, test_idx in folds:
        assert set(train_idx).isdisjoint(set(test_idx))


def test_knn_accuracy_above_baseline() -> None:
    x = np.array(
        [[0, 0], [0, 1], [1, 0], [1, 1], [5, 5], [5, 6], [6, 5], [6, 6]], dtype=float
    )
    y = np.array([0, 0, 0, 0, 1, 1, 1, 1])
    train_idx, test_idx = mod.train_test_split_indices(len(x), test_ratio=0.25, seed=3)
    model = mod.KNNClassifier(k=3)
    model.fit(x[train_idx], y[train_idx])
    pred = model.predict(x[test_idx])
    acc = mod.accuracy(y[test_idx], pred)
    assert acc >= 0.5
