"""Generated from book-content article."""

from pathlib import Path

import numpy as np
import torch


def get_batch(split: str, batch_size: int = 4, block_size: int = 8):
    data_path = Path("data") / ("train.bin" if split == "train" else "val.bin")
    data = np.memmap(data_path, dtype=np.uint16, mode="r")
    ix = torch.randint(len(data) - block_size - 1, (batch_size,))
    x = torch.stack([
        torch.from_numpy(np.array(data[int(i) : int(i) + block_size], dtype=np.int64))
        for i in ix
    ])
    y = torch.stack([
        torch.from_numpy(
            np.array(data[int(i) + 1 : int(i) + block_size + 1], dtype=np.int64)
        )
        for i in ix
    ])
    return x, y

x, y = get_batch("train")
print(x.shape, y.shape)
print(x[0])
print(y[0])
