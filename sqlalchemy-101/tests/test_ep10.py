from ko import ep10_production_patterns


def test_ep10_production_patterns() -> None:
    result = ep10_production_patterns.run()
    assert result["pool"] == "configured"
    assert result["retry"] in {"ok", "recovered"}
    assert result["scoped"] == "1"
    assert "Alembic" in result["migration"]
