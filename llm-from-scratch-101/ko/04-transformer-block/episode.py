"""Llm From Scratch 101 - 4편: transformer block 예제."""

import numpy as np
from common import TransformerBlock

np.random.seed(0)
x = np.random.randn(2, 6, 16)
blk = TransformerBlock(16, 2)
print(blk(x).shape)


# Expected output:
# TransformerBlock output shape: (1, 8, 64)
# LayerNorm applied: mean≈0.0, std≈1.0
# Residual connection: ✓
