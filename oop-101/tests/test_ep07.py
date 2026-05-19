from ko.ep07_composition_vs_inheritance import (
    EmailSender,
    NotificationService,
    SmsSender,
)


def test_ep07_composition_switch_sender() -> None:
    assert NotificationService(EmailSender()).notify("ok") == "email:ok"
    assert NotificationService(SmsSender()).notify("ok") == "sms:ok"
