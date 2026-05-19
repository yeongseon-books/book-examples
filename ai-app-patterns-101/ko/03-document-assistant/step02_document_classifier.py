from __future__ import annotations

from common import DEFAULT_MODEL, as_messages, build_client, print_section, response_text


DOCUMENTS = [
    "고객이 결제 실패 화면과 오류 시간을 함께 보내 주었습니다. 결제 게이트웨이 로그 확인이 필요합니다.",
    "다음 분기 추천 기능 실험 예산과 예상 지표를 정리한 제안서 초안입니다.",
    "신입 개발자 온보딩 문서에 로컬 실행 방법과 FAQ를 추가해 주세요.",
]


def classify_documents() -> None:
    client = build_client()
    system_prompt = "문서를 '운영 이슈', '기획 문서', '내부 가이드' 중 하나로 분류하고 이유를 한 줄로 설명하세요."

    for idx, document in enumerate(DOCUMENTS, start=1):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": document},
        ]
        response = client.chat.completions.create(model=DEFAULT_MODEL, messages=as_messages(messages), temperature=0.1)
        print_section(f"문서 {idx}")
        print(document)
        print(response_text(response.choices[0].message))


if __name__ == "__main__":
    classify_documents()
