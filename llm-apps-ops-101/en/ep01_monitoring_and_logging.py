from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from en.common import CompletionResult, build_logger, call_groq, utc_now

logger = build_logger('en.monitoring')


@dataclass(slots=True)
class LLMCallRecord:
    call_id: str = field(default_factory=lambda: str(uuid4())[:8])
    model: str = ''
    latency_ms: float = 0.0
    input_tokens: int = 0
    output_tokens: int = 0
    success: bool = True
    error: str = ''
    prompt_preview: str = ''
    response_preview: str = ''
    ts: str = field(default_factory=utc_now)

    def to_payload(self) -> dict[str, Any]:
        return {
            'call_id': self.call_id,
            'model': self.model,
            'latency_ms': round(self.latency_ms, 1),
            'input_tokens': self.input_tokens,
            'output_tokens': self.output_tokens,
            'success': self.success,
            'error': self.error,
            'prompt_preview': self.prompt_preview[:80],
            'response_preview': self.response_preview[:80],
            'ts': self.ts,
        }


class InstrumentedLLM:
    def __init__(self, model: str = 'llama-3.1-8b-instant') -> None:
        self.model = model

    def invoke(self, system_prompt: str, user_prompt: str) -> tuple[str, LLMCallRecord]:
        record = LLMCallRecord(model=self.model, prompt_preview=user_prompt)
        logger.info('Starting LLM call.', extra={'payload': {'call_id': record.call_id, 'model': self.model}})
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
            logger.info('LLM call completed.', extra={'payload': record.to_payload()})
            return result.text, record
        except Exception as exc:
            record.success = False
            record.error = str(exc)
            logger.exception('LLM call failed.', extra={'payload': record.to_payload()})
            raise


def sample_monitoring_session() -> None:
    llm = InstrumentedLLM()
    system_prompt = 'You are an SRE assistant writing short health summaries for an ops dashboard.'
    user_prompt = 'Summarize the likely cause of a five-minute latency spike in two sentences.'
    answer, record = llm.invoke(system_prompt, user_prompt)
    print(answer)
    print(record.to_payload())


if __name__ == '__main__':
    sample_monitoring_session()
