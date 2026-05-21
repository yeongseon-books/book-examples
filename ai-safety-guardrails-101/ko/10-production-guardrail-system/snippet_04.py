"""Generated from book-content article."""

import asyncio


async def run_pre_input(request: dict) -> list[GuardrailResult]:
    return await asyncio.gather(
        rate_limit_async(request),
        jailbreak_async(request["prompt"]),
        authz_async(request),
    )

async def run_post_output(answer: str, chunks: list[dict]) -> list[GuardrailResult]:
    return await asyncio.gather(
        moderate_async(answer),
        grounding_async(answer, chunks),
        pii_recheck_async(answer),
    )
