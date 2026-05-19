from __future__ import annotations

import numpy as np


def _train_bernoulli_nb(
    x: np.ndarray, y: np.ndarray, alpha: float = 1.0
) -> tuple[np.ndarray, np.ndarray]:
    classes = np.array([0, 1])
    class_priors = np.array([(y == c).mean() for c in classes])
    feat_probs = np.zeros((2, x.shape[1]))
    for idx, c in enumerate(classes):
        xc = x[y == c]
        feat_probs[idx] = (xc.sum(axis=0) + alpha) / (len(xc) + 2 * alpha)
    return class_priors, feat_probs


def _predict(
    x: np.ndarray, class_priors: np.ndarray, feat_probs: np.ndarray
) -> np.ndarray:
    log_priors = np.log(class_priors)
    log_like_1 = np.log(feat_probs)
    log_like_0 = np.log(1 - feat_probs)
    scores = []
    for row in x:
        class_scores = log_priors + (row * log_like_1 + (1 - row) * log_like_0).sum(
            axis=1
        )
        scores.append(int(np.argmax(class_scores)))
    return np.array(scores)


def run() -> dict[str, float]:
    x_train = np.array(
        [
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
            [0, 1, 1],
            [1, 1, 1],
            [0, 0, 0],
        ]
    )
    y_train = np.array([1, 1, 0, 0, 1, 0])
    x_test = np.array([[1, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 1]])
    y_test = np.array([1, 0, 1, 0])

    class_priors, feat_probs = _train_bernoulli_nb(x_train, y_train)
    pred = _predict(x_test, class_priors, feat_probs)
    acc = float((pred == y_test).mean())
    return {"accuracy": acc, "n_test": float(len(y_test))}


if __name__ == "__main__":
    print(run())
