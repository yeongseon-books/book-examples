"""Generated from book-content article."""

import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

images = [Image.open(p) for p in ["cat.jpg", "dog.jpg", "car.jpg"]]
queries = ["a photo of a cat", "a vehicle on the street"]

inputs = processor(text=queries, images=images,
                   return_tensors="pt", padding=True)

with torch.no_grad():
    out = model(**inputs)

# image-text similarity matrix (queries x images)
logits = out.logits_per_text
probs = logits.softmax(dim=-1)
print(probs)
