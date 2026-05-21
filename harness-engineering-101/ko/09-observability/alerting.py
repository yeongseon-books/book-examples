"""Generated from book-content article."""

def should_alert(metrics: AgentMetrics, baseline: AgentMetrics) -> str | None:
    if metrics.error_rate > baseline.error_rate * 2 and metrics.error_rate > 0.05:
        return f"Error rate spike: {metrics.error_rate:.1%}"
    if metrics.p95_latency_ms > baseline.p95_latency_ms * 3:
        return f"P95 latency spike: {metrics.p95_latency_ms:.0f}ms"
    if metrics.avg_cost_usd > baseline.avg_cost_usd * 5:
        return f"Cost spike: ${metrics.avg_cost_usd:.4f}/run"
    return None
