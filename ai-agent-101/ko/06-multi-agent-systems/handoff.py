"""Generated from book-content article."""

from dataclasses import dataclass, field

@dataclass
class SharedState:
    topic: str
    research_notes: list[str] = field(default_factory=list)
    draft: str = ""
    review_comment: str = ""

def researcher(state: SharedState) -> None:
    state.research_notes = [
        f"{state.topic}은 여러 tool call을 묶어 자동화하는 구조입니다.",
        "역할 분리가 없으면 handoff 비용만 커질 수 있습니다.",
    ]

def writer(state: SharedState) -> None:
    state.draft = " ".join(state.research_notes)

def reviewer(state: SharedState) -> None:
    if "handoff" not in state.draft:
        state.review_comment = "handoff 비용 설명이 빠졌습니다."
    else:
        state.review_comment = "Pass"

state = SharedState(topic="multi-agent 시스템")
researcher(state)
writer(state)
reviewer(state)
print(state)
