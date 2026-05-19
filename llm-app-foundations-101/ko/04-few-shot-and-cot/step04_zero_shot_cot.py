"""
Step 04 — zero-shot Chain-of-Thought
======================================================
실행:
    python step04_zero_shot_cot.py

단계적으로 생각해 달라는 한 문장으로 복합 계산 문제의
중간 추론 단계를 끌어내는 패턴입니다.
"""
import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    question = (
        "온라인 강의가 120000원입니다. 쿠폰 10%를 먼저 적용하고, "
        "그 결과에 부가세 10%를 붙이면 최종 결제 금액은 얼마인가요?"
    )

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "당신은 계산 과정을 차분히 설명하는 도우미입니다.",
            },
            {
                "role": "user",
                "content": question + " 단계적으로 생각해 주세요. 마지막 줄에는 final_answer: <숫자>원 형식으로만 적어 주세요.",
            },
        ],
        temperature=0.0,
    )

    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
