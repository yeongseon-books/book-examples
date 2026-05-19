"""Episode 01: Observe-Think-Act-Check 수동 루프 예제입니다."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import MockLLM, get_weather


def run(goal: str) -> dict[str, object]:
    """Run."""
    llm = MockLLM()
    history: list[dict[str, object]] = []
    state: dict[str, object] = {"goal": goal, "weather": None, "history": history}
    for _ in range(4):
        action = llm.next_action(goal, state)
        if isinstance(action, str):
            return {"success": True, "answer": action, "state": state}
        if action.name == "get_weather":
            result = get_weather(action.args["city"])
            state["weather"] = result
            history.append({"action": action.name, "result": result})
    return {"success": False, "answer": "loop limit", "state": state}


if __name__ == "__main__":
    print(run("도쿄 날씨를 확인하고 우산 필요 여부를 알려줘"))
