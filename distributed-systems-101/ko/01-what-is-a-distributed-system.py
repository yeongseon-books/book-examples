"""Distributed Systems 101 - Episode 1: What is a distributed system."""

# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ko.common import FakeNetwork, SimulatedClock


def run_demo() -> dict[str, object]:
    # 분산 환경에서는 지연과 부분 실패가 항상 존재합니다.
    """Run demo."""
    clock = SimulatedClock()
    net = FakeNetwork(clock, seed=1, drop_rate=0.0, min_latency=2, max_latency=2)
    ok = net.send("client", "service", {"op": "ping"})
    clock.tick(1)
    first = len(net.deliver_ready())
    clock.tick(1)
    second = len(net.deliver_ready())
    return {"sent": ok, "delivered_before": first, "delivered_after": second}


if __name__ == "__main__":
    print(run_demo())
