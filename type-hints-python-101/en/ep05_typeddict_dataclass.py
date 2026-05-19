"""Type Hints Python 101 - Episode 5: Typeddict dataclass."""

from dataclasses import dataclass
from typing import TypedDict

from typing_extensions import NotRequired, Required


class UserProfile(TypedDict):
    """User profile."""

    name: Required[str]
    age: NotRequired[int]


@dataclass(frozen=True, slots=True)
class Point:
    """Point."""

    x: int
    y: int


def profile_greeting(profile: UserProfile) -> str:
    """Profile greeting."""
    age = profile.get("age")
    return f"{profile['name']}({age})" if age is not None else profile["name"]
