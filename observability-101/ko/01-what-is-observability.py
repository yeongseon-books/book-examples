from common import ObservabilityStack


def run_demo() -> dict[str, str]:
    stack = ObservabilityStack()
    return stack.handle_request("/health", 0.03, 200)
