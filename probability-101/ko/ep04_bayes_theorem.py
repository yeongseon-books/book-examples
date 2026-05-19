"""Probability 101 - Episode 4: Bayes theorem."""

from __future__ import annotations

from common import make_rng


def run(n: int = 300_000) -> dict[str, float]:
    """Run."""
    prev = 0.01
    sensitivity = 0.95
    specificity = 0.90
    fpr = 1 - specificity
    posterior = (sensitivity * prev) / (sensitivity * prev + fpr * (1 - prev))

    rng = make_rng()
    disease = rng.random(n) < prev
    test_pos = disease * (rng.random(n) < sensitivity) + (~disease) * (
        rng.random(n) < fpr
    )
    sim = float((disease & test_pos).sum() / test_pos.sum())
    return {"posterior": posterior, "sim": sim}


if __name__ == "__main__":
    print(run())
