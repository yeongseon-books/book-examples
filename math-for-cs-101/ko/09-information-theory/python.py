"""Generated from book-content article."""

import math

def entropy(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0)

print(entropy([0.5, 0.5]))
print(entropy([0.9, 0.1]))
