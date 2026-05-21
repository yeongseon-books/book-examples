"""Generated from book-content article."""

import random
import time
from collections.abc import Callable
from typing import Tuple, Type


def retry_with_backoff(
    fn: Callable,
    max_attempts: int = 3,
    initial_delay: float = 1.0,
    max_delay: float = 30.0,
    exponential_base: float = 2.0,
    jitter: bool = True,
    retryable_exceptions: tuple[type[Exception], ...] = (Exception,)
):
    """Retry with exponential backoff."""
    last_exception = None

    for attempt in range(max_attempts):
        try:
            return fn()
        except retryable_exceptions as e:
            last_exception = e
            if attempt == max_attempts - 1:
                break

            delay = min(initial_delay * (exponential_base ** attempt), max_delay)
            if jitter:
                delay = delay * (0.5 + random.random())

            print(f"attempt {attempt + 1} failed: {e}. retrying in {delay:.1f}s")
            time.sleep(delay)

    raise last_exception
