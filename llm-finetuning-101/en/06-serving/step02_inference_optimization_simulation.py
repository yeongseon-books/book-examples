"""Inference optimization simulation"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class OptimizationCase:
    name: str
    latency_ms: float
    throughput_rps: float
    memory_gb: float


def main() -> None:
    baseline = OptimizationCase("baseline fp16 single request", 420.0, 2.4, 14.0)
    cases = [
        baseline,
        OptimizationCase("dynamic batching", 280.0, 5.8, 14.5),
        OptimizationCase("kv-cache reuse", 230.0, 6.3, 15.0),
        OptimizationCase("4-bit quantization", 260.0, 5.1, 8.2),
    ]
    print("Optimization comparison")
    print("=" * 80)
    for item in cases:
        latency_gain = (
            (baseline.latency_ms - item.latency_ms) / baseline.latency_ms * 100
        )
        throughput_gain = (
            (item.throughput_rps - baseline.throughput_rps)
            / baseline.throughput_rps
            * 100
        )
        print(f"{item.name}")
        print(f"  - Latency: {item.latency_ms:.1f} ms")
        print(f"  - Throughput: {item.throughput_rps:.1f} rps")
        print(f"  - Memory: {item.memory_gb:.1f} GB")
        print(f"  - Latency improvement: {latency_gain:+.1f}%")
        print(f"  - Throughput improvement: {throughput_gain:+.1f}%")
        print()


if __name__ == "__main__":
    main()
