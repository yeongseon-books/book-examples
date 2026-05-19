from unittest.mock import Mock


class EmailClient:
    def send(self, to: str, subject: str, body: str) -> bool:
        raise NotImplementedError


class WelcomeService:
    def __init__(self, email_client: EmailClient):
        self.email_client = email_client

    def send_welcome(self, email: str) -> bool:
        return self.email_client.send(email, "Welcome", "Thanks for joining")


class StubEmailClient(EmailClient):
    def __init__(self, success: bool = True):
        self.success = success

    def send(self, to: str, subject: str, body: str) -> bool:
        return self.success


def make_mock_client(result: bool = True) -> Mock:
    client = Mock(spec=EmailClient)
    client.send.return_value = result
    return client
