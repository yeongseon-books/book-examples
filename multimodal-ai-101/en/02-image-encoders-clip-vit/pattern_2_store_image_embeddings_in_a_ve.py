"""Generated from book-content article."""

import faiss
import numpy as np
import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").eval()
proc = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def embed_images(paths: list[str]) -> np.ndarray:
    imgs = [Image.open(p).convert("RGB") for p in paths]
    inputs = proc(images=imgs, return_tensors="pt")
    with torch.no_grad():
        feats = model.get_image_features(**inputs)
    feats = feats / feats.norm(dim=-1, keepdim=True)
    return feats.cpu().numpy().astype("float32")

paths = ["a.jpg", "b.jpg", "c.jpg", "d.jpg"]
vecs = embed_images(paths)

index = faiss.IndexFlatIP(vecs.shape[1])  # cosine = inner product on normalized
index.add(vecs)

# query by text
query = proc(text=["a red sports car"], return_tensors="pt", padding=True)
with torch.no_grad():
    qv = model.get_text_features(**query)
qv = (qv / qv.norm(dim=-1, keepdim=True)).cpu().numpy().astype("float32")

D, I = index.search(qv, k=3)
print("top-3:", [paths[i] for i in I[0]])
