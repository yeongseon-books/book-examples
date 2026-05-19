"""Episode 10: Production-ready structure with cache, queue, and observability."""

import sys
from pathlib import Path

from fastapi import FastAPI

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import InMemoryCache, InMemoryQueue, request_id_middleware


def build_app() -> FastAPI:
    """Build app."""
    app = FastAPI()
    cache = InMemoryCache(values={})
    queue = InMemoryQueue(jobs=[])
    request_id_middleware(app)

    @app.post("/tasks/{task_id}")
    def create_task(task_id: str):
        """Create task."""
        cached = cache.get(task_id)
        if cached is not None:
            return {"task_id": task_id, "status": cached, "source": "cache"}
        queue.enqueue("process_task", {"task_id": task_id})
        cache.set(task_id, "queued")
        return {"task_id": task_id, "status": "queued", "source": "queue"}

    @app.get("/ops/metrics")
    def metrics():
        """Metrics."""
        return {"queued_jobs": len(queue.jobs), "cached_keys": len(cache.values)}

    return app
