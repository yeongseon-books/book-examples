# Bad: sequential processing of all items
def process_items_sequential(items: List[str]) -> List[Any]:
    """Sequential processing (slow)"""
    results = []
    for item in items:
        result = process_item(item)  # 1 second each
        results.append(result)
    return results
    # 100 items = 100 seconds

# Good: parallel processing
import asyncio


async def process_items_parallel(items: List[str]) -> List[Any]:
    """Parallel processing (fast)"""
    tasks = [async_process_item(item) for item in items]
    results = await asyncio.gather(*tasks)
    return results
    # 100 items = ~1 second (parallelized network I/O)
