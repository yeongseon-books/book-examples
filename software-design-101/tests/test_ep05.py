from ko.ep05_interfaces_abstraction import MockGateway, checkout


def test_ep05_gateway_abstraction() -> None:
    gateway = MockGateway()
    assert checkout(500, gateway) == "mock:500:ok"
    assert gateway.calls == [500]
