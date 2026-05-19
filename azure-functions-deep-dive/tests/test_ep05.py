"""Tests for ep05 in Azure Functions Deep Dive."""

from conftest import load_module

ko_run = load_module("ko/05-scaling-internals/step01_scaling.py", "ko_ep05").run
en_run = load_module("en/05-scaling-internals/step01_scaling.py", "en_ep05").run


def test_ep05_target_based_scaling() -> None:
    """Test ep05 target based scaling."""
    ko_result = ko_run(backlog=95, target_per_instance=16, current_instances=2)
    en_result = en_run(backlog=5, target_per_instance=16, current_instances=3)
    assert ko_result["desired_instances"] == 6
    assert en_result["desired_instances"] == 3
