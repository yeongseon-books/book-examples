from dataclasses import dataclass


@dataclass
class EmailSender:
    def send(self, msg: str) -> str:
        return f"email:{msg}"


@dataclass
class SmsSender:
    def send(self, msg: str) -> str:
        return f"sms:{msg}"


def send_without_pattern(kind: str, msg: str) -> str:
    if kind == "email":
        return f"email:{msg}"
    if kind == "sms":
        return f"sms:{msg}"
    raise ValueError(kind)


def send_with_pattern(kind: str, msg: str) -> str:
    strategy = {"email": EmailSender(), "sms": SmsSender()}[kind]
    return strategy.send(msg)
