"""Serverless 101 - Episode 4: Cold start."""

from __future__ import annotations

from common import *


def run_demo():
    """Run demo."""
    if 4 == 1:
        return ep01_handler({"episode": 4}, {"request_id": "demo-4"})
    if 4 == 2:
        rt = FaaSRuntime()
        rt.register("hello", lambda e, c: {"echo": e, "request_id": c["request_id"]})
        return rt.dispatch("hello", {"msg": "hi"}, {"request_id": "r2"})
    if 4 == 3:
        router = EventRouter()
        router.on(HTTPEvent, lambda e: {"kind": "http", "path": e.path})
        return router.dispatch(HTTPEvent(path="/ping", method="GET", body={}))
    if 4 == 4:
        sim = ColdStartSimulator(capacity=2)
        first = sim.invoke("fn")
        second = sim.invoke("fn")
        return {"first": first, "second": second}
    if 4 == 5:
        sim = AutoScalerSimulator(max_containers=3, queue_limit=2)
        return sim.process_burst(concurrent_requests=8)
    if 4 == 6:
        store = ExternalKVStore()
        store.put("user:1", {"name": "kim"})
        first = store.seen_idempotency_key("idem-1")
        second = store.seen_idempotency_key("idem-1")
        return {"user": store.get("user:1"), "first_seen": first, "second_seen": second}
    if 4 == 7:
        pool = WorkerPool(worker_count=2, max_retries=2)
        pool.submit("m1", fail_times=1)
        pool.run()
        return {"processed": pool.processed, "dead_letter": pool.dead_letter}
    if 4 == 8:
        obs = Observability()
        obs.record(lambda e, c: {"ok": True, "rid": c["request_id"]}, {"x": 1})
        return {"metrics": obs.metrics(), "logs": obs.logs}
    if 4 == 9:
        calls = [
            {"memory_mb": 128, "duration_ms": 120},
            {"memory_mb": 512, "duration_ms": 240},
        ]
        return {"total_cost": aggregate_cost(calls)}
    if 4 == 10:
        app = OrderSystem()
        return app.run_demo()
    raise ValueError("unsupported episode")


if __name__ == "__main__":
    print(run_demo())
