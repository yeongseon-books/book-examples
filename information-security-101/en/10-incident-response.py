"""Information Security 101 - Episode 10: Incident response."""

from common import IncidentDetector

detector = IncidentDetector()
events = [
    {"user": "alice", "ts": 0, "km": 0},
    {"user": "alice", "ts": 1800, "km": 900},
]
print({"impossible_travel": detector.detect_impossible_travel(events)})
