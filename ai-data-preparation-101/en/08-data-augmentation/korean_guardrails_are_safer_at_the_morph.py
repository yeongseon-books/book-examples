"""Generated from book-content article."""

from konlpy.tag import Okt

okt = Okt()
PROTECTED_POS = {"Josa", "Eomi", "Punctuation"}

def extract_replaceable_tokens(text: str) -> list[str]:
    tokens = []
    for surface, pos in okt.pos(text, norm=True, stem=True):
        if pos not in PROTECTED_POS and len(surface) > 1:
            tokens.append(surface)
    return tokens

text = "환불이 아직 안 됐는데 언제 처리되나요?"
print(extract_replaceable_tokens(text))
# ['환불', '아직', '처리']
