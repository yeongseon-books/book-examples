"""Tests for ep03 in Azure App Service Deep Dive."""

from conftest import load_module

run = load_module("ko/03-worker-and-sandbox/step01_sandbox_profile.py", "ep03").run


def test_ep03_windows_sandbox_restriction_profile() -> None:
    """Test ep03 windows sandbox restriction profile."""
    windows = run("windows")
    linux = run("linux")
    assert windows["registry_write_allowed"] is False
    assert windows["gdi_restricted"] is True
    assert linux["boundary"] == "container"
