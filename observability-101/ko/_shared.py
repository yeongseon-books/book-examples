"""Observability 101 - Shared."""

from datetime import datetime, timedelta, timezone

from common import (
    AlertEngine,
    AlertRule,
    CardinalityAnalyzer,
    Dashboard,
    MetricRegistry,
    ObservabilityStack,
    OnCallRouter,
    SLOTracker,
    StructuredLogger,
    Tracer,
)


def run01() -> dict[str, str]:
    """Run01."""
    return ObservabilityStack().handle_request("/health", 0.03, 200)


def run02() -> tuple[str, int, int]:
    """Run02."""
    reg = MetricRegistry()
    reg.counter("requests_total", {"path": "/checkout"}).inc()
    log = StructuredLogger()
    tracer = Tracer()
    with tracer.start_span("checkout") as span:
        log.with_context(trace_id=span.trace_id).log("INFO", "checkout_started")
    return reg.export_openmetrics(), len(log.lines), len(tracer.spans)


def run03() -> str:
    """Run03."""
    reg = MetricRegistry()
    c = reg.counter("http_requests_total", {"path": "/api"})
    c.inc()
    c.inc()
    reg.histogram("http_duration_seconds", {"path": "/api"}).observe(0.2)
    return reg.export_openmetrics()


def run04() -> str:
    """Run04."""
    log = StructuredLogger(sample_rate=1.0).with_context(service="auth")
    log.log("ERROR", "login_failed", user_id="42", reason="bad_password")
    return log.lines[0]


def run05() -> tuple[str, int]:
    """Run05."""
    tracer = Tracer()
    with tracer.start_span("api") as root:
        headers = tracer.inject(root.trace_id, {"user_tier": "pro"})
        trace_id, baggage = tracer.extract(headers)
        with tracer.start_span("db", trace_id=trace_id, baggage=baggage):
            pass
    return root.trace_id, len(tracer.spans)


def run06() -> tuple[str, dict[str, float]]:
    """Run06."""
    values = [0.2, 0.3, 0.5, 0.4, 0.9]
    return Dashboard.sparkline(values), Dashboard.summary(values)


def run07() -> tuple[list[dict[str, str]], str]:
    """Run07."""
    engine = AlertEngine(dedup_window_s=60)
    engine.add_rule(AlertRule("high_error", "error_rate", 0.05, 120, "page"))
    now = datetime.now(timezone.utc)
    fired: list[dict[str, str]] = []
    for i in range(4):
        fired.extend(
            engine.evaluate(("error_rate", 0.10), now + timedelta(seconds=i * 40))
        )
    router = OnCallRouter(
        {"page": "primary-rotation", "ticket": "daytime-rotation", "default": "triage"}
    )
    return fired, router.route("page")


def run08() -> tuple[float, float, float]:
    """Run08."""
    tracker = SLOTracker(target=0.999)
    tracker.record(9980, 10000)
    return tracker.sli(), tracker.error_budget_remaining(), tracker.burn_rate()


def run09() -> dict[str, object]:
    """Run09."""
    series = [
        ("http_requests_total", {"path": f"/p/{i}", "status": "200"})
        for i in range(1101)
    ]
    return CardinalityAnalyzer.analyze(series, threshold=1000)


def run10() -> tuple[str, int, int]:
    """Run10."""
    stack = ObservabilityStack()
    stack.handle_request("/checkout", 0.45, 200)
    stack.handle_request("/checkout", 0.90, 500)
    return (
        stack.registry.export_openmetrics(),
        len(stack.logger.lines),
        len(stack.tracer.spans),
    )
