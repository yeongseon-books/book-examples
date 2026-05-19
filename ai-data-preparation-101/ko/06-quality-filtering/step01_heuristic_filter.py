import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import quality_signals


def run() -> dict[str, object]:
    samples = [
        "This sentence looks normal and useful for training data pipelines.",
        "BUY NOW!!! 999999 CLICK CLICK CLICK",
    ]
    kept: list[str] = []
    for text in samples:
        sig = quality_signals(text)
        if (
            sig["n_words"] >= 6
            and sig["symbol_ratio"] < 0.25
            and sig["digit_ratio"] < 0.3
            and sig["upper_ratio"] < 0.25
        ):
            kept.append(text)
    return {"input": len(samples), "kept": len(kept), "kept_text": kept}


if __name__ == "__main__":
    print(run())
