from dataclasses import dataclass


@dataclass
class Dummy:
    value: str = "unused"


class StubTaxService:
    def tax_rate(self) -> float:
        return 0.1


class SpyNotifier:
    def __init__(self):
        self.calls = []

    def send(self, message: str) -> None:
        self.calls.append(message)


class FakeUserStore:
    def __init__(self):
        self.users = {}

    def save(self, user_id: int, name: str) -> None:
        self.users[user_id] = name


def classify_double(name: str) -> str:
    mapping = {
        "dummy": "placeholder only",
        "stub": "predefined return values",
        "spy": "records interactions",
        "fake": "working simplified implementation",
        "mock": "pre-programmed expectations",
    }
    return mapping[name]
