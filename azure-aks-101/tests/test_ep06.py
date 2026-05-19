"""Tests for ep06 in Azure Aks 101."""

from conftest import load_module


def test_ep06_hpa_and_keda_scaled_object() -> None:
    """Test ep06 hpa and keda scaled object."""
    ko = load_module("ko/06-scaling-hpa-ca-keda/step01_scaling_manifests.py", "ep06_ko")
    en = load_module("en/06-scaling-hpa-ca-keda/step01_scaling_manifests.py", "ep06_en")
    for module in (ko, en):
        hpa = module.build_hpa()
        scaled = module.build_scaled_object()
        assert hpa["kind"] == "HorizontalPodAutoscaler"
        assert hpa["spec"]["metrics"][0]["resource"]["name"] == "cpu"
        assert scaled["spec"]["minReplicaCount"] == 0
        assert scaled["spec"]["triggers"][0]["type"] == "azure-servicebus"
