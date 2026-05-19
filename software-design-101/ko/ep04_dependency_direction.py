"""Software Design 101 - Episode 4: Dependency direction."""


class SqlOrderRepository:
    """Sql order repository."""

    def save(self, order_id: str) -> str:
        """Save."""
        return f"saved:{order_id}"


class BadOrderService:
    """Bad order service."""

    def place(self, order_id: str) -> str:
        """Place."""
        repo = SqlOrderRepository()
        return repo.save(order_id)


class OrderRepositoryPort:
    """Order repository port."""

    def save(self, order_id: str) -> str:
        """Save."""
        raise NotImplementedError


class GoodOrderService:
    """Good order service."""

    def __init__(self, repo: OrderRepositoryPort) -> None:
        self.repo = repo

    def place(self, order_id: str) -> str:
        """Place."""
        return self.repo.save(order_id)


class InMemoryOrderRepository(OrderRepositoryPort):
    """In memory order repository."""

    def __init__(self) -> None:
        self.saved: list[str] = []

    def save(self, order_id: str) -> str:
        """Save."""
        self.saved.append(order_id)
        return f"saved:{order_id}"
