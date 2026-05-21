"""Generated from book-content article."""

from datetime import datetime, timedelta


class BudgetEnforcer:
    """Budget enforcement."""

    PRICING = {
        "gpt-4": {"prompt": 0.03 / 1000, "completion": 0.06 / 1000},
        "gpt-4o-mini": {"prompt": 0.15 / 1_000_000, "completion": 0.60 / 1_000_000}
    }

    def __init__(self):
        # Per-user daily usage
        self._usage = defaultdict(lambda: {"date": None, "spent_usd": 0.0})
        self._limits = {}  # user_id -> daily_limit_usd

    def set_limit(self, user_id: str, daily_limit_usd: float):
        self._limits[user_id] = daily_limit_usd

    def check_and_record(
        self,
        user_id: str,
        model: str,
        prompt_tokens: int,
        completion_tokens: int
    ) -> bool:
        """Check budget and record usage. False = block."""
        today = datetime.utcnow().date()
        usage = self._usage[user_id]

        # Reset on date change
        if usage["date"] != today:
            usage["date"] = today
            usage["spent_usd"] = 0.0

        # Estimated cost
        cost = (
            prompt_tokens * self.PRICING[model]["prompt"] +
            completion_tokens * self.PRICING[model]["completion"]
        )

        limit = self._limits.get(user_id, float("inf"))
        if usage["spent_usd"] + cost > limit:
            return False

        usage["spent_usd"] += cost
        return True

# Example usage
budget = BudgetEnforcer()
budget.set_limit("user_123", daily_limit_usd=5.0)

if not budget.check_and_record("user_123", "gpt-4o", 1500, 500):
    raise RuntimeError("daily budget exceeded")
