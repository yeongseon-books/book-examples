"""Generated from book-content article."""

from diffusers import StableDiffusionInpaintPipeline
from diffusers.utils import load_image

pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-inpainting",
    torch_dtype=torch.float16,
).to("cuda")

init = load_image("samples/product.png")
mask = load_image("samples/product_mask.png")  # white = replace, black = keep

result = pipe(
    prompt="a wooden desk with morning sunlight, soft shadow",
    image=init, mask_image=mask,
    num_inference_steps=30, guidance_scale=7.5,
).images[0]
result.save("product_recomposed.png")
