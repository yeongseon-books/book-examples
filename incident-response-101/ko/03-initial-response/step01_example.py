"""Incident Response 101 - Episode 1: Example."""

from common import OnCallRouter


def run() -> dict[str, object]:
    """Run."""
    router = OnCallRouter()
    responders = router.route("SEV1", "payments")
    return {"severity": "SEV1", "service": "payments", "responders": responders}


if __name__ == "__main__":
    print(run())
