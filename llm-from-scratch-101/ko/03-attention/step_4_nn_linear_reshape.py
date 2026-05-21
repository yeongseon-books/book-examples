"""Generated from book-content article."""

from dataclasses import dataclass
import math

import torch
import torch.nn as nn
import torch.nn.functional as F

@dataclass
class GPTConfig:
    vocab_size: int = 65
    block_size: int = 64
    n_layer: int = 6
    n_head: int = 4
    n_embd: int = 128

class CausalSelfAttention(nn.Module):
    def __init__(self, config: GPTConfig) -> None:
        super().__init__()
        assert config.n_embd % config.n_head == 0
        self.n_head = config.n_head
        self.head_size = config.n_embd // config.n_head
        self.key = nn.Linear(config.n_embd, config.n_embd, bias=False)
        self.query = nn.Linear(config.n_embd, config.n_embd, bias=False)
        self.value = nn.Linear(config.n_embd, config.n_embd, bias=False)
        self.proj = nn.Linear(config.n_embd, config.n_embd)
        self.register_buffer(
            "tril", torch.tril(torch.ones(config.block_size, config.block_size))
        )

    def forward(self, x: torch.Tensor):
        b, t, c = x.shape
        k = self.key(x).view(b, t, self.n_head, self.head_size).transpose(1, 2)
        q = self.query(x).view(b, t, self.n_head, self.head_size).transpose(1, 2)
        v = self.value(x).view(b, t, self.n_head, self.head_size).transpose(1, 2)

        wei = q @ k.transpose(-2, -1) / math.sqrt(self.head_size)
        wei = wei.masked_fill(self.tril[:t, :t] == 0, float("-inf"))
        wei = F.softmax(wei, dim=-1)

        out = wei @ v
        out = out.transpose(1, 2).contiguous().view(b, t, c)
        out = self.proj(out)
        self.last_attn = wei
        return out

config = GPTConfig()
attn = CausalSelfAttention(config)
x = torch.randn(2, 8, config.n_embd)
out = attn(x)
print(out.shape)
print(attn.last_attn.shape)
