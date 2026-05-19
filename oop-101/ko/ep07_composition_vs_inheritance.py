from typing import Protocol


class Sender(Protocol):
    def send(self, message: str) -> str: ...


class EmailSender:
    def send(self, message: str) -> str:
        return f"email:{message}"


class SmsSender:
    def send(self, message: str) -> str:
        return f"sms:{message}"


class NotificationService:
    sender: Sender

    def __init__(self, sender: Sender) -> None:
        self.sender = sender

    def notify(self, message: str) -> str:
        return self.sender.send(message)


if __name__ == "__main__":
    service = NotificationService(EmailSender())
    print(service.notify("배포 완료"))
