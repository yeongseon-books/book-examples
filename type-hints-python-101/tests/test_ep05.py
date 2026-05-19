from dataclasses import FrozenInstanceError

from ko.ep05_typeddict_dataclass import Point, profile_greeting


def test_ep05_typeddict_and_frozen_dataclass() -> None:
    assert profile_greeting({'name': 'kim'}) == 'kim'
    p = Point(1, 2)
    try:
        p.x = 3  # type: ignore[misc]
        assert False, 'FrozenInstanceError expected'
    except FrozenInstanceError:
        assert True
