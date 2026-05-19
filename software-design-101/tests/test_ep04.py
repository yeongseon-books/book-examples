from ko.ep04_dependency_direction import GoodOrderService, InMemoryOrderRepository


def test_ep04_dependency_inversion() -> None:
    repo = InMemoryOrderRepository()
    service = GoodOrderService(repo)
    assert service.place("O-1") == "saved:O-1"
    assert repo.saved == ["O-1"]
