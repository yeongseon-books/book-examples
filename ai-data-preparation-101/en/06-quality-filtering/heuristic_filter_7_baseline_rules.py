"""Generated from book-content article."""

import re
from dataclasses import dataclass

@dataclass
class QualitySignals:
    n_chars: int
    n_words: int
    avg_word_len: float
    symbol_ratio: float
    digit_ratio: float
    upper_ratio: float
    repetition_ratio: float

def compute_signals(text: str) -> QualitySignals:
    n_chars = len(text)
    words = text.split()
    n_words = len(words)
    if n_words == 0:
        return QualitySignals(n_chars, 0, 0, 1, 1, 1, 1)
    avg_word_len = sum(len(w) for w in words) / n_words
    symbol_ratio = sum(1 for c in text if not c.isalnum() and not c.isspace()) / max(n_chars, 1)
    digit_ratio = sum(1 for c in text if c.isdigit()) / max(n_chars, 1)
    upper_ratio = sum(1 for c in text if c.isupper()) / max(n_chars, 1)
    # 5-gram repetition
    grams = [" ".join(words[i:i+5]) for i in range(len(words)-4)]
    repetition_ratio = 1 - len(set(grams)) / max(len(grams), 1)
    return QualitySignals(n_chars, n_words, avg_word_len,
                          symbol_ratio, digit_ratio, upper_ratio, repetition_ratio)

def passes_heuristic(text: str) -> tuple[bool, str]:
    s = compute_signals(text)
    if s.n_words < 50:
        return False, "too_short"
    if s.n_words > 100_000:
        return False, "too_long"
    if s.avg_word_len < 2 or s.avg_word_len > 15:
        return False, "bad_avg_word_len"
    if s.symbol_ratio > 0.3:
        return False, "symbol_heavy"
    if s.digit_ratio > 0.5:
        return False, "digit_heavy"
    if s.upper_ratio > 0.4:
        return False, "shouting"
    if s.repetition_ratio > 0.3:
        return False, "repetitive"
    return True, "ok"
