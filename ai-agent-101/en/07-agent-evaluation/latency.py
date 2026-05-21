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

# Example usage
with measure_latency() as m:
    t0 = time.time()
    plan = agent.plan(user_input)
    record_step(m, "planning", time.time() - t0)

    t0 = time.time()
    tools_result = agent.execute_tools(plan)
    record_step(m, "tool_calls", time.time() - t0)

    t0 = time.time()
    final = agent.synthesize(tools_result)
    record_step(m, "synthesis", time.time() - t0)

print(f"total {m['total_seconds']:.2f}s, per-step: {m['steps']}")
