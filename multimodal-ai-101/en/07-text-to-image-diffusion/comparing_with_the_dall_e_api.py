"""Generated from book-content article."""

from openai import OpenAI

client = OpenAI()
resp = client.images.generate(
    model="dall-e-3",
    prompt="A cozy reading nook with warm lamp, late afternoon light",
    size="1024x1024", quality="hd", n=1,
)
print(resp.data[0].url)
