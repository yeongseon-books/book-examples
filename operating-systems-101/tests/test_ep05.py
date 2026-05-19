from common import ep05_producer_consumer


def test_ep05_producer_consumer_balanced():
    out = ep05_producer_consumer(count=8, capacity=2)
    assert out["produced"] == list(range(8))
    assert sorted(out["consumed"]) == list(range(8))
