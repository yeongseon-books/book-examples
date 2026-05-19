from common import ObservabilityStack


def run_demo() -> tuple[str, int, int]:
    stack = ObservabilityStack()
    stack.handle_request("/checkout", 0.45, 200)
    stack.handle_request("/checkout", 0.90, 500)
    return (
        stack.registry.export_openmetrics(),
        len(stack.logger.lines),
        len(stack.tracer.spans),
    )
