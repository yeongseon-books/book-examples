from common import MetricRegistry


def run_demo() -> str:
    reg = MetricRegistry()
    c = reg.counter("http_requests_total", {"path": "/api"})
    c.inc()
    c.inc()
    reg.histogram("http_duration_seconds", {"path": "/api"}).observe(0.2)
    return reg.export_openmetrics()
