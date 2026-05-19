from ko.ep06_mock_vs_stub import StubEmailClient, WelcomeService, make_mock_client


def test_ep06_stub_controls_return_value():
    service = WelcomeService(StubEmailClient(success=False))
    assert service.send_welcome("a@example.com") is False


def test_ep06_mock_verifies_interaction():
    mock_client = make_mock_client(True)
    service = WelcomeService(mock_client)
    assert service.send_welcome("b@example.com") is True
    mock_client.send.assert_called_once()
