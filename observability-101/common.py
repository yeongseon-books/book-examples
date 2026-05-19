"""Shared utilities and domain models for Observability 101."""

from __future__ import annotations

import json
import math
import random
import statistics
import time
import uuid
from collections import defaultdict, deque
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone


class Counter:
    """Counter."""

    def __init__(self) -> None:
        self.value = 0.0

    def inc(self, amount: float = 1.0) -> None:
        """Inc."""
        self.value += float(amount)


class Gauge:
    """Gauge."""

    def __init__(self) -> None:
        self.value = 0.0

    def set(self, value: float) -> None:
        """Set."""
        self.value = float(value)


class Histogram:
    """Histogram."""

    def __init__(self, buckets: list[float] | None = None) -> None:
        self.buckets = sorted(buckets or [0.1, 0.5, 1.0, 2.5, 5.0])
        self.counts = {b: 0 for b in self.buckets}
        self.inf = 0
        self.values: list[float] = []

    def observe(self, value: float) -> None:
        """Observe."""
        v = float(value)
        self.values.append(v)
        for b in self.buckets:
            if v <= b:
                self.counts[b] += 1
                return
        self.inf += 1


class MetricRegistry:
    """Metric registry."""

    def __init__(self) -> None:
        self._counters: dict[tuple[str, tuple[tuple[str, str], ...]], Counter] = {}
        self._gauges: dict[tuple[str, tuple[tuple[str, str], ...]], Gauge] = {}
        self._histograms: dict[tuple[str, tuple[tuple[str, str], ...]], Histogram] = {}

    @staticmethod
    def _key(
        name: str, labels: dict[str, str] | None
    ) -> tuple[str, tuple[tuple[str, str], ...]]:
        """Key."""
        return name, tuple(sorted((labels or {}).items()))

    def counter(self, name: str, labels: dict[str, str] | None = None) -> Counter:
        """Counter."""
        key = self._key(name, labels)
        self._counters.setdefault(key, Counter())
        return self._counters[key]

    def gauge(self, name: str, labels: dict[str, str] | None = None) -> Gauge:
        """Gauge."""
        key = self._key(name, labels)
        self._gauges.setdefault(key, Gauge())
        return self._gauges[key]

    def histogram(
        self,
        name: str,
        labels: dict[str, str] | None = None,
        buckets: list[float] | None = None,
    ) -> Histogram:
        """Histogram."""
        key = self._key(name, labels)
        self._histograms.setdefault(key, Histogram(buckets=buckets))
        return self._histograms[key]

    def export_openmetrics(self) -> str:
        """Export openmetrics."""
        lines: list[str] = []
        for (name, labels), metric in sorted(self._counters.items()):
            lines.append(f"{name}{_fmt_labels(labels)} {metric.value}")
        for (name, labels), metric in sorted(self._gauges.items()):
            lines.append(f"{name}{_fmt_labels(labels)} {metric.value}")
        for (name, labels), metric in sorted(self._histograms.items()):
            cum = 0
            for b in metric.buckets:
                cum += metric.counts[b]
                lines.append(
                    f"{name}_bucket{_fmt_labels(labels + (('le', str(b)),))} {cum}"
                )
            lines.append(
                f"{name}_bucket{_fmt_labels(labels + (('le', '+Inf'),))} {cum + metric.inf}"
            )
            lines.append(f"{name}_count{_fmt_labels(labels)} {len(metric.values)}")
            lines.append(f"{name}_sum{_fmt_labels(labels)} {sum(metric.values):.6f}")
        return "\n".join(lines)


def _fmt_labels(labels: tuple[tuple[str, str], ...]) -> str:
    """Fmt labels."""
    if not labels:
        return ""
    content = ",".join(f'{k}="{v}"' for k, v in labels)
    return "{" + content + "}"


class StructuredLogger:
    """Structured logger."""

    def __init__(self, level: str = "INFO", sample_rate: float = 1.0) -> None:
        self.level = level
        self.sample_rate = max(0.0, min(1.0, sample_rate))
        self._context: dict[str, str] = {}
        self.lines: list[str] = []
        self._rng = random.Random(7)

    def with_context(self, **kwargs: str) -> StructuredLogger:
        """With context."""
        clone = StructuredLogger(self.level, self.sample_rate)
        clone.lines = self.lines
        clone._context = {**self._context, **kwargs}
        return clone

    def log(self, level: str, event: str, **fields: object) -> None:
        """Log."""
        if self._rng.random() > self.sample_rate:
            return
        payload = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "level": level,
            "event": event,
            **self._context,
            **fields,
        }
        self.lines.append(json.dumps(payload, sort_keys=True))


@dataclass
class Span:
    """Span."""

    trace_id: str
    span_id: str
    name: str
    parent_id: str | None
    start: float
    end: float | None = None
    attributes: dict[str, object] = field(default_factory=dict)
    baggage: dict[str, str] = field(default_factory=dict)


