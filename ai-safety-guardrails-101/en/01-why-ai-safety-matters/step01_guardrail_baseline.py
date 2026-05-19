import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))


def run(user_input: str) -> dict[str, str | bool]:
    if len(user_input) > 500:
        return {"allowed": False, "reason": "too_long"}
    return {"allowed": True, "reason": "baseline_pass"}


if __name__ == "__main__":
    print(run("This is a safe query."))
