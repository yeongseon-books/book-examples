from __future__ import annotations

from common import ComponentSim


def render_counter(props: dict[str, object], state: dict[str, object]) -> str:
    return f"count={state['count']} step={props['step']}"


def run_demo() -> str:
    comp = ComponentSim(props={"step": 1}, state={"count": 0}, renderer=render_counter)
    comp.set_state({"count": int(comp.state["count"]) + int(comp.props["step"])})
    return comp.render()
