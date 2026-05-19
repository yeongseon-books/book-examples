"""Generate synthetic instruction-response pairs with Groq"""

from __future__ import annotations

import json
import os
from pathlib import Path

try:
    from groq import Groq
except ImportError:
    Groq = None

MODEL = os.getenv('GROQ_MODEL', 'llama-3.1-8b-instant')
OUTPUT_PATH = Path(__file__).resolve().parent / 'outputs' / 'synthetic_pairs.json'


def extract_json(text: str):
    text = text.strip()
    if text.startswith('```'):
        lines = [line for line in text.splitlines() if not line.startswith('```')]
        text = '\n'.join(lines).strip()
    return json.loads(text)


def main() -> None:
    if Groq is None:
        print('Skipping synthetic generation because the groq package is unavailable.')
        return

    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        print('Skipping synthetic generation because GROQ_API_KEY is missing.')
        return

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.5,
        messages=[
            {'role': 'system', 'content': 'You are a dataset generation assistant. Output only a JSON array.'},
            {'role': 'user', 'content': 'Generate five instruction-response pairs for fine-tuning a customer support chatbot as a JSON array. Each item must have instruction, response, and category fields. Write everything in English.'},
        ],
    )
    content = response.choices[0].message.content or "[]"
    items = extract_json(content)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Saved: {OUTPUT_PATH}")
    print(json.dumps(items, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
