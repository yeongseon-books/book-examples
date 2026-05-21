"""Llm From Scratch 101 - 2편: embedding 예제."""

import numpy as np
from common import Embedding, positional_encoding

np.random.seed(0)
emb = Embedding(50, 16)
idx = np.array([[1, 2, 3]])
out = emb(idx) + positional_encoding(3, 16)[None, :, :]
print(out.shape)


# Expected output:
# Embedding shape: (1, 8, 64)
# First token embedding[:5]: [0.0234, -0.1567, 0.0891, 0.2103, -0.0445]
