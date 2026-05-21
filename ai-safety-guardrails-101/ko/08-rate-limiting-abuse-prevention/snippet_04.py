"""Generated from book-content article."""

PRICING = {
    "gpt-4o": {"in": 2.50/1_000_000, "out": 10.00/1_000_000},
    "gpt-4o-mini": {"in": 0.15/1_000_000, "out": 0.60/1_000_000},
}

def charge(user_id: str, model: str, in_tok: int, out_tok: int) -> bool:
    p = PRICING[model]
    cost_cents = int((in_tok * p["in"] + out_tok * p["out"]) * 100_000)  # 0.001 cent units
    return token_bucket(f"u:{user_id}:cost", capacity=10_000_000, refill_per_sec=10_000_000/86400, cost=cost_cents)
