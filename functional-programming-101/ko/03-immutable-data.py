"""Functional Programming 101 - Episode 3: Immutable data."""

from __future__ import annotations

from common import ImmutableState, immutable_append, impossible_mutation


def next_state(state: ImmutableState, value: int) -> ImmutableState:
    """Next state."""
    return immutable_append(state, value)


if __name__ == "__main__":
    s1 = ImmutableState(values=(1, 2))
    s2 = next_state(s1, 3)
    print(s1, s2, impossible_mutation(s1).__name__)
