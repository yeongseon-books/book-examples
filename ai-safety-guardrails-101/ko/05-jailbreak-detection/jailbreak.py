"""Generated from book-content article."""

from langdetect import detect


def multilingual_check(text: str) -> bool:
    try:
        lang = detect(text)
    except Exception:
        lang = "unknown"
    if lang != "en":
        translated = translate_to_english(text)  # DeepL, Google Translate, etc.
        if llm_judge(translated)["jailbreak"]:
            return True
    return llm_judge(text)["jailbreak"]
