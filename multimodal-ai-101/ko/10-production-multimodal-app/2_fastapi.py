"""Generated from book-content article."""

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

@app.post("/v1/multimodal/query")
async def multimodal_query(
    image: UploadFile = File(...),
    question: str = Form(...),
):
    image_bytes = await image.read()
    image_id = await store_image(image_bytes)

    # 1. cache check
    cached = await get_cache(image_id, question)
    if cached:
        return {"answer": cached, "cached": True}

    # 2. parallel pre-extraction
    caption_task = asyncio.create_task(run_caption(image_bytes))
    ocr_task = asyncio.create_task(run_ocr(image_bytes))
    embed_task = asyncio.create_task(run_embed(image_bytes))

    caption, ocr_text, embed = await asyncio.gather(caption_task, ocr_task, embed_task)

    # 3. RAG retrieval
    docs = await search_docs(embed, question, k=4)

    # 4. final VLM Q&A with streaming
    return StreamingResponse(
        stream_vlm_answer(image_bytes, question, caption, ocr_text, docs),
        media_type="text/event-stream",
    )
