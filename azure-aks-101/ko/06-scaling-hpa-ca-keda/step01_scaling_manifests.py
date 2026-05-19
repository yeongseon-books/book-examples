from __future__ import annotations

from common import dump_yaml


def build_hpa() -> dict[str, object]:
    return {
        "apiVersion": "autoscaling/v2",
        "kind": "HorizontalPodAutoscaler",
        "metadata": {"name": "fastapi-hello"},
        "spec": {
            "scaleTargetRef": {
                "apiVersion": "apps/v1",
                "kind": "Deployment",
                "name": "fastapi-hello",
            },
            "minReplicas": 2,
            "maxReplicas": 10,
            "metrics": [
                {
                    "type": "Resource",
                    "resource": {
                        "name": "cpu",
                        "target": {"type": "Utilization", "averageUtilization": 60},
                    },
                }
            ],
        },
    }


def build_scaled_object() -> dict[str, object]:
    return {
        "apiVersion": "keda.sh/v1alpha1",
        "kind": "ScaledObject",
        "metadata": {"name": "orders-scaler"},
        "spec": {
            "scaleTargetRef": {"name": "orders-deployment"},
            "minReplicaCount": 0,
            "maxReplicaCount": 20,
            "triggers": [
                {
                    "type": "azure-servicebus",
                    "metadata": {"queueName": "orders", "messageCount": "5"},
                    "authenticationRef": {"name": "servicebus-trigger-auth"},
                }
            ],
        },
    }


def build_hpa_yaml() -> str:
    return dump_yaml(build_hpa())


if __name__ == "__main__":
    print(build_hpa_yaml())
