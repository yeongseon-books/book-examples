"""Generated from book-content article."""

def allow_request(user_id: str, ip: str, api_key: str, input_tokens: int) -> tuple[bool, str]:
    if not token_bucket(f"u:{user_id}:rps", capacity=60, refill_per_sec=1, cost=1):
        return False, "user rps"
    if not token_bucket(f"u:{user_id}:tok", capacity=100_000, refill_per_sec=100_000/60, cost=input_tokens):
        return False, "user tokens"
    if not token_bucket(f"ip:{ip}:rps", capacity=120, refill_per_sec=2, cost=1):
        return False, "ip rps"
    if not token_bucket(f"k:{api_key}:tok", capacity=1_000_000, refill_per_sec=1_000_000/60, cost=input_tokens):
        return False, "key tokens"
    return True, ""
