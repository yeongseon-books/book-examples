"""Generated from book-content article."""

import time
from contextlib import contextmanager


@contextmanager
def measure_latency():
    """Latency-measuring context manager."""
    start = time.time()
    metrics = {"steps": []}
    yield metrics
    metrics["total_seconds"] = time.time() - start

def record_step(metrics: dict, step_name: str, duration: float):
    metrics["steps"].append({"name": step_name, "seconds": duration})
