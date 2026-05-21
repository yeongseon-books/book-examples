"""Generated from book-content article."""

import torch
import torch.nn as nn


class MiniEmbedding(nn.Module):
    def __init__(self, vocab_size: int, n_embd: int) -> None:
        super().__init__()
        self.weight = nn.Parameter(torch.randn(vocab_size, n_embd) * 0.02)

    def forward(self, idx: torch.Tensor) -> torch.Tensor:
        return self.weight[idx]

idx = torch.tensor([[0, 1, 2], [2, 1, 0]])
emb = MiniEmbedding(vocab_size=4, n_embd=3)
print(emb(idx).shape)
