"""Tests for ep10 in Information Security 101."""

from common import IncidentDetector


def test_incident_detector_bruteforce_and_travel():
    """Test incident detector bruteforce and travel."""
    det = IncidentDetector()
    events = [{"event": "auth", "ok": False} for _ in range(6)]
    assert det.detect_bruteforce(events)
    travel = [
        {"user": "u", "ts": 0, "km": 0},
        {"user": "u", "ts": 1800, "km": 1000},
    ]
    assert det.detect_impossible_travel(travel)
