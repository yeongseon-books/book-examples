# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from en.common import FakeNetwork, SimulatedClock


def run_demo() -> dict[str, object]:
    # Distributed calls always include latency and partial failure.
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