class Tracer:
    """Tracer."""

    def __init__(self) -> None:
        self.spans: list[Span] = []
        self._stack: list[Span] = []

    @contextmanager
    def start_span(
        self,
        name: str,
        trace_id: str | None = None,
        baggage: dict[str, str] | None = None,
    ):
        """Start span."""
        parent = self._stack[-1] if self._stack else None
        tid = trace_id or (parent.trace_id if parent else uuid.uuid4().hex)
        span = Span(
            trace_id=tid,
            span_id=uuid.uuid4().hex[:16],
            name=name,
            parent_id=parent.span_id if parent else None,
            start=time.time(),
            baggage=dict(parent.baggage if parent else {}),
        )
        if baggage:
            span.baggage.update(baggage)
        self._stack.append(span)
        try:
            yield span
        finally:
            span.end = time.time()
            self._stack.pop()
            self.spans.append(span)

    @staticmethod
    def inject(trace_id: str, baggage: dict[str, str] | None = None) -> dict[str, str]:
        """Inject."""
        headers = {"x-trace-id": trace_id}
        if baggage:
            headers["x-baggage"] = json.dumps(baggage, sort_keys=True)
        return headers

    @staticmethod
    def extract(headers: dict[str, str]) -> tuple[str | None, dict[str, str]]:
        """Extract."""
        trace_id = headers.get("x-trace-id")
        baggage_raw = headers.get("x-baggage")
        baggage = json.loads(baggage_raw) if baggage_raw else {}
        return trace_id, baggage


class Dashboard:
    """Dashboard."""

    def __init__(self, registry: MetricRegistry) -> None:
        self.registry = registry

    def query_counter(
        self, name: str, label_filter: dict[str, str] | None = None
    ) -> float:
        """Query counter."""
        total = 0.0
        for (n, labels), c in self.registry._counters.items():
            if n != name:
                continue
            d = dict(labels)
            if label_filter and any(d.get(k) != v for k, v in label_filter.items()):
                continue
            total += c.value
        return total

    @staticmethod
    def sparkline(values: list[float]) -> str:
        """Sparkline."""
        blocks = "▁▂▃▄▅▆▇█"
        if not values:
            return ""
        lo, hi = min(values), max(values)
        if math.isclose(lo, hi):
            return blocks[0] * len(values)
        return "".join(blocks[min(7, int((v - lo) / (hi - lo) * 7))] for v in values)

    @staticmethod
    def summary(values: list[float]) -> dict[str, float]:
        """Summary."""
        return {
            "min": min(values),
            "max": max(values),
            "mean": statistics.mean(values),
        }


@dataclass
class AlertRule:
    """Alert rule."""

    name: str
    metric_name: str
    threshold: float
    duration_s: int
    severity: str


class AlertEngine:
    """Alert engine."""

    def __init__(self, dedup_window_s: int = 60) -> None:
        self.rules: list[AlertRule] = []
        self._history: dict[str, deque[tuple[datetime, float]]] = defaultdict(deque)
        self._last_fired: dict[str, datetime] = {}
        self.dedup_window = timedelta(seconds=dedup_window_s)

    def add_rule(self, rule: AlertRule) -> None:
        """Add rule."""
        self.rules.append(rule)

    def evaluate(
        self, metric_point: tuple[str, float], now: datetime
    ) -> list[dict[str, str]]:
        """Evaluate."""
        name, value = metric_point
        fired: list[dict[str, str]] = []
        for rule in self.rules:
            if rule.metric_name != name:
                continue
            hist = self._history[rule.name]
            hist.append((now, value))
            cutoff = now - timedelta(seconds=rule.duration_s)
            while hist and hist[0][0] < cutoff:
                hist.popleft()
            if hist and all(v > rule.threshold for _, v in hist):
                last = self._last_fired.get(rule.name)
                if last is None or now - last > self.dedup_window:
                    self._last_fired[rule.name] = now
                    fired.append({"rule": rule.name, "severity": rule.severity})
        return fired


class OnCallRouter:
    """On call router."""

    def __init__(self, rotations: dict[str, str]) -> None:
        self.rotations = rotations

    def route(self, severity: str) -> str:
        """Route."""
        return self.rotations.get(severity, self.rotations.get("default", "unassigned"))


class SLOTracker:
    """SLO tracker."""

    def __init__(self, target: float) -> None:
        self.target = target
        self.good = 0
        self.total = 0

    def record(self, good_events: int, total_events: int) -> None:
        """Record."""
        self.good += good_events
        self.total += total_events

    def sli(self) -> float:
        """Sli."""
        return self.good / self.total if self.total else 1.0

    def error_budget_remaining(self) -> float:
        """Error budget remaining."""
        used = max(0.0, 1.0 - self.sli())
        budget = 1.0 - self.target
        return max(0.0, budget - used)

    def burn_rate(self) -> float:
        """Burn rate."""
        budget = 1.0 - self.target
        if budget == 0:
            return float("inf")
        return max(0.0, 1.0 - self.sli()) / budget


class CardinalityAnalyzer:
    @staticmethod
    def analyze(
        series: list[tuple[str, dict[str, str]]], threshold: int = 1000
    ) -> dict[str, object]:
        """Analyze."""
        keys = {(name, tuple(sorted(labels.items()))) for name, labels in series}
        count = len(keys)
        return {"unique_series": count, "explosion": count > threshold}


class ObservabilityStack:
    """Observability stack."""

    def __init__(self) -> None:
        self.registry = MetricRegistry()
        self.logger = StructuredLogger()
        self.tracer = Tracer()

    def handle_request(
        self, path: str, latency_s: float, status: int
    ) -> dict[str, str]:
        """Handle request."""
        self.registry.counter(
            "http_requests_total", {"path": path, "status": str(status)}
        ).inc()
        self.registry.histogram("http_latency_seconds", {"path": path}).observe(
            latency_s
        )
        with self.tracer.start_span("request", baggage={"path": path}) as span:
            span.attributes["status"] = status
            self.logger.with_context(trace_id=span.trace_id).log(
                "INFO",
                "request_finished",
                path=path,
                status=status,
                latency_s=latency_s,
            )
        return {"trace_id": span.trace_id}
