"""Devops 101 - Episode 8: Logging and analysis."""

from __future__ import annotations

import json
from collections import Counter


def parse_json_logs(lines: list[str]) -> list[dict[str, object]]:
    """Parse json logs."""
    return [json.loads(line) for line in lines]


def latency_percentile(logs: list[dict[str, object]], percentile: int) -> float:
    """Latency percentile."""
    latencies = sorted(float(log["latency_ms"]) for log in logs)
    if not latencies:
        return 0.0
    index = min(int(percentile / 100 * len(latencies)), len(latencies) - 1)
    return latencies[index]


def top_error_patterns(
    logs: list[dict[str, object]], n: int = 3
) -> list[tuple[str, int]]:
    """Top error patterns."""
    counter = Counter(
        str(log.get("error_code", "UNKNOWN"))
        for log in logs
        if log.get("level") == "ERROR"
    )
    return counter.most_common(n)
