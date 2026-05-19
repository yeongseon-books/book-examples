"""Azure Aks Deep Dive - Episode 1: Keda scaledobject flow."""

from __future__ import annotations

import yaml


def build_scaledobject(
    name: str, deployment: str, queue_name: str
) -> dict[str, object]:
    """Build scaledobject."""
    return {
        "apiVersion": "keda.sh/v1alpha1",
        "kind": "ScaledObject",
        "metadata": {"name": name},
        "spec": {
            "scaleTargetRef": {"name": deployment},
            "minReplicaCount": 0,
            "maxReplicaCount": 20,
            "triggers": [
                {
                    "type": "azure-servicebus",
                    "metadata": {
                        "queueName": queue_name,
                        "messageCount": "5",
                    },
                }
            ],
        },
    }


def scale_to_zero_boundary(current_replicas: int, active: bool) -> int:
    """Scale to zero boundary."""
    if not active:
        return 0
    return 1 if current_replicas == 0 else current_replicas


def scaledobject_yaml(name: str, deployment: str, queue_name: str) -> str:
    """Scaledobject yaml."""
    return yaml.safe_dump(
        build_scaledobject(name, deployment, queue_name), sort_keys=False
    )
