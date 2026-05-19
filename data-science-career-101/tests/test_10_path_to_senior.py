from __future__ import annotations

from .conftest import load_module


mod = load_module("ko/10-path-to-senior.py")


def test_senior_readiness_flags_gaps() -> None:
    result = mod.assess_senior_readiness(
        {
            "technical_depth": 4.2,
            "cross_functional": 2.0,
            "mentorship": 2.1,
            "strategy": 2.4,
            "impact": 3.9,
        }
    )
    assert result["ready"] is False
    assert "cross_functional" in result["gaps"]
