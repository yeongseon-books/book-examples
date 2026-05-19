from __future__ import annotations

from common import (
    DEFAULT_MODEL,
    as_messages,
    build_client,
    print_section,
    response_text,
)

SYSTEM_PROMPT = "You are a helpful AI tutor. Continue the conversation and answer in concise English."


def run_session_chatbot() -> None:
    client = build_client()
    sessions: dict[str, list[dict[str, str]]] = {
        "demo-user": [
            {"role": "system", "content": SYSTEM_PROMPT},
        ]
    }

    user_turns = [
        "Explain the difference between FastAPI and Flask in two sentences.",
        "Then which one is easier for a learning project?",
    ]

    for turn in user_turns:
        sessions["demo-user"].append({"role": "user", "content": turn})
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=as_messages(sessions["demo-user"]),
            temperature=0.2,
        )
        answer = response_text(response.choices[0].message)
        sessions["demo-user"].append({"role": "assistant", "content": answer})

        print_section("User turn")
        print(turn)
        print_section("Chatbot answer")
        print(answer)

    print_section("Stored message count")
    print(len(sessions["demo-user"]))


if __name__ == "__main__":
    run_session_chatbot()
