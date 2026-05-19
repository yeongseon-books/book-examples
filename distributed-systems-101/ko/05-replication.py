# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ko.common import ReplicaSet


def run_demo() -> dict[str, object]:
    # async 복제는 lagging replica에서 stale read를 유발할 수 있습니다.
    rs = ReplicaSet(["p", "r1", "r2"])
    rs.write_async("price", 100, lagging={"r2"})
    stale = rs.nodes["r2"].get("price")
    acks = rs.write_quorum("qty", 5, w=2)
    return {"stale_read": stale, "quorum_acks": acks}


if __name__ == "__main__":
    print(run_demo())
