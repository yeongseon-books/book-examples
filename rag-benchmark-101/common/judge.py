from __future__ import annotations

import json
import os
import re

from common.models import JudgeScore


def parse_score(raw: str, default: float = 3.0) -> JudgeScore:
    try:
        matched = re.search(r"\{.*\}", raw, re.DOTALL)
        if not matched:
            return JudgeScore(default, "")
        payload = json.loads(matched.group(0))
        return JudgeScore(
            float(payload.get("score", default)), str(payload.get("reason", ""))
        )
    except Exception:
        return JudgeScore(default, "")


def judge_with_groq(
    system_prompt: str, user_prompt: str, model: str = "llama-3.1-8b-instant"
) -> JudgeScore:
    from groq import Groq

    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    response = client.chat.completions.create(
        model=model,
        temperature=0.0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    raw = response.choices[0].message.content or ""
    return parse_score(raw)


def evaluate_generation(
    question: str, context: str, answer: str, language: str
) -> dict[str, JudgeScore]:
    if language == "ko":
        faithfulness_user = (
            "다음 컨텍스트와 답변을 보고 faithfulness를 1-5점으로 평가하세요. "
            'JSON만 반환하세요: {"score": <1-5>, "reason": "한 문장"}.\n\n'
            f"컨텍스트:\n{context}\n\n답변:\n{answer}"
        )
        relevance_user = (
            "다음 질문과 답변을 보고 answer relevance를 1-5점으로 평가하세요. "
            'JSON만 반환하세요: {"score": <1-5>, "reason": "한 문장"}.\n\n'
            f"질문:\n{question}\n\n답변:\n{answer}"
        )
    else:
        faithfulness_user = (
            "Rate answer faithfulness from 1 to 5 using the context only. "
            'Return JSON only: {"score": <1-5>, "reason": "one sentence"}.\n\n'
            f"Context:\n{context}\n\nAnswer:\n{answer}"
        )
        relevance_user = (
            "Rate answer relevance from 1 to 5 for the question. "
            'Return JSON only: {"score": <1-5>, "reason": "one sentence"}.\n\n'
            f"Question:\n{question}\n\nAnswer:\n{answer}"
        )

    system_prompt = "You are a strict RAG evaluator. Always return valid JSON."
    return {
        "faithfulness": judge_with_groq(system_prompt, faithfulness_user),
        "answer_relevance": judge_with_groq(system_prompt, relevance_user),
    }
