"""Ai Data Preparation 101 - 8편: data augmentation 예제."""

import random

SYN = {"빠른": "신속한", "중요": "핵심", "품질": "퀄리티"}


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
    src = "빠른 데이터 준비는 모델 품질에 중요 합니다"
    aug = augment(src, seed=11)
    return {"source": src, "augmented": aug}


if __name__ == "__main__":
    print(run())
