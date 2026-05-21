"""Harness Engineering 101 - Episode 9: observability example."""

from __future__ import annotations

from pathlib import Path

from common import (
    ApprovalGate,
    ConstraintHarness,
    ContextHarness,
    EvalCase,
    FeedbackLoop,
    MockLLM,
    Observability,
    ProductionHarness,
    TaskHarness,
    TaskSpec,
    TestHarness,
    ToolHarness,
    ToolSpec,
)


def _tools() -> ToolHarness:
    """Tools."""
    return ToolHarness(
        [
            ToolSpec(
                name="lookup",
                required_args={"key"},
                output_keys={"value"},
                fn=lambda key: {"value": f"resolved:{key}"},
            )
        ]
    )


def what_is_harness_engineering_example() -> dict:
    """What is harness engineering example."""
    llm = MockLLM()
    return {"answer": llm.complete("what is harness engineering")}


def task_harness_example() -> dict:
    """Task harness example."""
    th = TaskHarness()
    spec = TaskSpec(goal="make report", inputs={"source": "db"}, output_keys=["status"])
    return th.run(spec, lambda _: {"status": "done"})


def context_harness_example() -> list[str]:
    """Context harness example."""
    ch = ContextHarness(max_items=3)
    return ch.build(["a", "b", "b", "goal-info", "older"], query="goal")


def constraint_harness_example() -> str:
    """Constraint harness example."""
    c = ConstraintHarness(forbidden_tokens=["SECRET"], max_length=32)
    txt = "safe output"
    c.validate_output(txt)
    return txt


def tool_harness_example() -> dict:
    """Tool harness example."""
    return _tools().invoke("lookup", {"key": "customer-1"})


def test_harness_example() -> list[dict]:
    """Test harness example."""
    h = TestHarness()
    rows = h.run(MockLLM(), [EvalCase("json-case", "return json", "status")])
    return rows


def feedback_loop_example() -> tuple[str, int]:
    """Feedback loop example."""
    loop = FeedbackLoop(max_iterations=3)
    return loop.run(
        "draft", lambda _: "improved output", lambda x: 1 if "improved" in x else 0
    )


def approval_gate_example() -> str:
    """Approval gate example."""
    return ApprovalGate("require-approve").decide(approved=True)


def observability_example(log_path: Path) -> dict:
    """Observability example."""
    obs = Observability(log_path)
    return obs.time_call(lambda: {"status": "ok"})


def production_harness_example(log_path: Path) -> dict:
    """Production harness example."""
    ph = ProductionHarness(
        llm=MockLLM(),
        task=TaskHarness(),
        context=ContextHarness(max_items=3),
        constraints=ConstraintHarness(forbidden_tokens=["BAD"], max_length=64),
        tools=_tools(),
        tests=TestHarness(),
        feedback=FeedbackLoop(max_iterations=2),
        approval=ApprovalGate("auto-approve"),
        observability=Observability(log_path),
    )
    spec = TaskSpec(
        goal="email summary",
        inputs={"ticket": 1},
        output_keys=["status", "context", "tool", "output"],
    )
    return ph.run(
        spec,
        ["email policy", "ticket context", "email policy"],
        "lookup",
        {"key": "ticket-1"},
    )
