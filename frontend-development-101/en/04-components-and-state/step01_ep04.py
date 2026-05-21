"""Frontend Development 101 - Episode 4: components and state example."""

from __future__ import annotations

from common import ComponentSim


def render_counter(props: dict[str, object], state: dict[str, object]) -> str:
    """Render counter."""
    return f"count={state['count']} step={props['step']}"


def run_demo() -> str:
    """Run demo."""
    comp = ComponentSim(props={"step": 1}, state={"count": 0}, renderer=render_counter)
    comp.set_state({"count": int(comp.state["count"]) + int(comp.props["step"])})
    return comp.render()
