"""Generated from book-content article."""

from PIL import Image

def prepare_for_vlm(path: str, max_side: int = 1024) -> Image.Image:
    img = Image.open(path).convert("RGB")
    w, h = img.size
    scale = min(max_side / max(w, h), 1.0)
    if scale < 1.0:
        img = img.resize((int(w * scale), int(h * scale)),
                         Image.LANCZOS)
    return img
