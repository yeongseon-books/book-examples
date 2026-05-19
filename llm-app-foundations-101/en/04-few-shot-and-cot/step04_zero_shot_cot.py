"""
Step 04 — Zero-shot Chain-of-Thought
======================================================
Run:
    python step04_zero_shot_cot.py

Use a single step-by-step instruction to encourage
intermediate reasoning for a calculation task.
"""
import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    question = (
        "An online course costs 120000 won. If you apply a 10% coupon first and then add 10% VAT to the discounted price, "
        "what is the final payment amount?"
    )

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a careful assistant that explains calculations step by step.",
            },
            {
                "role": "user",
                "content": question + " Think step by step. On the last line, write only final_answer: <number> won.",
            },
        ],
        temperature=0.0,
    )

    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
