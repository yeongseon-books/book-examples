"""Generated from book-content article."""

import threading
from collections import defaultdict


class MetricsCollector:
    """Metrics collector."""

    def __init__(self):
        self._counters = defaultdict(int)
        self._timers = defaultdict(list)
        self._lock = threading.Lock()

    def increment(self, name: str, value: int = 1, **tags):
        key = self._make_key(name, tags)
        with self._lock:
            self._counters[key] += value

    def timing(self, name: str, value_ms: float, **tags):
        key = self._make_key(name, tags)
        with self._lock:
            self._timers[key].append(value_ms)
