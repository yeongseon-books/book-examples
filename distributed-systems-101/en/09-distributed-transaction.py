# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from en.common import Participant, two_phase_commit


def run_demo() -> dict[str, object]:
    # In 2PC, one prepare failure forces full rollback.
    p1 = Participant("inventory", can_commit=True)
    p2 = Participant("payment", can_commit=False)
    ok = two_phase_commit([p1, p2])
    return {"committed": ok, "states": [p1.state, p2.state]}


if __name__ == "__main__":
    print(run_demo())
