"""Tests for ep01 in Azure Functions Deep Dive."""

from conftest import load_module

ko_run = load_module("ko/01-host-bootstrap/step01_host_bootstrap.py", "ko_ep01").run
en_run = load_module("en/01-host-bootstrap/step01_host_bootstrap.py", "en_ep01").run


def test_ep01_host_bootstrap_merges_env_override() -> None:
    """Test ep01 host bootstrap merges env override."""
    ko_result = ko_run()
    en_result = en_run()
    assert ko_result["resolved"]["function_timeout"] == "00:02:00"
    assert en_result["resolved"]["worker_process_count"] == 2
