"""Generated from book-content article."""

class Tracer:
    def __init__(self, exporter):
        self.exporter = exporter
        self._stack: list[Span] = []

    def start(self, name: str, **attrs) -> Span:
        parent_id = self._stack[-1].span_id if self._stack else None
        trace_id = self._stack[0].trace_id if self._stack else str(uuid.uuid4())
        span = Span(
            span_id=str(uuid.uuid4()),
            trace_id=trace_id,
            parent_id=parent_id,
            name=name,
            started_at=datetime.now(timezone.utc),
            attributes=dict(attrs),
        )
        self._stack.append(span)
        return span

    def end(self, status: str = "ok"):
        span = self._stack.pop()
        span.ended_at = datetime.now(timezone.utc)
        span.status = status
        self.exporter.export(span)
