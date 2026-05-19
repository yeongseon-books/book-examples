"""Distributed Systems 101 - Episode 3: Rpc and message passing."""

# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ko.common import MessageQueue


def rpc_add(a: int, b: int) -> int:
    """Rpc add."""
    return a + b


def run_demo() -> dict[str, object]:
    # RPC는 즉시 응답, 큐는 비동기 처리입니다.
    """Run demo."""
    rpc_result = rpc_add(3, 4)
    q = MessageQueue()
    q.publish({"task": "ship-order", "order_id": 10})
    polled = q.poll()
    return {"rpc": rpc_result, "message_task": polled["task"] if polled else None}


if __name__ == "__main__":
    print(run_demo())
