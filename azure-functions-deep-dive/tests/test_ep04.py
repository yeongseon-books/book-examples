"""Tests for ep04 in Azure Functions Deep Dive."""

from conftest import load_module

ko_run = load_module(
    "ko/04-dispatcher-and-invocation/step01_dispatcher.py", "ko_ep04"
).run
en_run = load_module(
    "en/04-dispatcher-and-invocation/step01_dispatcher.py", "en_ep04"
).run


def test_ep04_dispatcher_http_and_non_http() -> None:
    """Test ep04 dispatcher http and non http."""
    ko_result = ko_run("http")
    en_result = en_run("queue")
    assert ko_result["status"] == 200
    assert en_result["status"] == 202
