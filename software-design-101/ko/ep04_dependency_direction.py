class SqlOrderRepository:
    def save(self, order_id: str) -> str:
        return f"saved:{order_id}"


class BadOrderService:
    def place(self, order_id: str) -> str:
        repo = SqlOrderRepository()
        return repo.save(order_id)


class OrderRepositoryPort:
    def save(self, order_id: str) -> str:
        raise NotImplementedError


class GoodOrderService:
    def __init__(self, repo: OrderRepositoryPort) -> None:
        self.repo = repo

    def place(self, order_id: str) -> str:
        return self.repo.save(order_id)


class InMemoryOrderRepository(OrderRepositoryPort):
    def __init__(self) -> None:
        self.saved: list[str] = []

    def save(self, order_id: str) -> str:
        self.saved.append(order_id)
        return f"saved:{order_id}"
