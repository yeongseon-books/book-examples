from common import IncidentDetector

detector = IncidentDetector()
events = [{"event": "auth", "ok": False} for _ in range(6)]
print({"bruteforce": detector.detect_bruteforce(events)})
