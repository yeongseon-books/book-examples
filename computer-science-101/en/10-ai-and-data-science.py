"""Episode 10: linear regression with gradient descent"""


def train_linear_regression(
    xs: list[float], ys: list[float], lr: float = 0.01, epochs: int = 3000
) -> tuple[float, float]:
    """Train linear regression."""
    w = 0.0
    b = 0.0
    n = len(xs)
    for _ in range(epochs):
        dw = 0.0
        db = 0.0
        for x, y in zip(xs, ys, strict=False):
            pred = w * x + b
            err = pred - y
            dw += err * x
            db += err
        w -= lr * (2.0 / n) * dw
        b -= lr * (2.0 / n) * db
    return w, b


def predict(x: float, w: float, b: float) -> float:
    """Predict."""
    return w * x + b


if __name__ == "__main__":
    xs = [0, 1, 2, 3, 4, 5]
    ys = [1, 3, 5, 7, 9, 11]
    w, b = train_linear_regression(xs, ys)
    print(f"w={w:.3f}, b={b:.3f}, pred(6)={predict(6, w, b):.3f}")
