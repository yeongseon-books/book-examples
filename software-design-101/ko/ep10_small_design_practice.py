"""Software Design 101 - Episode 10: Small design practice."""

from ko.ep05_interfaces_abstraction import PaymentGateway


class UrlRepository:
    """Url repository."""

    def __init__(self) -> None:
        self._store: dict[str, str] = {}

    def save(self, code: str, url: str) -> None:
        """Save."""
        self._store[code] = url

    def get(self, code: str) -> str | None:
        """Get."""
        return self._store.get(code)


class UrlShortenerService:
    """Url shortener service."""

    def __init__(self, repo: UrlRepository, gateway: PaymentGateway) -> None:
        self.repo = repo
        self.gateway = gateway

    def _parse(self, raw_url: str) -> str:
        """Parse."""
        if not raw_url.startswith("http"):
            raise ValueError("url must start with http")
        return raw_url

    def _transform(self, url: str) -> str:
        """Transform."""
        return hex(abs(hash(url)) % 4096)[2:].zfill(3)

    def create(self, raw_url: str, amount: int = 0) -> str:
        """Create."""
        url = self._parse(raw_url)
        code = self._transform(url)
        if amount > 0:
            self.gateway.charge(amount)
        self.repo.save(code, url)
        return code

    def resolve(self, code: str) -> str | None:
        """Resolve."""
        return self.repo.get(code)
