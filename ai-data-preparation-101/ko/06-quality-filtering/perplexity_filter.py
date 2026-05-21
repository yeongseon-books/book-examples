# pip install kenlm
import math

import kenlm


class PerplexityFilter:
    def __init__(self, model_path: str, max_perplexity: float = 1000.0):
        self.model = kenlm.Model(model_path)
        self.max_perplexity = max_perplexity

    def score(self, text: str) -> float:
        # KenLM returns log10 probability
        log_prob = self.model.score(text, bos=True, eos=True)
        n_tokens = len(text.split()) + 1
        return 10 ** (-log_prob / n_tokens)

    def passes(self, text: str) -> bool:
        return self.score(text) <= self.max_perplexity

# Use a KenLM model trained on Wikipedia as the reference
pf = PerplexityFilter("wiki-en.binary", max_perplexity=500.0)
