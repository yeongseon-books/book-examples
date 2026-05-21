"""Generated from book-content article."""

import torch
import torch.nn as nn

class GatedCrossAttention(nn.Module):
    def __init__(self, dim: int, num_heads: int = 8):
        super().__init__()
        self.attn = nn.MultiheadAttention(dim, num_heads, batch_first=True)
        self.gate = nn.Parameter(torch.zeros(1))  # tanh-gated
        self.ff = nn.Sequential(nn.Linear(dim, dim * 4), nn.GELU(),
                                nn.Linear(dim * 4, dim))
        self.gate_ff = nn.Parameter(torch.zeros(1))

    def forward(self, x: torch.Tensor, vision: torch.Tensor) -> torch.Tensor:
        attn_out, _ = self.attn(x, vision, vision)
        x = x + torch.tanh(self.gate) * attn_out
        x = x + torch.tanh(self.gate_ff) * self.ff(x)
        return x
