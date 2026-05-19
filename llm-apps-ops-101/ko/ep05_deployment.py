from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from ko.common import call_groq, utc_now
from ko.ep04_security import InputValidator, OutputFilter

app = FastAPI(title="llm-apps-ops-101 ko deployment")
validator = InputValidator(max_length=1000)
filter_ = OutputFilter()


class ChatRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=1000)
    temperature: float = Field(default=0.2, ge=0.0, le=1.0)
    max_tokens: int = Field(default=250, ge=32, le=512)


class HealthResponse(BaseModel):
    status: str
    ts: str


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", ts=utc_now())


@app.post("/chat")
def chat(request: ChatRequest) -> dict[str, object]:
    validation = validator.validate(request.prompt)
    if not validation.accepted:
        raise HTTPException(status_code=400, detail=validation.reason)

    try:
        result = call_groq(
            system_prompt="당신은 운영팀을 돕는 한국어 LLM 어시스턴트입니다.",
            user_prompt=request.prompt,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Groq 호출 실패: {exc}") from exc

    answer = filter_.redact(result.text)
    return {
        "answer": answer,
        "model": result.model,
        "usage": {
            "input_tokens": result.input_tokens,
            "output_tokens": result.output_tokens,
            "total_tokens": result.total_tokens,
        },
        "latency_ms": round(result.latency_ms, 1),
        "estimated_cost_usd": result.estimated_cost_usd,
    }
