"""Generated from book-content article."""

from typing import Any

from pydantic import BaseModel


class TaskSpec(BaseModel):
    """Task Harness: clear inputs and completion criteria."""
    goal: str
    inputs: dict[str, Any]
    completion_criteria: list[str]

class AgentContext(BaseModel):
    """Context Harness: what to show and what to hide."""
    system_prompt: str
    allowed_data_sources: list[str]
    forbidden_topics: list[str]

class ToolPolicy(BaseModel):
    """Constraint + Tool Harness: allowed and forbidden actions."""
    allowed_tools: list[str]
    require_approval: list[str]
    max_iterations: int = 5

def run_agent_with_harness(task: TaskSpec, ctx: AgentContext, policy: ToolPolicy) -> dict[str, Any]:
    """Agent execution with harnesses applied."""
    trace = []  # Observability Harness: record every step

    for iteration in range(policy.max_iterations):
        decision = think_with_context(task, ctx, trace)
        trace.append({"iteration": iteration, "decision": decision})

        if decision["action"] in policy.require_approval:
            if not request_human_approval(decision):
                trace.append({"approval": "denied"})
                break

        result = execute_tool(decision, policy.allowed_tools)
        trace.append({"result": result})

        if check_completion(result, task.completion_criteria):
            return {"status": "success", "trace": trace, "result": result}

    return {"status": "incomplete", "trace": trace}
