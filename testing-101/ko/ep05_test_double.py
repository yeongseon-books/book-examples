"""Testing 101 - Episode 5: Test double."""

from dataclasses import dataclass


@dataclass
class Dummy:
    """Dummy."""

    value: str = "unused"


class StubTaxService:
    """Stub tax service."""

    def tax_rate(self) -> float:
        """Tax rate."""
        return 0.1


class SpyNotifier:
    """Spy notifier."""

    def __init__(self):
        self.calls = []

    def send(self, message: str) -> None:
        """Send."""
        self.calls.append(message)


class FakeUserStore:
    """Fake user store."""

    def __init__(self):
        self.users = {}

    def save(self, user_id: int, name: str) -> None:
        """Save."""
        self.users[user_id] = name


def classify_double(name: str) -> str:
    """Classify double."""
    mapping = {
        "dummy": "placeholder only",
        "stub": "predefined return values",
        "spy": "records interactions",
        "fake": "working simplified implementation",
        "mock": "pre-programmed expectations",
    }
    return mapping[name]
