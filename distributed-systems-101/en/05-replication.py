# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from en.common import ReplicaSet


def run_demo() -> dict[str, object]:
    # Async replication can leave stale reads on lagging replicas.
    rs = ReplicaSet(["p", "r1", "r2"])
    rs.write_async("price", 100, lagging={"r2"})
    stale = rs.nodes["r2"].get("price")
    acks = rs.write_quorum("qty", 5, w=2)
    return {"stale_read": stale, "quorum_acks": acks}


if __name__ == "__main__":
    print(run_demo())
