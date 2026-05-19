"""Tests for ep01 in Rag Deep Dive."""

from ko.ep01_loader_chunking import fixed_size_chunks, sentence_aware_chunks


def test_ep01_chunking_outputs_non_empty():
    """Test ep01 chunking outputs non empty."""
    text = "A. B. C. D."
    fixed = fixed_size_chunks(text, size=5, overlap=1)
    sent = sentence_aware_chunks(text, max_chars=6)
    assert len(fixed) >= 2
    assert len(sent) >= 2
