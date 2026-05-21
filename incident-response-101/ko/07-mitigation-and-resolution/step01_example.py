"""Incident Response 101 - 7편: mitigation and resolution 예제."""

from common import MitigationTracker


def run() -> list[str]:
    """Run."""
    tracker = MitigationTracker()
    states = [tracker.state, tracker.advance(), tracker.advance()]
    return states


if __name__ == "__main__":
    print(run())
