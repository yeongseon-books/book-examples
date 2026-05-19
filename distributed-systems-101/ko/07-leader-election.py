"""Distributed Systems 101 - Episode 7: Leader election."""

# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ko.common import elect_leader


def run_demo() -> dict[str, object]:
    # 과반 생존 시 리더가 선출되고 fencing token은 단조 증가해야 합니다.
    """Run demo."""
    ids = ["a", "b", "c", "d", "e"]
    leader = elect_leader(ids, alive={"a", "c", "e"})
    old_token, new_token = 5, 6
    stale_rejected = old_token < new_token
    return {"leader": leader, "stale_rejected": stale_rejected}


if __name__ == "__main__":
    print(run_demo())
