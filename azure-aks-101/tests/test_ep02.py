"""Tests for ep02 in Azure Aks 101."""

from conftest import load_module


def test_ep02_node_pool_separation_rules() -> None:
    """Test ep02 node pool separation rules."""
    ko = load_module("ko/02-cluster-architecture/step01_node_pool_layout.py", "ep02_ko")
    en = load_module("en/02-cluster-architecture/step01_node_pool_layout.py", "ep02_en")
    for module in (ko, en):
        layout = module.build_node_pool_layout()
        assert layout["system_pool"]["mode"] == "System"
        assert layout["user_pools"][0]["mode"] == "User"
        assert "spot only for interruptible workloads" in layout["rules"]
