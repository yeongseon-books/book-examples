# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from en.common import MessageQueue


def rpc_add(a: int, b: int) -> int:
    return a + b


def run_demo() -> dict[str, object]:
    # RPC is request-response; queueing is asynchronous.
    rpc_result = rpc_add(3, 4)
    q = MessageQueue()
    q.publish({"task": "ship-order", "order_id": 10})
    polled = q.poll()
    return {"rpc": rpc_result, "message_task": polled["task"] if polled else None}


if __name__ == "__main__":
    print(run_demo())
