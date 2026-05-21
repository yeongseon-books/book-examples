"""Generated from book-content article."""

from datetime import datetime, timedelta

class BudgetEnforcer:
    """Budget enforcement."""

    PRICING = {
        "gpt-4": {"prompt": 0.03 / 1000, "completion": 0.06 / 1000},
        "gpt-4o-mini": {"prompt": 0.15 / 1_000_000, "completion": 0.60 / 1_000_000}
    }
