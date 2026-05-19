from common import SeverityClassifier


def run() -> dict[str, str]:
    classifier = SeverityClassifier()
    sev = classifier.classify(users_affected=250000, revenue_loss=5000, regions=2)
    return {"severity": sev, "cadence_min": "15" if sev == "SEV1" else "30"}


if __name__ == "__main__":
    print(run())
