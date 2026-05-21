"""Generated from book-content article."""

from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
from diffusers.utils import load_image
from controlnet_aux import OpenposeDetector

openpose = OpenposeDetector.from_pretrained("lllyasviel/Annotators")
control_image = openpose(load_image("samples/dancer.jpg"))

controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-openpose", torch_dtype=torch.float16
)
pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    controlnet=controlnet,
    torch_dtype=torch.float16,
).to("cuda")

image = pipe(
    "an astronaut dancing on the moon, dramatic lighting, cinematic",
    image=control_image,
    num_inference_steps=30,
    controlnet_conditioning_scale=1.0,
).images[0]
image.save("astronaut_pose.png")
