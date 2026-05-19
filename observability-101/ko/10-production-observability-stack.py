"""Observability 101 - Episode 10: Production observability stack."""

from common import ObservabilityStack


def run_demo() -> tuple[str, int, int]:
    """Run demo."""
    stack = ObservabilityStack()
    stack.handle_request("/checkout", 0.45, 200)
    stack.handle_request("/checkout", 0.90, 500)
    return (
        stack.registry.export_openmetrics(),
        len(stack.logger.lines),
        len(stack.tracer.spans),
    )
