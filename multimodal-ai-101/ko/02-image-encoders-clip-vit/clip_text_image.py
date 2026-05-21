"""Generated from book-content article."""

import torch
import torch.nn.functional as F

def clip_loss(image_emb: torch.Tensor, text_emb: torch.Tensor,
              temperature: float = 0.07) -> torch.Tensor:
    image_emb = F.normalize(image_emb, dim=-1)
    text_emb = F.normalize(text_emb, dim=-1)
    logits = image_emb @ text_emb.T / temperature
    targets = torch.arange(len(image_emb), device=logits.device)
    loss_i = F.cross_entropy(logits, targets)
    loss_t = F.cross_entropy(logits.T, targets)
    return (loss_i + loss_t) / 2
