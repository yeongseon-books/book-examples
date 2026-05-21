"""Generated from book-content article."""

import math
from collections import deque

class AnomalyDetector:
    def __init__(self, window: int = 60):
        self.window = window
        self.history: dict[str, deque] = {}

    def observe(self, user_id: str, rate: float) -> bool:
        h = self.history.setdefault(user_id, deque(maxlen=self.window))
        h.append(rate)
        if len(h) < 10:
            return False
        mean = sum(h) / len(h)
        var = sum((x - mean) ** 2 for x in h) / len(h)
        sd = math.sqrt(var) or 1
        z = (rate - mean) / sd
        return z > 3.0
