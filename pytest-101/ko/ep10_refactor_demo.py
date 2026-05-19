"""Pytest 101 - Episode 10: Refactor demo."""

GLOBAL_QUEUE: list[str] = []


def enqueue_global(message: str) -> None:
    """Enqueue global."""
    GLOBAL_QUEUE.append(message)


def enqueue_with_dependency(message: str, sink) -> None:
    """Enqueue with dependency."""
    sink.append(message)
