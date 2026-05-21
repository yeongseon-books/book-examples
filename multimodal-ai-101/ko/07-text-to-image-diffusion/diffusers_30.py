"""Generated from book-content article."""

import torch
from diffusers import StableDiffusionXLPipeline

pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    variant="fp16",
).to("cuda")

prompt = (
    "A cozy reading nook with a warm lamp, an open book, "
    "a steaming mug of tea, late afternoon light, photorealistic, 35mm"
)
negative = "blurry, low quality, watermark, text, deformed hands"

image = pipe(
    prompt=prompt,
    negative_prompt=negative,
    num_inference_steps=30,
    guidance_scale=7.0,
    height=1024, width=1024,
).images[0]

image.save("nook.png")
