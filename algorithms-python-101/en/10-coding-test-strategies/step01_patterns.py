"""Algorithms Python 101 - Episode 1: Patterns."""


def longest_unique_substring(text: str) -> int:
    """Longest unique substring."""
    last_seen: dict[str, int] = {}
    left = 0
    best = 0
    for right, ch in enumerate(text):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    print(longest_unique_substring("abcabcbb"))
