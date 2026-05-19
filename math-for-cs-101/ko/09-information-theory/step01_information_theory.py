from common import entropy, kl_divergence, huffman_code_lengths


def sample_metrics():
    p = [0.5, 0.5]
    q = [0.75, 0.25]
    lengths = huffman_code_lengths({'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5})
    return entropy(p), kl_divergence(p, q), lengths
