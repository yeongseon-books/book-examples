# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ko.common import EventStore, MessageQueue


def run_demo() -> dict[str, object]:
    # 큐는 전달, 이벤트 스토어는 상태 재구성을 담당합니다.
    q = MessageQueue()
    q.publish({"event_id": "e1", "type": "order-created"})
    msg = q.poll()
    store = EventStore()
    store.append({"account_id": "u1", "type": "credit", "amount": 100})
    store.append({"account_id": "u1", "type": "debit", "amount": 30})
    balance = store.replay_balance("u1")
    return {"message_type": msg["type"] if msg else None, "balance": balance}


if __name__ == "__main__":
    print(run_demo())
