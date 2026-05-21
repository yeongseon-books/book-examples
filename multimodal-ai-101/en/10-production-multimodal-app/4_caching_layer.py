"""Generated from book-content article."""

import hashlib

import redis.asyncio as redis

r = redis.from_url("redis://cache:6379")

def image_hash(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

async def get_cache(image_id: str, question: str) -> str | None:
    key = f"qa:{image_id}:{hashlib.sha256(question.encode()).hexdigest()}"
    return await r.get(key)

async def set_cache(image_id: str, question: str, answer: str):
    key = f"qa:{image_id}:{hashlib.sha256(question.encode()).hexdigest()}"
    await r.setex(key, 3600, answer)
