"""Design Patterns 101 - Episode 1: What are design patterns."""

from dataclasses import dataclass


@dataclass
class EmailSender:
    """Email sender."""

    def send(self, msg: str) -> str:
        """Send."""
        return f"email:{msg}"


@dataclass
class SmsSender:
    """Sms sender."""

    def send(self, msg: str) -> str:
        """Send."""
        return f"sms:{msg}"


def send_without_pattern(kind: str, msg: str) -> str:
    """Send without pattern."""
    if kind == "email":
        return f"email:{msg}"
    if kind == "sms":
        return f"sms:{msg}"
    raise ValueError(kind)


def send_with_pattern(kind: str, msg: str) -> str:
    """Send with pattern."""
    strategy = {"email": EmailSender(), "sms": SmsSender()}[kind]
    return strategy.send(msg)
