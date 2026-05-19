from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from time import perf_counter
from typing import Any


@dataclass
class TaskSpec:
    goal: str
    inputs: dict[str, Any]
    output_keys: list[str]


class MockLLM:
    """Deterministic LLM stub based on input patterns."""

    def complete(self, prompt: str) -> str:
        p = prompt.lower()
        if "forbidden" in p:
            return "blocked"
        if "email" in p:
            return "priority=high"
        if "improve" in p:
            return "improved output"
        if "json" in p:
            return '{"status": "ok"}'
        return "ok"


class TaskHarness:
    def run(
        self, spec: TaskSpec, worker: Callable[[TaskSpec], dict[str, Any]]
    ) -> dict[str, Any]:
        if not spec.goal.strip():
            raise ValueError("goal is required")
        if not spec.output_keys:
            raise ValueError("output_keys are required")
        result = worker(spec)
        missing = [k for k in spec.output_keys if k not in result]
        if missing:
            raise ValueError(f"missing output keys: {missing}")
        return result


class ContextHarness:
    def __init__(self, max_items: int = 5) -> None:
        self.max_items = max_items

    def build(self, items: list[str], query: str = "") -> list[str]:
        dedup = list(dict.fromkeys(items))
        if query:
            q = query.lower()
            dedup.sort(key=lambda x: (q in x.lower(), len(x)), reverse=True)
        if len(dedup) > self.max_items:
            dedup = dedup[: self.max_items]
        return dedup


class ConstraintHarness:
    def __init__(
        self, forbidden_tokens: list[str], max_length: int, require_json: bool = False
    ) -> None:
        self.forbidden_tokens = forbidden_tokens
        self.max_length = max_length
        self.require_json = require_json

    def validate_output(self, text: str) -> None:
        for token in self.forbidden_tokens:
            if token.lower() in text.lower():
                raise ValueError(f"forbidden token detected: {token}")
        if len(text) > self.max_length:
            raise ValueError("output too long")
        if self.require_json:
            try:
                json.loads(text)
            except json.JSONDecodeError as exc:
                raise ValueError("output must be json") from exc


@dataclass
class ToolSpec:
    name: str
    required_args: set[str]
    output_keys: set[str]
    fn: Callable[..., dict[str, Any]]


class ToolHarness:
    def __init__(self, tools: list[ToolSpec]) -> None:
        self.tools = {t.name: t for t in tools}

    def invoke(self, name: str, args: dict[str, Any]) -> dict[str, Any]:
        if name not in self.tools:
            raise ValueError("unknown tool")
        spec = self.tools[name]
        if not spec.required_args.issubset(args.keys()):
            raise ValueError("invalid args")
        result = spec.fn(**args)
        if not spec.output_keys.issubset(result.keys()):
            raise ValueError("invalid tool result schema")
        return result


@dataclass
class EvalCase:
    name: str
    prompt: str
    expected_substring: str


class TestHarness:
    def run(self, llm: MockLLM, cases: list[EvalCase]) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []
        for case in cases:
            out = llm.complete(case.prompt)
            rows.append(
                {
                    "name": case.name,
                    "passed": case.expected_substring in out,
                    "output": out,
                }
            )
        return rows


class FeedbackLoop:
    def __init__(self, max_iterations: int = 3) -> None:
        self.max_iterations = max_iterations

    def run(
        self, initial: str, improve: Callable[[str], str], score: Callable[[str], int]
    ) -> tuple[str, int]:
        current = initial
        current_score = score(current)
        for i in range(self.max_iterations):
            candidate = improve(current)
            candidate_score = score(candidate)
            if candidate_score > current_score:
                current, current_score = candidate, candidate_score
            else:
                return current, i + 1
        return current, self.max_iterations


class ApprovalGate:
    def __init__(self, policy: str = "auto-approve") -> None:
        if policy not in {"auto-approve", "require-approve", "block"}:
            raise ValueError("invalid approval policy")
        self.policy = policy

    def decide(self, approved: bool | None = None) -> str:
        if self.policy == "block":
            return "blocked"
        if self.policy == "auto-approve":
            return "approved"
        if approved:
            return "approved"
        return "blocked"


class Observability:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.metrics: dict[str, float] = {"runs": 0, "total_ms": 0}

    def log_event(self, event: str, payload: dict[str, Any]) -> None:
        row = {"event": event, "payload": payload}
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")

    def time_call(self, fn: Callable[[], dict[str, Any]]) -> dict[str, Any]:
        start = perf_counter()
        result = fn()
        elapsed = (perf_counter() - start) * 1000
        self.metrics["runs"] += 1
        self.metrics["total_ms"] += elapsed
        self.log_event("timing", {"elapsed_ms": round(elapsed, 3)})
        return result


class ProductionHarness:
    def __init__(
        self,
        llm: MockLLM,
        task: TaskHarness,
        context: ContextHarness,
        constraints: ConstraintHarness,
        tools: ToolHarness,
        tests: TestHarness,
        feedback: FeedbackLoop,
        approval: ApprovalGate,
        observability: Observability,
    ) -> None:
        self.llm = llm
        self.task = task
        self.context = context
        self.constraints = constraints
        self.tools = tools
        self.tests = tests
        self.feedback = feedback
        self.approval = approval
        self.observability = observability

    def run(
        self,
        spec: TaskSpec,
        context_items: list[str],
        tool_name: str,
        tool_args: dict[str, Any],
    ) -> dict[str, Any]:
        def worker(_: TaskSpec) -> dict[str, Any]:
            ctx = self.context.build(context_items, query=spec.goal)
            decision = self.approval.decide(approved=True)
            if decision != "approved":
                return {"status": "blocked", "context": ctx}
            tool_result = self.tools.invoke(tool_name, tool_args)
            output = self.llm.complete(spec.goal)
            self.constraints.validate_output(output)
            return {
                "status": "ok",
                "context": ctx,
                "tool": tool_result,
                "output": output,
            }

        result = self.observability.time_call(lambda: self.task.run(spec, worker))
        self.observability.log_event("pipeline_complete", {"status": result["status"]})
        return result
