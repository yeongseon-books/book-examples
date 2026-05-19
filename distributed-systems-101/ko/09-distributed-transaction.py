"""Distributed Systems 101 - Episode 9: Distributed transaction."""

# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ko.common import Participant, two_phase_commit


def run_demo() -> dict[str, object]:
    # 2PC는 prepare 단계에서 하나라도 실패하면 전체 rollback합니다.
    """Run demo."""
    p1 = Participant("inventory", can_commit=True)
    p2 = Participant("payment", can_commit=False)
    ok = two_phase_commit([p1, p2])
    return {"committed": ok, "states": [p1.state, p2.state]}


if __name__ == "__main__":
    print(run_demo())
