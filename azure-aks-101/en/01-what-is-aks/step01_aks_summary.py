"""Azure Aks 101 - Episode 1: Aks summary."""

from __future__ import annotations

from common import build_az_aks_create_command, shell_join


def build_example() -> dict[str, object]:
    """Build example."""
    command = build_az_aks_create_command("rg-aks-101", "aks-101-cluster", 1)
    return {
        "concept": "aks-shared-responsibility",
        "control_plane_managed_by": "azure",
        "user_responsibility": ["node_pool", "workload", "network_policy", "cost"],
        "command_tokens": command,
        "command_preview": shell_join(command),
    }


if __name__ == "__main__":
    print(build_example())
