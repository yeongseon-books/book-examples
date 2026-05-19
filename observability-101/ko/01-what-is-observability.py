"""Observability 101 - Episode 1: What is observability."""

from common import ObservabilityStack


def run_demo() -> dict[str, str]:
    """Run demo."""
    stack = ObservabilityStack()
    return stack.handle_request("/health", 0.03, 200)
