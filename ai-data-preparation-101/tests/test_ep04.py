"""Tests for ep04 in Ai Data Preparation 101."""

from conftest import run_dict


def test_ep04_redaction() -> None:
    """Test ep04 redaction."""
    result = run_dict("ko/04-pii-detection-anonymization/step01_regex_redaction.py")
    assert "@" in str(result["raw"])
    assert "@" not in str(result["redacted"])
