"""Generated from book-content article."""

from dataclasses import dataclass

@dataclass
class MathStudyPlan:
    week: int
    concept: str
    coding_task: str
    verification: str

plan = [
    MathStudyPlan(1, "논리와 함의", "조건식 동치 리팩터링", "진리표로 동치 검증"),
    MathStudyPlan(2, "집합/함수", "전처리 파이프라인 분해", "단위 테스트 + 불변식"),
    MathStudyPlan(3, "그래프", "의존성 그래프 순회", "BFS/DFS 결과 비교"),
    MathStudyPlan(4, "조합/확률", "탐색 공간 추정", "시뮬레이션과 이론값 비교"),
]

for item in plan:
    print(item)
