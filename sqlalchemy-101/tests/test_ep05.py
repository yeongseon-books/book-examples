from ko import ep05_session_uow


def test_ep05_session_uow() -> None:
    first_id, ok = ep05_session_uow.run()
    assert first_id > 0
    assert ok is True
