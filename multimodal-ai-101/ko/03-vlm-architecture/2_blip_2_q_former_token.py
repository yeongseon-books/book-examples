"""Generated from book-content article."""

import torch
import torch.nn as nn

class QFormer(nn.Module):
    def __init__(self, num_queries: int = 32, vision_dim: int = 1408,
                 hidden_dim: int = 768, num_layers: int = 12):
        super().__init__()
        self.queries = nn.Parameter(torch.randn(num_queries, hidden_dim))
        layer = nn.TransformerDecoderLayer(
            d_model=hidden_dim, nhead=12, batch_first=True
        )
        self.decoder = nn.TransformerDecoder(layer, num_layers=num_layers)
        self.vision_proj = nn.Linear(vision_dim, hidden_dim)

    def forward(self, vision_features: torch.Tensor) -> torch.Tensor:
        # vision_features: (B, num_patches, vision_dim)
        B = vision_features.size(0)
        q = self.queries.unsqueeze(0).expand(B, -1, -1)  # (B, 32, hidden)
        memory = self.vision_proj(vision_features)
        return self.decoder(q, memory)  # (B, 32, hidden)
