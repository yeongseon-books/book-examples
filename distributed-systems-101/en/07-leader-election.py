"""Distributed Systems 101 - Episode 7: Leader election."""

# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from en.common import elect_leader


def run_demo() -> dict[str, object]:
    # Election needs majority; fencing token must be monotonic.
    """Run demo."""
    ids = ["a", "b", "c", "d", "e"]
    leader = elect_leader(ids, alive={"a", "c", "e"})
    old_token, new_token = 5, 6
    stale_rejected = old_token < new_token
    return {"leader": leader, "stale_rejected": stale_rejected}


if __name__ == "__main__":
    print(run_demo())
