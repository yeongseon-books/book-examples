"""Generated from book-content article."""

import faiss
import numpy as np

DIM = 512  # ViT-B/32

# 1. Image corpus -> embeddings -> index
image_paths = ["img_001.jpg", "img_002.jpg", "img_003.jpg"]
image_embeds = embed_image(image_paths).cpu().numpy().astype("float32")

index = faiss.IndexFlatIP(DIM)  # inner product == cosine for normalized vectors
index.add(image_embeds)

# 2. Text query -> embedding -> search
query = embed_text(["a sunset over the ocean"]).cpu().numpy().astype("float32")
scores, ids = index.search(query, k=3)
for rank, (i, s) in enumerate(zip(ids[0], scores[0]), 1):
    print(f"{rank}. {image_paths[i]} (score={s:.3f})")
