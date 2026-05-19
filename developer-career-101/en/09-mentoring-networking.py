from dataclasses import dataclass


@dataclass
class Contact:
    name: str
    priority: int
    days_since_touch: int


def recommend_follow_up(contacts: list[Contact]) -> Contact:
    return max(contacts, key=lambda c: (c.days_since_touch, c.priority))


def meeting_agenda(topic: str) -> list[str]:
    return ["context", f"topic: {topic}", "questions", "next actions"]
