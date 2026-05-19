"""Llm Api Production 101 - Episode 1: Retry backoff."""

import os
import time
from typing import Any, cast

from groq import APIStatusError, Groq


class TransientError(Exception):
    """Transient error."""

    pass


class PermanentError(Exception):
    """Permanent error."""

    pass


def classify_error(exc: APIStatusError) -> type[Exception]:
    """Classify error."""
    if exc.status_code in {429, 500, 502, 503, 504}:
        return TransientError
    return PermanentError


def call_with_retry(
    client: Groq,
    messages: list[dict],
    max_retries: int = 3,
    base_delay: float = 1.0,
) -> str:
    """Call with retry."""
    last_exc: Exception | None = None

    for attempt in range(max_retries + 1):
        try:
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=cast("Any", messages),
                temperature=0.2,
            )
            return completion.choices[0].message.content or ""
        except APIStatusError as exc:
            last_exc = exc
            error_type = classify_error(exc)
            if error_type is PermanentError:
                raise PermanentError(
                    f"Permanent error returned. status={exc.status_code}"
                ) from exc
            if attempt < max_retries:
                delay = base_delay * (2**attempt)
                print(
                    f"[retry {attempt + 1}] status={exc.status_code}, waiting {delay:.1f}s"
                )
                time.sleep(delay)
        except Exception as exc:
            last_exc = exc
            raise

    raise TransientError(f"Failed after {max_retries} retries.") from last_exc


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    result = call_with_retry(
        client,
        [{"role": "user", "content": "Explain exponential backoff in two sentences."}],
    )
    print(result)


if __name__ == "__main__":
    main()


# Expected output:
# Attempt 1: RateLimitError - retrying in 1.0s...
# Attempt 2: RateLimitError - retrying in 2.0s...
# Attempt 3: Success!
# Response received after 3 attempts.
