"""Llm From Scratch 101 - Episode."""

import numpy as np
from common import CharTokenizer

np.random.seed(0)
tok = CharTokenizer("hello tiny llm")
ids = tok.encode("hello")
print(ids, tok.decode(ids))
