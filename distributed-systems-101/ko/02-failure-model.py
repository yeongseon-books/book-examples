"""Distributed Systems 101 - Episode 2: Failure model."""

# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ko.common import FakeNetwork, SimulatedClock


def run_demo() -> dict[str, bool]:
    # omission(유실)과 partition(단절)을 분리해서 관찰합니다.
    """Run demo."""
    clock = SimulatedClock()
    net = FakeNetwork(clock, seed=2, drop_rate=1.0)
    omitted = not net.send("a", "b", {"m": 1})
    net.drop_rate = 0.0
    net.block("a", "b")
    partitioned = not net.send("a", "b", {"m": 2})
    return {"omission": omitted, "partition": partitioned}


if __name__ == "__main__":
    print(run_demo())
