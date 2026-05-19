"""에피소드 02: 워커 설정 카탈로그와 다중 프로세스 구성을 모사합니다."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import resolve_worker_configs


def run() -> dict[str, object]:
    configs = [
        {"language": "python", "defaultExecutablePath": "python", "entry": "worker.py"},
        {"language": "node", "defaultExecutablePath": "node", "entry": "worker.js"},
    ]
    catalog = resolve_worker_configs(configs)
    return {"worker_count": len(catalog), "python_entry": catalog["python"]["entry"]}


if __name__ == "__main__":
    print(run())
