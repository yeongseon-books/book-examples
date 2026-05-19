class EmailSender:
    def send(self, message: str) -> str:
        return f"email:{message}"


class SmsSender:
    def send(self, message: str) -> str:
        return f"sms:{message}"


class NotificationService:
    def __init__(self, sender: object) -> None:
        self.sender = sender

    def notify(self, message: str) -> str:
        return self.sender.send(message)  # type: ignore[attr-defined]


if __name__ == "__main__":
    service = NotificationService(EmailSender())
    print(service.notify("deployment complete"))
