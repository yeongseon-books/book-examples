"""Tests for ep06 in Azure Functions Deep Dive."""

from conftest import load_module

ko_run = load_module(
    "ko/06-cold-start-placeholder/step01_placeholder.py", "ko_ep06"
).run
en_run = load_module(
    "en/06-cold-start-placeholder/step01_placeholder.py", "en_ep06"
).run


def test_ep06_placeholder_specialization_paths() -> None:
    """Test ep06 placeholder specialization paths."""
    ko_result = ko_run(container_ready=True, first_request=True)
    en_result = en_run(container_ready=False, first_request=False)
    assert ko_result["specialized"] is True
    assert ko_result["path"] == "request"
    assert en_result["specialized"] is False
    assert en_result["path"] == "standby"
