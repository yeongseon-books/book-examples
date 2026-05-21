"""Generated from book-content article."""

from collections import defaultdict
import threading

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

    def _make_key(self, name: str, tags: dict) -> str:
        if not tags:
            return name
        tag_str = ",".join(f"{k}={v}" for k, v in sorted(tags.items()))
        return f"{name}[{tag_str}]"

    def report(self) -> dict:
        with self._lock:
            return {
                "counters": dict(self._counters),
                "timers": {
                    k: {
                        "count": len(v),
                        "avg_ms": sum(v) / len(v),
                        "p95_ms": sorted(v)[int(len(v) * 0.95)] if v else 0
                    }
                    for k, v in self._timers.items()
                }
            }

# Example usage — core metrics to track
metrics = MetricsCollector()
metrics.increment("agent.requests", status="success")
metrics.increment("agent.tool_calls", tool="search")
metrics.increment("agent.errors", type="timeout")
metrics.timing("agent.request.duration", 1234, model="gpt-4o")
metrics.timing("agent.tool.duration", 234, tool="search")
