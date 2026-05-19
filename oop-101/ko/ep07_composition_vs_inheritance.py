"""Oop 101 - Episode 7: Composition vs inheritance."""

from typing import Protocol


class Sender(Protocol):
    """Sender."""

    def send(self, message: str) -> str: ...


class EmailSender:
    """Email sender."""

    def send(self, message: str) -> str:
        """Send."""
        return f"email:{message}"


class SmsSender:
    """Sms sender."""

    def send(self, message: str) -> str:
        """Send."""
        return f"sms:{message}"


class NotificationService:
    """Notification service."""

    sender: Sender

    def __init__(self, sender: Sender) -> None:
        self.sender = sender

    def notify(self, message: str) -> str:
        """Notify."""
        return self.sender.send(message)


if __name__ == "__main__":
    service = NotificationService(EmailSender())
    print(service.notify("배포 완료"))
