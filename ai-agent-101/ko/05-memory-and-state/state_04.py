"""Generated from book-content article."""

import json
from pathlib import Path

STATE_PATH = Path("state.json")

def save_state(step: str, completed: list[str]) -> None:
    STATE_PATH.write_text(
        json.dumps({"current_step": step, "completed": completed}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"current_step": "collect", "completed": []}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))

state = load_state()
print("before:", state)

if state["current_step"] == "collect":
    state["completed"].append("collect")
    state["current_step"] = "summarize"
    save_state(state["current_step"], state["completed"])

reloaded = load_state()
print("after:", reloaded)
