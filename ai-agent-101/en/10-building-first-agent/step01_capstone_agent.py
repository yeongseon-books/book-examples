"""Episode 10: capstone agent combining core concepts."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import MockLLM, get_weather, safe_calculate


def run(goal: str) -> dict[str, object]:
    llm = MockLLM()
    state: dict[str, object] = {"weather": None}
    action = llm.next_action(goal, state)
    if isinstance(action, str):
        answer = action
    else:
        state["weather"] = get_weather(action.args["city"])
        answer = str(llm.next_action(goal, state))
    calc = safe_calculate("1000*0.5")
    return {"success": True, "answer": answer, "calc": calc}


if __name__ == "__main__":
    print(run("Check Tokyo weather and tell if umbrella is needed"))
