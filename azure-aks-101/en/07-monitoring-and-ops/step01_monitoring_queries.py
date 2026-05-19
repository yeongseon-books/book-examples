"""Azure Aks 101 - Episode 1: Monitoring queries."""

from __future__ import annotations


def build_kql_queries() -> dict[str, str]:
    """Build kql queries."""
    return {
        "recent_events": "KubeEvents | where not(isempty(Namespace)) | sort by TimeGenerated desc | take 50",
        "pod_logs": "ContainerLogV2 | where PodNamespace == 'default' | where PodName startswith 'fastapi-hello'",
        "failed_pods": "KubePodInventory | where PodStatus == 'Failed' | project TimeGenerated, Namespace, Name",
    }


def build_alert_targets() -> list[str]:
    """Build alert targets."""
    return [
        "deployment_available_replicas",
        "pod_restart_spike",
        "node_not_ready",
        "hpa_max_replica_stuck",
    ]


if __name__ == "__main__":
    print(build_kql_queries())
