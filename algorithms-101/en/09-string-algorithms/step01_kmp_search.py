"""Algorithms 101 - Episode 1: Kmp search."""

from __future__ import annotations


def compute_failure(pat: str) -> list[int]:
    """Compute failure."""
    fail = [0] * len(pat)
    k = 0
    for i in range(1, len(pat)):
        while k > 0 and pat[k] != pat[i]:
            k = fail[k - 1]
        if pat[k] == pat[i]:
            k += 1
        fail[i] = k
    return fail


def kmp_search(text: str, pat: str) -> int:
    """Kmp search."""
    if not pat:
        return 0
    fail = compute_failure(pat)
    j = 0
    for i, c in enumerate(text):
        while j > 0 and c != pat[j]:
            j = fail[j - 1]
        if c == pat[j]:
            j += 1
            if j == len(pat):
                return i - j + 1
    return -1


def run() -> dict[str, object]:
    """Run."""
    text = "ababcababcabc"
    pat = "ababcabc"
    return {"text": text, "pat": pat, "index": kmp_search(text, pat)}


if __name__ == "__main__":
    print(run())
