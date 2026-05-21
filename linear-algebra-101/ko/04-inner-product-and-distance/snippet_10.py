"""Generated from book-content article."""

import numpy as np


def measure_distance_concentration(dim, n_samples=100):
    """
    차원별로 거리 분포를 측정합니다.
    """
    samples = np.random.randn(n_samples, dim)

    # 첨 번째 점에서 나머지 모든 점까지의 거리
    distances = []
    for i in range(1, n_samples):
        dist = np.linalg.norm(samples[0] - samples[i])
        distances.append(dist)

    distances = np.array(distances)
    mean_dist = np.mean(distances)
    std_dist = np.std(distances)
    min_dist = np.min(distances)
    max_dist = np.max(distances)

    # 분별력 지표: (max - min) / mean
    discriminability = (max_dist - min_dist) / mean_dist

    return {
        'dim': dim,
        'mean': mean_dist,
        'std': std_dist,
        'min': min_dist,
        'max': max_dist,
        'discriminability': discriminability
    }

# 차원별 비교
for d in [2, 10, 50, 100, 500]:
    result = measure_distance_concentration(d)
    print(f"Dim {result['dim']:3d}: mean={result['mean']:6.2f}, ",
          f"std={result['std']:5.2f}, disc={result['discriminability']:.3f}")
