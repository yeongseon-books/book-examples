"""Generated from book-content article."""

import torch
import torch.nn as nn

class LLaVAProjector(nn.Module):
    def __init__(self, vision_dim: int = 1024, llm_dim: int = 4096):
        super().__init__()
        self.proj = nn.Sequential(
            nn.Linear(vision_dim, llm_dim),
            nn.GELU(),
            nn.Linear(llm_dim, llm_dim),
        )

    def forward(self, vision_features: torch.Tensor) -> torch.Tensor:
        # vision_features: (B, num_patches, vision_dim)
        return self.proj(vision_features)  # (B, num_patches, llm_dim)
