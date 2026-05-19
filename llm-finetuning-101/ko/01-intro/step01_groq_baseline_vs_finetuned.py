"""Groq API로 베이스 모델 vs 파인튜닝 효과 시뮬레이션"""

from __future__ import annotations

import os
from textwrap import indent
from typing import Any

try:
    from groq import Groq
except ImportError:
    Groq = None

MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")


def request_completion(client: Any, system_prompt: str, user_prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.3,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content.strip()


def main() -> None:
    if Groq is None:
        print("groq 패키지가 없습니다. `pip install groq==1.2.0` 후 다시 실행하세요.")
        return

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("GROQ_API_KEY 환경 변수가 없습니다.")
        return

    client = Groq(api_key=api_key)
    user_request = "우리 SaaS 분석 제품의 장애 공지 메시지를 4문장으로 작성해 주세요. 원인, 영향 범위, 대응 상황, 다음 업데이트 시각을 포함해 주세요."

    print(
        "동일한 사용자 요청을 베이스 프롬프트와 도메인 특화 프롬프트로 각각 실행합니다."
    )
    print()
    print("사용자 요청")
    print(indent(user_request, prefix="  "))
    print()

    base_response = request_completion(
        client,
        "당신은 일반적인 한국어 비서입니다. 사용자의 요청에 짧고 무난하게 답하세요.",
        user_request,
    )
    tuned_response = request_completion(
        client,
        "당신은 B2B SaaS 운영 공지 작성에 특화된 모델입니다. 제품명 PulseBoard, 고객 대상 톤, 상태 요약, 다음 업데이트 시각, 재발 방지 의지를 반영해 구조화된 공지를 작성하세요.",
        user_request,
    )

    print("베이스 모델 스타일 응답")
    print("-" * 80)
    print(base_response)
    print()
    print("파인튜닝된 모델 스타일 응답")
    print("-" * 80)
    print(tuned_response)


if __name__ == "__main__":
    main()
