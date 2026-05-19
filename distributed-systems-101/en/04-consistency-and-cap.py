"""Distributed Systems 101 - Episode 4: Consistency and cap."""

# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from en.common import ReplicaSet


def cp_write(replica: ReplicaSet, partitioned: bool, key: str, value: int) -> bool:
    # In CP mode, reject writes without majority.
    # Partition is simplified as losing exactly two nodes when partitioned=True.
    """Cp write."""
    total = len(replica.nodes)
    available = total - (2 if partitioned else 0)
    if available <= total // 2:
        return False
    replica.write_sync(key, value)
    return True


def run_demo() -> dict[str, bool]:
    """Run demo."""
    rs = ReplicaSet(["n1", "n2", "n3"])
    ok = cp_write(rs, partitioned=False, key="x", value=1)
    fail = cp_write(rs, partitioned=True, key="x", value=2)
    return {"normal_write": ok, "partition_write": fail}


if __name__ == "__main__":
    print(run_demo())
