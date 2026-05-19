"""Oop 101 - Episode 7: Composition vs inheritance."""


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

    def __init__(self, sender: object) -> None:
        self.sender = sender

    def notify(self, message: str) -> str:
        """Notify."""
        return self.sender.send(message)  # type: ignore[attr-defined]


if __name__ == "__main__":
    service = NotificationService(EmailSender())
    print(service.notify("deployment complete"))
