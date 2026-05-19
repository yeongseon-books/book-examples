\
"""
Step 01 — 기본 few-shot 분류
======================================================
실행:
    python step01_few_shot_classify.py

system 프롬프트와 예시 쌍을 사용해 고객 문의를
category, priority, reason 형식으로 분류합니다.
"""
import os
from typing import Any

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    messages: list[Any] = [
        {
            "role": "system",
            "content": (
                "당신은 고객 문의를 분류하는 운영 도우미입니다. "
                "항상 아래 형식으로만 답하세요:\n"
                "category: <billing|technical|account>\n"
                "priority: <low|medium|high>\n"
                "reason: <한 문장>"
            ),
        },
        {"role": "user", "content": "결제는 됐는데 영수증 메일이 오지 않았어요."},
        {
            "role": "assistant",
            "content": (
                "category: billing\n"
                "priority: medium\n"
                "reason: 결제 이후 증빙 메일 누락 문제라 과금 영역으로 본다."
            ),
        },
        {"role": "user", "content": "비밀번호를 바꿨는데도 로그인에 계속 실패합니다."},
        {
            "role": "assistant",
            "content": (
                "category: account\n"
                "priority: high\n"
                "reason: 계정 접근 실패는 사용 불가 상태로 이어질 수 있다."
            ),
        },
        {"role": "user", "content": "CSV 업로드를 누르면 서버 오류가 납니다."},
    ]

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.2,
    )

    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
