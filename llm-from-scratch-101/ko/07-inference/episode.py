"""Llm From Scratch 101 - 7편: inference 예제."""

import numpy as np
from common import sample_topk

np.random.seed(0)
logits = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
print(sample_topk(logits, top_k=3, temperature=0.8))


# 예상 출력:
# Prompt: 'The meaning of life is'
# Generated: 'The meaning of life is to find purpose in what you do and'
# Tokens generated: 12
# Generation time: 0.34s
