# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ko.common import CircuitBreaker


def run_demo() -> dict[str, object]:
    # 반복 실패 시 circuit breaker가 열려 장애 전파를 줄입니다.
    breaker = CircuitBreaker(threshold=2)

    def fail() -> str:
        raise RuntimeError("boom")

    errors = 0
    for _ in range(3):
        try:
            breaker.call(fail)
        except RuntimeError:
            errors += 1
    return {"errors": errors, "open": breaker.open}


if __name__ == "__main__":
    print(run_demo())
