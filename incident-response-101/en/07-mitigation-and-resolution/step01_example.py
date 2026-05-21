"""Incident Response 101 - Episode 7: mitigation and resolution example."""

from common import MitigationTracker


def run() -> list[str]:
    """Run."""
    tracker = MitigationTracker()
    states = [tracker.state, tracker.advance(), tracker.advance()]
    return states


if __name__ == "__main__":
    print(run())
