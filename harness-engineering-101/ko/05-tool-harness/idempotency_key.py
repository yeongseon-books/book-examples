"""Generated from book-content article."""

import hashlib
from dataclasses import dataclass

@dataclass
class IdempotencyStore:
    """Stores results per idempotency key."""
    _cache: dict[str, dict] = None

    def __post_init__(self):
        self._cache = self._cache or {}

    def get_or_run(self, key: str, fn, *args, **kwargs) -> dict:
        if key in self._cache:
            return self._cache[key]
        result = fn(*args, **kwargs)
        self._cache[key] = result
        return result

def create_charge(amount: int, currency: str, idempotency_key: str, store: IdempotencyStore) -> dict:
    """Create a charge. Same idempotency_key runs only once."""
    def _do_charge():
        return {
            "charge_id": "ch_" + hashlib.sha256(idempotency_key.encode()).hexdigest()[:12],
            "amount": amount,
        }
    return store.get_or_run(idempotency_key, _do_charge)

# The agent uses a key unique per task
store = IdempotencyStore()
key = "task-abc123-charge-001"
r1 = create_charge(1000, "USD", key, store)
r2 = create_charge(1000, "USD", key, store)
assert r1 == r2  # Same result, executed once
