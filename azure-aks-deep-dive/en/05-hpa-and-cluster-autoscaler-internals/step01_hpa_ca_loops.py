"""Azure Aks Deep Dive - Episode 1: Hpa ca loops."""

from __future__ import annotations

import math


def desired_replicas(
    current_replicas: int, current_metric: float, target_metric: float
) -> int:
    """Desired replicas."""
    ratio = current_metric / target_metric
    return max(1, math.ceil(current_replicas * ratio))


def ca_scale_up_needed(pending_pods: int, free_node_slots: int) -> bool:
    """Ca scale up needed."""
    return pending_pods > free_node_slots


def aks_autoscaler_profile() -> dict[str, str]:
    """Aks autoscaler profile."""
    return {
        "scan-interval": "10s",
        "scale-down-unneeded-time": "10m",
        "scale-down-delay-after-add": "10m",
    }
