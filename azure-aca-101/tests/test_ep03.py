"""Tests for ep03 in Azure Aca 101."""

from conftest import load_module

run = load_module("ko/03-first-deploy/step01_first_deploy.py", "ep03").run


def test_ep03_plan_order() -> None:
    """Test ep03 plan order."""
    result = run()
    commands = result["commands"]
    assert result["steps"] == 4
    assert "az group create" in commands[0]
    assert "az acr build" in commands[2]
    assert "az containerapp create" in commands[3]
