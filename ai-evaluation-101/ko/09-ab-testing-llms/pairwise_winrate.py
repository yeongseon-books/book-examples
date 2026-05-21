# ab/pairwise_winrate.py
import json

from openai import OpenAI

client = OpenAI()

def get_response(model: str, question: str) -> str:
    return client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": question}],
        temperature=0,
    ).choices[0].message.content

def judge_pairwise(question, ans_a, ans_b) -> str:
    prompt = f"""Pick the better answer.
Question: {question}
Answer A: {ans_a}
Answer B: {ans_b}
Output JSON: {{"winner": "A" | "B" | "Tie", "reason": "..."}}
"""
    r = client.chat.completions.create(
        model="gpt-4o", temperature=0,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
    )
    return json.loads(r.choices[0].message.content)["winner"]

def ab_test(questions: list[str], model_a: str, model_b: str) -> dict:
    results = {"A": 0, "B": 0, "Tie": 0}
    for q in questions:
        ans_a = get_response(model_a, q)
        ans_b = get_response(model_b, q)
        # Control position bias by swapping (Ep4)
        v1 = judge_pairwise(q, ans_a, ans_b)
        v2 = judge_pairwise(q, ans_b, ans_a)
        flip = {"A": "B", "B": "A", "Tie": "Tie"}
        if v1 == flip[v2]:
            results[v1] += 1
        else:
            results["Tie"] += 1
    total = sum(results.values())
    return {
        "win_rate_a": results["A"] / total,
        "win_rate_b": results["B"] / total,
        "tie_rate":   results["Tie"] / total,
        "n":          total,
    }
