"""Generated from book-content article."""

class HybridIndex:
    def __init__(self, clip_index, text_index, items):
        self.clip = clip_index   # CLIP image vectors
        self.text = text_index   # caption+OCR text vectors
        self.items = items

    def search(self, query: str, k: int = 5,
               alpha: float = 0.5) -> list[dict]:
        # alpha=0: text only / alpha=1: image only
        d_clip, i_clip = self.clip.search(self._clip_q(query), k=k * 3)
        d_text, i_text = self.text.search(self._text_q(query), k=k * 3)
        scores: dict[int, float] = {}
        for d, i in zip(d_clip[0], i_clip[0]):
            scores[i] = scores.get(i, 0) + alpha * float(d)
        for d, i in zip(d_text[0], i_text[0]):
            scores[i] = scores.get(i, 0) + (1 - alpha) * float(d)
        ranked = sorted(scores.items(), key=lambda x: -x[1])[:k]
        return [self.items[i] for i, _ in ranked]
