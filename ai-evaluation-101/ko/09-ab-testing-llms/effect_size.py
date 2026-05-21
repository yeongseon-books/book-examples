# ab/effect_size.py
import math


def cohen_h(p1: float, p2: float) -> float:
    """Effect size (Cohen's h) between two proportions."""
    phi1 = 2 * math.asin(math.sqrt(p1))
    phi2 = 2 * math.asin(math.sqrt(p2))
    return abs(phi1 - phi2)

# Interpretation (Cohen, 1988):
# 0.2 = small, 0.5 = medium, 0.8 = large
print(cohen_h(0.51, 0.50))  # 0.020 ← negligible
print(cohen_h(0.60, 0.50))  # 0.201 ← small but meaningful
print(cohen_h(0.70, 0.50))  # 0.412 ← clearly meaningful
