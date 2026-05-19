from ko import _03_cd_and_deployment as ep03


def test_canary_rollout_and_health_invariant() -> None:
    result = ep03.simulate_canary("v2.0.0")
    splits = [p["traffic_percent"] for p in result["timeline"]]
    assert splits == [10, 50, 100]
    assert result["zero_downtime"] is True
