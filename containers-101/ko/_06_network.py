from __future__ import annotations

import ipaddress


class BridgeNetwork:
    def __init__(self, name: str, cidr: str) -> None:
        self.name = name
        self.pool = ipaddress.ip_network(cidr)
        self._hosts = iter(self.pool.hosts())
        self.endpoints: dict[str, str] = {}

    def connect(self, container_name: str) -> str:
        if container_name in self.endpoints:
            return self.endpoints[container_name]
        ip = str(next(self._hosts))
        self.endpoints[container_name] = ip
        return ip

    def can_ping(self, source: str, target: str) -> bool:
        return source in self.endpoints and target in self.endpoints
