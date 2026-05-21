"""Generated from book-content article."""

import signal
from contextlib import contextmanager

class TimeoutError(Exception):
    pass

@contextmanager
def time_limit(seconds: int):
    """Limit function execution time."""
    def signal_handler(signum, frame):
        raise TimeoutError(f"execution exceeded {seconds}s")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

def run_tool_with_limits(tool_fn, *args, timeout: int = 30, **kwargs):
    """Run a tool with timeout and exception handling."""
    try:
        with time_limit(timeout):
            return tool_fn(*args, **kwargs)
    except TimeoutError as e:
        raise ToolExecutionError("tool", str(e), recoverable=True)
    except Exception as e:
        raise ToolExecutionError("tool", str(e), recoverable=False)
