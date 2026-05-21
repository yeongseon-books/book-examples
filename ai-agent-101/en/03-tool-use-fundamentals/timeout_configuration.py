"""Generated from book-content article."""

import signal
from contextlib import contextmanager


@contextmanager
def timeout(seconds: int):
    """Limit function execution time."""
    def timeout_handler(signum, frame):
        raise TimeoutError(f"Operation timed out after {seconds} seconds")

    # Set timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(seconds)

    try:
        yield
    finally:
        # Clear timeout
        signal.alarm(0)

# Usage example
try:
    with timeout(10):
        result = execute_tool("slow_api_call", {"param": "value"})
except TimeoutError:
    result = {"success": False, "error": "Tool execution timeout"}
