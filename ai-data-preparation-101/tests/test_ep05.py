from conftest import run_dict


def test_ep05_chunk() -> None:
    result = run_dict("ko/05-tokenization-chunking/step01_token_chunk.py")
    assert int(result["tokens"]) >= int(result["first_chunk_size"])
    assert int(result["chunks"]) >= 2
