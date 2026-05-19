\
"""
Step 05 — few-shot Chain-of-Thought
======================================================
실행:
    python step05_few_shot_cot.py

예시 답변 안에 추론 단계까지 포함한 few-shot CoT 패턴입니다.
풀이 순서를 고정해 final_answer 형식을 안정시킵니다.
"""
import os

from groq import Groq
from groq.types.chat import ChatCompletionMessageParam


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    messages: list[ChatCompletionMessageParam] = [
        {
            "role": "system",
            "content": (
                "당신은 주문 금액을 계산하는 도우미입니다. "
                "항상 1) 계산 단계 2) final_answer 형식으로 답하세요."
            ),
        },
        {
            "role": "user",
            "content": "가격이 50000원이고 20% 할인 후 배송비 3000원을 더하면 얼마인가요?",
        },
        {
            "role": "assistant",
            "content": (
                "1) 50000원의 20%는 10000원입니다.\n"
                "2) 할인 적용 후 금액은 40000원입니다.\n"
                "3) 배송비 3000원을 더하면 43000원입니다.\n"
                "final_answer: 43000원"
            ),
        },
        {
            "role": "user",
            "content": "가격이 80000원이고 25% 할인 후 배송비 5000원을 더하면 얼마인가요?",
        },
    ]

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.0,
    )

    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
