"""Shared utilities and domain models for Serverless 101."""

from __future__ import annotations

import queue
import random
import statistics
import threading
import time
import uuid
from collections import OrderedDict, deque
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any


def ep01_handler(event: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
    """Ep01 handler."""
    return {
        "ok": True,
        "request_id": context.get("request_id", "unknown"),
        "echo": event,
    }


class FaaSRuntime:
    """Faa s runtime."""

    def __init__(self) -> None:
        self._handlers: dict[str, Callable[[dict[str, Any], dict[str, Any]], Any]] = {}

    def register(
        self, name: str, handler: Callable[[dict[str, Any], dict[str, Any]], Any]
    ) -> None:
        """Register."""
        self._handlers[name] = handler

    def dispatch(
        self, name: str, event: dict[str, Any], context: dict[str, Any]
    ) -> Any:
        """Dispatch."""
        if name not in self._handlers:
            raise KeyError(f"handler not found: {name}")
        return self._handlers[name](event, context)


@dataclass
class HTTPEvent:
    """HTTP event."""

    path: str
    method: str
    body: dict[str, Any]


@dataclass
class S3Event:
    """S3 event."""

    bucket: str
    key: str


@dataclass
class QueueEvent:
    """Queue event."""

    queue_name: str
    payload: dict[str, Any]


@dataclass
class ScheduleEvent:
    """Schedule event."""

    cron: str
    timestamp: float


class EventRouter:
    """Event router."""

    def __init__(self) -> None:
        self._routes: dict[type[Any], Callable[[Any], Any]] = {}

    def on(self, event_type: type[Any], handler: Callable[[Any], Any]) -> None:
        """On."""
        self._routes[event_type] = handler

    def dispatch(self, event: Any) -> Any:
        """Dispatch."""
        for event_type, handler in self._routes.items():
            if isinstance(event, event_type):
                return handler(event)
        raise KeyError(f"no route for {type(event).__name__}")


@dataclass
class Container:
    """Container."""

    container_id: str
    cold: bool = True
    invoke_count: int = 0


class ColdStartSimulator:
    """Cold start simulator."""

    def __init__(
        self, capacity: int = 2, cold_start_ms: int = 120, warm_ms: int = 8
    ) -> None:
        self.capacity = capacity
        self.cold_start_ms = cold_start_ms
        self.warm_ms = warm_ms
        self._containers: OrderedDict[str, Container] = OrderedDict()

    def invoke(self, key: str) -> dict[str, Any]:
        """Invoke."""
        if key in self._containers:
            c = self._containers.pop(key)
            self._containers[key] = c
            c.invoke_count += 1
            c.cold = False
            return {
                "container_id": c.container_id,
                "cold_start": False,
                "latency_ms": self.warm_ms,
            }

        if len(self._containers) >= self.capacity:
            self._containers.popitem(last=False)
        c = Container(
            container_id=f"c-{uuid.uuid4().hex[:8]}", cold=True, invoke_count=1
        )
        self._containers[key] = c
        return {
            "container_id": c.container_id,
            "cold_start": True,
            "latency_ms": self.cold_start_ms,
        }


class AutoScalerSimulator:
    """Auto scaler simulator."""

    def __init__(self, max_containers: int, queue_limit: int) -> None:
        self.max_containers = max_containers
        self.queue_limit = queue_limit

    def process_burst(self, concurrent_requests: int) -> dict[str, int]:
        """Process burst."""
        active = min(concurrent_requests, self.max_containers)
        waiting = max(0, concurrent_requests - active)
        queued = min(waiting, self.queue_limit)
        dropped = max(0, waiting - queued)
        return {"active": active, "queued": queued, "dropped": dropped}


class ExternalKVStore:
    """External k v store."""

    def __init__(self) -> None:
        self._data: dict[str, Any] = {}
        self._idempotency: set[str] = set()

    def put(self, key: str, value: Any) -> None:
        """Put."""
        self._data[key] = value

    def get(self, key: str) -> Any:
        """Get."""
        return self._data.get(key)

    def seen_idempotency_key(self, key: str) -> bool:
        """Seen idempotency key."""
        if key in self._idempotency:
            return True
        self._idempotency.add(key)
        return False


def stateless_counter(event: dict[str, Any], context: dict[str, Any]) -> int:
    """Stateless counter."""
    value = event.get("value", 1)
    return value


class WorkerPool:
    """Worker pool."""

    def __init__(
        self, worker_count: int = 2, max_retries: int = 2, base_backoff: float = 0.001
    ) -> None:
        self.worker_count = worker_count
        self.max_retries = max_retries
        self.base_backoff = base_backoff
        self.q: queue.Queue[dict[str, Any]] = queue.Queue()
        self.processed: list[str] = []
        self.dead_letter: list[str] = []

    def submit(self, message_id: str, fail_times: int = 0) -> None:
        """Submit."""
        self.q.put({"id": message_id, "fail_times": fail_times, "attempt": 0})

    def _handle(self, item: dict[str, Any]) -> bool:
        """Handle."""
        return item["attempt"] >= item["fail_times"]

    def run(self) -> None:
        """Run."""

        def worker() -> None:
            """Worker."""
            while True:
                try:
                    item = self.q.get_nowait()
                except queue.Empty:
                    return
                ok = self._handle(item)
                if ok:
                    self.processed.append(item["id"])
                else:
                    item["attempt"] += 1
                    if item["attempt"] > self.max_retries:
                        self.dead_letter.append(item["id"])
                    else:
                        time.sleep(self.base_backoff * (2 ** (item["attempt"] - 1)))
                        self.q.put(item)
                self.q.task_done()

        threads = [threading.Thread(target=worker) for _ in range(self.worker_count)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()


@dataclass
class Observability:
    """Observability."""

    invocations: int = 0
    errors: int = 0
    latencies: list[float] = field(default_factory=list)
    logs: list[dict[str, Any]] = field(default_factory=list)

    def record(
        self,
        handler: Callable[[dict[str, Any], dict[str, Any]], Any],
        event: dict[str, Any],
    ) -> Any:
        """Record."""
        request_id = str(uuid.uuid4())
        trace_id = str(uuid.uuid4())
        context = {"request_id": request_id, "trace_id": trace_id}
        start = time.perf_counter()
        self.invocations += 1
        status = "ok"
        try:
            result = handler(event, context)
            return result
        except Exception:
            self.errors += 1
            status = "error"
            raise
        finally:
            latency = (time.perf_counter() - start) * 1000
            self.latencies.append(latency)
            self.logs.append(
                {
                    "request_id": request_id,
                    "trace_id": trace_id,
                    "status": status,
                    "latency_ms": latency,
                }
            )

    def metrics(self) -> dict[str, float]:
        """Metrics."""
        if not self.latencies:
            return {
                "invocations": float(self.invocations),
                "errors": float(self.errors),
                "p50_ms": 0.0,
                "p99_ms": 0.0,
            }
        p50 = statistics.median(self.latencies)
        sorted_lat = sorted(self.latencies)
        idx = max(0, min(len(sorted_lat) - 1, int(len(sorted_lat) * 0.99) - 1))
        p99 = sorted_lat[idx]
        return {
            "invocations": float(self.invocations),
            "errors": float(self.errors),
            "p50_ms": p50,
            "p99_ms": p99,
        }


def compute_cost(
    memory_mb: int, duration_ms: int, price_per_gb_sec: float = 0.0000166667
) -> float:
    """Compute cost."""
    gb = memory_mb / 1024
    sec = duration_ms / 1000
    return gb * sec * price_per_gb_sec


def aggregate_cost(invocations: list[dict[str, int]]) -> float:
    """Aggregate cost."""
    return sum(compute_cost(i["memory_mb"], i["duration_ms"]) for i in invocations)


class OrderSystem:
    """Order system."""

    def __init__(self) -> None:
        self.runtime = FaaSRuntime()
        self.router = EventRouter()
        self.pool = WorkerPool(worker_count=2)
        self.obs = Observability()
        self.orders: deque[str] = deque()
        self.runtime.register("create_order", self._create_order)
        self.router.on(HTTPEvent, self._on_http)
        self.router.on(QueueEvent, self._on_queue)

    def _create_order(
        self, event: dict[str, Any], context: dict[str, Any]
    ) -> dict[str, Any]:
        """Create order."""
        order_id = event["order_id"]
        self.orders.append(order_id)
        self.pool.submit(order_id)
        return {
            "accepted": True,
            "order_id": order_id,
            "request_id": context["request_id"],
        }

    def _on_http(self, event: HTTPEvent) -> dict[str, Any]:
        """On http."""
        return self.obs.record(
            lambda e, c: self.runtime.dispatch("create_order", e, c), event.body
        )

    def _on_queue(self, event: QueueEvent) -> dict[str, Any]:
        """On queue."""
        self.pool.submit(event.payload["order_id"])
        self.pool.run()
        return {"processed": list(self.pool.processed)}

    def run_demo(self) -> dict[str, Any]:
        """Run demo."""
        self.router.dispatch(
            HTTPEvent(
                path="/orders",
                method="POST",
                body={"order_id": f"ord-{random.randint(100, 999)}"},
            )
        )
        self.pool.run()
        return {
            "orders": list(self.orders),
            "processed": list(self.pool.processed),
            "metrics": self.obs.metrics(),
        }
