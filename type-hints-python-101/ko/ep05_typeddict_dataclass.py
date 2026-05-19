from dataclasses import dataclass
from typing import TypedDict

from typing_extensions import NotRequired, Required


class UserProfile(TypedDict):
    name: Required[str]
    age: NotRequired[int]


@dataclass(frozen=True, slots=True)
class Point:
    x: int
    y: int


def profile_greeting(profile: UserProfile) -> str:
    age = profile.get("age")
    return f"{profile['name']}({age})" if age is not None else profile["name"]
