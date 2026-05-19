import math


def linear(x: float, a: float = 2.0, b: float = 1.0) -> float:
    return a * x + b


def relu(x: float) -> float:
    return max(0.0, x)


def relu_grad(x: float) -> float:
    return 1.0 if x > 0 else 0.0


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def run_demo() -> dict[str, float]:
    return {
        "linear_slope": 2.0,
        "relu_neg": relu(-1.0),
        "relu_pos_grad": relu_grad(3.0),
        "sigmoid_0": sigmoid(0.0),
    }
