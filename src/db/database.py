from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator

DATABASE_URL = "postgresql+asyncpg://postgres:root@localhost:5432/taskmanager"

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session