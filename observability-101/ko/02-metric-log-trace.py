from common import MetricRegistry, StructuredLogger, Tracer


def run_demo() -> tuple[str, int, int]:
    reg = MetricRegistry()
    reg.counter("requests_total", {"path": "/checkout"}).inc()
    log = StructuredLogger()
    tracer = Tracer()
    with tracer.start_span("checkout") as span:
        log.with_context(trace_id=span.trace_id).log("INFO", "checkout_started")
    return reg.export_openmetrics(), len(log.lines), len(tracer.spans)
