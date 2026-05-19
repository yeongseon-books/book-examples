"""에피소드 05: target-based scaling과 인스턴스 계산을 모사합니다."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import target_based_instances


def run(backlog: int, target_per_instance: int, current_instances: int) -> dict[str, int]:
    desired = target_based_instances(backlog, target_per_instance, current_instances)
    return {"backlog": backlog, "target_per_instance": target_per_instance, "desired_instances": desired}


if __name__ == "__main__":
    print(run(backlog=95, target_per_instance=16, current_instances=2))
