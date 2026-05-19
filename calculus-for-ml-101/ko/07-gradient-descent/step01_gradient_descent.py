def loss(w: float) -> float:
    return (w - 3.0) ** 2


def grad(w: float) -> float:
    return 2.0 * (w - 3.0)


def train(w0: float, lr: float = 0.1, steps: int = 60) -> float:
    w = w0
    for _ in range(steps):
        w -= lr * grad(w)
    return w


def run_demo() -> dict[str, float]:
    w = train(0.0)
    return {"w": w, "loss": loss(w)}
