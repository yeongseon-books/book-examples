"""Capstone Project 101 - Episode 1: Problem card."""

from __future__ import annotations


def run() -> dict[str, str]:
    """Run."""
    return {
        "observation": "수강 신청 시 시간표 충돌이 잦다",
        "user": "신입생 + 복수 전공 학생",
        "value": "충돌을 빠르게 발견",
        "assumption": "사용자가 시간표를 텍스트로 입력 가능",
        "metric": "충돌 발견 시간 30s 이내",
    }


if __name__ == "__main__":
    print(run())
