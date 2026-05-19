from common import Tracer


def run_demo() -> tuple[str, int]:
    tracer = Tracer()
    with tracer.start_span("api") as root:
        headers = tracer.inject(root.trace_id, {"user_tier": "pro"})
        trace_id, baggage = tracer.extract(headers)
        with tracer.start_span("db", trace_id=trace_id, baggage=baggage):
            pass
    return root.trace_id, len(tracer.spans)
