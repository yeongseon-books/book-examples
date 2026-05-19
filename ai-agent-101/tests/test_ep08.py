"""Tests for ep08 in Ai Agent 101."""

from conftest import load_module

run = load_module(
    "ko/08-error-handling-reliability/step01_retry_fallback.py", "ep08"
).run


def test_ep08_retry_path() -> None:
    """Test ep08 retry path."""
    result = run()
    assert result["path"] in {"retry", "fallback"}
