# rubric/judge_rubric.py
from openai import OpenAI
import json

client = OpenAI()

RUBRIC_PROMPT = """Grade the answer on each dimension from 1 to 5.

Question: {question}
Answer: {answer}

Dimensions:
1. Correctness — Are the facts right (5: all correct, 1: contains false info)
2. Completeness — Is the key information complete (5: complete, 1: more than half missing)
3. Clarity — Easy to understand (5: understood on first read, 1: incomprehensible)
4. Tone — Appropriate tone (5: polite and professional, 1: rude or off)

Respond with JSON only. No other text.
{{
  "correctness": <int>,
  "completeness": <int>,
  "clarity": <int>,
  "tone": <int>,
  "reasoning": "one-sentence justification"
}}
"""

def judge_rubric(question: str, answer: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": RUBRIC_PROMPT.format(
            question=question, answer=answer
        )}],
        temperature=0,
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)

if __name__ == "__main__":
    result = judge_rubric(
        "Where do I set the API key?",
        "Set it in the OPENAI_API_KEY environment variable."
    )
    print(result)
    # {'correctness': 5, 'completeness': 4, 'clarity': 5, 'tone': 5, 'reasoning': '...'}
