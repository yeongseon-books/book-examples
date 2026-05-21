"""Generated from book-content article."""

from dataclasses import dataclass, field


@dataclass
class AgentState:
    goal: str
    step: int = 0
    max_steps: int = 6
    history: list[dict] = field(default_factory=list)
    stop_reason: str | None = None


def run_agent(goal: str, planner, tools: dict[str, callable]) -> AgentState:
    state = AgentState(goal=goal)

    while state.step < state.max_steps:
        state.step += 1
        action = planner(goal=state.goal, history=state.history)

        if action["type"] == "final":
            state.history.append({"step": state.step, "final": action["answer"]})
            state.stop_reason = "goal_achieved"
            return state

        tool_name = action["tool"]
        if tool_name not in tools:
            state.stop_reason = f"unknown_tool:{tool_name}"
            return state

        result = tools[tool_name](**action.get("args", {}))
        state.history.append({"step": state.step, "action": action, "result": result})

    state.stop_reason = "max_steps_exceeded"
    return state
