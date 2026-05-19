GLOBAL_QUEUE: list[str] = []


def enqueue_global(message: str) -> None:
    GLOBAL_QUEUE.append(message)


def enqueue_with_dependency(message: str, sink) -> None:
    sink.append(message)
