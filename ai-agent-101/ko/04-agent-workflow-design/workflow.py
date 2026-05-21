"""Generated from book-content article."""

from dataclasses import dataclass
from typing import Any

@dataclass
class StepResult:
    name: str
    ok: bool
    output: Any
    retryable: bool = False

def fetch_customer(customer_id: str) -> StepResult:
    fake_db = {"C-001": {"name": "Minji", "tier": "pro"}}
    customer = fake_db.get(customer_id)
    if not customer:
        return StepResult("fetch_customer", False, "customer not found")
    return StepResult("fetch_customer", True, customer)

def draft_reply(customer: dict) -> StepResult:
    text = f"{customer['name']} 고객은 {customer['tier']} 요금제를 사용 중입니다."
    return StepResult("draft_reply", True, text)

def run_workflow(customer_id: str) -> list[StepResult]:
    results: list[StepResult] = []

    customer_result = fetch_customer(customer_id)
    results.append(customer_result)
    if not customer_result.ok:
        return results

    reply_result = draft_reply(customer_result.output)
    results.append(reply_result)
    return results

for step in run_workflow("C-001"):
    print(step)
