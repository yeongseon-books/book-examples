"""Tests for ep06 in Ai Web Dev 101."""

from conftest import load_module

module = load_module("ko/06-deploy/step01_deploy_checklist.py", "ep06")
deployment_checklist = module.deployment_checklist
estimate_monthly_cost = module.estimate_monthly_cost


def test_ep06_deploy_checklist_and_cost() -> None:
    """Test ep06 deploy checklist and cost."""
    status = deployment_checklist(True, False, True)
    assert status["ready"] is False
    assert "secrets" in status["missing"]
    assert estimate_monthly_cost(100, 200, 0.002) > 0
