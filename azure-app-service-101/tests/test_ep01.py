"""Tests for ep01 in Azure App Service 101."""

from __future__ import annotations

from conftest import load_module


def test_three_plane_classification_and_command() -> None:
    """Test three plane classification and command."""
    mod = load_module("ko/01-what-is-app-service/step01_three_planes.py", "ep01")
    assert mod.classify_plane("https://x.scm.azurewebsites.net") == "scm"
    assert (
        mod.classify_plane("https://management.azure.com/subscriptions/1")
        == "management"
    )
    cmd = mod.build_webapp_show_command("rg", "app").as_string()
    assert "az webapp show" in cmd
