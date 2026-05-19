"""Sre 101 - Episode 5: Monitoring windows."""

from common import percentile


def aggregate_window(latencies_ms: list[float], window_seconds: int) -> dict:
    """Aggregate window."""
    count = len(latencies_ms)
    rate = count / max(1, window_seconds)
    return {
        "count": count,
        "rate": rate,
        "p50": percentile(latencies_ms, 50),
        "p95": percentile(latencies_ms, 95),
        "p99": percentile(latencies_ms, 99),
    }
