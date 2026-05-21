# finetune.py
import json
from dataclasses import asdict

import torch
import torch.nn.functional as F
from data import encode
from model import GPT, GPTConfig


def load_rows(path="instructions.jsonl"):
    with open(path, encoding="utf-8") as f: return [json.loads(line) for line in f]

def build_example(row, block_size):
    prompt = f"Q: {row['instruction']}\nA:"
    full = f"{prompt} {row['response']}"[:block_size]
    ids = encode(full)
    x = torch.tensor(ids[:-1], dtype=torch.long)
    y = torch.tensor(ids[1:], dtype=torch.long)
    prompt_len = min(len(encode(prompt)), len(ids))
    y[: max(prompt_len - 1, 0)] = -100
    return x, y

device = "cuda" if torch.cuda.is_available() else "cpu"
ckpt = torch.load("ckpt.pt", map_location=device)
config = GPTConfig(**ckpt["config"])
model = GPT(config).to(device); model.load_state_dict(ckpt["model"])
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-5)
rows = load_rows()

for step in range(500):
    row = rows[step % len(rows)]
    xb, yb = build_example(row, config.block_size)
    xb, yb = xb[None, :].to(device), yb[None, :].to(device)
    logits, _ = model(xb)
    loss = F.cross_entropy(logits.view(-1, config.vocab_size), yb.view(-1), ignore_index=-100)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    optimizer.step()

torch.save({"model": model.state_dict(), "config": asdict(config)}, "ckpt_sft.pt")
