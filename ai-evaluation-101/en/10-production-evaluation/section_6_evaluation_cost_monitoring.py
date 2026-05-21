"""Generated from book-content article."""

@dataclass
class JudgeUsage:
    date: str
    judge_calls: int
    judge_cost_usd: float
    serving_cost_usd: float

def cost_ratio_alert(usage: JudgeUsage, max_ratio: float = 0.1):
    ratio = usage.judge_cost_usd / usage.serving_cost_usd
    if ratio > max_ratio:
        alert(f"Judge cost is {ratio:.1%} of serving cost — exceeds {max_ratio:.0%} budget")
