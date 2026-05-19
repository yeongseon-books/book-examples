import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import mock_scale_decision


def scale_http(concurrency: int) -> int:
    return mock_scale_decision(
        signal=concurrency, threshold=50, min_replicas=1, max_replicas=10
    )


def scale_servicebus(messages: int) -> int:
    return mock_scale_decision(
        signal=messages, threshold=5, min_replicas=0, max_replicas=10
    )


def run() -> dict[str, int]:
    return {
        "http_replicas": scale_http(120),
        "worker_replicas": scale_servicebus(26),
    }


if __name__ == "__main__":
    print(run())
