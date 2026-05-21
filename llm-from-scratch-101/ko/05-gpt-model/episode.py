"""Llm From Scratch 101 - 5편: gpt model 예제."""

import numpy as np
from common import TinyGPT, TinyGPTConfig

np.random.seed(0)
cfg = TinyGPTConfig(vocab_size=50, block_size=8, n_embd=16, n_head=2, n_layer=2)
model = TinyGPT(cfg)
idx = np.random.randint(0, 50, size=(2, 8))
print(model.forward(idx).shape)


# 예상 출력:
# GPT model parameters: 1,234,944
# Forward pass output shape: (1, 8, 5000)
# Logits sample: [-0.12, 0.45, -0.89, 0.23, ...]
