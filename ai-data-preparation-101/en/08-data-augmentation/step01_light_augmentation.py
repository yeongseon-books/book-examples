"""Ai Data Preparation 101 - Episode 8: data augmentation example."""

import random

SYN = {"fast": "quick", "important": "critical", "quality": "reliability"}


def augment(text: str, seed: int) -> str:
    """Augment."""
    rng = random.Random(seed)
    out: list[str] = []
    for token in text.split():
        if token in SYN and rng.random() < 0.6:
            out.append(SYN[token])
        else:
            out.append(token)
    return " ".join(out)


def run() -> dict[str, str]:
    """Run."""
    src = "fast data preparation is important for model quality"
    aug = augment(src, seed=11)
    return {"source": src, "augmented": aug}


if __name__ == "__main__":
    print(run())
