from __future__ import annotations


def build_node_pool_layout() -> dict[str, object]:
    return {
        "system_pool": {"name": "syspool", "mode": "System", "min_nodes": 2},
        "user_pools": [
            {"name": "userpool-api", "mode": "User", "vm_size": "Standard_D4s_v5"},
            {"name": "userpool-batch", "mode": "User", "spot": True},
        ],
        "rules": [
            "critical addons on system pool",
            "application workloads on user pools",
            "spot only for interruptible workloads",
        ],
    }


if __name__ == "__main__":
    print(build_node_pool_layout())
