from __future__ import annotations

from collections import defaultdict, deque


class MetricStore:
    def __init__(self, window: int = 5) -> None:
        self.window = window
        self.counters = defaultdict(int)
        self.gauges = defaultdict(float)
        self.histograms = defaultdict(lambda: deque(maxlen=window))

    def inc(self, name: str, amount: int = 1) -> None:
        self.counters[name] += amount

    def set_gauge(self, name: str, value: float) -> None:
        self.gauges[name] = value

    def observe(self, name: str, value: float) -> None:
        self.histograms[name].append(value)


class AlertRule:
    def __init__(self, metric: str, threshold: float, mode: str = "above") -> None:
        self.metric = metric
        self.threshold = threshold
        self.mode = mode

    def evaluate(self, store: MetricStore) -> bool:
        samples = list(store.histograms[self.metric])
        if not samples:
            return False
        average = sum(samples) / len(samples)
        if self.mode == "above":
            return average > self.threshold
        return average < self.threshold
