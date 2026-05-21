"""Calculus For Ml 101 - 7편: gradient descent 예제."""


def loss(w: float) -> float:
    """Loss."""
    return (w - 3.0) ** 2


def grad(w: float) -> float:
    """Grad."""
    return 2.0 * (w - 3.0)


def train(w0: float, lr: float = 0.1, steps: int = 60) -> float:
    """Train."""
    w = w0
    for _ in range(steps):
        w -= lr * grad(w)
    return w


def run_demo() -> dict[str, float]:
    """데모를 실행합니다."""
    w = train(0.0)
    return {"w": w, "loss": loss(w)}
