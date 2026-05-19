from common import async_memory_engine
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


async def run() -> int:
    engine = async_memory_engine()
    async with engine.connect() as conn:
        value = (await conn.execute(text("select 9"))).scalar_one()

    async with AsyncSession(engine) as session:
        check = (await session.execute(text("select 1"))).scalar_one()

    await engine.dispose()
    return int(value + check)
