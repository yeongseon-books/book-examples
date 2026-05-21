"""Generated from book-content article."""

import torch
from PIL import Image
from transformers import BlipForConditionalGeneration, BlipProcessor

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
).eval()

def caption(img_path: str, prompt: str | None = None) -> str:
    img = Image.open(img_path).convert("RGB")
    if prompt:
        inputs = processor(img, prompt, return_tensors="pt")
    else:
        inputs = processor(img, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=50)
    return processor.decode(out[0], skip_special_tokens=True)

print(caption("samples/dog.jpg"))
# > a brown dog sitting on a wooden floor
print(caption("samples/dog.jpg", prompt="a photography of"))
# > a photography of a brown dog with a happy face
