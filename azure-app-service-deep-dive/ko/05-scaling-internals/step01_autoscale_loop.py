from __future__ import annotations

from common import autoscale_decision


def evaluate(cpu: float, http_queue: float) -> str:
    # App Service autoscale의 OR(out)/AND(in) 성질을 단순화해 표현합니다.
    return autoscale_decision({"cpu": cpu, "http_queue": http_queue})


if __name__ == "__main__":
    print(evaluate(81.0, 2.0))
