from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

BASE = declarative_base()


class Database:
    __engine: AsyncEngine

    async def connect(self, *, url: str):
        self.__engine = create_async_engine(url, poolclass=NullPool)
        async with self.__engine.begin() as conn:
            await conn.run_sync(BASE.metadata.create_all)

    async def disconnect(self):
        await self.__engine.dispose()

    @property
    def make_session(self) -> async_sessionmaker:
        return async_sessionmaker(self.engine, class_=AsyncSession)

    @property
    def engine(self) -> AsyncEngine:
        return self.__engine
