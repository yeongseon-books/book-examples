"""Generated from book-content article."""

import pytesseract
from PIL import Image


def ocr_simple(img_path: str, lang: str = "kor+eng") -> str:
    img = Image.open(img_path)
    return pytesseract.image_to_string(img, lang=lang)

print(ocr_simple("samples/screenshot.png"))
