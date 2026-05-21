"""Generated from book-content article."""

from transformers import VideoLlavaProcessor, VideoLlavaForConditionalGeneration
import torch

processor = VideoLlavaProcessor.from_pretrained("LanguageBind/Video-LLaVA-7B-hf")
model = VideoLlavaForConditionalGeneration.from_pretrained(
    "LanguageBind/Video-LLaVA-7B-hf",
    torch_dtype=torch.float16,
    device_map="auto",
)

frames = sample_uniform_frames("cooking.mp4", n_frames=8)
prompt = "USER: <video>\nWhat is the person doing in this video? ASSISTANT:"
inputs = processor(text=prompt, videos=frames, return_tensors="pt").to(model.device, torch.float16)

with torch.no_grad():
    out = model.generate(**inputs, max_new_tokens=200)
print(processor.batch_decode(out, skip_special_tokens=True)[0])
