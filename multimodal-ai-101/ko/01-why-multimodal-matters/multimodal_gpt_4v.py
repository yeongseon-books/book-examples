"""Generated from book-content article."""

import base64
from openai import OpenAI

client = OpenAI()

def encode_image(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def analyze_receipt(image_path: str) -> dict:
    b64 = encode_image(image_path)
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": (
                        "Extract each item name and price from this receipt "
                        "and return a JSON array. "
                        'Format: [{"item": "...", "price": 0}]'
                    )},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{b64}"},
                    },
                ],
            }
        ],
        response_format={"type": "json_object"},
    )
    return resp.choices[0].message.content

print(analyze_receipt("samples/receipt.jpg"))
