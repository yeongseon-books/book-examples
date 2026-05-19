from __future__ import annotations

from common import build_az_aks_create_command


def build_bootstrap_flow() -> dict[str, list[str]]:
    create = build_az_aks_create_command("rg-aks-101", "aks-101-cluster", 1)
    add_user_pool = [
        "az",
        "aks",
        "nodepool",
        "add",
        "--resource-group",
        "rg-aks-101",
        "--cluster-name",
        "aks-101-cluster",
        "--name",
        "userpool1",
        "--node-count",
        "1",
        "--mode",
        "User",
    ]
    credentials = [
        "az",
        "aks",
        "get-credentials",
        "--resource-group",
        "rg-aks-101",
        "--name",
        "aks-101-cluster",
    ]
    return {
        "create_cluster": create,
        "add_user_pool": add_user_pool,
        "get_credentials": credentials,
    }


if __name__ == "__main__":
    print(build_bootstrap_flow())
