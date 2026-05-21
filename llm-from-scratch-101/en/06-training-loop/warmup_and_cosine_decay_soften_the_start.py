"""Generated from book-content article."""

import math


def get_lr(it: int, learning_rate: float) -> float:
    warmup_iters = 100
    lr_decay_iters = 5000
    min_lr = learning_rate * 0.1

    if it < warmup_iters:
        return learning_rate * (it + 1) / warmup_iters
    if it > lr_decay_iters:
        return min_lr

    decay_ratio = (it - warmup_iters) / (lr_decay_iters - warmup_iters)
    coeff = 0.5 * (1.0 + math.cos(math.pi * decay_ratio))
    return min_lr + coeff * (learning_rate - min_lr)
