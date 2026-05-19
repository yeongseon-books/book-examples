import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import redact_pii


def run(text: str) -> str:
    return redact_pii(text)


if __name__ == "__main__":
    print(run("연락처 010-1234-5678, 이메일 alice@example.com, SSN 123-45-6789"))
