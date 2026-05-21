"""Generated from book-content article."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    session_id: str
    message: str

SESSIONS: dict[str, ResearchAgent] = {}

@app.post("/chat")
def chat(req: ChatRequest) -> dict[str, str]:
    agent = SESSIONS.setdefault(req.session_id, ResearchAgent())
    try:
        answer = agent.run(req.message)
        return {"answer": answer}
    except Exception as exc:
        raise HTTPException(500, detail=str(exc))
