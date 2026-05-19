"""Tests for ep06 in Testing 101."""

from ko.ep06_mock_vs_stub import StubEmailClient, WelcomeService, make_mock_client


def test_ep06_stub_controls_return_value():
    """Test ep06 stub controls return value."""
    service = WelcomeService(StubEmailClient(success=False))
    assert service.send_welcome("a@example.com") is False


def test_ep06_mock_verifies_interaction():
    """Test ep06 mock verifies interaction."""
    mock_client = make_mock_client(True)
    service = WelcomeService(mock_client)
    assert service.send_welcome("b@example.com") is True
    mock_client.send.assert_called_once()
