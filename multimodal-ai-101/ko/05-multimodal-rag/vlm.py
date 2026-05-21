"""Generated from book-content article."""

import base64

from openai import OpenAI

client = OpenAI()

def encode(p: str) -> str:
    return base64.b64encode(open(p, "rb").read()).decode()

def answer(question: str, top_paths: list[str]) -> str:
    content = [{"type": "text", "text": question}]
    for p in top_paths[:3]:
        content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/png;base64,{encode(p)}"},
        })
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": content}],
    )
    return resp.choices[0].message.content
