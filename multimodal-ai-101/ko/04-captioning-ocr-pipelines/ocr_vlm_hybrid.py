"""Generated from book-content article."""

from openai import OpenAI
from paddleocr import PaddleOCR
from PIL import Image

ocr = PaddleOCR(use_angle_cls=True, lang="korean")
client = OpenAI()

def extract_then_reason(img_path: str, question: str) -> str:
    raw = ocr.ocr(img_path, cls=True)[0]
    text_block = "\n".join(line[1][0] for line in raw)
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": (
                "The user gives you OCR-extracted text and a question. "
                "Answer while accounting for OCR errors."
            )},
            {"role": "user", "content": (
                f"OCR result:\n```\n{text_block}\n```\n\nQuestion: {question}"
            )},
        ],
    )
    return resp.choices[0].message.content

answer = extract_then_reason("samples/receipt.jpg",
                             "What is the total amount paid and the store name?")
print(answer)
