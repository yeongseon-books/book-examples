from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from ko.common import CompletionResult, build_logger, call_groq, utc_now

logger = build_logger("ko.monitoring")


@dataclass(slots=True)
class LLMCallRecord:
    call_id: str = field(default_factory=lambda: str(uuid4())[:8])
    model: str = ""
    latency_ms: float = 0.0
    input_tokens: int = 0
    output_tokens: int = 0
    success: bool = True
    error: str = ""
    prompt_preview: str = ""
    response_preview: str = ""
    ts: str = field(default_factory=utc_now)

    def to_payload(self) -> dict[str, Any]:
        return {
            "call_id": self.call_id,
            "model": self.model,
            "latency_ms": round(self.latency_ms, 1),
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "success": self.success,
            "error": self.error,
            "prompt_preview": self.prompt_preview[:80],
            "response_preview": self.response_preview[:80],
            "ts": self.ts,
        }


class InstrumentedLLM:
    def __init__(self, model: str = "llama-3.1-8b-instant") -> None:
        self.model = model

    def invoke(self, system_prompt: str, user_prompt: str) -> tuple[str, LLMCallRecord]:
        record = LLMCallRecord(model=self.model, prompt_preview=user_prompt)
        logger.info(
            "LLM 호출을 시작합니다.",
            extra={"payload": {"call_id": record.call_id, "model": self.model}},
        )
        try:
            result: CompletionResult = call_groq(
                model=self.model,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
            )
            record.latency_ms = result.latency_ms
            record.input_tokens = result.input_tokens
            record.output_tokens = result.output_tokens
            record.response_preview = result.text
            logger.info(
                "LLM 호출이 완료되었습니다.", extra={"payload": record.to_payload()}
            )
            return result.text, record
        except Exception as exc:
            record.success = False
            record.error = str(exc)
            logger.exception(
                "LLM 호출이 실패했습니다.", extra={"payload": record.to_payload()}
            )
            raise


def sample_monitoring_session() -> None:
    llm = InstrumentedLLM()
    system_prompt = (
        "당신은 운영 대시보드에 짧은 상태 요약을 남기는 SRE 어시스턴트입니다."
    )
    user_prompt = "지난 5분 동안 지연 시간이 급증한 원인을 두 문장으로 요약해 주세요."
    answer, record = llm.invoke(system_prompt, user_prompt)
    print(answer)
    print(record.to_payload())


if __name__ == "__main__":
    sample_monitoring_session()
