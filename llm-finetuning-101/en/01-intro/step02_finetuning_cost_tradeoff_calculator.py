"""Fine-tuning cost and trade-off calculator"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Scenario:
    """Scenario."""

    model_name: str
    parameters_billion: float
    hours: float
    gpu_hour_price: float
    quality_gain: float
    engineering_days: int


def estimate_vram_gb(parameters_billion: float, bytes_per_param: int = 2) -> float:
    """Estimate vram gb."""
    return parameters_billion * 1_000_000_000 * bytes_per_param / 1024**3


def estimate_training_cost(hours: float, gpu_hour_price: float) -> float:
    """Estimate training cost."""
    return hours * gpu_hour_price


def main() -> None:
    """Main."""
    scenarios = [
        Scenario("7B full fine-tuning", 7.0, 18.0, 2.9, 0.18, 5),
        Scenario("7B LoRA", 7.0, 4.0, 2.9, 0.12, 2),
        Scenario("RAG + prompt tuning only", 7.0, 0.0, 2.9, 0.07, 3),
    ]

    print("Fine-tuning strategy comparison")
    print("=" * 80)
    for item in scenarios:
        vram = estimate_vram_gb(item.parameters_billion)
        cost = estimate_training_cost(item.hours, item.gpu_hour_price)
        score = item.quality_gain / max(item.engineering_days, 1)
        print(f"{item.model_name}")
        print(f"  - Estimated VRAM (fp16): {vram:.1f} GB")
        print(f"  - Training time: {item.hours:.1f} h")
        print(f"  - Estimated cost: ${cost:.2f}")
        print(f"  - Assumed quality gain: +{item.quality_gain * 100:.0f}%")
        print(f"  - Engineering effort score: {score:.3f}")
        print()

    print(
        "Interpretation: LoRA tends to deliver the best cost-to-quality ratio, full fine-tuning is the most expensive, and if RAG already solves the problem, skipping training is often better."
    )


if __name__ == "__main__":
    main()
