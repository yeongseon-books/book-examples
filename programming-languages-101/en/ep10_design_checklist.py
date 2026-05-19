from common import FeatureScore

def score_language(orthogonality: int, readability: int, safety: int, tooling: int) -> dict:
    fs = FeatureScore(orthogonality, readability, safety, tooling)
    return {"total": fs.total(), "pass": fs.total() >= 24}
