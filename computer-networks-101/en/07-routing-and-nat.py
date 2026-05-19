# English mirror of the corresponding episode demo
import ipaddress
from dataclasses import dataclass


@dataclass(frozen=True)
class Route:
    prefix: ipaddress.IPv4Network
    next_hop: str


class RoutingTable:
    def __init__(self, routes: list[Route]):
        self.routes = routes

    def lookup(self, destination: str) -> Route:
        ip = ipaddress.ip_address(destination)
        matched = [route for route in self.routes if ip in route.prefix]
        if not matched:
            raise KeyError(destination)
        return max(matched, key=lambda route: route.prefix.prefixlen)


class NatTable:
    def __init__(self, public_ip: str):
        self.public_ip = public_ip
        self._map: dict[tuple[str, int], tuple[str, int]] = {}
        self._next_port = 40000

    def translate_outbound(self, private_ip: str, private_port: int) -> tuple[str, int]:
        key = (private_ip, private_port)
        if key not in self._map:
            self._map[key] = (self.public_ip, self._next_port)
            self._next_port += 1
        return self._map[key]

    def translate_inbound(self, public_port: int) -> tuple[str, int]:
        for private, public in self._map.items():
            if public[1] == public_port:
                return private
        raise KeyError(public_port)


if __name__ == "__main__":
    table = RoutingTable(
        [
            Route(ipaddress.ip_network("0.0.0.0/0"), "192.168.0.1"),
            Route(ipaddress.ip_network("10.0.0.0/8"), "10.0.0.1"),
        ]
    )
    print(table.lookup("10.20.30.40"))
