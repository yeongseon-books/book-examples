"""Generated from book-content article."""

@dataclass
class ModerationLog:
    timestamp: datetime
    response_excerpt: str  # first 200 chars only
    flagged_category: str
    score: float
    user_complaint: bool = False  # user reported "I do not see why this was blocked"

def fp_rate(logs: list[ModerationLog], window_days: int = 7) -> float:
    cutoff = datetime.utcnow() - timedelta(days=window_days)
    recent = [l for l in logs if l.timestamp > cutoff]
    if not recent:
        return 0.0
    return sum(1 for l in recent if l.user_complaint) / len(recent)
