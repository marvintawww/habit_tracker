from src.config import DATABASE_URL

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Database:
    def __init__(self, url, base):
        self.__engine = create_async_engine(url=url, echo=True)
        self.__async_session = async_sessionmaker(
            bind=self.__engine, class_=AsyncSession, expire_on_commit=False
        )
        self.__Base = base

    async def get_session(self):
        async with self.__async_session() as session:
            try:
                yield session
            finally:
                session.close()

    async def create_tables(self):
        async with self.__engine.begin() as conn:
            await conn.run_sync(self.__Base.metadata.create_all)

    async def drop_tables(self):
        async with self.__engine.begin() as conn:
            await conn.run_sync(self.__Base.metadata.drop_all)

    @property
    def engine(self):
        return self.__engine


db = Database(DATABASE_URL, Base)
