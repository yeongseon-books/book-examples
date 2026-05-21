# pip install fasttext-langdetect
from ftlangdetect import detect

def keep_languages(text: str, allowed: set[str], min_conf: float = 0.7) -> bool:
    sample = text[:1000]  # the head is enough
    result = detect(text=sample, low_memory=True)
    return result["lang"] in allowed and result["score"] >= min_conf

# Korean and English만 유지
ok = keep_languages(doc, allowed={"ko", "en"})
