"""
Step 01 — 환경변수 확인
======================================================
실행:
    python step01_check_env.py

GROQ_API_KEY 환경변수가 제대로 설정됐는지 확인합니다.
키 전체를 출력하지 않고 앞 6자리만 보여줍니다.
"""
import os


def main() -> None:
    api_key = os.environ["GROQ_API_KEY"]
    print(f"API 키를 불러왔습니다: {api_key[:6]}...")
    print("환경변수 설정 확인 완료.")


if __name__ == "__main__":
    main()
