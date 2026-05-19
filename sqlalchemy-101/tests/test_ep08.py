from ko import ep08_events_hybrid


def test_ep08_events_hybrid() -> None:
    assert ep08_events_hybrid.run() == "Alice Kim"
