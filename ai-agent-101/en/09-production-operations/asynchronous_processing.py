"""Generated from book-content article."""

import asyncio
from asyncio import Queue


class AgentTaskQueue:
    """Async task queue."""

    def __init__(self, num_workers: int = 5):
        self.queue: Queue = Queue()
        self.num_workers = num_workers
        self.workers = []

    async def submit(self, task: dict) -> str:
        task_id = str(uuid.uuid4())
        await self.queue.put({"id": task_id, **task})
        return task_id

    async def _worker(self, worker_id: int):
        while True:
            task = await self.queue.get()
            try:
                # Real agent execution
                await process_task(task)
            except Exception as e:
                logger.error("task_failed", task_id=task["id"], error=str(e))
            finally:
                self.queue.task_done()

    async def start(self):
        for i in range(self.num_workers):
            self.workers.append(asyncio.create_task(self._worker(i)))
