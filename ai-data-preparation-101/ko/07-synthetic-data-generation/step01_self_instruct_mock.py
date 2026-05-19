"""Ai Data Preparation 101 - Episode 1: Self instruct mock."""

import random


def run(seed: int = 7) -> dict[str, object]:
    """Run."""
    rng = random.Random(seed)
    seeds = [
        {
            "instruction": "문장을 요약하세요.",
            "input": "데이터 준비는 모델 품질을 좌우합니다.",
            "output": "데이터 준비가 중요합니다.",
        },
        {
            "instruction": "문장을 분류하세요.",
            "input": "이 문서는 광고입니다.",
            "output": "label=spam",
        },
    ]
    generated: list[dict[str, str]] = []
    for task in seeds:
        tone = rng.choice(["간결하게", "두 단계로", "근거를 포함해"])
        generated.append(
            {
                "instruction": f"{task['instruction']} ({tone})",
                "input": task["input"],
                "output": task["output"],
            }
        )
    return {"count": len(generated), "samples": generated}


if __name__ == "__main__":
    print(run())
