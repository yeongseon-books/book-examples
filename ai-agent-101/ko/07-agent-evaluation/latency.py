"""Generated from book-content article."""

@dataclass
class CostMetrics:
    """Cost metrics."""
    total_tokens: int
    prompt_tokens: int
    completion_tokens: int
    api_calls: int
    estimated_usd: float

class CostTracker:
    """Tracks API call cost."""

    PRICING = {
        "gpt-4": {"prompt": 0.03 / 1000, "completion": 0.06 / 1000},
        "gpt-4o-mini": {"prompt": 0.15 / 1_000_000, "completion": 0.60 / 1_000_000}
    }

    def __init__(self):
        self.metrics = CostMetrics(0, 0, 0, 0, 0.0)

    def record(self, model: str, prompt_tokens: int, completion_tokens: int):
        """Record an API call."""
        self.metrics.api_calls += 1
        self.metrics.prompt_tokens += prompt_tokens
        self.metrics.completion_tokens += completion_tokens
        self.metrics.total_tokens += prompt_tokens + completion_tokens

        if model in self.PRICING:
            cost = (
                prompt_tokens * self.PRICING[model]["prompt"] +
                completion_tokens * self.PRICING[model]["completion"]
            )
            self.metrics.estimated_usd += cost

    def report(self) -> dict:
        return {
            "api_calls": self.metrics.api_calls,
            "total_tokens": self.metrics.total_tokens,
            "estimated_usd": round(self.metrics.estimated_usd, 4)
        }
