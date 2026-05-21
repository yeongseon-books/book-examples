"""Llm From Scratch 101 - 1편: tokenizer 예제."""

import numpy as np
from common import CharTokenizer

np.random.seed(0)
tok = CharTokenizer("hello tiny llm")
ids = tok.encode("hello")
print(ids, tok.decode(ids))


# Expected output:
# Vocabulary size: 5000
# Encoded: 'hello world' → [142, 867]
# Decoded: [142, 867] → 'hello world'
