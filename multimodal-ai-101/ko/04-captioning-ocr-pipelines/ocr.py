"""Generated from book-content article."""

from PIL import Image, ImageOps

def auto_rotate(path: str) -> Image.Image:
    img = Image.open(path)
    return ImageOps.exif_transpose(img)
