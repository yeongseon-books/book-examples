from __future__ import annotations

from common import *


def run_demo():
    if 5 == 1:
        return ep01_handler({"episode": 5}, {"request_id": "demo-5"})
    if 5 == 2:
        rt = FaaSRuntime()
        rt.register("hello", lambda e, c: {"echo": e, "request_id": c["request_id"]})
        return rt.dispatch("hello", {"msg": "hi"}, {"request_id": "r2"})
    if 5 == 3:
        router = EventRouter()
        router.on(HTTPEvent, lambda e: {"kind": "http", "path": e.path})
        return router.dispatch(HTTPEvent(path="/ping", method="GET", body={}))
    if 5 == 4:
        sim = ColdStartSimulator(capacity=2)
        first = sim.invoke("fn")
        second = sim.invoke("fn")
        return {"first": first, "second": second}
    if 5 == 5:
        sim = AutoScalerSimulator(max_containers=3, queue_limit=2)
        return sim.process_burst(concurrent_requests=8)
    if 5 == 6:
        store = ExternalKVStore()
        store.put("user:1", {"name": "kim"})
        first = store.seen_idempotency_key("idem-1")
        second = store.seen_idempotency_key("idem-1")
        return {"user": store.get("user:1"), "first_seen": first, "second_seen": second}
    if 5 == 7:
        pool = WorkerPool(worker_count=2, max_retries=2)
        pool.submit("m1", fail_times=1)
        pool.run()
        return {"processed": pool.processed, "dead_letter": pool.dead_letter}
    if 5 == 8:
        obs = Observability()
        obs.record(lambda e, c: {"ok": True, "rid": c["request_id"]}, {"x": 1})
        return {"metrics": obs.metrics(), "logs": obs.logs}
    if 5 == 9:
        calls = [{"memory_mb": 128, "duration_ms": 120}, {"memory_mb": 512, "duration_ms": 240}]
        return {"total_cost": aggregate_cost(calls)}
    if 5 == 10:
        app = OrderSystem()
        return app.run_demo()
    raise ValueError("unsupported episode")


if __name__ == "__main__":
    print(run_demo())
