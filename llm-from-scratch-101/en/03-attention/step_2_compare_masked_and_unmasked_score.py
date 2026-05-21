"""Generated from book-content article."""

import math

import torch
import torch.nn.functional as F

q = torch.randn(1, 4, 8)
k = torch.randn(1, 4, 8)
scores = q @ k.transpose(-2, -1) / math.sqrt(k.size(-1))

print("without mask")
print(F.softmax(scores, dim=-1)[0])

tril = torch.tril(torch.ones(4, 4))
masked_scores = scores.masked_fill(tril == 0, float("-inf"))

print("with mask")
print(F.softmax(masked_scores, dim=-1)[0])
