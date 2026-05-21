# server.py
from contextlib import asynccontextmanager

import torch
from data import decode, stoi
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from model import GPT, GPTConfig
from pydantic import BaseModel

templates = Jinja2Templates(directory="templates"); state = {}

class ChatBody(BaseModel):
    prompt: str
    history: list[dict[str, str]] = []
    max_new_tokens: int = 120

def build_prompt(history, prompt):
    lines = []
    for t in history: lines += [f"User: {t['user']}", f"Bot: {t['bot']}"]
    lines.append(f"User: {prompt}")
    lines.append("Bot:")
    return "\n".join(lines)

def encode_chat_text(text: str):
    dropped = sorted({c for c in text if c not in stoi})
    ids = [stoi[c] for c in text if c in stoi]
    if not ids:
        raise ValueError("Prompt became empty after dropping unsupported characters.")
    return ids, dropped

@asynccontextmanager
async def lifespan(app: FastAPI):
    d = "cuda" if torch.cuda.is_available() else "cpu"
    ckpt = torch.load("ckpt_sft.pt", map_location=d)
    m = GPT(GPTConfig(**ckpt["config"])).to(d); m.load_state_dict(ckpt["model"]); m.eval()
    state["device"] = d; state["model"] = m
    yield
    state.clear()

app = FastAPI(lifespan=lifespan)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(body: ChatBody):
    text = build_prompt(body.history, body.prompt)
    try:
        ids, dropped = encode_chat_text(text)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    idx = torch.tensor([ids], dtype=torch.long, device=state["device"])
    with torch.no_grad(): out = state["model"].generate(idx, body.max_new_tokens, 0.8, 20, 0.9)
    response = {"response": decode(out[0].tolist())[len(ids):]}
    if dropped:
        response["warning"] = f"Dropped unsupported characters: {''.join(dropped)}"
    return response

@app.get("/chat/stream")
async def chat_stream(prompt: str):
    async def event_gen():
        try:
            ids, dropped = encode_chat_text(build_prompt([], prompt))
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e)) from e
        if dropped:
            yield f"data: [warning] Dropped unsupported characters: {''.join(dropped)}\n\n"
        current = torch.tensor([ids], dtype=torch.long, device=state["device"])
        for _ in range(120):
            with torch.no_grad(): next_ids = state["model"].generate(current, 1, 0.8, 20, 0.9)
            current = next_ids; token_id = next_ids[0, -1].item()
            yield f"data: {decode([token_id])}\n\n"
    return StreamingResponse(event_gen(), media_type="text/event-stream")
