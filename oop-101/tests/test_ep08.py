from ko.ep08_solid_principles import FakeGateway, OrderService


def test_ep08_dependency_inversion_like() -> None:
    assert OrderService(FakeGateway(True)).place_order(1000) == "paid"
    assert OrderService(FakeGateway(False)).place_order(1000) == "failed"
