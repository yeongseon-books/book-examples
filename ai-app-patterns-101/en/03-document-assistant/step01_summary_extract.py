from __future__ import annotations

from common import DEFAULT_MODEL, as_messages, build_client, print_section, response_text


DOCUMENT = """
Meeting title: May checkout conversion review
Participants: Jimin, Hyunwoo, Sua
Key points:
- Mobile checkout drop-off increased by 12% compared with last month.
- Suspected causes are slow address entry, card authentication failures, and coupon confusion.
- Next week the team will run an address autocomplete experiment and inspect authentication error logs.
""".strip()


def run_document_assistant() -> None:
    client = build_client()

    summary_messages = [
        {"role": "system", "content": "Summarize the document in three English sentences."},
        {"role": "user", "content": DOCUMENT},
    ]
    summary_response = client.chat.completions.create(model=DEFAULT_MODEL, messages=as_messages(summary_messages), temperature=0.1)

    extract_messages = [
        {
            "role": "system",
            "content": "Extract only the action items as English bullet points. Include owners and deadlines when present.",
        },
        {"role": "user", "content": DOCUMENT},
    ]
    extract_response = client.chat.completions.create(model=DEFAULT_MODEL, messages=as_messages(extract_messages), temperature=0.1)

    print_section("Document summary")
    print(response_text(summary_response.choices[0].message))
    print_section("Extraction result")
    print(response_text(extract_response.choices[0].message))


if __name__ == "__main__":
    run_document_assistant()
