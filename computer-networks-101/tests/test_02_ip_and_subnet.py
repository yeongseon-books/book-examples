import ipaddress
from tests._loader import load_ko


def test_ipaddress_basics() -> None:
    assert ipaddress.ip_network("192.168.1.0/24").num_addresses == 256


def test_summary() -> None:
    ep = load_ko("02-ip-and-subnet")
    data = ep.summarize_network("192.168.1.0/24")
    assert data["contains_192_168_1_42"] is True
    assert data["first_subnet"] == "192.168.1.0/26"
