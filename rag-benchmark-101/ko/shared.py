from __future__ import annotations

from common.models import BenchmarkConfig, EmbeddingCandidate, GenerationCase, PipelineCase, QueryGroundTruth, VectorIndexCandidate

CORPUS = [
    {"id": "d01", "text": "벡터 데이터베이스는 임베딩 벡터를 저장하고 유사도 검색을 지원합니다.", "topic": "vectordb"},
    {"id": "d02", "text": "FAISS는 Facebook AI Research에서 만든 고성능 벡터 검색 라이브러리입니다.", "topic": "faiss"},
    {"id": "d03", "text": "IndexFlatIP는 내적 기반의 정확한 검색을 제공합니다.", "topic": "faiss"},
    {"id": "d04", "text": "코사인 유사도는 두 벡터 방향의 유사성을 측정합니다.", "topic": "similarity"},
    {"id": "d05", "text": "HNSW는 그래프 기반 ANN 인덱스로 빠른 근사 검색에 적합합니다.", "topic": "ann"},
    {"id": "d06", "text": "임베딩 모델은 텍스트를 숫자 벡터로 바꿔 의미 공간에 배치합니다.", "topic": "embedding"},
    {"id": "d07", "text": "all-MiniLM-L6-v2는 가볍고 빠른 384차원 임베딩 모델입니다.", "topic": "embedding"},
    {"id": "d08", "text": "청크 크기가 너무 작으면 문맥이 끊기고 너무 크면 잡음이 늘어납니다.", "topic": "chunking"},
    {"id": "d09", "text": "하이브리드 검색은 키워드 검색과 벡터 검색을 결합해 재현율을 높입니다.", "topic": "hybrid"},
    {"id": "d10", "text": "리랭킹은 1차 검색 결과의 순서를 다시 정렬해 정밀도를 높입니다.", "topic": "reranking"},
]

QUERIES = [
    QueryGroundTruth("FAISS란 무엇인가요?", {"d02", "d03"}, "faiss"),
    QueryGroundTruth("임베딩 모델은 어떻게 동작하나요?", {"d06", "d07"}, "embedding"),
    QueryGroundTruth("코사인 유사도와 내적은 어떤 관계인가요?", {"d03", "d04"}, "similarity"),
    QueryGroundTruth("HNSW는 어떤 인덱스인가요?", {"d05"}, "ann"),
    QueryGroundTruth("청크 크기는 검색 품질에 어떤 영향을 주나요?", {"d08"}, "chunking"),
    QueryGroundTruth("하이브리드 검색은 왜 쓰나요?", {"d09"}, "hybrid"),
]

GENERATION_CASE = GenerationCase(
    question="FAISS는 어떤 도구인가요?",
    context="FAISS는 Facebook AI Research에서 만든 고성능 벡터 검색 라이브러리입니다. IndexFlatIP는 내적 기반의 정확한 검색을 제공합니다.",
    answer="FAISS는 대규모 벡터를 빠르게 검색하는 라이브러리이며, IndexFlatIP 같은 인덱스로 정확한 검색도 할 수 있습니다.",
)

PIPELINE_CASES = [
    PipelineCase("FAISS란 무엇인가요?", {"d02", "d03"}, "FAISS는 고성능 벡터 검색 라이브러리입니다."),
    PipelineCase("임베딩 모델은 어떻게 동작하나요?", {"d06", "d07"}, "임베딩 모델은 텍스트를 의미 벡터로 변환합니다."),
    PipelineCase("하이브리드 검색은 왜 쓰나요?", {"d09"}, "하이브리드 검색은 커버리지를 높이기 위해 키워드와 벡터 검색을 함께 사용합니다."),
]

EMBEDDING_MODELS = [
    EmbeddingCandidate("minilm", "sentence-transformers/all-MiniLM-L6-v2"),
    EmbeddingCandidate("multilingual-minilm", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"),
]

VECTOR_INDEXES = [
    VectorIndexCandidate("flat", "Flat"),
    VectorIndexCandidate("hnsw32", "HNSW32"),
    VectorIndexCandidate("ivf32_flat", "IVF32,Flat"),
]

FULL_CONFIGS = [
    BenchmarkConfig(
        name="baseline-ko",
        embedding_model="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        top_k=3,
        answer_prompt="다음 컨텍스트만 사용해 질문에 답하세요. 정보가 없으면 없다고 말하세요.\n\n컨텍스트:\n{context}\n\n질문:\n{question}",
    ),
    BenchmarkConfig(
        name="minilm-ko",
        embedding_model="sentence-transformers/all-MiniLM-L6-v2",
        top_k=3,
        answer_prompt="다음 컨텍스트만 사용해 질문에 답하세요. 정보가 없으면 없다고 말하세요.\n\n컨텍스트:\n{context}\n\n질문:\n{question}",
    ),
]
