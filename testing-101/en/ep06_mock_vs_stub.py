"""Testing 101 - Episode 6: Mock vs stub."""

from unittest.mock import Mock


class EmailClient:
    """Email client."""

    def send(self, to: str, subject: str, body: str) -> bool:
        """Send."""
        raise NotImplementedError


class WelcomeService:
    """Welcome service."""

    def __init__(self, email_client: EmailClient):
        self.email_client = email_client

    def send_welcome(self, email: str) -> bool:
        """Send welcome."""
        return self.email_client.send(email, "Welcome", "Thanks for joining")


class StubEmailClient(EmailClient):
    """Stub email client."""

    def __init__(self, success: bool = True):
        self.success = success

    def send(self, to: str, subject: str, body: str) -> bool:
        """Send."""
        return self.success


def make_mock_client(result: bool = True) -> Mock:
    """Make mock client."""
    client = Mock(spec=EmailClient)
    client.send.return_value = result
    return client
