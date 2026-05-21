"""Generated from book-content article."""

import time
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser

import requests


class PoliteScraper:
    def __init__(self, base_url: str, user_agent: str, rps: float = 1.0):
        self.base_url = base_url
        self.user_agent = user_agent
        self.min_interval = 1.0 / rps
        self._last = 0.0
        self.rp = RobotFileParser()
        self.rp.set_url(urljoin(base_url, "/robots.txt"))
        try:
            self.rp.read()
        except Exception:
            pass  # Treat missing robots.txt conservatively

    def can_fetch(self, path: str) -> bool:
        return self.rp.can_fetch(self.user_agent, urljoin(self.base_url, path))

    def get(self, path: str) -> requests.Response:
        if not self.can_fetch(path):
            raise PermissionError(f"robots.txt disallows {path}")
        elapsed = time.time() - self._last
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self._last = time.time()
        return requests.get(
            urljoin(self.base_url, path),
            headers={"User-Agent": self.user_agent},
            timeout=10,
        )
