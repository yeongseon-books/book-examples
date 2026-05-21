"""Generated from book-content article."""

from pydantic import BaseModel, ValidationError

class ReportResult(BaseModel):
    title: str
    summary: str
    next_actions: list[str]

def verify_report_result(payload: dict) -> tuple[bool, str]:
    try:
        result = ReportResult.model_validate(payload)
    except ValidationError as exc:
        return False, f"schema validation failed: {exc.errors()}"

    if len(result.next_actions) < 2:
        return False, "need at least two follow-up actions"

    return True, "pass"
