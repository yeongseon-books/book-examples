"""Generated from book-content article."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class TraceMetric:
    trace_id: str
    timestamp: datetime
    latency_ms: int
    input_tokens: int
    output_tokens: int
    user_feedback: str | None  # "up", "down", None
    re_asked: bool

def daily_summary(metrics: list[TraceMetric]) -> dict:
    n = len(metrics)
    return {
        "total": n,
        "thumbs_down_rate": sum(1 for m in metrics if m.user_feedback == "down") / n,
        "re_ask_rate": sum(1 for m in metrics if m.re_asked) / n,
        "p95_latency_ms": sorted(m.latency_ms for m in metrics)[int(n * 0.95)],
        "avg_cost_usd": sum(m.input_tokens * 0.000005 + m.output_tokens * 0.000015 for m in metrics) / n,
    }
