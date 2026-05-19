"""Azure Aks Deep Dive - Episode 1: Network mode model."""

from __future__ import annotations

import yaml


def build_network_profile(mode: str) -> dict[str, str]:
    """Build network profile."""
    if mode == "overlay":
        return {
            "networkPlugin": "azure",
            "networkPluginMode": "overlay",
            "podCidr": "10.244.0.0/16",
        }
    if mode == "pod-subnet":
        return {
            "networkPlugin": "azure",
            "networkPluginMode": "transparent",
            "podSubnet": "10.10.0.0/16",
        }
    return {
        "networkPlugin": "azure",
        "networkPluginMode": "legacy",
        "nodeSubnet": "10.0.0.0/16",
    }


def network_profile_yaml(mode: str) -> str:
    """Network profile yaml."""
    return yaml.safe_dump(
        {"networkProfile": build_network_profile(mode)}, sort_keys=False
    )
