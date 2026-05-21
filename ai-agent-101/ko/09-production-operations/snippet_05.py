"""Generated from book-content article."""

from uuid import uuid4

def estimate_cost(prompt_tokens: int, completion_tokens: int) -> float:
    return prompt_tokens * 0.00003 + completion_tokens * 0.00006

daily_budget = 0.20
spent_today = 0.11
request_id = f"req-{uuid4().hex[:8]}"
prompt_tokens = 1200
completion_tokens = 400
estimated = estimate_cost(prompt_tokens, completion_tokens)

print({
    "request_id": request_id,
    "prompt_tokens": prompt_tokens,
    "completion_tokens": completion_tokens,
    "estimated_usd": round(estimated, 4),
})

if spent_today + estimated > daily_budget:
    print({"request_id": request_id, "status": "blocked", "reason": "budget_exceeded"})
else:
    print({"request_id": request_id, "status": "allowed"})
