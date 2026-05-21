"""Generated from book-content article."""

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    user_id: str
    team: str


def team_members(users: set[User], team: str) -> set[User]:
    return {u for u in users if u.team == team}
