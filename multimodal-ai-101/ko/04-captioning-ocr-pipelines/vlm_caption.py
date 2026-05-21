"""Generated from book-content article."""

from openai import OpenAI

client = OpenAI()

def rich_caption(image_url: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": (
                    "Describe this image as alt text for visually impaired users "
                    "in 150 characters or less. "
                    "Include the objects, the scene, and key numbers if a chart "
                    "or table is present."
                )},
                {"type": "image_url", "image_url": {"url": image_url}},
            ],
        }],
    )
    return resp.choices[0].message.content
