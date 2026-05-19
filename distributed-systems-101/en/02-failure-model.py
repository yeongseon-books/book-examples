# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from en.common import FakeNetwork, SimulatedClock


def run_demo() -> dict[str, bool]:
    # Observe omission failure separately from network partition.
    clock = SimulatedClock()
    net = FakeNetwork(clock, seed=2, drop_rate=1.0)
    omitted = not net.send("a", "b", {"m": 1})
    net.drop_rate = 0.0
    net.block("a", "b")
    partitioned = not net.send("a", "b", {"m": 2})
    return {"omission": omitted, "partition": partitioned}


if __name__ == "__main__":
    print(run_demo())
