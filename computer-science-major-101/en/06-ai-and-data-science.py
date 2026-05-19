"""Computer Science Major 101 - Episode 6: Ai and data science."""

import math


def sigmoid(x: float) -> float:
    """Sigmoid."""
    return 1.0 / (1.0 + math.exp(-x))


def train_logistic_regression(
    features: list[list[float]], labels: list[int], lr: float = 0.1, epochs: int = 300
) -> tuple[list[float], float]:
    """Train logistic regression."""
    weights = [0.0 for _ in features[0]]
    bias = 0.0
    sample_count = len(features)
    for _ in range(epochs):
        grad_w = [0.0 for _ in weights]
        grad_b = 0.0
        for x, y in zip(features, labels, strict=False):
            z = sum(w * xi for w, xi in zip(weights, x, strict=False)) + bias
            pred = sigmoid(z)
            err = pred - y
            for idx in range(len(weights)):
                grad_w[idx] += err * x[idx]
            grad_b += err
        for idx in range(len(weights)):
            weights[idx] -= lr * grad_w[idx] / sample_count
        bias -= lr * grad_b / sample_count
    return weights, bias


def predict_probability(x: list[float], weights: list[float], bias: float) -> float:
    """Predict probability."""
    return sigmoid(sum(w * xi for w, xi in zip(weights, x, strict=False)) + bias)


if __name__ == "__main__":
    xs = [[0.1], [0.3], [0.7], [0.9]]
    ys = [0, 0, 1, 1]
    w, b = train_logistic_regression(xs, ys)
    print(predict_probability([0.2], w, b), predict_probability([0.8], w, b))
