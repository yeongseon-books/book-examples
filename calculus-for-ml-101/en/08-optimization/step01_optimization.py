import math


def momentum_step(
    w: float, v: float, g: float, lr: float = 0.1, beta: float = 0.9
) -> tuple[float, float]:
    v = beta * v + g
    return w - lr * v, v


def adam_step(
    w: float,
    m: float,
    v: float,
    g: float,
    t: int,
    lr: float = 0.05,
    b1: float = 0.9,
    b2: float = 0.999,
    eps: float = 1e-8,
) -> tuple[float, float, float]:
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * g * g
    mh = m / (1 - b1**t)
    vh = v / (1 - b2**t)
    return w - lr * mh / (math.sqrt(vh) + eps), m, v


def cosine_lr(step: int, total: int, lr0: float = 0.1) -> float:
    return 0.5 * lr0 * (1 + math.cos(math.pi * step / total))


def run_demo() -> dict[str, float]:
    w, m, v = 2.0, 0.0, 0.0
    target = 0.0
    for t in range(1, 121):
        g = 2 * (w - target)
        lr = cosine_lr(t - 1, 120, lr0=0.1)
        w, m, v = adam_step(w, m, v, g, t, lr=lr)
    return {"w": w}
