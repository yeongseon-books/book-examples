from common import MitigationTracker


def run() -> list[str]:
    tracker = MitigationTracker()
    states = [tracker.state, tracker.advance(), tracker.advance()]
    return states


if __name__ == "__main__":
    print(run())
