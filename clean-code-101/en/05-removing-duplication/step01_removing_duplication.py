def with_tax(price: int, rate: float) -> int:
    return int(price * (1 + rate))


def greet(name: str, lang: str = "ko") -> str:
    messages = {"ko": "안녕하세요", "en": "Hello"}
    return f"{messages[lang]}, {name}"


PLANS = {
    "free": {"price": 0, "limit": 100},
    "pro": {"price": 10, "limit": 1000},
    "team": {"price": 30, "limit": 10_000},
}


def quota(plan: str) -> int:
    return PLANS[plan]["limit"]
