"""Tests for 08 logging and analysis in Devops 101."""

from ko import _08_logging_and_analysis as ep08


def test_p95_latency_and_top_errors() -> None:
    """Test p95 latency and top errors."""
    logs = [
        {"level": "INFO", "latency_ms": 10, "error_code": ""},
        {"level": "ERROR", "latency_ms": 50, "error_code": "E_DB"},
        {"level": "ERROR", "latency_ms": 30, "error_code": "E_DB"},
        {"level": "ERROR", "latency_ms": 90, "error_code": "E_TIMEOUT"},
        {"level": "INFO", "latency_ms": 70, "error_code": ""},
    ]
    assert ep08.latency_percentile(logs, 95) == 90.0
    top = ep08.top_error_patterns(logs, n=2)
    assert top[0] == ("E_DB", 2)
