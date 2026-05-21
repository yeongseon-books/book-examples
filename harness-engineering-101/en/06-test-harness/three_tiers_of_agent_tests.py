"""Generated from book-content article."""

from dataclasses import dataclass

import pytest


# 1. Unit test — tool schema
def test_create_user_input_validation():
    from pydantic import ValidationError
    with pytest.raises(ValidationError):
        CreateUserInput(email="invalid", name="A", role="admin")

# 2. Integration test — task flow
def test_report_generation_flow(mock_llm):
    """The report generation task uses only read_db."""
    agent = build_agent(tools=["read_db"], llm=mock_llm)
    result = agent.run(task=ReportTaskSpec(date="2026-05-03"))
    assert result.status == "completed"
    assert all(call.tool == "read_db" for call in result.tool_calls)

# 3. Eval test — qualitative quality
def test_summary_quality(eval_dataset):
    agent = build_summary_agent()
    scores = []
    for example in eval_dataset:
        output = agent.run(input=example.input)
        scores.append(rubric_score(output, example.expected))
    assert sum(scores) / len(scores) >= 0.85
