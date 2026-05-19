"""Llm Apps Ops 101 - Episode 6: Ops complete."""

from __future__ import annotations

from en.common import call_groq, utc_now
from en.ep02_cost_tracking import CostTracker, PricingTable, TTLCache
from en.ep03_evaluation import EvaluationCase, LLMJudge
from en.ep04_security import InputValidator, OutputFilter
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="llm-apps-ops-101 en complete")
validator = InputValidator(max_length=1200)
filter_ = OutputFilter()
cache = TTLCache(ttl_seconds=60)
tracker = CostTracker(PricingTable())
judge = LLMJudge()


class OpsRequest(BaseModel):
    """Ops request."""

    prompt: str = Field(min_length=1, max_length=1200)
    evaluate: bool = True


@app.get("/health")
def health() -> dict[str, str]:
    """Health."""
    return {"status": "ok", "ts": utc_now()}


@app.post("/answer")
def answer(request: OpsRequest) -> dict[str, object]:
    """Answer."""
    validation = validator.validate(request.prompt)
    if not validation.accepted:
        raise HTTPException(status_code=400, detail=validation.reason)

    cached = cache.get(request.prompt)
    cache_hit = cached is not None
    if cache_hit:
        answer_text = cached
        usage = {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
        estimated_cost_usd = 0.0
        latency_ms = 0.0
    else:
        try:
            result = call_groq(
                system_prompt="You are an English operations assistant that helps with incident response.",
                user_prompt=request.prompt,
                max_tokens=300,
            )
        except Exception as exc:
            raise HTTPException(
                status_code=502, detail=f"Groq call failed: {exc}"
            ) from exc
        answer_text = filter_.redact(result.text)
        cache.set(request.prompt, answer_text)
        tracker.track("ops-complete", request.prompt, answer_text)
        usage = {
            "input_tokens": result.input_tokens,
            "output_tokens": result.output_tokens,
            "total_tokens": result.total_tokens,
        }
        estimated_cost_usd = result.estimated_cost_usd
        latency_ms = round(result.latency_ms, 1)

    evaluation: dict[str, object] | None = None
    if request.evaluate:
        evaluation = judge.evaluate(
            EvaluationCase(
                question=request.prompt,
                answer=answer_text,
                reference="An ops assistant should separate likely root causes from mitigations and keep the response concise.",
            )
        )

    return {
        "answer": answer_text,
        "cache_hit": cache_hit,
        "usage": usage,
        "estimated_cost_usd": estimated_cost_usd,
        "latency_ms": latency_ms,
        "evaluation": evaluation,
        "cost_summary": tracker.summary(),
    }
