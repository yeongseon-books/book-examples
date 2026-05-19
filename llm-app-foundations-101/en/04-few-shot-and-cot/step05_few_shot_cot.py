"""
Step 05 — Few-shot Chain-of-Thought
======================================================
Run:
    python step05_few_shot_cot.py

Include reasoning steps inside the example answer
to stabilize the final_answer format.
"""

import os

from groq import Groq
from groq.types.chat import ChatCompletionMessageParam


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    messages: list[ChatCompletionMessageParam] = [
        {
            "role": "system",
            "content": (
                "You are an assistant that calculates order totals. "
                "Always answer with 1) calculation steps and 2) a final_answer line."
            ),
        },
        {
            "role": "user",
            "content": "If the price is 50000 won, the discount is 20%, and shipping is 3000 won, what is the final amount?",
        },
        {
            "role": "assistant",
            "content": (
                "1) Twenty percent of 50000 won is 10000 won.\n"
                "2) After the discount, the price becomes 40000 won.\n"
                "3) Adding 3000 won for shipping gives 43000 won.\n"
                "final_answer: 43000 won"
            ),
        },
        {
            "role": "user",
            "content": "If the price is 80000 won, the discount is 25%, and shipping is 5000 won, what is the final amount?",
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


# Expected output:
# Input: 'The movie was absolutely terrible'
# Classification: negative
# Confidence: 0.95
