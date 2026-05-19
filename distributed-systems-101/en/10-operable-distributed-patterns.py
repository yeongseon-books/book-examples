# pyright: reportMissingImports=false
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from en.common import CircuitBreaker


def run_demo() -> dict[str, object]:
    # Repeated failures open circuit breaker to prevent cascading failures.
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
