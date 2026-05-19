"""Tests for 07 routing and nat in Computer Networks 101."""

import ipaddress

from tests._loader import load_ko


def test_longest_prefix_match() -> None:
    """Test longest prefix match."""
    ep = load_ko("07-routing-and-nat")
    table = ep.RoutingTable(
        [
            ep.Route(ipaddress.ip_network("0.0.0.0/0"), "gw-default"),
            ep.Route(ipaddress.ip_network("10.0.0.0/8"), "gw-10"),
            ep.Route(ipaddress.ip_network("10.1.0.0/16"), "gw-10-1"),
        ]
    )
    assert table.lookup("10.1.2.3").next_hop == "gw-10-1"


def test_nat_translation() -> None:
    """Test nat translation."""
    ep = load_ko("07-routing-and-nat")
    nat = ep.NatTable("203.0.113.9")
    public = nat.translate_outbound("192.168.0.10", 50000)
    assert public[0] == "203.0.113.9"
    assert nat.translate_inbound(public[1]) == ("192.168.0.10", 50000)
