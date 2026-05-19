import math


def sigmoid(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-z))


def model(x: float, w: float, b: float) -> float:
    return sigmoid(w * x + b)


def grads(x: float, y: float, w: float, b: float) -> tuple[float, float]:
    p = model(x, w, b)
    err = p - y
    return err * x, err


def train(
    data: list[tuple[float, float]], epochs: int = 200, lr: float = 0.2
) -> tuple[float, float]:
    w, b = 0.0, 0.0
    for _ in range(epochs):
        for x, y in data:
            dw, db = grads(x, y, w, b)
            w -= lr * dw
            b -= lr * db
    return w, b


def run_demo() -> dict[str, float]:
    data = [(0.0, 0.0), (1.0, 1.0)]
    w, b = train(data)
    return {"p0": model(0.0, w, b), "p1": model(1.0, w, b)}
