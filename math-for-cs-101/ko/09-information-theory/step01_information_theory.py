"""Math For Cs 101 - 9편: information theory 예제."""

from common import entropy, huffman_code_lengths, kl_divergence


def sample_metrics():
    """Sample metrics."""
    p = [0.5, 0.5]
    q = [0.75, 0.25]
    lengths = huffman_code_lengths({"a": 45, "b": 13, "c": 12, "d": 16, "e": 9, "f": 5})
    return entropy(p), kl_divergence(p, q), lengths
