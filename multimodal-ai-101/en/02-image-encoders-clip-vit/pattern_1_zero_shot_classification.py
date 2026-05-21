"""Generated from book-content article."""

import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
proc = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

labels = ["cat", "dog", "car", "airplane"]
prompts = [f"a photo of a {l}" for l in labels]
img = Image.open("samples/test.jpg").convert("RGB")

inputs = proc(text=prompts, images=img, return_tensors="pt", padding=True)
with torch.no_grad():
    out = model(**inputs)

probs = out.logits_per_image.softmax(dim=-1)[0]
for label, p in zip(labels, probs, strict=False):
    print(f"{label:>10}: {p:.3f}")
