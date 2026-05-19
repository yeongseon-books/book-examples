import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import exact_match


def run() -> dict[str, float]:
    references = ["seoul", "retrieval augmented generation", "python"]
    predictions = ["Seoul", "RAG means retrieval augmented generation", "python"]
    hit = sum(exact_match(p, r) for p, r in zip(predictions, references))
    accuracy = hit / len(references)
    return {"accuracy": accuracy, "has_regression_risk": float(accuracy < 1.0)}


if __name__ == "__main__":
    print(run())
