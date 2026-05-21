"""Generated from book-content article."""

import httpx

VLM_ENDPOINT = "http://llava-worker:8000/v1/chat/completions"

async def stream_vlm_answer(image_bytes, question, caption, ocr_text, docs):
    prompt = build_prompt(question, caption, ocr_text, docs)
    payload = {
        "model": "llava-v1.6-mistral-7b",
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64(image_bytes)}"}},
            ],
        }],
        "stream": True,
        "max_tokens": 512,
    }
    async with httpx.AsyncClient(timeout=60) as client:
        async with client.stream("POST", VLM_ENDPOINT, json=payload) as resp:
            async for line in resp.aiter_lines():
                if line.startswith("data: "):
                    yield f"{line}\n\n"
