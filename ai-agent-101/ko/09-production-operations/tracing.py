"""Generated from book-content article."""

import time
import uuid
from contextlib import contextmanager


class TraceContext:
    """Simple distributed tracing."""

    def __init__(self):
        self.trace_id = str(uuid.uuid4())
        self.spans = []
        self._current_parent = None

    @contextmanager
    def span(self, name: str, **attributes):
        span_id = str(uuid.uuid4())
        parent_id = self._current_parent
        start = time.time()

        self._current_parent = span_id
        try:
            yield span_id
            status = "ok"
            error = None
        except Exception as e:
            status = "error"
            error = str(e)
            raise
        finally:
            self._current_parent = parent_id
            self.spans.append({
                "span_id": span_id,
                "parent_id": parent_id,
                "trace_id": self.trace_id,
                "name": name,
                "start": start,
                "duration_ms": (time.time() - start) * 1000,
                "status": status,
                "error": error,
                "attributes": attributes
            })
