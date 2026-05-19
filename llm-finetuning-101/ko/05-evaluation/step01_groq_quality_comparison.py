"""Groq으로 파인튜닝 전/후 응답 품질 비교"""

from __future__ import annotations

import os
import textwrap
from typing import Any

try:
    from groq import Groq
except ImportError:
    Groq = None

MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")


def complete(client: Any, system_prompt: str, user_prompt: str) -> str:
    """Complete."""
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content.strip()


def judge(client: Any, prompt: str, first: str, second: str) -> str:
    """Judge."""
    judge_prompt = textwrap.dedent(
        f"""
        두 응답 중 더 나은 답을 고르고 이유를 3줄 이내로 설명하세요.

        질문:
        {prompt}

        응답 A:
        {first}

        응답 B:
        {second}
        """
    ).strip()
    return complete(
        client, "당신은 평가자입니다. 정확성, 구체성, 톤을 봅니다.", judge_prompt
    )


def main() -> None:
    """Main."""
    if Groq is None:
        print("groq 패키지가 없어 비교를 건너뜁니다.")
        return

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("GROQ_API_KEY 환경 변수가 없어 비교를 건너뜁니다.")
        return

    client = Groq(api_key=api_key)
    prompt = '다음 고객 문의에 답하세요: "새 요금제에서 감사 로그는 얼마나 보관되나요?"'
    base_answer = complete(
        client, "당신은 범용 비서입니다. 모르면 일반적인 답을 주세요.", prompt
    )
    tuned_answer = complete(
        client,
        "당신은 PulseBoard 제품 문서를 학습한 고객지원 모델입니다. 보관 기간, 플랜 제한, 문의 경로를 구체적으로 설명하세요.",
        prompt,
    )
    verdict = judge(client, prompt, base_answer, tuned_answer)

    print("응답 A")
    print("-" * 80)
    print(base_answer)
    print()
    print("응답 B")
    print("-" * 80)
    print(tuned_answer)
    print()
    print("평가 결과")
    print("-" * 80)
    print(verdict)


if __name__ == "__main__":
    main()
