from common import Incident, SeverityClassifier

def run() -> dict[str, str]:
    classifier = SeverityClassifier()
    sev = classifier.classify(users_affected=15000, revenue_loss=3000, regions=1)
    incident = Incident(id="INC-001", title="checkout timeout", severity=sev)
    kind = "incident" if sev in {"SEV1", "SEV2", "SEV3"} else "bug"
    return {"incident_id": incident.id, "severity": sev, "classification": kind}

if __name__ == "__main__":
    print(run())
