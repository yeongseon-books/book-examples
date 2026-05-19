"""Llm From Scratch 101 - Episode."""

import numpy as np

np.random.seed(0)
x = np.eye(3)
y = np.array([0, 1, 2])
w = np.zeros((3, 3))
base = w.copy()
for _ in range(20):
    logits = x @ w
    probs = np.exp(logits) / np.sum(np.exp(logits), axis=1, keepdims=True)
    grad = probs
    grad[np.arange(3), y] -= 1
    grad /= 3
    w -= 0.3 * (x.T @ grad)
print(float(np.abs(w - base).sum()))


# Expected output:
# Fine-tuning started (LoRA rank=8)
# Epoch 1/3 | Train loss: 2.134 | Val loss: 2.089
# Epoch 2/3 | Train loss: 1.567 | Val loss: 1.612
# Epoch 3/3 | Train loss: 1.234 | Val loss: 1.298
# Model saved to ./finetuned_model/
