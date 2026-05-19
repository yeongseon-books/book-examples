from __future__ import annotations

import math


FAQ_DATA = [
    "영업시간은 평일 오전 9시부터 오후 6시까지입니다.",
    "환불은 구매 후 7일 이내 고객센터를 통해 신청 가능합니다.",
    "프리미엄 요금제는 월 19,900원입니다.",
]


def embed(text: str) -> dict[str, int]:
    tokens = [t.strip(".,!? ") for t in text.split() if t.strip(".,!? ")]
    bag: dict[str, int] = {}
    for token in tokens:
        bag[token] = bag.get(token, 0) + 1
    return bag


def cosine_sim(a: dict[str, int], b: dict[str, int]) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0) * b.get(k, 0) for k in keys)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def search(query: str) -> str:
    for doc in FAQ_DATA:
        if any(token and token in doc for token in query.split()):
            return doc
    q = embed(query)
    scored = [(cosine_sim(q, embed(doc)), doc) for doc in FAQ_DATA]
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[0][1]


def answer_with_rag(query: str) -> str:
    context = search(query)
    return f"근거: {context}\n답변: 제공된 근거 기준으로 안내드립니다."
