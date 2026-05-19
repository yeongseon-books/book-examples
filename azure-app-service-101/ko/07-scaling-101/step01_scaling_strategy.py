"""Azure App Service 101 - Episode 1: Scaling strategy."""

from __future__ import annotations


def choose_scaling(
    cpu_percent: int, memory_percent: int, concurrent_spike: bool
) -> str:
    """Choose scaling."""
    if memory_percent >= 80 and concurrent_spike:
        return "scale_up_then_out"
    if memory_percent >= 80 and not concurrent_spike:
        return "scale_up"
    if concurrent_spike and cpu_percent >= 65:
        return "scale_out"
    return "observe"


def autoscale_rules() -> dict[str, str]:
    """Autoscale rules."""
    return {
        "scale_out": "Percentage CPU > 70 avg 10m",
        "scale_in": "Percentage CPU < 35 avg 20m",
        "bounds": "min=2,max=6,default=2",
    }


def projected_db_connections(instances: int, pool_size: int) -> int:
    """Projected db connections."""
    return instances * pool_size
