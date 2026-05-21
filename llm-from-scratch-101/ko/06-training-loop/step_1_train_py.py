"""Generated from book-content article."""

import math
from dataclasses import asdict
from pathlib import Path

import numpy as np
import torch
from model import GPT, GPTConfig

batch_size = 32
block_size = 64
max_iters = 5000
eval_interval = 500
eval_iters = 50
learning_rate = 3e-4
weight_decay = 0.1
betas = (0.9, 0.95)
device = "cuda" if torch.cuda.is_available() else "cpu"

config = GPTConfig(block_size=block_size)
model = GPT(config).to(device)
optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=learning_rate,
    weight_decay=weight_decay,
    betas=betas,
)

train_data = np.memmap(Path("data") / "train.bin", dtype=np.uint16, mode="r")
val_data = np.memmap(Path("data") / "val.bin", dtype=np.uint16, mode="r")

def get_batch(split: str):
    data = train_data if split == "train" else val_data
    ix = torch.randint(len(data) - block_size - 1, (batch_size,))
    x = torch.stack([
        torch.from_numpy(np.array(data[i : i + block_size], dtype=np.int64))
        for i in ix.tolist()
    ])
    y = torch.stack([
        torch.from_numpy(np.array(data[i + 1 : i + block_size + 1], dtype=np.int64))
        for i in ix.tolist()
    ])
    return x.to(device), y.to(device)

def get_lr(it: int) -> float:
    warmup_iters = 100
    lr_decay_iters = 5000
    min_lr = learning_rate * 0.1
    if it < warmup_iters:
        return learning_rate * (it + 1) / warmup_iters
    if it > lr_decay_iters:
        return min_lr
    decay_ratio = (it - warmup_iters) / (lr_decay_iters - warmup_iters)
    coeff = 0.5 * (1.0 + math.cos(math.pi * decay_ratio))
    return min_lr + coeff * (learning_rate - min_lr)

@torch.no_grad()
def estimate_loss() -> dict[str, float]:
    model.eval()
    out = {}
    for split in ["train", "val"]:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            xb, yb = get_batch(split)
            _, loss = model(xb, yb)
            losses[k] = loss.item()
        out[split] = losses.mean().item()
    model.train()
    return out

for iter_num in range(max_iters + 1):
    lr = get_lr(iter_num)
    for param_group in optimizer.param_groups:
        param_group["lr"] = lr

    if iter_num % eval_interval == 0:
        losses = estimate_loss()
        print(
            f"step {iter_num}: train {losses['train']:.4f}, "
            f"val {losses['val']:.4f}, lr {lr:.6f}"
        )

    xb, yb = get_batch("train")
    optimizer.zero_grad(set_to_none=True)
    _, loss = model(xb, yb)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    optimizer.step()

torch.save({"model": model.state_dict(), "config": asdict(config)}, "ckpt.pt")
