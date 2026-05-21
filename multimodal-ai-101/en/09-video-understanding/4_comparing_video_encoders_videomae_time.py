"""Generated from book-content article."""

import torch
from transformers import VideoMAEForVideoClassification, VideoMAEImageProcessor

processor = VideoMAEImageProcessor.from_pretrained("MCG-NJU/videomae-base-finetuned-kinetics")
model = VideoMAEForVideoClassification.from_pretrained("MCG-NJU/videomae-base-finetuned-kinetics")

frames = sample_uniform_frames("clip.mp4", n_frames=16)
inputs = processor(frames, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

pred_id = logits.argmax(-1).item()
print(f"Kinetics-400 label: {model.config.id2label[pred_id]}")
