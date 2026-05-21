"""Generated from book-content article."""

import random

def estimate_tail_prob(trials: int = 100000) -> float:
    cnt = 0
    for _ in range(trials):
        x = random.random() + random.random()
        if x > 1.6:
            cnt += 1
    return cnt / trials
