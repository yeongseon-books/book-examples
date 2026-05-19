"""파인튜닝 비용/트레이드오프 계산기"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Scenario:
    model_name: str
    parameters_billion: float
    hours: float
    gpu_hour_price: float
    quality_gain: float
    engineering_days: int


def estimate_vram_gb(parameters_billion: float, bytes_per_param: int = 2) -> float:
    return parameters_billion * 1_000_000_000 * bytes_per_param / 1024**3


def estimate_training_cost(hours: float, gpu_hour_price: float) -> float:
    return hours * gpu_hour_price


def main() -> None:
    scenarios = [
        Scenario("7B full fine-tuning", 7.0, 18.0, 2.9, 0.18, 5),
        Scenario("7B LoRA", 7.0, 4.0, 2.9, 0.12, 2),
        Scenario("RAG + prompt tuning only", 7.0, 0.0, 2.9, 0.07, 3),
    ]

    print("파인튜닝 전략 비교")
    print("=" * 80)
    for item in scenarios:
        vram = estimate_vram_gb(item.parameters_billion)
        cost = estimate_training_cost(item.hours, item.gpu_hour_price)
        score = item.quality_gain / max(item.engineering_days, 1)
        print(f"{item.model_name}")
        print(f"  - 예상 VRAM(fp16): {vram:.1f} GB")
        print(f"  - 학습 시간: {item.hours:.1f} h")
        print(f"  - 예상 비용: ${cost:.2f}")
        print(f"  - 품질 향상 가정: +{item.quality_gain * 100:.0f}%")
        print(f"  - 개발 난이도 점수: {score:.3f}")
        print()

    print(
        "해석: LoRA는 비용 대비 효율이 높고, 풀 파인튜닝은 가장 비싸며, RAG만으로 해결되는 문제라면 학습을 생략하는 편이 유리합니다."
    )


if __name__ == "__main__":
    main()
