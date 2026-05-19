"""Azure App Service Deep Dive - Episode 1: Autoscale loop."""

from __future__ import annotations

from common import autoscale_decision


def evaluate(cpu: float, http_queue: float) -> str:
    # Simplified autoscale behavior: OR for out, conservative in.
    """Evaluate."""
    return autoscale_decision({"cpu": cpu, "http_queue": http_queue})


if __name__ == "__main__":
    print(evaluate(81.0, 2.0))
