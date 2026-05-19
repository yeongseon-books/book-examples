"""Programming Languages 101 - Episode 10: Design checklist."""

from common import FeatureScore


def score_language(
    orthogonality: int, readability: int, safety: int, tooling: int
) -> dict:
    """Score language."""
    fs = FeatureScore(orthogonality, readability, safety, tooling)
    return {"total": fs.total(), "pass": fs.total() >= 24}
