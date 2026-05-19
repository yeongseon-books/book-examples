"""Tests for 08 load balancer in Computer Networks 101."""

from tests._loader import load_ko


def test_round_robin_even_distribution() -> None:
    """Test round robin even distribution."""
    ep = load_ko("08-load-balancer")
    rr = ep.RoundRobinBalancer([ep.Backend("a"), ep.Backend("b"), ep.Backend("c")])
    picks = [rr.pick().name for _ in range(6)]
    assert picks.count("a") == 2
    assert picks.count("b") == 2
    assert picks.count("c") == 2


def test_weighted_and_least_connections() -> None:
    """Test weighted and least connections."""
    ep = load_ko("08-load-balancer")
    weighted = ep.WeightedRoundRobinBalancer([ep.Backend("a", 1), ep.Backend("b", 2)])
    picks = [weighted.pick().name for _ in range(6)]
    assert picks.count("b") == 4
    least = ep.LeastConnectionsBalancer(
        [ep.Backend("x", active_connections=3), ep.Backend("y", active_connections=1)]
    )
    assert least.pick().name == "y"
