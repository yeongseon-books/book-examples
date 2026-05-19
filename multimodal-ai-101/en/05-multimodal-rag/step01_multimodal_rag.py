from common import MultimodalRAG


def run(query: str = "receipt") -> str:
    rag = MultimodalRAG(
        [
            {"id": "doc-1", "image": "grid-a", "text": "receipt with totals"},
            {"id": "doc-2", "image": "grid-b", "text": "vision language architecture"},
        ]
    )
    return rag.retrieve("grid-a", query)[0]["id"]
