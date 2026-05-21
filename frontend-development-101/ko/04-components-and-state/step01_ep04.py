"""Frontend Development 101 - 4편: components and state 예제."""

from __future__ import annotations

from common import ComponentSim


def render_counter(props: dict[str, object], state: dict[str, object]) -> str:
    """Render counter."""
    return f"count={state['count']} step={props['step']}"


def run_demo() -> str:
    """데모를 실행합니다."""
    comp = ComponentSim(props={"step": 1}, state={"count": 0}, renderer=render_counter)
    comp.set_state({"count": int(comp.state["count"]) + int(comp.props["step"])})
    return comp.render()
