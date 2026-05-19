import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import KB, verify_grounded_answer


def run(answer: str) -> dict[str, str | bool]:
    decision = verify_grounded_answer(answer, KB)
    return {"allowed": decision.allowed, "reason": decision.reason}


if __name__ == "__main__":
    print(run("Seoul is the capital of Korea [kb:seoul-capital]."))
