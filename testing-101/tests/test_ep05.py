from ko.ep05_test_double import FakeUserStore, SpyNotifier, classify_double


def test_ep05_classification_map():
    assert classify_double("stub") == "predefined return values"


def test_ep05_spy_records_calls_and_fake_stores_data():
    spy = SpyNotifier()
    spy.send("hello")
    assert spy.calls == ["hello"]
    fake = FakeUserStore()
    fake.save(1, "Kim")
    assert fake.users[1] == "Kim"
