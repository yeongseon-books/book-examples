"""Generated from book-content article."""

import torch
from PIL import Image
from transformers import ViTImageProcessor, ViTModel

processor = ViTImageProcessor.from_pretrained("google/vit-base-patch16-224")
model = ViTModel.from_pretrained("google/vit-base-patch16-224")

img = Image.open("samples/cat.jpg").convert("RGB")
inputs = processor(images=img, return_tensors="pt")

with torch.no_grad():
    out = model(**inputs)

cls_vec = out.last_hidden_state[:, 0, :]  # (1, 768)
print(cls_vec.shape, cls_vec.norm().item())
