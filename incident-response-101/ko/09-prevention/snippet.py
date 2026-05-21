"""Generated from book-content article."""

from datetime import datetime


def minutes(a: str, b: str) -> float:
    t1 = datetime.fromisoformat(a)
    t2 = datetime.fromisoformat(b)
    return (t2 - t1).total_seconds() / 60.0


def metrics(incident: dict) -> dict:
    detected = incident["detected"]
    acked = incident["acknowledged"]
    mitigated = incident["mitigated"]
    resolved = incident["resolved"]
    return {
        "mtta": minutes(detected, acked),
        "mttm": minutes(detected, mitigated),
        "mttr": minutes(detected, resolved),
    }
