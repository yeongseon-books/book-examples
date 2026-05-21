"""Generated from book-content article."""

from dataclasses import dataclass

@dataclass
class ActionItem:
    text: str
    owner: str
    due: str
    priority: str
    verify: str
    status: str = "open"


def is_complete(item: ActionItem) -> bool:
    return item.status == "done" and bool(item.verify)
