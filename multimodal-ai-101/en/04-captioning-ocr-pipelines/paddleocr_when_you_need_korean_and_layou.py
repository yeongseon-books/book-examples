"""Generated from book-content article."""

from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="korean")

def ocr_with_boxes(img_path: str) -> list[dict]:
    result = ocr.ocr(img_path, cls=True)
    rows = []
    for line in result[0]:
        bbox, (text, conf) = line
        rows.append({
            "text": text,
            "confidence": float(conf),
            "bbox": bbox,  # 4-point polygon
        })
    return rows

for r in ocr_with_boxes("samples/receipt.jpg")[:5]:
    print(f"[{r['confidence']:.2f}] {r['text']}")
