"""Generated from book-content article."""

def build_cause_graph():
    # 노드: 원인 요소
    # 엣지: 인과관계 (A → B = A가 B를 유발)
    graph = {
        "배포": ["잘못된 timeout"],
        "잘못된 timeout": ["결제 API 지연"],
        "staging 부하 테스트 부재": ["잘못된 timeout"],
        "배포 보호 장치 부재": ["잘못된 timeout"],
        "결제 API 지연": ["고객 영향"],
    }
    return graph


def find_root_paths(graph, target="고객 영향"):
    # 타겟 노드까지 이어지는 모든 경로를 찾습니다
    def backtrack(node, path):
        if node not in graph or not graph[node]:
            return [path]
        paths = []
        for parent in graph:
            if node in graph[parent]:
                paths.extend(backtrack(parent, [parent] + path))
        return paths

    return backtrack(target, [target])


# 분석 실행
g = build_cause_graph()
paths = find_root_paths(g)
for p in paths:
    print(" → ".join(p))
