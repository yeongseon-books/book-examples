from __future__ import annotations

from .conftest import load_module


mod = load_module("ko/09-domain-expertise.py")


def test_domain_mapper_returns_structured_spec() -> None:
    spec = mod.build_domain_spec("fintech")
    assert spec["industry"] == "fintech"
    assert "승인율" in spec["metrics"]
    assert len(spec["regulations"]) >= 2
