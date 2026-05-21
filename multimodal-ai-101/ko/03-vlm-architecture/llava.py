"""Generated from book-content article."""

import torch
from PIL import Image
from transformers import AutoProcessor, LlavaForConditionalGeneration

model_id = "llava-hf/llava-1.5-7b-hf"
processor = AutoProcessor.from_pretrained(model_id)
model = LlavaForConditionalGeneration.from_pretrained(
    model_id, torch_dtype=torch.float16, device_map="auto"
)

image = Image.open("samples/chart.png").convert("RGB")
prompt = "USER: <image>\nSummarize the key trend in this chart in one sentence.\nASSISTANT:"

inputs = processor(images=image, text=prompt, return_tensors="pt").to(model.device)
with torch.no_grad():
    output = model.generate(**inputs, max_new_tokens=128, do_sample=False)
print(processor.decode(output[0], skip_special_tokens=True))
